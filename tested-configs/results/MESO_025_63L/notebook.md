
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `1440` |
| `NJGLOBAL` | `450` |
| `NK` | `63` |
| `GRID_CONFIG` | `mercator` |
| `TOPO_CONFIG` | `file` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `False` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `WRIGHT` |
| `THICKNESS_CONFIG` | `file` |
| `TS_CONFIG` | `file` |
| `WIND_CONFIG` | `file` |
| `BUOY_CONFIG` | `MESO` |
| `ICE_SHELF` | `False` |
| `DT` | `600.0` |
| `DT_THERM` | `3600.0` |
| `DAYMAX` | `6.0` |


## Domain and bottom depth


Grid: 1440 x 450 points (`GRID_CONFIG = mercator`), x from 0.125 to 359.875 degrees_east, y from -73.9851 to -0.125 degrees_north. Bottom depth `D` from 7.5 to 5500 m (`TOPO_CONFIG = file`).



    
![png](@ASSETS@/tested-configs/notebooks/MESO_025_63L/notebook_8_1.png)
    


## Initial state


`Temp` from `MOM_IC.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/MESO_025_63L/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = file` and `BUOY_CONFIG = MESO` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/MESO_025_63L/notebook_14_0.png)
    



From `ocean.stats.nc`: 7 records; time axis in hours.


## Final state


`Temp` at the last record of `MOM_IC.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/MESO_025_63L/notebook_16_1.png)
    

