#!/bin/bash

python3 -m bibmgr clear --force
for file in old_bibs/*.bib; do
    python3 -m bibmgr load -f $file -m --force
done
python3 -m bibmgr load -f bibmgr_db.yaml -m --force
rm -f bibmgr_db.yaml
python3 -m bibmgr save --force

cat workflow/readme_head > README.md
python3 workflow/make_readme.py AI SciML optimization HPC software \
        "computational geometry" "design of experiments" "quantum computing" >> README.md
