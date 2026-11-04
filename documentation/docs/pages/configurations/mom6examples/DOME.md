# DOME

!!! success ":white_check_mark: This configuration ran successfully"
    Tested on 2026-11-04 with `access-om3/2026.05.004` (`mom6-solo`): 6 cores, walltime used 00:00:19, 0.06 SU. Details further down this page.


150 x 70 x 25 cartesian grid, layer mode (no regridding), topography `DOME`, wind `zero`, buoyancy `zero`, 2 days ([upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/DOME))

Configuration files: [`ocean_only/DOME`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/DOME) in NOAA-GFDL/MOM6-examples, at commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802): the version this run used. (The model itself is the `mom6-solo` listed under Provenance.)

!!! warning "Known issue"
    Not a failure: the run is fine, but its `diag_table` writes diagnostics every 5 days while the example runs for only 2 days (`DAYMAX = 2`), so the output files hold one empty record and only the energy time series can be plotted. Increase `DAYMAX` (or the output frequency) to see the overflow.

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash DOME.sh
```

where `DOME.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "DOME.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/DOME.sh"
    ```

## What we got

![DOME](../../../assets/tested-configs/DOME.png)

*Left: no suitable diagnostic; right: total energy (`En`) from `ocean.stats.nc`.*

Last lines of `ocean.stats`:

```text
            [days]                 [m2 s-2]           [Nondim]        [m]             [kg]           [Nondim]
     0,       0.000,     0, En 8.2935908164461674E-13, CFL  0.00000, SL  0.0000E+00, Mass 2.65070E+18, Me  0.00E+00
    72,       1.000,     0, En 6.1856781647926734E-03, CFL  0.27483, SL  8.3525E-01, Mass 2.65148E+18, Me  2.96E-04
   144,       2.000,     0, En 1.0794704149043441E-02, CFL  0.25261, SL  1.6705E+00, Mass 2.65227E+18, Me  2.95E-04
```

## Domain, forcing and output

Made by running the notebook [`explore_run.ipynb`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/blob/main/tested-configs/notebooks/explore_run.ipynb) on this run's output folder (code hidden here). It only plots files MOM6 wrote during the run.

### Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `150` |
| `NJGLOBAL` | `70` |
| `NK` | `25` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `DOME` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `False` |
| `ENABLE_THERMODYNAMICS` | `False` |
| `THICKNESS_CONFIG` | `DOME` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `zero` |
| `ICE_SHELF` | `False` |
| `DT` | `1200.0` |
| `DT_THERM` | `3600.0` |
| `DAYMAX` | `2.0` |


### Domain and bottom depth


Grid: 150 x 70 points (`GRID_CONFIG = cartesian`), x from 5 to 1495 kilometers, y from 5 to 695 kilometers. Bottom depth `D` from 0.5 to 3600 m (`TOPO_CONFIG = DOME`).



    
![png](../../../assets/tested-configs/notebooks/DOME/notebook_8_1.png)
    


### Initial state


MOM6 did not write an initial-state file for this run (it does when `SAVE_INITIAL_CONDS = True`), so the initial state is not shown here; see the run's `MOM_parameter_doc.all` (`THICKNESS_CONFIG = DOME`, `TS_CONFIG = n/a`).


### Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = zero` (see the MOM6 documentation for these options).


### Energy and stability through the run


    
![png](../../../assets/tested-configs/notebooks/DOME/notebook_14_0.png)
    



From `ocean.stats.nc`: 3 records; time axis in days.


### Final state


No diagnostic output with a varying field was written for this run.

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
| PBS Job Id | `183114888.gadi-pbs` |
| PBS Exit Status | `0` |
| PBS Service Units | `0.06` |
| PBS NCPUs Requested | `6` |
| PBS Walltime Used | `00:00:19` |
| PBS Memory Used | `1.75GB` |

This example needs no input files: grid, bathymetry, initial state and forcing are all set analytically in `MOM_input`.

