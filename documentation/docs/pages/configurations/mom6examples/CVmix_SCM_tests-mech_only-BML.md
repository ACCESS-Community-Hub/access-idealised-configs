# CVmix_SCM_tests / mech_only / BML

!!! failure "Run status: :x: did not run"
    Tested on 2026-11-04 with `access-om3/2026.05.004`. The bulk-mixed-layer (BML) cases read `isopyc_coords.nc` from the run directory (`COORD_FILE = "isopyc_coords.nc"`, `INPUTDIR = "."`), but upstream only links that file in `common_BML/`, not in the `*/BML` directories, so MOM6 stops with `set_coord_from_file: Unable to open ./isopyc_coords.nc`.


!!! abstract "Description (as on the Overview)"
    - Set-up not recorded (this run failed)

    Read from this run's `MOM_parameter_doc.all`. Source: [upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/CVmix_SCM_tests/mech_only/BML), [README](https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/CVmix_SCM_tests/README.md).

Configuration files: [`ocean_only/CVmix_SCM_tests/mech_only/BML`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/CVmix_SCM_tests/mech_only/BML) in NOAA-GFDL/MOM6-examples, at commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802): the version this run used. (The model itself is the `mom6-solo` listed under Provenance.)

!!! failure "Known issue"
    The bulk-mixed-layer (BML) cases read `isopyc_coords.nc` from the run directory (`COORD_FILE = "isopyc_coords.nc"`, `INPUTDIR = "."`), but upstream only links that file in `common_BML/`, not in the `*/BML` directories, so MOM6 stops with `set_coord_from_file: Unable to open ./isopyc_coords.nc`. GFDL's restart-test script (`tools/MRS/setup_restart_test.sh`) copies the file in by hand. The ePBL and KPP versions of the same tests run.

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash CVmix_SCM_tests-mech_only-BML.sh
```

where `CVmix_SCM_tests-mech_only-BML.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "CVmix_SCM_tests-mech_only-BML.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/CVmix_SCM_tests-mech_only-BML.sh"
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
    libc-2.28.so       000014C740E1E865  __libc_start_main     Unknown  Unknown
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
| PBS Job Id | `183115184.gadi-pbs` |
| PBS Exit Status | `1` |
| PBS Service Units | `0.01` |
| PBS NCPUs Requested | `1` |
| PBS Walltime Used | `00:00:19` |
| PBS Memory Used | `1.15GB` |

This example needs no input files: grid, bathymetry, initial state and forcing are all set analytically in `MOM_input`.

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/CVmix_SCM_tests/mech_only/BML (written by CVmix_SCM_tests-mech_only-BML.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 1
    walltime: 00:30:00
    jobname: CVmix_SCM_tests-mech_only-BML
    experiment: CVmix_SCM_tests-mech_only-BML
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

