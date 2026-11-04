# ISOMIP+ Ocean0 (ice-shelf cavity)

--8<-- "tested-configs/results/isomip-plus-ocean0/status.md"

An idealised ice-shelf cavity configuration in the spirit of the
[ISOMIP+](https://doi.org/10.5194/gmd-9-2471-2016) **Ocean0** (warm) experiment, set up by
[Claire Yung](https://github.com/claireyung) (ANU). It is modified from the MOM6-examples
[`ISOMIP/rho`](https://github.com/NOAA-GFDL/MOM6-examples/tree/dev/gfdl/ocean_only/ISOMIP/rho)
case:

- it uses a symmetric ice-shelf thickness file (`Ocean0_3D_Claire.nc`) and fixes some
  pressure-gradient and initialisation bugs in the original example;
- parameters follow the [ISOMIP+ setup of G. Marques](https://github.com/gustavo-marques/ISOMIP)
  so that it resembles the warm Ocean0 case (the MOM6-examples case is closer to the cold one);
- vertical coordinate: a "sigma-shelf z*" hybrid (36 levels);
- it uses the Holland & Jenkins (1999) melt parameterisation and (non-standard) conductive
  heat flux into the ice shelf;
- domain: 240 x 40 points (2 km), runs for 3 months on 48 cores in about 6 minutes.

The configuration lives on the branch
[`isomip-plus-ocean0-sigmashelfzstar`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/isomip-plus-ocean0-sigmashelfzstar)
of this repository (it may become its own repository). The input file is in
[claireyung/isomip-test-mom6-for-iom3-configs](https://github.com/claireyung/isomip-test-mom6-for-iom3-configs/tree/master/INPUT),
which also has a [plotting notebook](https://github.com/claireyung/isomip-test-mom6-for-iom3-configs/blob/master/plot.ipynb).
To plot in depth coordinates under the ice shelf you need the interface heights `e`.

The configuration was originally run by Claire with her own MOM6 build; here it is run
unchanged with the **released ACCESS-OM3 `mom6-solo` executable**, so nobody needs to
compile MOM6 to use it.

## The tested run at a glance

--8<-- "tested-configs/results/isomip-plus-ocean0/figure.md"

## Run it yourself

From a Gadi **login node** (membership of `vk83` needed):

```bash
PROJECT=<your-project> bash isomip-plus-ocean0.sh
```

where `isomip-plus-ocean0.sh` is the script below (click to expand; copy button
top-right). It clones the configuration and the input file at the tested commits, writes a
payu `config.yaml` that uses the ACCESS-OM3 module, and runs `payu run`. The output appears in
`/scratch/<your-project>/$USER/mom6/archive/isomip-plus-ocean0/output000/`.

??? example "isomip-plus-ocean0.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/isomip-plus-ocean0.sh"
    ```

### How this differs from the branch's own `config.yaml`

The `config.yaml` on the branch points at Claire's own executable and input directory in
`/g/data/x77` (which most people can't read), loads `openmpi/4.1.2` and uses the Cascade
Lake `normal` queue. The script above instead uses:

| | branch `config.yaml` | tested script |
|---|---|---|
| executable | `/g/data/x77/cy8964/.../MOM6` (ninja build) | `mom6-solo` from `access-om3/2026.05.004` |
| input | `/g/data/x77/cy8964/.../INPUT` | `INPUT/` of `claireyung/isomip-test-mom6-for-iom3-configs` (same file, md5 `a9e43676e2c0acbfe1d48ce856d2ff84`) |
| MPI | `mpi: module: openmpi/4.1.2` | provided by the module |
| queue | `normal`, `platform: nodesize: 48` | `normalsr` (the executable is built for Sapphire Rapids) |

Every parameter value in the run matches Claire's original run (see "Parameters
differing" below: only parameter *names* that are new in, or were removed from, the newer
MOM6 appear).

## Tested run

--8<-- "tested-configs/results/isomip-plus-ocean0/tested.md"
