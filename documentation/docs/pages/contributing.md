# Contributing

## Report a bug or make a suggestion

Technical issues related to access-idealised are best posted to the repository's [issues](https://github.com/ACCESS-Community-Hub/access-idealised-configs/issues). If you would like to discuss the issue first, feel free to post it on the [access hive forum](https://forum.access-hive.org.au/c/cosima/29).

## Add a new configuration

There are several different ways to do this depending on the kind of contribution. Best to get in touch on the [access hive forum](https://forum.access-hive.org.au/c/cosima/29), ping `ACCESS-NRI/ocean` on GitHub or email `chris.bull@anu.edu.au`.

## access-idealised documentation

We appreciate contributions, typo and bug fixes to this documentation. To make suggestions please see steps below.

### Quick contributions 
!!! tip
    This method has the advantage that it's *very quick* (<1 minute!). The caveat is that, unless you have write access to the `access-idealised-configs` repository, you will not be able to preview the changes rendered into a website or create whole new pages. <br>

The simplest and fastest way to make a change to an _existing_ page is to click the edit "pencil" on the top-right corner. This will go to the relevant GitHub markdown file and clicking the _top-right pencil again_ on GitHub will allow you to edit the file. Once complete, click `Commit changes...`. There are then _two_ possibilities, depending on whether you have write access to [`access-idealised-configs`](https://github.com/ACCESS-Community-Hub/access-idealised-configs): 

1.  **No write access**: this will prompt you to make a fork and then a pull request (less than 1 minute!). 
1.  **You have write access**: please commit changes on a new branch and then use a pull request (this relates to the next option). 

### Larger contributions (online PR-previews)
!!! tip
    This method allows you to create whole new pages, and to preview the changes rendered into a website. It does not require you to install any software, but is **only available for people with write access to [`access-idealised-configs`](https://github.com/ACCESS-Community-Hub/access-idealised-configs)**.<br>

Create a new branch, e.g. `jblogs/doc-update`, make doc changes (the documentation sources are in [`documentation/`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/tree/main/documentation)), then open a related PR and a GitHub preview will be made automatically.

### Larger contributions (`mkdocs` offline)
!!! tip
    Similar to the above, this method allows you to create whole new pages and to preview the changes rendered into a website. It works whether or not you have write access to [`access-idealised-configs`](https://github.com/ACCESS-Community-Hub/access-idealised-configs), but requires you to install `mkdocs` and takes the longest to set up.<br>

Follow [these instructions](https://docs.access-hive.org.au/about/contribute/#lets-get-started), but fork and clone [`access-idealised-configs`](https://github.com/ACCESS-Community-Hub/access-idealised-configs) rather than the ACCESS-Hive Docs repository. Once cloned, install the requirements (`pip install -r documentation/requirements.txt`) and run `python -m mkdocs serve` from within the `documentation` directory. (Plain `mkdocs serve` fails with `No such file or directory: 'gh'`, because one of the requirements replaces the `mkdocs` command with one that needs the GitHub CLI.)

If you want to add a new page, then you need to add another markdown file in the folder (or sub-folder as appropriate):
[`documentation/docs/pages/`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/tree/main/documentation/docs/pages)

Once done, update the documentation navigation in [`documentation/mkdocs.yml`](https://github.com/ACCESS-Community-Hub/access-idealised-configs/blob/main/documentation/mkdocs.yml) by adding an entry under the `nav:` section. Note you'll need to add the sub-folder paths as appropriate.
