#!/bin/bash
#==============================================================================
# Run the ACCESS-OM3 MOM6 single-column configuration with WOMBAT biogeochemistry
# (BATS site, JRA55-do repeat-year forcing) on NCI Gadi.
#
# Configuration: github.com/ACCESS-Community-Hub/om3-mom6-single-column
#   (default branch jra_ryf+wombatlite). Unlike the other configurations on this
#   website it runs the coupled ACCESS-OM3 executable (access-om3-MOM6: MOM6 with
#   data atmosphere and runoff, and stub sea ice and waves), not mom6-solo.
#
# Usage (from a Gadi login node):
#     PROJECT=<your NCI project> bash om3-mom6-single-column.sh
#
# Written with Claude Code for github.com/ACCESS-Community-Hub/access-idealised-configs
#==============================================================================
set -euo pipefail

# ---- Settings you may want to change ----------------------------------------
PROJECT=${PROJECT:?"Please set PROJECT to your NCI project, e.g. PROJECT=tm70"}
SCM_DIR=${SCM_DIR:-/g/data/$PROJECT/$USER/om3-mom6-single-column}   # where the repository is cloned
LAB=${LAB:-/scratch/$PROJECT/$USER/access-om3}                      # payu "laboratory" (work + archive)

# ---- Pinned versions (exactly what was tested) -------------------------------
CONFIG_COMMIT=9a8310b09bd4b97c676ccbd0b54ddf4dfe686b5f   # branch jra_ryf+wombatlite
ACCESS_OM3_MODULE=access-om3/2026.05.004                 # provides access-om3-MOM6
PAYU_MODULE=payu/1.3.6_1

# ---- 1. Get the configuration -------------------------------------------------
if [ ! -d "$SCM_DIR/.git" ]; then
    git clone https://github.com/ACCESS-Community-Hub/om3-mom6-single-column.git "$SCM_DIR"
fi
cd "$SCM_DIR"
git -c advice.detachedHead=false checkout "$CONFIG_COMMIT"
git checkout -- config.yaml          # start from the repository's config.yaml every time

# ---- 2. Small changes to config.yaml ------------------------------------------
# - use the current ACCESS-OM3 release (the repository names access-om3/2026.03.000);
# - don't insist on the executable recorded in manifests/exe.yaml (that older release);
# - say which project to charge and where payu should work and archive.
sed -i -e "s|access-om3/2026\.03\.000|$ACCESS_OM3_MODULE|" \
       -e "/^manifest:/,/^ *exe: true/ s|exe: true|exe: false|" config.yaml
cat >> config.yaml <<EOF

# added by $(basename "$0")
project: $PROJECT
experiment: om3-mom6-single-column
laboratory: $LAB
EOF

# ---- 3. Run it (one model year, as set in nuopc.runconfig) ---------------------
module use /g/data/vk83/modules
module load "$PAYU_MODULE"
payu sweep > /dev/null 2>&1 || true
payu run
echo "Submitted. Check with: qstat -u \$USER ; output: $LAB/archive/om3-mom6-single-column/output000"
