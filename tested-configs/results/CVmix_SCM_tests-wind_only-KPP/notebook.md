
## Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `2` |
| `NJGLOBAL` | `2` |
| `NK` | `400` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `True` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `Z*` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `coord` |
| `TS_CONFIG` | `SCM_CVMix_tests` |
| `WIND_CONFIG` | `const` |
| `BUOY_CONFIG` | `zero` |
| `ICE_SHELF` | `False` |
| `DT` | `1200.0` |
| `DT_THERM` | `1200.0` |
| `DAYMAX` | `5.0` |


## Domain and bottom depth


Grid: 2 x 2 points (`GRID_CONFIG = cartesian`), x from 0.5 to 1.5 degrees_east, y from 28.336 to 29.336 degrees_north. Bottom depth `D` from 400 to 400 m (`TOPO_CONFIG = flat`).



    
![png](@ASSETS@/tested-configs/notebooks/CVmix_SCM_tests-wind_only-KPP/notebook_8_1.png)
    


## Initial state


`Temp` from `MOM_IC.nc`, which MOM6 writes with the initial state.



    
![png](@ASSETS@/tested-configs/notebooks/CVmix_SCM_tests-wind_only-KPP/notebook_10_1.png)
    


## Surface forcing


Time-mean of the surface forcing saved in the diagnostics: `taux` (Zonal surface stress from ocean interactions with atmos and ice, from `surffluxes.nc`), `ustar` (Surface friction velocity = [(gustiness + tau_magnitude)/rho0]^(1/2), from `surffluxes.nc`).



    
![png](@ASSETS@/tested-configs/notebooks/CVmix_SCM_tests-wind_only-KPP/notebook_12_1.png)
    



    
![png](@ASSETS@/tested-configs/notebooks/CVmix_SCM_tests-wind_only-KPP/notebook_12_2.png)
    


## Energy and stability through the run


    
![png](@ASSETS@/tested-configs/notebooks/CVmix_SCM_tests-wind_only-KPP/notebook_14_0.png)
    



From `ocean.stats.nc`: 21 records; time axis in days.


## Final state


`temp` at the last record of `prog_z.nc` (snapshot).



    
![png](@ASSETS@/tested-configs/notebooks/CVmix_SCM_tests-wind_only-KPP/notebook_16_1.png)
    

