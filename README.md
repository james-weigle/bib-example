# Bib Example

This is an example of a GitHub Pages site that
generates a bibliography automatically
without using the jekyll-scholar plugin (which is supported by
jekyll, but not by GitHub Pages).

My workaround is to use a commit hook to
- run a script locally (`make_bibliography.py`) which updates `_pages/publications.md`, then 
- add `_pages/publications.md` to the commit.

What this comes to is
that **you don’t have to worry about the publications list**:
you don’t have to edit that page,
and you don’t have to add/commit that page.
**All you should have to change are the BibTeX files**.

## Organizing the bibliography

Under `bibliography/`,
I’ve saved a file `journal.bib`.
These appear under the heading "Journal"
on the Publications page,
in the order in which they appear in the `.bib` file.

Not implemented yet:
- functions for properly citing resources besides journal articles
  (books, films, etc.).
- capability of specifying the resource types and files
  in `_config.yml`.

## Setup

Run `init.sh` from the root directory first,
which just creates a (local) hook
that runs `make_bibliography.py`.
**This hook doesn’t get committed**:
just leave it on your local machine.

If you’re reusing this code, you probably have your
own needs and preferences. Therefore,
it might be best to scrap _my_ implementation of
`make_bibliography.py`
(either by replacing it with a fresh python script,
or by changing `githooks/pre-commit` to do something else entirely---perhaps
using `bib2html` or `pandoc`).
