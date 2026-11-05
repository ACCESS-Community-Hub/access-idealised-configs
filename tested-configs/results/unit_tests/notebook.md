
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `4` |
| `NJGLOBAL` | `4` |
| `NK` | `1` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `False` |
| `ENABLE_THERMODYNAMICS` | `False` |
| `THICKNESS_CONFIG` | `uniform` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `zero` |
| `ICE_SHELF` | `False` |
| `DT` | `8.64E+04` |
| `DT_THERM` | `8.64E+04` |
| `DAYMAX` | `1.0` |


## Domain and bottom depth


Grid: 4 x 4 points (`GRID_CONFIG = cartesian`), x from 0.125 to 0.875 degrees_east, y from 0.125 to 0.875 degrees_north. Bottom depth `D` from 100 to 100 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/unit_tests/notebook_8_1.png)
    


## Initial state


MOM6 did not write an initial-state file for this run (it does when `SAVE_INITIAL_CONDS = True`), so the initial state is not shown here; see the run's `MOM_parameter_doc.all` (`THICKNESS_CONFIG = uniform`, `TS_CONFIG = n/a`).


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = zero` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/unit_tests/notebook_14_0.png)
    



From `ocean.stats.nc`: 2 records; time axis in days.


## Final state


No diagnostic output with a varying field was written for this run.

