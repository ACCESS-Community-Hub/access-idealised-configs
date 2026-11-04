#!/bin/bash
#==============================================================================
# Check a self-built mom6-solo by running MOM6-examples double_gyre with it.
#
#     PROJECT=<proj> MOM6_SOLO=/path/to/bin/mom6-solo bash test_own_build.sh
#
# Uses the double_gyre run script from the website, then swaps the executable
# in its config.yaml before running payu. Run from a Gadi login node.
# Written with Claude Code for github.com/ACCESS-Community-Hub/mom6-idealised-configs
#==============================================================================
set -euo pipefail
PROJECT=${PROJECT:?"set PROJECT"}
MOM6_SOLO=${MOM6_SOLO:?"set MOM6_SOLO to the full path of your mom6-solo"}
HERE=$(cd "$(dirname "$0")/.." && pwd)
EXAMPLES_DIR=${EXAMPLES_DIR:-/g/data/$PROJECT/$USER/MOM6-examples}
LAB=${LAB:-/scratch/$PROJECT/$USER/mom6-examples}

# 1. Set up a copy of double_gyre with the website's script, but don't run it yet:
#    we reuse the script up to (not including) "payu run".
TEST_DIR=$EXAMPLES_DIR/ocean_only/double_gyre_ownbuild
mkdir -p "$TEST_DIR"
sed -e '/^payu sweep/,$d' "$HERE/run_scripts/double_gyre.sh" > "$TEST_DIR/setup.sh"
PROJECT=$PROJECT EXAMPLES_DIR=$EXAMPLES_DIR LAB=$LAB bash "$TEST_DIR/setup.sh"

# 2. Copy the example next to it and point its config.yaml at our executable.
cp "$EXAMPLES_DIR"/ocean_only/double_gyre/{MOM_input,MOM_override,input.nml,diag_table,config.yaml} "$TEST_DIR/"
cd "$TEST_DIR"
sed -i -e "s|^exe: .*|exe: $MOM6_SOLO|" \
       -e "s|^jobname: .*|jobname: double_gyre-own|" \
       -e "s|^experiment: .*|experiment: double_gyre-ownbuild|" config.yaml

# 3. Run. The access-om3 module stays loaded for the MPI and netCDF libraries.
module use /g/data/vk83/modules
module load payu/1.3.6_1
payu sweep > /dev/null 2>&1 || true
payu run
