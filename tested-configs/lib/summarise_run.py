#!/usr/bin/env python
"""Summarise one finished payu/MOM6 run for the website.

    python summarise_run.py NAME CONTROL_DIR ARCHIVE_DIR OUT_DIR [REFERENCE_DIR]

NAME          experiment name (e.g. double_gyre)
CONTROL_DIR   payu control directory (holds config.yaml and manifests/)
ARCHIVE_DIR   payu archive directory for this experiment (holds output000/)
OUT_DIR       where to write summary.json, figure.png, ocean.stats
REFERENCE_DIR (optional) directory holding the MOM_parameter_doc.all that the
              upstream repository ships, to report which parameters changed.

Everything written here is generated: do not edit by hand.
"""
import glob
import json
import os
import re
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import xarray as xr  # noqa: E402
import yaml  # noqa: E402

name, control, archive, outdir = sys.argv[1:5]
reference = sys.argv[5] if len(sys.argv) > 5 else None
os.makedirs(outdir, exist_ok=True)
out0 = os.path.join(archive, "output000")
summary = {"name": name, "control_dir": control, "output_dir": out0}


# --- 1. Did it run? -------------------------------------------------------------
def read_text(path):
    return open(path, errors="replace").read() if os.path.exists(path) else ""


# The energy/statistics file is "ocean.stats" unless ENERGYFILE says otherwise
# (e.g. MESO_025_23L uses "timestats").
m = re.search(r'^ENERGYFILE\s*=\s*"([^"]+)"',
              read_text(os.path.join(out0, "MOM_parameter_doc.all")), flags=re.M)
STATS = m.group(1) if m else "ocean.stats"
summary["stats_file"] = STATS
stats_txt = read_text(os.path.join(out0, STATS))
stats_lines = [l for l in stats_txt.splitlines() if l.strip()]
summary["ocean_stats_tail"] = stats_lines[-4:]
summary["ok"] = len(stats_lines) > 2 and "NaN" not in stats_txt
if stats_txt:
    open(os.path.join(outdir, "ocean.stats"), "w").write(stats_txt)
if not summary["ok"]:
    # payu leaves a failed run in the work directory: keep the end of its logs
    # payu moves the logs of a failed model run to archive/error_logs/mom6.<jobid>.err;
    # a run that died later (e.g. while archiving) leaves them in the work directory.
    work = os.path.join(os.path.dirname(os.path.dirname(archive)), "work", name)
    for log in ["mom6.err", "mom6.out"]:
        stem = log.split(".")[0] + ".*." + log.split(".")[1]
        candidates = sorted(glob.glob(os.path.join(archive, "error_logs", stem)), key=os.path.getmtime)
        txt = (read_text(candidates[-1]) if candidates else "") or \
            read_text(os.path.join(work, log)) or read_text(os.path.join(out0, log))
        fatal = [l for l in txt.splitlines() if "FATAL" in l or "ERROR" in l]
        if txt:
            summary["failure_log"] = (fatal[:5] + ["..."] if fatal else []) + txt.splitlines()[-25:]
            break
    if "failure_log" not in summary:
        summary["failure_log"] = ["no output and no log found: the job probably never started "
                                  "(check the payu submission log)"]

# --- 2. What was run? (payu manifests hold the exe + input md5 hashes) --------
def load_manifest(fname):
    path = os.path.join(control, "manifests", fname)
    if not os.path.exists(path):
        return {}
    docs = list(yaml.safe_load_all(open(path)))
    entries = docs[-1] or {}
    return {k.replace("work/", ""): {"fullpath": v.get("fullpath"),
                                      "md5": v.get("hashes", {}).get("md5")}
            for k, v in entries.items()}


summary["exe"] = load_manifest("exe.yaml")
summary["inputs"] = load_manifest("input.yaml")
summary["config_yaml"] = read_text(os.path.join(control, "config.yaml"))

# --- 2b. Run-time environment recorded by payu (output000/env.yaml) ------------
ENV_KEYS = ("PAYU_TELEMETRY_ENV_VERSION", "LOADEDMODULES", "LD_LIBRARY_PATH", "PBS_QUEUE",
            "PBS_NCPUS", "PBS_NCI_NCPUS_PER_NODE", "OMPI_MCA_", "UCX_", "FI_", "I_MPI_")
env_path = os.path.join(out0, "env.yaml")
if os.path.exists(env_path):
    env = yaml.safe_load(open(env_path)) or {}
    summary["env"] = {k: str(v) for k, v in sorted(env.items())
                      if any(k == key or (key.endswith("_") and k.startswith(key)) for key in ENV_KEYS)}

