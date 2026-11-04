# CVmix_SCM_tests / mech_only / EPBL

!!! success ":white_check_mark: This configuration ran successfully"
    Tested on 2026-11-04 with `access-om3/2026.05.004` (`mom6-solo`): 1 cores, walltime used 00:00:16, 0.01 SU. Details further down this page.


2 x 2 x 400 cartesian grid, `Z*` coordinate, topography `flat`, wind `zero`, buoyancy `zero`, 5 days ([upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/CVmix_SCM_tests/mech_only/EPBL), [README](https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/CVmix_SCM_tests/README.md))

Configuration files: [`ocean_only/CVmix_SCM_tests/mech_only/EPBL`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/CVmix_SCM_tests/mech_only/EPBL) in NOAA-GFDL/MOM6-examples, at commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802): the version this run used. (The model itself is the `mom6-solo` listed under Provenance.)

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash CVmix_SCM_tests-mech_only-EPBL.sh
```

where `CVmix_SCM_tests-mech_only-EPBL.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "CVmix_SCM_tests-mech_only-EPBL.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/CVmix_SCM_tests-mech_only-EPBL.sh"
    ```

## What we got

![CVmix_SCM_tests-mech_only-EPBL](../../../assets/tested-configs/CVmix_SCM_tests-mech_only-EPBL.png)

*Left: `temp` time-depth evolution; right: total energy (`En`) from `ocean.stats.nc`.*

Last lines of `ocean.stats`:

```text
   306,       4.250,     0, En 1.4258435336003221E-27, CFL  0.00000, SL -3.4106E-13, M 1.98264E+16, S 35.0000, T 13.0000, Me  0.00E+00, Se  0.00E+00, Te  0.00E+00
   324,       4.500,     0, En 1.4258435336003221E-27, CFL  0.00000, SL -3.4106E-13, M 1.98264E+16, S 35.0000, T 13.0000, Me  0.00E+00, Se  0.00E+00, Te  0.00E+00
   342,       4.750,     0, En 1.4258435336003221E-27, CFL  0.00000, SL -3.4106E-13, M 1.98264E+16, S 35.0000, T 13.0000, Me  0.00E+00, Se -6.46E-15, Te  0.00E+00
   360,       5.000,     0, En 1.4258435336003221E-27, CFL  0.00000, SL -3.4106E-13, M 1.98264E+16, S 35.0000, T 13.0000, Me  0.00E+00, Se  6.46E-15, Te  0.00E+00
