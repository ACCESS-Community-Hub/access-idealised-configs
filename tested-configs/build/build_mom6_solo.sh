#!/bin/bash
#==============================================================================
# Build your own MOM6 ocean-only ("solo") executable on NCI Gadi with
# shared Spack 1.1 installation that ACCESS-NRI provides on Gadi, starting from an ACCESS-OM3 release.
#
# You only need this if you want to CHANGE MOM6 source code: the released
# module (module load access-om3/<version>) already provides `mom6-solo`.
#
# Usage (needs membership of vk83), on a node with AVX-512 (see the check below):
#     bash build_mom6_solo.sh
# PBS compute nodes have no internet. To build in a PBS job (e.g. queue normalsr),
# first run the script on a login node with FETCH_ONLY=1 (clones the recipe, creates
# the Spack environment and downloads all sources), then run it again in the job.
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


mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

# ---- 1. Enable the shared Spack installation (provided by ACCESS-NRI) -------------
module use /g/data/vk83/modules
module load spack          # the default is Spack 1.1 (tested with spack/1.1); see
                           # https://docs.access-hive.org.au/getting_started/spack/#enable-spack
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
    if [ "$LOCAL_SPACK_DIRS" = 1 ]; then
        spack -e "$ENV_DIR" config add "config:install_tree:root:$BUILD_DIR/spack/release"
        spack -e "$ENV_DIR" config add "config:source_cache:$BUILD_DIR/spack/sourcecache"
        spack -e "$ENV_DIR" config add "config:misc_cache:$BUILD_DIR/spack/cache"
    fi
fi

if [ "${FETCH_ONLY:-0}" = 1 ]; then
    spack -e "$ENV_DIR" concretize -f --reuse-deps
    spack -e "$ENV_DIR" fetch            # sources into the Spack source cache
    echo "Sources fetched; now run this script without FETCH_ONLY on an AVX-512 node."
    exit 0
fi

# ---- 4. Concretize and build ---------------------------------------------------
# The release (and its build tools, e.g. cmake) is compiled for x86_64_v4 (AVX-512).
# On an older CPU (e.g. Broadwell `normalbw` nodes) Spack would target x86_64_v3 and try
# to rebuild every dependency, and the release's cmake would crash (illegal instruction).
if ! grep -q -m1 avx512f /proc/cpuinfo; then
    echo "This CPU has no AVX-512: build on an AVX-512 node instead (e.g. a normalsr PBS job)." >&2
    exit 1
fi
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
echo "Check it matches the release: bash $(dirname "$0")/compare_with_release.sh $MOM6_SOLO"