# --- 3. PBS resource usage (from the model job's .o file) ---------------------
pbs_logs = sorted(glob.glob(os.path.join(archive, "pbs_logs", "*.o*")) +
                  glob.glob(os.path.join(control, "*.o[0-9]*")), key=os.path.getmtime)
if pbs_logs:
    log = read_text(pbs_logs[-1])
    usage = {}
    for key in ["Job Id", "Exit Status", "Service Units", "NCPUs Requested",
                "Walltime Used", "Memory Used"]:
        m = re.search(re.escape(key) + r":\s+([^\s]+)", log)
        if m:
            usage[key] = m.group(1)
    summary["pbs"] = usage
    summary["pbs_log"] = os.path.basename(pbs_logs[-1])

# --- 4. Parameters changed relative to the upstream MOM_parameter_doc.all ------
def params(path):
    """Return {PARAM: value-string} from a MOM_parameter_doc file."""
    out = {}
    for line in read_text(path).splitlines():
        m = re.match(r"^([A-Z][A-Z0-9_]*)\s*=\s*(.*?)\s*(!.*)?$", line)
        if m:
            out[m.group(1)] = m.group(2)
    return out


new_doc = os.path.join(out0, "MOM_parameter_doc.all")
if not os.path.exists(new_doc):          # payu may have moved it to control/docs
    new_doc = os.path.join(control, "docs", "MOM_parameter_doc.all")
KEY_PARAMS = ["NIGLOBAL", "NJGLOBAL", "NK", "GRID_CONFIG", "TOPO_CONFIG", "REENTRANT_X",
              "REENTRANT_Y", "USE_REGRIDDING", "REGRIDDING_COORDINATE_MODE", "BOUSSINESQ",
              "ENABLE_THERMODYNAMICS", "EQN_OF_STATE", "THICKNESS_CONFIG", "TS_CONFIG",
              "WIND_CONFIG", "BUOY_CONFIG", "ICE_SHELF", "DT", "DT_THERM", "DAYMAX", "TIMEUNIT"]
all_params = params(new_doc)
summary["key_params"] = {k: all_params[k] for k in KEY_PARAMS if k in all_params}
if reference and os.path.exists(os.path.join(reference, "MOM_parameter_doc.all")):
    ref, new = params(os.path.join(reference, "MOM_parameter_doc.all")), params(new_doc)
    summary["param_changes"] = {
        "added": sorted(set(new) - set(ref)),
        "removed": sorted(set(ref) - set(new)),
        "changed": {k: [ref[k], new[k]] for k in sorted(set(ref) & set(new)) if ref[k] != new[k]},
    }

# --- 5. Output files ------------------------------------------------------------
ncfiles = sorted(glob.glob(os.path.join(out0, "*.nc")))
summary["output_files"] = {os.path.basename(f): os.path.getsize(f) for f in ncfiles}

# --- 6. A picture ---------------------------------------------------------------
# Left panel: a field at the last output time (free surface if present, else
# temperature, else layer thickness; or what plots.yaml asks for).
# Right panel: total energy from ocean.stats.nc (or a second plots.yaml panel).
PREFERRED = ["SSH", "ssh", "zos", "e", "SST", "sst", "temp", "tos", "salt", "h", "u"]
SKIP = ("ocean_geometry", "Vertical_coordinate", STATS, "MOM_IC", "_IC.nc", "static")
ZDIMS = ("zl", "zi", "z_l", "z_i", "Layer", "Interface")


def time_dim(da):
    """Name of the time dimension (MOM6 writes 'Time'), or None."""
    return next((d for d in da.dims if d.lower() == "time"), None)


def pick_field():
    """(file, DataArray) holding one of PREFERRED with a time dimension. Files are
    searched newest first, so multi-year runs (prog__0010_001.nc, ...) show the end."""
    for var in PREFERRED:
        for f in reversed(ncfiles):
            if any(s in os.path.basename(f) for s in SKIP):
                continue
            try:
                ds = xr.open_dataset(f, decode_times=False)
            except Exception:
                continue
            if var in ds and time_dim(ds[var]) and varies(ds[var]):
                return f, ds[var]
    return None, None


def varies(da):
    """True if the last time of `da` has valid data that is not spatially uniform."""
    last = da.isel({time_dim(da): -1})
    last = last.where(abs(last) < 1e15)          # fill values (1e20, 1e37, ...) -> NaN
    return bool(last.notnull().any()) and float(last.std()) > 0


