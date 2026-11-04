
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `360` |
| `NJGLOBAL` | `210` |
| `NK` | `50` |
| `GRID_CONFIG` | `mosaic` |
| `TOPO_CONFIG` | `file` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `HYCOM1` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `WRIGHT` |
| `WIND_CONFIG` | `file` |
| `BUOY_CONFIG` | `file` |
| `ICE_SHELF` | `False` |
| `DT` | `3600.0` |
| `DT_THERM` | `7200.0` |
| `DAYMAX` | `1.0` |


## Domain and bottom depth


Grid: 360 x 210 points (`GRID_CONFIG = mosaic`), x from -279.5 to 79.5 degrees_east, y from -76.75 to 89.75 degrees_north. Bottom depth `D` from 0.25 to 6000 m (`TOPO_CONFIG = file`).



    
![png](@ASSETS@/tested-configs/notebooks/global_ALE-hycom/notebook_8_1.png)
    


## Initial state


`Temp` from `MOM_IC.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/global_ALE-hycom/notebook_10_1.png)
    


## Surface forcing


Time-mean of the surface forcing saved in the diagnostics: `taux` (Zonal surface stress from ocean interactions with atmos and ice, from `forcing.nc`), `net_heat_surface` (Surface ocean heat flux from SW+LW+lat+sens+mass transfer+frazil+restore+seaice_melt_heat or flux adjustments, from `forcing.nc`).



    
![png](@ASSETS@/tested-configs/notebooks/global_ALE-hycom/notebook_12_1.png)
    



    
![png](@ASSETS@/tested-configs/notebooks/global_ALE-hycom/notebook_12_2.png)
    


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/global_ALE-hycom/notebook_14_0.png)
    



From `ocean.stats.nc`: 3 records; time axis in days.


## Final state


`SSH` at the last record of `surface.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/global_ALE-hycom/notebook_16_1.png)
    

