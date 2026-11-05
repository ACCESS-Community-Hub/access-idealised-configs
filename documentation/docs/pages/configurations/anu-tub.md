# ANU-TUB, an idealised sector model

--8<-- "tested-configs/results/anu-tub-zstar/status.md"

--8<-- "tested-configs/results/anu-tub-zstar/description.md"

[ANU-TUB](https://github.com/ACCESS-Community-Hub/anu-tub) is a MOM6 configuration that aims to

> produce the simplest configuration that incorporates buoyancy and wind forcing, gyre
> circulation, overturning circulation and topographically-constrained overflow.

It was set up by [Andy Hogg](https://github.com/AndyHoggANU) and
[Angus Gibson](https://github.com/angus-g) to explore vertical-coordinate choices in MOM6,
which uses [generalised vertical coordinates](https://mom6.readthedocs.io/en/dev-gfdl/api/generated/pages/General_Coordinate.html)
and so puts that choice in the user's hands. From the repository
[README](https://github.com/ACCESS-Community-Hub/anu-tub#anu-tub):

- The sector is 40° wide, and goes from ~70.3°S to ~70.3°N.
- It has a 1/4° nominal resolution and a Mercator grid refinement.
- The default vertical coordinate is z* with 75 vertical levels.
- The bathymetry is simple, with a vertical wall to the north, an "Antarctic shelf and
  slope" in the south and sloping sidewalls on the east and west.
- The domain is periodic in the east-west direction, allowing zonal flow in a narrow
  "Drake Passage" between ~65°S and ~52°S.
- Surface momentum forcing is a prescribed zonal wind that is constant in time but varies
  with latitude.
- Thermal forcing is restoring to a latitude-dependent SST profile. There is (currently) no
  freshwater forcing, so salinity is constant.
- It uses the WRIGHT equation of state, without frazil formation or sea ice.
- It includes the PBL surface boundary-layer scheme with a constant background diffusivity
  of $2 \times 10^{-5}$ m$^{2}$ s$^{-1}$.
- The MEKE eddy parameterisation and the mixed-layer restratification scheme are off.

The model has $160 \times 800$ grid points and a $6 \times 52$ tile layout, so it runs on
312 cores (three Sapphire Rapids nodes). With a 1200 s timestep, the z* case takes about
1:20 hours per model year (~18 years/day) and uses ~800 SU per model year.

The script and results below use the **released** ACCESS-OM3 `mom6-solo` executable rather
than the pre-release one named in the repository.

## The tested run at a glance

--8<-- "tested-configs/results/anu-tub-zstar/figure.md"

## Run it yourself

You need to be a member of NCI project `vk83` (ACCESS-NRI software,
[join here](https://my.nci.org.au/mancini/project/vk83/join)) and of the project you
charge the run to. Then, from a Gadi **login node**:

```bash
PROJECT=<your-project> bash anu-tub.sh                 # one model year (12 months), as in the repository
PROJECT=<your-project> MONTHS=1 WALLTIME=1:00:00 bash anu-tub.sh   # a quick 1-month test (what we ran)
COORD=adapt PROJECT=<your-project> bash anu-tub.sh     # the adaptive-coordinate variant
```

where `anu-tub.sh` is the script below (click to expand; copy button top-right). It:

1. clones anu-tub at the tested commit (to `/g/data/<project>/$USER/anu-tub` by default);
2. creates the three input files (`topog.nc`, `forcing.nc`, `sst.nc`) by running the
   repository's own notebook `input/mom6-anu-tub-driver.ipynb` as a script. No input
   files need to be copied from anywhere;
3. chooses the vertical coordinate by pointing the `MOM_override` symlink at
   `zstar/`, `adapt/` or `hycom1/`;
4. edits `config.yaml` (project, released module, laboratory, walltime) and runs `payu run`.

The run starts from rest with the initial state set in `MOM_input`, so **no restart files
are needed**. Output goes to `/scratch/<project>/$USER/mom6/archive/anu-tub-<coord>/`.
Scratch files are deleted after a period without use, so copy anything you want to keep to
`/g/data`. To continue the run, just run `payu run` again in the anu-tub directory: payu
picks up the latest restart automatically.

??? example "anu-tub.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/anu-tub.sh"
    ```

!!! warning "Things we found while testing (suggested README fixes)"
    - `config.yaml` sets `manifest: reproduce: exe: true` and `manifests/exe.yaml` records
      the pre-release executable (`access-om3/pr140-7`). If you use a different executable
      (such as the released `access-om3/2026.05.004`), payu stops with
      `Run cannot reproduce: manifest manifests/exe.yaml is not correct`. Set
      `exe: false` under `manifest: reproduce:` (the script does this), or update the
      manifest.
    - The `hycom1` coordinate reads `hycom1_75_800m.nc`, which the notebook does not
      create, so `COORD=hycom1` will not run out of the box.
    - The pre-release module `access-om3/pr140-7` in `config.yaml` can be swapped for the
      released `access-om3/2026.05.004` (which now ships `mom6-solo`).

## Changing the experiment

- **Diagnostics**: edit `diag_table`; see
  [MOM6 run-time diagnostics](https://mom6.readthedocs.io/en/main/api/generated/pages/Diagnostics.html).
- **Run length** per submission: `months`/`days` in the `ocean_solo_nml` section of
  `input.nml` (the script's `MONTHS` variable sets `months`). Leave the rest of
  `input.nml` alone unless you know what you are doing.
- **Your own MOM6 code**: build your own `mom6-solo` (see
  [Building MOM6](../infrastructure/Building.md)) and set `exe:` in `config.yaml` to
  its full path. With `reproduce: exe: false`, payu uses whatever executable is at that
  path when you next run `payu run`, so rebuilding is enough to pick up code changes.
  (Not yet tested here: whether you still need the `modules:` block with your own build.)

## Tested run

--8<-- "tested-configs/results/anu-tub-zstar/tested.md"

## Other resources

- [MOM6 documentation](https://mom6.readthedocs.io/en/main/)
- [Running ACCESS models with `payu`](https://docs.access-hive.org.au/models/run_a_model/run_access-om3/)
