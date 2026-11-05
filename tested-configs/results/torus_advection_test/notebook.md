
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `48` |
| `NJGLOBAL` | `48` |
| `NK` | `5` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `True` |
| `USE_REGRIDDING` | `False` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `uniform` |
| `TS_CONFIG` | `fit` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `NONE` |
| `ICE_SHELF` | `False` |
| `DT` | `3600.0` |
| `DT_THERM` | `3600.0` |
| `DAYMAX` | `2.0` |


## Domain and bottom depth


Grid: 48 x 48 points (`GRID_CONFIG = cartesian`), x from 1.8 to 171 kilometers, y from 1.8 to 171 kilometers. Bottom depth `D` from 200 to 200 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/torus_advection_test/notebook_8_1.png)
    


## Initial state


`Temp` from `GOLD_IC.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/torus_advection_test/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = NONE` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/torus_advection_test/notebook_14_0.png)
    



From `ocean.stats.nc`: 5 records; time axis in days.


## Final state


`tr1` at the last record of `prog.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/torus_advection_test/notebook_16_1.png)
    

