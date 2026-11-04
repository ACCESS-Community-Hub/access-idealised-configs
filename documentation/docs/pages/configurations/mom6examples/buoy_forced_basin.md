# buoy_forced_basin

Buoyancy-forced ("BFB") flat-bottomed basin on a Mercator grid (10°N-60°N, 10 levels).

Upstream configuration: [`ocean_only/buoy_forced_basin`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/buoy_forced_basin) (MOM6-examples commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802)).

!!! warning "Not yet tested"
    This example has not been run yet.

!!! note "Generated with Claude Code"
    This page, the script and the figure were generated automatically by [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs) (written with Claude Code). See [How these pages were made](../mom6examples.md#how-these-pages-were-made).

## Run it yourself

From a Gadi **login node** (membership of `vk83` and `ol01` needed):

```bash
PROJECT=<your-project> bash buoy_forced_basin.sh
```

where `buoy_forced_basin.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "buoy_forced_basin.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/buoy_forced_basin.sh"
    ```

