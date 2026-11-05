# resting / z

!!! success "Run status: :white_check_mark: ran successfully"
    Tested on 2026-11-04 with `access-om3/2026.05.004` (`mom6-solo`): 2 cores, walltime used 00:00:14, 0.02 SU. Details further down this page.


!!! abstract "Description (as on the Overview)"
    - **Grid:** 20 x 2 points, 9 layers/levels (`GRID_CONFIG = cartesian`)
    - **Vertical coordinate:** `Z*`
    - **Topography:** `TOPO_CONFIG = flat`
    - **Surface forcing:** `WIND_CONFIG = zero`, `BUOY_CONFIG = NONE`
    - **Run length:** 5 days

    Read from this run's `MOM_parameter_doc.all`. Source: [upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z).

Configuration files: [`ocean_only/resting/z`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z) in NOAA-GFDL/MOM6-examples, at commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802): the version this run used. (The model itself is the `mom6-solo` listed under [Provenance](#provenance).)

!!! info "Workaround in the payu set-up (the MOM6-examples files are unchanged)"
    Nothing in the MOM6-examples files is changed: `MOM_input` and `MOM_override` are used as they are at the tested commit, so the model runs exactly as GFDL set it up. This example switches restart files off (`RESTART_CONTROL = -1`), and payu 1.3.6 cannot archive such a run: it deletes empty directories and then tries to move `work/<name>/RESTART`, which fails with `FileNotFoundError`. So the run script adds a payu `run` userscript to the `config.yaml` it writes (see `userscripts:` in the payu config.yaml under [Provenance](#provenance)). After the model finishes, the userscript creates `RESTART/` with a one-line `README`, and payu can then archive the run.

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed):

```bash
PROJECT=<your-project> bash resting-z.sh
```

where `resting-z.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "resting-z.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/resting-z.sh"
    ```

## What we got

Last lines of `ocean.stats`:

```text
   144,       2.000,     0, En 0.0000000000000000E+00, CFL  0.00000, SL  0.0000E+00, M 4.14000E+15, S 33.0000, T  0.0000, Me  0.00E+00, Se  8.21E-14, Te  0.00E+00
   216,       3.000,     0, En 0.0000000000000000E+00, CFL  0.00000, SL  0.0000E+00, M 4.14000E+15, S 33.0000, T  0.0000, Me  0.00E+00, Se  7.25E-14, Te  0.00E+00
   288,       4.000,     0, En 0.0000000000000000E+00, CFL  0.00000, SL  0.0000E+00, M 4.14000E+15, S 33.0000, T  0.0000, Me  0.00E+00, Se  6.76E-14, Te  0.00E+00
   360,       5.000,     0, En 0.0000000000000000E+00, CFL  0.00000, SL  0.0000E+00, M 4.14000E+15, S 33.0000, T  0.0000, Me  0.00E+00, Se  5.80E-14, Te  0.00E+00
```

## Domain, forcing and output

Made by running the notebook [`explore_run.ipynb`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/main/tested-configs/notebooks/explore_run.ipynb) on this run's output folder; it only plots files MOM6 wrote during the run. **[See the notebook with its code](../notebooks/resting-z.md)**.

### Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `20` |
| `NJGLOBAL` | `2` |
| `NK` | `9` |
| `GRID_CONFIG` | `cartesian` |
| `TOPO_CONFIG` | `flat` |
| `REENTRANT_X` | `False` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `Z*` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `LINEAR` |
| `THICKNESS_CONFIG` | `uniform` |
| `TS_CONFIG` | `linear` |
| `WIND_CONFIG` | `zero` |
| `BUOY_CONFIG` | `NONE` |
| `ICE_SHELF` | `False` |
| `DT` | `1200.0` |
| `DT_THERM` | `1200.0` |
| `DAYMAX` | `5.0` |


### Domain and bottom depth


Grid: 20 x 2 points (`GRID_CONFIG = cartesian`), x from 5 to 195 kilometers, y from 5 to 15 kilometers. Bottom depth `D` from 1000 to 1000 m (`TOPO_CONFIG = flat`).



    
![png](../../../assets/tested-configs/notebooks/resting-z/notebook_8_1.png)
    


### Initial state


`Salt` from `MOM_IC.nc`, which MOM6 writes with the initial state.



    
![png](../../../assets/tested-configs/notebooks/resting-z/notebook_10_1.png)
    


### Surface forcing


No surface forcing is saved in this run's diagnostics. The forcing is set by `WIND_CONFIG = zero` and `BUOY_CONFIG = NONE` (see the MOM6 documentation for these options).


### Energy and stability through the run


    
![png](../../../assets/tested-configs/notebooks/resting-z/notebook_14_0.png)
    



From `ocean.stats.nc`: 6 records; time axis in days.


### Final state


`salt` at the last record of `prog.nc` (snapshot).



    
![png](../../../assets/tested-configs/notebooks/resting-z/notebook_16_1.png)

## Parameters compared with the reference

<span class="chip a">A</span> GFDL's file in MOM6-examples (`c1730b8e`): [`MOM_parameter_doc.all`](https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all)  
<span class="chip b">B</span> this run: [`MOM_parameter_doc.all`](../parameters/resting-z.md) in the run's output, `/scratch/<your-project>/$USER/mom6-examples/archive/resting-z/output000/MOM_parameter_doc.all` when you run the script

**1** parameter values differ; **5** parameters exist only in this run's MOM6 version and **10** only in the reference (new, removed or renamed parameters). Values are compared ignoring quotes, case and number formatting. Parameter names link to a search of the MOM6 source; reference values link to their line on GitHub and this run's line numbers to its file.

<table class="diff" markdown="1"><thead><tr><th>Parameter</th><th>Units</th><th>A: reference</th><th>B: this run</th></tr></thead><tbody markdown="1"><tr class="mod"><td colspan="4">MOM_set_visc</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=SET_VISC_ANSWER_DATE" target="_blank" rel="noopener">SET_VISC_ANSWER_DATE</a></td><td class="units"></td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all#L854" target="_blank" rel="noopener">20260703</a></td><td class="val b" data-label="B: this run" markdown="span">99991231 [line 844](../parameters/resting-z.md#L844){.ln}</td></tr></tbody></table>

??? note "Parameters in only one of the two files (15)"
    <table class="diff" markdown="1"><thead><tr><th>Parameter</th><th>Units</th><th>A: reference</th><th>B: this run</th></tr></thead><tbody markdown="1"><tr class="mod"><td colspan="4">MOM</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=NONBLOCKING_P_SURF_BUG" target="_blank" rel="noopener">NONBLOCKING_P_SURF_BUG</a></td><td class="units">Boolean</td><td class="val a unset" data-label="A: reference">(not in this version)</td><td class="val b" data-label="B: this run" markdown="span">True [line 147](../parameters/resting-z.md#L147){.ln}</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=USE_UH_PARTICLES" target="_blank" rel="noopener">USE_UH_PARTICLES</a></td><td class="units">Boolean</td><td class="val a unset" data-label="A: reference">(not in this version)</td><td class="val b" data-label="B: this run" markdown="span">False [line 187](../parameters/resting-z.md#L187){.ln}</td></tr><tr class="mod"><td colspan="4">MOM_continuity_PPM</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=CONT_USE_H_MARG_MIN" target="_blank" rel="noopener">CONT_USE_H_MARG_MIN</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all#L1071" target="_blank" rel="noopener">False</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_coord_initialization</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=REGRID_USE_DEPTH_BASED_TIME_FILTER" target="_blank" rel="noopener">REGRID_USE_DEPTH_BASED_TIME_FILTER</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all#L594" target="_blank" rel="noopener">True</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=USE_ADJUST_INTERFACE_MOTION" target="_blank" rel="noopener">USE_ADJUST_INTERFACE_MOTION</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all#L532" target="_blank" rel="noopener">True</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_diag_mediator</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=NUM_DIAG_DOWNSAMP_LEV" target="_blank" rel="noopener">NUM_DIAG_DOWNSAMP_LEV</a></td><td class="units"></td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all#L738" target="_blank" rel="noopener">0</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=SYMMETRIC_DOWNSAMPLE_SUMS" target="_blank" rel="noopener">SYMMETRIC_DOWNSAMPLE_SUMS</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all#L727" target="_blank" rel="noopener">False</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_grid_init</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=READ_MEAN_SEA_LEVEL" target="_blank" rel="noopener">READ_MEAN_SEA_LEVEL</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all#L245" target="_blank" rel="noopener">False</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_PressureForce_FV</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=RHO_PGF_REF_BUG" target="_blank" rel="noopener">RHO_PGF_REF_BUG</a></td><td class="units">Boolean</td><td class="val a unset" data-label="A: reference">(not in this version)</td><td class="val b" data-label="B: this run" markdown="span">True [line 1099](../parameters/resting-z.md#L1099){.ln}</td></tr><tr class="mod"><td colspan="4">MOM_restart</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=ENSEMBLE_APPENDIX_PREFIX" target="_blank" rel="noopener">ENSEMBLE_APPENDIX_PREFIX</a></td><td class="units"></td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all#L405" target="_blank" rel="noopener">&quot;&quot;</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_set_visc</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=CDRAG_MAP" target="_blank" rel="noopener">CDRAG_MAP</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all#L888" target="_blank" rel="noopener">False</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_thickness_diffuse</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=USE_THICKNESS_DIFFUSE_ANN" target="_blank" rel="noopener">USE_THICKNESS_DIFFUSE_ANN</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all#L927" target="_blank" rel="noopener">False</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_tracer_flow_control</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=USE_FILE_DYES" target="_blank" rel="noopener">USE_FILE_DYES</a></td><td class="units">Boolean</td><td class="val a unset" data-label="A: reference">(not in this version)</td><td class="val b" data-label="B: this run" markdown="span">False [line 440](../parameters/resting-z.md#L440){.ln}</td></tr><tr class="mod"><td colspan="4">MOM_verticalGrid</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=ADVECTION_SCHEME_VARIANCE_UNDERFLOW" target="_blank" rel="noopener">ADVECTION_SCHEME_VARIANCE_UNDERFLOW</a></td><td class="units">Conc2 (tracer dependent)</td><td class="val a unset" data-label="A: reference">(not in this version)</td><td class="val b" data-label="B: this run" markdown="span">1.0E-23 [line 342](../parameters/resting-z.md#L342){.ln}</td></tr><tr class="mod"><td colspan="4">ocean_stochastics_init</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=STOCHASTICS_ANSWER_DATE" target="_blank" rel="noopener">STOCHASTICS_ANSWER_DATE</a></td><td class="units"></td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/resting/z/MOM_parameter_doc.all#L1812" target="_blank" rel="noopener">20250101</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr></tbody></table>

## Provenance

| What | Value |
|---|---|
| MOM6-examples | [`c1730b8efe16cf7f12fc8db588115cae50f3e802`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802) |
| ACCESS-OM3 module | `access-om3/2026.05.004` |
| MOM6 source code | `ACCESS-NRI/MOM6 2026.05.003 d11a149ccba676d524312328f7eb62560a156dc3` |
| Executable | `/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access-mom6-2026.05.003-ld7hklzo5ajizx5u4yl74i4ijberrpv6/bin/mom6-solo` |
| Executable md5 | `4785d157c76c30d8d01baf7d0f69d218` |
| payu | `1.3.6_1` (module `payu/1.3.6_1`) |
| Date tested | 2026-11-04 |
| PBS Job Id | `183115995.gadi-pbs` |
| PBS Exit Status | `0` |
| PBS Service Units | `0.02` |
| PBS NCPUs Requested | `2` |
| PBS Walltime Used | `00:00:14` |
| PBS Memory Used | `1.31GB` |

This example needs no input files: grid, bathymetry, initial state and forcing are all set analytically in `MOM_input`.

??? info "Run-time environment (selected variables from payu's `env.yaml`)"
    | Variable | Value |
    |---|---|
    | `LD_LIBRARY_PATH` | `/apps/openmpi/4.1.7/lib:/apps/openmpi/4.1.7/lib/profilers` |
    | `LOADEDMODULES` | `access3-share/2026.03.002-eale5gm:access-cice/CICE6.6.3-2-huasrvo:access-mocsy/2025.07.002-saj7rvh:access-generic-tracers/2026.09.000-e3zb3ez:access-mom6/2026.05.003-ld7hklz:access-ww3/2026.03.001-bjzidie:access3/2026.03.002-26wbxup:access-om3/2026.05.004:pbs:openmpi/4.1.7` |
    | `OMPI_MCA_orte_tmpdir_base` | `/jobfs/183115995.gadi-pbs` |
    | `PAYU_TELEMETRY_ENV_VERSION` | `1.3.6_1` |
    | `PBS_NCI_NCPUS_PER_NODE` | `104` |
    | `PBS_NCPUS` | `2` |
    | `PBS_QUEUE` | `normalsr-exec` |

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/resting/z (written by resting-z.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 2
    walltime: 00:30:00
    jobname: resting-z
    experiment: resting-z
    laboratory: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab

    model: mom6
    exe: mom6-solo           # found on PATH once the module below is loaded

    userscripts:             # this example writes no restart files
      run: mkdir -p /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab/work/resting-z/RESTART && echo 'no restart files (RESTART_CONTROL = -1)' > /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab/work/resting-z/RESTART/README
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

??? info "Output files"
    | File | Size | What it is |
    |---|---|---|
    | `MOM_IC.nc` | 0.06 MB | Initial state written by MOM6 at the start of the run |
    | `Vertical_coordinate.nc` | 0.00 MB | The vertical coordinate: target values of the layers or levels |
    | `ocean.stats.nc` | 0.01 MB | Domain totals at each energy-save time (energy, mass, heat, salt, maximum CFL); the netCDF form of `ocean.stats` |
    | `ocean_geometry.nc` | 0.03 MB | Static grid: coordinates, cell sizes and areas, bottom depth `D`, Coriolis parameter, land mask |
    | `prog.nc` | 0.16 MB | Diagnostics set in `diag_table`: snapshots of `u`, `v`, `h`, `e`, `temp`, `salt`, `ea`, `eb` and 1 more, every 12 hours |

