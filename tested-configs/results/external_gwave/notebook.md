
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `128` |
| `NJGLOBAL` | `4` |
| `NK` | `21` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `True` |
| `USE_REGRIDDING` | `False` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `external_gwave` |
| `TS_CONFIG` | `fit` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `NONE` |
| `ICE_SHELF` | `False` |
| `DT` | `60.0` |
| `DT_THERM` | `120.0` |
| `DAYMAX` | `1800.0` |


## Domain and bottom depth


Grid: 128 x 4 points (`GRID_CONFIG = cartesian`), x from -31.75 to 31.75 kilometers, y from 0.5 to 3.5 kilometers. Bottom depth `D` from 20 to 20 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/external_gwave/notebook_8_1.png)
    


## Initial state


`Temp` from `GOLD_IC.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/external_gwave/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = NONE` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/external_gwave/notebook_14_0.png)
    



From `ocean.stats.nc`: 4 records; time axis in seconds.


## Final state


`temp` at the last record of `prog.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/external_gwave/notebook_16_1.png)
    

