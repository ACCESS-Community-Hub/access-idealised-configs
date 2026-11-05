
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `4` |
| `NJGLOBAL` | `80` |
| `NK` | `40` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `Z*` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `rossby_front` |
| `TS_CONFIG` | `rossby_front` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `NONE` |
| `ICE_SHELF` | `False` |
| `DT` | `3600.0` |
| `DT_THERM` | `3600.0` |
| `DAYMAX` | `10.0` |


## Domain and bottom depth


Grid: 4 x 80 points (`GRID_CONFIG = cartesian`), x from 5 to 35 kilometers, y from 2.5 to 397.5 kilometers. Bottom depth `D` from 400 to 400 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/mixed_layer_restrat_2d/notebook_8_1.png)
    


## Initial state


`Temp` from `Initial_state.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/mixed_layer_restrat_2d/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = NONE` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/mixed_layer_restrat_2d/notebook_14_0.png)
    



From `ocean.stats.nc`: 25 records; time axis in hours.


## Final state


`temp` at the last record of `prog.nc` (average over the last output interval).



    
![png](@ASSETS@/tested-configs/notebooks/mixed_layer_restrat_2d/notebook_16_1.png)
    

