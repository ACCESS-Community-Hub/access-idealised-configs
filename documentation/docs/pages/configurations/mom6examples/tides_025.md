# tides_025

!!! failure ":x: This configuration did not run"
    Tested on 2026-11-04 with `access-om3/2026.05.004`. Needs the OM4 1/4° grid files (`ocean_hgrid.nc`, `ocean_topog.nc`, `All_edits.nc`) in `INPUT/`, which the repository does not link (`set_grid_metrics_from_mosaic: Unable to open INPUT/ocean_hgrid.nc`).


Set-up not recorded (this run failed) ([upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/tides_025))

Configuration files: [`ocean_only/tides_025`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/tides_025) in NOAA-GFDL/MOM6-examples, at commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802): the version this run used. (The model itself is the `mom6-solo` listed under Provenance.)

GFDL excludes this example from its own automated test suite (`EXCLUDE` in [`ocean_only/Makefile`](https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/Makefile)).

!!! failure "Known issue"
    Needs the OM4 1/4° grid files (`ocean_hgrid.nc`, `ocean_topog.nc`, `All_edits.nc`) in `INPUT/`, which the repository does not link (`set_grid_metrics_from_mosaic: Unable to open INPUT/ocean_hgrid.nc`). GFDL also excludes this example from its own test suite.

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash tides_025.sh
```

where `tides_025.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "tides_025.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/tides_025.sh"
    ```

??? failure "End of the error log"
    ```text
    FATAL from PE   103:  set_grid_metrics_from_mosaic: Unable to open INPUT/ocean_hgrid.nc
    FATAL from PE     1:  set_grid_metrics_from_mosaic: Unable to open INPUT/ocean_hgrid.nc
    FATAL from PE     2:  set_grid_metrics_from_mosaic: Unable to open INPUT/ocean_hgrid.nc
    FATAL from PE     3:  set_grid_metrics_from_mosaic: Unable to open INPUT/ocean_hgrid.nc
    FATAL from PE     4:  set_grid_metrics_from_mosaic: Unable to open INPUT/ocean_hgrid.nc
    ...
    mom6-solo          0000000000412A4E  Unknown               Unknown  Unknown
    Image              PC                Routine            Line        Source             
    mom6-solo          000000000183E5BB  mpp_error_basic            80  mpp_util_mpi.inc
    mom6-solo          00000000006C2AE6  mom_error                 180  MOM_error_handler.F90
    mom6-solo          000000000075D53E  set_grid_metrics_         204  MOM_grid_initialize.F90
    mom6-solo          000000000075BFAD  set_grid_metrics           92  MOM_grid_initialize.F90
    mom6-solo          000000000075A117  mom_initialize_fi          82  MOM_fixed_initialization.F90
    mom6-solo          0000000000466C8A  initialize_mom           2881  MOM.F90
    mom6-solo          00000000004387C5  mom6                      284  MOM_driver.F90
    mom6-solo          0000000000412B2D  Unknown               Unknown  Unknown
    libc-2.28.so       000014AECA50F865  __libc_start_main     Unknown  Unknown
    mom6-solo          0000000000412A4E  Unknown               Unknown  Unknown
    Image              PC                Routine            Line        Source             
    mom6-solo          000000000183E5BB  mpp_error_basic            80  mpp_util_mpi.inc
    mom6-solo          00000000006C2AE6  mom_error                 180  MOM_error_handler.F90
    mom6-solo          000000000075D53E  set_grid_metrics_         204  MOM_grid_initialize.F90
    mom6-solo          000000000075BFAD  set_grid_metrics           92  MOM_grid_initialize.F90
    mom6-solo          000000000075A117  mom_initialize_fi          82  MOM_fixed_initialization.F90
    mom6-solo          0000000000466C8A  initialize_mom           2881  MOM.F90
    mom6-solo          00000000004387C5  mom6                      284  MOM_driver.F90
    mom6-solo          0000000000412B2D  Unknown               Unknown  Unknown
    libc-2.28.so       0000146D68C67865  __libc_start_main     Unknown  Unknown
    mom6-solo          0000000000412A4E  Unknown               Unknown  Unknown
    [gadi-cpu-spr-0187.gadi.nci.org.au:2569953] 479 more processes have sent help message help-mpi-api.txt / mpi-abort
    [gadi-cpu-spr-0187.gadi.nci.org.au:2569953] Set MCA parameter "orte_base_help_aggregate" to 0 to see all help / error messages
    ```

## What we got

## Provenance

| What | Value |
|---|---|
| MOM6-examples | [`c1730b8efe16cf7f12fc8db588115cae50f3e802`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802) |
| ACCESS-OM3 module | `access-om3/2026.05.004` |
| MOM6 source code | `ACCESS-NRI/MOM6 2026.05.003 d11a149ccba676d524312328f7eb62560a156dc3` |
| Executable | `/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access-mom6-2026.05.003-ld7hklzo5ajizx5u4yl74i4ijberrpv6/bin/mom6-solo` |
| Executable md5 | `4785d157c76c30d8d01baf7d0f69d218` |
| payu | `payu/1.3.6_1` (module `payu/1.3.6_1`) |
| Date tested | 2026-11-04 |
| PBS Job Id | `183115267.gadi-pbs` |
| PBS Exit Status | `1` |
| PBS Service Units | `22.24` |
| PBS NCPUs Requested | `520` |
| PBS Walltime Used | `00:01:17` |
| PBS Memory Used | `104.09GB` |

??? info "Input files and md5 hashes (from payu `manifests/input.yaml`)"
    | File | md5 | Comes from |
    |---|---|---|
    | `INPUT/MOM_channels_global_025` | `1370f6237715504e67d36784f0d6f47b` | MOM6-examples: `ocean_only/tides_025/INPUT/MOM_channels_global_025` |
    | `INPUT/interface_IC_2layer.cdl` | `c851a96db606df249b191e56aaca33a8` | MOM6-examples: `ocean_only/tides_025/INPUT/interface_IC_2layer.cdl` |

??? info "Parameters differing from the upstream MOM_parameter_doc.all (367)"
    Comparison of this run's `MOM_parameter_doc.all` with the upstream MOM_parameter_doc.all.
    Differences show where the ACCESS-OM3 MOM6 version adds, drops or changes default parameters.

    Only upstream: `ADD_LES_VISCOSITY`, `ADIABATIC`, `ADJUST_BT_CONT`, `AH`, `AH_TIME_SCALE`, `AH_VEL_SCALE`, `ALLOW_LANDMASK_CHANGES`, `ALTERNATE_FIRST_DIRECTION`, `ANALYTIC_FV_PGF`, `ANGSTROM`, `ANISOTROPIC_VISCOSITY`, `APPLY_INTERFACE_FILTER`, `AVAILABLE_DIAGS_FILE`, `BAD_VAL_COLUMN_THICKNESS`, `BAD_VAL_SSH_MAX`, `BAD_VAL_SSS_MAX`, `BAD_VAL_SST_MAX`, `BAD_VAL_SST_MIN`, `BAROTROPIC_2018_ANSWERS`, `BAROTROPIC_ANSWER_DATE`, `BAROTROPIC_TIDAL_SAL_BUG`, `BATHYMETRY_AT_VEL`, `BBL_THICK_MIN`, `BBL_USE_TIDAL_BG`, `BE`, `BEBT`, `BEGW`, `BETTER_BOUND_AH`, `BETTER_BOUND_KH`, `BIHARMONIC`, `BOTTOMDRAGLAW`, `BOUNDARY_EXTRAPOLATION_PRESSURE`, `BOUND_AH`, `BOUND_BT_CORRECTION`, `BOUND_CORIOLIS`, `BOUND_CORIOLIS_BIHARM`, `BOUND_CORIOLIS_VEL`, `BOUND_KH`, `BOUSSINESQ`, `BT_CONT_CORR_BOUNDS`, `BT_CORIOLIS_SCALE`, `BT_LINEAR_WAVE_DRAG`, `BT_NONLIN_STRESS`, `BT_PROJECT_VELOCITY`, `BT_STRONG_DRAG`, `BT_THICK_SCHEME`, `BT_USE_LAYER_FLUXES`, `BT_USE_OLD_CORIOLIS_BRACKET_BUG`, `BT_USE_VISC_REM_U_UH0`, `BULKMIXEDLAYER`, `BUOY_CONFIG`, `CALCULATE_APE`, `CALC_RHO_FOR_SEA_LEVEL`, `CDRAG`, `CFL_BASED_TRUNCATIONS`, `CFL_REPORT`, `CFL_TRUNCATE`, `CFL_TRUNCATE_RAMP_TIME`, `CFL_TRUNCATE_START`, `CHANNEL_CONFIG`, `CHANNEL_DRAG`, `CHANNEL_DRAG_MAX_BBL_THICK`, `CHANNEL_LIST_360_LON_CHECK`, `CHANNEL_LIST_FILE`, `CHECK_BAD_SURFACE_VALS`, `CHECK_DIFFUSIVE_CFL`, `CLIP_BT_VELOCITY`, `COMPLETE_DOCUMENTATION`, `CONTINUITY_CFL_LIMIT`, `CONTINUITY_SCHEME`, `CONT_PPM_AGGRESS_ADJUST`, `CONT_PPM_BETTER_ITER`, `CONT_PPM_MARGINAL_FACE_AREAS`, `CONT_PPM_USE_VISC_REM_MAX`, `CONT_PPM_VOLUME_BASED_CFL`, `CONVERT_THICKNESS_UNITS`, `COORD_CONFIG`, `CORIOLIS_EN_DIS`, `CORIOLIS_SCHEME`, `CORRECT_BBL_BOUNDS`, `CPU_TIME_FILE`, `DATE_STAMPED_STDOUT`, `DAYMAX`, `DEFAULT_2018_ANSWERS`, `DEFAULT_ANSWER_DATE`, `DEPRESS_INITIAL_SURFACE`, `DEPTH_LIST_FILE`, `DEPTH_LIST_MIN_INC`, `DEPTH_SCALED_KHTH`, `DETANGLE_INTERFACES`, `DIABATIC_FIRST`, `DIAG_AS_CHKSUM`, `DIAG_COORDS`, `DIAG_COORD_DEF_Z`, `DIAG_EBT_MONO_N2_COLUMN_FRACTION`, `DIAG_EBT_MONO_N2_DEPTH`, `DIAG_MISVAL`, `DIFFUSE_ML_TO_INTERIOR`, `DIRECT_STRESS`, `DOCUMENT_FILE`, `DO_DYNAMICS`, `DO_SPPT`, `DRAG_AS_BODY_FORCE`, `DRAG_BG_VEL`, `DT`, `DTBT`, `DTBT_RESET_PERIOD`, `DT_BT_FILTER`, `DT_FORCING`, `DT_THERM`, `DYNAMIC_SURFACE_PRESSURE`, `DYNAMIC_VISCOUS_ML`, `ENABLE_THERMODYNAMICS`, `ENERGYFILE`, `ENERGYSAVEDAYS`, `ENERGYSAVEDAYS_GEOMETRIC`, `ENSEMBLE_OCEAN`, `ETA_TOLERANCE`, `FATAL_INCONSISTENT_RESTART_TIME`, `FATAL_UNUSED_CHANNEL_WIDTHS`, `FIRST_DIRECTION`, `FIXED_DEPTH_LOTW_ML`, `FIX_USTAR_GUSTLESS_BUG`, `GFS`, `GILL_EQUATORIAL_LD`, `GINT`, `GRADUAL_BT_ICS`, `GRID_CONFIG`, `GRID_FILE`, `GRID_ROTATION_ANGLE_BUGS`, `GUST_CONST`, `G_BT_EXTRA`, `G_EARTH`, `HARMONIC_BL_SCALE`, `HARMONIC_VISC`, `HBBL`, `HFREEZE`, `HMIX_FIXED`, `HMIX_SFC_PROP`, `HMIX_STRESS`, `HMIX_UV_SFC_PROP`, `HOMOGENIZE_FORCINGS`, `HORVISC_BOUND_COEF`, `HOR_VISC_2018_ANSWERS`, `HOR_VISC_ANSWER_DATE`, `HTBL_SHELF`, `HTBL_SHELF_MIN`, `H_TO_KG_M2`, `ICE_SHELF`, `IC_OUTPUT_FILE`, `INIT_LAYERS_FROM_Z_FILE`, `INPUTDIR`, `INTEGRAL_BT_CONTINUITY`, `INTERFACE_IC_FILE`, `INTERFACE_IC_VAR`, `INTERNAL_WAVE_SPEED_BETTER_EST`, `INTERNAL_WAVE_SPEED_MIN`, `INTERNAL_WAVE_SPEED_TOL`, `INTERPOLATE_P_SURF`, `INTERPOLATE_RES_FN`, `KD_GL90_USE_EBT_STRUCT`, `KD_SMOOTH`, `KE_SCHEME`, `KH`, `KHTH`, `KHTH_MAX`, `KHTH_MAX_CFL`, `KHTH_MIN`, `KHTH_SLOPE_CFF`, `KHTH_SLOPE_MAX`, `KHTH_USE_EBT_STRUCT`, `KHTH_USE_FGNV_STREAMFUNCTION`, `KHTR`, `KHTR_MAX`, `KHTR_MIN`, `KHTR_PASSIVITY_COEFF`, `KHTR_PASSIVITY_MIN`, `KHTR_SLOPE_CFF`, `KH_BG_MIN`, `KH_ETA_CONST`, `KH_ETA_VEL_SCALE`, `KH_RES_FN_POWER`, `KH_RES_SCALE_COEF`, `KH_SIN_LAT`, `KH_VEL_SCALE`, `KV`, `KV_BBL_MIN`, `KV_ML_INVZ2`, `KV_TBL_MIN`, `LAPLACIAN`, `LATENT_HEAT_FUSION`, `LATENT_HEAT_VAPORIZATION`, `LEITH_AH`, `LEITH_KH`, `LINEARIZED_BT_CORIOLIS`, `LINEAR_DRAG`, `LOTW_VISCOUS_ML_FLOOR`, `MASKING_DEPTH`, `MASS_WEIGHT_IN_PRESSURE_GRADIENT`, `MAXCFL_BT_CONT`, `MAXCPU`, `MAXIMUM_DEPTH`, `MAXTRUNC`, `MAXVEL`, `MAX_ENERGY`, `MAX_FIELDS`, `MAX_TR_DIFFUSION_CFL`, `MEKE_GEOMETRIC`, `MEKE_GM_SRC_ALT`, `MINIMAL_DOCUMENTATION`, `MINIMUM_DEPTH`, `MIXEDLAYER_RESTRAT`, `MONOTONIC_CONTINUITY`, `NIGLOBAL`, `NIHALO`, `NJGLOBAL`, `NJHALO`, `NK`, `NOSLIP`, `NUM_DIAG_COORDS`, `OBC_NUMBER_OF_SEGMENTS`, `OBSOLETE_DIAGNOSTIC_IS_FATAL`, `ODA_INCUPD`, `OFFLINE_TRACER_MODE`, `OMEGA`, `PARALLEL_RESTARTFILES`, `PERT_EPBL`, `PORBAR_ANSWER_DATE`, `PORBAR_ETA_INTERP`, `PORBAR_MASKING_DEPTH`, `PRANDTL_TURB`, `PRESSURE_RECONSTRUCTION_SCHEME`, `PV_ADV_SCHEME`, `RAD_EARTH`, `READ_DEPTH_LIST`, `READ_GUST_2D`, `READ_KHTH`, `RECALC_NEUTRAL_SURF`, `RECONSTRUCT_FOR_PRESSURE`, `REENTRANT_X`, `REENTRANT_Y`, `REFERENCE_HEIGHT`, `REMAPPING_2018_ANSWERS`, `REMAPPING_ANSWER_DATE`, `REQUIRE_DEPTH_LIST_CHECKSUMS`, `RESOLN_SCALED_KH`, `RESOLN_SCALED_KHTH`, `RESOLN_SCALED_KHTR`, `RESOLN_USE_EBT`, `RESTARTFILE`, `RESTART_CHECKSUMS_REQUIRED`, `RESTART_CONTROL`, `RESTINT`, `RESTOREBUOY`, `RE_AH`, `RHO_0`, `ROTATION`, `SADOURNY`, `SAVE_INITIAL_CONDS`, `SEND_LOG_TO_STDOUT`, `SET_VISC_2018_ANSWERS`, `SET_VISC_ANSWER_DATE`, `SIMPLE_2ND_PPM_CONTINUITY`, `SINGLE_STEPPING_CALL`, `SMAGORINSKY_AH`, `SMAGORINSKY_KH`, `SMAG_BI_CONST`, `SMAG_CONST_CHANNEL`, `SPLIT`, `SPLIT_BOTTOM_STRESS`, `SPONGE`, `SSH_EXTRA`, `STOKES_MIXING_COMBINED`, `STORE_CORIOLIS_ACCEL`, `SUBGRID_TOPO_AT_VEL`, `SURFACE_2018_ANSWERS`, `SURFACE_ANSWER_DATE`, `THERMO_SPANS_COUPLING`, `THICKNESSDIFFUSE`, `THICKNESS_CONFIG`, `TIDAL_SAL_FROM_FILE`, `TIDAL_SAL_SHT`, `TIDES`, `TIDE_K1`, `TIDE_K2`, `TIDE_M2`, `TIDE_M2_AMP`, `TIDE_M2_FREQ`, `TIDE_M2_PHASE_T0`, `TIDE_MF`, `TIDE_MM`, `TIDE_N2`, `TIDE_O1`, `TIDE_P1`, `TIDE_Q1`, `TIDE_REF_DATE`, `TIDE_S2`, `TIDE_SAL_SCALAR_VALUE`, `TIDE_USE_EQ_PHASE`, `TIDE_USE_SAL_SCALAR`, `TIMEUNIT`, `TOPO_CONFIG`, `TOPO_EDITS_FILE`, `TOPO_FILE`, `TOPO_VARNAME`, `TRACER_ADVECTION_SCHEME`, `TRIM_IC_FOR_P_SURF`, `TRIPOLAR_N`, `UPWIND_1ST_CONTINUITY`, `USE_ADVECTION_TEST_TRACER`, `USE_BOUNDARY_IMPULSE_TRACER`, `USE_BT_CONT_TYPE`, `USE_CFC_CAP`, `USE_CONTEMP_ABSSAL`, `USE_DBCLIENT`, `USE_DIABATIC_TIME_BUG`, `USE_DOME_TRACER`, `USE_DYED_OBC_TRACER`, `USE_EOS`, `USE_GL90_IN_SSW`, `USE_GME`, `USE_GM_WORK_BUG`, `USE_GRID_SPACE_DIAGNOSTIC_AXES`, `USE_IDEAL_AGE_TRACER`, `USE_INACCURATE_PGF_RHO_ANOM`, `USE_ISOMIP_TRACER`, `USE_KH_BG_2D`, `USE_KH_IN_MEKE`, `USE_LAND_MASK_FOR_HVISC`, `USE_LATERAL_BOUNDARY_DIFFUSION`, `USE_MEKE`, `USE_NEUTRAL_DIFFUSION`, `USE_NW2_TRACERS`, `USE_OCMIP2_CFC`, `USE_OIL_TRACER`, `USE_PARTICLES`, `USE_POROUS_BARRIER`, `USE_PREVIOUS_TIDES`, `USE_PSEUDO_SALT_TRACER`, `USE_QG_LEITH_GM`, `USE_REGIONAL_DYES`, `USE_REGRIDDING`, `USE_RGC_TRACER`, `USE_STANLEY_GM`, `USE_STANLEY_ISO`, `USE_STANLEY_PGF`, `USE_STORED_SLOPES`, `USE_TRIPOLAR_GEOLONB_BUG`, `USE_USER_TRACER_EXAMPLE`, `USE_VARIABLE_MIXING`, `USE_VISBECK`, `USE_WAVES`, `VARIABLE_BUOYFORCE`, `VARIABLE_WINDS`, `VELOCITY_CONFIG`, `VELOCITY_TOLERANCE`, `VEL_UNDERFLOW`, `VERT_FRICTION_2018_ANSWERS`, `VERT_FRICTION_ANSWER_DATE`, `VERY_SMALL_FREQUENCY`, `VISC_RES_FN_POWER`, `VISC_RES_SCALE_COEF`, `VON_KARMAN_CONST`, `WIND_CONFIG`, `WRITE_CPU_STEPS`, `WRITE_GEOM`, `WRITE_STOCKS`

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/tides_025 (written by tides_025.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 480
    walltime: 01:00:00
    jobname: tides_025
    experiment: tides_025
    laboratory: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab

    model: mom6
    exe: mom6-solo           # found on PATH once the module below is loaded
    input: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/MOM6-examples/ocean_only/tides_025/INPUT

    modules:
      use:
        - /g/data/vk83/modules
      load:
        - access-om3/2026.05.004

    storage:                 # vk83: executable, ol01: input data
      gdata:
        - vk83
        - ol01

    collate: false           # mom6 writes un-split netCDF files when IO_LAYOUT = 1,1
    runlog: false            # don't commit run logs into the MOM6-examples clone
    metadata:
      enable: false
    ```

