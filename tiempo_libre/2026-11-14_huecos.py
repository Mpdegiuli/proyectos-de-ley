#!/usr/bin/env python3
"""Los números de ley que no son leyes.

Cuaderno de tiempo libre del 14/11/2026. Este script no lee ninguna corrida del repositorio:
lleva adentro, como datos, la lista de proyectos de ley vetados en su totalidad que figura en la
tabla "Vetos" de Infoleg (https://www.infoleg.gob.ar/?page_id=2751), tal como la transcribió un
agente de lectura web esta mañana (puede traer errores de transcripción; ver el cuaderno), más
las leyes cuya insistencia por el Congreso pude documentar. Escribe `2026-11-14_huecos.csv` (una
fila por número vetado) y `2026-11-14_registro.svg`, un registro de leyes con los huecos marcados.

Uso: python3 2026-11-14_huecos.py          (escribe el CSV y el SVG en la carpeta actual)
     python3 2026-11-14_huecos.py --png    (además, el PNG; pide cairosvg)
"""
import csv
import sys

PRIMERA = 23040   # primera ley del Congreso de 1983 (derogación de la autoamnistía)
ULTIMA = 27828    # última sancionada que encontré hoy (24/9/2026; B.O. 13/10/2026)

# Vetos totales, por presidencia del decreto de veto, según la tabla de Infoleg.
VETADAS = {
    "Alfonsín": [23080, 23100, 23104, 23108, 23131, 23134, 23135, 23136, 23137, 23141, 23142,
                 23144, 23146, 23147, 23148, 23159, 23163, 23198, 23209, 23250, 23275, 23294,
                 23301, 23303, 23304, 23305, 23355, 23363, 23373, 23381, 23391, 23421, 23430,
                 23431, 23486, 23523, 23635],
    "Menem": [23688, 23699, 23792, 23823, 23852, 23872, 23889, 23894, 23901, 23938, 23951,
              24006, 24027, 24032, 24041, 24058, 24087, 24092, 24139, 24142, 24152, 24157,
              24164, 24168, 24180, 24182, 24197, 24245, 24247, 24250, 24251, 24255, 24277,
              24381, 24404, 24416, 24471, 24476, 24482, 24490, 24506, 24509, 24511, 24528,
              24547, 24550, 24559, 24565, 24567, 24577, 24592, 24597, 24600, 24641, 24651,
              24662, 24665, 24672, 24690, 24720, 24726, 24732, 24735, 24740, 24745, 24752,
              24822, 24858, 24863, 24873, 24889, 24899, 24902, 24909, 24913, 24914, 24962,
              25009, 25014, 25016, 25017, 25028, 25029, 25037, 25055, 25059, 25119],
    "De la Rúa": [25194, 25195, 25201, 25204, 25206, 25207, 25208, 25228, 25245, 25267, 25268,
                  25271, 25274, 25282, 25283, 25294, 25296, 25301, 25373, 25377, 25416, 25435,
                  25464, 25471, 25472, 25500],
    "Rodríguez Saá": [25547, 25548],
    "Duhalde": [25534, 25541, 25544, 25567, 25609, 25647, 25662, 25666, 25676, 25683, 25711,
                25715],
    "N. Kirchner": [25759, 25773, 25818, 25821, 25897, 25941, 25969, 25978, 25979, 25980,
                    25984, 25993, 26325],
    "C. Fernández": [26418, 26649, 26751],
    "Macri": [27251, 27331, 27335, 27344, 27443],
    "Milei": [27756, 27757, 27790, 27791, 27792, 27793, 27794, 27795, 27796],
}
# Nota: la tabla dice "24.028" para el decreto 1279/1998; las leyes de 1998 llevan 25.0xx, así
# que lo anoto como 25028 y lo declaro como corrección mía.

# Vetos totales insistidos por el Congreso (la ley se promulgó igual, con el mismo número).
# Fuente: Revista de Derecho Parlamentario n.º 10 (HCDN, "Veto e insistencia"), que llega hasta
# mediados de los noventa, más 25.715 (2003) y las tres de 2025. Entre 1995 y 2002 hubo unas
# trece insistencias más que no pude identificar una por una (ver el cuaderno): esos números
# siguen marcados acá como huecos y no lo son.
INSISTIDAS = {23523, 23852, 23872, 23950, 24014, 24164, 24251, 24476, 24482, 24490, 24506,
              25715, 27793, 27795, 27796}
