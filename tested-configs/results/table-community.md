<div class="config-table" markdown>

| Configuration | Tags | Status | Cores | Prerequisites | Description |
|---|---|---|---|---|---|
| [ANU-TUB](anu-tub.md) | <span class="cfg-tag">Basin</span> <span class="cfg-tag">Coordinates</span> | :white_check_mark: ran | 312 | `vk83`, `xp65` (the script makes the input files with `conda/analysis3`) | "A bathtub-sector ocean configuration for MOM6 ... designed primarily as a test case for implementing new vertical coordinate systems into MOM6" ([README](https://github.com/ACCESS-Community-Hub/anu-tub#anu-tub)). By Andy Hogg and Angus Gibson. Tested set-up: 160 x 800 x 75 mercator grid, `ZSTAR` coordinate, topography `file`, wind `file`, buoyancy `file`, 31 days. |
| [ISOMIP+ Ocean0](isomip-plus.md) | <span class="cfg-tag">Ice shelf</span> | :white_check_mark: ran | 48 | `vk83`; the input file comes from Claire Yung's input repository (the script clones it) | "Idealised ISOMIP+ like config" that "resembles the Ocean0 warm test case" ([README](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/isomip-plus-ocean0-sigmashelfzstar#readme)). By Claire Yung. Tested set-up: 240 x 40 x 36 cartesian grid, `SIGMA_SHELF_ZSTAR` coordinate, topography `ISOMIP`, wind `zero`, buoyancy `NONE`, ice shelf, 90 days. |

</div>
