# buoy_forced_basin

!!! failure ":x: This configuration did not run"
    Tested on 2026-11-04 with `access-om3/2026.05.004`. The model goes numerically unstable: after about 105 model days (of the 100 years set by `DAYMAX = 36500`) it stops with `write_energy : Ocean velocity has been truncated too many times`.


!!! abstract "Description (as on the Overview)"
    - Set-up not recorded (this run failed)

    Read from this run's `MOM_parameter_doc.all`. Source: [upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/buoy_forced_basin).

Configuration files: [`ocean_only/buoy_forced_basin`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/buoy_forced_basin) in NOAA-GFDL/MOM6-examples, at commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802): the version this run used. (The model itself is the `mom6-solo` listed under Provenance.)

GFDL excludes this example from its own automated test suite (`EXCLUDE` in [`ocean_only/Makefile`](https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/Makefile)).

!!! failure "Known issue"
    The model goes numerically unstable: after about 105 model days (of the 100 years set by `DAYMAX = 36500`) it stops with `write_energy : Ocean velocity has been truncated too many times`. GFDL also excludes this example from its own test suite.

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash buoy_forced_basin.sh
```

where `buoy_forced_basin.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "buoy_forced_basin.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/buoy_forced_basin.sh"
    ```

??? failure "End of the error log"
    ```text
    FATAL from PE     3: write_energy : Ocean velocity has been truncated too many times.
    FATAL from PE     4: write_energy : Ocean velocity has been truncated too many times.
    FATAL from PE     5: write_energy : Ocean velocity has been truncated too many times.
    FATAL from PE     2: write_energy : Ocean velocity has been truncated too many times.
    FATAL from PE     1: write_energy : Ocean velocity has been truncated too many times.
    ...
    mom6-solo          000000000043A166  mom6                      490  MOM_driver.F90
    mom6-solo          0000000000412B2D  Unknown               Unknown  Unknown
    libc-2.28.so       00001512A6D79865  __libc_start_main     Unknown  Unknown
    mom6-solo          0000000000412A4E  Unknown               Unknown  Unknown
    forrtl: error (78): process killed (SIGTERM)
    Image              PC                Routine            Line        Source             
    libpthread-2.28.s  0000154812961990  Unknown               Unknown  Unknown
    libpthread-2.28.s  000015481295D36F  pthread_cond_wait     Unknown  Unknown
    libopen-pal.so.40  000015480DE3B53D  PMIx_Abort            Unknown  Unknown
    libopen-pal.so.40  000015480DEA8780  pmix3x_abort          Unknown  Unknown
    libopen-rte.so.40  000015480E5D0ED7  Unknown               Unknown  Unknown
    libopen-rte.so.40  000015480E5E8C66  orte_errmgr_base_     Unknown  Unknown
    libopen-rte.so.40  000015480E5D8A1B  Unknown               Unknown  Unknown
    libmpi.so.40.30.7  0000154812DBC19A  ompi_mpi_abort        Unknown  Unknown
    libmpi_mpifh.so    00001548130EF2AE  Unknown               Unknown  Unknown
    mom6-solo          000000000183E5D1  mpp_error_basic            84  mpp_util_mpi.inc
    mom6-solo          00000000006C2AE6  mom_error                 180  MOM_error_handler.F90
    mom6-solo          00000000005F48B6  write_energy             1009  MOM_sum_output.F90
    mom6-solo          000000000044D833  step_mom                 1147  MOM.F90
    mom6-solo          000000000043A166  mom6                      490  MOM_driver.F90
    mom6-solo          0000000000412B2D  Unknown               Unknown  Unknown
    libc-2.28.so       00001548123AF865  __libc_start_main     Unknown  Unknown
    mom6-solo          0000000000412A4E  Unknown               Unknown  Unknown
    [gadi-cpu-spr-0717.gadi.nci.org.au:2186622] 5 more processes have sent help message help-mpi-api.txt / mpi-abort
    [gadi-cpu-spr-0717.gadi.nci.org.au:2186622] Set MCA parameter "orte_base_help_aggregate" to 0 to see all help / error messages
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
| PBS Job Id | `183114903.gadi-pbs` |
| PBS Exit Status | `1` |
| PBS Service Units | `0.21` |
| PBS NCPUs Requested | `6` |
| PBS Walltime Used | `00:01:02` |
| PBS Memory Used | `1.4GB` |

