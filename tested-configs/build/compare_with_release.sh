#!/bin/bash
#==============================================================================
# Check that a self-built mom6-solo contains the same machine code as the
# ACCESS-OM3 release's mom6-solo.
#
#     bash compare_with_release.sh /path/to/your/bin/mom6-solo
#
# A plain md5sum of the two files always differs, because each binary records
# where it is installed (Spack install path, RPATH); that changes the size of a
# few header sections and so shifts every address in the program. This script
# compares what does not depend on the install location:
#   1. the symbol table: every function and variable, with its size;
#   2. the disassembled machine code, with all addresses replaced by "X".
# If both match, the two executables run the same instructions.
# Takes about a minute. Written with Claude Code for
# github.com/ACCESS-Community-Hub/access-idealised-configs
#==============================================================================
set -euo pipefail
OWN=${1:?"usage: bash compare_with_release.sh /path/to/your/bin/mom6-solo"}
ACCESS_OM3_MODULE=${ACCESS_OM3_MODULE:-access-om3/2026.05.004}

module use /g/data/vk83/modules
module load "$ACCESS_OM3_MODULE"
RELEASE=$(command -v mom6-solo)

fingerprint() {   # prints "<symbols md5> <code md5>" for one executable
    local syms code
    syms=$(nm -S --defined-only "$1" | awk '{print $2, $3, $4}' | LC_ALL=C sort -k3 | md5sum | cut -d' ' -f1)
    code=$(objdump -d --no-show-raw-insn "$1" | tail -n +3 \
           | sed -E 's/^ *[0-9a-f]+:\t//; s/0x[0-9a-f]+/X/g; s/\b[0-9a-f]{6,16}\b/X/g; s/<[^>]*\+X>/<>/g' \
           | md5sum | cut -d' ' -f1)
    echo "$syms $code"
}

echo "release ($ACCESS_OM3_MODULE): $RELEASE"
echo "yours:                        $OWN"
read -r rel_syms rel_code <<< "$(fingerprint "$RELEASE")"
read -r own_syms own_code <<< "$(fingerprint "$OWN")"
printf '%-14s %-34s %-34s\n' "" "release" "yours"
printf '%-14s %-34s %-34s\n' "file md5" "$(md5sum < "$RELEASE" | cut -d' ' -f1)" "$(md5sum < "$OWN" | cut -d' ' -f1)"
printf '%-14s %-34s %-34s\n' "symbols md5" "$rel_syms" "$own_syms"
printf '%-14s %-34s %-34s\n' "code md5" "$rel_code" "$own_code"
if [ "$rel_syms" = "$own_syms" ] && [ "$rel_code" = "$own_code" ]; then
    echo "MATCH: same symbols and same machine code as the release."
else
    echo "DIFFERENT: your mom6-solo is not the same code as the release."
    exit 1
fi
