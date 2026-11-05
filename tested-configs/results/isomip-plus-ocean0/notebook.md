
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `240` |
| `NJGLOBAL` | `40` |
| `NK` | `36` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `ISOMIP` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `SIGMA_SHELF_ZSTAR` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `ISOMIP` |
| `TS_CONFIG` | `ISOMIP` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `NONE` |
| `ICE_SHELF` | `True` |
| `DT` | `720.0` |
| `DT_THERM` | `720.0` |
| `DAYMAX` | `90.0` |


## Domain and bottom depth


Grid: 240 x 40 points (`GRID_CONFIG = cartesian`), x from 321 to 799 kilometers, y from 1 to 79 kilometers. Bottom depth `D` from 104.607 to 720 m (`TOPO_CONFIG = ISOMIP`).



    
![png](@ASSETS@/tested-configs/notebooks/isomip-plus-ocean0/notebook_8_1.png)
    


## Initial state


MOM6 did not write an initial-state file for this run (it does when `SAVE_INITIAL_CONDS = True`), so the initial state is not shown here; see the run's `MOM_parameter_doc.all` (`THICKNESS_CONFIG = ISOMIP`, `TS_CONFIG = ISOMIP`).


## Surface forcing


Time-mean of the surface forcing saved in the diagnostics: `PRCmE` (Net surface water flux (precip+melt+lrunoff+ice calving-evap), from `forcing.nc`), `ustar` (Surface friction velocity = [(gustiness + tau_magnitude)/rho0]^(1/2), from `forcing.nc`).



    
![png](@ASSETS@/tested-configs/notebooks/isomip-plus-ocean0/notebook_12_1.png)
    



    
![png](@ASSETS@/tested-configs/notebooks/isomip-plus-ocean0/notebook_12_2.png)
    


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/isomip-plus-ocean0/notebook_14_0.png)
    



From `ocean.stats.nc`: 721 records; time axis in days.


## Final state


`temp` at the last record of `ave_prog.nc` (average over the last output interval).



    
![png](@ASSETS@/tested-configs/notebooks/isomip-plus-ocean0/notebook_16_1.png)
    

