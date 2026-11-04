#!/usr/bin/env python
"""Write the website pages for the tested MOM6-examples from results/*/summary.json.

    python lib/make_pages.py            (run from anywhere; paths are relative to this file)

Writes (all generated, do not edit by hand):
  documentation/docs/pages/configurations/how-they-were-run.md    how every configuration was run
  documentation/docs/pages/configurations/mom6examples.md         stub pointing there (keeps old URL)
  tested-configs/results/<name>/status.md                         status banner (top of each page)
  tested-configs/results/status-summary.md                        one sentence: how many ran (Overview)
  tested-configs/results/table-community.md                       the two tables at the top of the
  tested-configs/results/table-mom6examples.md                    Configurations page (Overview.md);
                                                                  tags become filter buttons
  documentation/docs/pages/configurations/mom6examples/<name>.md  one page per example
  documentation/docs/assets/tested-configs/<name>.png             figures
and replaces the block between the "generated mom6examples nav" markers in
documentation/mkdocs.yml.
"""
import json
import os
import re
import shutil

import yaml

import param_diff   # lib/param_diff.py: parameter comparison (same method as access-om3-live)

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))     # tested-configs/
REPO = os.path.dirname(HERE)
DOCS = os.path.join(REPO, "documentation", "docs")
PAGES = os.path.join(DOCS, "pages", "configurations", "mom6examples")
ASSETS = os.path.join(DOCS, "assets", "tested-configs")
MKDOCS = os.path.join(REPO, "documentation", "mkdocs.yml")
UPSTREAM = "https://github.com/NOAA-GFDL/MOM6-examples"


def read_env(path):
    """Read KEY=value lines (ignoring comments) from versions.env."""
    env = {}
    for line in open(path):
        m = re.match(r"^\s*([A-Z0-9_]+)=(\S+)", line)
        if m:
            env[m.group(1)] = m.group(2)
    return env


versions = read_env(os.path.join(HERE, "versions.env"))
environment = json.load(open(os.path.join(HERE, "results", "environment.json")))
known_issues = yaml.safe_load(open(os.path.join(HERE, "known_issues.yaml"))) or {}


def gfdl_excluded():
    """Patterns GFDL excludes from `make test` (EXCLUDE in ocean_only/Makefile)."""
    mk = os.path.join(environment.get("work_root", ""), "MOM6-examples", "ocean_only", "Makefile")
    if not os.path.exists(mk):
        return []
    m = re.search(r"^EXCLUDE \?= \\\n((?:\s+\S+ ?\\?\n)+)", open(mk).read(), flags=re.M)
    return [t for t in re.split(r"[\s\\]+", m.group(1)) if t] if m else []


EXCLUDED = gfdl_excluded()


def is_excluded(example):
    """True if ocean_only/<example> matches one of GFDL's EXCLUDE patterns (% = wildcard)."""
    rel = example.replace("ocean_only/", "")
    return any(re.fullmatch(pat.replace("%", ".*"), rel) for pat in EXCLUDED)
commit = versions["MOM6_EXAMPLES_COMMIT"]

examples = []
section = "Examples"
for line in open(os.path.join(HERE, "examples.txt")):
    m = re.match(r"^# --- (.*?) ---\s*$", line)
    if m:
        section = m.group(1)
    if line.strip() and not line.lstrip().startswith("#"):
        example, ncpus, walltime, *variant = line.split()
        name = example.replace("ocean_only/", "").replace("/", "-")
        base = name
        if variant:                                    # e.g. ["10yr", "DAYMAX=3650.0"]
            name = f"{name}-{variant[0]}"
        examples.append(dict(example=example, name=name, base=base, ncpus=ncpus,
                             walltime=walltime, variant=variant, section=section))


def setup_line(s):
    """Set-up summary read from the run's own MOM_parameter_doc.all (summary.json key_params),
    so it is correct by construction. Empty if none were recorded (failed runs)."""
    k = (s or {}).get("key_params") or {}
    if not k:
        return ""
    v = lambda p: k.get(p, "").strip('"')
    parts = [f"{v('NIGLOBAL')} x {v('NJGLOBAL')} x {v('NK')} {v('GRID_CONFIG')} grid"]
    parts.append(f"`{v('REGRIDDING_COORDINATE_MODE')}` coordinate" if v("USE_REGRIDDING") == "True"
                 else "layer mode (no regridding)")
    parts.append(f"topography `{v('TOPO_CONFIG')}`")
    if v("WIND_CONFIG"):
        parts.append(f"wind `{v('WIND_CONFIG')}`")
    if v("BUOY_CONFIG"):
        parts.append(f"buoyancy `{v('BUOY_CONFIG')}`")
    if v("ICE_SHELF") == "True":
        parts.append("ice shelf")
    try:
        parts.append(f"{float(v('DAYMAX')) * float(v('TIMEUNIT')) / 86400:g} days")
    except ValueError:
        pass
    return ", ".join(parts)


