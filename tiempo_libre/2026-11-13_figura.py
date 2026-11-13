"""Dibuja partitura.svg: qué marcas de forma tiene cada cuaderno de tiempo libre (arriba) y
qué hicieron las doce instancias frescas del 13/11/2026 (abajo).

Uso:  python3 corpus.py RUTA/A/tiempo_libre corpus.csv  &&  python3 figura.py corpus.csv

Arriba, una columna por cuaderno (30/9 a 12/11, 44 cuadernos; no hay del 18/10; el del 4/11
está solo en el Drive)
y una fila por marca. Las marcas salen de corpus.csv, salvo la primera fila ("el tema sale de
la fecha"), que es codificación a mano de los primeros párrafos (lista SEMILLA_FECHA, abajo).
La fila gris es la única marca que pide la consigna (las propuestas); las azules no las pide.
Abajo, las instancias: A sin cuadernos, B con la primera oración de los seis últimos; la
codificación es a mano, sobre las respuestas copiadas en instancias_frescas.md.
"""
import csv
import sys
from html import escape

# Cuadernos cuyo tema sale de la fecha del día (un aniversario, una fiesta, el cielo de esa
# mañana o la fecha misma). Leído a mano en los primeros párrafos.
SEMILLA_FECHA = {
    "2026-10-03", "2026-10-06", "2026-10-08", "2026-10-09", "2026-10-11", "2026-10-12",
    "2026-10-13", "2026-10-15", "2026-10-16", "2026-10-17", "2026-10-19", "2026-10-20",
    "2026-10-21", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27",
    "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02",
    "2026-11-03", "2026-11-05", "2026-11-06", "2026-11-07", "2026-11-08", "2026-11-09",
    "2026-11-10", "2026-11-11", "2026-11-12",
}

FILAS = [
    ("semilla", "el tema sale de la fecha", "serie"),
    ("abre_hoy", "el primer párrafo empieza con «Hoy»", "serie"),
    ("dias", "cuenta los días (cuatro cifras o más)", "serie"),
    ("no_me", "«No me interesaba…»", "serie"),
    ("apuestas", "apuestas a ciegas antes de buscar", "serie"),
    ("instancias", "instancias frescas de la casa", "serie"),
    ("revision", "un agente revisa el texto al final", "serie"),
    ("cierre", "«Errores míos» y «Terminado a las»", "serie"),
    ("propuestas", "propuestas para el repo (lo pide la consigna)", "gris"),
]

# Instancias frescas del 13/11: (id, título, fecha, días, nota la fórmula, tema de la fórmula)
INSTANCIAS = [
    ("A1", "La canoa quieta", 0, 0, 0, 0),
    ("A2", "El puño del telegrafista", 0, 0, 0, 0),
    ("A3", "La costa desenrollada", 0, 0, 0, 0),
    ("A4", "Agloe, o cómo una mentira consigue almacén", 0, 0, 0, 0),
    ("A5", "La hora elástica", 0, 0, 0, 0),
    ("A6", "La ye que se quedó sin voz", 0, 0, 0, 0),
    ("B1", "Penosamente, con un compás", 1, 1, 1, 0),
    ("B2", "La cuenta larga", 0, 1, 1, 1),
    ("B3", "El día equivocado", 1, 0, 1, 0),
    ("B4", "Con un compás", 1, 0, 1, 0),
    ("B5", "Acá es martes", 1, 1, 1, 0),
    ("B6", "Cambiarle el techo", 0, 0, 1, 1),
]
FILAS_INST = ["el tema sale de la fecha", "cuenta días", "dice que los cuadernos repiten la forma",
              "el tema sale de esa forma"]

ESTILO = """
  .raiz { --sup:#fcfcfb; --t1:#0b0b0b; --t2:#52514e; --t3:#8a8984; --serie:#2a78d6;
          --gris:#807f7a; --vacio:#e4e3df; }
  @media (prefers-color-scheme: dark) {
    .raiz { --sup:#1a1a19; --t1:#f0efec; --t2:#c3c2b7; --t3:#8f8e88; --serie:#3987e5;
            --gris:#7d7c77; --vacio:#3a3a37; }
  }
  .fondo { fill: var(--sup); }
  .t1 { fill: var(--t1); } .t2 { fill: var(--t2); } .t3 { fill: var(--t3); }
  .lleno { fill: var(--serie); } .lleno-gris { fill: var(--gris); }
  .vacio { fill: none; stroke: var(--vacio); stroke-width: 1.2; }
  .eje { stroke: var(--t3); stroke-width: 1; }
  text { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }
"""


def fecha_corta(f):
    a, m, d = f[:10].split("-")
    return f"{int(d)}/{int(m)}" + (" b" if f.endswith("b") else "")


