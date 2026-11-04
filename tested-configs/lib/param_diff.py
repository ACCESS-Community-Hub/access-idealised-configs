"""Compare two MOM_parameter_doc.all files and render the result as a website section.

The parsing and the value comparison follow the "Config Diff" page of access-om3-live
(github.com/chrisb13/access-om3-live: scripts/config_diff_data.py and pages/config_diff.js):
parameters are grouped by MOM6 module ("! === module X ==="), values are compared ignoring
quotes, case and number formatting (1.0E-04 == 0.0001), and the table uses the same classes
(table.diff, td.a / td.b, tr.mod), styled by documentation/docs/css/config_diff.css.
Written with Claude Code for github.com/ACCESS-Community-Hub/mom6-idealised-configs
"""
import html
import re

MODULE = re.compile(r"^!\s*===\s*module\s+(.+?)\s*===")
PARAM = re.compile(r"^(?:#override\s+)?([A-Za-z]\w*)\s*=\s*([^!]*?)\s*(?:!(.*))?$")
MOM6_SEARCH = "https://github.com/mom-ocean/MOM6/search?q="   # as on the access-om3-live Config Diff page


def parse(path):
    """{NAME: {"module", "value", "units", "default", "line"}} from a MOM_parameter_doc.all."""
    params, module = {}, "MOM"
    for n, line in enumerate(open(path), 1):
        line = line.rstrip("\n")
        if m := MODULE.match(line):
            module = m[1]
        elif m := PARAM.match(line):
            note = m[3] or ""
            units = re.search(r"\[([^\]]+)\]", note)
            default = re.search(r"default\s*=\s*(.+)", note)
            params[m[1]] = {"module": module, "value": m[2], "line": n,
                            "units": units[1].strip() if units else "",
                            "default": default[1].strip() if default else None}
    return params


def norm(value):
    """Value for comparison: no quotes, lower case, numbers as numbers."""
    if value is None:
        return None
    s = str(value).strip().strip("\"'").lower()
    if re.match(r"^[-+.\d]", s):
        try:
            return float(s.replace("d", "e"))
        except ValueError:
            pass
    return s


def compare(ref_path, run_path):
    """Rows for every parameter whose value differs or that is in only one file, sorted by module."""
    a, b = parse(ref_path), parse(run_path)
    rows = []
    for name in sorted(set(a) | set(b)):
        pa, pb = a.get(name), b.get(name)
        if pa and pb and norm(pa["value"]) == norm(pb["value"]):
            continue
        rows.append({"name": name, "module": (pb or pa)["module"], "a": pa, "b": pb,
                     "units": (pb or pa)["units"]})
    return sorted(rows, key=lambda r: (r["module"].lower(), r["name"]))


def _table(rows, ref_url, label_a, label_b):
    esc = html.escape
    out = ['<table class="diff"><thead><tr><th>Parameter</th><th>Units</th>'
           f"<th>{esc(label_a)}</th><th>{esc(label_b)}</th></tr></thead><tbody>"]
    module = None
    for r in rows:
        if r["module"] != module:
            module = r["module"]
            out.append(f'<tr class="mod"><td colspan="4">{esc(module)}</td></tr>')
        a, b = r["a"], r["b"]
        cell_a = (f'<td class="val a" data-label="{esc(label_a)}"><a href="{ref_url}#L{a["line"]}" '
                  f'target="_blank" rel="noopener">{esc(a["value"])}</a></td>' if a else
                  f'<td class="val a unset" data-label="{esc(label_a)}">(not in this version)</td>')
        cell_b = (f'<td class="val b" data-label="{esc(label_b)}">{esc(b["value"])}'
                  f'<span class="ln"> line {b["line"]}</span></td>' if b else
                  f'<td class="val b unset" data-label="{esc(label_b)}">(not in this version)</td>')
        out.append(f'<tr class="param"><td><a href="{MOM6_SEARCH}{esc(r["name"])}" target="_blank" '
                   f'rel="noopener">{esc(r["name"])}</a></td><td class="units">{esc(r["units"])}</td>'
                   f"{cell_a}{cell_b}</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def section(ref_path, run_path, ref_url, ref_label, run_gadi_path, level=2):
    """Markdown lines for the "Parameters compared with the reference" section.
    ref_url: GitHub URL of the reference file (lines are linked as ref_url#L<n>);
    run_gadi_path: where the run's own MOM_parameter_doc.all is on Gadi when you run the script."""
    rows = compare(ref_path, run_path)
    changed = [r for r in rows if r["a"] and r["b"]]
    one_side = [r for r in rows if not (r["a"] and r["b"])]
    only_run = sum(1 for r in one_side if r["b"])
    only_ref = len(one_side) - only_run
    h = "#" * level
    lines = [f"{h} Parameters compared with the reference", "",
             f'<span class="chip a">A</span> {ref_label}: [`MOM_parameter_doc.all`]({ref_url})  ',
             f'<span class="chip b">B</span> this run: `MOM_parameter_doc.all` in the run\'s output, '
             f"`{run_gadi_path}` when you run the script", "",
             f"**{len(changed)}** parameter values differ; **{only_run}** parameters exist only in this "
             f"run's MOM6 version and **{only_ref}** only in the reference (new, removed or renamed "
             "parameters). Values are compared ignoring quotes, case and number formatting. "
             "Parameter names link to a search of the MOM6 source; reference values link to their "
             "line on GitHub.", ""]
    if changed:
        lines += [_table(changed, ref_url, "A: reference", "B: this run"), ""]
    if one_side:
        lines += [f'??? note "Parameters in only one of the two files ({len(one_side)})"',
                  "    " + _table(one_side, ref_url, "A: reference", "B: this run"), ""]
    return lines