def setup_points(s):
    """The same set-up facts as setup_line(), one per dot point (for the configuration page)."""
    k = (s or {}).get("key_params") or {}
    if not k:
        return ["- Set-up not recorded (this run failed)"]
    v = lambda p: k.get(p, "").strip('"')
    pts = [f"- **Grid:** {v('NIGLOBAL')} x {v('NJGLOBAL')} points, {v('NK')} layers/levels "
           f"(`GRID_CONFIG = {v('GRID_CONFIG')}`)",
           "- **Vertical coordinate:** " + (f"`{v('REGRIDDING_COORDINATE_MODE')}`" if v("USE_REGRIDDING") == "True"
                                            else "layer mode (no regridding)"),
           f"- **Topography:** `TOPO_CONFIG = {v('TOPO_CONFIG')}`"]
    forcing = []
    if v("WIND_CONFIG"):
        forcing.append(f"`WIND_CONFIG = {v('WIND_CONFIG')}`")
    if v("BUOY_CONFIG"):
        forcing.append(f"`BUOY_CONFIG = {v('BUOY_CONFIG')}`")
    if forcing:
        pts.append("- **Surface forcing:** " + ", ".join(forcing))
    if v("ICE_SHELF") == "True":
        pts.append("- **Ice shelf:** yes")
    try:
        pts.append(f"- **Run length:** {float(v('DAYMAX')) * float(v('TIMEUNIT')) / 86400:g} days")
    except ValueError:
        pass
    return pts


def description_box(name, ex, s):
    """Admonition with the same description as the Overview table, as dot points, plus sources."""
    lines = ['!!! abstract "Description (as on the Overview)"']
    if ex["variant"]:
        changes = ", ".join(f"`{c}`" for c in ex["variant"][1].split(","))
        lines += [f"    Variant of [`{ex['base']}`]({ex['base']}.md) with {changes}.", ""]
    lines += ["    " + p for p in setup_points(s)]
    lines += ["", f"    Read from this run's `MOM_parameter_doc.all`. Source: {upstream_links(ex)}."]
    return lines


def upstream_links(ex):
    """Link to the example's directory upstream, and to its README if it (or a parent) has one."""
    links = [f"[upstream]({UPSTREAM}/tree/{commit}/{ex['example']})"]
    path = ex["example"]
    while path.count("/") >= 1:
        for readme in ("README.md", "README"):
            if os.path.exists(os.path.join(environment.get("work_root", ""), "MOM6-examples", path, readme)):
                links.append(f"[README]({UPSTREAM}/blob/{commit}/{path}/{readme})")
                break
        else:
            path = os.path.dirname(path)
            continue
        break
    return ", ".join(links)


def describe(name, ex):
    """Description shown in the table and at the top of each example page."""
    s = load_summary(name)
    text = setup_line(s) or "Set-up not recorded (this run failed)"
    if ex["variant"]:
        changes = ", ".join(f"`{c}`" for c in ex["variant"][1].split(","))
        text = f"Variant of `{ex['base']}` with {changes}. " + text
    return f"{text} ({upstream_links(ex)})"


# Short tags for the filter buttons on the Configurations page, one per examples.txt section.
SECTION_TAGS = {"Basins and channels": "Basin", "Vertical-coordinate tests": "Coordinates",
                "Ice-shelf cavity": "Ice shelf", "Hurricanes and single columns": "Column",
                "Realistic": "Realistic"}


def section_tag(section):
    return next((tag for key, tag in SECTION_TAGS.items() if section.startswith(key)), section)


def input_source(fullpath):
    """Short description of where an input file lives (instead of the full test-area path)."""
    real = os.path.realpath(fullpath)
    datasets = os.path.realpath(versions["DATASETS"])
    work_root = environment.get("work_root", "")
    if real.startswith(datasets + "/"):
        return f"`ol01` data: `{os.path.relpath(real, datasets)}`"
    if work_root and real.startswith(os.path.join(work_root, "MOM6-examples") + "/"):
        return f"MOM6-examples: `{os.path.relpath(real, os.path.join(work_root, 'MOM6-examples'))}`"
    if work_root and real.startswith(work_root + "/"):
        return f"`{os.path.relpath(real, work_root)}`"
    return f"`{real}`"


