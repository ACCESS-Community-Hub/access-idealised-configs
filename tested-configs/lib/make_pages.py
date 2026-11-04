#!/usr/bin/env python
"""Write the website pages for the tested MOM6-examples from results/*/summary.json.

    python lib/make_pages.py            (run from anywhere; paths are relative to this file)

Writes (all generated, do not edit by hand):
  documentation/docs/pages/configurations/mom6examples.md         overview table
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
descriptions = yaml.safe_load(open(os.path.join(HERE, "descriptions.yaml")))
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


def describe(name, ex=None):
    if ex and ex["variant"]:
        changes = ", ".join(f"`{c}`" for c in ex["variant"][1].split(","))
        return f"Variant of `{ex['base']}` with {changes}. " + describe(ex["base"])
    if name in descriptions:
        return " ".join(descriptions[name].split())
    if name.startswith("CVmix_SCM_tests"):
        _, forcing, scheme = name.split("-")
        return (f"CVMix single-column test: `{forcing}` surface forcing with the "
                f"`{scheme}` boundary-layer scheme.")
    return ""


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
def example_page(ex, s):
    name, example = ex["name"], ex["example"]
    lines = [f"# {name.replace('-', ' / ')}", ""]
    lines += [describe(name, ex), ""]
    if ex["variant"]:
        lines += [f"This is a copy of [{ex['base']}]({ex['base']}.md) with these lines added to "
                  "`MOM_override`, e.g. to run long enough to see a spun-up state:", "", "```text"]
        lines += [f"#override {c.replace('=', ' = ')}" for c in ex["variant"][1].split(",")]
        lines += ["```", ""]
    lines += [f"Upstream configuration: [`{example}`]({UPSTREAM}/tree/{commit}/{example}) "
              f"(MOM6-examples commit [`{commit[:8]}`]({UPSTREAM}/commit/{commit})).", ""]

    if s is None:
        lines += ['!!! warning "Not yet tested"', "    This example has not been run yet.", ""]
    elif s["ok"]:
        pbs = s.get("pbs", {})
        lines += ['!!! success "Tested: this example runs"',
                  f"    Ran on Gadi on {environment['date']} with `{versions['ACCESS_OM3_MODULE']}` "
                  f"(`mom6-solo`) and `{versions['PAYU_MODULE']}` on {ex['ncpus']} Sapphire Rapids "
                  f"core(s); walltime used {pbs.get('Walltime Used', '?')}, "
                  f"{pbs.get('Service Units', '?')} SU.", ""]
    else:
        lines += ['!!! failure "Tested: this example did NOT run successfully"',
                  "    See the details below; the log tail shows where it stopped.", ""]

    lines += ['!!! note "Generated with Claude Code"',
              "    This page, the script and the figure were generated automatically by "
              "[`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/"
              "mom6-idealised-configs/tree/main/tested-configs) (written with Claude Code). "
              "See [How these pages were made](../mom6examples.md#how-these-pages-were-made).", ""]

    lines += ["## Run it yourself", "",
              "From a Gadi **login node** (membership of NCI project `vk83` needed"
              + (", and `ol01` for the input data" if (s or {}).get("inputs") else "") + "):", "",
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


def results_section(name, s, assets, config_rows, reference_label):
    """Markdown lines for "What we got" + "Provenance" of one run.
    assets: path from the page to docs/assets; config_rows: table rows naming the config source."""
    lines = []
    if not s["ok"] and s.get("failure_log"):
        lines += ['??? failure "End of the error log"', "    ```text",
                  indent("\n".join(s["failure_log"])), "    ```", ""]
    lines += ["## What we got", ""]
    if s.get("figure"):
        lines += [f"![{name}]({assets}/tested-configs/{name}.png)", "",
                  f"*{s.get('figure_note', '')}.*", ""]
    if s.get("ocean_stats_tail"):
        lines += ["Last lines of `ocean.stats`:", "", "```text"] + s["ocean_stats_tail"] + ["```", ""]
    if s.get("key_params"):
        lines += ["Key parameters of this run (from `MOM_parameter_doc.all`):", "",
                  "| Parameter | Value |", "|---|---|"]
        lines += [f"| `{k}` | `{v}` |" for k, v in s["key_params"].items()]
        lines += [""]

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
                  "    | File | md5 | Path |", "    |---|---|---|"]
        lines += [f"    | `{k}` | `{v['md5']}` | `{v['fullpath']}` |"
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
    body = results_section(name, s, "../../assets", STANDALONE[name], REFERENCE_LABEL[name])
    # demote headings one level so they sit under the page's "Tested run" section
    body = [("#" + l) if l.startswith("## ") else l for l in body]
    return "\n".join(head + body)


# ---------------------------------------------------------------------------------
os.makedirs(PAGES, exist_ok=True)
os.makedirs(ASSETS, exist_ok=True)
rows = []
for i, ex in enumerate(examples):
    if i == 0 or ex["section"] != examples[i - 1]["section"]:
        rows.append(f"| **{ex['section']}** | | | | |")
    s = load_summary(ex["name"])
    if s and s.get("figure"):
        shutil.copy(os.path.join(HERE, "results", ex["name"], "figure.png"),
                    os.path.join(ASSETS, ex["name"] + ".png"))
    open(os.path.join(PAGES, ex["name"] + ".md"), "w").write(example_page(ex, s) + "\n")
    su = (s or {}).get("pbs", {}).get("Service Units", "")
    rows.append(f"| [{ex['name']}](mom6examples/{ex['name']}.md) | {status_badge(s)} | {ex['ncpus']} | {su} | "
                f"{describe(ex['name'], ex)} |")

for name in STANDALONE:
    s = load_summary(name)
    os.makedirs(os.path.join(HERE, "results", name), exist_ok=True)
    if s and s.get("figure"):
        shutil.copy(os.path.join(HERE, "results", name, "figure.png"),
                    os.path.join(ASSETS, name + ".png"))
    text = standalone_fragment(name, s) if s else '!!! warning "Not yet tested"\n    No test run has been recorded yet.'
    open(os.path.join(HERE, "results", name, "tested.md"), "w").write(text + "\n")

n_ok = sum(1 for ex in examples if (load_summary(ex["name"]) or {}).get("ok"))
index = open(os.path.join(HERE, "templates", "mom6examples_index.md.in")).read()
index = (index.replace("@TABLE@", "\n".join(rows))
              .replace("@N_OK@", str(n_ok)).replace("@N_TOTAL@", str(len(examples)))
              .replace("@DATE@", environment["date"])
              .replace("@COMMIT@", commit).replace("@COMMIT8@", commit[:8])
              .replace("@ACCESS_OM3_MODULE@", versions["ACCESS_OM3_MODULE"])
              .replace("@PAYU@", environment.get("payu_version", versions["PAYU_MODULE"]))
              .replace("@MOM6_SOLO@", environment.get("mom6_solo", ""))
              .replace("@MOM6_SOLO_MD5@", environment.get("mom6_solo_md5", ""))
              .replace("@ACCESS_MOM6@", environment.get("access_mom6_module", ""))
              .replace("@MOM6_SOURCE@", environment.get("mom6_source", ""))
              .replace("@WEBSITE_COMMIT@", environment.get("website_commit", "")))
open(PAGES + ".md", "w").write(index)

# ---- navigation block in mkdocs.yml ---------------------------------------------------
nav = ["        - MOM6 Examples:",
       "            - pages/configurations/mom6examples.md"]
for i, ex in enumerate(examples):
    if i == 0 or ex["section"] != examples[i - 1]["section"]:
        nav.append(f"            - {ex['section']}:")
    nav.append(f"                - {ex['name']}: pages/configurations/mom6examples/{ex['name']}.md")
text = open(MKDOCS).read()
text = re.sub(r"( *# BEGIN generated mom6examples nav[^\n]*\n).*?( *# END generated mom6examples nav)",
              lambda m: m.group(1) + "\n".join(nav) + "\n" + m.group(2), text, flags=re.S)
open(MKDOCS, "w").write(text)
print(f"wrote {len(examples)} pages; {n_ok} ran successfully")
