#!/usr/bin/env python3
"""Figura del cuaderno "Diez a la veintitrés" (tiempo libre, 23/10/2026).

Escribe `veintitres.svg`: tres paneles.
  A. Las primeras cuentas de N (1865-1917), en unidades de 10^23.
  B. Los valores recomendados (CODATA 1998-2014), dos medidas con esferas de silicio
     (2011, 2015) y el valor fijado en 2019, como apartamiento del valor fijado, en
     partes por diez millones.
  C. Cuántos moles son 12 g de carbono 12 según CODATA 2018 y 2022, como apartamiento
     de un mol en partes en 10^10. Hasta el 20/5/2019 era exactamente uno, por definición.

Datos: ver el cuaderno (fuentes al pie). Solo biblioteca estándar.
Colores: paleta de referencia de la guía de visualización (azul #2a78d6 para la serie,
naranja #eb6834 para la referencia), texto en gris; sin color como único portador.
"""

AZUL, NARANJA = "#2a78d6", "#eb6834"
TINTA, TINTA2, GRIS = "#0b0b0b", "#52514e", "#d9d8d3"
FUENTE = "font-family='Helvetica, Arial, sans-serif'"

# A. primeras cuentas (año, valor ×10^23, etiqueta, hueco si es derivado y no publicado como N)
A = [
    (1865, 0.4,   "Loschmidt (derivado de su diámetro)", True),
    (1873, 4.2,   "Maxwell", False),
    (1900, 6.175, "Planck (cuerpo negro)", False),
    (1905, 2.1,   "Einstein (tesis, con un error de álgebra)", False),
    (1908, 7.05,  "Perrin (emulsiones)", False),
    (1909, 6.2,   "Perrin (van der Waals)", False),
    (1911, 6.6,   "Einstein (corregido)", False),
    (1917, 6.064, "Millikan (carga del electrón)", False),
]
A_RANGO = (1913, 6.0, 7.5, "1913 Perrin, Les Atomes: 13 métodos, de 6,0 a 7,5")

# B. valores recomendados y medidas (año, valor ×10^23, u ×10^23, etiqueta)
FIJO = 6.02214076
B = [
    (1998, 6.02214199, 0.00000047, "CODATA 1998"),
    (2006, 6.02214179, 0.00000030, "CODATA 2006"),
    (2010, 6.02214129, 0.00000027, "CODATA 2010"),
    (2011, 6.02214084, 0.00000018, "esferas de Si-28 (Andreas 2011)"),
    (2014, 6.022140857, 0.000000074, "CODATA 2014"),
    (2015, 6.02214076, 0.00000012, "esferas de Si-28 (Azuma 2015)"),
]

# C. 12 g de C-12 en moles, menos uno, en partes en 10^10 (y su incertidumbre)
C = [
    ("CODATA 2018", 12 / 11.9999999958 - 1, 3.6e-9 / 12),
    ("CODATA 2022", 12 / 12.0000000126 - 1, 3.7e-9 / 12),
]

W, H = 980, 1180
out = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}' {FUENTE}>",
       f"<rect width='{W}' height='{H}' fill='#fcfcfb'/>",
       f"<text x='40' y='44' font-size='22' fill='{TINTA}'>Cuántas cosas hay en un mol: ciento cincuenta años de contar sin contar</text>",
       f"<text x='40' y='68' font-size='13' fill='{TINTA2}'>Tiempo libre, 23/10/2026. Tres paneles, tres escalas; los datos y las fuentes están en el cuaderno.</text>"]

def texto(x, y, s, size=12, fill=TINTA2, anchor="start", extra=""):
    out.append(f"<text x='{x:.1f}' y='{y:.1f}' font-size='{size}' fill='{fill}' text-anchor='{anchor}' {extra}>{s}</text>")

