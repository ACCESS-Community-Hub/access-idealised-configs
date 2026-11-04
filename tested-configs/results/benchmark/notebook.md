
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `360` |
| `NJGLOBAL` | `180` |
| `NK` | `22` |
| `GRID_CONFIG` | `mercator` |
| `TOPO_CONFIG` | `benchmark` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `False` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `WRIGHT` |
| `THICKNESS_CONFIG` | `benchmark` |
| `TS_CONFIG` | `benchmark` |
| `WIND_CONFIG` | `gyres` |
| `BUOY_CONFIG` | `linear` |
| `ICE_SHELF` | `False` |
| `DT` | `900.0` |
| `DT_THERM` | `3600.0` |
| `DAYMAX` | `1.0` |


## Domain and bottom depth


Grid: 360 x 180 points (`GRID_CONFIG = mercator`), x from 0.125 to 89.875 degrees_east, y from -40.8855 to -0.125 degrees_north. Bottom depth `D` from 0.5 to 5454.72 m (`TOPO_CONFIG = benchmark`).



    
![png](@ASSETS@/tested-configs/notebooks/benchmark/notebook_8_1.png)
    


## Initial state


`Temp` from `GOLD_IC.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/benchmark/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = gyres` and `BUOY_CONFIG = linear` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/benchmark/notebook_14_0.png)
    



From `ocean.stats.nc`: 5 records; time axis in days.


## Final state


`temp` at the last record of `prog.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/benchmark/notebook_16_1.png)
    