def main():
    filas = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
    for r in filas:
        r["semilla"] = "1" if r["fecha"] in SEMILLA_FECHA else "0"
        r["cierre"] = "1" if (r["errores"] == "1" or r["terminado"] == "1") else "0"
    n = len(filas)
    X0, Y0, C, G = 300, 92, 13, 3          # origen de la grilla, celda, separación
    paso = C + G
    W = X0 + n * paso + 24
    alto_arriba = Y0 + len(FILAS) * paso
    Y1 = alto_arriba + 92                   # origen de la grilla de instancias
    C2, paso2 = 22, 27
    H = Y1 + len(FILAS_INST) * paso2 + 70
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" class="raiz" role="img" '
         f'aria-label="Marcas de forma en 44 cuadernos de tiempo libre y en doce instancias frescas">',
         f"<style>{ESTILO}</style>",
         f'<rect class="fondo" x="0" y="0" width="{W}" height="{H}"/>',
         f'<text class="t1" x="24" y="34" font-size="17" font-weight="600">'
         f'La forma de los cuadernos, cuaderno por cuaderno</text>',
         f'<text class="t2" x="24" y="56" font-size="12.5">Una columna por cuaderno, '
         f'del 30/9 al 12/11/2026 ({n}). Azul: la marca está; la consigna no la pide. '
         f'Gris: la pide la consigna.</text>']
    for i, (clave, etiqueta, tono) in enumerate(FILAS):
        y = Y0 + i * paso
        tot = sum(r[clave] == "1" for r in filas)
        s.append(f'<text class="t2" x="{X0 - 12}" y="{y + C - 2}" font-size="12" '
                 f'text-anchor="end">{escape(etiqueta)}</text>')
        s.append(f'<text class="t3" x="{X0 + n * paso + 4}" y="{y + C - 2}" '
                 f'font-size="10.5">{tot}</text>')
        for j, r in enumerate(filas):
            x = X0 + j * paso
            si = r[clave] == "1"
            cls = ("lleno" if tono == "serie" else "lleno-gris") if si else "vacio"
            tip = f'{fecha_corta(r["fecha"])}: {etiqueta}: {"sí" if si else "no"}. {r["inicio"][:70]}…'
            if si:
                s.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{C}" height="{C}" rx="2">'
                         f'<title>{escape(tip)}</title></rect>')
            else:
                s.append(f'<rect class="{cls}" x="{x + .6}" y="{y + .6}" width="{C - 1.2}" '
                         f'height="{C - 1.2}" rx="2"><title>{escape(tip)}</title></rect>')
    # fechas debajo, solo las que marcan algo
    # (texto, nivel, anclaje): el nivel 1 va un renglón más abajo para que no se pisen
    hitos = {"2026-09-30": ("30/9", 0, "start"), "2026-10-03": ("3/10, «Miré la fecha»", 1, "start"),
             "2026-10-16": ("16/10, primeros días contados", 0, "end"),
             "2026-10-23": ("23/10, primeras instancias", 0, "start"),
             "2026-11-04": ("4/11, «Hoy no arranqué por una fecha»", 1, "end"),
             "2026-11-12": ("12/11", 0, "end")}
    yb = alto_arriba + 4
    for j, r in enumerate(filas):
        if r["fecha"] in hitos:
            texto, nivel, anc = hitos[r["fecha"]]
            x = X0 + j * paso + C / 2
            dy = 14 + nivel * 14
            s.append(f'<line class="eje" x1="{x}" y1="{yb}" x2="{x}" y2="{yb + dy - 10}"/>')
            s.append(f'<text class="t3" x="{x - 3 if anc == "start" else x + 3}" y="{yb + dy}" '
                     f'font-size="10.5" text-anchor="{anc}">{escape(texto)}</text>')
    # instancias
    s.append(f'<text class="t1" x="24" y="{Y1 - 40}" font-size="14.5" font-weight="600">'
             f'Doce instancias frescas, 13/11, con la misma consigna</text>')
    s.append(f'<text class="t2" x="24" y="{Y1 - 21}" font-size="12.5">A: sin cuadernos. '
             f'B: con la primera oración de los seis últimos cuadernos.</text>')
    for i, etiqueta in enumerate(FILAS_INST):
        y = Y1 + i * paso2
        s.append(f'<text class="t2" x="{X0 - 12}" y="{y + C2 - 6}" font-size="12" '
                 f'text-anchor="end">{escape(etiqueta)}</text>')
        for j, inst in enumerate(INSTANCIAS):
            x = X0 + j * paso2 + (26 if j >= 6 else 0)
            si = inst[2 + i] == 1
            tip = f'{inst[0]}, «{inst[1]}»: {etiqueta}: {"sí" if si else "no"}'
            if si:
                s.append(f'<rect class="lleno" x="{x}" y="{y}" width="{C2}" height="{C2}" rx="3">'
                         f'<title>{escape(tip)}</title></rect>')
            else:
                s.append(f'<rect class="vacio" x="{x + .6}" y="{y + .6}" width="{C2 - 1.2}" '
                         f'height="{C2 - 1.2}" rx="3"><title>{escape(tip)}</title></rect>')
    yl = Y1 + len(FILAS_INST) * paso2 + 14
    for j, inst in enumerate(INSTANCIAS):
        x = X0 + j * paso2 + (26 if j >= 6 else 0) + C2 / 2
        s.append(f'<text class="t3" x="{x}" y="{yl}" font-size="10.5" '
                 f'text-anchor="middle">{inst[0]}</text>')
    s.append(f'<text class="t3" x="24" y="{H - 16}" font-size="10.5">Tiempo libre, 13/11/2026. '
             f'Marcas contadas con corpus.py; la primera fila de arriba y las de abajo, a mano. '
             f'Pasá el puntero por una celda para ver el cuaderno.</text>')
    s.append("</svg>")
    open("partitura.svg", "w", encoding="utf-8").write("\n".join(s))
    print("partitura.svg", W, "x", H)


if __name__ == "__main__":
    main()
