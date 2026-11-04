# ISOMIP / rho

!!! failure "Run status: :x: did not run"
    Tested on 2026-11-04 with `access-om3/2026.05.004`. Needs the ice-shelf file `INPUT/Ocean1_3D.nc`, which is not in the repository or in the GFDL input data (`initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc`).


!!! abstract "Description (as on the Overview)"
    - Set-up not recorded (this run failed)

    Read from this run's `MOM_parameter_doc.all`. Source: [upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/ISOMIP/rho).

Configuration files: [`ocean_only/ISOMIP/rho`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/ISOMIP/rho) in NOAA-GFDL/MOM6-examples, at commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802): the version this run used. (The model itself is the `mom6-solo` listed under [Provenance](#provenance).)

GFDL excludes this example from its own automated test suite (`EXCLUDE` in [`ocean_only/Makefile`](https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/Makefile)).

!!! failure "Known issue"
    Needs the ice-shelf file `INPUT/Ocean1_3D.nc`, which is not in the repository or in the GFDL input data (`initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc`). GFDL also excludes the ISOMIP examples from its own test suite. For a working ice-shelf cavity case see [ISOMIP+ Ocean0](../isomip-plus.md).

!!! info "Workaround in the payu set-up (the MOM6-examples files are unchanged)"
    Nothing in the MOM6-examples files is changed: `MOM_input` and `MOM_override` are used as they are at the tested commit, so the model runs exactly as GFDL set it up. This example switches restart files off (`RESTART_CONTROL = -1`), and payu 1.3.6 cannot archive such a run: it deletes empty directories and then tries to move `work/<name>/RESTART`, which fails with `FileNotFoundError`. So the run script adds a payu `run` userscript to the `config.yaml` it writes (see `userscripts:` in the payu config.yaml under [Provenance](#provenance)). After the model finishes, the userscript creates `RESTART/` with a one-line `README`, and payu can then archive the run.

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash ISOMIP-rho.sh
```

where `ISOMIP-rho.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "ISOMIP-rho.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/ISOMIP-rho.sh"
    ```

??? failure "End of the error log"
    ```text
    FATAL from PE    15:  initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc
    FATAL from PE    12:  initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc
    FATAL from PE    18:  initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc
    FATAL from PE    23:  initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc
    FATAL from PE    13:  initialize_topography_from_file: Unable to open INPUT/Ocean1_3D.nc
    ...
    libc-2.28.so       0000153FC301C865  __libc_start_main     Unknown  Unknown
    mom6-solo          0000000000412A4E  Unknown               Unknown  Unknown
    forrtl: error (78): process killed (SIGTERM)
    Image              PC                Routine            Line        Source             
    libpthread-2.28.s  00001490DBE09990  Unknown               Unknown  Unknown
    libpthread-2.28.s  00001490DBE0536F  pthread_cond_wait     Unknown  Unknown
    libopen-pal.so.40  00001490D72E353D  PMIx_Abort            Unknown  Unknown
    libopen-pal.so.40  00001490D7350780  pmix3x_abort          Unknown  Unknown
    libopen-rte.so.40  00001490D7A78ED7  Unknown               Unknown  Unknown
    libopen-rte.so.40  00001490D7A90C66  orte_errmgr_base_     Unknown  Unknown
    libopen-rte.so.40  00001490D7A80A1B  Unknown               Unknown  Unknown
    libmpi.so.40.30.7  00001490DC26419A  ompi_mpi_abort        Unknown  Unknown
    libmpi_mpifh.so    00001490DC5972AE  Unknown               Unknown  Unknown
    mom6-solo          000000000183E5D1  mpp_error_basic            84  mpp_util_mpi.inc
    mom6-solo          00000000006C2AE6  mom_error                 180  MOM_error_handler.F90
    mom6-solo          000000000074BEE8  initialize_ice_th         132  MOM_ice_shelf_initialize.F90
    mom6-solo          000000000074B651  initialize_ice_th          82  MOM_ice_shelf_initialize.F90
    mom6-solo          000000000073C7E1  initialize_ice_sh        1891  MOM_ice_shelf.F90
    mom6-solo          000000000046E7DE  initialize_mom           3283  MOM.F90
    mom6-solo          00000000004387C5  mom6                      284  MOM_driver.F90
    mom6-solo          0000000000412B2D  Unknown               Unknown  Unknown
    libc-2.28.so       00001490DB857865  __libc_start_main     Unknown  Unknown
    mom6-solo          0000000000412A4E  Unknown               Unknown  Unknown
    [gadi-cpu-spr-0140.gadi.nci.org.au:3349469] 23 more processes have sent help message help-mpi-api.txt / mpi-abort
    [gadi-cpu-spr-0140.gadi.nci.org.au:3349469] Set MCA parameter "orte_base_help_aggregate" to 0 to see all help / error messages
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
| PBS Job Id | `183115599.gadi-pbs` |
| PBS Exit Status | `1` |
| PBS Service Units | `0.16` |
| PBS NCPUs Requested | `24` |
| PBS Walltime Used | `00:00:12` |
| PBS Memory Used | `4.88GB` |

This example needs no input files: grid, bathymetry, initial state and forcing are all set analytically in `MOM_input`.

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/ISOMIP/rho (written by ISOMIP-rho.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 24
    walltime: 00:30:00
    jobname: ISOMIP-rho
    experiment: ISOMIP-rho
    laboratory: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab

    model: mom6
    exe: mom6-solo           # found on PATH once the module below is loaded

    userscripts:             # this example writes no restart files
      run: mkdir -p /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab/work/ISOMIP-rho/RESTART
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

