
Welcome to the documentation for the [mom6-idealised ocean model configurations](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs)! 

The purpose of this repository is to encourage community users to both use and share _idealised_ ocean model configurations.

!!! tip "Tested configurations, one script each"
    You don't need to compile MOM6 to run these configurations: the ACCESS-OM3 release
    (`module load access-om3/2026.05.004`) ships the ocean-only executable `mom6-solo`.
    Each [configuration page](configurations/Overview.md) has one script that sets the
    case up and runs it with payu on Gadi, and shows what that script produced. This
    includes [ANU-TUB](configurations/anu-tub.md), [ISOMIP+ Ocean0](configurations/isomip-plus.md)
    and [GFDL's MOM6 examples](configurations/mom6examples.md).

    These scripts and results were made with [Claude Code](https://claude.com/claude-code)
    and are regenerated with `tested-configs/regenerate_all.sh`. Every page states the
    exact versions, input hashes and environment used.

## Getting involved in mom6-idealised

**Contributions from people of all career stages and backgrounds are highly encouraged.** All these models and configurations are open source. Development is led by ACCESS-NRI and the [COSIMA working group](https://cosima.org.au/) where we follow an open development model building on the work of international modelling consortia.

Contributors so far include: Christopher Bull (ACCESS-NRI), Claire Yung (Australian National University), Josef Bisits (University of New South Wales), Andy Hogg (Australian National University).

### Report a bug or make a suggestion

Technical issues related to mom6-idealised are best posted to [github.com/ACCESS-Community-Hub/mom6-idealised-configs/issues](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/issues). If you would like to discuss the issue first, feel free to post it on the [access hive forum](https://forum.access-hive.org.au/c/cosima/29).

### Add a new configuration

There are several different ways to do this depending on the kind of contribution. Best to get in touch on the [access hive forum](https://forum.access-hive.org.au/c/cosima/29), ping `ACCESS-NRI/ocean` on GitHub or email `chris.bull@anu.edu.au`.

### mom6-idealised documentation

We appreciate contributions, typo and bugs fixes to this documentation. To make suggestions please see steps below.

#### Quick contributions 
!!! tip
    This method has the advantage is that it's *very quick* (<1 minute!). The caveat is that, unless you have write access to the `mom6-idealised-configs` repository, you will not be able to preview the changes rendered into a website or create whole new pages. <br>

The simplest and fastest way to make a change to an _existing_ page is to click the edit "pencil" on the top-right corner. This will go to the relevant GitHub markdown file and clicking the _top-right pencil again_ on GitHub will allow you to edit the file. Once complete, click `Commit changes...`. There are then _two_ possibilities, depending on whether you have  write access to [`mom6-idealised-configs`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs): 

1.  **No write access**: this will prompt you to make a fork and then a pull request (less than 1 minute!). 
1.  **You have write access**: please commit changes on a new branch and then use a pull request (this relates to the next option). 

#### Larger contributions (online PR-previews)
!!! tip
    This method allows you create whole new pages, and to preview the changes rendered into a website. It does not require you to install any software, but is **only available for people with write access to [`mom6-idealised-configs`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs)**.<br>

Create a new branch, e.g. `jblogs/doc-update`, make doc changes (the documentation sources are in [github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/documentation](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/documentation)), then open a related PR and a GitHub preview will be made automatically.

#### Larger contributions (`mkdocs` offline)
!!! tip
    Similar to the above, this method allows you create whole new pages and to preview the changes rendered into a website. It works whether or not you have write access to [`mom6-idealised-configs`](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs), but requires you to install `mkdocs` and takes the longest to set up.<br>

Fork and clone [github.com/ACCESS-Community-Hub/mom6-idealised-configs](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs), install the requirements and serve the site from the `documentation` directory:

```bash
git clone git@github.com:<your-username>/mom6-idealised-configs.git
cd mom6-idealised-configs/documentation
python -m venv ~/venv-docs && ~/venv-docs/bin/pip install -r requirements.txt
~/venv-docs/bin/python -m mkdocs serve      # then open http://127.0.0.1:8000
```

!!! tip
    Use `python -m mkdocs` rather than plain `mkdocs`: one of the requirements
    (`mkdocs_include_configuration_stubs_plugin`) installs its own `mkdocs` command, which
    needs the GitHub CLI `gh` and fails with `No such file or directory: 'gh'` without it.

The general ACCESS-Hive [contribution guide](https://docs.access-hive.org.au/about/contribute/) has more on writing documentation.


If you want to add a new page, then you need to add another markdown file in the folder (or sub-folder as appropriate):
[github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/documentation/docs/pages](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/tree/main/documentation/docs/pages)

Once done, update the documentation navigation in [github.com/ACCESS-Community-Hub/mom6-idealised-configs/blob/main/documentation/mkdocs.yml](https://github.com/ACCESS-Community-Hub/mom6-idealised-configs/blob/main/documentation/mkdocs.yml) by adding an entry under the `nav:` section. Note you'll need to add the sub-folder paths as appropriate.


