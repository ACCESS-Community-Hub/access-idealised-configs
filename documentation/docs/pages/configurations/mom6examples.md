# MOM6 examples on Gadi

The [NOAA-GFDL/MOM6-examples](https://github.com/NOAA-GFDL/MOM6-examples) repository holds
GFDL's MOM6 test cases, from idealised ones that need no input data (double gyre,
seamount, lock exchange, ...) to realistic global ones.
This section shows which of the ocean-only (`ocean_only/`) cases run on NCI Gadi with the
**prebuilt MOM6 ocean-only executable `mom6-solo` from the ACCESS-OM3 release**, so
you don't have to compile MOM6 yourself.

**1 of 57 tested runs completed successfully** (tested on 2026-11-04).

!!! note "Generated with Claude Code"
    Everything in this section was run, checked and written up automatically by
    [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs),
    a set of scripts written with [Claude Code](https://claude.com/claude-code) and
    reviewed by humans. Each page shows the exact script that produced it, plus the
    versions, input-file hashes and run-time environment that were used.
    Spotted something wrong? Please [raise an issue](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/issues).

## Quick start

From a Gadi **login node**, any example is one command. For example, the wind-driven
double gyre:

```bash
PROJECT=<your-project> bash double_gyre.sh
```

where `double_gyre.sh` is the script on the [double_gyre](mom6examples/double_gyre.md) page
(copy it with the button in the top-right of the code block). It:

1. clones `MOM6-examples` (configuration files only) at the tested commit,
2. links the shared input data in `/g/data/ol01`,
3. writes a [payu](https://payu.readthedocs.io) `config.yaml` that uses `mom6-solo` from
   the `access-om3/2026.05.004` module, and
4. submits the run with `payu run`. Output appears in
   `/scratch/<your-project>/$USER/mom6-examples/archive/<example>/output000/`.

You need to be a member of the NCI projects **`vk83`** (ACCESS-NRI software:
[join vk83](https://my.nci.org.au/mancini/project/vk83/join)) and **`ol01`**
(the MOM6-examples input data: [join ol01](https://my.nci.org.au/mancini/project/ol01/join)).

!!! warning "Run from a login node, not from ARE/JupyterLab"
    `payu` runs inside its own container and **cannot be started from inside another
    container**, such as an ARE JupyterLab terminal with `conda/analysis3` loaded. There it
    hangs (the launcher keeps re-executing itself) or fails with
    `starter-suid doesn't have setuid bit set`. Use an ordinary `ssh gadi` login shell, or
    submit the script as a small PBS job (see
    [`lib/run_in_pbs.pbs`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/blob/main/tested-configs/lib/run_in_pbs.pbs)).

## Results

| Example | Status | Cores | SU | Description |
|---|---|---|---|---|
| **Basins and channels** | | | | |
| [double_gyre](mom6examples/double_gyre.md) | :white_check_mark: ran | 8 | 0.07 | Wind-driven, adiabatic two-layer-style double gyre in a 22° x 20° spherical box (30°N-50°N) with "spoon" bathymetry. A classic test bed for western boundary currents (think Gulf Stream/East Australian Current) and their separation. |
| [double_gyre-10yr](mom6examples/double_gyre-10yr.md) | not run | 8 |  | Variant of `double_gyre` with `DAYMAX=3650.0`. Wind-driven, adiabatic two-layer-style double gyre in a 22° x 20° spherical box (30°N-50°N) with "spoon" bathymetry. A classic test bed for western boundary currents (think Gulf Stream/East Australian Current) and their separation. |
| [DOME](mom6examples/DOME.md) | not run | 6 |  | Dynamics of Overflow Mixing and Entrainment: dense water flows from an embayment down a continental slope (Legg et al. 2006 test case). |
| [Phillips_2layer](mom6examples/Phillips_2layer.md) | not run | 64 |  | Two-layer, flat-bottomed Cartesian channel initialised with a Phillips-type baroclinically unstable flow. |
| [benchmark](mom6examples/benchmark.md) | not run | 72 |  | The MOM6 benchmark case: a 360 x 180 Mercator basin (41°S-41°N, 22 layers) with analytic "benchmark" bathymetry and stratification, gyre winds and linear buoyancy forcing. |
| [buoy_forced_basin](mom6examples/buoy_forced_basin.md) | not run | 6 |  | Buoyancy-forced ("BFB") flat-bottomed basin on a Mercator grid (10°N-60°N, 10 levels). |
| [circle_obcs](mom6examples/circle_obcs.md) | not run | 2 |  | Open-boundary-condition test: a circular anomaly in a 25 x 25 flat box with four open boundary segments. |
| [external_gwave](mom6examples/external_gwave.md) | not run | 2 |  | Simple gravitational adjustment of a sea-surface displacement (external gravity wave). |
| [lock_exchange](mom6examples/lock_exchange.md) | not run | 2 |  | Lock-exchange gravity current: two fluids of different density released side by side. |
| [mixed_layer_restrat_2d](mom6examples/mixed_layer_restrat_2d.md) | not run | 2 |  | Quasi-2-D (4 x 80) Rossby-front mixed-layer restratification test in z* coordinates. |
| [torus_advection_test](mom6examples/torus_advection_test.md) | not run | 2 |  | Advection test on a flat, doubly periodic (torus) 48 x 48 Cartesian domain. |
| [unit_tests](mom6examples/unit_tests.md) | not run | 1 |  | Runs MOM6's internal unit tests on a trivial domain. |
| **Vertical-coordinate tests** | | | | |
| [adjustment2d-layer](mom6examples/adjustment2d-layer.md) | not run | 2 |  | Two-dimensional geostrophic adjustment of a front, in layered (isopycnal) coordinates. |
| [adjustment2d-rho](mom6examples/adjustment2d-rho.md) | not run | 2 |  | Two-dimensional geostrophic adjustment of a front, in ALE density coordinates. |
| [adjustment2d-z](mom6examples/adjustment2d-z.md) | not run | 2 |  | Two-dimensional geostrophic adjustment of a front, in ALE z* coordinates. |
| [flow_downslope-layer](mom6examples/flow_downslope-layer.md) | not run | 2 |  | Dense water flowing down a 2-D slope, in layered (isopycnal) coordinates. |
| [flow_downslope-rho](mom6examples/flow_downslope-rho.md) | not run | 2 |  | Dense water flowing down a 2-D slope, in ALE density coordinates. |
| [flow_downslope-sigma](mom6examples/flow_downslope-sigma.md) | not run | 2 |  | Dense water flowing down a 2-D slope, in terrain-following (sigma) coordinates. |
| [flow_downslope-z](mom6examples/flow_downslope-z.md) | not run | 2 |  | Dense water flowing down a 2-D slope, in ALE z* coordinates. |
| [resting-layer](mom6examples/resting-layer.md) | not run | 2 |  | A resting, stratified ocean that should stay at rest (pressure-gradient error test), layered coordinates. |
| [resting-z](mom6examples/resting-z.md) | not run | 2 |  | A resting, stratified ocean that should stay at rest (pressure-gradient error test), z* coordinates. |
| [seamount-layer](mom6examples/seamount-layer.md) | not run | 2 |  | Stratified ocean at rest over a seamount; spurious currents measure pressure-gradient errors (layered coordinates). |
| [seamount-rho](mom6examples/seamount-rho.md) | not run | 2 |  | Stratified ocean at rest over a seamount; spurious currents measure pressure-gradient errors (density coordinates). |
| [seamount-sigma](mom6examples/seamount-sigma.md) | not run | 2 |  | Stratified ocean at rest over a seamount; spurious currents measure pressure-gradient errors (sigma coordinates). |
| [seamount-z](mom6examples/seamount-z.md) | not run | 2 |  | Stratified ocean at rest over a seamount; spurious currents measure pressure-gradient errors (z* coordinates). |
| [sloshing-layer](mom6examples/sloshing-layer.md) | not run | 2 |  | Sloshing of a tilted stratification in a closed 2-D basin (layered coordinates). |
| [sloshing-rho](mom6examples/sloshing-rho.md) | not run | 2 |  | Sloshing of a tilted stratification in a closed 2-D basin (density coordinates). |
| [sloshing-z](mom6examples/sloshing-z.md) | not run | 2 |  | Sloshing of a tilted stratification in a closed 2-D basin (z* coordinates). |
| [tracer_mixing-rho](mom6examples/tracer_mixing-rho.md) | not run | 2 |  | Tracer mixing/advection test in density coordinates. |
| [tracer_mixing-z](mom6examples/tracer_mixing-z.md) | not run | 2 |  | Tracer mixing/advection test in z* coordinates. |
| **Ice-shelf cavity** | | | | |
| [ISOMIP-layer](mom6examples/ISOMIP-layer.md) | not run | 24 |  | ISOMIP (first phase) ice-shelf cavity test with a static ice shelf, layered coordinates. |
| [ISOMIP-rho](mom6examples/ISOMIP-rho.md) | not run | 24 |  | ISOMIP (first phase) ice-shelf cavity test with a static ice shelf, density coordinates. |
| **Hurricanes and single columns** | | | | |
| [SCM_idealized_hurricane](mom6examples/SCM_idealized_hurricane.md) | not run | 1 |  | Single-column version of the idealized hurricane case: boundary-layer response to a passing storm. |
| [idealized_hurricane](mom6examples/idealized_hurricane.md) | not run | 32 |  | An idealized (Holland-profile) hurricane moving across an ocean basin. |
| [single_column-BML](mom6examples/single_column-BML.md) | not run | 1 |  | Single column at BATS with the bulk mixed layer (BML) scheme. |
| [single_column-EPBL](mom6examples/single_column-EPBL.md) | not run | 1 |  | Single column at BATS with the energetic planetary boundary layer (ePBL) scheme. |
| [single_column-KPP](mom6examples/single_column-KPP.md) | not run | 1 |  | Single column at BATS with the K-profile parameterisation (KPP). |
| [CVmix_SCM_tests-cooling_only-BML](mom6examples/CVmix_SCM_tests-cooling_only-BML.md) | not run | 1 |  | CVMix single-column test: `cooling_only` surface forcing with the `BML` boundary-layer scheme. |
| [CVmix_SCM_tests-cooling_only-EPBL](mom6examples/CVmix_SCM_tests-cooling_only-EPBL.md) | not run | 1 |  | CVMix single-column test: `cooling_only` surface forcing with the `EPBL` boundary-layer scheme. |
| [CVmix_SCM_tests-cooling_only-KPP](mom6examples/CVmix_SCM_tests-cooling_only-KPP.md) | not run | 1 |  | CVMix single-column test: `cooling_only` surface forcing with the `KPP` boundary-layer scheme. |
| [CVmix_SCM_tests-mech_only-BML](mom6examples/CVmix_SCM_tests-mech_only-BML.md) | not run | 1 |  | CVMix single-column test: `mech_only` surface forcing with the `BML` boundary-layer scheme. |
| [CVmix_SCM_tests-mech_only-EPBL](mom6examples/CVmix_SCM_tests-mech_only-EPBL.md) | not run | 1 |  | CVMix single-column test: `mech_only` surface forcing with the `EPBL` boundary-layer scheme. |
| [CVmix_SCM_tests-mech_only-KPP](mom6examples/CVmix_SCM_tests-mech_only-KPP.md) | not run | 1 |  | CVMix single-column test: `mech_only` surface forcing with the `KPP` boundary-layer scheme. |
| [CVmix_SCM_tests-skin_warming_wind-BML](mom6examples/CVmix_SCM_tests-skin_warming_wind-BML.md) | not run | 1 |  | CVMix single-column test: `skin_warming_wind` surface forcing with the `BML` boundary-layer scheme. |
| [CVmix_SCM_tests-skin_warming_wind-EPBL](mom6examples/CVmix_SCM_tests-skin_warming_wind-EPBL.md) | not run | 1 |  | CVMix single-column test: `skin_warming_wind` surface forcing with the `EPBL` boundary-layer scheme. |
| [CVmix_SCM_tests-skin_warming_wind-KPP](mom6examples/CVmix_SCM_tests-skin_warming_wind-KPP.md) | not run | 1 |  | CVMix single-column test: `skin_warming_wind` surface forcing with the `KPP` boundary-layer scheme. |
| [CVmix_SCM_tests-wind_only-BML](mom6examples/CVmix_SCM_tests-wind_only-BML.md) | not run | 1 |  | CVMix single-column test: `wind_only` surface forcing with the `BML` boundary-layer scheme. |
| [CVmix_SCM_tests-wind_only-EPBL](mom6examples/CVmix_SCM_tests-wind_only-EPBL.md) | not run | 1 |  | CVMix single-column test: `wind_only` surface forcing with the `EPBL` boundary-layer scheme. |
| [CVmix_SCM_tests-wind_only-KPP](mom6examples/CVmix_SCM_tests-wind_only-KPP.md) | not run | 1 |  | CVMix single-column test: `wind_only` surface forcing with the `KPP` boundary-layer scheme. |
| **Realistic (need the GFDL input data)** | | | | |
| [global](mom6examples/global.md) | not run | 64 |  | Global 1° (360 x 210 mosaic grid) ocean with 63 layers, MEKE and tides, forced by data from files. |
| [nonBous_global](mom6examples/nonBous_global.md) | not run | 60 |  | As `global`, but non-Boussinesq. |
| [global_ALE-hycom](mom6examples/global_ALE-hycom.md) | not run | 64 |  | Global 1° ocean with ALE hybrid (HYCOM-like) coordinates. |
| [global_ALE-layer](mom6examples/global_ALE-layer.md) | not run | 64 |  | Global 1° ocean with ALE in layer mode. |
| [global_ALE-z](mom6examples/global_ALE-z.md) | not run | 64 |  | Global 1° ocean with ALE z* coordinates. |
| [MESO_025_23L](mom6examples/MESO_025_23L.md) | not run | 288 |  | Near-global 1/4° (1440 x 450 Mercator, 74°S-74°N) "MESO" configuration with 23 layers. |
| [MESO_025_63L](mom6examples/MESO_025_63L.md) | not run | 288 |  | Near-global 1/4° "MESO" configuration with 63 layers. |
| [tides_025](mom6examples/tides_025.md) | not run | 480 |  | Global 1/4° (1440 x 1080) non-Boussinesq, two-layer tides configuration. |

Cores = processor layout GFDL used for that example (`NIPROC x NJPROC` in its
`MOM_parameter_doc.layout`). Runs use the example's own run length, which is usually a
few days: these are tests that the model runs, not science-ready simulations.
Pages with a suffix (e.g. `double_gyre-10yr`) are *variants*: copies of the example with
a few extra lines in `MOM_override`, such as a longer run, to show a spun-up state.

## How these pages were made

| What | Version used |
|---|---|
| MOM6-examples | [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802) (branch `dev/gfdl`) |
| ACCESS-OM3 release | [`access-om3/2026.05.004`](https://github.com/ACCESS-NRI/ACCESS-OM3/releases) |
| MOM6 component module | `access-mom6/2026.05.003-ld7hklz` |
| MOM6 source code | `` ([ACCESS-NRI/MOM6](https://github.com/ACCESS-NRI/MOM6)) |
| Executable | `/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access-mom6-2026.05.003-ld7hklzo5ajizx5u4yl74i4ijberrpv6/bin/mom6-solo` |
| Executable md5 | `4785d157c76c30d8d01baf7d0f69d218` |
| payu | `payu 1.3.6_1` |
| Scripts (this repository) | commit `958cc953bd63140389928448716e1d9297f4369e` |

The pipeline lives in [`tested-configs/`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs):

| File | Purpose |
|---|---|
| `versions.env` | pinned versions: MOM6-examples commit, ACCESS-OM3 module, payu module, data path |
| `examples.txt` | which examples to run, with how many cores and what walltime |
| `templates/run_example.sh.in` | the commented run script that every page embeds |
| `regenerate_all.sh` | does everything: write scripts, run, wait, summarise, write pages |
| `lib/summarise_run.py` | checks a run (`ocean.stats`), reads payu manifests (md5 hashes), makes the figure |
| `lib/make_pages.py` | writes these pages from `results/*/summary.json` |

To re-test everything with a new ACCESS-OM3 release, edit `versions.env` and run
`PROJECT=<proj> ./regenerate_all.sh` from a login node.

**What "ran" means:** the job finished, `ocean.stats` has more than two lines and contains
no `NaN`. We also compare every run's `MOM_parameter_doc.all` with the one GFDL
committed for that example. The differences (renamed, new or removed parameters,
changed defaults) are listed on each page, because they show where the ACCESS-OM3 MOM6
version behaves differently from the GFDL version the example was written for. We did
**not** compare answers bit-for-bit with GFDL.
