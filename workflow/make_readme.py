#!/usr/bin/python

import sys

from bibmgr.database_manager import DatabaseManager

db_mgr = DatabaseManager()
db_mgr.read_yaml("bibmgr_db.yaml")

print("List of topics (may be some overlap between topics):\n")
for topic in sys.argv[1:]:
    print(f" * [{topic}](#{topic.strip().replace(' ', '-')})")

for topic in sys.argv[1:]:
    print(f"\n## {topic}\n")
    for entry in db_mgr.entries(predicate=lambda x: topic in x.get_tags()):
        print(" * ", end="")
        if (
            entry.get_doi() is not None or
            entry.get_url() is not None or
            entry.get_git() is not None
        ):
            print(f"[", end="")
        if len(entry.get_authors()) == 1:
            print(f"{entry.get_authors()[0][-1].replace('~', ' ')}, ", end="")
        elif len(entry.get_authors()) > 1:
            print(
                f"{entry.get_authors()[0][-1].replace('~', ' ')} et al., ",
                end=""
            )
        print(f"{entry.get_year()}. ", end="")
        print(entry.get_title().replace('{', '').replace('}', ''), end="")
        if entry.get_url() is not None:
            print(f"]({entry.get_url()})")
        elif entry.get_doi() is not None:
            print(f"](https://doi.com/{entry.get_doi()})")
        elif entry.get_git() is not None:
            print(f"]({entry.get_git()})")
        else:
            print()
