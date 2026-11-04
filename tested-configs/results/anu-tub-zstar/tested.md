!!! success "Tested: this configuration runs"
    Ran on Gadi on 2026-11-04 with `access-om3/2026.05.004` (`mom6-solo`) and `payu/1.3.6_1`: 312 cores, walltime used 00:07:57, 82.68 SU.

### What we got

![anu-tub-zstar](../../assets/tested-configs/anu-tub-zstar.png)

*Left: `zos` at the last output time; right: total energy (`En`) from `ocean.stats.nc`.*

Last lines of `ocean.stats`:

```text
  2016,      28.000,     0, En 2.2046255034558730E-05, CFL  0.00977, SL -3.3249E-10, M 1.98038E+20, S 35.0000, T  5.8743, Me  3.41E-19, Se -1.73E-17, Te -6.68E-18
  2088,      29.000,     0, En 2.2172450632205962E-05, CFL  0.00946, SL -3.3065E-10, M 1.98038E+20, S 35.0000, T  5.8746, Me -2.99E-19, Se  3.83E-17, Te -1.93E-17
  2160,      30.000,     0, En 2.2344876639622647E-05, CFL  0.00971, SL -3.3311E-10, M 1.98038E+20, S 35.0000, T  5.8749, Me  3.26E-19, Se -1.29E-16, Te -9.95E-18
  2232,      31.000,     0, En 2.2542865984382882E-05, CFL  0.00961, SL -3.3188E-10, M 1.98038E+20, S 35.0000, T  5.8752, Me  1.46E-19, Se  4.54E-17, Te -1.56E-17
```

Key parameters of this run (from `MOM_parameter_doc.all`):

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `160` |
| `NJGLOBAL` | `800` |
| `NK` | `75` |
| `GRID_CONFIG` | `"mercator"` |
| `TOPO_CONFIG` | `"file"` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `"ZSTAR"` |
| `BOUSSINESQ` | `True` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `"WRIGHT"` |
| `THICKNESS_CONFIG` | `"coord"` |
| `TS_CONFIG` | `"linear"` |
| `WIND_CONFIG` | `"file"` |
| `BUOY_CONFIG` | `"file"` |
| `ICE_SHELF` | `False` |
| `DT` | `1200.0` |
| `DT_THERM` | `3600.0` |
| `DAYMAX` | `31.0` |
| `TIMEUNIT` | `8.64E+04` |

### Provenance

| What | Value |
|---|---|
| Configuration | [ACCESS-Community-Hub/anu-tub](https://github.com/ACCESS-Community-Hub/anu-tub) `e413708c`, `zstar` coordinate |
| ACCESS-OM3 module | `access-om3/2026.05.004` |
| MOM6 source code | `ACCESS-NRI/MOM6 2026.05.003 d11a149ccba676d524312328f7eb62560a156dc3` |
| Executable | `/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access-mom6-2026.05.003-ld7hklzo5ajizx5u4yl74i4ijberrpv6/bin/mom6-solo` |
| Executable md5 | `4785d157c76c30d8d01baf7d0f69d218` |
| payu | `1.3.6_1` (module `payu/1.3.6_1`) |
| Date tested | 2026-11-04 |
| PBS Job Id | `183114788.gadi-pbs` |
| PBS Exit Status | `0` |
| PBS Service Units | `82.68` |
| PBS NCPUs Requested | `312` |
| PBS Walltime Used | `00:07:57` |
| PBS Memory Used | `90.94GB` |

??? info "Input files and md5 hashes (from payu `manifests/input.yaml`)"
    | File | md5 | Path |
    |---|---|---|
    | `INPUT/forcing.nc` | `aa75509526935276ef3f5346b3ad15b8` | `/g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/anu-tub/input/forcing.nc` |
    | `INPUT/sst.nc` | `3bb095f47357de92d5a8e743e3e1a1f4` | `/g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/anu-tub/input/sst.nc` |
    | `INPUT/topog.nc` | `53582824d67e2420f52498cfdff1d593` | `/g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/anu-tub/input/topog.nc` |

??? info "Parameters differing from the `docs/MOM_parameter_doc.all` committed in anu-tub (0)"
    Comparison of this run's `MOM_parameter_doc.all` with the `docs/MOM_parameter_doc.all` committed in anu-tub.
    Differences show where the ACCESS-OM3 MOM6 version adds, drops or changes default parameters.

??? info "Run-time environment (selected variables from payu's `env.yaml`)"
    | Variable | Value |
    |---|---|
    | `LD_LIBRARY_PATH` | `/apps/openmpi/4.1.7/lib:/apps/openmpi/4.1.7/lib/profilers` |
    | `LOADEDMODULES` | `access3-share/2026.03.002-eale5gm:access-cice/CICE6.6.3-2-huasrvo:access-mocsy/2025.07.002-saj7rvh:access-generic-tracers/2026.09.000-e3zb3ez:access-mom6/2026.05.003-ld7hklz:access-ww3/2026.03.001-bjzidie:access3/2026.03.002-26wbxup:access-om3/2026.05.004:pbs:openmpi/4.1.7` |
    | `OMPI_MCA_orte_tmpdir_base` | `/jobfs/183114788.gadi-pbs` |
    | `PAYU_TELEMETRY_ENV_VERSION` | `1.3.6_1` |
    | `PBS_NCI_NCPUS_PER_NODE` | `104` |
    | `PBS_NCPUS` | `312` |
    | `PBS_QUEUE` | `normalsr-exec` |

??? info "payu config.yaml written by the script"
    ```yaml
    # Payu configuration

    # If submitting to a different project to your default, uncomment line below
    # and change project code as appropriate; also set shortpath below
    project: tm70
    # Force payu to always find, and save, files in this scratch project directory
    # shortpath: /scratch/<project>

    modules:
      use:
        - /g/data/vk83/modules
      load:
        - access-om3/2026.05.004

    queue: normalsr
    ncpus: 312
    walltime: 01:00:00
    jobname: anu-tub-zstar
    experiment: anu-tub-zstar
    laboratory: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab

    model: mom6
    exe: mom6-solo
    input:
      # Inputs can be created using the notebook in ./input
      - ./input/topog.nc
      - ./input/forcing.nc
      - ./input/sst.nc

    runlog: false
    metadata:
      enable: false
    manifest:
      reproduce:
        exe: false   # manifests/exe.yaml records the pre-release exe

    collate: false

    qsub_flags: -W umask=027

    restart_freq: 1
    ```

??? info "Output files"
    | File | Size |
    |---|---|
    | `Depth_list.nc` | 0.13 MB |
    | `MOM_IC.nc` | 1165.61 MB |
    | `Vertical_coordinate.nc` | 0.00 MB |
    | `ocean.stats.nc` | 0.09 MB |
    | `ocean_daily.nc` | 63.64 MB |
    | `ocean_geometry.nc` | 19.56 MB |
    | `ocean_month.nc` | 158.77 MB |
    | `ocean_month_rho2.nc` | 71.85 MB |
    | `ocean_month_z.nc` | 230.73 MB |
    | `ocean_static.nc` | 12.88 MB |

