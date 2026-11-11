#!/bin/sh
# Baja el texto escaneado (OCR) de dos tomos de los Acuerdos del extinguido
# Cabildo de Buenos Aires desde archive.org y saca los pasajes que cita la
# nota 2 del 11/11/2026: el patrono "San Martín" en 1589, las hormigas en 1590,
# la langosta en 1607, el sorteo de 1611 y la fiesta de 1614. Los números de
# línea no se usan: se busca por frase, con contexto. Pide curl y grep.
# Libro I (1589-1591, 1603?, 1606-1608): copia de Harvard digitalizada por Google.
# Libro II (1609-1614): edición del Archivo General de la Nación, ed. J. J. Biedma.
set -e
L1=acuerdosdelexti00cabigoog
L2=acuerdosdelextin00cabi
for id in $L1 $L2; do
  [ -f "$id.txt" ] || curl -sSL -o "$id.txt" "https://archive.org/download/$id/${id}_djvu.txt"
  printf '%s: %s bytes\n' "$id" "$(wc -c < "$id.txt")"
done
echo; echo "== 1589, foja 14 vuelta: San Martin nuestro patron y abogado"
grep -n -B2 -A3 "nuestro  patrón  y  abogado" $L1.txt
echo; echo "== 1590, 1 de octubre, foja 51: las hormigas y el Padre"
grep -n -B1 -A2 "en  lo  de  las  hormigas" $L1.txt
echo; echo "== 1607, 15 de octubre, foja 216: las once mil virgenes y la langosta"
grep -n -A6 "ynnumerable  can-" $L1.txt
echo; echo "== 1611, 21 de noviembre, foja 188: el sorteo"
grep -n -A56 "CABILDO  DEL  2 i  DE  NOVIEMBRE  DE  161 1" $L2.txt
echo; echo "== 1614, 6 de octubre, foja 353: San Simon y Judas, y la fiesta de San Martin"
grep -n -A34 "se  trato  como  el  dia  de  San   Simón" $L2.txt
echo; echo "== cuantas veces 'San Martin' y cuantas 'Tours' en cada tomo"
for id in $L1 $L2; do
  printf '%s: San Martin %s, Tours %s\n' "$id" \
    "$(grep -o -i 'san[t]*  *mart[iy]n' $id.txt | wc -l)" "$(grep -o -i 'tours' $id.txt | wc -l)"
done