This example needs no input files: grid, bathymetry, initial state and forcing are all set analytically in `MOM_input`.

??? info "Parameters differing from the upstream MOM_parameter_doc.all (373)"
    Comparison of this run's `MOM_parameter_doc.all` with the upstream MOM_parameter_doc.all.
    Differences show where the ACCESS-OM3 MOM6 version adds, drops or changes default parameters.

    Only upstream: `ADD_LES_VISCOSITY`, `ADIABATIC`, `ADJUST_BT_CONT`, `AGGREGATE_FW_FORCING`, `AH`, `AH_TIME_SCALE`, `AH_VEL_SCALE`, `ALTERNATE_FIRST_DIRECTION`, `ANALYTIC_FV_PGF`, `ANGSTROM`, `ANISOTROPIC_VISCOSITY`, `APPLY_INTERFACE_FILTER`, `AVAILABLE_DIAGS_FILE`, `BAROTROPIC_2018_ANSWERS`, `BAROTROPIC_ANSWER_DATE`, `BATHYMETRY_AT_VEL`, `BBL_THICK_MIN`, `BE`, `BEBT`, `BEGW`, `BETTER_BOUND_AH`, `BETTER_BOUND_KH`, `BIHARMONIC`, `BOTTOMDRAGLAW`, `BOUNDARY_EXTRAPOLATION_PRESSURE`, `BOUND_AH`, `BOUND_BT_CORRECTION`, `BOUND_CORIOLIS`, `BOUND_CORIOLIS_BIHARM`, `BOUND_KH`, `BOUSSINESQ`, `BRYAN_LEWIS_DIFFUSIVITY`, `BT_CORIOLIS_SCALE`, `BT_LINEAR_WAVE_DRAG`, `BT_NONLIN_STRESS`, `BT_PROJECT_VELOCITY`, `BT_STRONG_DRAG`, `BT_THICK_SCHEME`, `BT_USE_LAYER_FLUXES`, `BT_USE_OLD_CORIOLIS_BRACKET_BUG`, `BT_USE_VISC_REM_U_UH0`, `BULKMIXEDLAYER`, `BUOY_CONFIG`, `CALCULATE_APE`, `CALC_RHO_FOR_SEA_LEVEL`, `CFL_BASED_TRUNCATIONS`, `CFL_REPORT`, `CFL_TRUNCATE`, `CFL_TRUNCATE_RAMP_TIME`, `CFL_TRUNCATE_START`, `CHANNEL_CONFIG`, `CHANNEL_DRAG`, `CHECK_BAD_SURFACE_VALS`, `CHECK_DIFFUSIVE_CFL`, `CLIP_BT_VELOCITY`, `COMPLETE_DOCUMENTATION`, `CONTINUITY_CFL_LIMIT`, `CONTINUITY_SCHEME`, `CONT_PPM_AGGRESS_ADJUST`, `CONT_PPM_BETTER_ITER`, `CONT_PPM_MARGINAL_FACE_AREAS`, `CONT_PPM_USE_VISC_REM_MAX`, `CONT_PPM_VOLUME_BASED_CFL`, `CONVERT_THICKNESS_UNITS`, `COORD_CONFIG`, `CORIOLIS_EN_DIS`, `CORIOLIS_SCHEME`, `CORRECT_BBL_BOUNDS`, `CPU_TIME_FILE`, `DATE_STAMPED_STDOUT`, `DAYMAX`, `DEFAULT_2018_ANSWERS`, `DEFAULT_ANSWER_DATE`, `DEPRESS_INITIAL_SURFACE`, `DEPTH_LIST_MIN_INC`, `DEPTH_SCALED_KHTH`, `DETANGLE_INTERFACES`, `DIABATIC_FIRST`, `DIAG_AS_CHKSUM`, `DIAG_COORDS`, `DIAG_COORD_DEF_Z`, `DIAG_DEPTH_SUBML_N2`, `DIAG_EBT_MONO_N2_COLUMN_FRACTION`, `DIAG_EBT_MONO_N2_DEPTH`, `DIAG_MISVAL`, `DIAG_MLD_DENSITY_DIFF`, `DIFFUSE_ML_TO_INTERIOR`, `DIRECT_STRESS`, `DISSIPATION_KD_MIN`, `DISSIPATION_MIN`, `DISSIPATION_N0`, `DISSIPATION_N1`, `DOCUMENT_FILE`, `DOUBLE_DIFFUSION`, `DO_DYNAMICS`, `DO_SPPT`, `DRHO_DT`, `DT`, `DTBT`, `DTBT_RESET_PERIOD`, `DT_BT_FILTER`, `DT_FORCING`, `DT_THERM`, `DYNAMIC_SURFACE_PRESSURE`, `DYNAMIC_VISCOUS_ML`, `ENABLE_THERMODYNAMICS`, `ENERGETICS_SFC_PBL`, `ENERGYFILE`, `ENERGYSAVEDAYS`, `ENERGYSAVEDAYS_GEOMETRIC`, `ENSEMBLE_OCEAN`, `EPBL_IS_ADDITIVE`, `EQUATOR_REFERENCE`, `ETA_TOLERANCE`, `EVAP_CFL_LIMIT`, `FATAL_INCONSISTENT_RESTART_TIME`, `FIRST_DIRECTION`, `FIXED_DEPTH_LOTW_ML`, `FIX_USTAR_GUSTLESS_BUG`, `FLUXCONST`, `FLUX_RI_MAX`, `GRADUAL_BT_ICS`, `GRID_CONFIG`, `GRID_ROTATION_ANGLE_BUGS`, `GUST_CONST`, `G_BT_EXTRA`, `G_EARTH`, `HARMONIC_BL_SCALE`, `HARMONIC_VISC`, `HBBL`, `HENYEY_IGW_BACKGROUND`, `HFREEZE`, `HMIX_FIXED`, `HMIX_SFC_PROP`, `HMIX_UV_SFC_PROP`, `HOMOGENIZE_FORCINGS`, `HORIZ_VARYING_BACKGROUND`, `HORVISC_BOUND_COEF`, `HOR_VISC_2018_ANSWERS`, `HOR_VISC_ANSWER_DATE`, `HTBL_SHELF`, `HTBL_SHELF_MIN`, `H_TO_M`, `ICE_SHELF`, `IC_OUTPUT_FILE`, `INIT_LAYERS_FROM_Z_FILE`, `INPUTDIR`, `INTEGRAL_BT_CONTINUITY`, `INTERNAL_TIDES`, `INTERNAL_WAVE_SPEED_BETTER_EST`, `INTERNAL_WAVE_SPEED_MIN`, `INTERNAL_WAVE_SPEED_TOL`, `INTERPOLATE_P_SURF`, `INT_TIDE_DISSIPATION`, `ISOTROPIC`, `KD`, `KD_ADD`, `KD_BBL_TR`, `KD_GL90_USE_EBT_STRUCT`, `KD_MAX`, `KD_MIN`, `KD_MIN_TR`, `KD_ML_TOT`, `KD_SEED_KAPPA_SHEAR`, `KD_SMOOTH`, `KD_TANH_LAT_FN`, `KE_SCHEME`, `KH`, `KHTH`, `KHTH_MAX`, `KHTH_MAX_CFL`, `KHTH_MIN`, `KHTH_SLOPE_CFF`, `KHTH_SLOPE_MAX`, `KHTH_USE_EBT_STRUCT`, `KHTH_USE_FGNV_STREAMFUNCTION`, `KHTR`, `KHTR_MAX`, `KHTR_MIN`, `KHTR_PASSIVITY_COEFF`, `KHTR_PASSIVITY_MIN`, `KHTR_SLOPE_CFF`, `KH_BG_MIN`, `KH_ETA_CONST`, `KH_ETA_VEL_SCALE`, `KH_SIN_LAT`, `KH_VEL_SCALE`, `KV`, `KV_BBL_MIN`, `KV_EXTRA_BBL`, `KV_ML_INVZ2`, `KV_TBL_MIN`, `LAPLACIAN`, `LATENT_HEAT_FUSION`, `LATENT_HEAT_VAPORIZATION`, `LAT_ENHANCE_FACTOR`, `LAT_EQ_ENHANCE`, `LEITH_AH`, `LEITH_KH`, `LENLAT`, `LENLON`, `LFR_NLAT`, `LFR_SLAT`, `LINEARIZED_BT_CORIOLIS`, `LINEAR_DRAG`, `LOTW_VISCOUS_ML_FLOOR`, `MASKING_DEPTH`, `MASSLESS_MATCH_TARGETS`, `MASS_WEIGHT_IN_PRESSURE_GRADIENT`, `MAXCFL_BT_CONT`, `MAXCPU`, `MAXIMUM_DEPTH`, `MAXTRUNC`, `MAXVEL`, `MAX_ENERGY`, `MAX_ENT_IT`, `MAX_FIELDS`, `MAX_TR_DIFFUSION_CFL`, `MEKE_GEOMETRIC`, `MEKE_GM_SRC_ALT`, `MINIMAL_DOCUMENTATION`, `MINIMUM_DEPTH`, `MINIMUM_FORCING_DEPTH`, `MIXEDLAYER_RESTRAT`, `MIX_BOUNDARY_TRACERS`, `ML_RADIATION`, `MONOTONIC_CONTINUITY`, `NIGLOBAL`, `NIHALO`, `NJGLOBAL`, `NJHALO`, `NK`, `NOSLIP`, `NUM_DIAG_COORDS`, `OBC_NUMBER_OF_SEGMENTS`, `OBSOLETE_DIAGNOSTIC_IS_FATAL`, `ODA_INCUPD`, `OFFLINE_TRACER_MODE`, `OMEGA`, `PARALLEL_RESTARTFILES`, `PERT_EPBL`, `PORBAR_ANSWER_DATE`, `PORBAR_ETA_INTERP`, `PORBAR_MASKING_DEPTH`, `PRANDTL_BKGND`, `PRANDTL_TURB`, `PRESSURE_RECONSTRUCTION_SCHEME`, `PV_ADV_SCHEME`, `RAD_EARTH`, `READ_DEPTH_LIST`, `READ_GUST_2D`, `READ_KHTH`, `RECALC_NEUTRAL_SURF`, `RECONSTRUCT_FOR_PRESSURE`, `REENTRANT_X`, `REENTRANT_Y`, `REFERENCE_HEIGHT`, `REGULARIZE_SURFACE_LAYERS`, `REMAPPING_2018_ANSWERS`, `REMAPPING_ANSWER_DATE`, `RESOLN_SCALED_KH`, `RESOLN_SCALED_KHTH`, `RESOLN_SCALED_KHTR`, `RESOLN_USE_EBT`, `RESTARTFILE`, `RESTART_CHECKSUMS_REQUIRED`, `RESTART_CONTROL`, `RESTINT`, `RESTOREBUOY`, `RE_AH`, `RHO_0`, `ROTATION`, `SADOURNY`, `SAVE_INITIAL_CONDS`, `SEND_LOG_TO_STDOUT`, `SET_DIFF_2018_ANSWERS`, `SET_DIFF_ANSWER_DATE`, `SET_VISC_2018_ANSWERS`, `SET_VISC_ANSWER_DATE`, `SIMPLE_2ND_PPM_CONTINUITY`, `SINGLE_STEPPING_CALL`, `SMAGORINSKY_AH`, `SMAGORINSKY_KH`, `SMAG_BI_CONST`, `SOUTHLAT`, `SPLIT`, `SPLIT_BOTTOM_STRESS`, `SPONGE`, `SPONGE_CONFIG`, `SSH_EXTRA`, `SST_N`, `SST_S`, `STOKES_MIXING_COMBINED`, `STORE_CORIOLIS_ACCEL`, `SUBGRID_TOPO_AT_VEL`, `SURFACE_2018_ANSWERS`, `SURFACE_ANSWER_DATE`, `THERMO_SPANS_COUPLING`, `THICKNESSDIFFUSE`, `THICKNESS_CONFIG`, `TIDES`, `TIMEUNIT`, `TKE_BACKGROUND`, `TOLERANCE_ENT`, `TOPO_CONFIG`, `TRACER_ADVECTION_SCHEME`, `TRACER_TRIDIAG`, `TRIM_IC_FOR_P_SURF`, `TRIPOLAR_N`, `T_BOT`, `UPWIND_1ST_CONTINUITY`, `USER_CHANGE_DIFFUSIVITY`, `USE_ADVECTION_TEST_TRACER`, `USE_BOUNDARY_IMPULSE_TRACER`, `USE_BT_CONT_TYPE`, `USE_CFC_CAP`, `USE_CONTEMP_ABSSAL`, `USE_CVMIX_DDIFF`, `USE_DBCLIENT`, `USE_DIABATIC_TIME_BUG`, `USE_DOME_TRACER`, `USE_DYED_OBC_TRACER`, `USE_EOS`, `USE_GL90_IN_SSW`, `USE_GME`, `USE_GM_WORK_BUG`, `USE_GRID_SPACE_DIAGNOSTIC_AXES`, `USE_IDEAL_AGE_TRACER`, `USE_INACCURATE_PGF_RHO_ANOM`, `USE_ISOMIP_TRACER`, `USE_JACKSON_PARAM`, `USE_KH_BG_2D`, `USE_KH_IN_MEKE`, `USE_KPP`, `USE_LAND_MASK_FOR_HVISC`, `USE_LATERAL_BOUNDARY_DIFFUSION`, `USE_LEGACY_DIABATIC_DRIVER`, `USE_LMD94`, `USE_MEKE`, `USE_NEUTRAL_DIFFUSION`, `USE_NW2_TRACERS`, `USE_OCMIP2_CFC`, `USE_OIL_TRACER`, `USE_PARTICLES`, `USE_POROUS_BARRIER`, `USE_PP81`, `USE_PSEUDO_SALT_TRACER`, `USE_QG_LEITH_GM`, `USE_REGIONAL_DYES`, `USE_REGRIDDING`, `USE_RGC_TRACER`, `USE_STANLEY_GM`, `USE_STANLEY_ISO`, `USE_STANLEY_PGF`, `USE_STORED_SLOPES`, `USE_USER_TRACER_EXAMPLE`, `USE_VARIABLE_MIXING`, `USE_VISBECK`, `USE_WAVES`, `VARIABLE_BUOYFORCE`, `VARIABLE_WINDS`, `VELOCITY_CONFIG`, `VELOCITY_TOLERANCE`, `VEL_UNDERFLOW`, `VERT_FRICTION_2018_ANSWERS`, `VERT_FRICTION_ANSWER_DATE`, `VERY_SMALL_FREQUENCY`, `VON_KARMAN_CONST`, `WESTLON`, `WIND_CONFIG`, `WRITE_CPU_STEPS`, `WRITE_GEOM`, `WRITE_STOCKS`

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/buoy_forced_basin (written by buoy_forced_basin.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 6
    walltime: 00:30:00
    jobname: buoy_forced_basin
    experiment: buoy_forced_basin
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

