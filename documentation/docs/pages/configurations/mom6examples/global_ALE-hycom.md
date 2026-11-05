# global_ALE / hycom

!!! success "Run status: :white_check_mark: ran successfully"
    Tested on 2026-11-04 with `access-om3/2026.05.004` (`mom6-solo`): 64 cores, walltime used 00:00:47, 1.67 SU. Details further down this page.


!!! abstract "Description (as on the Overview)"
    - **Grid:** 360 x 210 points, 50 layers/levels (`GRID_CONFIG = mosaic`)
    - **Vertical coordinate:** `HYCOM1`
    - **Topography:** `TOPO_CONFIG = file`
    - **Surface forcing:** `WIND_CONFIG = file`, `BUOY_CONFIG = file`
    - **Run length:** 1 days

    Read from this run's `MOM_parameter_doc.all`. Source: [upstream](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom).

Configuration files: [`ocean_only/global_ALE/hycom`](https://github.com/NOAA-GFDL/MOM6-examples/tree/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom) in NOAA-GFDL/MOM6-examples, at commit [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802): the version this run used. (The model itself is the `mom6-solo` listed under [Provenance](#provenance).)

## Run it yourself

From a Gadi **login node** (membership of NCI project `vk83` needed, and `ol01` for the input data):

```bash
PROJECT=<your-project> bash global_ALE-hycom.sh
```

where `global_ALE-hycom.sh` is the script below (click to expand; copy button top-right). It is exactly the script that produced the results on this page.

??? example "global_ALE-hycom.sh"
    ```bash
    --8<-- "tested-configs/run_scripts/global_ALE-hycom.sh"
    ```

## What we got

Last lines of `ocean.stats`:

```text
            [days]                 [m2 s-2]           [Nondim]       [m]             [kg]         [PSU]      [degC]       [Nondim]        [PSU]        [degC]
     0,       0.000,     0, En 6.7020727204868003E-01, CFL  0.00000, SL  6.2440E-11, M 1.37953E+21, S 34.7202, T  3.6184, Me  0.00E+00, Se  0.00E+00, Te  0.00E+00
    12,       0.500,     0, En 6.7029838990407165E-01, CFL  0.08340, SL  6.1895E-04, M 1.37953E+21, S 34.7202, T  3.6185, Me -2.82E-19, Se -2.97E-17, Te  7.99E-18
    24,       1.000,     0, En 6.7015429163718077E-01, CFL  0.10192, SL  1.2865E-03, M 1.37953E+21, S 34.7202, T  3.6185, Me  4.89E-19, Se  9.62E-18, Te  8.54E-18
```

## Domain, forcing and output

Made by running the notebook [`explore_run.ipynb`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/main/tested-configs/notebooks/explore_run.ipynb) on this run's output folder; it only plots files MOM6 wrote during the run. **[See the notebook with its code](../notebooks/global_ALE-hycom.md)**.

### Set-up


Values from this run's `MOM_parameter_doc.all`:

| Parameter | Value |
|---|---|
| `NIGLOBAL` | `360` |
| `NJGLOBAL` | `210` |
| `NK` | `50` |
| `GRID_CONFIG` | `mosaic` |
| `TOPO_CONFIG` | `file` |
| `REENTRANT_X` | `True` |
| `REENTRANT_Y` | `False` |
| `USE_REGRIDDING` | `True` |
| `REGRIDDING_COORDINATE_MODE` | `HYCOM1` |
| `ENABLE_THERMODYNAMICS` | `True` |
| `EQN_OF_STATE` | `WRIGHT` |
| `WIND_CONFIG` | `file` |
| `BUOY_CONFIG` | `file` |
| `ICE_SHELF` | `False` |
| `DT` | `3600.0` |
| `DT_THERM` | `7200.0` |
| `DAYMAX` | `1.0` |


### Domain and bottom depth


Grid: 360 x 210 points (`GRID_CONFIG = mosaic`), x from -279.5 to 79.5 degrees_east, y from -76.75 to 89.75 degrees_north. Bottom depth `D` from 0.25 to 6000 m (`TOPO_CONFIG = file`).



    
![png](../../../assets/tested-configs/notebooks/global_ALE-hycom/notebook_8_1.png)
    


### Initial state


`Temp` from `MOM_IC.nc`, which MOM6 writes with the initial state.



    
![png](../../../assets/tested-configs/notebooks/global_ALE-hycom/notebook_10_1.png)
    


### Surface forcing


Time-mean of the surface forcing saved in the diagnostics: `taux` (Zonal surface stress from ocean interactions with atmos and ice, from `forcing.nc`), `tauuo` (Surface Downward X Stress, from `cmor.nc`).



    
![png](../../../assets/tested-configs/notebooks/global_ALE-hycom/notebook_12_1.png)
    



    
![png](../../../assets/tested-configs/notebooks/global_ALE-hycom/notebook_12_2.png)
    


### Energy and stability through the run


    
![png](../../../assets/tested-configs/notebooks/global_ALE-hycom/notebook_14_0.png)
    



From `ocean.stats.nc`: 3 records; time axis in days.


### Final state


`SSH` at the last record of `surface.nc` (snapshot).



    
![png](../../../assets/tested-configs/notebooks/global_ALE-hycom/notebook_16_1.png)

## Parameters compared with the reference

<span class="chip a">A</span> GFDL's file in MOM6-examples (`c1730b8e`): [`MOM_parameter_doc.all`](https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all)  
<span class="chip b">B</span> this run: [`MOM_parameter_doc.all`](../parameters/global_ALE-hycom.md) in the run's output, `/scratch/<your-project>/$USER/mom6-examples/archive/global_ALE-hycom/output000/MOM_parameter_doc.all` when you run the script

**1** parameter values differ; **5** parameters exist only in this run's MOM6 version and **13** only in the reference (new, removed or renamed parameters). Values are compared ignoring quotes, case and number formatting. Parameter names link to a search of the MOM6 source; reference values link to their line on GitHub and this run's line numbers to its file.

<table class="diff" markdown="1"><thead><tr><th>Parameter</th><th>Units</th><th>A: reference</th><th>B: this run</th></tr></thead><tbody markdown="1"><tr class="mod"><td colspan="4">MOM_set_visc</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=SET_VISC_ANSWER_DATE" target="_blank" rel="noopener">SET_VISC_ANSWER_DATE</a></td><td class="units"></td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L1123" target="_blank" rel="noopener">20260703</a></td><td class="val b" data-label="B: this run" markdown="span">99991231 [line 1112](../parameters/global_ALE-hycom.md#L1112){.ln}</td></tr></tbody></table>

??? note "Parameters in only one of the two files (18)"
    <table class="diff" markdown="1"><thead><tr><th>Parameter</th><th>Units</th><th>A: reference</th><th>B: this run</th></tr></thead><tbody markdown="1"><tr class="mod"><td colspan="4">MOM</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=NONBLOCKING_P_SURF_BUG" target="_blank" rel="noopener">NONBLOCKING_P_SURF_BUG</a></td><td class="units">Boolean</td><td class="val a unset" data-label="A: reference">(not in this version)</td><td class="val b" data-label="B: this run" markdown="span">True [line 152](../parameters/global_ALE-hycom.md#L152){.ln}</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=USE_UH_PARTICLES" target="_blank" rel="noopener">USE_UH_PARTICLES</a></td><td class="units">Boolean</td><td class="val a unset" data-label="A: reference">(not in this version)</td><td class="val b" data-label="B: this run" markdown="span">False [line 207](../parameters/global_ALE-hycom.md#L207){.ln}</td></tr><tr class="mod"><td colspan="4">MOM_barotropic</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=DTBT_RESTART_BUG" target="_blank" rel="noopener">DTBT_RESTART_BUG</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L1831" target="_blank" rel="noopener">True</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_continuity_PPM</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=CONT_USE_H_MARG_MIN" target="_blank" rel="noopener">CONT_USE_H_MARG_MIN</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L1361" target="_blank" rel="noopener">False</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_coord_initialization</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=REGRID_USE_DEPTH_BASED_TIME_FILTER" target="_blank" rel="noopener">REGRID_USE_DEPTH_BASED_TIME_FILTER</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L681" target="_blank" rel="noopener">True</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=USE_ADJUST_INTERFACE_MOTION" target="_blank" rel="noopener">USE_ADJUST_INTERFACE_MOTION</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L601" target="_blank" rel="noopener">True</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_diag_mediator</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=NUM_DIAG_DOWNSAMP_LEV" target="_blank" rel="noopener">NUM_DIAG_DOWNSAMP_LEV</a></td><td class="units"></td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L820" target="_blank" rel="noopener">0</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=SYMMETRIC_DOWNSAMPLE_SUMS" target="_blank" rel="noopener">SYMMETRIC_DOWNSAMPLE_SUMS</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L809" target="_blank" rel="noopener">False</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_geothermal</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=GEOTHERMAL_MIN_COLUMN_THICKNESS" target="_blank" rel="noopener">GEOTHERMAL_MIN_COLUMN_THICKNESS</a></td><td class="units">m</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L2007" target="_blank" rel="noopener">0.0</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_grid_init</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=READ_MEAN_SEA_LEVEL" target="_blank" rel="noopener">READ_MEAN_SEA_LEVEL</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L255" target="_blank" rel="noopener">False</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_PressureForce_FV</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=RHO_PGF_REF_BUG" target="_blank" rel="noopener">RHO_PGF_REF_BUG</a></td><td class="units">Boolean</td><td class="val a unset" data-label="A: reference">(not in this version)</td><td class="val b" data-label="B: this run" markdown="span">True [line 1455](../parameters/global_ALE-hycom.md#L1455){.ln}</td></tr><tr class="mod"><td colspan="4">MOM_restart</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=ENSEMBLE_APPENDIX_PREFIX" target="_blank" rel="noopener">ENSEMBLE_APPENDIX_PREFIX</a></td><td class="units"></td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L404" target="_blank" rel="noopener">&quot;&quot;</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_set_visc</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=CDRAG_MAP" target="_blank" rel="noopener">CDRAG_MAP</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L1159" target="_blank" rel="noopener">False</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=CHANNEL_DRAG_SHELFBREAK_DEPTH" target="_blank" rel="noopener">CHANNEL_DRAG_SHELFBREAK_DEPTH</a></td><td class="units">m</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L1141" target="_blank" rel="noopener">0.0</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_thickness_diffuse</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=USE_THICKNESS_DIFFUSE_ANN" target="_blank" rel="noopener">USE_THICKNESS_DIFFUSE_ANN</a></td><td class="units">Boolean</td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L1211" target="_blank" rel="noopener">False</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr><tr class="mod"><td colspan="4">MOM_tracer_flow_control</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=USE_FILE_DYES" target="_blank" rel="noopener">USE_FILE_DYES</a></td><td class="units">Boolean</td><td class="val a unset" data-label="A: reference">(not in this version)</td><td class="val b" data-label="B: this run" markdown="span">False [line 439](../parameters/global_ALE-hycom.md#L439){.ln}</td></tr><tr class="mod"><td colspan="4">MOM_verticalGrid</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=ADVECTION_SCHEME_VARIANCE_UNDERFLOW" target="_blank" rel="noopener">ADVECTION_SCHEME_VARIANCE_UNDERFLOW</a></td><td class="units">Conc2 (tracer dependent)</td><td class="val a unset" data-label="A: reference">(not in this version)</td><td class="val b" data-label="B: this run" markdown="span">1.0E-23 [line 359](../parameters/global_ALE-hycom.md#L359){.ln}</td></tr><tr class="mod"><td colspan="4">ocean_stochastics_init</td></tr><tr class="param" markdown="1"><td><a href="https://github.com/mom-ocean/MOM6/search?q=STOCHASTICS_ANSWER_DATE" target="_blank" rel="noopener">STOCHASTICS_ANSWER_DATE</a></td><td class="units"></td><td class="val a" data-label="A: reference"><a href="https://github.com/NOAA-GFDL/MOM6-examples/blob/c1730b8efe16cf7f12fc8db588115cae50f3e802/ocean_only/global_ALE/hycom/MOM_parameter_doc.all#L2600" target="_blank" rel="noopener">20250101</a></td><td class="val b unset" data-label="B: this run">(not in this version)</td></tr></tbody></table>

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
| PBS Job Id | `183115754.gadi-pbs` |
| PBS Exit Status | `0` |
| PBS Service Units | `1.67` |
| PBS NCPUs Requested | `64` |
| PBS Walltime Used | `00:00:47` |
| PBS Memory Used | `25.34GB` |

??? info "Input files and md5 hashes (from payu `manifests/input.yaml`)"
    | File | md5 | Comes from |
    |---|---|---|
    | `INPUT/31Layer_zgrid.nc` | `2d1b8673dc763a835081ab6d0e13d6d2` | `ol01` data: `global/siena_201204/INPUT/31Layer_zgrid.nc` |
    | `INPUT/GOLD_IC.2010.11.15.nc` | `bf6ba441e98ff5c1b04b635b0ad84dac` | `ol01` data: `global/siena_201204/INPUT/GOLD_IC.2010.11.15.nc` |
    | `INPUT/Layer_coord.cdl` | `db3247a6fa0db236260ed2baf3ec0225` | MOM6-examples: `ocean_only/global_ALE/common/INPUT/Layer_coord.cdl` |
    | `INPUT/Layer_coord.nc` | `1d91bdff8a01fe461ecbc3dc1804b2a6` | MOM6-examples: `ocean_only/global_ALE/common/INPUT/Layer_coord.nc` |
    | `INPUT/Layer_coord50.cdl` | `0281af583b85dd773581c0c5244a0a84` | MOM6-examples: `ocean_only/global_ALE/common/INPUT/Layer_coord50.cdl` |
    | `INPUT/Layer_coord50.nc` | `696fbfcf664b79c14815e678a9107f71` | MOM6-examples: `ocean_only/global_ALE/common/INPUT/Layer_coord50.nc` |
    | `INPUT/OM3_zgrid.nc` | `0830d67f80834fe2796b219a84b3ba8d` | `ol01` data: `global/siena_201204/INPUT/OM3_zgrid.nc` |
    | `INPUT/WOA05_pottemp_salt.nc` | `46803f1e1595e29ea527086438a58391` | `ol01` data: `obs/WOA05_pottemp_salt.nc` |
    | `INPUT/analysis_vgrid_lev35.v1.cdl` | `777b45acea071ca1a147760a2b850e41` | MOM6-examples: `ocean_only/global_ALE/common/INPUT/analysis_vgrid_lev35.v1.cdl` |
    | `INPUT/analysis_vgrid_lev35.v1.nc` | `cdfdc287b327daa2be262a67e57519fd` | MOM6-examples: `ocean_only/global_ALE/common/INPUT/analysis_vgrid_lev35.v1.nc` |
    | `INPUT/atmos_hgrid.nc` | `a4d8a2cc7554b265f53da1f91a48fee1` | `ol01` data: `global/siena_201204/mosaic.unpacked/atmos_hgrid.nc` |
    | `INPUT/atmos_mosaic.nc` | `ed209f7d19cc856ec1a257c0ca63af90` | `ol01` data: `global/siena_201204/mosaic.unpacked/atmos_mosaic.nc` |
    | `INPUT/atmos_mosaic_tile1Xland_mosaic_tile1.nc` | `6025fff17ee89d0ef6f4ac530c4a833b` | `ol01` data: `global/siena_201204/mosaic.unpacked/atmos_mosaic_tile1Xland_mosaic_tile1.nc` |
    | `INPUT/atmos_mosaic_tile1Xocean_mosaic_tile1.nc` | `c4ee9d91f1b2146d8e0c60827670fee6` | `ol01` data: `global/siena_201204/mosaic.unpacked/atmos_mosaic_tile1Xocean_mosaic_tile1.nc` |
    | `INPUT/geothermal_heating_cm2g.nc` | `2604459298a435e292be908e6059a89f` | `ol01` data: `global/siena_201204/INPUT/geothermal_heating_cm2g.nc` |
    | `INPUT/grid_spec.nc` | `a2d3b842655c6ee2e0213db46154dc22` | `ol01` data: `global/siena_201204/mosaic.unpacked/grid_spec.nc` |
    | `INPUT/gustiness_qscat.nc` | `2fbcc31e266329ddb4dd1cd8c8d221f7` | `ol01` data: `global/siena_201204/INPUT/gustiness_qscat.nc` |
    | `INPUT/hycom1_50.cdl` | `bb6a8c90545b7511de61b93c4f44c01a` | MOM6-examples: `ocean_only/global_ALE/common/INPUT/hycom1_50.cdl` |
    | `INPUT/hycom1_50.nc` | `bbd1cf56686a11a342d61d9db3286b0d` | MOM6-examples: `ocean_only/global_ALE/common/INPUT/hycom1_50.nc` |
    | `INPUT/land_hgrid.nc` | `a4d8a2cc7554b265f53da1f91a48fee1` | `ol01` data: `global/siena_201204/mosaic.unpacked/land_hgrid.nc` |
    | `INPUT/land_mask.nc` | `d5caa6ffe6379a31e692f10ec65af033` | `ol01` data: `global/siena_201204/mosaic.unpacked/land_mask.nc` |
    | `INPUT/land_mosaic.nc` | `5aeb9c82ad3a1c2ecc3d7988aa641ad2` | `ol01` data: `global/siena_201204/mosaic.unpacked/land_mosaic.nc` |
    | `INPUT/land_mosaic_tile1Xocean_mosaic_tile1.nc` | `56c455a11d61a23e19f056bf6c99cb7c` | `ol01` data: `global/siena_201204/mosaic.unpacked/land_mosaic_tile1Xocean_mosaic_tile1.nc` |
    | `INPUT/mosaic.nc` | `a2d3b842655c6ee2e0213db46154dc22` | `ol01` data: `global/siena_201204/mosaic.unpacked/mosaic.nc` |
    | `INPUT/ocean_forcing_daily.nc` | `7065687a13038c404173d8c19525794b` | `ol01` data: `global/siena_201204/INPUT/ocean_forcing_daily.nc` |
    | `INPUT/ocean_forcing_monthly.nc` | `b26fd7fb52928bbfea285f87479c15f0` | `ol01` data: `global/siena_201204/INPUT/ocean_forcing_monthly.nc` |
    | `INPUT/ocean_hgrid.nc` | `c4782f49333b46f9ea53322ac1eff53a` | `ol01` data: `global/siena_201204/mosaic.unpacked/ocean_hgrid.nc` |
    | `INPUT/ocean_mask.nc` | `b49dce31f5a9cd53a8ebbb47518e238c` | `ol01` data: `global/siena_201204/mosaic.unpacked/ocean_mask.nc` |
    | `INPUT/ocean_mosaic.nc` | `1263df68b94e7a256be52283df611e94` | `ol01` data: `global/siena_201204/mosaic.unpacked/ocean_mosaic.nc` |
    | `INPUT/ocean_precip_monthly.nc` | `12031a11fbcd3ca1a0534d7feb9193fc` | `ol01` data: `global/siena_201204/INPUT/ocean_precip_monthly.nc` |
    | `INPUT/ocean_vgrid.nc` | `34d06772f261d0ef502b4e3998109c28` | `ol01` data: `global/siena_201204/mosaic.unpacked/ocean_vgrid.nc` |
    | `INPUT/seawifs_1998-2006_GOLD_smoothed_2X.nc` | `7217a6bb87ebdf4570bbf8940e8b3c72` | `ol01` data: `global/siena_201204/INPUT/seawifs_1998-2006_GOLD_smoothed_2X.nc` |
    | `INPUT/sgs_h2.nc` | `5f3897a97a4366edba744f35cea97d7d` | `ol01` data: `global/siena_201204/INPUT/sgs_h2.nc` |
    | `INPUT/tideamp.nc` | `8136b3e8b8f587734fc5b0abcb338702` | `ol01` data: `global/siena_201204/INPUT/tideamp.nc` |
    | `INPUT/topog.nc` | `bd19baefec0f42e89e90870fbee5a7e3` | `ol01` data: `global/siena_201204/mosaic.unpacked/topog.nc` |
    | `INPUT/vgrid.cdl` | `5a93ca59f7f4d4807eeaef83ebce0297` | MOM6-examples: `ocean_only/global_ALE/common/INPUT/vgrid.cdl` |
    | `INPUT/vgrid.nc` | `36555c9866ffd1f20b9d1954f3dd24b4` | MOM6-examples: `ocean_only/global_ALE/common/INPUT/vgrid.nc` |

??? info "Run-time environment (selected variables from payu's `env.yaml`)"
    | Variable | Value |
    |---|---|
    | `LD_LIBRARY_PATH` | `/apps/openmpi/4.1.7/lib:/apps/openmpi/4.1.7/lib/profilers` |
    | `LOADEDMODULES` | `access3-share/2026.03.002-eale5gm:access-cice/CICE6.6.3-2-huasrvo:access-mocsy/2025.07.002-saj7rvh:access-generic-tracers/2026.09.000-e3zb3ez:access-mom6/2026.05.003-ld7hklz:access-ww3/2026.03.001-bjzidie:access3/2026.03.002-26wbxup:access-om3/2026.05.004:pbs:openmpi/4.1.7` |
    | `OMPI_MCA_orte_tmpdir_base` | `/jobfs/183115754.gadi-pbs` |
    | `PAYU_TELEMETRY_ENV_VERSION` | `1.3.6_1` |
    | `PBS_NCI_NCPUS_PER_NODE` | `104` |
    | `PBS_NCPUS` | `64` |
    | `PBS_QUEUE` | `normalsr-exec` |

??? info "payu config.yaml written by the script"
    ```yaml
    # payu configuration for MOM6-examples/ocean_only/global_ALE/hycom (written by global_ALE-hycom.sh)
    project: tm70
    queue: normalsr          # mom6-solo is compiled for Sapphire Rapids nodes
    ncpus: 64
    walltime: 01:00:00
    jobname: global_ALE-hycom
    experiment: global_ALE-hycom
    laboratory: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/lab

    model: mom6
    exe: mom6-solo           # found on PATH once the module below is loaded
    input: /g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs/MOM6-examples/ocean_only/global_ALE/hycom/INPUT

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
    | `MOM_IC.nc` | 461.20 MB | Initial state written by MOM6 at the start of the run |
    | `Vertical_coordinate.nc` | 0.00 MB | The vertical coordinate: target values of the layers or levels |
    | `ave_prog.nc` | 76.05 MB | Diagnostics set in `diag_table`: time averages of `u`, `v`, `h`, `e`, every 1 days |
    | `cmor.nc` | 159.83 MB | Diagnostics set in `diag_table`: snapshots and averages of `pso`, `tauuo`, `tauvo`, `wfo`, `rsntds`, `rlntds`, `hfibthermds`, `hfrunoffds` and 27 more, every 1 days |
    | `cmor2.nc` | 3.66 MB | Diagnostics set in `diag_table`: snapshots and averages of `hfgeou`, `hfrainds`, `hfevapds`, `hfrunoffds`, `hfsnthermds`, `hfsifrazil`, `hfibthermds`, `rlntds` and 2 more, every 1 days |
    | `cmor_scalar.nc` | 0.02 MB | Diagnostics set in `diag_table`: time averages of `masso`, `thetaoga`, `soga`, `tosga`, `sosga`, `volo`, every 1 days |
    | `cmor_z.nc` | 61.88 MB | Diagnostics set in `diag_table`: time averages of `uo`, `vo`, `so`, `thetao`, `umo`, `vmo`, every 1 days |
    | `cont.nc` | 229.95 MB | Diagnostics set in `diag_table`: time averages of `wd`, `uh`, `vh`, `h_rho`, `uh_rho`, `vh_rho`, `uhGM_rho`, `vhGM_rho` and 11 more, every 1 days |
    | `forcing.nc` | 36.34 MB | Diagnostics set in `diag_table`: time averages of `taux`, `tauy`, `ustar`, `p_surf`, `PRCmE`, `net_massin`, `net_massout`, `lrunoff` and 55 more, every 12 hours |
    | `layer.nc` | 0.02 MB | Diagnostics set in `diag_table`: time averages of `temp_layer_ave`, `salt_layer_ave`, every 1 days |
    | `ocean.stats.nc` | 0.01 MB | Domain totals at each energy-save time (energy, mass, heat, salt, maximum CFL); the netCDF form of `ocean.stats` |
    | `ocean_geometry.nc` | 11.56 MB | Static grid: coordinates, cell sizes and areas, bottom depth `D`, Coriolis parameter, land mask |
    | `ocean_static.nc` | 5.79 MB | Diagnostics set in `diag_table`: snapshots of `geolon`, `geolat`, `geolon_c`, `geolat_c`, `geolon_u`, `geolat_u`, `geolon_v`, `geolat_v` and 7 more, written once (static) |
    | `ocean_static_cmor.nc` | 0.32 MB | Diagnostics set in `diag_table`: snapshots of `areacello`, written once (static) |
    | `prog.nc` | 106.29 MB | Diagnostics set in `diag_table`: snapshots of `u`, `v`, `h`, `e`, `temp`, `salt`, every 1 days |
    | `prog_z.nc` | 41.23 MB | Diagnostics set in `diag_table`: time averages of `u`, `v`, `temp`, `temp_xyave`, `salt`, every 1 days |
    | `scalar.nc` | 0.02 MB | Diagnostics set in `diag_table`: time averages of `masso`, `thetaoga`, `soga`, `tosga`, `sosga`, `volo`, `ssh_ga`, `prcme_ga` and 9 more, every 1 days |
    | `sfc_ave.nc` | 3.66 MB | Diagnostics set in `diag_table`: time averages of `SSH`, `SST`, `SSS`, `speed`, `SSU`, `SSV`, every 12 hours |
    | `surface.nc` | 7.90 MB | Diagnostics set in `diag_table`: snapshots of `mass_wt`, `opottempmint`, `somint`, `SSH`, `SST`, `SSS`, `speed`, `SSU` and 1 more, every 12 hours |
    | `tracer.nc` | 243.92 MB | Diagnostics set in `diag_table`: time averages of `T_adx`, `T_ady`, `T_diffx`, `T_diffy`, `S_adx`, `S_ady`, `S_diffx`, `S_diffy` and 13 more, every 1 days |
    | `visc.nc` | 78.35 MB | Diagnostics set in `diag_table`: time averages of `Kd_interface`, `Kd_layer`, `Kd_effective`, `Kd_itides`, `Kd_shear`, `Kd_BBL`, `MLD_003`, `subML_N2` and 3 more, every 1 days |