# ---------- Panel A ----------
ax, ay, aw, ah = 70, 110, 860, 300
x0, x1 = 1860, 1922
y0, y1 = 0, 8
def XA(t): return ax + (t - x0) / (x1 - x0) * aw
def YA(v): return ay + ah - (v - y0) / (y1 - y0) * ah
texto(ax, ay - 14, "A. Las primeras cuentas de N, en unidades de 10<tspan font-size='9' baseline-shift='super'>23</tspan> por mol", 14, TINTA)
for v in range(0, 9, 2):
    out.append(f"<line x1='{ax}' y1='{YA(v):.1f}' x2='{ax+aw}' y2='{YA(v):.1f}' stroke='{GRIS}' stroke-width='1'/>")
    texto(ax - 8, YA(v) + 4, str(v), 11, TINTA2, "end")
for t in range(1860, 1921, 10):
    texto(XA(t), ay + ah + 18, str(t), 11, TINTA2, "middle")
# valor fijado en 2019, como referencia
out.append(f"<line x1='{ax}' y1='{YA(FIJO):.1f}' x2='{ax+aw}' y2='{YA(FIJO):.1f}' stroke='{NARANJA}' stroke-width='2' stroke-dasharray='6 4'/>")
texto(ax + 6, YA(FIJO) - 7, "6,02214076 × 10<tspan font-size='8' baseline-shift='super'>23</tspan>, el valor fijado en 2019", 11, TINTA2, "start")
# rango de Perrin 1913
t, lo, hi, et = A_RANGO
out.append(f"<rect x='{XA(t)-5:.1f}' y='{YA(hi):.1f}' width='10' height='{YA(lo)-YA(hi):.1f}' rx='4' fill='{AZUL}' fill-opacity='0.35'/>")
texto(XA(t) - 10, YA(hi) - 9, et, 11, TINTA2, 'end')
for t, v, et, hueco in A:
    fill = "#fcfcfb" if hueco else AZUL
    out.append(f"<circle cx='{XA(t):.1f}' cy='{YA(v):.1f}' r='5' fill='{fill}' stroke='{AZUL}' stroke-width='2'/>")
    dx, dy, anchor = 9, 4, "start"
    if t == 1908: dy, anchor, dx = -8, "end", -9
    if t == 1909: dy, anchor, dx = 18, "end", -9
    if t == 1917: dy, anchor, dx = 36, "end", -9
    if t == 1911: dx, dy = (XA(1913) - XA(1911)) + 12, 4   # a la derecha de la barra de 1913
    if t == 1900: dy, anchor, dx = -10, "end", -9
    texto(XA(t) + dx, YA(v) + dy, f"{t} {et}", 11, TINTA2, anchor)
texto(ax, ay + ah + 40, "Punto hueco: valor derivado de los datos de Loschmidt; las fuentes no coinciden en si él mismo publicó el número.", 11, TINTA2)

# ---------- Panel B ----------
bx, by, bw, bh = 70, 490, 860, 270
x0, x1 = 1996, 2021
y0, y1 = -0.6, 3.0        # partes por 10^7 respecto del valor fijado
def XB(t): return bx + (t - x0) / (x1 - x0) * bw
def YB(v): return by + bh - (v - y0) / (y1 - y0) * bh
texto(bx, by - 14, "B. Lo mismo, de cerca: apartamiento del valor fijado, en partes por diez millones", 14, TINTA)
for v in [-0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3]:
    out.append(f"<line x1='{bx}' y1='{YB(v):.1f}' x2='{bx+bw}' y2='{YB(v):.1f}' stroke='{GRIS}' stroke-width='1'/>")
    texto(bx - 8, YB(v) + 4, f"{v:+.1f}".replace(".", ",").replace("+0,0", "0"), 11, TINTA2, "end")
for t in range(1998, 2021, 2):
    texto(XB(t), by + bh + 18, str(t), 11, TINTA2, "middle")
out.append(f"<line x1='{bx}' y1='{YB(0):.1f}' x2='{bx+bw}' y2='{YB(0):.1f}' stroke='{NARANJA}' stroke-width='2' stroke-dasharray='6 4'/>")
for t, v, u, et in B:
    d = (v - FIJO) / FIJO * 1e7
    ud = u / FIJO * 1e7
    out.append(f"<line x1='{XB(t):.1f}' y1='{YB(d-ud):.1f}' x2='{XB(t):.1f}' y2='{YB(d+ud):.1f}' stroke='{AZUL}' stroke-width='2'/>")
    out.append(f"<circle cx='{XB(t):.1f}' cy='{YB(d):.1f}' r='5' fill='{AZUL}'/>")
    anchor, dx, dy = "start", 9, 16
    if t == 2011: anchor, dx, dy = "end", -9, -10
    if t == 2014: anchor, dx, dy = "start", 9, -10
    if t == 2015: anchor, dx, dy = "end", -9, 24
    texto(XB(t) + dx, YB(d) + dy, et, 11, TINTA2, anchor)
