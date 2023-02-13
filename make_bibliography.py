#!/usr/bin/python3
"""
Goal: make a page _pages/success.md
with the following content:

---
layout: page
title: Success
---

Success!
"""

with open("./_pages/publications.md", "w") as file:
    file.write("""---
layout: page
title: Publications
---

# Publications

Some content

                """)