def needs_ol01(s):
    """True if any input file of the run resolves into /g/data/ol01 (GFDL's input data)."""
    return any("/ol01/" in os.path.realpath(v.get("fullpath", ""))
               for v in ((s or {}).get("inputs") or {}).values())


def prerequisites(name, s):
    """NCI projects and special input steps, for the Prerequisites column."""
    items = ["`vk83`"]
    if needs_ol01(s):
        items.append("`ol01` (GFDL input data)")
    if "Unable to open" in known_issues.get(name, "") or "Unable to open" in str(known_issues.get(name.split("-")[0], "")):
        items.append("**missing input files** (see page)")
    return ", ".join(items)


def load_summary(name):
    path = os.path.join(HERE, "results", name, "summary.json")
    return json.load(open(path)) if os.path.exists(path) else None


def indent(text, n=4):
    return "\n".join((" " * n + l) if l.strip() else "" for l in text.splitlines())


def status_badge(s):
    if s is None:
        return "not run"
    return ":white_check_mark: ran" if s["ok"] else ":x: failed"


# ---------------------------------------------------------------------------------
NOTEBOOK_URL = ("https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/blob/main/"
                "tested-configs/notebooks/explore_run.ipynb")


NOTEBOOK_PAGES = os.path.join(DOCS, "pages", "configurations", "notebooks")
SUMMARISE_URL = ("https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/blob/main/"
                 "tested-configs/lib/summarise_run.py")


def notebook_section(name, assets, nb_link, level=2):
    """The rendered explore_run notebook for this run (results/<name>/notebook.md, written by
    lib/run_notebooks.sh), with its headings put `level` deep and figure paths made relative.
    nb_link: relative link from the page to this run's full notebook page (with the code)."""
    path = os.path.join(HERE, "results", name, "notebook.md")
    if not os.path.exists(path):
        return []
    body = open(path).read().replace("@ASSETS@", assets).strip().splitlines()
    body = [("#" * level) + l[1:] if l.startswith("## ") else l for l in body]
    return ["#" * level + " Domain, forcing and output", "",
            f"Made by running the notebook [`explore_run.ipynb`]({NOTEBOOK_URL}) on this run's "
            f"output folder; it only plots files MOM6 wrote during the run. "
            f"**[See the notebook with its code]({nb_link})**.", ""] + body + [""]


def write_notebook_page(name, back_link, back_title):
    """pages/configurations/notebooks/<name>.md: the executed notebook with its code
    (results/<name>/notebook_full.md, written by lib/run_notebooks.sh)."""
    path = os.path.join(HERE, "results", name, "notebook_full.md")
    if not os.path.exists(path):
        return
    os.makedirs(NOTEBOOK_PAGES, exist_ok=True)
    body = open(path).read().replace("@ASSETS@", "../../../assets").strip().splitlines()
    body = [("#" + l) if l.startswith("#") else l for l in body]      # page has its own title
    head = [f"# {back_title}: notebook", "",
            f"The notebook [`explore_run.ipynb`]({NOTEBOOK_URL}) as it ran on the output folder of "
            f"the tested run, with its code and output. It made the figures in the \"Domain, forcing "
            f"and output\" section of [{back_title}]({back_link}); the \"What we got\" figure on that "
            f"page is made by [`lib/summarise_run.py`]({SUMMARISE_URL}).", ""]
    open(os.path.join(NOTEBOOK_PAGES, name + ".md"), "w").write("\n".join(head + body) + "\n")


def status_banner(name, s):
    """Admonition at the top of a configuration's page saying whether its tested run worked."""
    if s is None:
        return '!!! warning "Run status: :grey_question: not tested yet"\n    No test run has been recorded for this configuration.\n'
    if s["ok"]:
        pbs = s.get("pbs", {})
        return (f'!!! success "Run status: :white_check_mark: ran successfully"\n'
                f"    Tested on {environment['date']} with `{versions['ACCESS_OM3_MODULE']}` (`mom6-solo`): "
                f"{pbs.get('NCPUs Requested', '?')} cores, walltime used {pbs.get('Walltime Used', '?')}, "
                f"{pbs.get('Service Units', '?')} SU. Details further down this page.\n")
    issue = known_issues.get(name, "")
    reason = (issue.split(". ")[0].rstrip(".") + ".") if issue else "See the error log further down this page."
    return (f'!!! failure "Run status: :x: did not run"\n'
            f"    Tested on {environment['date']} with `{versions['ACCESS_OM3_MODULE']}`. {reason}\n")


