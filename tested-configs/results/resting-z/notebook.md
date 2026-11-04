
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `20` |
| `NJGLOBAL` | `2` |
| `NK` | `9` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `Z*` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `uniform` |
| `TS_CONFIG` | `linear` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `NONE` |
| `ICE_SHELF` | `False` |
| `DT` | `1200.0` |
| `DT_THERM` | `1200.0` |
| `DAYMAX` | `5.0` |


## Domain and bottom depth


Grid: 20 x 2 points (`GRID_CONFIG = cartesian`), x from 5 to 195 kilometers, y from 5 to 15 kilometers. Bottom depth `D` from 1000 to 1000 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/resting-z/notebook_8_1.png)
    


## Initial state


`Salt` from `MOM_IC.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/resting-z/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = NONE` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/resting-z/notebook_14_0.png)
    



From `ocean.stats.nc`: 6 records; time axis in days.


## Final state


`salt` at the last record of `prog.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/resting-z/notebook_16_1.png)
    

