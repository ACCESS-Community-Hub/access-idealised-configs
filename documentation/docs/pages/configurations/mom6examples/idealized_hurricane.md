# idealized_hurricane

An idealized (Holland-profile) hurricane moving across an ocean basin.

Upstream configuration: [`ocean_only/idealized_hurricane`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/idealized_hurricane) (MOM6-examples commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802)).

!!! warning "Not yet tested"
    This example has not been run yet.

!!! note "Generated with Claude Code"
    This page, the script and the figure were generated automatically by [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs) (written with Claude Code). See [How these pages were made](../mom6examples.md#how-these-pages-were-made).

## Run it yourself

From a Gadi **login node** (membership of `vk83` and `ol01` needed):

```bash
PROJECT=<your-project> bash idealized_hurricane.sh
```

where `idealized_hurricane.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "idealized_hurricane.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/idealized_hurricane.sh"
    ```