def field_panel(ax, f, da, kind=None, level=0, cmap=None):
    """Plot the last time of `da` as a map, a vertical section or a time-depth plot."""
    tdim = time_dim(da)
    zdim = [d for d in da.dims if d in ZDIMS]
    xdim = [d for d in da.dims if d.startswith("x")]
    ydim = [d for d in da.dims if d.startswith("y")]
    nx = da.sizes[xdim[0]] if xdim else 1
    ny = da.sizes[ydim[0]] if ydim else 1
    # mask fill values (some files use 1e20 or larger instead of NaN for land)
    da = da.where(abs(da) < 1e15)
    last = da.isel({tdim: -1})
    if kind is None:                       # choose from the shape of the domain
        thin = min(nx, ny) <= 8           # quasi-2-D channel, e.g. 64 x 4 points
        kind = "section" if (thin and max(nx, ny) > 3 and zdim) else \
               "map" if (nx > 3 and ny > 3) else "column" if zdim else "series"
    if cmap is None:
        cmap = "RdBu_r" if da.name in ("e", "SSH", "ssh", "zos", "u", "v") else "viridis"
    if kind == "map":
        if zdim:
            last = last.isel({zdim[0]: level})
        last.plot(ax=ax, cmap=cmap)
        if da.name == "e" and level == 0:
            note = "sea-surface height (`e`, top interface) at the last output time"
        else:
            note = f"`{da.name}` (level {level}) at the last output time" if zdim else \
                   f"`{da.name}` at the last output time"
    elif kind == "section":                # slice through the middle of the shorter axis
        along, across = (xdim[0], ydim[0]) if nx >= ny else (ydim[0], xdim[0])
        sec = last.isel({across: last.sizes[across] // 2})
        sec.transpose(zdim[0], along).plot(ax=ax, yincrease=False, cmap=cmap)
        note = f"`{da.name}` vertical section (model levels) at the last output time"
    elif kind == "column":
        col = da.isel({d: 0 for d in xdim + ydim})
        col.transpose(zdim[0], tdim).plot(ax=ax, yincrease=False, cmap=cmap)
        note = f"`{da.name}` time-depth evolution"
    else:
        da.isel({d: 0 for d in xdim + ydim}).plot(ax=ax)
        note = f"`{da.name}` time series"
    ax.set_title(f"{os.path.basename(f)}: {da.name}", fontsize=9)
    return note


def energy_panel(ax):
    st = os.path.join(out0, STATS + ".nc")
    s = xr.open_dataset(st, decode_times=False)
    s["En"].plot(ax=ax, marker=".")
    ax.set_title(f"{STATS}.nc: En", fontsize=9)
    return f"total energy (`En`) from `{STATS}.nc`"


plots_yaml = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "plots.yaml")
custom = (yaml.safe_load(open(plots_yaml)) or {}).get(name, [])
old_fig = os.path.join(outdir, "figure.png")
if not summary["ok"] and os.path.exists(old_fig):
    os.remove(old_fig)                       # don't keep a figure from an earlier run
try:
    if not summary["ok"]:
        raise RuntimeError("run failed: no figure")
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    notes = []
    for i, ax in enumerate(axes):
        if i < len(custom):                                   # panel chosen in plots.yaml
            spec = custom[i]
            f = sorted(glob.glob(os.path.join(out0, spec["file"])))[-1]   # newest file
            da = xr.open_dataset(f, decode_times=False)[spec["var"]]
            notes.append(field_panel(ax, f, da, spec.get("kind"), spec.get("level", 0), spec.get("cmap")))
        elif i == 0:                                          # automatic choice
            f, da = pick_field()
            if da is not None:
                ds = xr.open_dataset(f, decode_times=False)
                ny = min(n for d, n in da.sizes.items() if d.startswith(("x", "y")))
                if ny <= 8:                                # sections: a tracer is clearer
                    for v in ("temp", "salt"):
                        if v in ds and time_dim(ds[v]) and varies(ds[v]):
                            da = ds[v]
                            break
            notes.append(field_panel(ax, f, da) if da is not None else "no suitable diagnostic")
        elif os.path.exists(os.path.join(out0, STATS + ".nc")):
            notes.append(energy_panel(ax))
    fig.suptitle(f"MOM6 run: {name}", fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "figure.png"), dpi=90)
    summary["figure"] = "figure.png"
    summary["figure_note"] = "Left: " + notes[0] + ("; right: " + notes[1] if len(notes) > 1 else "")
except Exception as err:  # a failed plot should not hide a successful run
    summary["figure_error"] = repr(err)


json.dump(summary, open(os.path.join(outdir, "summary.json"), "w"), indent=1, default=str)
print(name, "ok" if summary["ok"] else "FAILED")
