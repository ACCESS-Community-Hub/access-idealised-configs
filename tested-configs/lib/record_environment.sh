#!/bin/bash
# Print a JSON record of the software environment used for the tested runs:
# module versions, the mom6-solo path + md5, payu version, git commits.
# Called by regenerate_all.sh (summarise stage) -> results/environment.json
set -euo pipefail
HERE=$(cd "$(dirname "$0")/.." && pwd)
source "$HERE/versions.env"

module use /g/data/vk83/modules
module load "$ACCESS_OM3_MODULE" 2> /dev/null
MOM6_SOLO=$(command -v mom6-solo)
ACCESS_MOM6=$(module -t list 2>&1 | grep '^access-mom6/' || true)
LOADED=$(module -t list 2>&1 | grep -v -E '^(Currently|$)' | paste -sd' ' -)

# payu's version as recorded by payu itself in a finished run's env.yaml
# (payu can't be started from inside a container, so we don't call `payu --version`)
PAYU_VERSION=$(grep -h -m1 '"PAYU_TELEMETRY_ENV_VERSION"' "$HERE"/results/*/summary.json 2>/dev/null \
               | head -1 | sed 's/.*: *"\(.*\)".*/payu \1/' || true)

# MOM6 source version/commit, from the Spack spec installed next to the executable
SPEC=$(dirname "$MOM6_SOLO")/../.spack/spec.json
MOM6_SOURCE=$(python -c "import json,sys; n=[x for x in json.load(open(sys.argv[1]))['spec']['nodes'] if x['name']=='access-mom6'][0]; print(n['version'], n['parameters'].get('commit',''))" "$SPEC")

export MOM6_SOLO ACCESS_MOM6 LOADED PAYU_VERSION MOM6_SOURCE
export MOM6_SOLO_MD5=$(md5sum "$MOM6_SOLO" | cut -d' ' -f1)
export WEBSITE_COMMIT=$(git -C "$HERE" rev-parse HEAD)
export DATE=$(date +%Y-%m-%d) HOST=$(hostname)
export MOM6_EXAMPLES_COMMIT ACCESS_OM3_MODULE PAYU_MODULE DATASETS
python - <<'PY'
import json, os
e = os.environ
print(json.dumps({
    "date": e["DATE"],
    "host": e["HOST"],
    "website_commit": e["WEBSITE_COMMIT"],
    "mom6_examples_commit": e["MOM6_EXAMPLES_COMMIT"],
    "access_om3_module": e["ACCESS_OM3_MODULE"],
    "access_mom6_module": e["ACCESS_MOM6"],
    "modules_loaded": e["LOADED"],
    "mom6_solo": e["MOM6_SOLO"],
    "mom6_solo_md5": e["MOM6_SOLO_MD5"],
    "mom6_source": "ACCESS-NRI/MOM6 " + e["MOM6_SOURCE"],
    "payu_module": e["PAYU_MODULE"],
    "payu_version": e["PAYU_VERSION"] or e["PAYU_MODULE"],
    "datasets": e["DATASETS"],
}, indent=1))
PY
