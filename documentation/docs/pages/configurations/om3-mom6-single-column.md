# ACCESS-OM3 single column (with WOMBAT)

--8<-- "tested-configs/results/om3-mom6-single-column/status.md"

--8<-- "tested-configs/results/om3-mom6-single-column/description.md"

[om3-mom6-single-column](https://github.com/ACCESS-Community-Hub/om3-mom6-single-column) is a
single-column version of ACCESS-OM3, based on the single-column MOM6 configurations in
[`ocean_only/single_column`](https://github.com/NOAA-GFDL/MOM6-examples/tree/dev/gfdl/ocean_only/single_column)
of MOM6-examples. From its [README](https://github.com/ACCESS-Community-Hub/om3-mom6-single-column#readme),
the configurations have been modified to:

- use ACCESS-OM3 MOM6 (with stub ice and wave components);
- include WOMBAT biogeochemistry;
- run with payu;
- use ocean parameters based on those of the ACCESS-OM3 25 km configurations.

The default branch (`jra_ryf+wombatlite`, tested here) uses JRA55-do repeat-year forcing and
WOMBATlite at the BATS site; other branches hold other forcing and WOMBAT variants. The domain
is 2 x 2 cells spanning 1° x 1°, and the repository includes a script to move it to another
location (see its README).

Unlike the other configurations on this website, it runs the **coupled ACCESS-OM3 executable**
(`access-om3-MOM6`, with a data atmosphere and data runoff), not the ocean-only `mom6-solo`.

## The tested run at a glance

--8<-- "tested-configs/results/om3-mom6-single-column/figure.md"

## Run it yourself

From a Gadi **login node** (membership of `vk83` needed):

```bash
PROJECT=<your-project> bash om3-mom6-single-column.sh
```

where `om3-mom6-single-column.sh` is the script below (copy button at the top right). It clones
the repository at the tested commit, makes three small changes to its `config.yaml` (the current
ACCESS-OM3 module instead of `access-om3/2026.03.000`, payu's executable check turned off
because `manifests/exe.yaml` records that older executable, and your project and payu
laboratory), and runs `payu run` for one model year. Output appears in
`/scratch/<your-project>/$USER/access-om3/archive/om3-mom6-single-column/output000/`.

??? example "om3-mom6-single-column.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/om3-mom6-single-column.sh"
    ```

## Tested run

--8<-- "tested-configs/results/om3-mom6-single-column/tested.md"
