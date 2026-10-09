#!/bin/sh
# Cómo se consiguieron los datos que leen sandy.py y figura.py (2/10/2026).
# No baja el repositorio entero: solo los archivos que hacen falta.
set -e
git clone --filter=blob:none --no-checkout https://github.com/matplotlib/basemap.git basemap_hist
mkdir -p gshhs ne
cd basemap_hist
# v1.0.7rel (17/8/2013): datos de GSHHS 2.2.0, commit 8442448 del 7/3/2012
for r in l i f; do
  git show v1.0.7rel:lib/mpl_toolkits/basemap/data/gshhs_$r.dat     > ../gshhs/old_$r.dat
  git show v1.0.7rel:lib/mpl_toolkits/basemap/data/gshhsmeta_$r.dat > ../gshhs/oldmeta_$r.dat
done
# v2.0.0 (13/6/2025): datos de GSHHG 2.3.6, commit 006cf93 del 23/9/2016
git show v2.0.0:data/basemap_data/src/mpl_toolkits/basemap_data/gshhs_i.dat           > ../gshhs/new_i.dat
git show v2.0.0:data/basemap_data/src/mpl_toolkits/basemap_data/gshhsmeta_i.dat       > ../gshhs/newmeta_i.dat
git show v2.0.0:data/basemap_data_hires/src/mpl_toolkits/basemap_data/gshhs_f.dat     > ../gshhs/new_f.dat
git show v2.0.0:data/basemap_data_hires/src/mpl_toolkits/basemap_data/gshhsmeta_f.dat > ../gshhs/newmeta_f.dat
cd ..
git clone --filter=blob:none --no-checkout --depth 1 https://github.com/nvkelso/natural-earth-vector.git ne_hist
cd ne_hist
for e in shp shx dbf; do git show HEAD:10m_physical/ne_10m_minor_islands.$e > ../ne/ne_10m_minor_islands.$e; done
cd ..
# después: pip install numpy pyshp ephem ; python3 sandy.py gshhs ; python3 figura.py ; python3 auroras.py ; python3 sarah_ann.py