def example_page(ex, s):
    name, example = ex["name"], ex["example"]
    lines = [f"# {name.replace('-', ' / ')}", ""]
    lines += [status_banner(name, s), ""]
    lines += description_box(name, ex, s) + [""]
    if ex["variant"]:
        lines += [f"This is a copy of [{ex['base']}]({ex['base']}.md) with these lines added to "
                  "`MOM_override`, e.g. to run long enough to see a spun-up state:", "", "```text"]
        lines += [f"#override {c.replace('=', ' = ')}" for c in ex["variant"][1].split(",")]
        lines += ["```", ""]
    lines += [f"Configuration files: [`{example}`]({UPSTREAM}/tree/{commit}/{example}) in "
              f"NOAA-GFDL/MOM6-examples, at commit [`{commit[:8]}`]({UPSTREAM}/commit/{commit}): the version "
              "this run used. (The model itself is the `mom6-solo` listed under Provenance.)", ""]
    if is_excluded(example):
        lines += ["GFDL excludes this example from its own automated test suite (`EXCLUDE` in "
                  f"[`ocean_only/Makefile`]({UPSTREAM}/blob/{commit}/ocean_only/Makefile)).", ""]
    if name in known_issues:
        kind = "failure" if (s is not None and not s["ok"]) else "warning"
        lines += [f'!!! {kind} "Known issue"', indent(" ".join(known_issues[name].split())), ""]
    if s is not None and "userscripts:" in s.get("config_yaml", ""):
        lines += ['!!! info "Workaround in the payu set-up (the MOM6-examples files are unchanged)"',
                  indent(" ".join(known_issues["_restart_control"].split())), ""]

    # (whether it ran is the status banner at the top of the page; how pages are made is on the Overview)

    lines += ["## Run it yourself", "",
              "From a Gadi **login node** (membership of NCI project `vk83` needed"
              + (", and `ol01` for the input data" if needs_ol01(s) else "") + "):", "",
              "```bash",
              f"PROJECT=<your-project> bash {name}.sh",
              "```", "",
              f"where `{name}.sh` is the script below (click to expand; copy button top-right). "
              "It is exactly the script that produced the results on this page.", "",
              f'??? example "{name}.sh"',
              "    ```bash",
              f'    --8<-- "tested-configs/run_scripts/{name}.sh"',
              "    ```", ""]

    if s is None:
        return "\n".join(lines)
    upstream_rows = [f"| MOM6-examples | [`{commit}`]({UPSTREAM}/commit/{commit}) |"]
    return "\n".join(lines + results_section(name, s, "../../../assets", upstream_rows,
                                              "the upstream MOM_parameter_doc.all", ex=ex))


def figure_lines(name, s, assets):
    """The run's summary figure with its caption (empty if there is none)."""
    if not s.get("figure"):
        return []
    return [f"![{name}]({assets}/tested-configs/{name}.png)", "", f"*{s.get('figure_note', '')}.*", ""]


# Files MOM6 writes itself (not set by diag_table), described for the "Output files" table.
FIXED_OUTPUT = {
    "ocean_geometry.nc": "Static grid: coordinates, cell sizes and areas, bottom depth `D`, Coriolis parameter, land mask",
    "Vertical_coordinate.nc": "The vertical coordinate: target values of the layers or levels",
    "ocean.stats.nc": "Domain totals at each energy-save time (energy, mass, heat, salt, maximum CFL); "
                      "the netCDF form of `ocean.stats`",
    "timestats.nc": "Domain totals at each energy-save time (energy, mass, maximum CFL); the netCDF "
                    "form of the energy file",
    "Depth_list.nc": "Ocean area and volume as a function of depth, used for the energy diagnostics",
    "MOM_IC.nc": "Initial state written by MOM6 at the start of the run",
    "GOLD_IC.nc": "Initial state written by MOM6 at the start of the run",
    "Initial_state.nc": "Initial state written by MOM6 at the start of the run",
}


def _csv(line):
    """Split one diag_table line on commas outside quotes; strip quotes and spaces."""
    return [x.strip().strip('"').strip("'") for x in re.findall(r'(?:"[^"]*"|[^,])+', line)]


