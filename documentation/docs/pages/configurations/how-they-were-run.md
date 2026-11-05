# How this website is generated

Every configuration on this website, both the COSIMA community ones and the MOM6 examples,
was run in the same way:

- on NCI Gadi, with a **prebuilt executable from the ACCESS-OM3 release**
  (`access-om3/2026.05.004`): the MOM6 ocean-only `mom6-solo`, or the coupled `access-om3-MOM6` for
  the ACCESS-OM3 single column; so nobody has to compile MOM6;
- with [payu](https://payu.readthedocs.io), from **one script per configuration**, shown in
  full on that configuration's page;
- then checked, summarised and written up by the same scripts.

To run one yourself, see the [quick start](../index.md#quick-start).

**Last test:** 2026-11-04. 49 of 57 MOM6-example runs completed successfully; the
status of every run is in the tables on the [Overview](Overview.md).

--8<-- "tested-configs/templates/claude_caveat.md"

## Versions used for every run

| What | Version used |
|---|---|
| ACCESS-OM3 release | [`access-om3/2026.05.004`](https://github.com/ACCESS-NRI/ACCESS-OM3/releases) |
| MOM6 component module | `access-mom6/2026.05.003-ld7hklz` |
| MOM6 source code | `ACCESS-NRI/MOM6 2026.05.003 d11a149ccba676d524312328f7eb62560a156dc3` ([ACCESS-NRI/MOM6](https://github.com/ACCESS-NRI/MOM6)) |
| Executable | `/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access-mom6-2026.05.003-ld7hklzo5ajizx5u4yl74i4ijberrpv6/bin/mom6-solo` |
| Executable md5 | `4785d157c76c30d8d01baf7d0f69d218` |
| payu | `payu 1.3.6_1` |
| MOM6-examples | [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802) (branch `dev/gfdl`) |
| Scripts (this repository) | runs: [`0bf2ffcf`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/tree/0bf2ffcfef6199dd6461cbbc64d2bdaf06f3d671/tested-configs); pages: [`31427534`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/tree/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs) |

Each configuration's page also lists the md5 hash of every input file (from payu's
manifests), the run-time environment and the PBS resources used.

## What each script does

### MOM6 examples

All MOM6 examples use the same script template
([`templates/run_example.sh.in`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/templates/run_example.sh.in)),
filled in with the example's name, cores and walltime from `examples.txt`. Each script:

1. clones `MOM6-examples` (configuration files only) at the tested commit;
2. links the shared input data in `/g/data/ol01` (see [About the input data](#about-the-input-data));
3. writes a payu `config.yaml` that uses `mom6-solo` from the `access-om3/2026.05.004` module;
4. runs `payu run`. Output appears in
   `/scratch/<your-project>/$USER/mom6-examples/archive/<example>/output000/`.

Examples that switch restart files off (`RESTART_CONTROL = -1`) also get a small payu
`run` userscript, because payu 1.3.6 otherwise fails while archiving them (explained on
those pages). *Variants* (names with a suffix, e.g. `double_gyre-10yr`) are copies of the
example with a few extra lines in `MOM_override`, such as a longer run.

### ANU-TUB

[`anu-tub.sh`](anu-tub.md#run-it-yourself) clones
[anu-tub](https://github.com/ACCESS-Community-Hub/anu-tub) at the tested commit, makes its
three input files by running the repository's own notebook
`input/mom6-anu-tub-driver.ipynb` as a script (with `conda/analysis3` from `xp65`), picks the
vertical coordinate (`zstar`, `adapt` or `hycom1`), edits `config.yaml` (project, released
module, walltime) and runs `payu run`. It also turns off payu's executable check
(`manifest: reproduce: exe`), because the repository's manifest records an older,
pre-release executable. We tested the `zstar` coordinate for 1 month.

### ISOMIP+ Ocean0

[`isomip-plus-ocean0.sh`](isomip-plus.md#run-it-yourself) clones the configuration (branch
`isomip-plus-ocean0-sigmashelfzstar` of this repository) and its input file
([claireyung/isomip-test-mom6-for-iom3-configs](https://github.com/claireyung/isomip-test-mom6-for-iom3-configs))
at the tested commits, writes a payu `config.yaml` that uses the ACCESS-OM3 module on the
`normalsr` queue, and runs `payu run` (3 months).

### ACCESS-OM3 single column

[`om3-mom6-single-column.sh`](om3-mom6-single-column.md#run-it-yourself) clones
[om3-mom6-single-column](https://github.com/ACCESS-Community-Hub/om3-mom6-single-column) at the
tested commit and edits its `config.yaml`: the current ACCESS-OM3 module, payu's executable check
off (the repository's manifest records `access-om3/2026.03.000`), and your project and laboratory.
It then runs `payu run` for one model year with the coupled `access-om3-MOM6` executable.

## How each run was checked

**What "ran" means:** the job finished, the energy file (`ocean.stats`) has more than two
lines and contains no `NaN`.

**Parameters:** we compare every run's `MOM_parameter_doc.all` with a reference: for the
MOM6 examples, the one GFDL committed for that example; for ANU-TUB, the one committed in
the anu-tub repository; for ISOMIP+, Claire Yung's own run; for the ACCESS-OM3 single column, the
one committed in om3-mom6-single-column. The differences (renamed, new
or removed parameters, changed defaults) are listed on each page, because they show where
the ACCESS-OM3 MOM6 version behaves differently from the one the configuration was
written for. We did **not** compare answers bit-for-bit.

**Domain, forcing and output:** each successful run's page shows the output of the notebook
[`notebooks/explore_run.ipynb`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/notebooks/explore_run.ipynb),
run on that run's output folder. It plots only files MOM6 wrote during the run: the bottom
depth, the initial state, any surface forcing saved in the diagnostics, the energy and CFL
number through the run, and the final state.

## The pipeline

The scripts live in [`tested-configs/`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/tree/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs). The links below are to the versions that wrote these pages (commit `31427534`); the runs themselves were started with the scripts at commit `0bf2ffcf`.

| File | Purpose |
|---|---|
| [`versions.env`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/versions.env) | pinned versions: MOM6-examples commit, ACCESS-OM3 module, payu module, data path |
| [`examples.txt`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/examples.txt) | which MOM6 examples to run, with how many cores and what walltime |
| [`templates/run_example.sh.in`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/templates/run_example.sh.in) | the commented run script that every MOM6-example page embeds |
| [`lib/make_run_scripts.sh`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/lib/make_run_scripts.sh) | writes `run_scripts/<example>.sh` from that template |
| [`run_scripts/anu-tub.sh`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/run_scripts/anu-tub.sh), [`run_scripts/isomip-plus-ocean0.sh`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/run_scripts/isomip-plus-ocean0.sh), [`run_scripts/om3-mom6-single-column.sh`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/run_scripts/om3-mom6-single-column.sh) | the hand-written scripts for the COSIMA community configurations |
| [`regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/regenerate_all.sh) | does everything: write scripts, run, wait, summarise, run the notebooks, write pages |
| [`lib/record_environment.sh`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/lib/record_environment.sh) | records the executable, its md5, the MOM6 source, payu version and the date |
| [`lib/summarise_run.py`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/lib/summarise_run.py) | checks a run (`ocean.stats`), reads payu manifests (md5 hashes) and the run's parameters |
| [`lib/run_notebooks.sh`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/lib/run_notebooks.sh) | runs [`notebooks/explore_run.ipynb`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/notebooks/explore_run.ipynb) on each successful run (papermill) |
| [`lib/run_in_pbs.pbs`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/lib/run_in_pbs.pbs) | runs a command in a PBS job (used for the notebooks) |
| [`lib/param_diff.py`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/lib/param_diff.py) | the "Parameters compared with the reference" tables |
| [`lib/make_pages.py`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/lib/make_pages.py) | writes these pages from `results/*/summary.json` |
| [`build/build_mom6_solo.sh`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/build/build_mom6_solo.sh), [`build/compare_with_release.sh`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/tested-configs/build/compare_with_release.sh) | build your own `mom6-solo` and check it matches the release |

To re-test everything with a new ACCESS-OM3 release, edit `versions.env` and run
`PROJECT=<proj> ./regenerate_all.sh` from a login node.

For these tests the scripts ran with `EXAMPLES_DIR`, `LAB`, `TUB_DIR` and `WORK_DIR` set
to a test area (`/g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs`) instead of their defaults under
`/g/data/<project>/$USER` and `/scratch/<project>/$USER`. Apart from these paths, the
scripts ran exactly as shown.

### About the input data

`/g/data/ol01/access-iom3-configs/mom6exampledata/` holds GFDL's MOM6-examples data
tarballs (downloaded with
[`scripts/grab_mom6examples_data.sh`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/31427534453fb2304744b9a19fb0b54a15b13de9/scripts/grab_mom6examples_data.sh)),
and its `backup/` sub-directory holds them **unpacked**. The examples' `INPUT/` links expect
the unpacked layout (e.g. `.datasets/global/siena_201204/INPUT/...`), so `.datasets`
must point at `.../mom6exampledata/backup`, not at the directory of tarballs. The run
scripts do this for you.

## Learning more

- The MOM6-examples wiki: [Getting started](https://github.com/NOAA-GFDL/MOM6-examples/wiki/Getting-started)
  and the [FAQ](https://github.com/NOAA-GFDL/MOM6-examples/wiki/FAQ).
- The [2022 AOS MOM6 tutorial](https://github.com/NOAA-GFDL/MOM6-examples/wiki/Tutorials):
  "Running and controlling MOM6", "Analyzing MOM6 output" and "Create your own experiment"
  are good next steps after running an example here.
- [MOM6 documentation](https://mom6.readthedocs.io): what the run-time parameters in
  `MOM_input`/`MOM_override` mean. Each run also writes `MOM_parameter_doc.all`,
  which lists every parameter with its documentation.
