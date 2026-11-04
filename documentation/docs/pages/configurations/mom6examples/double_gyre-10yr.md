# double_gyre / 10yr

Variant of `double_gyre` with `DAYMAX=3650.0`. Wind-driven, adiabatic two-layer-style double gyre in a 22° x 20° spherical box (30°N-50°N) with "spoon" bathymetry. A classic test bed for western boundary currents (think Gulf Stream/East Australian Current) and their separation.

This is a copy of [double_gyre](double_gyre.md) with these lines added to `MOM_override`, e.g. to run long enough to see a spun-up state:

```text
#override DAYMAX = 3650.0
```

Upstream configuration: [`ocean_only/double_gyre`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/double_gyre) (MOM6-examples commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802)).

!!! warning "Not yet tested"
    This example has not been run yet.

!!! note "Generated with Claude Code"
    This page, the script and the figure were generated automatically by [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs) (written with Claude Code). See [How these pages were made](../mom6examples.md#how-these-pages-were-made).

## Run it yourself

From a Gadi **login node** (membership of `vk83` and `ol01` needed):

```bash
PROJECT=<your-project> bash double_gyre-10yr.sh
```

where `double_gyre-10yr.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "double_gyre-10yr.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/double_gyre-10yr.sh"
    ```

