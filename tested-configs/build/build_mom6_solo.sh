#!/bin/bash
#==============================================================================
# Build your own MOM6 ocean-only ("solo") executable on NCI Gadi with
# ACCESS-NRI's shared Spack 1.1 instance, starting from an ACCESS-OM3 release.
#
# You only need this if you want to CHANGE MOM6 source code: the released
# module (module load access-om3/<version>) already provides `mom6-solo`.
#
# Usage (Gadi login node, or a PBS job; needs membership of vk83):
#     bash build_mom6_solo.sh
#
# Written with Claude Code for github.com/ACCESS-Community-Hub/mom6-idealised-configs
#==============================================================================
set -euo pipefail

# ---- Settings you may want to change ----------------------------------------
BUILD_DIR=${BUILD_DIR:-/g/data/$PROJECT/$USER/mom6-solo-build}  # holds ACCESS-OM3 clone + Spack env
ACCESS_OM3_RELEASE=${ACCESS_OM3_RELEASE:-2026.05.004}           # github.com/ACCESS-NRI/ACCESS-OM3/releases
# Optional: keep Spack's install tree and caches inside BUILD_DIR instead of
# the default /g/data/$PROJECT/$USER/spack/1.1/{release,sourcecache,cache} (1 = yes).
LOCAL_SPACK_DIRS=${LOCAL_SPACK_DIRS:-0}
# Building on a node older than the login nodes (e.g. a Broadwell `normalbw` job)?
# Spack would then target x86_64_v3, find none of the release's x86_64_v4 packages
# reusable and rebuild everything (hours). 1 = target x86_64_v4 anyway (compiling works;
# the executable then runs only on Cascade Lake / Sapphire Rapids nodes, like the release).
ALLOW_FOREIGN_TARGET=${ALLOW_FOREIGN_TARGET:-0}

mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

# ---- 1. Enable ACCESS-NRI's shared Spack -----------------------------------------
module use /g/data/vk83/modules
module load spack/1.1
# Note: Spack keeps small cache files in /g/data/$PROJECT/$USER/spack/1.1 even with
# LOCAL_SPACK_DIRS=1 (the module sets the user-cache path, and the first env commands
# run before our env-level settings exist). We redirect what we can:
[ "$LOCAL_SPACK_DIRS" = 1 ] && export SPACK_USER_CACHE_PATH=$BUILD_DIR/spack/user-cache

# ---- 2. Get the ACCESS-OM3 release recipe ---------------------------------------
# Its spack.yaml pins every component version and compiler flag of the release.
if [ ! -d ACCESS-OM3/.git ]; then
    git clone https://github.com/ACCESS-NRI/ACCESS-OM3.git
fi
git -C ACCESS-OM3 -c advice.detachedHead=false checkout "$ACCESS_OM3_RELEASE"

# ---- 3. Make a Spack environment that builds only MOM6 solo ---------------------
# The release builds the full coupled model (spec `access-om3`). We swap that
# spec for `access-mom6`; the release already requires `+mom6_solo`, and we add
# `~access3` so the coupled-model library (and its ESMF stack) isn't built.
ENV_DIR=$BUILD_DIR/mom6-solo-env
if [ ! -d "$ENV_DIR" ]; then
    spack env create -d "$ENV_DIR" ACCESS-OM3/spack.yaml
    spack -e "$ENV_DIR" remove access-om3
    spack -e "$ENV_DIR" add access-mom6
    spack -e "$ENV_DIR" config add 'packages:access-mom6:require:["~access3"]'
    if [ "$ALLOW_FOREIGN_TARGET" = 1 ]; then
        spack -e "$ENV_DIR" config add "concretizer:targets:host_compatible:false"
    fi
    if [ "$LOCAL_SPACK_DIRS" = 1 ]; then
        spack -e "$ENV_DIR" config add "config:install_tree:root:$BUILD_DIR/spack/release"
        spack -e "$ENV_DIR" config add "config:source_cache:$BUILD_DIR/spack/sourcecache"
        spack -e "$ENV_DIR" config add "config:misc_cache:$BUILD_DIR/spack/cache"
    fi
fi

# ---- 4. Concretize and build ---------------------------------------------------
# --reuse-deps: dependencies (FMS, netCDF, OpenMPI, ...) are reused from the release
# where possible, while MOM6 itself is concretized and compiled afresh.
spack -e "$ENV_DIR" concretize -f --reuse-deps
echo "Packages that will be compiled from source:"
spack -e "$ENV_DIR" spec -I | grep -E "^ - " || echo "(none besides those listed)"
spack -e "$ENV_DIR" install

# ---- 5. Where is the executable? ---------------------------------------------------
MOM6_SOLO=$(spack -e "$ENV_DIR" location -i access-mom6)/bin/mom6-solo
ls -l "$MOM6_SOLO"
echo "Built: $MOM6_SOLO"
echo "In a payu config.yaml use:   exe: $MOM6_SOLO"
