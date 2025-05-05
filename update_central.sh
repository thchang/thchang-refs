rm bibmgr_db.yaml
bibmgr clear --force
for file in old_bibs/*.bib; do
    bibmgr load -f $file -m --force
done
bibmgr save --force
