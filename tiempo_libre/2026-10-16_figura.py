#!/usr/bin/env python3
"""Figura del cuaderno del 16/10/2026: la técnica del antebrazo aislado.

Panel A: el mecanismo. Un manguito inflado en el brazo antes de dar el relajante
muscular deja ese brazo fuera de la parálisis; durante la operación se le pide al
paciente que apriete la mano.
Panel B: los 260 pacientes de Sanders y otros (Anesthesiology 2017): 12 apretaron
la mano después de la intubación; 5 de esos 12 dijeron que les dolía cuando se les
preguntó; 0 de los 253 interrogados después recordaban algo (el resumen no dice si
los doce están entre los 253).

Escribe antebrazo_aislado.svg. Si está cairosvg, también el PNG. No lee nada del
repositorio y no llama a nadie.
"""
from pathlib import Path

W, H = 900, 540
TINTA = "#222"
GRIS = "#8a8a8a"
CLARO = "#e9e4d8"
ROJO = "#b5412a"
AZUL = "#2f5d8a"
FUENTE = "Georgia, 'Times New Roman', serif"

out = []
w = out.append
w(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FUENTE}">')
w(f'<rect width="{W}" height="{H}" fill="#fbf9f4"/>')

# ---------- Panel A: el mecanismo ----------
w(f'<text x="30" y="36" font-size="15" fill="{TINTA}">A. El antebrazo aislado (Tunstall, 1977)</text>')

# mesa
w(f'<rect x="40" y="300" width="420" height="10" fill="{GRIS}"/>')
w(f'<rect x="60" y="310" width="8" height="60" fill="{GRIS}"/>')
w(f'<rect x="420" y="310" width="8" height="60" fill="{GRIS}"/>')

# cuerpo acostado: cabeza a la izquierda, pies a la derecha
w(f'<circle cx="95" cy="255" r="26" fill="{CLARO}" stroke="{TINTA}" stroke-width="2"/>')
# ojos cerrados
w(f'<path d="M84 254 q6 4 12 0 M98 254 q6 4 12 0" stroke="{TINTA}" stroke-width="1.6" fill="none"/>')
# torso + piernas (tapados con una sábana)
w(f'<path d="M122 240 h150 q20 0 30 12 l100 0 q12 0 12 12 l0 20 q0 16 -16 16 h-276 z" fill="{CLARO}" stroke="{TINTA}" stroke-width="2"/>')
# brazo aislado: sale del hombro hacia el frente (abajo), por fuera de la sábana
w(f'<path d="M150 262 q-8 40 10 70 q14 24 46 30" stroke="{TINTA}" stroke-width="18" stroke-linecap="round" fill="{CLARO}"/>')
w(f'<path d="M150 262 q-8 40 10 70 q14 24 46 30" stroke="{CLARO}" stroke-width="14" stroke-linecap="round" fill="none"/>')
# manguito (torniquete) en la parte alta del brazo
w(f'<rect x="131" y="282" width="38" height="18" rx="3" fill="{ROJO}" transform="rotate(-6 150 291)"/>')
w(f'<path d="M150 282 q-20 -40 20 -58 l60 0" stroke="{ROJO}" stroke-width="1.6" fill="none"/>')  # línea de llamada
w(f'<text x="236" y="228" font-size="12" fill="{ROJO}">manguito inflado antes del relajante</text>')
# mano cerrada (apretando) al final del brazo
w(f'<g transform="translate(206 362)">')
w(f'<ellipse cx="14" cy="0" rx="18" ry="13" fill="{CLARO}" stroke="{TINTA}" stroke-width="2"/>')
for i, (x, y) in enumerate([(0, -9), (10, -12), (20, -11), (29, -7)]):
    w(f'<rect x="{x}" y="{y}" width="8" height="12" rx="3.5" fill="{CLARO}" stroke="{TINTA}" stroke-width="1.6"/>')
w(f'<path d="M-2 4 q10 10 24 8" stroke="{TINTA}" stroke-width="1.6" fill="none"/>')
w('</g>')

# la otra mano del anestesista: solo el borde, para no dibujar otra persona

