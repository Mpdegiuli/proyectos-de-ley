# figura.py — tiempo libre 4/10/2026. Escribe dos_ordenes.svg (y un PNG si está cairosvg).
# Dos maneras de ordenar la palabra entre siete asientos durante catorce rondas:
# la rotación cíclica de isla/bucle.py y la caza simple de los campaneros.
from campanas import caza

rot = [tuple((i + r) % 7 + 1 for i in range(7)) for r in range(14)]
hunt = caza(7)[:-1]
W, H, dx, dy = 760, 600, 40, 30

def panel(x0, y0, filas, titulo, pie):
    s = [f'<g transform="translate({x0},{y0})">',
         f'<text x="{3*dx}" y="-44" class="t">{titulo}</text>',
         '<g class="c"><text x="-34" y="-18">ronda</text>'
         + "".join(f'<text x="{j*dx}" y="-18">{j+1}.º</text>' for j in range(7))
         + "".join(f'<text x="-34" y="{r*dy}">{r+1}</text>' for r in range(14)) + '</g>']
    for clase, asiento in (("b", 2), ("a", 1)):
        pts = [(f.index(asiento) * dx, r * dy - 4) for r, f in enumerate(filas)]
        tramo = [pts[0]]; tramos = []; saltos = []
        for p, q in zip(pts, pts[1:]):
            if abs(q[0] - p[0]) > dx:
                tramos.append(tramo); saltos.append((p, q)); tramo = [q]
            else:
                tramo.append(q)
        tramos.append(tramo)
        s.append(f'<g class="{clase}">' + "".join('<polyline points="' + " ".join(f"{x},{y}" for x, y in t) + '"/>' for t in tramos if len(t) > 1)
                 + "".join(f'<line class="s" x1="{p[0]}" y1="{p[1]}" x2="{q[0]}" y2="{q[1]}"/>' for p, q in saltos) + '</g>')
    s.append('<g fill="#fff">' + "".join(f'<circle cx="{f.index(a)*dx}" cy="{r*dy-4}" r="9"/>' for r, f in enumerate(filas) for a in (1, 2)) + '</g>')
    for clase, cuales in (("n", (3, 4, 5, 6, 7)), ("n na", (1,)), ("n nb", (2,))):
        s.append(f'<g class="{clase}">' + "".join(f'<text x="{f.index(a)*dx}" y="{r*dy}">{a}</text>' for r, f in enumerate(filas) for a in cuales) + '</g>')
    s.append('<g class="p">' + "".join(f'<text x="{3*dx}" y="{14*dy + 8 + 17*k}">{l}</text>' for k, l in enumerate(pie)) + '</g></g>')
    return "\n".join(s)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="DejaVu Sans, Helvetica, Arial, sans-serif" text-anchor="middle">
<style>
.t{{font-size:15px;font-weight:bold;fill:#1a1a1a}} .c{{font-size:10.5px;fill:#777}} .p{{font-size:11.5px;fill:#333}}
.n{{font-size:13.5px;font-family:DejaVu Sans Mono,Menlo,monospace;fill:#333}} .na{{fill:#1d4ed8;font-weight:bold}} .nb{{fill:#c2410c;font-weight:bold}}
.a,.b{{fill:none;stroke-linecap:round;stroke-linejoin:round}} .a{{stroke:#1d4ed8;stroke-width:2.6}} .b{{stroke:#c2410c;stroke-width:1.6}}
.s{{stroke-dasharray:3 5;opacity:.35}}
</style>
<rect width="{W}" height="{H}" fill="#fff"/>
{panel(70, 90, rot, "La rotación de la isla", ["Cada asiento abre una ronda de cada siete,", "y habla siempre justo después del mismo:", "el 2 después del 1 en doce rondas de catorce."])}
{panel(450, 90, hunt, "La caza simple en siete", ["Cada asiento pasa dos veces por cada lugar", "y habla dos veces justo después", "de cada uno de los otros seis."])}
<text x="{W/2}" y="{H-14}" class="c">Lugar en el orden de la palabra (columnas) en catorce rondas (filas). En azul el asiento 1, en naranja el 2.</text>
</svg>
'''
open("dos_ordenes.svg", "w").write(svg)
try:
    import cairosvg
    cairosvg.svg2png(url="dos_ordenes.svg", write_to="dos_ordenes.png", scale=2)
except Exception as e:
    print("sin PNG:", e)
print("rotación: el 2 habla justo después del 1 en", sum(1 for f in rot if f.index(2) == f.index(1) + 1), "de 14 rondas")
