
## Set-up


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


## Domain and bottom depth


Grid: 160 x 800 points (`GRID_CONFIG = mercator`), x from 0.125 to 39.875 degrees_east, y from -70.151 to 70.151 degrees_north. Bottom depth `D` from 0 to 4000 m (`TOPO_CONFIG = file`).



    
![png](@ASSETS@/tested-configs/notebooks/anu-tub-zstar/notebook_8_1.png)
    


## Initial state


`Temp` from `MOM_IC.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/anu-tub-zstar/notebook_10_1.png)
    


## Surface forcing


Time-mean of the surface forcing saved in the diagnostics: `tauuo` (Surface Downward X Stress, from `ocean_month.nc`), `hfds` (Surface ocean heat flux from SW+LW+latent+sensible+masstransfer+frazil+seaice_melt_heat, from `ocean_month.nc`).



    
![png](@ASSETS@/tested-configs/notebooks/anu-tub-zstar/notebook_12_1.png)
    



    
![png](@ASSETS@/tested-configs/notebooks/anu-tub-zstar/notebook_12_2.png)
    


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/anu-tub-zstar/notebook_14_0.png)
    



From `ocean.stats.nc`: 32 records; time axis in days.


## Final state


`thetao` at the last record of `ocean_month_z.nc` (average over the last output interval).



    
![png](@ASSETS@/tested-configs/notebooks/anu-tub-zstar/notebook_16_1.png)
    

