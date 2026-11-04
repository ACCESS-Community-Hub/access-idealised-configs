# tides_025

!!! failure "Run status: :x: did not run"
    Tested on 2026-11-04 with `access-om3/2026.05.004`. Needs the OM4 1/4° grid files (`ocean_hgrid.nc`, `ocean_topog.nc`, `All_edits.nc`) in `INPUT/`, which the repository does not link (`set_grid_metrics_from_mosaic: Unable to open INPUT/ocean_hgrid.nc`).


!!! abstract "Description (as on the Overview)"
    - Set-up not recorded (this run failed)

    Read from this run's `MOM_parameter_doc.all`. Source: [upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/tides_025).

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

