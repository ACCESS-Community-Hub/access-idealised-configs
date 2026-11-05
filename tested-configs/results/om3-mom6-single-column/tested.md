!!! success "Tested: this configuration runs"
    Ran on Gadi on 2026-11-04 with `access-om3/2026.05.004` (`mom6-solo`) and `payu/1.3.6_1`: 2 cores, walltime used 00:07:16, 0.48 SU.

### What we got

Last lines of `ocean.stats`:

```text
  8687,  693497.000,     0, En 7.5261615026835847E-06, CFL  0.00443, SL  1.0805E-01, M 7.69526E+16, S 35.2852, T  4.6864, Me -3.32E-18, Se -3.33E-15, Te  4.72E-16
  8711,  693498.000,     0, En 4.3882487069297339E-06, CFL  0.00398, SL  1.0772E-01, M 7.69526E+16, S 35.2852, T  4.6865, Me -9.93E-18, Se  1.66E-14, Te  1.54E-15
  8735,  693499.000,     0, En 4.2839949271770052E-06, CFL  0.00404, SL  1.0691E-01, M 7.69526E+16, S 35.2852, T  4.6865, Me  7.14E-18, Se  6.65E-15, Te  1.27E-15
  8759,  693500.000,     0, En 3.5697553201165393E-06, CFL  0.00248, SL  1.0497E-01, M 7.69525E+16, S 35.2852, T  4.6864, Me  4.72E-18, Se  9.98E-15, Te -3.33E-15
```

### Domain, forcing and output

Made by running the notebook [`explore_run.ipynb`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/main/tested-configs/notebooks/explore_run.ipynb) on this run's output folder; it only plots files MOM6 wrote during the run. **[See the notebook with its code](notebooks/om3-mom6-single-column.md)**.

#### Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `2` |
| `NJGLOBAL` | `2` |
| `NK` | `75` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `True` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `ZSTAR` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `ROQUET_RHO` |
| `ICE_SHELF` | `False` |
| `DT` | `3600.0` |
| `DT_THERM` | `3600.0` |


#### Domain and bottom depth


Grid: 2 x 2 points (`GRID_CONFIG = cartesian`), x from -64.45 to -63.95 degrees_east, y from 31.45 to 31.95 degrees_north. Bottom depth `D` from 6000 to 6000 m (`TOPO_CONFIG = flat`).



    
![png](../../assets/tested-configs/notebooks/om3-mom6-single-column/notebook_8_1.png)
    


#### Initial state


MOM6 did not write an initial-state file for this run (it does when `SAVE_INITIAL_CONDS = True`), so the initial state is not shown here; see the run's `MOM_parameter_doc.all` (`THICKNESS_CONFIG = n/a`, `TS_CONFIG = n/a`).


#### Surface forcing


Time-mean of the surface forcing saved in the diagnostics: `tauuo` (Surface Downward X Stress, from `access-om3.mom6.2d.tauuo.1day.mean.1900.nc`), `hfds` (Surface ocean heat flux from SW+LW+latent+sensible+masstransfer+frazil+seaice_melt_heat, from `access-om3.mom6.2d.hfds.1day.mean.1900.nc`).



    
![png](../../assets/tested-configs/notebooks/om3-mom6-single-column/notebook_12_1.png)
    



    
![png](../../assets/tested-configs/notebooks/om3-mom6-single-column/notebook_12_2.png)
    


#### Energy and stability through the run


    
![png](../../assets/tested-configs/notebooks/om3-mom6-single-column/notebook_14_0.png)
    



From `ocean.stats.nc`: 366 records; time axis in days.


#### Final state


`thetao` at the last record of `access-om3.mom6.3d.thetao.1day.mean.1900.nc` (average over the last output interval).



    
![png](../../assets/tested-configs/notebooks/om3-mom6-single-column/notebook_16_1.png)

### Parameters compared with the reference

