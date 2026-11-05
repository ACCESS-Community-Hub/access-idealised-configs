
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `300` |
| `NJGLOBAL` | `180` |
| `NK` | `80` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `Z*` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `coord` |
| `TS_CONFIG` | `SCM_CVMix_tests` |
| `WIND_CONFIG` | `ideal_hurr` |
| `BUOY_CONFIG` | `const` |
| `ICE_SHELF` | `False` |
| `DT` | `300.0` |
| `DT_THERM` | `300.0` |
| `DAYMAX` | `0.05` |


## Domain and bottom depth


Grid: 300 x 180 points (`GRID_CONFIG = cartesian`), x from 5 to 2995 kilometers, y from 5 to 1795 kilometers. Bottom depth `D` from 4000 to 4000 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/idealized_hurricane/notebook_8_1.png)
    


## Initial state


MOM6 did not write an initial-state file for this run (it does when `SAVE_INITIAL_CONDS = True`), so the initial state is not shown here; see the run's `MOM_parameter_doc.all` (`THICKNESS_CONFIG = coord`, `TS_CONFIG = SCM_CVMix_tests`).


## Surface forcing


Time-mean of the surface forcing saved in the diagnostics: `taux` (Zonal surface stress from ocean interactions with atmos and ice, from `surffluxes.nc`), `tauy` (Meridional surface stress ocean interactions with atmos and ice, from `surffluxes.nc`).



    
![png](@ASSETS@/tested-configs/notebooks/idealized_hurricane/notebook_12_1.png)
    



    
![png](@ASSETS@/tested-configs/notebooks/idealized_hurricane/notebook_12_2.png)
    


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/idealized_hurricane/notebook_14_0.png)
    



From `ocean.stats.nc`: 2 records; time axis in days.


## Final state


`temp` at the last record of `prog.nc` (average over the last output interval).



    
![png](@ASSETS@/tested-configs/notebooks/idealized_hurricane/notebook_16_1.png)
    

