# ISOMIP / layer

!!! failure "Run status: :x: did not run"
    Tested on 2026-11-04 with `access-om3/2026.05.004`. Needs the ice-shelf file `INPUT/Ocean1_3D.nc`, which is not in the repository or in the GFDL input data (`initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc`).


!!! abstract "Description (as on the Overview)"
    - Set-up not recorded (this run failed)

    Read from this run's `MOM_parameter_doc.all`. Source: [upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/ISOMIP/layer).

Configuration files: [`ocean_only/ISOMIP/layer`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/ISOMIP/layer) in NOAA-GFDL/MOM6-examples, at commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802): the version this run used. (The model itself is the `mom6-solo` listed under [Provenance](#provenance).)

GFDL excludes this example from its own automated test suite (`EXCLUDE` in [`ocean_only/Makefile`](https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/Makefile)).

!!! failure "Known issue"
    Needs the ice-shelf file `INPUT/Ocean1_3D.nc`, which is not in the repository or in the GFDL input data (`initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc`). GFDL also excludes the ISOMIP examples from its own test suite. For a working ice-shelf cavity case see [ISOMIP+ Ocean0](../isomip-plus.md).

!!! info "Workaround in the payu set-up (the MOM6-examples files are unchanged)"
    Nothing in the MOM6-examples files is changed: `MOM_input` and `MOM_override` are used as they are at the tested commit, so the model runs exactly as GFDL set it up. This example switches restart files off (`RESTART_CONTROL = -1`), and payu 1.3.6 cannot archive such a run: it deletes empty directories and then tries to move `work/<name>/RESTART`, which fails with `FileNotFoundError`. So the run script adds a payu `run` userscript to the `config.yaml` it writes (see `userscripts:` in the payu config.yaml under [Provenance](#provenance)). After the model finishes, the userscript creates `RESTART/` with a one-line `README`, and payu can then archive the run.

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash ISOMIP-layer.sh
```

where `ISOMIP-layer.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "ISOMIP-layer.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/ISOMIP-layer.sh"
    ```

??? failure "End of the error log"
    ```text
    FATAL from PE     7:  initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc
    FATAL from PE     8:  initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc
    FATAL from PE    11:  initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc
    FATAL from PE    17:  initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc
    FATAL from PE    21:  initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc
    ...
    mom6-solo          00000000004387C5  mom6                      284  MOM_driver.F90
    mom6-solo          0000000000412B2D  Unknown               Unknown  Unknown
    libc-2.28.so       000014B8DF44F865  __libc_start_main     Unknown  Unknown
    mom6-solo          0000000000412A4E  Unknown               Unknown  Unknown
    Image              PC                Routine            Line        Source             
    mom6-solo          000000000183E5BB  mpp_error_basic            80  mpp_util_mpi.inc
    mom6-solo          00000000006C2AE6  mom_error                 180  MOM_error_handler.F90
    mom6-solo          000000000074BEE8  initialize_ice_th         132  MOM_ice_shelf_initialize.F90
    mom6-solo          000000000074B651  initialize_ice_th          82  MOM_ice_shelf_initialize.F90
    mom6-solo          000000000073C7E1  initialize_ice_sh        1891  MOM_ice_shelf.F90
    mom6-solo          000000000046E7DE  initialize_mom           3283  MOM.F90
    mom6-solo          00000000004387C5  mom6                      284  MOM_driver.F90
    mom6-solo          0000000000412B2D  Unknown               Unknown  Unknown
    libc-2.28.so       00001533B8965865  __libc_start_main     Unknown  Unknown
    mom6-solo          0000000000412A4E  Unknown               Unknown  Unknown
    --------------------------------------------------------------------------
    MPI_ABORT was invoked on rank 0 in communicator MPI_COMM_WORLD
    with errorcode 1.

    NOTE: invoking MPI_ABORT causes Open MPI to kill all MPI processes.
    You may or may not see output from other processes, depending on
    exactly when Open MPI kills them.
    --------------------------------------------------------------------------
    [gadi-cpu-spr-0121.gadi.nci.org.au:2108194] 23 more processes have sent help message help-mpi-api.txt / mpi-abort
    [gadi-cpu-spr-0121.gadi.nci.org.au:2108194] Set MCA parameter "orte_base_help_aggregate" to 0 to see all help / error messages
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
| PBS Job Id | `183115590.gadi-pbs` |
| PBS Exit Status | `1` |
| PBS Service Units | `0.20` |
| PBS NCPUs Requested | `24` |
| PBS Walltime Used | `00:00:15` |
| PBS Memory Used | `4.78GB` |

This example needs no input files: grid, bathymetry, initial state and forcing are all set analytically in `MOM_input`.

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/ISOMIP/layer (written by ISOMIP-layer.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 24
    walltime: 00:30:00
    jobname: ISOMIP-layer
    experiment: ISOMIP-layer
    laboratory: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab

    model: mom6
    exe: mom6-solo           # found on PATH once the module below is loaded

    userscripts:             # this example writes no restart files
      run: mkdir -p /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab/work/ISOMIP-layer/RESTART
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