<span class="chip a">A</span> the file committed in om3-mom6-single-column (`9a8310b0`): [`MOM_parameter_doc.all`](https://github.com/ACCESS-Community-Hub/om3-mom6-single-column/blob/9a8310b09bd4b97c676ccbd0b54ddf4dfe686b5f/docs/MOM_parameter_doc.all)  
<span class="chip b">B</span> this run: [`MOM_parameter_doc.all`](parameters/om3-mom6-single-column.md) in the run's output, `/scratch/<your-project>/$USER/access-om3/archive/om3-mom6-single-column/output000/MOM_parameter_doc.all` when you run the script

**0** parameter values differ; **0** parameters exist only in this run's MOM6 version and **0** only in the reference (new, removed or renamed parameters). Values are compared ignoring quotes, case and number formatting. Parameter names link to a search of the MOM6 source; reference values link to their line on GitHub and this run's line numbers to its file.

### Provenance

| What | Value |
|---|---|
| Configuration | [ACCESS-Community-Hub/om3-mom6-single-column](https://github.com/ACCESS-Community-Hub/om3-mom6-single-column) `9a8310b0` (branch `jra_ryf+wombatlite`) |
| Executable | `access-om3-MOM6` (coupled ACCESS-OM3, not `mom6-solo`) |
| ACCESS-OM3 module | `access-om3/2026.05.004` |
| MOM6 source code | `ACCESS-NRI/MOM6 2026.05.003 d11a149ccba676d524312328f7eb62560a156dc3` |
| Executable | `/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access3-2026.03.002-26wbxupakyegbkd366xjob3d7do5maoj/bin/access-om3-MOM6` |
| Executable md5 | `6656aea8e7ba5d4a4dd6e215fe6efdd3` |
| payu | `1.3.6_1` (module `payu/1.3.6_1`) |
| Date tested | 2026-11-04 |
| PBS Job Id | `183150773.gadi-pbs` |
| PBS Exit Status | `0` |
| PBS Service Units | `0.48` |
| PBS NCPUs Requested | `2` |
| PBS Walltime Used | `00:07:16` |
| PBS Memory Used | `8.0GB` |

??? info "Input files and md5 hashes (from payu `manifests/input.yaml`)"
    | File | md5 | Comes from |
    |---|---|---|
    | `INPUT/JRA55do-datm-ESMFmesh.nc` | `0ecb68f878b91b8adc90838e2c413914` | `/g/data/vk83/prerelease/configurations/inputs/access-om3/share/meshes/share/2026.01.21/JRA55do-datm-ESMFmesh.nc` |
    | `INPUT/JRA55do-drof-ESMFmesh.nc` | `bf62c4e7786ddfbe56d61b3074d5d16d` | `/g/data/vk83/prerelease/configurations/inputs/access-om3/share/meshes/share/2026.01.21/JRA55do-drof-ESMFmesh.nc` |
    | `INPUT/MOM_override` | `3f60a8a4e1369b6d72ecb30600d755f3` | `om3-mom6-single-column/domains/BATS/MOM_override` |
    | `INPUT/RYF.friver.1990_1991.nc` | `beb16730c02db9a730f69dfdc843b774` | `/g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15/RYF.friver.1990_1991.nc` |
    | `INPUT/RYF.huss.1990_1991.nc` | `1b184b232a31382443e5818bb623a9cb` | `/g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15/RYF.huss.1990_1991.nc` |
    | `INPUT/RYF.licalvf.1990_1991.nc` | `1d9233a590fb94d052196cdd5245a585` | `/g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15/RYF.licalvf.1990_1991.nc` |
    | `INPUT/RYF.prra.1990_1991.nc` | `a03d5b51f44fb9fcad5036a0b7d408d0` | `/g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15/RYF.prra.1990_1991.nc` |
    | `INPUT/RYF.prsn.1990_1991.nc` | `914dcf6080c0fc9b9d46bf7082a4c0be` | `/g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15/RYF.prsn.1990_1991.nc` |
    | `INPUT/RYF.psl.1990_1991.nc` | `98206e380baf0f229b2983f569f9b0e0` | `/g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15/RYF.psl.1990_1991.nc` |
    | `INPUT/RYF.rlds.1990_1991.nc` | `6e9242d3a02c1ee768337dcab710de39` | `/g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15/RYF.rlds.1990_1991.nc` |
    | `INPUT/RYF.rsds.1990_1991.nc` | `5f9721311ff7ac4908ca79a9d9cfa5fd` | `/g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15/RYF.rsds.1990_1991.nc` |
    | `INPUT/RYF.tas.1990_1991.nc` | `5fdf6d3b0369f1b50138013101c288a6` | `/g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15/RYF.tas.1990_1991.nc` |
    | `INPUT/RYF.uas.1990_1991.nc` | `264a82753021ba094b54cc0cfae4f3ec` | `/g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15/RYF.uas.1990_1991.nc` |
    | `INPUT/RYF.vas.1990_1991.nc` | `bd0ccd8ef7f639ca77b6705f0d6d1fcb` | `/g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15/RYF.vas.1990_1991.nc` |
    | `INPUT/SFe_Hamiltonetal2020_monthly_clim.nc` | `a5c9d1c99c3db0a33e23e42a21890282` | `om3-mom6-single-column/domains/BATS/SFe_Hamiltonetal2020_monthly_clim.nc` |
    | `INPUT/chl_globcolour_monthly_clim.nc` | `df6a9e7d1096b9d2deab6213ee7dc9a2` | `om3-mom6-single-column/domains/BATS/chl_globcolour_monthly_clim.nc` |
    | `INPUT/grid_spec.nc` | `709268cd891e6f0e827f6de0249f1a3d` | `/g/data/vk83/prerelease/configurations/inputs/access-om3/mom/grids/mosaic/share/2024.05.08/grid_spec.nc` |
    | `INPUT/horizontal_grid.nc` | `4470d89a909779200f3841428d5b486c` | `om3-mom6-single-column/domains/BATS/horizontal_grid.nc` |
    | `INPUT/ocean_mosaic.nc` | `c267baee375329253290655b83ed11b2` | `om3-mom6-single-column/domains/BATS/ocean_mosaic.nc` |
    | `INPUT/ocean_vgrid.nc` | `04e88652ff339b09b29ea4adb8fa2229` | `/g/data/vk83/prerelease/configurations/inputs/access-om3/mom/grids/vertical/global.25km/2026.03.16/ocean_vgrid.nc` |
    | `INPUT/single-column-ESMFmesh.nc` | `1bf9a35376fd0a7df792cdac489fc536` | `om3-mom6-single-column/domains/BATS/single-column-ESMFmesh.nc` |
    | `INPUT/woa23_ts_01_mom.nc` | `bd9559e8a3dbefa16080d0340b26be12` | `/g/data/vk83/configurations/inputs/access-om3/mom/initial_conditions/global.25km/2025.10.24/woa23_ts_01_mom.nc` |
    | `INPUT/wombatlite_ic.nc` | `b06bb6902d518887a30fb6154989c7ea` | `/g/data/vk83/prerelease/configurations/inputs/access-om3/wombat/initial_conditions/share/2026.05.07/wombatlite_ic.nc` |

??? info "Run-time environment (selected variables from payu's `env.yaml`)"
    | Variable | Value |
    |---|---|
    | `LD_LIBRARY_PATH` | `/apps/openmpi/4.1.7/lib:/apps/openmpi/4.1.7/lib/profilers` |
    | `LOADEDMODULES` | `access3-share/2026.03.002-eale5gm:access-cice/CICE6.6.3-2-huasrvo:access-mocsy/2025.07.002-saj7rvh:access-generic-tracers/2026.09.000-e3zb3ez:access-mom6/2026.05.003-ld7hklz:access-ww3/2026.03.001-bjzidie:access3/2026.03.002-26wbxup:access-om3/2026.05.004:pbs:openmpi/4.1.7` |
    | `OMPI_MCA_orte_tmpdir_base` | `/jobfs/183150773.gadi-pbs` |
    | `PAYU_TELEMETRY_ENV_VERSION` | `1.3.6_1` |
    | `PBS_NCI_NCPUS_PER_NODE` | `104` |
    | `PBS_NCPUS` | `2` |
    | `PBS_QUEUE` | `normalsr-exec` |

??? info "payu config.yaml written by the script"
    ```yaml
    # Payu configuration

    # If submitting to a different project to your default, uncomment line below 
    # and change project code as appropriate; also set shortpath below
    # project: x77
    # Force payu to always find, and save, files in this scratch project directory
    # shortpath: /scratch/v45

    # Model software version
    modules:
        use:
            - /g/data/vk83/modules
        load:
            - access-om3/2026.05.004

    queue: normalsr
    ncpus: 2
    walltime: 1:00:00
    jobname: single_column

    model: access-om3
    exe: access-om3-MOM6
    input:
        - /g/data/vk83/prerelease/configurations/inputs/access-om3/mom/grids/mosaic/share/2024.05.08/grid_spec.nc
        - /g/data/vk83/prerelease/configurations/inputs/access-om3/mom/grids/vertical/global.25km/2026.03.16/ocean_vgrid.nc
        - /g/data/vk83/configurations/inputs/access-om3/mom/initial_conditions/global.25km/2025.10.24/woa23_ts_01_mom.nc
        - /g/data/vk83/prerelease/configurations/inputs/access-om3/share/meshes/share/2026.01.21/JRA55do-datm-ESMFmesh.nc
        - /g/data/vk83/prerelease/configurations/inputs/access-om3/share/meshes/share/2026.01.21/JRA55do-drof-ESMFmesh.nc
        - /g/data/vk83/prerelease/configurations/inputs/access-om3/wombat/initial_conditions/share/2026.05.07/wombatlite_ic.nc
        - /g/data/vk83/prerelease/configurations/inputs/JRA-55/RYF/v1-6/2026.04.15
        - ./INPUT

    runlog: false
    metadata: 
        enable: false
    manifest:
      reproduce:
        exe: false

    platform:
        nodesize: 104
        nodemem: 512

    collate: false

    userscripts:
        archive: /usr/bin/bash /g/data/vk83/apps/om3-scripts/payu_config/archive.sh

    qsub_flags: -W umask=027

    restart_freq: 1YS
    payu_minimum_version: 1.2.0


    # added by om3-mom6-single-column.sh
    project: tm70
    experiment: om3-mom6-single-column
    laboratory: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab
    ```

??? info "Output files"
    | File | Size | What it is |
    |---|---|---|
    | `Vertical_coordinate.nc` | 0.00 MB | The vertical coordinate: target values of the layers or levels |
    | `access-om3.mom6.2d.caco3_sediment.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.2d.det_sediment.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.2d.detfe_sediment.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.2d.dic_csurf.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.dic_stf.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.ePBL_h_ML.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.evs.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.ficeberg.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.friver.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.h_ML.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.hfds.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.hfrainds.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.hfrunoffds.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.hfsso.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.mlotst.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.net_heat_coupler.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.o2_stf.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.pco2.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.prlq.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.prsn.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.pso.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.rlntds.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.rsntds.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.tauuo.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.tauvo.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.ustar.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.wfo.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.2d.zeuphot.1day.mean.1900.nc` | 0.04 MB |  |
    | `access-om3.mom6.3d.Kd_interface.1day.mean.1900.nc` | 0.48 MB |  |
    | `access-om3.mom6.3d.alk.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.caco3.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.caco3_vmove.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.det.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.det_vmove.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.detfe.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.detremi.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.dic.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.e.1day.mean.1900.nc` | 0.48 MB |  |
    | `access-om3.mom6.3d.fe.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.fesinks.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.fesources.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.htotal.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.no3.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.npp3d.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.o2.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.omega_ara.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.omega_cal.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.pchl.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.pchl_mu.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.phy.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.phy_dfeupt.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.phy_lfer.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.phy_lnit.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.phy_lpar.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.phy_mu.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.phyfe.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.phygrow.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.phymorl.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.phymorq.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.pic2poc.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.radbio.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.so.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.thetao.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.thkcello.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.uo.1day.mean.1900.nc` | 0.69 MB |  |
    | `access-om3.mom6.3d.vo.1day.mean.1900.nc` | 0.69 MB |  |
    | `access-om3.mom6.3d.zoo.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.zooeps.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.zoofe.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.zoograzdet.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.zoograzphy.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.3d.zsp3d.1day.mean.1900.nc` | 0.47 MB |  |
    | `access-om3.mom6.static.nc` | 0.03 MB | Diagnostics set in `diag_table`: snapshots of `areacello`, `areacello_cu`, `areacello_cv`, `areacello_bu`, `dxt`, `dyt`, `geolat_c`, `geolat` and 20 more, written once (static) |
    | `ocean.stats.nc` | 0.98 MB | Domain totals at each energy-save time (energy, mass, heat, salt, maximum CFL); the netCDF form of `ocean.stats` |
    | `ocean_geometry.nc` | 0.02 MB | Static grid: coordinates, cell sizes and areas, bottom depth `D`, Coriolis parameter, land mask |

