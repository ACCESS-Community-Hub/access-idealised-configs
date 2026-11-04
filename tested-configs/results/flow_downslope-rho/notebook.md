
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `80` |
| `NJGLOBAL` | `4` |
| `NK` | `40` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `DOME2D` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `RHO` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `DOME2D` |
| `TS_CONFIG` | `DOME2D` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `NONE` |
| `ICE_SHELF` | `False` |
| `DT` | `300.0` |
| `DT_THERM` | `900.0` |
| `DAYMAX` | `12.0` |


## Domain and bottom depth


Grid: 80 x 4 points (`GRID_CONFIG = cartesian`), x from 5 to 795 kilometers, y from 35 to 65 kilometers. Bottom depth `D` from 800 to 4000 m (`TOPO_CONFIG = DOME2D`).



    
![png](@ASSETS@/tested-configs/notebooks/flow_downslope-rho/notebook_8_1.png)
    


## Initial state


`Temp` from `Initial_state.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/flow_downslope-rho/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = NONE` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/flow_downslope-rho/notebook_14_0.png)
    



From `ocean.stats.nc`: 13 records; time axis in hours.


## Final state


`temp` at the last record of `prog.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/flow_downslope-rho/notebook_16_1.png)
    