def diag_table_files(run_dir):
    """{file name prefix: {"freq": str, "fields": [(field, averaged)]}} from the run's diag_table."""
    path = os.path.join(run_dir or "", "diag_table")
    files = {}
    if not os.path.exists(path):
        return files
    for line in open(path).read().splitlines()[2:]:
        line = line.split("#")[0].strip()
        if not line:
            continue
        parts = _csv(line)
        if len(parts) >= 6 and re.fullmatch(r"-?\d+", parts[1]):          # a file line
            base = parts[0].split("%")[0].rstrip("_")
            freq = "written once (static)" if int(parts[1]) < 0 else f"every {parts[1]} {parts[2]}"
            files.setdefault(base, {"freq": freq, "fields": []})["freq"] = freq
        elif len(parts) >= 6:                                               # a field line
            base = parts[3].split("%")[0].rstrip("_")
            avg = parts[5].lower() in (".true.", "true", "average", "mean")
            files.setdefault(base, {"freq": "", "fields": []})["fields"].append((parts[2], avg))
    return files


def output_description(fname, files):
    if fname in FIXED_OUTPUT:
        return FIXED_OUTPUT[fname]
    stem = fname[:-3] if fname.endswith(".nc") else fname
    base = max((b for b in files if stem == b or stem.startswith(b + "_")), key=len, default=None)
    if base is None:
        return ""
    info = files[base]
    names = [f for f, _ in info["fields"]]
    kinds = {avg for _, avg in info["fields"]}
    kind = "time averages" if kinds == {True} else "snapshots" if kinds == {False} else "snapshots and averages"
    shown = ", ".join(f"`{n}`" for n in names[:8]) + (f" and {len(names) - 8} more" if len(names) > 8 else "")
    return f"Diagnostics set in `diag_table`: {kind} of {shown}, {info['freq']}" if names else \
           f"Diagnostics set in `diag_table`, {info['freq']}"


def results_section(name, s, assets, config_rows, reference_label, show_figure=True, nb_prefix="../notebooks/",
                    ex=None):
    """Markdown lines for "What we got", the notebook section (if any) and "Provenance" of one run.
    assets: path from the page to docs/assets; config_rows: table rows naming the config source;
    show_figure=False when the page shows the figure higher up (community pages)."""
    lines = []
    notebook = notebook_section(name, assets, f"{nb_prefix}{name}.md")
    if not s["ok"] and s.get("failure_log"):
        lines += ['??? failure "End of the error log"', "    ```text",
                  indent("\n".join(s["failure_log"])), "    ```", ""]
    lines += ["## What we got", ""]
    if show_figure:
        lines += figure_lines(name, s, assets)
    if s.get("ocean_stats_tail"):
        lines += [f"Last lines of `{s.get('stats_file', 'ocean.stats')}`:", "", "```text"] + s["ocean_stats_tail"] + ["```", ""]
    if s.get("key_params") and not notebook:          # the notebook shows the same table
        lines += ["Key parameters of this run (from `MOM_parameter_doc.all`):", "",
                  "| Parameter | Value |", "|---|---|"]
        lines += [f"| `{k}` | `{v}` |" for k, v in s["key_params"].items()]
        lines += [""]

    lines += notebook
    lines += param_section(name, s, ex)

    # ---- provenance --------------------------------------------------------------
    lines += ["## Provenance", "",
              "| What | Value |", "|---|---|"] + config_rows + [
              f"| ACCESS-OM3 module | `{versions['ACCESS_OM3_MODULE']}` |",
              f"| MOM6 source code | `{environment.get('mom6_source', '?')}` |"]
    for exe, info in s.get("exe", {}).items():
        lines += [f"| Executable | `{info['fullpath']}` |", f"| Executable md5 | `{info['md5']}` |"]
    payu = s.get("env", {}).get("PAYU_TELEMETRY_ENV_VERSION", versions["PAYU_MODULE"])
    lines += [f"| payu | `{payu}` (module `{versions['PAYU_MODULE']}`) |",
              f"| Date tested | {environment['date']} |"]
    for k, v in s.get("pbs", {}).items():
        lines += [f"| PBS {k} | `{v}` |"]
    lines += [""]

    if s.get("inputs"):
        lines += ['??? info "Input files and md5 hashes (from payu `manifests/input.yaml`)"',
                  "    | File | md5 | Comes from |", "    |---|---|---|"]
        lines += [f"    | `{k}` | `{v['md5']}` | {input_source(v['fullpath'])} |"
                  for k, v in sorted(s["inputs"].items())]
        lines += [""]
    else:
        lines += ["This example needs no input files: grid, bathymetry, initial state and "
                  "forcing are all set analytically in `MOM_input`.", ""]

    if s.get("env"):
        lines += ['??? info "Run-time environment (selected variables from payu\'s `env.yaml`)"',
                  "    | Variable | Value |", "    |---|---|"]
        lines += [f"    | `{k}` | `{v}` |" for k, v in s["env"].items()]
        lines += [""]
    lines += ['??? info "payu config.yaml written by the script"', "    ```yaml",
              indent(s.get("config_yaml", "").rstrip()), "    ```", ""]
    if s.get("output_files"):
        files = diag_table_files(s.get("output_dir"))
        lines += ['??? info "Output files"', "    | File | Size | What it is |", "    |---|---|---|"]
        lines += [f"    | `{f}` | {sz/1e6:.2f} MB | {output_description(f, files)} |"
                  for f, sz in s["output_files"].items()]
        lines += [""]
    return lines


