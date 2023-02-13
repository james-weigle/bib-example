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

with open("./_pages/success.md", "w") as file:
    file.write("""---
layout: page
title: Success
---

Success! Now with a bonus!
                """)
