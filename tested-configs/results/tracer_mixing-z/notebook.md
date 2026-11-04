
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `20` |
| `NJGLOBAL` | `4` |
| `NK` | `10` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `True` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `Z*` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `uniform` |
| `TS_CONFIG` | `baroclinic_zone` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `NONE` |
| `ICE_SHELF` | `False` |
| `DT` | `3600.0` |
| `DT_THERM` | `3600.0` |
| `DAYMAX` | `20.0` |


## Domain and bottom depth


Grid: 20 x 4 points (`GRID_CONFIG = cartesian`), x from 5 to 195 kilometers, y from 5 to 35 kilometers. Bottom depth `D` from 100 to 100 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/tracer_mixing-z/notebook_8_1.png)
    


## Initial state


`Temp` from `Initial_state.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/tracer_mixing-z/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = NONE` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/tracer_mixing-z/notebook_14_0.png)
    



From `ocean.stats.nc`: 5 records; time axis in days.


## Final state


`temp` at the last record of `prog_z.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/tracer_mixing-z/notebook_16_1.png)
    

