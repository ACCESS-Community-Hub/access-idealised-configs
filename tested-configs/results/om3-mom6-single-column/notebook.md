
## Set-up


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


## Domain and bottom depth


Grid: 2 x 2 points (`GRID_CONFIG = cartesian`), x from -64.45 to -63.95 degrees_east, y from 31.45 to 31.95 degrees_north. Bottom depth `D` from 6000 to 6000 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/om3-mom6-single-column/notebook_8_1.png)
    


## Initial state


MOM6 did not write an initial-state file for this run (it does when `SAVE_INITIAL_CONDS = True`), so the initial state is not shown here; see the run's `MOM_parameter_doc.all` (`THICKNESS_CONFIG = n/a`, `TS_CONFIG = n/a`).


## Surface forcing


Time-mean of the surface forcing saved in the diagnostics: `tauuo` (Surface Downward X Stress, from `access-om3.mom6.2d.tauuo.1day.mean.1900.nc`), `hfds` (Surface ocean heat flux from SW+LW+latent+sensible+masstransfer+frazil+seaice_melt_heat, from `access-om3.mom6.2d.hfds.1day.mean.1900.nc`).



    
![png](@ASSETS@/tested-configs/notebooks/om3-mom6-single-column/notebook_12_1.png)
    



    
![png](@ASSETS@/tested-configs/notebooks/om3-mom6-single-column/notebook_12_2.png)
    


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/om3-mom6-single-column/notebook_14_0.png)
    



From `ocean.stats.nc`: 366 records; time axis in days.


## Final state


`thetao` at the last record of `access-om3.mom6.3d.thetao.1day.mean.1900.nc` (average over the last output interval).



    
![png](@ASSETS@/tested-configs/notebooks/om3-mom6-single-column/notebook_16_1.png)
    