# ---- fragments for the hand-written pages of stand-alone configurations ---------------
# Reference MOM_parameter_doc.all for the COSIMA configurations: (local path, GitHub URL, label, Gadi run path)
COMMUNITY_REF = {
    "anu-tub-zstar": ("anu-tub/docs/MOM_parameter_doc.all",
                      "https://github.com/ACCESS-Community-Hub/anu-tub/blob/e413708c4b1446e267b42f2f0da95d6ab48ae0e0/docs/MOM_parameter_doc.all",
                      "the file committed in anu-tub (`e413708c`)",
                      "/scratch/<your-project>/$USER/mom6/archive/anu-tub-zstar/output000/MOM_parameter_doc.all"),
    "isomip-plus-ocean0": ("isomip-plus/input-repo/docs/MOM_parameter_doc.all",
                           "https://github.com/claireyung/isomip-test-mom6-for-iom3-configs/blob/3b86dc0bcb4b7a38156bdb3b94952fe47bb51887/docs/MOM_parameter_doc.all",
                           "Claire Yung's own run (`3b86dc0b`)",
                           "/scratch/<your-project>/$USER/mom6/archive/isomip-plus-ocean0/output000/MOM_parameter_doc.all"),
}


def param_section(name, s, ex=None, level=2):
    """The "Parameters compared with the reference" section (lib/param_diff.py), or nothing."""
    run_file = os.path.join(s.get("output_dir") or "", "MOM_parameter_doc.all")
    work_root = environment.get("work_root", "")
    if ex is not None:
        ref_file = os.path.join(work_root, "MOM6-examples", ex["example"], "MOM_parameter_doc.all")
        ref_url = f"{UPSTREAM}/blob/{commit}/{ex['example']}/MOM_parameter_doc.all"
        label = f"GFDL's file in MOM6-examples (`{commit[:8]}`)"
        gadi = f"/scratch/<your-project>/$USER/mom6-examples/archive/{name}/output000/MOM_parameter_doc.all"
    else:
        rel, ref_url, label, gadi = COMMUNITY_REF[name]
        ref_file = os.path.join(work_root, rel)
    if not (os.path.exists(run_file) and os.path.exists(ref_file)):
        return []
    return param_diff.section(ref_file, run_file, ref_url, label, gadi, level=level)


STANDALONE = {   # run name -> (page that includes the fragment, rows describing the config source)
    "anu-tub-zstar": ["| Configuration | [ACCESS-Community-Hub/anu-tub](https://github.com/ACCESS-Community-Hub/anu-tub) "
                      "`e413708c`, `zstar` coordinate |"],
    "isomip-plus-ocean0": ["| Configuration | [mom6-idealised-configs branch `isomip-plus-ocean0-sigmashelfzstar`]"
                           "(https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/"
                           "isomip-plus-ocean0-sigmashelfzstar) `094d9177` |",
                           "| Input file | [claireyung/isomip-test-mom6-for-iom3-configs]"
                           "(https://github.com/claireyung/isomip-test-mom6-for-iom3-configs) `3b86dc0b` |"],
}
REFERENCE_LABEL = {"anu-tub-zstar": "the `docs/MOM_parameter_doc.all` committed in anu-tub",
                   "isomip-plus-ocean0": "Claire Yung's own run (`docs/` in isomip-test-mom6-for-iom3-configs)"}


