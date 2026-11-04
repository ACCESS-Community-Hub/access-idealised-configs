# seamount / layer

Stratified ocean at rest over a seamount; spurious currents measure pressure-gradient errors (layered coordinates).

Upstream configuration: [`ocean_only/seamount/layer`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/seamount/layer) (MOM6-examples commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802)).

!!! success "Tested: this example runs"
    Ran on Gadi on 2026-11-04 with `access-om3/2026.05.004` (`mom6-solo`) and `payu/1.3.6_1` on 2 Sapphire Rapids core(s); walltime used 00:00:19, 0.02 SU.

!!! note "Generated with Claude Code"
    This page, the script and the figure were generated automatically by [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs) (written with Claude Code). See [How these pages were made](../mom6examples.md#how-these-pages-were-made).

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash seamount-layer.sh
```

where `seamount-layer.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "seamount-layer.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/seamount-layer.sh"
    ```

## What we got

![seamount-layer](../../../assets/tested-configs/seamount-layer.png)

*Left: `salt` vertical section (model levels) at the last output time; right: total energy (`En`) from `ocean.stats.nc`.*

Last lines of `ocean.stats`:

```text
   192,       2.000,     0, En 8.7894793127269044E-14, CFL  0.00000, SL -4.5475E-13, M 7.54620E+15, S 34.9374, T  0.0000, Me -5.53E-18, Se -5.23E-15, Te  0.00E+00
   288,       3.000,     0, En 8.7894037204077209E-14, CFL  0.00000, SL -4.5475E-13, M 7.54620E+15, S 34.9374, T  0.0000, Me -1.09E-17, Se -3.91E-15, Te  0.00E+00
   384,       4.000,     0, En 8.7894793127289819E-14, CFL  0.00000, SL -4.5475E-13, M 7.54620E+15, S 34.9374, T  0.0000, Me  1.46E-17, Se -8.15E-15, Te  0.00E+00
   480,       5.000,     0, En 8.7894037204094274E-14, CFL  0.00000, SL -4.5475E-13, M 7.54620E+15, S 34.9374, T  0.0000, Me  3.43E-18, Se -8.22E-15, Te  0.00E+00
```

Key parameters of this run (from `MOM_parameter_doc.all`):

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `40` |
| `NJGLOBAL` | `2` |
| `NK` | `20` |
| `GRID_CONFIG` | `"cartesian"` |
| `TOPO_CONFIG` | `"seamount"` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `False` |
| `BOUSSINESQ` | `True` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `"LINEAR"` |
| `THICKNESS_CONFIG` | `"seamount"` |
| `TS_CONFIG` | `"seamount"` |
| `WIND_CONFIG` | `"zero"` |
| `BUOY_CONFIG` | `"NONE"` |
| `ICE_SHELF` | `False` |
| `DT` | `900.0` |
| `DT_THERM` | `900.0` |
| `DAYMAX` | `5.0` |
| `TIMEUNIT` | `8.64E+04` |

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
| PBS Job Id | `183115012.gadi-pbs` |
| PBS Exit Status | `0` |
| PBS Service Units | `0.02` |
| PBS NCPUs Requested | `2` |
| PBS Walltime Used | `00:00:19` |
| PBS Memory Used | `1.13GB` |

This example needs no input files: grid, bathymetry, initial state and forcing are all set analytically in `MOM_input`.

??? info "Parameters differing from the upstream MOM_parameter_doc.all (14)"
    Comparison of this run's `MOM_parameter_doc.all` with the upstream MOM_parameter_doc.all.
    Differences show where the ACCESS-OM3 MOM6 version adds, drops or changes default parameters.

    | Parameter | reference | this run |
    |---|---|---|
    | `SET_VISC_ANSWER_DATE` | `20260703` | `99991231` |

    New in this run: `ADVECTION_SCHEME_VARIANCE_UNDERFLOW`, `NONBLOCKING_P_SURF_BUG`, `RHO_PGF_REF_BUG`, `USE_FILE_DYES`, `USE_UH_PARTICLES`

    Only upstream: `CDRAG_MAP`, `CONT_USE_H_MARG_MIN`, `ENSEMBLE_APPENDIX_PREFIX`, `NUM_DIAG_DOWNSAMP_LEV`, `READ_MEAN_SEA_LEVEL`, `STOCHASTICS_ANSWER_DATE`, `SYMMETRIC_DOWNSAMPLE_SUMS`, `USE_THICKNESS_DIFFUSE_ANN`

??? info "Run-time environment (selected variables from payu's `env.yaml`)"
    | Variable | Value |
    |---|---|
    | `LD_LIBRARY_PATH` | `/apps/openmpi/4.1.7/lib:/apps/openmpi/4.1.7/lib/profilers` |
    | `LOADEDMODULES` | `access3-share/2026.03.002-eale5gm:access-cice/CICE6.6.3-2-huasrvo:access-mocsy/2025.07.002-saj7rvh:access-generic-tracers/2026.09.000-e3zb3ez:access-mom6/2026.05.003-ld7hklz:access-ww3/2026.03.001-bjzidie:access3/2026.03.002-26wbxup:access-om3/2026.05.004:pbs:openmpi/4.1.7` |
    | `OMPI_MCA_orte_tmpdir_base` | `/jobfs/183115012.gadi-pbs` |
    | `PAYU_TELEMETRY_ENV_VERSION` | `1.3.6_1` |
    | `PBS_NCI_NCPUS_PER_NODE` | `104` |
    | `PBS_NCPUS` | `2` |
    | `PBS_QUEUE` | `normalsr-exec` |

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/seamount/layer (written by seamount-layer.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 2
    walltime: 00:30:00
    jobname: seamount-layer
    experiment: seamount-layer
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
    | `Initial_state.nc` | 0.21 MB |
    | `Vertical_coordinate.nc` | 0.00 MB |
    | `ocean.stats.nc` | 0.01 MB |
    | `ocean_geometry.nc` | 0.04 MB |
    | `prog.nc` | 5.84 MB |

