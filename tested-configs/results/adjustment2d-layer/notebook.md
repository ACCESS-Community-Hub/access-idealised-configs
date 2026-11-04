
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `128` |
| `NJGLOBAL` | `4` |
| `NK` | `25` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `True` |
| `USE_REGRIDDING` | `False` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `adjustment2d` |
| `TS_CONFIG` | `adjustment2d` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `NONE` |
| `ICE_SHELF` | `False` |
| `DT` | `150.0` |
| `DT_THERM` | `300.0` |
| `DAYMAX` | `2.0` |


## Domain and bottom depth


Grid: 128 x 4 points (`GRID_CONFIG = cartesian`), x from 0.25 to 63.75 kilometers, y from 35 to 65 kilometers. Bottom depth `D` from 20 to 20 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/adjustment2d-layer/notebook_8_1.png)
    


## Initial state


`Salt` from `Initial_state.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/adjustment2d-layer/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = NONE` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/adjustment2d-layer/notebook_14_0.png)
    



From `ocean.stats.nc`: 5 records; time axis in hours.


## Final state


`salt` at the last record of `prog.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/adjustment2d-layer/notebook_16_1.png)
    

