# Configurations

This site collects MOM6 ocean-only configurations from two communities:

- **The Australian community:** configurations set up by members of the Australian MOM6
  community and kept on GitHub under
  [ACCESS-Community-Hub](https://github.com/ACCESS-Community-Hub).
- **The global MOM6 community:** the test cases in
  [NOAA-GFDL/MOM6-examples](https://github.com/NOAA-GFDL/MOM6-examples). MOM6 is developed by
  the [MOM6 Consortium](https://mom6.readthedocs.io/en/main/api/generated/pages/Testing.html#consortium-testing),
  of which [ACCESS-NRI is a node](https://access-om3-configs.access-hive.org.au/latest/infrastructure/MOM6-node-PR-testing/).

Every configuration below was run on NCI Gadi with the `mom6-solo` executable from the
ACCESS-OM3 release `access-om3/2026.05.004`, using one script per configuration (on its page).
Every configuration needs membership of the NCI project `vk83`; the Prerequisites column
lists anything else.

## Australian community

--8<-- "tested-configs/results/table-community.md"

## MOM6 examples

Press a tag to show only those examples; press it again to show all.
How these runs were made, and how to run one yourself, is on
[MOM6 examples: how they were run](mom6examples.md).

--8<-- "tested-configs/results/table-mom6examples.md"

&dagger; = GFDL excludes this example from its own automated test suite (`EXCLUDE` in
`ocean_only/Makefile`). Cores = the processor layout GFDL used for that example
(`NIPROC x NJPROC` in its `MOM_parameter_doc.layout`). Each run uses the example's own run
length, usually a few days: these check that the model runs; they are not science-ready
simulations. Names with a suffix (e.g. `double_gyre-10yr`) are *variants*: copies of the
example with a few extra lines in `MOM_override`, such as a longer run.

The Description column is read from each run's own `MOM_parameter_doc.all`
(grid size `NIGLOBAL x NJGLOBAL x NK`, `GRID_CONFIG`, vertical coordinate, `TOPO_CONFIG`,
`WIND_CONFIG`, `BUOY_CONFIG`, run length), with links to the example's directory and README upstream.

!!! note "Tested with Claude Code"
    The run scripts, test results and most of the text on this page were produced with
    [Claude Code](https://claude.com/claude-code) via the scripts in
    [`tested-configs/`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs).
    Every page states exactly which versions were used.
