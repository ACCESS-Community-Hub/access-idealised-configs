#!/bin/bash
#==============================================================================
# Run the ISOMIP+ "Ocean0"-like ice-shelf cavity configuration (sigma-shelf
# z* coordinate, by Claire Yung) on NCI Gadi with the prebuilt MOM6
# ocean-only ("solo") executable from ACCESS-OM3.
#
# Configuration: branch isomip-plus-ocean0-sigmashelfzstar of
#   github.com/ACCESS-Community-Hub/access-idealised-configs
# Input file (ice-shelf thickness / surface pressure, 160 kB):
#   github.com/claireyung/isomip-test-mom6-for-iom3-configs  INPUT/Ocean0_3D_Claire.nc
#
# Usage (from a Gadi login node):
#     PROJECT=<your NCI project> bash isomip-plus-ocean0.sh
#
# Written with Claude Code for github.com/ACCESS-Community-Hub/access-idealised-configs
#==============================================================================
set -euo pipefail

# ---- Settings you may want to change ----------------------------------------
PROJECT=${PROJECT:?"Please set PROJECT to your NCI project, e.g. PROJECT=tm70"}
WORK_DIR=${WORK_DIR:-/g/data/$PROJECT/$USER/isomip-plus}   # where the config + input are cloned
LAB=${LAB:-/scratch/$PROJECT/$USER/mom6}                   # payu "laboratory" (work + archive)

# ---- Pinned versions (exactly what was tested) -------------------------------
CONFIG_COMMIT=094d9177bf5ada2032f502463f0546d87a24bd9b   # branch isomip-plus-ocean0-sigmashelfzstar
INPUT_COMMIT=3b86dc0bcb4b7a38156bdb3b94952fe47bb51887    # claireyung/isomip-test-mom6-for-iom3-configs
ACCESS_OM3_MODULE=access-om3/2026.05.004                 # provides the `mom6-solo` executable
PAYU_MODULE=payu/1.3.6_1

mkdir -p "$WORK_DIR"
cd "$WORK_DIR"

# ---- 1. Get the configuration and the input file ------------------------------
if [ ! -d config/.git ]; then
    git clone https://github.com/ACCESS-Community-Hub/access-idealised-configs.git config
fi
git -C config cat-file -e "$CONFIG_COMMIT" 2>/dev/null \
    || git -C config fetch -q origin isomip-plus-ocean0-sigmashelfzstar
git -C config -c advice.detachedHead=false checkout "$CONFIG_COMMIT"

if [ ! -d input-repo/.git ]; then
    git clone https://github.com/claireyung/isomip-test-mom6-for-iom3-configs.git input-repo
fi
git -C input-repo -c advice.detachedHead=false checkout "$INPUT_COMMIT"

# ---- 2. Point config.yaml at the released executable and the input file ------
# The branch's config.yaml uses a privately-built MOM6 (/g/data/x77/...) and
# openmpi/4.1.2; we swap in the ACCESS-OM3 module, which brings its own MPI.
cd config
cat > config.yaml <<EOF
# payu configuration for ISOMIP+ Ocean0 (written by $(basename "$0"))
project: $PROJECT
queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
ncpus: 48
walltime: 01:00:00
jobname: isomip-plus
experiment: isomip-plus-ocean0
laboratory: $LAB

model: mom6
exe: mom6-solo
input:
  - $WORK_DIR/input-repo/INPUT
modules:
  use:
    - /g/data/vk83/modules
  load:
    - $ACCESS_OM3_MODULE

collate: false
runlog: false            # don't commit run logs into the cloned repository
metadata:
  enable: false
EOF

# ---- 3. Run it (3 months, as set in input.nml) --------------------------------
module use /g/data/vk83/modules
module load "$PAYU_MODULE"
payu sweep > /dev/null 2>&1 || true
payu run
echo "Submitted. Check with: qstat -u \$USER ; output: $LAB/archive/isomip-plus-ocean0/output000"
