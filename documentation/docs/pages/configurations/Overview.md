# Available configurations

All configurations below run on NCI Gadi with the MOM6 ocean-only executable `mom6-solo`
that ships with the [ACCESS-OM3 release](https://github.com/ACCESS-NRI/ACCESS-OM3/releases)
(`module load access-om3/2026.05.004`). Each page has a single script that sets the
configuration up and runs it with [payu](https://payu.readthedocs.io), and shows the result
of running that script.

| Configuration | What it is | Contributors | Status |
|---|---|---|---|
| [ANU-TUB](anu-tub.md) | 1/4° 40°-wide pole-to-pole sector with a "Drake Passage", wind and buoyancy forcing; a test bed for vertical coordinates | Andy Hogg (`AndyHoggANU`), Angus Gibson (`angus-g`) | tested |
| [ISOMIP+ Ocean0](isomip-plus.md) | Idealised ice-shelf cavity (warm Ocean0 case), sigma-shelf z* coordinate | Claire Yung (`claireyung`) | tested |
| [MOM6 examples](mom6examples.md) | GFDL's test cases from [NOAA-GFDL/MOM6-examples](https://github.com/NOAA-GFDL/MOM6-examples): double gyre, seamount, lock exchange, single columns, global, ... | NOAA-GFDL and the MOM6 community | each tested; see the table there |

!!! note "Tested with Claude Code"
    The run scripts, test results and most of the text in this section were produced with
    [Claude Code](https://claude.com/claude-code) via the scripts in
    [`tested-configs/`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs).
    Every page states exactly which versions were used.