def standalone_fragment(name, s):
    pbs = s.get("pbs", {})
    if s["ok"]:
        head = ['!!! success "Tested: this configuration runs"',
                f"    Ran on Gadi on {environment['date']} with `{versions['ACCESS_OM3_MODULE']}` "
                f"(`mom6-solo`) and `{versions['PAYU_MODULE']}`: {pbs.get('NCPUs Requested', '?')} cores, "
                f"walltime used {pbs.get('Walltime Used', '?')}, {pbs.get('Service Units', '?')} SU.", ""]
    else:
        head = ['!!! failure "Tested: this configuration did NOT run successfully"', ""]
    body = results_section(name, s, "../../assets", STANDALONE[name], REFERENCE_LABEL[name], show_figure=False,
                           nb_prefix="notebooks/")
    # demote headings one level so they sit under the page's "Tested run" section
    body = [("#" + l) if l.startswith("##") else l for l in body]
    return "\n".join(head + body)


def table_row(link, tags, status, cores, prereq, description):
    """One row of the Configurations table; tags become filter buttons (docs/js/config-filter.js)."""
    tag_html = " ".join(f'<span class="cfg-tag">{t}</span>' for t in tags)
    return f"| {link} | {tag_html} | {status} | {cores} | {prereq} | {description} |"


TABLE_HEAD = ["| Configuration | Tags | Status | Cores | Prerequisites | Description |",
              "|---|---|---|---|---|---|"]


def write_table(filename, table_rows):
    open(os.path.join(HERE, "results", filename), "w").write("\n".join(
        ['<div class="config-table" markdown>', ""] + TABLE_HEAD + table_rows + ["", "</div>", ""]))


# The COSIMA community configurations (pages written by hand, results generated).
# Descriptions are quoted from each configuration's README, which is linked.
COMMUNITY = [
    ("anu-tub-zstar", "[ANU-TUB](anu-tub.md)", ["Basin", "Coordinates"],
     "`vk83`, `xp65` (the script makes the input files with `conda/analysis3`)",
     '"A bathtub-sector ocean configuration for MOM6 ... designed primarily as a test case for '
     'implementing new vertical coordinate systems into MOM6" '
     "([README](https://github.com/ACCESS-Community-Hub/anu-tub#anu-tub)). By Andy Hogg and Angus Gibson."),
    ("isomip-plus-ocean0", "[ISOMIP+ Ocean0](isomip-plus.md)", ["Ice shelf"],
     "`vk83`; the input file comes from Claire Yung's input repository (the script clones it)",
     '"Idealised ISOMIP+ like config" that "resembles the Ocean0 warm test case" '
     "([README](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/"
     "isomip-plus-ocean0-sigmashelfzstar#readme)). By Claire Yung."),
]

# ---------------------------------------------------------------------------------
os.makedirs(PAGES, exist_ok=True)
os.makedirs(ASSETS, exist_ok=True)
rows = []
for i, ex in enumerate(examples):
    s = load_summary(ex["name"])
    asset = os.path.join(ASSETS, ex["name"] + ".png")
    if s and s.get("figure"):
        shutil.copy(os.path.join(HERE, "results", ex["name"], "figure.png"), asset)
    elif os.path.exists(asset):
        os.remove(asset)                     # generated file from an earlier run
    open(os.path.join(PAGES, ex["name"] + ".md"), "w").write(example_page(ex, s) + "\n")
    write_notebook_page(ex["name"], f"../mom6examples/{ex['name']}.md", ex["name"].replace("-", " / "))
    flag = " &dagger;" if is_excluded(ex["example"]) else ""   # see note under the table
    rows.append(table_row(f"[{ex['name']}](mom6examples/{ex['name']}.md)", [section_tag(ex["section"])],
                          f"{status_badge(s)}{flag}", ex["ncpus"], prerequisites(ex["name"], s),
                          describe(ex["name"], ex)))

for name in STANDALONE:
    s = load_summary(name)
    os.makedirs(os.path.join(HERE, "results", name), exist_ok=True)
    if s and s.get("figure"):
        shutil.copy(os.path.join(HERE, "results", name, "figure.png"),
                    os.path.join(ASSETS, name + ".png"))
    fig = figure_lines(name, s, "../../assets") if s else []
    if fig:
        days = (s.get("key_params") or {}).get("DAYMAX", "?")
        fig[-2] = fig[-2].rstrip("*").rstrip(".") + (f", from the tested {float(days):g}-day run (see "
                  "[Tested run](#tested-run)). The run is short, so this shows the model early in its "
                  "spin-up, not an equilibrated state.*")
    open(os.path.join(HERE, "results", name, "figure.md"), "w").write("\n".join(fig) + "\n")
    page = {"anu-tub-zstar": ("../anu-tub.md", "ANU-TUB"), "isomip-plus-ocean0": ("../isomip-plus.md", "ISOMIP+ Ocean0")}[name]
    write_notebook_page(name, *page)
    text = standalone_fragment(name, s) if s else '!!! warning "Not yet tested"\n    No test run has been recorded yet.'
    open(os.path.join(HERE, "results", name, "tested.md"), "w").write(text + "\n")

