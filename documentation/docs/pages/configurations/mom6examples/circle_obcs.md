# circle_obcs

Open-boundary-condition test: a circular anomaly in a 25 x 25 flat box with four open boundary segments.

Upstream configuration: [`ocean_only/circle_obcs`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/circle_obcs) (MOM6-examples commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802)).

!!! success "Tested: this example runs"
    Ran on Gadi on 2026-11-04 with `access-om3/2026.05.004` (`mom6-solo`) and `payu/1.3.6_1` on 2 Sapphire Rapids core(s); walltime used 00:00:12, 0.01 SU.

!!! note "Generated with Claude Code"
    This page, the script and the figure were generated automatically by [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs) (written with Claude Code). See [How these pages were made](../mom6examples.md#how-these-pages-were-made).

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash circle_obcs.sh
```

where `circle_obcs.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "circle_obcs.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/circle_obcs.sh"
    ```

## What we got

![circle_obcs](../../../assets/tested-configs/circle_obcs.png)

*Left: sea-surface height (`e`, top interface) at the last output time; right: total energy (`En`) from `ocean.stats.nc`.*

Last lines of `ocean.stats`:

```text
    15,       0.500,     0, En 5.0615661833781763E-03, CFL  0.00323, SL -8.5100E-02, Mass 6.18512E+15, Me  4.34E-03
    30,       1.000,     0, En 4.4003105693290996E-03, CFL  0.00686, SL  5.7894E-03, Mass 6.18606E+15, Me  1.51E-04
    45,       1.500,     0, En 4.3803641547071337E-03, CFL  0.00926, SL  4.5783E-03, Mass 6.18605E+15, Me -2.02E-06
    60,       2.000,     0, En 4.3567986453925392E-03, CFL  0.01050, SL  4.2954E-03, Mass 6.18604E+15, Me -4.72E-07
```

Key parameters of this run (from `MOM_parameter_doc.all`):

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `25` |
| `NJGLOBAL` | `25` |
| `NK` | `10` |
| `GRID_CONFIG` | `"cartesian"` |
| `TOPO_CONFIG` | `"flat"` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `False` |
| `BOUSSINESQ` | `True` |
| `ENABLE_THERMODYNAMICS` | `False` |
| `THICKNESS_CONFIG` | `"circle_obcs"` |
| `WIND_CONFIG` | `"zero"` |
| `BUOY_CONFIG` | `"zero"` |
| `ICE_SHELF` | `False` |
| `DT` | `120.0` |
| `DT_THERM` | `120.0` |
| `DAYMAX` | `2.0` |
| `TIMEUNIT` | `3600.0` |

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
| PBS Job Id | `183114905.gadi-pbs` |
| PBS Exit Status | `0` |
| PBS Service Units | `0.01` |
| PBS NCPUs Requested | `2` |
| PBS Walltime Used | `00:00:12` |
| PBS Memory Used | `1.14GB` |

This example needs no input files: grid, bathymetry, initial state and forcing are all set analytically in `MOM_input`.

??? info "Parameters differing from the upstream MOM_parameter_doc.all (33)"
    Comparison of this run's `MOM_parameter_doc.all` with the upstream MOM_parameter_doc.all.
    Differences show where the ACCESS-OM3 MOM6 version adds, drops or changes default parameters.

    | Parameter | reference | this run |
    |---|---|---|
    | `SET_VISC_ANSWER_DATE` | `20260703` | `99991231` |

    New in this run: `ADVECTION_SCHEME_VARIANCE_UNDERFLOW`, `OBC_COMPUTED_STRAIN`, `OBC_COMPUTED_VORTICITY`, `OBC_FREESLIP_STRAIN`, `OBC_FREESLIP_VORTICITY`, `OBC_SPECIFIED_STRAIN`, `OBC_SPECIFIED_VORTICITY`, `OBC_ZERO_STRAIN`, `OBC_ZERO_VORTICITY`, `RHO_PGF_REF_BUG`, `USE_FILE_DYES`, `USE_FILE_OBC`, `USE_UH_PARTICLES`

    Only upstream: `CDRAG_MAP`, `CONT_USE_H_MARG_MIN`, `DTBT_RESTART_BUG`, `DT_OBC_SEG_UPDATE_OBGC`, `ENSEMBLE_APPENDIX_PREFIX`, `IGNORE_DT_OBC_SEG_UPDATE_OBGC`, `NUM_DIAG_DOWNSAMP_LEV`, `OBC_BGC_TIME_REF_BUG`, `OBC_SPECIFIED_STRAIN_BUG`, `OBC_STRAIN_CONFIG`, `OBC_TEMP_SALT_NEEDED_BUG`, `OBC_TRACER_DZ_BUG`, `OBC_TS_RESERVOIR_INIT_BUG`, `OBC_VALUE_UPDATE_BUG`, `OBC_VORTICITY_CONFIG`, `READ_MEAN_SEA_LEVEL`, `STOCHASTICS_ANSWER_DATE`, `SYMMETRIC_DOWNSAMPLE_SUMS`, `USE_THICKNESS_DIFFUSE_ANN`

??? info "Run-time environment (selected variables from payu's `env.yaml`)"
    | Variable | Value |
    |---|---|
    | `LD_LIBRARY_PATH` | `/apps/openmpi/4.1.7/lib:/apps/openmpi/4.1.7/lib/profilers` |
    | `LOADEDMODULES` | `access3-share/2026.03.002-eale5gm:access-cice/CICE6.6.3-2-huasrvo:access-mocsy/2025.07.002-saj7rvh:access-generic-tracers/2026.09.000-e3zb3ez:access-mom6/2026.05.003-ld7hklz:access-ww3/2026.03.001-bjzidie:access3/2026.03.002-26wbxup:access-om3/2026.05.004:pbs:openmpi/4.1.7` |
    | `OMPI_MCA_orte_tmpdir_base` | `/jobfs/183114905.gadi-pbs` |
    | `PAYU_TELEMETRY_ENV_VERSION` | `1.3.6_1` |
    | `PBS_NCI_NCPUS_PER_NODE` | `104` |
    | `PBS_NCPUS` | `2` |
    | `PBS_QUEUE` | `normalsr-exec` |

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/circle_obcs (written by circle_obcs.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 2
    walltime: 00:30:00
    jobname: circle_obcs
    experiment: circle_obcs
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
    | `GOLD_IC.nc` | 1.33 MB |
    | `Vertical_coordinate.nc` | 0.00 MB |
    | `ocean.stats.nc` | 0.00 MB |
    | `ocean_geometry.nc` | 0.12 MB |
    | `prog.nc` | 7.79 MB |

