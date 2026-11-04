!!! success "Tested: this configuration runs"
    Ran on Gadi on 2026-11-04 with `access-om3/2026.05.004` (`mom6-solo`) and `payu/1.3.6_1`: 48 cores, walltime used 00:05:44, 9.17 SU.

### What we got

Last lines of `ocean.stats`:

```text
 10755,      89.625,     0, En 2.6752921586712817E-04, CFL  0.09251, SL  0.0000E+00, M 1.33984E+16, S 34.2592, T -0.3998, Me -1.07E-14, Se  3.34E-05, Te  1.04E-04
 10770,      89.750,     0, En 2.6781129850780042E-04, CFL  0.09251, SL  0.0000E+00, M 1.33984E+16, S 34.2592, T -0.3998, Me -1.07E-14, Se  3.34E-05, Te  1.04E-04
 10785,      89.875,     0, En 2.6810178334436098E-04, CFL  0.09253, SL  0.0000E+00, M 1.33984E+16, S 34.2592, T -0.3998, Me -1.07E-14, Se  3.33E-05, Te  1.04E-04
 10800,      90.000,     0, En 2.6839108612804527E-04, CFL  0.09253, SL  0.0000E+00, M 1.33984E+16, S 34.2592, T -0.3998, Me -1.06E-14, Se  3.33E-05, Te  1.04E-04
```

### Domain, forcing and output

Made by running the notebook [`explore_run.ipynb`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/blob/main/tested-configs/notebooks/explore_run.ipynb) on this run's output folder; it only plots files MOM6 wrote during the run. **[See the notebook with its code](notebooks/isomip-plus-ocean0.md)**.

#### Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `240` |
| `NJGLOBAL` | `40` |
| `NK` | `36` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `ISOMIP` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `SIGMA_SHELF_ZSTAR` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `ISOMIP` |
| `TS_CONFIG` | `ISOMIP` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `NONE` |
| `ICE_SHELF` | `True` |
| `DT` | `720.0` |
| `DT_THERM` | `720.0` |
| `DAYMAX` | `90.0` |


#### Domain and bottom depth


Grid: 240 x 40 points (`GRID_CONFIG = cartesian`), x from 321 to 799 kilometers, y from 1 to 79 kilometers. Bottom depth `D` from 104.607 to 720 m (`TOPO_CONFIG = ISOMIP`).



    
![png](../../assets/tested-configs/notebooks/isomip-plus-ocean0/notebook_8_1.png)
    


#### Initial state


MOM6 did not write an initial-state file for this run (it does when `SAVE_INITIAL_CONDS = True`), so the initial state is not shown here; see the run's `MOM_parameter_doc.all` (`THICKNESS_CONFIG = ISOMIP`, `TS_CONFIG = ISOMIP`).


#### Surface forcing


Time-mean of the surface forcing saved in the diagnostics: `PRCmE` (Net surface water flux (precip+melt+lrunoff+ice calving-evap), from `forcing.nc`), `ustar` (Surface friction velocity = [(gustiness + tau_magnitude)/rho0]^(1/2), from `forcing.nc`).



    
![png](../../assets/tested-configs/notebooks/isomip-plus-ocean0/notebook_12_1.png)
    



    
![png](../../assets/tested-configs/notebooks/isomip-plus-ocean0/notebook_12_2.png)
    


#### Energy and stability through the run


    
![png](../../assets/tested-configs/notebooks/isomip-plus-ocean0/notebook_14_0.png)
    



From `ocean.stats.nc`: 721 records; time axis in days.


#### Final state


`temp` at the last record of `ave_prog.nc` (average over the last output interval).



    
![png](../../assets/tested-configs/notebooks/isomip-plus-ocean0/notebook_16_1.png)

### Provenance

