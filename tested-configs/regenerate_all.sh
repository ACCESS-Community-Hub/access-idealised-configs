#!/bin/bash
#==============================================================================
# Re-run every tested configuration and regenerate the website pages.
#
#   PROJECT=<proj> ./regenerate_all.sh [stage ...]
#
# stages (default: all of them, in this order):
#   scripts    write run_scripts/<name>.sh from templates/ + examples.txt + versions.env
#   run        submit every run script (payu run); old archives are moved aside, not deleted
#   wait       wait until all our PBS jobs have finished
#   summarise  write results/<name>/{summary.json,figure.png,ocean.stats} + results/environment.json
#   notebooks  run notebooks/explore_run.ipynb on each successful run (domain, forcing, output)
#   pages      write the website pages (documentation/docs/pages/configurations/...)
#
# To test a new ACCESS-OM3 release: edit versions.env, then run this script.
# Optional environment variables:
#   WORK_ROOT  where clones and the payu laboratory go (default /scratch/$PROJECT/$USER/access-idealised-tests)
#   ONLY       space-separated list of names to (re)run, e.g. ONLY="double_gyre anu-tub"
#
# Run it from a Gadi login node. If you are inside a container (ARE/JupyterLab),
# the "run" stage is sent to a small PBS job (lib/run_in_pbs.pbs) instead,
# because payu cannot start from inside another container.
#
# Written with Claude Code for github.com/ACCESS-Community-Hub/access-idealised-configs
#==============================================================================
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
cd "$HERE"
source versions.env

PROJECT=${PROJECT:?"set PROJECT"}
WORK_ROOT=${WORK_ROOT:-/scratch/$PROJECT/$USER/access-idealised-tests}
export PROJECT
export EXAMPLES_DIR=$WORK_ROOT/MOM6-examples   # read by the run_scripts
export LAB=$WORK_ROOT/lab
export TUB_DIR=$WORK_ROOT/anu-tub
export WORK_DIR=$WORK_ROOT/isomip-plus
export SCM_DIR=$WORK_ROOT/om3-mom6-single-column
mkdir -p "$WORK_ROOT/logs"
STAGES=${*:-scripts run wait summarise notebooks pages}

# ---- The list of runs: "name|control dir|reference dir for MOM_parameter_doc" ----
# MOM6-examples (from examples.txt), then the stand-alone configurations.
list_runs() {
    grep -v -E '^\s*(#|$)' examples.txt | while read -r example _ _ variant _; do
        name=$(echo "${example#ocean_only/}" | tr '/' '-')
        control=$EXAMPLES_DIR/$example
        if [ -n "${variant:-}" ]; then name=$name-$variant; control=${control}_$variant; fi
        echo "$name|$control|$EXAMPLES_DIR/$example"
    done
    echo "anu-tub-zstar|$TUB_DIR|$TUB_DIR/docs"   # anu-tub.sh runs COORD=zstar by default
    echo "isomip-plus-ocean0|$WORK_DIR/config|$WORK_DIR/input-repo/docs"   # compare with Claire's own run
    echo "om3-mom6-single-column|$SCM_DIR|$SCM_DIR/docs"   # coupled ACCESS-OM3 single column
}
selected() { [ -z "${ONLY:-}" ] || [[ " $ONLY " == *" $1 "* ]]; }
script_for() {   # run script that produces experiment <name>
    case $1 in anu-tub-*) echo run_scripts/anu-tub.sh ;; *) echo "run_scripts/$1.sh" ;; esac
}

for stage in $STAGES; do
case $stage in

scripts)
    bash lib/make_run_scripts.sh > /dev/null
    echo "== wrote $(ls run_scripts | wc -l) run scripts"
    ;;

run)
    if [ -n "${SINGULARITY_CONTAINER:-}${APPTAINER_CONTAINER:-}" ]; then
        # payu can't start inside a container: run this stage in a small PBS job instead.
        echo "== inside a container: submitting the 'run' stage as a PBS job"
        qsub -P "$PROJECT" -q normalbw -N drv-run -j oe -o "$WORK_ROOT/logs/run_stage.log" \
             -l storage=gdata/vk83+gdata/ol01+gdata/xp65+gdata/$PROJECT+scratch/$PROJECT \
             -v "CMD=bash regenerate_all.sh run,PROJECT=$PROJECT,WORK_ROOT=$WORK_ROOT,ONLY=${ONLY:-},MONTHS=${MONTHS:-1},WALLTIME=${WALLTIME:-01:00:00}" \
             lib/run_in_pbs.pbs > "$WORK_ROOT/logs/driver_jobs.txt"
        continue
    fi
    # Clone once up front (needs internet: login node or copyq) and check out the tested commit.
    [ -d "$EXAMPLES_DIR/.git" ] || git clone https://github.com/NOAA-GFDL/MOM6-examples.git "$EXAMPLES_DIR"
    list_runs | while IFS='|' read -r name control ref; do
        selected "$name" || continue
        # Start each experiment from scratch: move an old archive aside (never deleted).
        if [ -d "$LAB/archive/$name" ]; then
            mv "$LAB/archive/$name" "$LAB/archive/$name.old-$(date +%Y%m%d%H%M%S)"
        fi
        script=$(script_for "$name")
        log=$WORK_ROOT/logs/$name.submit.log    # payu prints "Job ID: <id>" here
        echo "== submitting $name ($script)"
        # Run a snapshot copy: bash reads scripts while running them, so regenerating
        # run_scripts/ at the same time would otherwise corrupt a running submission.
        mkdir -p "$WORK_ROOT/logs/scripts"
        cp "$script" "$WORK_ROOT/logs/scripts/"
        # anu-tub: 1 month by default here (~80 SU) instead of the repository's 12 months
        MONTHS=${MONTHS:-1} WALLTIME=${WALLTIME:-01:00:00} \
            bash "$WORK_ROOT/logs/scripts/$(basename "$script")" > "$log" 2>&1 \
            || echo "   submission FAILED, see $log"
    done
    ;;

wait)
    # 1) wrapper jobs (only used inside containers), 2) the model jobs payu submitted.
    wait_for() { for id in "$@"; do while qstat "$id" > /dev/null 2>&1; do sleep 60; done; done; }
    echo "== waiting for PBS jobs to finish"
    if [ -f "$WORK_ROOT/logs/driver_jobs.txt" ]; then
        wait_for $(cat "$WORK_ROOT/logs/driver_jobs.txt")
        rm "$WORK_ROOT/logs/driver_jobs.txt"
    fi
    wait_for $(grep -h "^Job ID:" "$WORK_ROOT"/logs/*.submit.log 2>/dev/null | awk '{print $3}')
    ;;

summarise)
    module use /g/data/xp65/public/modules
    module load conda/analysis3-26.10
    list_runs | while IFS='|' read -r name control ref; do
        selected "$name" || continue
        python lib/summarise_run.py "$name" "$control" "$LAB/archive/$name" "results/$name" $ref \
            2> >(grep -v PROJ >&2) || echo "   summarise failed for $name"
    done
    bash lib/record_environment.sh > results/environment.json
    ;;

notebooks)
    module use /g/data/xp65/public/modules
    module load conda/analysis3-26.10
    names=()
    for f in results/*/summary.json; do
        name=$(basename "$(dirname "$f")")
        selected "$name" && names+=("$name")
    done
    bash lib/run_notebooks.sh "${names[@]}"
    ;;

pages)
    module use /g/data/xp65/public/modules
    module load conda/analysis3-26.10
    python lib/make_pages.py
    ;;

*) echo "unknown stage: $stage"; exit 1 ;;
esac
done
