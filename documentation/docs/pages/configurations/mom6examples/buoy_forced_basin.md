# buoy_forced_basin

!!! failure "Run status: :x: did not run"
    Tested on 2026-11-04 with `access-om3/2026.05.004`. The model goes numerically unstable: after about 105 model days (of the 100 years set by `DAYMAX = 36500`) it stops with `write_energy : Ocean velocity has been truncated too many times`.


!!! abstract "Description (as on the Overview)"
    - Set-up not recorded (this run failed)

    Read from this run's `MOM_parameter_doc.all`. Source: [upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/buoy_forced_basin).

Configuration files: [`ocean_only/buoy_forced_basin`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/buoy_forced_basin) in NOAA-GFDL/MOM6-examples, at commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802): the version this run used. (The model itself is the `mom6-solo` listed under [Provenance](#provenance).)

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

