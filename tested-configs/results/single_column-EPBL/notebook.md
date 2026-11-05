
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
| `REGRIDDING_COORDINATE_MODE` | `Z*` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `WRIGHT` |
| `WIND_CONFIG` | `data_override` |
| `BUOY_CONFIG` | `data_override` |
| `ICE_SHELF` | `False` |
| `DT` | `3600.0` |
| `DT_THERM` | `3600.0` |
| `DAYMAX` | `180.0` |


## Domain and bottom depth


Grid: 2 x 2 points (`GRID_CONFIG = cartesian`), x from 0.25 to 0.75 degrees_east, y from 30.25 to 30.75 degrees_north. Bottom depth `D` from 6000 to 6000 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/single_column-EPBL/notebook_8_1.png)
    


## Initial state


`Temp` from `MOM_IC.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/single_column-EPBL/notebook_10_1.png)
    


## Surface forcing


Time-mean of the surface forcing saved in the diagnostics: `taux` (Zonal surface stress from ocean interactions with atmos and ice, from `surffluxes.nc`), `net_heat_surface` (Surface ocean heat flux from SW+LW+lat+sens+mass transfer+frazil+restore+seaice_melt_heat or flux adjustments, from `surffluxes.nc`).



    
![png](@ASSETS@/tested-configs/notebooks/single_column-EPBL/notebook_12_1.png)
    



    
![png](@ASSETS@/tested-configs/notebooks/single_column-EPBL/notebook_12_2.png)
    


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/single_column-EPBL/notebook_14_0.png)
    



From `ocean.stats.nc`: 19 records; time axis in days.


## Final state


`temp` at the last record of `prog_z.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/single_column-EPBL/notebook_16_1.png)
    

