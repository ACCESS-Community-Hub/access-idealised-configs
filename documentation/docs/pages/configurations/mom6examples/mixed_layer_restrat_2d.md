# mixed_layer_restrat_2d

4 x 80 x 40 cartesian grid, `Z*` coordinate, topography `flat`, wind `zero`, buoyancy `NONE`, 0.416667 days ([upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/mixed_layer_restrat_2d))

Upstream configuration: [`ocean_only/mixed_layer_restrat_2d`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/mixed_layer_restrat_2d) (MOM6-examples commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802)).

!!! info "Workaround used: no restart files"
    This example switches restart files off (`RESTART_CONTROL = -1`). payu 1.3.6 then fails while archiving (`FileNotFoundError: .../work/<name>/RESTART`), because it always moves `work/RESTART` and deletes empty directories first. The run script works around this with a payu `run` userscript that creates `RESTART/` with a placeholder file.

!!! success "Tested: this example runs"
    Ran on Gadi on 2026-11-04 with `access-om3/2026.05.004` (`mom6-solo`) and `payu/1.3.6_1` on 2 Sapphire Rapids core(s); walltime used 00:00:12, 0.01 SU.

!!! note "Generated with Claude Code"
    This page, the script and the figure were generated automatically by [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs) (written with Claude Code). See [How these pages were made](../mom6examples.md#how-these-pages-were-made).

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash mixed_layer_restrat_2d.sh
```

where `mixed_layer_restrat_2d.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "mixed_layer_restrat_2d.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/mixed_layer_restrat_2d.sh"
    ```

## What we got

![mixed_layer_restrat_2d](../../../assets/tested-configs/mixed_layer_restrat_2d.png)

*Left: `temp` vertical section (model levels) at the last output time; right: total energy (`En`) from `ocean.stats.nc`.*

Last lines of `ocean.stats`:

```text
    21,      21.000,     0, En 1.4475727956570332E-04, CFL  0.02818, SL -5.9375E-02, M 6.39905E+15, S 34.0000, T 16.6941, Me -9.92E-19, Se -1.09E-15, Te -1.00E-15
    22,      22.000,     0, En 1.4239224057199508E-04, CFL  0.02822, SL -5.9375E-02, M 6.39905E+15, S 34.0000, T 16.6941, Me -2.40E-18, Se  5.47E-16, Te  8.42E-16
    23,      23.000,     0, En 1.4246033785128486E-04, CFL  0.02819, SL -5.9375E-02, M 6.39905E+15, S 34.0000, T 16.6941, Me -2.67E-19, Se  8.60E-16, Te  8.02E-17
    24,      24.000,     0, En 1.4402539505845065E-04, CFL  0.02810, SL -5.9375E-02, M 6.39905E+15, S 34.0000, T 16.6941, Me -3.82E-20, Se -1.64E-15, Te  1.60E-16
```

Key parameters of this run (from `MOM_parameter_doc.all`):

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `4` |
| `NJGLOBAL` | `80` |
| `NK` | `40` |
| `GRID_CONFIG` | `"cartesian"` |
| `TOPO_CONFIG` | `"flat"` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `"Z*"` |
| `BOUSSINESQ` | `True` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `"LINEAR"` |
| `THICKNESS_CONFIG` | `"rossby_front"` |
| `TS_CONFIG` | `"rossby_front"` |
| `WIND_CONFIG` | `"zero"` |
| `BUOY_CONFIG` | `"NONE"` |
| `ICE_SHELF` | `False` |
| `DT` | `3600.0` |
| `DT_THERM` | `3600.0` |
| `DAYMAX` | `10.0` |
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
| PBS Job Id | `183115939.gadi-pbs` |
| PBS Exit Status | `0` |
| PBS Service Units | `0.01` |
| PBS NCPUs Requested | `2` |
| PBS Walltime Used | `00:00:12` |
| PBS Memory Used | `1.12GB` |

This example needs no input files: grid, bathymetry, initial state and forcing are all set analytically in `MOM_input`.

??? info "Parameters differing from the upstream MOM_parameter_doc.all (17)"
    Comparison of this run's `MOM_parameter_doc.all` with the upstream MOM_parameter_doc.all.
    Differences show where the ACCESS-OM3 MOM6 version adds, drops or changes default parameters.

    | Parameter | reference | this run |
    |---|---|---|
    | `SET_VISC_ANSWER_DATE` | `20260703` | `99991231` |

    New in this run: `ADVECTION_SCHEME_VARIANCE_UNDERFLOW`, `NONBLOCKING_P_SURF_BUG`, `RHO_PGF_REF_BUG`, `USE_FILE_DYES`, `USE_UH_PARTICLES`

    Only upstream: `CDRAG_MAP`, `CONT_USE_H_MARG_MIN`, `DTBT_RESTART_BUG`, `ENSEMBLE_APPENDIX_PREFIX`, `NUM_DIAG_DOWNSAMP_LEV`, `READ_MEAN_SEA_LEVEL`, `REGRID_USE_DEPTH_BASED_TIME_FILTER`, `STOCHASTICS_ANSWER_DATE`, `SYMMETRIC_DOWNSAMPLE_SUMS`, `USE_ADJUST_INTERFACE_MOTION`, `USE_THICKNESS_DIFFUSE_ANN`

??? info "Run-time environment (selected variables from payu's `env.yaml`)"
    | Variable | Value |
    |---|---|
    | `LD_LIBRARY_PATH` | `/apps/openmpi/4.1.7/lib:/apps/openmpi/4.1.7/lib/profilers` |
    | `LOADEDMODULES` | `access3-share/2026.03.002-eale5gm:access-cice/CICE6.6.3-2-huasrvo:access-mocsy/2025.07.002-saj7rvh:access-generic-tracers/2026.09.000-e3zb3ez:access-mom6/2026.05.003-ld7hklz:access-ww3/2026.03.001-bjzidie:access3/2026.03.002-26wbxup:access-om3/2026.05.004:pbs:openmpi/4.1.7` |
    | `OMPI_MCA_orte_tmpdir_base` | `/jobfs/183115939.gadi-pbs` |
    | `PAYU_TELEMETRY_ENV_VERSION` | `1.3.6_1` |
    | `PBS_NCI_NCPUS_PER_NODE` | `104` |
    | `PBS_NCPUS` | `2` |
    | `PBS_QUEUE` | `normalsr-exec` |

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/mixed_layer_restrat_2d (written by mixed_layer_restrat_2d.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 2
    walltime: 00:30:00
    jobname: mixed_layer_restrat_2d
    experiment: mixed_layer_restrat_2d
    laboratory: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab

    model: mom6
    exe: mom6-solo           # found on PATH once the module below is loaded

    userscripts:             # this example writes no restart files
      run: mkdir -p /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab/work/mixed_layer_restrat_2d/RESTART && echo 'no restart files (RESTART_CONTROL = -1)' > /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab/work/mixed_layer_restrat_2d/RESTART/README
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
    | `Initial_state.nc` | 1.38 MB |
    | `Vertical_coordinate.nc` | 0.00 MB |
    | `ocean.stats.nc` | 0.04 MB |
    | `ocean_geometry.nc` | 0.08 MB |
    | `prog.nc` | 21.56 MB |