# Promulgadas por insistencia pero con la ejecución suspendida por el decreto de promulgación
# (decretos 681/2025, 759/2025 y 760/2025).
SUSPENDIDAS = {27793, 27795, 27796}

NOTAS = {
    23080: "23.080: el primer hueco (1984)",
    23523: "23.523: la única insistencia de Alfonsín",
    25301: "25.301: aranceles al azúcar (2000)",
    25715: "25.715: azúcar otra vez; insistida en 2003",
    26418: "26.418: la primera ley de glaciares (2008)",
    26649: "26.649: el 82 % móvil (2010)",
    27757: "27.757: financiamiento universitario (2024)",
    27793: "27.793: discapacidad; insistida y suspendida (2025)",
}

# Hitos aproximados de año, para la regla de arriba (número de la primera ley de cada año que
# pude ubicar o estimar; los marcados con ~ son estimaciones a partir de leyes conocidas).
ANIOS = [(23040, "dic 1983"), (23300, "~1985"), (23700, "~1989"), (24000, "~1991"),
         (24500, "~1995"), (25000, "~1998"), (25500, "~2001"), (26000, "~2005"),
         (26500, "~2009"), (27000, "~2014"), (27500, "~2019"), (27828, "sep 2026")]


def todas():
    for pres, nums in VETADAS.items():
        for n in nums:
            yield pres, n


def escribir_csv(ruta):
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["numero", "veto_por", "insistida", "ejecucion_suspendida", "nota"])
        for pres, n in sorted(todas(), key=lambda t: t[1]):
            w.writerow([n, pres, int(n in INSISTIDAS), int(n in SUSPENDIDAS), NOTAS.get(n, "")])


