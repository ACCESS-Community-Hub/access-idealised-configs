!!! danger "Community-driven: not officially supported by ACCESS-NRI"
    This website and the workflow behind it are **not officially supported by ACCESS-NRI**. To report a problem or help improve them, see
    [Contributing](contributing.md).

--8<-- "tested-configs/templates/claude_caveat.md"

Welcome to the documentation for the [mom6-idealised ocean model configurations](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs)! 

This website aims to make idealised MOM6 configurations easier to run, and to make what is
available easy to browse and discover: for each configuration you can see how it is set up, its
surface forcing (where the run saved it) and its output, before running it yourself.

It collects _idealised_ ocean model configurations for MOM6, from the [COSIMA community](configurations/Overview.md#cosima-community-configurations)
and from [GFDL's MOM6 examples](configurations/Overview.md#global-mom6-community-configurations), so that the community can run, check and share them. Each one comes
with a tested script that runs it on NCI Gadi with the prebuilt `mom6-solo` from ACCESS-OM3, so
[you don't need to compile MOM6](#quick-start). If you do want to build your own `mom6-solo`
(for example, to change the MOM6 code), [Building MOM6](infrastructure/Building.md) shows how
with ACCESS-NRI's Spack. The website has:

- **Configurations**
    - [Overview](configurations/Overview.md): every configuration with whether it ran, its
      prerequisites and links to its page.
    - [How this website is generated](configurations/how-they-were-run.md): the versions, scripts and
      checks used for every run.
    - One page per configuration: the COSIMA community configurations (ANU-TUB,
      ISOMIP+ Ocean0) and the MOM6 examples, each with its run script and results.
- **Infrastructure**
    - [Building MOM6](infrastructure/Building.md): you don't need to build MOM6 to run these
      configurations; this page shows how to build your own `mom6-solo` with ACCESS-NRI's Spack.
- **[Contributing](contributing.md)**: report a bug, add a configuration or improve these pages.

## How this website is generated (mostly by Claude Code)

This website documents itself. Every configuration page, run script, status table and figure is
produced by the same scripts in
[`tested-configs/`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/tested-configs),
written mostly by Claude Code, and is regenerated each time the configurations are re-tested.
Every configuration, both the COSIMA community ones and the MOM6 examples, was run in the same way:

- on NCI Gadi, with the prebuilt MOM6 ocean-only executable `mom6-solo` from the ACCESS-OM3
  release ([`access-om3/2026.05.004`](https://github.com/ACCESS-NRI/ACCESS-OM3/releases)), so
  nobody has to compile MOM6;
- with [payu](https://payu.readthedocs.io), from one script per configuration, shown in full on
  that configuration's page;
- then checked, summarised and written up by the same scripts.

--8<-- "tested-configs/results/status-summary.md"
The status of every run is in the tables on the [Overview](configurations/Overview.md).
Details: [How this website is generated](configurations/how-they-were-run.md).

## Quick start

You don't need to compile MOM6: the ACCESS-OM3 release (`module load access-om3/2026.05.004`)
ships the ocean-only executable `mom6-solo`. Every configuration on the
[Overview](configurations/Overview.md) has one script that sets it up and runs it with
[payu](https://payu.readthedocs.io) on NCI Gadi.

1. Make sure you are a member of the NCI project **`vk83`**
   ([join vk83](https://my.nci.org.au/mancini/project/vk83/join)) and of a project to charge
   the run to. Some configurations need other projects too (the Prerequisites column on the
   [Overview](configurations/Overview.md)).
2. Open a configuration's page, for example [double_gyre](configurations/mom6examples/double_gyre.md),
   and copy its script (copy button at the top right of the code block).
3. From a Gadi **login node**, run it:

    ```bash
    PROJECT=<your-project> bash double_gyre.sh
    ```

    Output appears under `/scratch/<your-project>/$USER/` (each page says exactly where).

## Getting involved in mom6-idealised

**Contributions from people of all career stages and backgrounds are highly encouraged.** All these models and configurations are open source. Development is led by ACCESS-NRI and the [COSIMA working group](https://cosima.org.au/) where we follow an open development model building on the work of international modelling consortia.

Contributors so far include: Christopher Bull (ACCESS-NRI), Claire Yung (Australian National University), Josef Bisits (University of New South Wales), Andy Hogg (Australian National University).

To report a bug, suggest a change, add a configuration or improve this documentation, see
[Contributing](contributing.md).