??? info "Parameters differing from the upstream MOM_parameter_doc.all (34)"
    Comparison of this run's `MOM_parameter_doc.all` with the upstream MOM_parameter_doc.all.
    Differences show where the ACCESS-OM3 MOM6 version adds, drops or changes default parameters.

    | Parameter | reference | this run |
    |---|---|---|
    | `SET_VISC_ANSWER_DATE` | `20260703` | `99991231` |

    New in this run: `ADVECTION_SCHEME_VARIANCE_UNDERFLOW`, `OBC_COMPUTED_STRAIN`, `OBC_COMPUTED_VORTICITY`, `OBC_FREESLIP_STRAIN`, `OBC_FREESLIP_VORTICITY`, `OBC_SPECIFIED_STRAIN`, `OBC_SPECIFIED_VORTICITY`, `OBC_ZERO_STRAIN`, `OBC_ZERO_VORTICITY`, `USE_FILE_DYES`, `USE_FILE_OBC`, `USE_UH_PARTICLES`

    Only upstream: `CDRAG_MAP`, `CONT_USE_H_MARG_MIN`, `DTBT_RESTART_BUG`, `DT_OBC_SEG_UPDATE_OBGC`, `ENSEMBLE_APPENDIX_PREFIX`, `IGNORE_DT_OBC_SEG_UPDATE_OBGC`, `NUM_DIAG_DOWNSAMP_LEV`, `OBC_BGC_TIME_REF_BUG`, `OBC_SPECIFIED_STRAIN_BUG`, `OBC_STRAIN_CONFIG`, `OBC_TEMP_SALT_NEEDED_BUG`, `OBC_TRACER_DZ_BUG`, `OBC_TRACER_RESERVOIR_LENGTH_SCALE_IN`, `OBC_TRACER_RESERVOIR_LENGTH_SCALE_OUT`, `OBC_TS_RESERVOIR_INIT_BUG`, `OBC_VALUE_UPDATE_BUG`, `OBC_VORTICITY_CONFIG`, `READ_MEAN_SEA_LEVEL`, `STOCHASTICS_ANSWER_DATE`, `SYMMETRIC_DOWNSAMPLE_SUMS`, `USE_THICKNESS_DIFFUSE_ANN`

??? info "Run-time environment (selected variables from payu's `env.yaml`)"
    | Variable | Value |
    |---|---|
    | `LD_LIBRARY_PATH` | `/apps/openmpi/4.1.7/lib:/apps/openmpi/4.1.7/lib/profilers` |
    | `LOADEDMODULES` | `access3-share/2026.03.002-eale5gm:access-cice/CICE6.6.3-2-huasrvo:access-mocsy/2025.07.002-saj7rvh:access-generic-tracers/2026.09.000-e3zb3ez:access-mom6/2026.05.003-ld7hklz:access-ww3/2026.03.001-bjzidie:access3/2026.03.002-26wbxup:access-om3/2026.05.004:pbs:openmpi/4.1.7` |
    | `OMPI_MCA_orte_tmpdir_base` | `/jobfs/183114888.gadi-pbs` |
    | `PAYU_TELEMETRY_ENV_VERSION` | `1.3.6_1` |
    | `PBS_NCI_NCPUS_PER_NODE` | `104` |
    | `PBS_NCPUS` | `6` |
    | `PBS_QUEUE` | `normalsr-exec` |

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/DOME (written by DOME.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 6
    walltime: 00:30:00
    jobname: DOME
    experiment: DOME
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
    | `Vertical_coordinate.nc` | 0.00 MB |
    | `ave_prog__0001_003.nc` | 5.34 MB |
    | `cont__0001_003.nc` | 2.15 MB |
    | `ocean.stats.nc` | 0.00 MB |
    | `ocean_geometry.nc` | 1.63 MB |
    | `prog__0001_003.nc` | 6.39 MB |

