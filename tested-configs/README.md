# tested-configs

Scripts that **run** the configurations documented on
<https://mom6-idealised-configs.readthedocs.io> on NCI Gadi, check that they worked, and
regenerate the website pages from the results. Written with
[Claude Code](https://claude.com/claude-code); please review like any other code.

## Quick start

```bash
# from a Gadi login node, in this directory
PROJECT=<proj> ./regenerate_all.sh                 # everything (about an hour, mostly queueing)
PROJECT=<proj> ONLY="double_gyre anu-tub-zstar" ./regenerate_all.sh   # just some runs
PROJECT=<proj> ./regenerate_all.sh summarise pages # only redo the summaries + pages
```

To test a new ACCESS-OM3 release, edit `versions.env` and re-run. Old payu archives are
moved aside (`<name>.old-<date>`), never deleted.

## Layout

| Path | What |
|---|---|
| `versions.env` | pinned versions (MOM6-examples commit, ACCESS-OM3 + payu modules, data path) |
| `examples.txt` | MOM6-examples cases to run: directory, cores, walltime, optional variant |
| `descriptions.yaml` | one-line descriptions shown on the website |
| `plots.yaml` | optional per-run choice of figure panels |
| `templates/run_example.sh.in` | template for the user-facing run script of each MOM6 example |
| `templates/variant_block.sh.in` | extra block for variants (copy example + extra `MOM_override` lines) |
| `templates/mom6examples_index.md.in` | the MOM6 examples overview page |
| `run_scripts/` | the generated (and the two hand-written) run scripts; embedded on the website |
| `build/build_mom6_solo.sh` | builds your own `mom6-solo` with Spack (Building page) |
| `regenerate_all.sh` | the master script: `scripts` -> `run` -> `wait` -> `summarise` -> `pages` |
| `lib/make_run_scripts.sh` | renders `run_scripts/<name>.sh` from the template |
| `lib/run_in_pbs.pbs` | runs a command in a plain PBS job (payu can't start inside a container) |
| `lib/summarise_run.py` | checks one run, collects provenance (payu manifests, env, PBS usage), makes the figure |
| `lib/record_environment.sh` | records module versions, executable md5, MOM6 commit |
| `lib/make_pages.py` | writes the website pages from `results/` |
| `results/<name>/` | generated: `summary.json`, `figure.png`, `ocean.stats` (+ `tested.md` fragments) |

## What "ran successfully" means

`ocean.stats` exists, has more than two lines, and contains no `NaN`. Each page also
lists how the run's `MOM_parameter_doc.all` differs from the reference one (GFDL's for
MOM6-examples). Answers are **not** compared bit-for-bit.
