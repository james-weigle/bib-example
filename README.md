# Bib Example

Since GitHub Pages doesn’t want us to execute arbitrary code,
my workaround is to use a commit hook to
- run a script locally (`make_bibliography.py`) which updates `_pages/publications.md`, then 
- add `_pages/publications.md` to the commit.

## Setup

Run `init.sh` from the root directory first,
which just creates a (local) hook
that runs `make_bibliography.py`.
