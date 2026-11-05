
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `44` |
| `NJGLOBAL` | `40` |
| `NK` | `2` |
| `GRID_CONFIG` | `spherical` |
| `TOPO_CONFIG` | `spoon` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `False` |
| `ENABLE_THERMODYNAMICS` | `False` |
| `THICKNESS_CONFIG` | `uniform` |
| `WIND_CONFIG` | `2gyre` |
| `BUOY_CONFIG` | `zero` |
| `ICE_SHELF` | `False` |
| `DT` | `1200.0` |
| `DT_THERM` | `2400.0` |
| `DAYMAX` | `10.0` |


## Domain and bottom depth


Grid: 44 x 40 points (`GRID_CONFIG = spherical`), x from 0.25 to 21.75 degrees_east, y from 30.25 to 49.75 degrees_north. Bottom depth `D` from 105.179 to 2000 m (`TOPO_CONFIG = spoon`).



    
![png](@ASSETS@/tested-configs/notebooks/double_gyre/notebook_8_1.png)
    


## Initial state


MOM6 did not write an initial-state file for this run (it does when `SAVE_INITIAL_CONDS = True`), so the initial state is not shown here; see the run's `MOM_parameter_doc.all` (`THICKNESS_CONFIG = uniform`, `TS_CONFIG = n/a`).


## Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = 2gyre` and `BUOY_CONFIG = zero` (see the MOM6 documentation for these options).


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/double_gyre/notebook_14_0.png)
    



From `ocean.stats.nc`: 11 records; time axis in days.


## Final state


`e` at the last record of `prog__0001_006.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/double_gyre/notebook_16_1.png)
    

