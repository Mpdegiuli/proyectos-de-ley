#!/usr/bin/env python3
"""figura.py — escribe dos_octubres.svg (y el PNG si está cairosvg).
Arriba: los mismos días reales de octubre y noviembre de 1584 con el número que les tocaba
en Lima (según lo mandado: del 4 al 15) y el que les puso Córdoba (que no saltó).
Abajo: el día de la semana que el escribano de Córdoba anotó cada 1 de enero, contra los dos calendarios.
Uso: python3 figura.py     (importa dias.py, misma carpeta)
"""
from dias import jdn_jul, jdn_greg, de_jdn_greg, de_jdn_jul, dia

W, H = 1000, 790
LIMA, CBA, GRIS, TINTA, FONDO = "#b4532a", "#1f5f8b", "#8a8a8a", "#222222", "#fbfaf6"
MES = {9: "sep", 10: "oct", 11: "nov"}
o = []
def t(x, y, s, size=13, fill=TINTA, anchor="start", weight="normal", style="normal"):
    # atributos solo cuando difieren del valor por defecto del <svg>, para que el archivo sea corto
    a = ""
    if size != 12: a += ' font-size="%d"' % size
    if fill != GRIS: a += ' fill="%s"' % fill
    if anchor != "start": a += ' text-anchor="%s"' % anchor
    if weight != "normal": a += ' font-weight="bold"'
    o.append('<text x="%d" y="%d"%s>%s</text>' % (round(x), round(y), a, s))

o.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="DejaVu Sans, Verdana, sans-serif" font-size="12" fill="%s">' % (W, H, W, H, GRIS))
o.append('<rect width="100%%" height="100%%" fill="%s"/>' % FONDO)
o.append('<style>.c{stroke:#d8d5cc}</style>')   # borde de las casillas
t(40, 40, "Octubre de 1584: los mismos días, dos cuentas", 20, weight="bold")
t(40, 62, "Cada casilla es un día real. Arriba, el número que le tocaba en Lima según la pragmática (al domingo 4 le sigue el lunes 15).", 12, GRIS)
t(40, 79, "Abajo, el que le puso Córdoba del Tucumán, que ese octubre no saltó.", 12, GRIS)

# --- panel 1: grilla de semanas
x0, y0, cw, ch = 40, 122, 124, 62
cols = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
for i, c in enumerate(cols):
    t(x0 + i * cw + cw / 2, y0 - 10, c, 12, GRIS, "middle")
ini = jdn_jul(1584, 9, 28)            # lunes 28 de septiembre (juliano)
assert dia(ini) == "lunes"
fin = jdn_jul(1584, 10, 31)           # último día del octubre cordobés
semanas = (fin - ini) // 7 + 1
salto = jdn_jul(1584, 10, 4)          # último día común
for k in range(semanas * 7):
    j = ini + k
    col, fila = k % 7, k // 7
    x, y = x0 + col * cw, y0 + fila * ch
    yj, mj, dj = de_jdn_jul(j)
    yg, mg, dg = de_jdn_greg(j)
    cabildo = (mj, dj) == (10, 8)
    fill = "#fff3d6" if cabildo else ("#ffffff" if j > salto else "#f1efe8")
    o.append('<rect %s x="%d" y="%d" width="%d" height="%d" fill="%s"/>'
             % ('stroke="#c9a227" stroke-width="2.5"' if cabildo else 'class="c"', x, y, cw - 4, ch - 4, fill))
    if j <= salto:
        t(x + 10, y + 36, "%d %s" % (dj, MES[mj]), 16, TINTA, weight="bold")
        t(x + cw - 12, y + 36, "igual", 10, GRIS, "end")
    else:
        t(x + 10, y + 24, "%d %s" % (dg, MES[mg]), 15, LIMA, weight="bold")
        t(x + 10, y + 47, "%d %s" % (dj, MES[mj]), 15, CBA, weight="bold")
        if cabildo:
            t(x + cw - 10, y + 47, "cabildo", 11, CBA, "end", "bold")
yl = y0 + semanas * ch + 18
o.append('<rect x="40" y="%d" width="14" height="14" fill="%s"/>' % (yl - 12, LIMA)); t(60, yl, "Lima (cuenta nueva)", 12)
o.append('<rect x="230" y="%d" width="14" height="14" fill="%s"/>' % (yl - 12, CBA)); t(250, yl, "Córdoba (cuenta vieja)", 12)
t(40, yl + 22, "El jueves marcado es el «ocho días del mes de Octubre» del acta de Córdoba. Para Lima ese jueves era 18.", 12, GRIS)

# --- panel 2: los años nuevos del escribano
y1 = yl + 72
t(40, y1, "El 1 de enero en las actas de Córdoba", 17, weight="bold")
t(40, y1 + 20, "Día de la semana que anotó el escribano en el acta de año nuevo, y el que da cada calendario para esa fecha.", 12, GRIS)
acta = {1574: "viernes", 1575: "sábado", 1576: "domingo", 1577: "martes", 1580: "viernes", 1581: "domingo",
        1582: "lunes", 1583: "martes", 1584: "miércoles", 1585: "viernes", 1587: "jueves"}
AB = {"lunes": "lun", "martes": "mar", "miércoles": "mié", "jueves": "jue", "viernes": "vie", "sábado": "sáb", "domingo": "dom"}
xa, ya, ca, ra = 150, y1 + 62, 60, 34
t(40, ya + 22, "acta", 12, TINTA, weight="bold"); t(40, ya + ra + 22, "juliano", 12, CBA); t(40, ya + 2 * ra + 22, "gregoriano", 12, LIMA)
for i, y in enumerate(range(1574, 1588)):
    x = xa + i * ca
    t(x + ca / 2, ya - 8, str(y), 12, GRIS, "middle")
    a = acta.get(y); jl = dia(jdn_jul(y, 1, 1)); gr = dia(jdn_greg(y, 1, 1))
    for fila, (val, col) in enumerate(((a, TINTA), (jl, CBA), (gr, LIMA))):
        yy = ya + fila * ra
        coincide = a is not None and fila > 0 and val == a
        o.append('<rect class="c" x="%d" y="%d" width="%d" height="%d" fill="%s"/>'
                 % (x, yy, ca - 4, ra - 4, ("#dbe9f3" if col == CBA else "#f6ddd0") if coincide else "#ffffff"))
        t(x + ca / 2 - 2, yy + 20, AB[val] if val else "—", 13, col if (fila == 0 or coincide) else "#b5b5b5", "middle",
          "bold" if (fila == 0 or coincide) else "normal")
t(40, ya + 3 * ra + 22, "De 1574 a 1585 el acta coincide con el juliano; en 1587, con el gregoriano. Las de 1578 y 1579 no las encontré;", 12, GRIS)
t(40, ya + 3 * ra + 39, "la de 1586 no trae el día. El cambio está entre el viernes 1 de enero y el 6 de junio de 1585.", 12, GRIS)
o.append("</svg>")
svg = "\n".join(o)
open("dos_octubres.svg", "w", encoding="utf-8").write(svg)
print("dos_octubres.svg:", len(svg), "bytes")
try:
    import cairosvg
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to="dos_octubres.png", output_width=1400)
    print("dos_octubres.png escrito")
except ImportError:
    print("(sin cairosvg: no escribo el PNG)")
