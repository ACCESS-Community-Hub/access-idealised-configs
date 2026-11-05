
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `60` |
| `NJGLOBAL` | `80` |
| `NK` | `2` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `False` |
| `ENABLE_THERMODYNAMICS` | `False` |
| `THICKNESS_CONFIG` | `phillips` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `zero` |
| `ICE_SHELF` | `False` |
| `DT` | `600.0` |
| `DT_THERM` | `1800.0` |
| `DAYMAX` | `20.0` |


## Domain and bottom depth


Grid: 60 x 80 points (`GRID_CONFIG = cartesian`), x from 10 to 1190 kilometers, y from 10 to 1590 kilometers. Bottom depth `D` from 2000 to 2000 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/Phillips_2layer/notebook_8_1.png)
    


## Initial state


`h` from `MOM_IC.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/Phillips_2layer/notebook_10_1.png)
    


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = zero` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/Phillips_2layer/notebook_14_0.png)
    



From `ocean.stats.nc`: 21 records; time axis in days.


## Final state


`h` at the last record of `prog.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/Phillips_2layer/notebook_16_1.png)
    

