#!/usr/bin/python3
"""
Goal: print a list of bibliography entries.
"""
import pybtex.database
from inspect import getmembers

bibliography = { "Journal": "bibliography/journal.bib" }

def format_author(entry):
    """Returns a string in markdown format for an article citation."""
    def first_initials(author):
        first_names = list(iter(author.first_names))
        middle_names = list(iter(author.middle_names))
        return "".join(n[0] for n in first_names + middle_names)
    def last_name(author):
        return " ".join(author.last_names)
    authors = list(iter(entry.persons['author']))
    if len(authors) >= 4:
        a = authors[0]
        author_string = f"{last_name(a)} {first_initials(a)} et al. "
    else:
        author_string = ", ".join(f"{last_name(a)} {first_initials(a)}" for a in authors) + ". "
    return author_string

def format_title(entry):
    """Return a string in markdown format
    with the title in quotes, linking to the URL."""
    if 'url' in entry.fields:
        return f"[{entry.fields['title']}]({entry.fields['url']}). "
    return entry.fields['title']

def format_publication(entry):
    """Return a string in markdown format with
    journal date;volume(issue):pages"""
    journal = entry.fields['journal']
    year = entry.fields['year']
    if 'volume' in entry.fields:
        vol = f"{entry.fields['volume']}"
    else:
        vol = ""
    if 'issue' in entry.fields:
        iss = f"({entry.fields['issue']})"
    else:
        iss = ""
    voliss = "".join([vol,iss])
    return " ".join([journal, year, voliss])

# "Title": "path/to/file.bib"



def make_download_link(title, content):
    """Return an HTML expression for a link that downloads a text file
    with title `title` and content `content`."""
    return ('<a download="{{title}}" href="data:application/txt,{{content}}">BibTeX entry</a>'.replace("{{title}}", title)).replace("{{content}}", content)

def format_bibtex_entry(index, entry):
    """Return a formatted bibtex entry as a downlod link."""
    string = entry.to_string('bibtex')
    string = (string.replace('"', "'")).replace('\n', '')
    filename = next(iter(entry.persons['author'])).last_names[0] + "_" + entry.fields['year'] + "_" + f"{index}" + ".bib"
    return make_download_link(filename, string)


with open("./_pages/publications.md", "w") as file:
    file.write("""---
layout: page
title: Publications
permalink: /publications
---
""")

    for title, filepath in bibliography.items():
        file.write(f"## {title}\n")
        file.write("\n|--|--|--|\n")
        bib_data = pybtex.database.parse_file(filepath)
        entries = reversed(list(enumerate(reversed(list(bib_data.entries.items())),start=1)))
        for i, (key, entry) in entries:
            refstring = "".join([format_author(entry),
                                 format_title(entry),
                                 format_publication(entry)])
            if 'pages' in entry.fields:
                refstring += ", "+entry.fields['pages'] + "."
            link = format_bibtex_entry(i, entry)
            file.write(f"| {i} | {refstring} | {link} |\n")

# authors. [Title](google drive link). Journal volume (issue), pp. pages, year

# with open("./_pages/publications.md", "w") as file:
#     file.write("""---
# layout: page
# title: Publications
# ---
# 
# # Publications
# 
# Some content
# 
#                 """)
