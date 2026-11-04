!!! success "Tested: this configuration runs"
    Ran on Gadi on 2026-11-04 with `access-om3/2026.05.004` (`mom6-solo`) and `payu/1.3.6_1`: 312 cores, walltime used 00:07:57, 82.68 SU.

### What we got

Last lines of `ocean.stats`:

```text
  2016,      28.000,     0, En 2.2046255034558730E-05, CFL  0.00977, SL -3.3249E-10, M 1.98038E+20, S 35.0000, T  5.8743, Me  3.41E-19, Se -1.73E-17, Te -6.68E-18
  2088,      29.000,     0, En 2.2172450632205962E-05, CFL  0.00946, SL -3.3065E-10, M 1.98038E+20, S 35.0000, T  5.8746, Me -2.99E-19, Se  3.83E-17, Te -1.93E-17
  2160,      30.000,     0, En 2.2344876639622647E-05, CFL  0.00971, SL -3.3311E-10, M 1.98038E+20, S 35.0000, T  5.8749, Me  3.26E-19, Se -1.29E-16, Te -9.95E-18
  2232,      31.000,     0, En 2.2542865984382882E-05, CFL  0.00961, SL -3.3188E-10, M 1.98038E+20, S 35.0000, T  5.8752, Me  1.46E-19, Se  4.54E-17, Te -1.56E-17
```

### Domain, forcing and output

Made by running the notebook [`explore_run.ipynb`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/blob/main/tested-configs/notebooks/explore_run.ipynb) on this run's output folder; it only plots files MOM6 wrote during the run. **[See the notebook with its code](notebooks/anu-tub-zstar.md)**.

#### Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `160` |
| `NJGLOBAL` | `800` |
| `NK` | `75` |
| `GRID_CONFIG` | `mercator` |
| `TOPO_CONFIG` | `file` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `ZSTAR` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `WRIGHT` |
| `THICKNESS_CONFIG` | `coord` |
| `TS_CONFIG` | `linear` |
| `WIND_CONFIG` | `file` |
| `BUOY_CONFIG` | `file` |
| `ICE_SHELF` | `False` |
| `DT` | `1200.0` |
| `DT_THERM` | `3600.0` |
| `DAYMAX` | `31.0` |


#### Domain and bottom depth


Grid: 160 x 800 points (`GRID_CONFIG = mercator`), x from 0.125 to 39.875 degrees_east, y from -70.151 to 70.151 degrees_north. Bottom depth `D` from 0 to 4000 m (`TOPO_CONFIG = file`).



    
![png](../../assets/tested-configs/notebooks/anu-tub-zstar/notebook_8_1.png)
    


#### Initial state


`Temp` from `MOM_IC.nc`, which MOM6 writes with the initial state.



    
![png](../../assets/tested-configs/notebooks/anu-tub-zstar/notebook_10_1.png)
    


#### Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = file` and `BUOY_CONFIG = file` (see the MOM6 documentation for these options).


#### Energy and stability through the run


    
![png](../../assets/tested-configs/notebooks/anu-tub-zstar/notebook_14_0.png)
    



From `ocean.stats.nc`: 32 records; time axis in days.


#### Final state


`Temp` at the last record of `MOM_IC.nc` (snapshot).



    
![png](../../assets/tested-configs/notebooks/anu-tub-zstar/notebook_16_1.png)

### Parameters compared with the reference

<span class="chip a">A</span> the file committed in anu-tub (`e413708c`): [`MOM_parameter_doc.all`](https://github.com/ACCESS-Community-Hub/anu-tub/blob/e413708c4b1446e267b42f2f0da95d6ab48ae0e0/docs/MOM_parameter_doc.all)  
<span class="chip b">B</span> this run: `MOM_parameter_doc.all` in the run's output, `/scratch/<your-project>/$USER/mom6/archive/anu-tub-zstar/output000/MOM_parameter_doc.all` when you run the script

**0** parameter values differ; **0** parameters exist only in this run's MOM6 version and **0** only in the reference (new, removed or renamed parameters). Values are compared ignoring quotes, case and number formatting. Parameter names link to a search of the MOM6 source; reference values link to their line on GitHub.

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
    | File | md5 | Comes from |
    |---|---|---|
    | `INPUT/forcing.nc` | `aa75509526935276ef3f5346b3ad15b8` | `anu-tub/input/forcing.nc` |
    | `INPUT/sst.nc` | `3bb095f47357de92d5a8e743e3e1a1f4` | `anu-tub/input/sst.nc` |
    | `INPUT/topog.nc` | `53582824d67e2420f52498cfdff1d593` | `anu-tub/input/topog.nc` |

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
    | File | Size | What it is |
    |---|---|---|
    | `Depth_list.nc` | 0.13 MB | Ocean area and volume as a function of depth, used for the energy diagnostics |
    | `MOM_IC.nc` | 1165.61 MB | Initial state written by MOM6 at the start of the run |
    | `Vertical_coordinate.nc` | 0.00 MB | The vertical coordinate: target values of the layers or levels |
    | `ocean.stats.nc` | 0.09 MB | Domain totals at each energy-save time (energy, mass, heat, salt, maximum CFL); the netCDF form of `ocean.stats` |
    | `ocean_daily.nc` | 63.64 MB | Diagnostics set in `diag_table`: time averages of `zos`, `tos`, `umo_2d`, `vmo_2d`, every 1 days |
    | `ocean_geometry.nc` | 19.56 MB | Static grid: coordinates, cell sizes and areas, bottom depth `D`, Coriolis parameter, land mask |
    | `ocean_month.nc` | 158.77 MB | Diagnostics set in `diag_table`: time averages of `volcello`, `pbo`, `pso`, `thkcello`, `zos`, `thetao`, `tob`, `rhopot2` and 6 more, every 1 months |
    | `ocean_month_rho2.nc` | 71.85 MB | Diagnostics set in `diag_table`: time averages of `volcello`, `thkcello`, `umo`, `vmo`, every 1 months |
    | `ocean_month_z.nc` | 230.73 MB | Diagnostics set in `diag_table`: time averages of `volcello`, `thetao`, `rhopot2`, `agessc`, `uo`, `vo`, every 1 months |
    | `ocean_static.nc` | 12.88 MB | Diagnostics set in `diag_table`: snapshots of `areacello`, `deptho`, `hfgeou`, `sftof`, `Coriolis`, `geolon`, `geolat`, `geolon_c` and 18 more, written once (static) |