```

## Domain, forcing and output

Made by running the notebook [`explore_run.ipynb`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/blob/main/tested-configs/notebooks/explore_run.ipynb) on this run's output folder (code hidden here). It only plots files MOM6 wrote during the run.

### Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `2` |
| `NJGLOBAL` | `2` |
| `NK` | `400` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `True` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `Z*` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `coord` |
| `TS_CONFIG` | `SCM_CVMix_tests` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `zero` |
| `ICE_SHELF` | `False` |
| `DT` | `1200.0` |
| `DT_THERM` | `1200.0` |
| `DAYMAX` | `5.0` |


### Domain and bottom depth


Grid: 2 x 2 points (`GRID_CONFIG = cartesian`), x from 0.5 to 1.5 degrees_east, y from 28.336 to 29.336 degrees_north. Bottom depth `D` from 400 to 400 m (`TOPO_CONFIG = flat`).



    
![png](../../../assets/tested-configs/notebooks/CVmix_SCM_tests-mech_only-EPBL/notebook_8_1.png)
    


### Initial state


`Temp` from `MOM_IC.nc`, which MOM6 writes with the initial state.



    
![png](../../../assets/tested-configs/notebooks/CVmix_SCM_tests-mech_only-EPBL/notebook_10_1.png)
    


### Surface forcing


Time-mean of the surface forcing saved in the diagnostics: `ustar` (Surface friction velocity = [(gustiness + tau_magnitude)/rho0]^(1/2), from `surffluxes.nc`).



    
![png](../../../assets/tested-configs/notebooks/CVmix_SCM_tests-mech_only-EPBL/notebook_12_1.png)
    


### Energy and stability through the run


    
![png](../../../assets/tested-configs/notebooks/CVmix_SCM_tests-mech_only-EPBL/notebook_14_0.png)
    



From `ocean.stats.nc`: 21 records; time axis in days.


### Final state


`temp` at the last record of `prog_z.nc` (snapshot).



    
![png](../../../assets/tested-configs/notebooks/CVmix_SCM_tests-mech_only-EPBL/notebook_16_1.png)

## Provenance

| What | Value |
|---|---|
| MOM6-examples | [`c1730b8efe16cf7f12fc8db588115cae50f3e802`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802) |
| ACCESS-OM3 module | `access-om3/2026.05.004` |
| MOM6 source code | `ACCESS-NRI/MOM6 2026.05.003 d11a149ccba676d524312328f7eb62560a156dc3` |
| Executable | `/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access-mom6-2026.05.003-ld7hklzo5ajizx5u4yl74i4ijberrpv6/bin/mom6-solo` |
| Executable md5 | `4785d157c76c30d8d01baf7d0f69d218` |
| payu | `1.3.6_1` (module `payu/1.3.6_1`) |
| Date tested | 2026-11-04 |
| PBS Job Id | `183115189.gadi-pbs` |
| PBS Exit Status | `0` |
| PBS Service Units | `0.01` |
| PBS NCPUs Requested | `1` |
| PBS Walltime Used | `00:00:16` |
| PBS Memory Used | `1.13GB` |

This example needs no input files: grid, bathymetry, initial state and forcing are all set analytically in `MOM_input`.

??? info "Parameters differing from the upstream MOM_parameter_doc.all (16)"
    Comparison of this run's `MOM_parameter_doc.all` with the upstream MOM_parameter_doc.all.
    Differences show where the ACCESS-OM3 MOM6 version adds, drops or changes default parameters.

    | Parameter | reference | this run |
    |---|---|---|
    | `SET_VISC_ANSWER_DATE` | `20260703` | `99991231` |

    New in this run: `ADVECTION_SCHEME_VARIANCE_UNDERFLOW`, `NONBLOCKING_P_SURF_BUG`, `RHO_PGF_REF_BUG`, `USE_FILE_DYES`, `USE_UH_PARTICLES`

    Only upstream: `CDRAG_MAP`, `CONT_USE_H_MARG_MIN`, `ENSEMBLE_APPENDIX_PREFIX`, `NUM_DIAG_DOWNSAMP_LEV`, `READ_MEAN_SEA_LEVEL`, `REGRID_USE_DEPTH_BASED_TIME_FILTER`, `STOCHASTICS_ANSWER_DATE`, `SYMMETRIC_DOWNSAMPLE_SUMS`, `USE_ADJUST_INTERFACE_MOTION`, `USE_THICKNESS_DIFFUSE_ANN`

??? info "Run-time environment (selected variables from payu's `env.yaml`)"
    | Variable | Value |
    |---|---|
    | `LD_LIBRARY_PATH` | `/apps/openmpi/4.1.7/lib:/apps/openmpi/4.1.7/lib/profilers` |
    | `LOADEDMODULES` | `access3-share/2026.03.002-eale5gm:access-cice/CICE6.6.3-2-huasrvo:access-mocsy/2025.07.002-saj7rvh:access-generic-tracers/2026.09.000-e3zb3ez:access-mom6/2026.05.003-ld7hklz:access-ww3/2026.03.001-bjzidie:access3/2026.03.002-26wbxup:access-om3/2026.05.004:pbs:openmpi/4.1.7` |
    | `OMPI_MCA_orte_tmpdir_base` | `/jobfs/183115189.gadi-pbs` |
    | `PAYU_TELEMETRY_ENV_VERSION` | `1.3.6_1` |
    | `PBS_NCI_NCPUS_PER_NODE` | `104` |
    | `PBS_NCPUS` | `1` |
    | `PBS_QUEUE` | `normalsr-exec` |

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/CVmix_SCM_tests/mech_only/EPBL (written by CVmix_SCM_tests-mech_only-EPBL.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 1
    walltime: 00:30:00
    jobname: CVmix_SCM_tests-mech_only-EPBL
    experiment: CVmix_SCM_tests-mech_only-EPBL
    laboratory: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab

    model: mom6
    exe: mom6-solo           # found on PATH once the module below is loaded

    modules:
      use:
        - /g/data/vk83/modules
      load:
        - access-om3/2026.05.004

    storage:                 # vk83: executable, ol01: input data
      gdata:
        - vk83
        - ol01

    collate: false           # mom6 writes un-split netCDF files when IO_LAYOUT = 1,1
    runlog: false            # don't commit run logs into the MOM6-examples clone
    metadata:
      enable: false
    ```

??? info "Output files"
    | File | Size |
    |---|---|
    | `MOM_IC.nc` | 0.14 MB |
    | `Vertical_coordinate.nc` | 0.01 MB |
    | `ocean.stats.nc` | 0.28 MB |
    | `ocean_geometry.nc` | 0.02 MB |
    | `prog.nc` | 3.10 MB |
    | `prog_z.nc` | 1.95 MB |
    | `surffluxes.nc` | 0.04 MB |
    | `visc.nc` | 0.41 MB |

