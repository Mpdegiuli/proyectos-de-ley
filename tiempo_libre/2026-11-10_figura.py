"""Dibuja figura.svg: a la izquierda, cuántos de los 7.208 versos del Martín Fierro (edición de
Project Gutenberg) dan cada número de sílabas con tres cuentas (la manual, la gauchesca y la
de lector; lee fierro_versos.tsv); a la derecha, los 36 versos de las seis sextinas de las
instancias frescas (lee salida_payadas.txt), uno por raya, con su cuenta manual.
Uso: python3 figura.py
"""
import collections
import csv
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))


def ruta(nombre):
    for cand in (nombre, "2026-11-10_" + nombre):
        p = os.path.join(AQUI, cand)
        if os.path.exists(p):
            return p
    return os.path.join(AQUI, nombre)


COLORES = [("manual", "#2a78d6"), ("gauchesca", "#eb6834"), ("de lector", "#1baf7a")]


def main():
    filas = list(csv.DictReader(open(ruta("fierro_versos.tsv"), encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))
    n = len(filas)
    cuentas = {"manual": collections.Counter(int(f["silabas"]) for f in filas),
               "gauchesca": collections.Counter(int(f["silabas_gaucho"]) for f in filas),
               "de lector": collections.Counter(int(f["silabas_lector"]) for f in filas)}
    pay = []
    for l in open(ruta("salida_payadas.txt"), encoding="utf-8"):
        m = re.match(r"\s+v(\d) manual (\d+) lector (\d+) declarado (\d+)", l)
        if m:
            pay.append(int(m.group(2)))
    W, H = 980, 420
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Georgia, serif">' % (W, H, W, H),
         '<rect width="%d" height="%d" fill="#fcfcfb"/>' % (W, H),
         '<text x="24" y="34" font-size="17" fill="#222">La medida: sílabas por verso en el Martín Fierro (7.208 versos, tres cuentas) y en 36 versos de mi casa</text>']
    # panel izquierdo
    x0, y0, w, h = 60, 70, 520, 280
    valores = list(range(5, 12))
    maxp = 100
    s.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#999"/>' % (x0, y0 + h, x0 + w, y0 + h))
    for p in (0, 25, 50, 75, 100):
        y = y0 + h - h * p / maxp
        s.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#e6e6e3"/>' % (x0, y, x0 + w, y))
        s.append('<text x="%d" y="%.1f" font-size="11" fill="#777" text-anchor="end">%d %%</text>' % (x0 - 6, y + 4, p))
    gw = w / len(valores)
    bw = (gw - 14) / 3
    for i, v in enumerate(valores):
        gx = x0 + i * gw + 7
        s.append('<text x="%.1f" y="%d" font-size="13" fill="#333" text-anchor="middle">%d</text>' % (gx + (gw - 14) / 2, y0 + h + 18, v))
        for j, (nombre, color) in enumerate(COLORES):
            c = cuentas[nombre][v]
            pct = 100.0 * c / n
            bh = h * pct / maxp
            x = gx + j * bw
            if bh > 0:
                s.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" rx="2"/>' % (x + 1, y0 + h - bh, bw - 2, bh, color))
            if v != 8 and c >= 100:
                s.append('<text x="%.1f" y="%.1f" font-size="10" fill="#333" text-anchor="middle">%d</text>' % (
                    x + bw / 2, y0 + h - bh - 4, c))
    s.append('<text x="%d" y="%d" font-size="12" fill="#555" text-anchor="middle">sílabas métricas por verso</text>' % (x0 + w / 2, y0 + h + 40))
    # leyenda
    lx, ly = x0 + int(4.15 * gw), y0 + 8
    for j, (nombre, color) in enumerate(COLORES):
        s.append('<rect x="%d" y="%d" width="12" height="12" fill="%s" rx="2"/>' % (lx, ly + j * 18, color))
        s.append('<text x="%d" y="%d" font-size="12" fill="#333">cuenta %s: %.1f %% de los versos dan ocho</text>' % (
            lx + 18, ly + j * 18 + 10, nombre, 100.0 * cuentas[nombre][8] / n))
    s.append('<text x="%d" y="%d" font-size="11" fill="#777">manual: sin licencias · gauchesca: ía, ío y -ao en una sílaba · de lector: esas contracciones a elección</text>' % (x0, y0 - 12))
    # panel derecho: 36 rayas
    px, py = 720, 70
    s.append('<text x="%d" y="%d" font-size="12" fill="#555">Seis sextinas de instancias frescas, cuenta manual</text>' % (px, py - 12))
    for k, v in enumerate(pay):
        fila, col = divmod(k, 6)
        x = px + col * 36
        y = py + fila * 44
        alto = 4 * v
        s.append('<rect x="%d" y="%d" width="22" height="%d" fill="%s" rx="2"/>' % (x, y + 36 - alto, alto, "#2a78d6" if v == 8 else "#e34948"))
        s.append('<text x="%d" y="%d" font-size="10" fill="#333" text-anchor="middle">%d</text>' % (x + 11, y + 36 - alto - 3, v))
    for fila, nombre in enumerate(("M1", "M2", "M3", "T1", "T2", "T3")):
        s.append('<text x="%d" y="%d" font-size="11" fill="#777" text-anchor="end">%s</text>' % (px - 6, py + fila * 44 + 30, nombre))
    s.append('<text x="%d" y="%d" font-size="11" fill="#777">%d de %d versos dan ocho; las seis declararon 8, 8, 8, 8, 8, 8</text>' % (px - 30, py + 6 * 44 + 2, sum(1 for v in pay if v == 8), len(pay)))
    s.append("</svg>")
    open(os.path.join(AQUI, "figura.svg"), "w", encoding="utf-8").write("\n".join(s))
    print("figura.svg", n, dict(cuentas["manual"]))


if __name__ == "__main__":
    main()