# globo con la orden
w(f'<path d="M80 150 h260 q10 0 10 10 v44 q0 10 -10 10 h-170 l-22 18 l4 -18 h-72 q-10 0 -10 -10 v-44 q0 -10 10 -10 z" fill="#fff" stroke="{AZUL}" stroke-width="1.6"/>')
w(f'<text x="96" y="176" font-size="14" fill="{AZUL}">«Si me oís, apretame la mano.»</text>')
w(f'<text x="96" y="198" font-size="12" fill="{GRIS}">(el resto del cuerpo no puede moverse)</text>')

# leyenda del mecanismo
w(f'<text x="40" y="468" font-size="12.5" fill="{TINTA}">El relajante muscular paraliza todo lo que la sangre alcanza. El manguito dejó un brazo sin circulación antes de la dosis.</text>')
w(f'<text x="40" y="488" font-size="12.5" fill="{TINTA}">Ese brazo es el único que puede contestar. Si aprieta, hay alguien que oye. Lo que ese alguien recuerde después es otra cuenta.</text>')

# ---------- Panel B: los 260 ----------
x0, y0 = 520, 36
w(f'<text x="{x0}" y="{y0}" font-size="15" fill="{TINTA}">B. 260 pacientes (Sanders y otros, 2017)</text>')
cols, filas = 20, 13
paso = 17
r = 5.6
gx, gy = x0, y0 + 30
# tres fichas y 260 <use>: el archivo queda corto y el dibujo es el mismo
w('<defs>')
w(f'<circle id="v" r="{r}" fill="none" stroke="{GRIS}" stroke-width="1.1"/>')
w(f'<circle id="m" r="{r}" fill="{ROJO}"/>')
w(f'<g id="d"><circle r="{r}" fill="{ROJO}"/><circle r="{r + 3}" fill="none" stroke="{ROJO}" stroke-width="1.4"/></g>')
w('</defs>')
n = 0
for f in range(filas):
    fila = []
    for c in range(cols):
        cx = gx + c * paso + paso / 2
        cy = gy + f * paso + paso / 2
        ficha = "d" if n < 5 else ("m" if n < 12 else "v")
        fila.append(f'<use href="#{ficha}" x="{cx:.1f}" y="{cy:.1f}"/>')
        n += 1
    w("".join(fila))
ly = gy + filas * paso + 28
w(f'<circle cx="{x0 + 8}" cy="{ly}" r="{r}" fill="{ROJO}"/>')
w(f'<text x="{x0 + 22}" y="{ly + 4}" font-size="12.5" fill="{TINTA}">12 apretaron la mano después de la intubación (4,6 %)</text>')
w(f'<circle cx="{x0 + 8}" cy="{ly + 24}" r="{r}" fill="{ROJO}"/><circle cx="{x0 + 8}" cy="{ly + 24}" r="{r + 3}" fill="none" stroke="{ROJO}" stroke-width="1.4"/>')
w(f'<text x="{x0 + 22}" y="{ly + 28}" font-size="12.5" fill="{TINTA}">5 de esos 12 dijeron, con la mano, que les dolía</text>')
w(f'<circle cx="{x0 + 8}" cy="{ly + 48}" r="{r}" fill="none" stroke="{GRIS}" stroke-width="1.1"/>')
w(f'<text x="{x0 + 22}" y="{ly + 52}" font-size="12.5" fill="{TINTA}">248 no contestaron</text>')
w(f'<text x="{x0}" y="{ly + 84}" font-size="13" fill="{TINTA}">Después de la operación se les preguntó a 253 qué recordaban.</text>')
w(f'<text x="{x0}" y="{ly + 104}" font-size="13" fill="{TINTA}">Ninguno recordaba nada. (Siete no fueron entrevistados;</text>')
w(f'<text x="{x0}" y="{ly + 122}" font-size="13" fill="{TINTA}">el resumen no dice si alguno de los doce está entre ellos.)</text>')

# pie
w(f'<text x="30" y="{H - 16}" font-size="11" fill="{GRIS}">Cuaderno de tiempo libre, 16/10/2026. Panel A: esquema, no a escala. Panel B: Sanders RD y otros, Anesthesiology 126(2):214-222, 2017.</text>')
w('</svg>')

svg = "\n".join(out) + "\n"
Path("antebrazo_aislado.svg").write_text(svg, encoding="utf-8")
print("escrito antebrazo_aislado.svg")
try:
    import cairosvg  # type: ignore
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to="antebrazo_aislado.png", output_width=1800)
    print("escrito antebrazo_aislado.png")
except ImportError:
    print("sin cairosvg: no se escribe el PNG")
