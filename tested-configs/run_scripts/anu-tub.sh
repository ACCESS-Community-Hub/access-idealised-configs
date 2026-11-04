#!/bin/bash
#==============================================================================
# Run ANU-TUB (github.com/ACCESS-Community-Hub/anu-tub) on NCI Gadi with the
# prebuilt MOM6 ocean-only ("solo") executable from ACCESS-OM3.
#
# Usage (from a Gadi login node):
#     PROJECT=<your NCI project> bash anu-tub.sh
#
# What it does:
#   1. clones anu-tub at the commit we tested;
#   2. creates the three input files by running the repository's own notebook
#      (input/mom6-anu-tub-driver.ipynb) as a script;
#   3. picks a vertical coordinate (zstar by default) and edits config.yaml;
#   4. submits the run with `payu run`.
#
# Written with Claude Code for github.com/ACCESS-Community-Hub/access-idealised-configs
#==============================================================================
set -euo pipefail

# ---- Settings you may want to change ----------------------------------------
PROJECT=${PROJECT:?"Please set PROJECT to your NCI project, e.g. PROJECT=tm70"}
TUB_DIR=${TUB_DIR:-/g/data/$PROJECT/$USER/anu-tub}       # where anu-tub is cloned
LAB=${LAB:-/scratch/$PROJECT/$USER/mom6}                  # payu "laboratory" (work + archive)
COORD=${COORD:-zstar}      # vertical coordinate: zstar or adapt (hycom1 needs an extra file, see website)
MONTHS=${MONTHS:-12}       # run length per payu submission (the repository default is 12)
WALLTIME=${WALLTIME:-12:00:00}   # PBS walltime (repository default; ~1.5 h per model year on 312 cores)

# ---- Pinned versions (exactly what was tested) -------------------------------
ANU_TUB_COMMIT=e413708c4b1446e267b42f2f0da95d6ab48ae0e0   # ACCESS-Community-Hub/anu-tub main, 2026-07-27
ACCESS_OM3_MODULE=access-om3/2026.05.004                  # provides the `mom6-solo` executable
PAYU_MODULE=payu/1.3.6_1
PYTHON_MODULE=conda/analysis3-26.10                       # xarray/netCDF4 to make the inputs

# ---- 1. Get the configuration -----------------------------------------------
if [ ! -d "$TUB_DIR/.git" ]; then
    git clone https://github.com/ACCESS-Community-Hub/anu-tub.git "$TUB_DIR"
fi
cd "$TUB_DIR"
git -c advice.detachedHead=false checkout "$ANU_TUB_COMMIT"
git checkout -- config.yaml input.nml MOM_override   # undo edits from a previous run of this script

# ---- 2. Create the input files (topog.nc, forcing.nc, sst.nc) ---------------
# We run the code cells of the repository's notebook unchanged; only the
# NCI-specific helper `nci_ipynb` (used to find the notebook's folder) is stubbed.
if [ ! -f input/sst.nc ]; then
    module use /g/data/xp65/public/modules
    module load "$PYTHON_MODULE"
    python - input/mom6-anu-tub-driver.ipynb input <<'PY'
import json, os, sys, types
import matplotlib; matplotlib.use("Agg")           # no figures on screen
nb, outdir = sys.argv[1], os.path.abspath(sys.argv[2])
sys.modules["nci_ipynb"] = types.SimpleNamespace(dir=lambda: outdir)
ns = {}
for cell in json.load(open(nb))["cells"]:
    if cell["cell_type"] == "code":                 # skip markdown; drop %magics
        exec("".join(l for l in cell["source"] if not l.lstrip().startswith("%")), ns)
print("created:", sorted(f for f in os.listdir(outdir) if f.endswith(".nc")))
PY
    module unload "$PYTHON_MODULE"
fi

# ---- 3. Choose the vertical coordinate and adapt config.yaml -----------------
# input.nml reads MOM_input + MOM_override. In the repository MOM_override is a
# symlink to zstar/MOM_override; re-point it to choose another coordinate.
ln -sfn "$COORD/MOM_override" MOM_override

# Use the released ACCESS-OM3 module instead of the pre-release one in the repo,
# and set project / laboratory / walltime / run length. The repository asks payu to
# insist on the exact executable recorded in manifests/exe.yaml (manifest:
# reproduce: exe: true); as we deliberately use a different (released) executable,
# we switch that check off - payu then records the new executable's hash instead.
sed -i -e 's|/g/data/vk83/prerelease/modules|/g/data/vk83/modules|' \
       -e "s|access-om3/pr140-7|$ACCESS_OM3_MODULE|" \
       -e "s|^# project: <project>|project: $PROJECT|" \
       -e "s|^walltime: .*|walltime: $WALLTIME|" \
       -e "s|^    exe: true|    exe: false   # manifests/exe.yaml records the pre-release exe|" \
       -e "s|^jobname: anu-tub|jobname: anu-tub-$COORD\nexperiment: anu-tub-$COORD\nlaboratory: $LAB|" \
       config.yaml
sed -i -e "s|^\( *months *= *\).*|\1$MONTHS|" input.nml

# ---- 4. Run it ----------------------------------------------------------------
module use /g/data/vk83/modules
module load "$PAYU_MODULE"
payu sweep > /dev/null 2>&1 || true   # tidy any previous failed attempt
payu run
echo "Submitted. Check with: qstat -u \$USER ; output: $LAB/archive/anu-tub-$COORD/output000"
