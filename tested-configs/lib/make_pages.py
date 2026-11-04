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


def notebook_section(name, assets, level=2):
    """The rendered explore_run notebook for this run (results/<name>/notebook.md, written by
    lib/run_notebooks.sh), with its headings put `level` deep and figure paths made relative."""
    path = os.path.join(HERE, "results", name, "notebook.md")
    if not os.path.exists(path):
        return []
    body = open(path).read().replace("@ASSETS@", assets).strip().splitlines()
    body = [("#" * level) + l[1:] if l.startswith("## ") else l for l in body]
    return ["#" * level + " Domain, forcing and output", "",
            f"Made by running the notebook [`explore_run.ipynb`]({NOTEBOOK_URL}) on this run's "
            "output folder (code hidden here). It only plots files MOM6 wrote during the run.", ""] + body + [""]


def status_banner(name, s):
    """Admonition at the top of a configuration's page saying whether its tested run worked."""
    if s is None:
        return '!!! warning ":grey_question: Not tested yet"\n    No test run has been recorded for this configuration.\n'
    if s["ok"]:
        pbs = s.get("pbs", {})
        return (f'!!! success ":white_check_mark: This configuration ran successfully"\n'
                f"    Tested on {environment['date']} with `{versions['ACCESS_OM3_MODULE']}` (`mom6-solo`): "
                f"{pbs.get('NCPUs Requested', '?')} cores, walltime used {pbs.get('Walltime Used', '?')}, "
                f"{pbs.get('Service Units', '?')} SU. Details further down this page.\n")
    issue = known_issues.get(name, "")
    reason = (issue.split(". ")[0].rstrip(".") + ".") if issue else "See the error log further down this page."
    return (f'!!! failure ":x: This configuration did not run"\n'
            f"    Tested on {environment['date']} with `{versions['ACCESS_OM3_MODULE']}`. {reason}\n")


def example_page(ex, s):
    name, example = ex["name"], ex["example"]
    lines = [f"# {name.replace('-', ' / ')}", ""]
    lines += [status_banner(name, s), ""]
    lines += [describe(name, ex), ""]
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
        lines += ['!!! info "Workaround used: no restart files"',
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
                                              "the upstream MOM_parameter_doc.all"))


def figure_lines(name, s, assets):
    """The run's summary figure with its caption (empty if there is none)."""
    if not s.get("figure"):
        return []
    return [f"![{name}]({assets}/tested-configs/{name}.png)", "", f"*{s.get('figure_note', '')}.*", ""]


def results_section(name, s, assets, config_rows, reference_label, show_figure=True):
    """Markdown lines for "What we got", the notebook section (if any) and "Provenance" of one run.
    assets: path from the page to docs/assets; config_rows: table rows naming the config source;
    show_figure=False when the page shows the figure higher up (community pages)."""
    lines = []
    notebook = notebook_section(name, assets)
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

    pc = s.get("param_changes")
    if pc:
        n = len(pc["added"]) + len(pc["removed"]) + len(pc["changed"])
        lines += [f'??? info "Parameters differing from {reference_label} ({n})"',
                  f"    Comparison of this run's `MOM_parameter_doc.all` with {reference_label}.",
                  "    Differences show where the ACCESS-OM3 MOM6 version adds, drops or "
                  "changes default parameters.", ""]
        if pc["changed"]:
            lines += ["    | Parameter | reference | this run |", "    |---|---|---|"]
            lines += [f"    | `{k}` | `{a}` | `{b}` |" for k, (a, b) in pc["changed"].items()]
            lines += [""]
        if pc["added"]:
            lines += ["    New in this run: " + ", ".join(f"`{p}`" for p in pc["added"]), ""]
        if pc["removed"]:
            lines += ["    Only upstream: " + ", ".join(f"`{p}`" for p in pc["removed"]), ""]

    if s.get("env"):
        lines += ['??? info "Run-time environment (selected variables from payu\'s `env.yaml`)"',
                  "    | Variable | Value |", "    |---|---|"]
        lines += [f"    | `{k}` | `{v}` |" for k, v in s["env"].items()]
        lines += [""]
    lines += ['??? info "payu config.yaml written by the script"', "    ```yaml",
              indent(s.get("config_yaml", "").rstrip()), "    ```", ""]
    if s.get("output_files"):
        lines += ['??? info "Output files"', "    | File | Size |", "    |---|---|"]
        lines += [f"    | `{f}` | {sz/1e6:.2f} MB |" for f, sz in s["output_files"].items()]
        lines += [""]
    return lines


# ---- fragments for the hand-written pages of stand-alone configurations ---------------
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
    body = results_section(name, s, "../../assets", STANDALONE[name], REFERENCE_LABEL[name], show_figure=False)
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
for name, *_ in COMMUNITY:
    open(os.path.join(HERE, "results", name, "status.md"), "w").write(status_banner(name, load_summary(name)))

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
