# global

Global 1° (360 x 210 mosaic grid) ocean with 63 layers, MEKE and tides, forced by data from files.

Upstream configuration: [`ocean_only/global`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global) (MOM6-examples commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802)).

!!! warning "Not yet tested"
    This example has not been run yet.

!!! note "Generated with Claude Code"
    This page, the script and the figure were generated automatically by [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs) (written with Claude Code). See [How these pages were made](../mom6examples.md#how-these-pages-were-made).

## Run it yourself

From a Gadi **login node** (membership of `vk83` and `ol01` needed):

```bash
PROJECT=<your-project> bash global.sh
```

where `global.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "global.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/global.sh"
    ```

