# Change the URL segment for pages in MkDocs to hide the "/pages" prefix, so that pages inside the
# "pages" directory are served directly at the root URL.
#
# This runs in on_files, before any page is rendered, so that links between pages
# (including links to pages later in the nav) resolve to the new URLs. It used to run in
# on_page_markdown, which renamed each page only when it was rendered, leaving links to
# later pages pointing at ".../pages/..." (fixed with Claude Code, 2026-11-04).
import os

from mkdocs.plugins import event_priority


@event_priority(-100)
def on_files(files, *, config):
    for file in files:
        if file.url.startswith("pages/"):
            file.url = file.url.removeprefix("pages/")
            file.dest_uri = file.dest_uri.removeprefix("pages/")
            file.abs_dest_path = os.path.normpath(os.path.join(config["site_dir"], file.dest_uri))
    return files