# 2019: valor fijado
out.append(f"<circle cx='{XB(2019):.1f}' cy='{YB(0):.1f}' r='6' fill='{NARANJA}'/>")
texto(XB(2019), YB(0) - 12, "20/5/2019: fijado, sin incertidumbre", 11, TINTA2, "middle")
texto(bx, by + bh + 40, "Barras: una incertidumbre estándar. Entre 1998 y 2019 el valor recomendado bajó dos partes por diez millones.", 11, TINTA2)

# ---------- Panel C ----------
cx, cy, cw, ch = 70, 840, 860, 230
texto(cx, cy - 14, "C. ¿Cuántos moles son 12 gramos de carbono 12? Apartamiento de un mol, en partes en 10<tspan font-size='9' baseline-shift='super'>10</tspan>", 14, TINTA)
y0, y1 = -16, 10
def YC(v): return cy + ch - (v - y0) / (y1 - y0) * ch
for v in range(-15, 11, 5):
    out.append(f"<line x1='{cx}' y1='{YC(v):.1f}' x2='{cx+cw}' y2='{YC(v):.1f}' stroke='{GRIS}' stroke-width='1'/>")
    texto(cx - 8, YC(v) + 4, f"{v:+d}".replace("+0", "0"), 11, TINTA2, "end")
out.append(f"<line x1='{cx}' y1='{YC(0):.1f}' x2='{cx+cw}' y2='{YC(0):.1f}' stroke='{NARANJA}' stroke-width='2' stroke-dasharray='6 4'/>")
texto(cx + cw, YC(0) - 7, "exactamente un mol: la definición de 1971 a 2019", 11, TINTA2, "end")
cols = [cx + cw * 0.3, cx + cw * 0.7]
for (et, d, u), X in zip(C, cols):
    d10, u10 = d * 1e10, u * 1e10
    out.append(f"<line x1='{X:.1f}' y1='{YC(d10-u10):.1f}' x2='{X:.1f}' y2='{YC(d10+u10):.1f}' stroke='{AZUL}' stroke-width='2'/>")
    out.append(f"<line x1='{X-8:.1f}' y1='{YC(d10-u10):.1f}' x2='{X+8:.1f}' y2='{YC(d10-u10):.1f}' stroke='{AZUL}' stroke-width='2'/>")
    out.append(f"<line x1='{X-8:.1f}' y1='{YC(d10+u10):.1f}' x2='{X+8:.1f}' y2='{YC(d10+u10):.1f}' stroke='{AZUL}' stroke-width='2'/>")
    out.append(f"<circle cx='{X:.1f}' cy='{YC(d10):.1f}' r='6' fill='{AZUL}'/>")
    texto(X, cy + ch + 18, et, 12, TINTA, "middle")
    signo = "+" if d10 > 0 else "−"
    texto(X + 14, YC(d10) + 4, f"{signo}{abs(d10):.1f} ± {u10:.1f}  ({'sobran' if d10>0 else 'faltan'} {abs(d)*6.02214076e23:.1e} átomos)".replace(".", ",").replace("e+14", " × 10^14"), 11, TINTA2)
texto(cx, cy + ch + 42, "El carbono no cambió entre 2018 y 2022: cambió el valor recomendado de la constante de estructura fina, y con él la masa molar.", 11, TINTA2)
texto(cx, cy + ch + 60, "Fuentes: NIST, listados CODATA 1998-2022; Azuma et al. 2015; Andreas et al. 2011; Perrin 1909 y 1926; Knowino para 1865-1917 (ver el cuaderno).", 10, TINTA2)

out.append("</svg>")
with open("veintitres.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("veintitres.svg escrito,", sum(len(s) for s in out), "caracteres")
