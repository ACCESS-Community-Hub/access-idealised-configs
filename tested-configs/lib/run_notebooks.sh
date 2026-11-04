#!/bin/bash
#==============================================================================
# Run notebooks/explore_run.ipynb on every successful run and render it for the website.
#
#     bash lib/run_notebooks.sh [name ...]        (default: every run with results/<name>/summary.json "ok")
#
# Needs conda/analysis3 (papermill, nbconvert, xarray); regenerate_all.sh's "notebooks"
# stage loads it. For each run it writes
#   $WORK_ROOT/notebooks/<name>.ipynb                      executed notebook (not kept in git)
#   results/<name>/notebook.md                              rendered output, code hidden
#   results/<name>/notebook_full.md                         rendered with the code (notebook sub-page)
#   documentation/docs/assets/tested-configs/notebooks/<name>/*.png   its figures
# lib/make_pages.py then puts notebook.md on the configuration's page.
# Written with Claude Code for github.com/ACCESS-Community-Hub/mom6-idealised-configs
#==============================================================================
set -uo pipefail
HERE=$(cd "$(dirname "$0")/.." && pwd)                 # tested-configs/
ASSETS=$HERE/../documentation/docs/assets/tested-configs/notebooks
EXEC_DIR=${WORK_ROOT:?"set WORK_ROOT (see regenerate_all.sh)"}/notebooks
mkdir -p "$EXEC_DIR" "$ASSETS"

names=("$@")
if [ ${#names[@]} -eq 0 ]; then
    names=($(cd "$HERE/results" && for f in */summary.json; do
        python -c "import json,sys; s=json.load(open('$f')); sys.exit(0 if s.get('ok') else 1)" && dirname "$f"
    done))
fi

for name in "${names[@]}"; do
    if ! python -c "import json,sys; sys.exit(0 if json.load(open('$HERE/results/$name/summary.json')).get('ok') else 1)" 2>/dev/null; then
        echo "== $name: skipped (no successful run recorded)"
        continue
    fi
    run_dir=$(python -c "import json; print(json.load(open('$HERE/results/$name/summary.json'))['output_dir'])")
    echo "== $name ($run_dir)"
    if ! papermill --log-level WARNING "$HERE/notebooks/explore_run.ipynb" "$EXEC_DIR/$name.ipynb" \
            -p name "$name" -p run_dir "$run_dir"; then
        echo "   notebook failed for $name (see $EXEC_DIR/$name.ipynb)"
        continue
    fi
    # Render without the code cells; move the figures into the docs assets and mark their
    # paths with @ASSETS@ so make_pages.py can write the right relative path for each page.
    # Drop stderr output (package warnings) from the executed notebook before rendering.
    python - "$EXEC_DIR/$name.ipynb" <<'PY'
import json, sys
nb = json.load(open(sys.argv[1]))
for cell in nb["cells"]:
    cell["outputs"] = [o for o in cell.get("outputs", [])
                       if not (o.get("output_type") == "stream" and o.get("name") == "stderr")]
json.dump(nb, open(sys.argv[1], "w"), indent=1)
PY
    tmp=$(mktemp -d -p "$EXEC_DIR")
    jupyter nbconvert --log-level WARN --to markdown --no-input --output-dir "$tmp" --output notebook \
        "$EXEC_DIR/$name.ipynb"
    mkdir -p "$ASSETS/$name"
    for old in "$ASSETS/$name"/*.png; do [ -e "$old" ] && rm "$old"; done
    for png in "$tmp"/notebook_files/*.png; do [ -e "$png" ] && mv "$png" "$ASSETS/$name/"; done
    sed -e "s|](notebook_files/|](@ASSETS@/tested-configs/notebooks/$name/|g" \
        -e '/^# Explore one MOM6 run/,/^To use it on your own run/d' \
        "$tmp/notebook.md" > "$HERE/results/$name/notebook.md"
    rm "$tmp/notebook.md"; rmdir "$tmp/notebook_files" 2>/dev/null
    # Full version with the code, for the notebook sub-page. Rendered into its own folder
    # under the same name, so its figure files are named exactly as the ones moved above.
    mkdir -p "$tmp/full"
    jupyter nbconvert --log-level WARN --to markdown --output-dir "$tmp/full" --output notebook \
        "$EXEC_DIR/$name.ipynb"
    sed -e "s|](notebook_files/|](@ASSETS@/tested-configs/notebooks/$name/|g" \
        "$tmp/full/notebook.md" > "$HERE/results/$name/notebook_full.md"
    for f in "$tmp"/full/notebook_files/*; do [ -e "$f" ] && rm "$f"; done
    rm "$tmp/full/notebook.md"; rmdir "$tmp/full/notebook_files" 2>/dev/null; rmdir "$tmp/full" "$tmp"
done
