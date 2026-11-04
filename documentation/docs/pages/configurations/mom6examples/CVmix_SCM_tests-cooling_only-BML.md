# CVmix_SCM_tests / cooling_only / BML

CVMix single-column test: `cooling_only` surface forcing with the `BML` boundary-layer scheme.

Upstream configuration: [`ocean_only/CVmix_SCM_tests/cooling_only/BML`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/CVmix_SCM_tests/cooling_only/BML) (MOM6-examples commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802)).

!!! failure "Known issue"
    The bulk-mixed-layer (BML) cases read `isopyc_coords.nc` from the run directory (`COORD_FILE = "isopyc_coords.nc"`, `INPUTDIR = "."`), but upstream only links that file in `common_BML/`, not in the `*/BML` directories, so MOM6 stops with `set_coord_from_file: Unable to open ./isopyc_coords.nc`. GFDL's restart-test script (`tools/MRS/setup_restart_test.sh`) copies the file in by hand. The ePBL and KPP versions of the same tests run.

!!! failure "Tested: this example did NOT run successfully"
    See the details below; the log tail shows where it stopped.

!!! note "Generated with Claude Code"
    This page, the script and the figure were generated automatically by [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs) (written with Claude Code). See [How these pages were made](../Overview.md#how-these-pages-were-made).

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash CVmix_SCM_tests-cooling_only-BML.sh
```

where `CVmix_SCM_tests-cooling_only-BML.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "CVmix_SCM_tests-cooling_only-BML.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/CVmix_SCM_tests-cooling_only-BML.sh"
    ```

??? failure "End of the error log"
    ```text
    FATAL:  set_coord_from_file: Unable to open ./isopyc_coords.nc
    ...


    WARNING: Open_file is appending .nc to the filename ./ocean_geometry


    FATAL:  set_coord_from_file: Unable to open ./isopyc_coords.nc

    Image              PC                Routine            Line        Source             
    mom6-solo          000000000183E5BB  mpp_error_basic            80  mpp_util_mpi.inc
    mom6-solo          00000000006C2AE6  mom_error                 180  MOM_error_handler.F90
    mom6-solo          00000000007585E1  set_coord_from_fi         467  MOM_coord_initialization.F90
    mom6-solo          000000000075582F  mom_initialize_co          92  MOM_coord_initialization.F90
    mom6-solo          000000000046E543  initialize_mom           3164  MOM.F90
    mom6-solo          00000000004387C5  mom6                      284  MOM_driver.F90
    mom6-solo          0000000000412B2D  Unknown               Unknown  Unknown
    libc-2.28.so       000014B7262B8865  __libc_start_main     Unknown  Unknown
    mom6-solo          0000000000412A4E  Unknown               Unknown  Unknown
    --------------------------------------------------------------------------
    MPI_ABORT was invoked on rank 0 in communicator MPI_COMM_WORLD
    with errorcode 1.

    NOTE: invoking MPI_ABORT causes Open MPI to kill all MPI processes.
    You may or may not see output from other processes, depending on
    exactly when Open MPI kills them.
    --------------------------------------------------------------------------
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
| PBS Job Id | `183115173.gadi-pbs` |
| PBS Exit Status | `1` |
| PBS Service Units | `0.01` |
| PBS NCPUs Requested | `1` |
| PBS Walltime Used | `00:00:15` |
| PBS Memory Used | `1.15GB` |

This example needs no input files: grid, bathymetry, initial state and forcing are all set analytically in `MOM_input`.

??? info "Parameters differing from the upstream MOM_parameter_doc.all (432)"
    Comparison of this run's `MOM_parameter_doc.all` with the upstream MOM_parameter_doc.all.
    Differences show where the ACCESS-OM3 MOM6 version adds, drops or changes default parameters.

    Only upstream: `ABSORB_ALL_SW`, `ADIABATIC`, `AGGREGATE_FW_FORCING`, `ALLOWED_DETRAIN_SALT_CHG`, `ALLOWED_DETRAIN_TEMP_CHG`, `ALTERNATE_FIRST_DIRECTION`, `ANALYTIC_FV_PGF`, `ANGSTROM`, `APPLY_INTERFACE_FILTER`, `AVAILABLE_DIAGS_FILE`, `AXIS_UNITS`, `BACKSCAT_EBT_POWER`, `BATHYMETRY_AT_VEL`, `BBL_EFFIC`, `BBL_MIXING_AS_MAX`, `BBL_MIXING_MAX_DECAY`, `BBL_THICK_MIN`, `BBL_USE_EOS`, `BBL_USE_TIDAL_BG`, `BETA`, `BETA_LAT_REF`, `BIHARMONIC`, `BMLD_EN_VALS`, `BML_NONBOUSINESQ`, `BML_USTAR_MIN`, `BOTTOMDRAGLAW`, `BOUNDARY_EXTRAPOLATION_PRESSURE`, `BOUND_CORIOLIS`, `BOUND_SALINITY`, `BOUSSINESQ`, `BRYAN_LEWIS_DIFFUSIVITY`, `BS_USE_SQG_STRUCT`, `BUFFER_LAYER_EXTRAP_LIMIT`, `BUFFER_LAYER_HMIN_REL`, `BUFFER_LAYER_HMIN_THICK`, `BUFFER_LAY_DETRAIN_TIME`, `BUFFER_SPLIT_RHO_TOL`, `BULKMIXEDLAYER`, `BULKML_CONV_MOMENTUM_BUG`, `BULK_RI_CONVECTIVE`, `BULK_RI_ML`, `BUOY_CONFIG`, `CALCULATE_APE`, `CALCULATE_SAL`, `CALC_RHO_FOR_SEA_LEVEL`, `CDRAG`, `CDRAG_MAP`, `CFL_REPORT`, `CFL_TRUNCATE`, `CFL_TRUNCATE_RAMP_TIME`, `CFL_TRUNCATE_START`, `CHANNEL_CONFIG`, `CHANNEL_DRAG`, `CHECK_BAD_SURFACE_VALS`, `CHECK_DIFFUSIVE_CFL`, `COMPLETE_DOCUMENTATION`, `CONTINUITY_CFL_LIMIT`, `CONT_PPM_AGGRESS_ADJUST`, `CONT_PPM_BETTER_ITER`, `CONT_PPM_MARGINAL_FACE_AREAS`, `CONT_PPM_USE_VISC_REM_MAX`, `CONT_PPM_VOLUME_BASED_CFL`, `CONT_USE_H_MARG_MIN`, `COORD_CONFIG`, `COORD_FILE`, `COORD_VAR`, `CORIOLIS_EN_DIS`, `CORIOLIS_SCHEME`, `CORRECTION_INTXPA`, `CORRECT_ABSORPTION_DEPTH`, `CORRECT_BBL_BOUNDS`, `CPU_TIME_FILE`, `C_P`, `DATE_STAMPED_STDOUT`, `DAYMAX`, `DEFAULT_ANSWER_DATE`, `DEPRESS_INITIAL_SURFACE`, `DEPTH_LIMIT_FLUXES`, `DEPTH_LIST_MIN_INC`, `DEPTH_SCALED_KHTH`, `DETANGLE_INTERFACES`, `DIABATIC_FIRST`, `DIAG_AS_CHKSUM`, `DIAG_COORDS`, `DIAG_COORD_DEF_Z`, `DIAG_DEPTH_SUBML_N2`, `DIAG_EBT_MONO_N2_COLUMN_FRACTION`, `DIAG_EBT_MONO_N2_DEPTH`, `DIAG_MISVAL`, `DIAG_MLD_DENSITY_DIFF`, `DIAG_REMAPPING_USE_OM4_SUBCELLS`, `DIFFUSE_ML_TO_INTERIOR`, `DIRECT_STRESS`, `DISSIPATION_KD_MIN`, `DISSIPATION_MIN`, `DISSIPATION_N0`, `DISSIPATION_N1`, `DOCUMENT_FILE`, `DOUBLE_DIFFUSION`, `DO_BRINE_PLUME`, `DO_DYNAMICS`, `DO_GEOTHERMAL`, `DO_RIVERMIX`, `DO_SKEB`, `DO_SPPT`, `DRAG_AS_BODY_FORCE`, `DRAG_BG_VEL`, `DRAG_DIFFUSIVITY_ANSWER_DATE`, `DRHO_DP`, `DRHO_DS`, `DRHO_DT`, `DT`, `DTFREEZE_DP`, `DTFREEZE_DS`, `DT_FORCING`, `DT_THERM`, `DT_TRACER_ADVECT`, `DYNAMIC_VISCOUS_ML`, `DZ_BBL_AVG_MIN`, `ENABLE_BUGS_BY_DEFAULT`, `ENABLE_THERMODYNAMICS`, `ENERGETICS_SFC_PBL`, `ENERGYFILE`, `ENERGYSAVEDAYS`, `ENERGYSAVEDAYS_GEOMETRIC`, `ENSEMBLE_APPENDIX_PREFIX`, `ENSEMBLE_OCEAN`, `ENTRAIN_DIFFUSIVE_MAX_ENT`, `EOS_QUADRATURE`, `EPBL_IS_ADDITIVE`, `EQN_OF_STATE`, `ETA_TOLERANCE`, `EVAP_CFL_LIMIT`, `EXP_OPACITY_SCHEME`, `FATAL_INCONSISTENT_RESTART_TIME`, `FIRST_DIRECTION`, `FIXED_DEPTH_LOTW_ML`, `FLUX_RI_MAX`, `FRAZIL`, `FRICTWORK_BUG`, `F_0`, `GEOM_FILE`, `GFS`, `GRID_CONFIG`, `GRID_ROTATION_ANGLE_BUGS`, `GUST_CONST`, `G_EARTH`, `HARMONIC_BL_SCALE`, `HARMONIC_VISC`, `HBBL`, `HENYEY_IGW_BACKGROUND`, `HFREEZE`, `HMIX_MIN`, `HOMOGENIZE_FORCINGS`, `HORIZ_VARYING_BACKGROUND`, `HREF_FOR_MLD`, `HTBL_SHELF`, `HTBL_SHELF_MIN`, `H_TO_M`, `ICE_SHELF`, `IC_OUTPUT_FILE`, `INIT_LAYERS_FROM_Z_FILE`, `INPUTDIR`, `INTERNAL_TIDES`, `INTERNAL_WAVE_SPEED_BETTER_EST`, `INTERNAL_WAVE_SPEED_MIN`, `INTERNAL_WAVE_SPEED_TOL`, `INTERPOLATE_P_SURF`, `INTWAVE_REMAPPING_USE_OM4_SUBCELLS`, `INT_TIDE_DISSIPATION`, `ISO_DATE_STAMPED_STDOUT`, `KD`, `KD_ADD`, `KD_BBL_TR`, `KD_GL90_USE_EBT_STRUCT`, `KD_GL90_USE_SQG_STRUCT`, `KD_MAX`, `KD_MIN`, `KD_MIN_TR`, `KD_SEED_KAPPA_SHEAR`, `KD_SMOOTH`, `KD_TANH_LAT_FN`, `KE_SCHEME`, `KHTH`, `KHTH_MAX`, `KHTH_MAX_CFL`, `KHTH_MIN`, `KHTH_SLOPE_CFF`, `KHTH_SLOPE_MAX`, `KHTH_USE_EBT_STRUCT`, `KHTH_USE_FGNV_STREAMFUNCTION`, `KHTH_USE_SQG_STRUCT`, `KHTR`, `KHTR_MAX`, `KHTR_MIN`, `KHTR_PASSIVITY_COEFF`, `KHTR_PASSIVITY_MIN`, `KHTR_SLOPE_CFF`, `KHTR_USE_EBT_STRUCT`, `KHTR_USE_SQG_STRUCT`, `KH_ETA_CONST`, `KH_ETA_VEL_SCALE`, `KV`, `KV_BBL_MIN`, `KV_TBL_MIN`, `LAPLACIAN`, `LATENT_HEAT_FUSION`, `LATENT_HEAT_VAPORIZATION`, `LENLAT`, `LENLON`, `LIMIT_BUFFER_DETRAIN`, `LINEAR_DRAG`, `LOTW_VISCOUS_ML_FLOOR`, `LZ_RESCALE`, `MASKING_DEPTH`, `MASSLESS_MATCH_TARGETS`, `MASS_WEIGHT_IN_PGF_VANISHED_ONLY`, `MASS_WEIGHT_IN_PRESSURE_GRADIENT`, `MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP`, `MAXCPU`, `MAXIMUM_DEPTH`, `MAXTRUNC`, `MAXVEL`, `MAX_ENERGY`, `MAX_ENT_IT`, `MAX_FIELDS`, `MAX_TR_DIFFUSION_CFL`, `MECH_TKE_FLOOR`, `MEKE_GEOMETRIC`, `MEKE_GM_SRC_ALT`, `MINIMAL_DOCUMENTATION`, `MINIMUM_DEPTH`, `MINIMUM_FORCING_DEPTH`, `MIXEDLAYER_RESTRAT`, `MIX_BOUNDARY_TRACERS`, `MLD_EN_VALS`, `ML_DT_DS_WEIGHT`, `ML_MIX_FIRST`, `ML_OMEGA_FRAC`, `ML_RADIATION`, `ML_RESORT`, `MONOTONIC_CONTINUITY`, `MSTAR`, `NIGLOBAL`, `NIHALO`, `NJGLOBAL`, `NJHALO`, `NK`, `NKBL`, `NKML`, `NOSLIP`, `NSTAR`, `NSTAR2`, `NUM_DIAG_COORDS`, `NUM_DIAG_DOWNSAMP_LEV`, `OBC_NUMBER_OF_SEGMENTS`, `OBSOLETE_DIAGNOSTIC_IS_FATAL`, `ODA_INCUPD`, `OFFLINE_TRACER_MODE`, `OMEGA`, `OPACITY_LAND_VALUE`, `OPTICS_ANSWER_DATE`, `PARALLEL_RESTARTFILES`, `PEN_SW_ABSORB_MINTHICK`, `PEN_SW_FLUX_ABSORB`, `PEN_SW_FRAC`, `PEN_SW_NBANDS`, `PEN_SW_SCALE`, `PERT_EPBL`, `PRANDTL_BKGND`, `PRESSURE_DEPENDENT_FRAZIL`, `PRESSURE_RECONSTRUCTION_SCHEME`, `PV_ADV_SCHEME`, `P_REF`, `P_REF_LINEAR_EOS`, `RAD_EARTH`, `READ_DEPTH_LIST`, `READ_GUST_2D`, `READ_KHTH`, `READ_MEAN_SEA_LEVEL`, `RECALC_NEUTRAL_SURF`, `RECLAIM_FRAZIL`, `RECONSTRUCT_FOR_PRESSURE`, `REENTRANT_X`, `REENTRANT_Y`, `REFERENCE_HEIGHT`, `REGULARIZE_SURFACE_LAYERS`, `REMAPPING_ANSWER_DATE`, `RESET_INTXPA_INTEGRAL`, `RESET_INTXPA_INTEGRAL_FLATTEST`, `RESOLN_SCALED_KH`, `RESOLN_SCALED_KHTH`, `RESOLN_SCALED_KHTR`, `RESOLN_USE_EBT`, `RESOLVE_EKMAN`, `RESTARTFILE`, `RESTART_CHECKSUMS_REQUIRED`, `RESTART_CONTROL`, `RESTART_SYMMETRIC_CHECKSUMS`, `RESTART_UNSIGNED_ZEROS`, `RESTINT`, `RESTOREBUOY`, `RHO_0`, `RHO_PGF_REF`, `RHO_REF_LINEAR_EOS`, `RHO_T0_S0`, `ROTATION`, `SALINITY_UNDERFLOW`, `SALT_EXTRACTION_LIMIT`, `SAVE_INITIAL_CONDS`, `SCM_L1_SALT`, `SCM_L1_TEMP`, `SCM_L2_DSDZ`, `SCM_L2_DTDZ`, `SCM_L2_MINTEMP`, `SCM_L2_SALT`, `SCM_L2_TEMP`, `SCM_SALT_MLD`, `SCM_TEMP_MLD`, `SEND_LOG_TO_STDOUT`, `SENSIBLE_HEAT_FLUX`, `SET_DIFF_ANSWER_DATE`, `SET_VISC_ANSWER_DATE`, `SIMPLE_2ND_PPM_CONTINUITY`, `SIMPLE_TKE_TO_KD`, `SINGLE_STEPPING_CALL`, `SOUTHLAT`, `SPLIT`, `SPONGE`, `SSH_IN_EOS_PRESSURE_FOR_PGF`, `STANLEY_COEFF`, `STOCHASTICS_ANSWER_DATE`, `STOCH_EOS`, `STOKES_MIXING_COMBINED`, `SUBGRID_TOPO_AT_VEL`, `SURFACE_ANSWER_DATE`, `SYMMETRIC_DOWNSAMPLE_SUMS`, `S_REF_LINEAR_EOS`, `TEMPERATURE_UNDERFLOW`, `TFREEZE_FORM`, `TFREEZE_S0_P0`, `TFREEZE_S_IS_PRACS`, `TFREEZE_T_IS_POTT`, `THERMO_SPANS_COUPLING`, `THICKNESSDIFFUSE`, `THICKNESS_CONFIG`, `TIDES`, `TIMEUNIT`, `TKE_BACKGROUND`, `TKE_DECAY`, `TOLERANCE_ENT`, `TOPO_CONFIG`, `TRACER_ADVECTION_SCHEME`, `TRACER_TRIDIAG`, `TRADV_SPANS_COUPLING`, `TRIM_IC_FOR_P_SURF`, `TRIPOLAR_N`, `TS_CONFIG`, `T_REF_LINEAR_EOS`, `UNSPLIT_DT_VISC_BUG`, `UPWIND_1ST_CONTINUITY`, `USER_CHANGE_DIFFUSIVITY`, `USE_ADVECTION_TEST_TRACER`, `USE_BOUNDARY_IMPULSE_TRACER`, `USE_CALVING_HEAT_CONTENT`, `USE_CFC_CAP`, `USE_CIRCULATION_IN_HORVISC`, `USE_CONTEMP_ABSSAL`, `USE_CONT_THICKNESS`, `USE_CVMIX_DDIFF`, `USE_DBCLIENT`, `USE_DOME_TRACER`, `USE_DYED_OBC_TRACER`, `USE_EOS`, `USE_GL90_IN_SSW`, `USE_GME`, `USE_GM_WORK_BUG`, `USE_HORIZONTAL_BOUNDARY_DIFFUSION`, `USE_IDEAL_AGE_TRACER`, `USE_INACCURATE_PGF_RHO_ANOM`, `USE_INDEX_DIAGNOSTIC_AXES`, `USE_ISOMIP_TRACER`, `USE_JACKSON_PARAM`, `USE_KPP`, `USE_LAND_MASK_FOR_HVISC`, `USE_LEGACY_DIABATIC_DRIVER`, `USE_LEITHY`, `USE_LMD94`, `USE_LOTW_BBL_DIFFUSIVITY`, `USE_MARBL_TRACERS`, `USE_MEKE`, `USE_NEUTRAL_DIFFUSION`, `USE_NW2_TRACERS`, `USE_OCMIP2_CFC`, `USE_OIL_TRACER`, `USE_PARTICLES`, `USE_POROUS_BARRIER`, `USE_PP81`, `USE_PSEUDO_SALT_TRACER`, `USE_PSURF_IN_EOS`, `USE_QG_LEITH_GM`, `USE_REGIONAL_DYES`, `USE_REGRIDDING`, `USE_RGC_TRACER`, `USE_RIVER_HEAT_CONTENT`, `USE_RK2`, `USE_STANLEY_GM`, `USE_STANLEY_ISO`, `USE_STANLEY_PGF`, `USE_STORED_SLOPES`, `USE_THICKNESS_DIFFUSE_ANN`, `USE_USER_TRACER_EXAMPLE`, `USE_VARIABLE_MIXING`, `USE_VISBECK`, `USE_WAVES`, `USE_ZB2020`, `USTAR_GUSTLESS_BUG`, `VARIABLE_BUOYFORCE`, `VARIABLE_WINDS`, `VAR_PEN_SW`, `VELOCITY_CONFIG`, `VELOCITY_TOLERANCE`, `VEL_UNDERFLOW`, `VERTEX_SHEAR_THICKNESS_MEAN`, `VERT_FRICTION_ANSWER_DATE`, `VERY_SMALL_FREQUENCY`, `VON_KARMAN_CONST`, `WESTLON`, `WIND_CONFIG`, `WRITE_CPU_STEPS`, `WRITE_GEOM`, `WRITE_STOCKS`

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/CVmix_SCM_tests/cooling_only/BML (written by CVmix_SCM_tests-cooling_only-BML.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 1
    walltime: 00:30:00
    jobname: CVmix_SCM_tests-cooling_only-BML
    experiment: CVmix_SCM_tests-cooling_only-BML
    laboratory: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab

    model: mom6
    exe: mom6-solo           # found on PATH once the module below is loaded

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

