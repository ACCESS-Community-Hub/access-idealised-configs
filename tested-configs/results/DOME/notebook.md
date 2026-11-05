
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `150` |
| `NJGLOBAL` | `70` |
| `NK` | `25` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `DOME` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `False` |
| `ENABLE_THERMODYNAMICS` | `False` |
| `THICKNESS_CONFIG` | `DOME` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `zero` |
| `ICE_SHELF` | `False` |
| `DT` | `1200.0` |
| `DT_THERM` | `3600.0` |
| `DAYMAX` | `2.0` |


## Domain and bottom depth


Grid: 150 x 70 points (`GRID_CONFIG = cartesian`), x from 5 to 1495 kilometers, y from 5 to 695 kilometers. Bottom depth `D` from 0.5 to 3600 m (`TOPO_CONFIG = DOME`).



    
![png](@ASSETS@/tested-configs/notebooks/DOME/notebook_8_1.png)
    


## Initial state


MOM6 did not write an initial-state file for this run (it does when `SAVE_INITIAL_CONDS = True`), so the initial state is not shown here; see the run's `MOM_parameter_doc.all` (`THICKNESS_CONFIG = DOME`, `TS_CONFIG = n/a`).


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = zero` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/DOME/notebook_14_0.png)
    



From `ocean.stats.nc`: 3 records; time axis in days.


## Final state


No diagnostic output with a varying field was written for this run.

