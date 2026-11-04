# benchmark

The MOM6 benchmark case: a 360 x 180 Mercator basin (41°S-41°N, 22 layers) with analytic "benchmark" bathymetry and stratification, gyre winds and linear buoyancy forcing.

Upstream configuration: [`ocean_only/benchmark`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/benchmark) (MOM6-examples commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802)).

!!! warning "Not yet tested"
    This example has not been run yet.

!!! note "Generated with Claude Code"
    This page, the script and the figure were generated automatically by [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs) (written with Claude Code). See [How these pages were made](../mom6examples.md#how-these-pages-were-made).

## Run it yourself

From a Gadi **login node** (membership of `vk83` and `ol01` needed):

```bash
PROJECT=<your-project> bash benchmark.sh
```

where `benchmark.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "benchmark.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/benchmark.sh"
    ```

