# circle_obcs

Open-boundary-condition test: a circular anomaly in a 25 x 25 flat box with four open boundary segments.

Upstream configuration: [`ocean_only/circle_obcs`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/circle_obcs) (MOM6-examples commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802)).

!!! warning "Not yet tested"
    This example has not been run yet.

!!! note "Generated with Claude Code"
    This page, the script and the figure were generated automatically by [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs) (written with Claude Code). See [How these pages were made](../mom6examples.md#how-these-pages-were-made).

## Run it yourself

From a Gadi **login node** (membership of `vk83` and `ol01` needed):

```bash
PROJECT=<your-project> bash circle_obcs.sh
```

where `circle_obcs.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "circle_obcs.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/circle_obcs.sh"
    ```