community_rows = []
for name, link, tags, prereq, text in COMMUNITY:
    s = load_summary(name)
    cores = (s or {}).get("pbs", {}).get("NCPUs Requested", "")
    setup = setup_line(s)
    community_rows.append(table_row(link, tags, status_badge(s), cores, prereq,
                                    text + (f" Tested set-up: {setup}." if setup else "")))
write_table("table-community.md", community_rows)
write_table("table-mom6examples.md", rows)
for name, link, tags, prereq, text in COMMUNITY:
    s = load_summary(name)
    open(os.path.join(HERE, "results", name, "status.md"), "w").write(status_banner(name, s))
    # same description as the Overview table (README quote), with the tested set-up as dot points
    box = ['!!! abstract "Description (as on the Overview)"', "    " + text, ""]
    box += ["    Tested set-up, read from this run's `MOM_parameter_doc.all`:", ""]
    box += ["    " + p for p in setup_points(s)]
    open(os.path.join(HERE, "results", name, "description.md"), "w").write("\n".join(box) + "\n")

n_comm_ok = sum(1 for name, *_ in COMMUNITY if (load_summary(name) or {}).get("ok"))
n_ex_ok = sum(1 for ex in examples if (load_summary(ex["name"]) or {}).get("ok"))
text = (f"In the last test ({environment['date']}), {n_comm_ok}/{len(COMMUNITY)} COSIMA community "
        f"configurations and {n_ex_ok}/{len(examples)} MOM6-example runs ran successfully.")
open(os.path.join(HERE, "results", "status-summary.md"), "w").write(text + "\n")

n_ok = sum(1 for ex in examples if (load_summary(ex["name"]) or {}).get("ok"))
index = open(os.path.join(HERE, "templates", "how_they_were_run.md.in")).read()
index = (index
              .replace("@N_OK@", str(n_ok)).replace("@N_TOTAL@", str(len(examples)))
              .replace("@DATE@", environment["date"])
              .replace("@COMMIT@", commit).replace("@COMMIT8@", commit[:8])
              .replace("@ACCESS_OM3_MODULE@", versions["ACCESS_OM3_MODULE"])
              .replace("@PAYU@", environment.get("payu_version", versions["PAYU_MODULE"]))
              .replace("@MOM6_SOLO@", environment.get("mom6_solo", ""))
              .replace("@MOM6_SOLO_MD5@", environment.get("mom6_solo_md5", ""))
              .replace("@ACCESS_MOM6@", environment.get("access_mom6_module", ""))
              .replace("@MOM6_SOURCE@", environment.get("mom6_source", ""))
              .replace("@WORK_ROOT@", environment.get("work_root", "?"))
              .replace("@WEBSITE_COMMIT@", environment.get("website_commit", "")))
open(os.path.join(DOCS, "pages", "configurations", "how-they-were-run.md"), "w").write(index)
# This page used to describe the MOM6 examples only; keep its URL working for old links.
open(PAGES + ".md", "w").write("# MOM6 examples\n\nThis page has moved: see "
                               "[How this website is generated](how-they-were-run.md).\n")

# ---- navigation block in mkdocs.yml ---------------------------------------------------
nav = ["        - MOM6 examples:"]
for i, ex in enumerate(examples):
    if i == 0 or ex["section"] != examples[i - 1]["section"]:
        nav.append(f"            - {ex['section']}:")
    nav.append(f"                - {ex['name']}: pages/configurations/mom6examples/{ex['name']}.md")
text = open(MKDOCS).read()
text = re.sub(r"( *# BEGIN generated mom6examples nav[^\n]*\n).*?( *# END generated mom6examples nav)",
              lambda m: m.group(1) + "\n".join(nav) + "\n" + m.group(2), text, flags=re.S)
open(MKDOCS, "w").write(text)
print(f"wrote {len(examples)} pages; {n_ok} ran successfully")