| What | Value |
|---|---|
| Configuration | [mom6-idealised-configs branch `isomip-plus-ocean0-sigmashelfzstar`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/isomip-plus-ocean0-sigmashelfzstar) `094d9177` |
| Input file | [claireyung/isomip-test-mom6-for-iom3-configs](https://github.com/claireyung/isomip-test-mom6-for-iom3-configs) `3b86dc0b` |
| ACCESS-OM3 module | `access-om3/2026.05.004` |
| MOM6 source code | `ACCESS-NRI/MOM6 2026.05.003 d11a149ccba676d524312328f7eb62560a156dc3` |
| Executable | `/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access-mom6-2026.05.003-ld7hklzo5ajizx5u4yl74i4ijberrpv6/bin/mom6-solo` |
| Executable md5 | `4785d157c76c30d8d01baf7d0f69d218` |
| payu | `1.3.6_1` (module `payu/1.3.6_1`) |
| Date tested | 2026-11-04 |
| PBS Job Id | `183114027.gadi-pbs` |
| PBS Exit Status | `0` |
| PBS Service Units | `9.17` |
| PBS NCPUs Requested | `48` |
| PBS Walltime Used | `00:05:44` |
| PBS Memory Used | `11.48GB` |

??? info "Input files and md5 hashes (from payu `manifests/input.yaml`)"
    | File | md5 | Comes from |
    |---|---|---|
    | `INPUT/Ocean0_3D_Claire.nc` | `a9e43676e2c0acbfe1d48ce856d2ff84` | `isomip-plus/input-repo/INPUT/Ocean0_3D_Claire.nc` |

??? info "Parameters differing from Claire Yung's own run (`docs/` in isomip-test-mom6-for-iom3-configs) (7)"
    Comparison of this run's `MOM_parameter_doc.all` with Claire Yung's own run (`docs/` in isomip-test-mom6-for-iom3-configs).
    Differences show where the ACCESS-OM3 MOM6 version adds, drops or changes default parameters.

    New in this run: `ADVECTION_SCHEME_VARIANCE_UNDERFLOW`, `ICE_SHELF_BUOYANCY_FLUX_ITT_BUG`, `ICE_SHELF_SALT_FLUX_ITT_BUG`, `NONBLOCKING_P_SURF_BUG`, `USE_FILE_DYES`

    Only upstream: `ICE_SHELF_BUOYANCY_FLUX_ITT_BUGFIX`, `ICE_SHELF_SALT_FLUX_ITT_BUGFIX`

??? info "Run-time environment (selected variables from payu's `env.yaml`)"
    | Variable | Value |
    |---|---|
    | `LD_LIBRARY_PATH` | `/apps/openmpi/4.1.7/lib:/apps/openmpi/4.1.7/lib/profilers` |
    | `LOADEDMODULES` | `access3-share/2026.03.002-eale5gm:access-cice/CICE6.6.3-2-huasrvo:access-mocsy/2025.07.002-saj7rvh:access-generic-tracers/2026.09.000-e3zb3ez:access-mom6/2026.05.003-ld7hklz:access-ww3/2026.03.001-bjzidie:access3/2026.03.002-26wbxup:access-om3/2026.05.004:pbs:openmpi/4.1.7` |
    | `OMPI_MCA_orte_tmpdir_base` | `/jobfs/183114027.gadi-pbs` |
    | `PAYU_TELEMETRY_ENV_VERSION` | `1.3.6_1` |
    | `PBS_NCI_NCPUS_PER_NODE` | `104` |
    | `PBS_NCPUS` | `48` |
    | `PBS_QUEUE` | `normalsr-exec` |

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for ISOMIP+ Ocean0 (written by isomip-plus-ocean0.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 48
    walltime: 01:00:00
    jobname: isomip-plus
    experiment: isomip-plus-ocean0
    laboratory: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab

    model: mom6
    exe: mom6-solo
    input:
      - /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/isomip-plus/input-repo/INPUT
    modules:
      use:
        - /g/data/vk83/modules
      load:
        - access-om3/2026.05.004

    collate: false
    runlog: false            # don't commit run logs into the cloned repository
    metadata:
      enable: false
    ```

??? info "Output files"
    | File | Size |
    |---|---|
    | `ISOMIP_IC.nc` | 39.91 MB |
    | `MOM_Shelf_IC.nc` | 0.25 MB |
    | `Vertical_coordinate.nc` | 0.00 MB |
    | `ave_prog.nc` | 175.63 MB |
    | `forcing.nc` | 27.77 MB |
    | `ice.nc` | 51.97 MB |
    | `ocean.stats.nc` | 0.93 MB |
    | `ocean_geometry.nc` | 1.50 MB |