def svg_registro(ruta):
    vetadas = {n: p for p, n in todas()}
    POR_FILA = 200
    CELDA, SEP = 5, 1
    PASO = CELDA + SEP
    ancho_reg = POR_FILA * PASO
    izq, arriba = 120, 150
    total = ULTIMA - PRIMERA + 1
    filas = (total + POR_FILA - 1) // POR_FILA
    alto_fila = 22
    W = izq + ancho_reg + 300
    H = arriba + filas * alto_fila + 60
    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
               f'viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">')
    out.append(f'<rect width="{W}" height="{H}" fill="#fbfaf6"/>')
    out.append('<text x="120" y="40" font-size="22" fill="#222">Registro de leyes de la Nación, '
               '23.040 a 27.828: cada cuadrito es un número de ley</text>')
    out.append('<text x="120" y="64" font-size="13" fill="#555">Gris: números que son leyes. '
               'Rojo: proyectos vetados en su totalidad (el número quedó, la ley no). '
               'Rojo con borde: vetados e insistidos por el Congreso (ley, con el mismo número). '
               'Naranja: insistidos en 2025 y promulgados con la ejecución suspendida.</text>')
    out.append('<text x="120" y="82" font-size="13" fill="#555">Fuente: tabla «Vetos» de Infoleg '
               '(transcripción de esta mañana) y Revista de Derecho Parlamentario n.º 10 (HCDN); '
               'unas trece insistencias de 1995–2002 no están identificadas y figuran como huecos.</text>')
    # regla de años
    y_regla = arriba - 30
    out.append(f'<line x1="{izq}" y1="{y_regla}" x2="{izq+ancho_reg}" y2="{y_regla}" '
               f'stroke="#999" stroke-width="1"/>')
    for n, rot in ANIOS:
        x = izq + (n - PRIMERA) / total * ancho_reg
        out.append(f'<line x1="{x:.1f}" y1="{y_regla-4}" x2="{x:.1f}" y2="{y_regla+4}" stroke="#999"/>')
        out.append(f'<text x="{x:.1f}" y="{y_regla-8}" font-size="10" fill="#777" '
                   f'text-anchor="middle">{rot}</text>')
    out.append(f'<text x="{izq}" y="{y_regla+18}" font-size="10" fill="#777">La regla de arriba '
               f'estira la serie entera en una línea; abajo, la misma serie en renglones de 200 '
               f'números, como un libro de registro.</text>')
    # celdas
    for i in range(total):
        n = PRIMERA + i
        fila, col = divmod(i, POR_FILA)
        x = izq + col * PASO
        y = arriba + fila * alto_fila
        if n in vetadas:
            if n in SUSPENDIDAS:
                out.append(f'<rect x="{x}" y="{y}" width="{CELDA}" height="{CELDA+6}" fill="#e08a1e"/>')
            elif n in INSISTIDAS:
                out.append(f'<rect x="{x-0.5}" y="{y-0.5}" width="{CELDA+1}" height="{CELDA+7}" '
                           f'fill="#c8322b" stroke="#222" stroke-width="1"/>')
            else:
                out.append(f'<rect x="{x}" y="{y}" width="{CELDA}" height="{CELDA+6}" fill="#c8322b"/>')
        else:
            out.append(f'<rect x="{x}" y="{y+3}" width="{CELDA}" height="{CELDA}" fill="#d9d6cc"/>')
    # rótulos de fila
    for fila in range(filas):
        n0 = PRIMERA + fila * POR_FILA
        y = arriba + fila * alto_fila + 9
        out.append(f'<text x="{izq-8}" y="{y}" font-size="10" fill="#666" text-anchor="end">'
                   f'{n0:,}'.replace(",", ".") + '</text>')
    # notas al margen derecho
    x_nota = izq + ancho_reg + 14
    usadas = set()
    for n, texto in sorted(NOTAS.items()):
        i = n - PRIMERA
        fila, col = divmod(i, POR_FILA)
        y = arriba + fila * alto_fila + 9
        while y in usadas:
            y += 12
        usadas.add(y)
        xcel = izq + col * PASO + CELDA / 2
        ycel = arriba + fila * alto_fila + 5
        out.append(f'<line x1="{xcel:.1f}" y1="{ycel}" x2="{x_nota-4}" y2="{y-3}" '
                   f'stroke="#c8322b" stroke-width="0.6" stroke-dasharray="2,2"/>')
        out.append(f'<text x="{x_nota}" y="{y}" font-size="10" fill="#333">{texto}</text>')
    # cuenta al pie
    nv = len(vetadas)
    ni = len(INSISTIDAS & set(vetadas))
    out.append(f'<text x="{izq}" y="{H-20}" font-size="12" fill="#333">{total:,} números; '
               f'{nv} vetados en su totalidad según la tabla; {ni} de ellos insistidos (identificados); '
               f'huecos marcados: {nv-ni}. Cuaderno de tiempo libre, 14/11/2026.</text>'
               .replace(f"{total:,}", f"{total:,}".replace(",", ".")))
    out.append('</svg>')
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    escribir_csv("2026-11-14_huecos.csv")
    svg_registro("2026-11-14_registro.svg")
    vetadas = dict((n, p) for p, n in todas())
    print(f"números en la serie: {ULTIMA - PRIMERA + 1}")
    print(f"vetados en su totalidad (tabla de Infoleg): {len(vetadas)}")
    for p, nums in VETADAS.items():
        print(f"  {p}: {len(nums)}")
    print(f"insistidos identificados: {len(INSISTIDAS & set(vetadas))} "
          f"(en la lista de insistidas hay {len(INSISTIDAS - set(vetadas))} que no están en la tabla de vetos)")
    print(f"huecos marcados: {len(vetadas) - len(INSISTIDAS & set(vetadas))}")
    print(f"proporción sobre la serie: {100*(len(vetadas) - len(INSISTIDAS & set(vetadas)))/(ULTIMA-PRIMERA+1):.2f} %")
    if "--png" in sys.argv:
        import cairosvg
        cairosvg.svg2png(url="2026-11-14_registro.svg", write_to="2026-11-14_registro.png", scale=1.6)
        print("png escrito")
