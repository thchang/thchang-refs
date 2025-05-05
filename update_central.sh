#!/bin/bash

bibmgr clear --force
for file in old_bibs/*.bib; do
    bibmgr load -f $file -m --force
done
bibmgr load -f bibmgr_db.yaml -m --force
rm bibmgr_db.yaml
bibmgr save --force

cat workflow/readme_head > README.md
python3 workflow/make_readme.py AI SciML optimization HPC software \
        "computational geometry" "design of experiments" "quantum computing" >> README.md
