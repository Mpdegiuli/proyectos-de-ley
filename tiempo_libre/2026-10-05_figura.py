#!/usr/bin/env python3
"""Dibuja dos_piedras.svg: Res Gestae 34.1 y 34.3 en tres estados.

  1. lo que se leía en Ancyra (corchetes de Fairley, 1898, que sigue a Mommsen)
  2. lo que Mommsen puso en los huecos (1883)
  3. el texto con los fragmentos de Antioquía (versión con corchetes de The Latin
     Library; en 34.1, además, el fragmento TENS RE que publicó Botteri en 2003)

Es un esquema: no respeta los renglones de la piedra ni el tamaño real de los huecos.
Uso: python3 figura.py   (escribe dos_piedras.svg; con cairosvg instalado, también el PNG)
"""
P, G, R, X, N = "piedra", "hueco", "restituido", "desmentido", "nueva"

def hueco(n): return ("·" * n, G)

BLOQUES = [
 ("34.1", [
  ("Ancyra", [("PER CONSENSVM VNIVERSORVM ", P), ("[", R), hueco(16), ("]", R), ("IVM REM PVBLICAM", P)]),
  ("Mommsen, 1883", [("PER CONSENSVM VNIVERSORVM ", P), ("[", R), ("POTITVS", X), (" RERVM OMN]", R), ("IVM REM PVBLICAM", P)]),
  ("con Antioquía", [("PER CONSENSVM VNIVERSORVM ", P), ("[PO]", R), ("TENS RE", N), ("[RV]", R), ("M OM", N), ("[N]", R), ("IVM REM PVBLICAM", P)]),
 ]),
 ("34.3", [
  ("Ancyra", [("POST ID TEM", P), ("[", R), hueco(34), ("]", R), ("ATIS AV", P), ("[", R), hueco(4), ("]", R), ("IHILO", P)]),
  ("Mommsen, 1883", [("POST ID TEM", P), ("[PVS PRAESTITI OMNIBVS ", R), ("DIGNITATE", X), (" POTEST]", R), ("ATIS AV", P), ("[TEM N]", R), ("IHILO", P)]),
  ("con Antioquía", [("POST ID TEM", P), ("[PVS A]", R), ("VCTORITATE", N), (" [OMNIBVS PRAESTITI POTEST]", R), ("ATIS AV", P), ("[TEM N]", R), ("IHILO", P)]),
 ]),
 ("", [
  ("Ancyra", [("AMPLIV", P), ("[", R), hueco(20), ("]", R), ("IHI QVOQVE IN MA", P), ("[", R), hueco(3), ("]", R), ("TRA", P), ("[·]", R), ("V CONLEGAE", P)]),
  ("Mommsen, 1883", [("AMPLIV", P), ("[S HABVI QVAM ", R), ("QVI FVERVNT", X), (" M]", R), ("IHI QVOQVE IN MA", P), ("[GIS]", R), ("TRA", P), ("[T]", R), ("V CONLEGAE", P)]),
  ("con Antioquía", [("AMPLIV", P), ("[S HABV]", R), ("I QVAM CET", N), ("[ERI QVI M]", R), ("IHI QVOQVE IN MA", P), ("[GIS]", R), ("TRA", P), ("[T]", R), ("V CONLEGAE ", P), ("F", N), ("[VERVNT]", R)]),
 ]),
]

FS = 13.5                    # cuerpo de letra
CW = 0.602 * FS               # ancho de celda: el avance de DejaVu Sans Mono
X0, XL = 212, 28             # donde empieza el texto, donde van los rótulos
W = 960
CL = {P: "p", G: "g", R: "r", X: "r", N: "n"}
out = []
y = 78
out.append(f'<text class="s" x="{XL}" y="38" font-size="19" fill="#1f1d1a">Res Gestae 34: lo que estaba en la piedra y lo que estaba entre corchetes</text>')
out.append(f'<text class="s" x="{XL}" y="58" fill="#6b665b">Esquema. No respeta los renglones de la inscripción ni el tamaño real de los huecos.</text>')
for titulo, filas in BLOQUES:
    if titulo:
        y += 22
        out.append(f'<text class="s" x="{XL}" y="{y}" font-size="14" font-weight="bold" fill="#1f1d1a">{titulo}</text>')
        y += 8
    else:
        y += 6
    for rotulo, segs in filas:
        y += 27
        out.append(f'<text class="s" x="{XL+26}" y="{y}" fill="#6b665b">{rotulo}</text>')
        i = 0
        for txt, k in segs:
            # cada segmento se estira a su lugar en una grilla fija, tenga la fuente que tenga
            a = len(txt) - len(txt.lstrip(" ")); t = txt.strip(" ")
            x1 = X0 + (i + a) * CW
            largo = len(t) * CW
            if len(t) == 1:
                out.append(f'<text class="m {CL[k]}" x="{x1:.1f}" y="{y}">{t}</text>')
            else:
                out.append(f'<text class="m {CL[k]}" x="{x1:.1f}" y="{y}" textLength="{largo:.1f}">{t}</text>')
            if k == X:   # tachado: lo que la piedra desmintió
                out.append(f'<line class="t" x1="{x1:.1f}" y1="{y-4.5}" x2="{x1 + len(t)*CW:.1f}" y2="{y-4.5}"/>')
            i += len(txt)
    y += 10
# leyenda
y += 30
ley = [(P, "letras leídas en Ancyra"), (N, "letras que agregó Antioquía"), (R, "[restituido por el editor]"), (X, "restitución desmentida")]
x = XL
for k, t in ley:
    out.append(f'<text class="m {CL[k]}" x="{x}" y="{y}" font-size="13">ABC</text>')
    if k == X:
        out.append(f'<line class="t" x1="{x}" y1="{y-4.5}" x2="{x+24}" y2="{y-4.5}"/>')
    out.append(f'<text class="s" x="{x+32}" y="{y}" fill="#3d3a34">{t}</text>')
    x += 32 + 6.3 * len(t) + 30
H = y + 28
ESTILO = ("<style>.s{font-family:Georgia,serif;font-size:12.5px}"
          ".m{font-family:'DejaVu Sans Mono',Menlo,Consolas,monospace;font-size:%spx}"
          ".p{fill:#1f1d1a;font-weight:bold}.n{fill:#b23a1e;font-weight:bold}.r{fill:#8d877a}.g{fill:#b9b4a8}"
          ".t{stroke:#b23a1e;stroke-width:1.4}</style>" % FS)
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n{ESTILO}\n'
       f'<rect width="{W}" height="{H}" fill="#f6f2e8"/>\n' + "\n".join(out) + "\n</svg>\n")
open("dos_piedras.svg", "w", encoding="utf-8").write(svg)
print("dos_piedras.svg", len(svg), "bytes", W, "x", H)
try:
    import cairosvg
    cairosvg.svg2png(url="dos_piedras.svg", write_to="dos_piedras.png", scale=1.6)
    print("dos_piedras.png")
except Exception as e:
    print("sin PNG (pip install cairosvg):", e)
