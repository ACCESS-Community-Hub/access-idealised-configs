
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `25` |
| `NJGLOBAL` | `25` |
| `NK` | `10` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `False` |
| `ENABLE_THERMODYNAMICS` | `False` |
| `THICKNESS_CONFIG` | `circle_obcs` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `zero` |
| `ICE_SHELF` | `False` |
| `DT` | `120.0` |
| `DT_THERM` | `120.0` |
| `DAYMAX` | `2.0` |


## Domain and bottom depth


Grid: 25 x 25 points (`GRID_CONFIG = cartesian`), x from 2 to 98 kilometers, y from 2 to 98 kilometers. Bottom depth `D` from 600 to 600 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/circle_obcs/notebook_8_1.png)
    


## Initial state


`h` from `GOLD_IC.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/circle_obcs/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = zero` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/circle_obcs/notebook_14_0.png)
    



From `ocean.stats.nc`: 5 records; time axis in hours.


## Final state


`h` at the last record of `prog.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/circle_obcs/notebook_16_1.png)
    

