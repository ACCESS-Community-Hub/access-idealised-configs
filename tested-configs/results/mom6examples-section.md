## MOM6 examples (NOAA-GFDL)

The [NOAA-GFDL/MOM6-examples](https://github.com/NOAA-GFDL/MOM6-examples) repository holds
GFDL's MOM6 test cases, from idealised ones that need no input data (double gyre,
seamount, lock exchange, ...) to realistic global ones.
This section shows which of the ocean-only (`ocean_only/`) cases run on NCI Gadi with the
**prebuilt MOM6 ocean-only executable `mom6-solo` from the ACCESS-OM3 release**, so
you don't have to compile MOM6 yourself.

**49 of 57 tested runs completed successfully** (tested on 2026-11-04).

!!! note "Generated with Claude Code"
    Everything in this section was run, checked and written up automatically by
    [`tested-configs/regenerate_all.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs),
    a set of scripts written with [Claude Code](https://claude.com/claude-code) and
    reviewed by humans. Each page shows the exact script that produced it, plus the
    versions, input-file hashes and run-time environment that were used.
    Spotted something wrong? Please [raise an issue](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/issues).

### Quick start: MOM6 examples

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

You need to be a member of the NCI project **`vk83`** (ACCESS-NRI software:
[join vk83](https://my.nci.org.au/mancini/project/vk83/join)). The examples that read GFDL's
input data (marked on their pages) also need read access to `/g/data/ol01`, where an
unpacked copy of the [MOM6-examples data](https://github.com/NOAA-GFDL/MOM6-examples/wiki/Getting-started#installing-data-sets-on-another-platform)
is kept.

!!! warning "Run from a login node, not from ARE/JupyterLab"
    `payu` runs inside its own container and **cannot be started from inside another
    container**, such as an ARE JupyterLab terminal with `conda/analysis3` loaded. There it
    hangs (the launcher keeps re-executing itself) or fails with
    `starter-suid doesn't have setuid bit set`. Use an ordinary `ssh gadi` login shell, or
    submit the script as a small PBS job (see
    [`lib/run_in_pbs.pbs`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/blob/main/tested-configs/lib/run_in_pbs.pbs)).

### Results: MOM6 examples

Every example is listed in the [table of all configurations](#all-configurations) at the
top of this page, with whether it ran; press **GFDL** there to show only these examples.

In that table, &dagger; = GFDL excludes this example from its own automated test suite (`EXCLUDE` in
`ocean_only/Makefile`), usually because it needs extra input files or runs for a long time.

Cores = processor layout GFDL used for that example (`NIPROC x NJPROC` in its
`MOM_parameter_doc.layout`). Runs use the example's own run length, which is usually a
few days: these are tests that the model runs, not science-ready simulations.
Pages with a suffix (e.g. `double_gyre-10yr`) are *variants*: copies of the example with
a few extra lines in `MOM_override`, such as a longer run, to show a spun-up state.

### How these pages were made

| What | Version used |
|---|---|
| MOM6-examples | [`c1730b8e`](https://github.com/NOAA-GFDL/MOM6-examples/commit/c1730b8efe16cf7f12fc8db588115cae50f3e802) (branch `dev/gfdl`) |
| ACCESS-OM3 release | [`access-om3/2026.05.004`](https://github.com/ACCESS-NRI/ACCESS-OM3/releases) |
| MOM6 component module | `access-mom6/2026.05.003-ld7hklz` |
| MOM6 source code | `ACCESS-NRI/MOM6 2026.05.003 d11a149ccba676d524312328f7eb62560a156dc3` ([ACCESS-NRI/MOM6](https://github.com/ACCESS-NRI/MOM6)) |
| Executable | `/g/data/vk83/apps/spack/1.1/release/linux-x86_64_v4/access-mom6-2026.05.003-ld7hklzo5ajizx5u4yl74i4ijberrpv6/bin/mom6-solo` |
| Executable md5 | `4785d157c76c30d8d01baf7d0f69d218` |
| payu | `payu 1.3.6_1` |
| Scripts (this repository) | commit `0bf2ffcfef6199dd6461cbbc64d2bdaf06f3d671` |

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

For these tests the scripts ran with `EXAMPLES_DIR`, `LAB`, `TUB_DIR` and `WORK_DIR` set
to a test area (`/g/data/tm70/cyb561/repos/claude/mom6-idealised-configs/runs`) instead of their defaults under
`/g/data/<project>/$USER` and `/scratch/<project>/$USER`. Apart from these paths, the
scripts ran exactly as shown.

**What "ran" means:** the job finished, `ocean.stats` has more than two lines and contains
no `NaN`. We also compare every run's `MOM_parameter_doc.all` with the one GFDL
committed for that example. The differences (renamed, new or removed parameters,
changed defaults) are listed on each page, because they show where the ACCESS-OM3 MOM6
version behaves differently from the GFDL version the example was written for. We did
**not** compare answers bit-for-bit with GFDL.

#### About the input data

`/g/data/ol01/access-iom3-configs/mom6exampledata/` holds GFDL's MOM6-examples data
tarballs (downloaded with
[`scripts/grab_mom6examples_data.sh`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/blob/main/scripts/grab_mom6examples_data.sh)),
and its `backup/` sub-directory holds them **unpacked**. The examples' `INPUT/` links expect
the unpacked layout (e.g. `.datasets/global/siena_201204/INPUT/...`), so `.datasets`
must point at `.../mom6exampledata/backup`, not at the directory of tarballs. The run
scripts do this for you.

### Learning more

- The MOM6-examples wiki: [Getting started](https://github.com/NOAA-GFDL/MOM6-examples/wiki/Getting-started)
  and the [FAQ](https://github.com/NOAA-GFDL/MOM6-examples/wiki/FAQ).
- The [2022 AOS MOM6 tutorial](https://github.com/NOAA-GFDL/MOM6-examples/wiki/Tutorials):
  "Running and controlling MOM6", "Analyzing MOM6 output" and "Create your own experiment"
  are good next steps after running an example here.
- [MOM6 documentation](https://mom6.readthedocs.io): what the run-time parameters in
  `MOM_input`/`MOM_override` mean. Each run also writes `MOM_parameter_doc.all`,
  which lists every parameter with its documentation.
