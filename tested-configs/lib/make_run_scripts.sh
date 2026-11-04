#!/bin/bash
# Turn templates/run_example.sh.in into one stand-alone script per example:
#   run_scripts/<expt_name>.sh
# Values come from versions.env (pinned versions) and examples.txt (per example).
# These generated scripts are what the website embeds AND what regenerate_all.sh runs.
set -euo pipefail
HERE=$(cd "$(dirname "$0")/.." && pwd)
source "$HERE/versions.env"

grep -v -E '^\s*(#|$)' "$HERE/examples.txt" | while read -r example ncpus walltime variant overrides; do
    # payu experiment name: ocean_only/seamount/z -> seamount-z ; variants get a suffix
    expt_name=$(echo "${example#ocean_only/}" | tr '/' '-')
    variant_block=""
    if [ -n "${variant:-}" ]; then
        expt_name="${expt_name}-${variant}"
        # "DAYMAX=3650.0,ENERGYSAVEDAYS=30.0" -> "#override DAYMAX = 3650.0" lines
        override_lines=$(echo "$overrides" | tr ',' '\n' | sed 's/^\([^=]*\)=\(.*\)$/#override \1 = \2/')
        variant_block=$(sed -e "s|@VARIANT@|$variant|g" -e "s|@SCRIPT_NAME@|${expt_name}.sh|g" \
                            "$HERE/templates/variant_block.sh.in")
        variant_block=${variant_block//@OVERRIDE_LINES@/$override_lines}
    fi
    script="$HERE/run_scripts/${expt_name}.sh"
    # replace the @VARIANT_BLOCK@ line (possibly with nothing), then the simple placeholders
    awk -v block="$variant_block" '$0=="@VARIANT_BLOCK@"{ if (block!="") { print block; print "" }; next } {print}' \
        "$HERE/templates/run_example.sh.in" |
    sed -e "s|@EXAMPLE@|$example|g" \
        -e "s|@EXPT_NAME@|$expt_name|g" \
        -e "s|@NCPUS@|$ncpus|g" \
        -e "s|@WALLTIME@|$walltime|g" \
        -e "s|@SCRIPT_NAME@|${expt_name}.sh|g" \
        -e "s|@MOM6_EXAMPLES_COMMIT@|$MOM6_EXAMPLES_COMMIT|g" \
        -e "s|@ACCESS_OM3_MODULE@|$ACCESS_OM3_MODULE|g" \
        -e "s|@PAYU_MODULE@|$PAYU_MODULE|g" \
        -e "s|@DATASETS@|$DATASETS|g" > "$script"
    chmod +x "$script"
    echo "$script"
done
