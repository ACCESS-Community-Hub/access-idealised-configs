
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `40` |
| `NJGLOBAL` | `2` |
| `NK` | `20` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `seamount` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `Z*` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `seamount` |
| `TS_CONFIG` | `seamount` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `NONE` |
| `ICE_SHELF` | `False` |
| `DT` | `900.0` |
| `DT_THERM` | `900.0` |
| `DAYMAX` | `5.0` |


## Domain and bottom depth


Grid: 40 x 2 points (`GRID_CONFIG = cartesian`), x from 2.5 to 197.5 kilometers, y from 32.5 to 37.5 kilometers. Bottom depth `D` from 2031.01 to 4000 m (`TOPO_CONFIG = seamount`).



    
![png](@ASSETS@/tested-configs/notebooks/seamount-z/notebook_8_1.png)
    


## Initial state


`Salt` from `Initial_state.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/seamount-z/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = NONE` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/seamount-z/notebook_14_0.png)
    



From `ocean.stats.nc`: 6 records; time axis in days.


## Final state


`salt` at the last record of `prog.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/seamount-z/notebook_16_1.png)
    

