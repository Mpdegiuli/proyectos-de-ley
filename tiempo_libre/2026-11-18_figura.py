#!/usr/bin/env python3
"""Dibuja `ventanas.svg`: el diagrama de ventanas de Schenker (1960, fig. 5) rehecho con
las cuentas de hoy, y debajo los ocho tonos sobre una regla de semitonos.

Arriba: ejes logarítmicos, tono grave (filas) en x y tono agudo (columnas) en y. Cada tecla
es un cuadrado de ±2 % (la ventana de reconocimiento del artículo). Las diagonales son los
pares de frecuencias en razón 1:2, 2:3, 3:4, 3:5, 4:5 y 5:6, que son las que una vocal
produce con sus armónicos y que el código quiso esquivar. En gris punteado, la columna de
1.094 Hz que el artículo de 1960 tenía y el estándar de 1963 no.

Abajo: los ocho tonos (y el 1.094) sobre una regla donde cada raya es un semitono del piano
(La4 = 440 Hz); se ve que el paso del teclado, 21:19, no es ni un semitono ni un tono.

No lee nada del repositorio. Uso: python3 figura.py > ventanas.svg
"""
import math

FILAS = [697, 770, 852, 941]
COLS = [1209, 1336, 1477, 1633]
TECLAS = [["1", "2", "3", "A"], ["4", "5", "6", "B"], ["7", "8", "9", "C"], ["*", "0", "#", "D"]]
DIAG = [("1:2", 2.0), ("2:3", 1.5), ("3:4", 4 / 3), ("3:5", 5 / 3), ("4:5", 1.25), ("5:6", 1.2)]
NOMBRES = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]

W, H = 760, 900
# panel de arriba
X0, X1, Y0, Y1 = 90, 700, 40, 540
FX0, FX1 = 640.0, 1010.0   # Hz en x
FY0, FY1 = 1000.0, 1760.0  # Hz en y


def px(f):
    return X0 + (X1 - X0) * (math.log(f) - math.log(FX0)) / (math.log(FX1) - math.log(FX0))


def py(f):
    return Y1 - (Y1 - Y0) * (math.log(f) - math.log(FY0)) / (math.log(FY1) - math.log(FY0))


out = []
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
out.append(f'<rect width="{W}" height="{H}" fill="white"/>')
out.append(f'<text x="{X0}" y="24" font-size="15">Las dieciséis ventanas del teclado y las diagonales que esquivan (según Schenker, 1960)</text>')
# marco
out.append(f'<rect x="{X0}" y="{Y0}" width="{X1-X0}" height="{Y1-Y0}" fill="none" stroke="#333"/>')
# diagonales: y = r x, recortadas al marco
for nombre, r in DIAG:
    pts = []
    for fx in (FX0, FX1):
        fy = r * fx
        pts.append((fx, fy))
    # recortar a [FY0, FY1]
    (ax, ay), (bx, by) = pts
    if ay < FY0:
        ax, ay = FY0 / r, FY0
    if by > FY1:
        bx, by = FY1 / r, FY1
    if ay > FY1 or by < FY0:
        continue
    out.append(f'<line x1="{px(ax):.1f}" y1="{py(ay):.1f}" x2="{px(bx):.1f}" y2="{py(by):.1f}" stroke="#b33" stroke-width="1"/>')
    # etiqueta en el extremo alto
    lx, ly = px(bx), py(by)
    out.append(f'<text x="{lx+3:.1f}" y="{ly-3:.1f}" fill="#b33" font-size="11">{nombre}</text>')
# ventanas
for i, fr in enumerate(FILAS):
    for j, fc in enumerate(COLS):
        x_a, x_b = px(fr * 0.98), px(fr * 1.02)
        y_a, y_b = py(fc * 1.02), py(fc * 0.98)
        out.append(f'<rect x="{x_a:.1f}" y="{y_a:.1f}" width="{x_b-x_a:.1f}" height="{y_b-y_a:.1f}" fill="#dde8f5" stroke="#235" stroke-width="1.2"/>')
        # rectángulo mayor ±(2 % + 10 Hz), el de extremo a extremo
        x_c, x_d = px(fr * 0.98 - 10), px(fr * 1.02 + 10)
        y_c, y_d = py(fc * 1.02 + 10), py(fc * 0.98 - 10)
        out.append(f'<rect x="{x_c:.1f}" y="{y_c:.1f}" width="{x_d-x_c:.1f}" height="{y_d-y_c:.1f}" fill="none" stroke="#235" stroke-width="0.6" stroke-dasharray="2,2"/>')
        out.append(f'<text x="{px(fr):.1f}" y="{py(fc)+4:.1f}" text-anchor="middle" font-size="12" font-weight="bold" fill="#123">{TECLAS[i][j]}</text>')
# columna de 1094 (1960), punteada
for i, fr in enumerate(FILAS):
    fc = 1094
    x_a, x_b = px(fr * 0.98), px(fr * 1.02)
    y_a, y_b = py(fc * 1.02), py(fc * 0.98)
    out.append(f'<rect x="{x_a:.1f}" y="{y_a:.1f}" width="{x_b-x_a:.1f}" height="{y_b-y_a:.1f}" fill="none" stroke="#888" stroke-width="1" stroke-dasharray="3,2"/>')
out.append(f'<text x="{px(FX0*1.01):.1f}" y="{py(1094)+34:.1f}" font-size="10" fill="#666">columna de 1.094 Hz del artículo de 1960 (punteado gris)</text>')
# ejes
for f in FILAS:
    out.append(f'<line x1="{px(f):.1f}" y1="{Y1}" x2="{px(f):.1f}" y2="{Y1+5}" stroke="#333"/>')
    out.append(f'<text x="{px(f):.1f}" y="{Y1+18}" text-anchor="middle">{f}</text>')
for f in COLS + [1094]:
    out.append(f'<line x1="{X0-5}" y1="{py(f):.1f}" x2="{X0}" y2="{py(f):.1f}" stroke="#333"/>')
    out.append(f'<text x="{X0-8}" y="{py(f)+4:.1f}" text-anchor="end">{f}</text>')
out.append(f'<text x="{(X0+X1)/2:.0f}" y="{Y1+36}" text-anchor="middle">tono grave (filas), Hz, escala logarítmica</text>')
out.append(f'<text x="22" y="{(Y0+Y1)/2:.0f}" text-anchor="middle" transform="rotate(-90 22 {(Y0+Y1)/2:.0f})">tono agudo (columnas), Hz</text>')
out.append(f'<text x="{X0}" y="{Y1+56}" font-size="11" fill="#444">Cuadrado: ventana de ±2 %. Punteado: ±(2 % + 10 Hz), la del extremo a extremo.</text>')
out.append(f'<text x="{X0}" y="{Y1+72}" font-size="11" fill="#444">Rojo: pares de frecuencias en razón simple, los que forman los armónicos de una vocal.</text>')

# panel de abajo: regla de semitonos
RY = 720
RX0, RX1 = 90, 700
RF0, RF1 = 650.0, 1750.0


def rx(f):
    return RX0 + (RX1 - RX0) * (math.log(f) - math.log(RF0)) / (math.log(RF1) - math.log(RF0))


out.append(f'<text x="{RX0}" y="{RY-62}" font-size="15">Los ocho tonos sobre la escala del piano</text>')
out.append(f'<line x1="{RX0}" y1="{RY}" x2="{RX1}" y2="{RY}" stroke="#333"/>')
n0 = math.ceil(12 * math.log2(RF0 / 440))
n1 = math.floor(12 * math.log2(RF1 / 440))
for n in range(n0, n1 + 1):
    f = 440 * 2 ** (n / 12)
    idx = (n + 9) % 12
    octava = 4 + (n + 9) // 12
    negra = "#" in NOMBRES[idx]
    out.append(f'<line x1="{rx(f):.1f}" y1="{RY}" x2="{rx(f):.1f}" y2="{RY+ (10 if negra else 16)}" stroke="#333" stroke-width="{0.8 if negra else 1.2}"/>')
    if not negra:
        out.append(f'<text x="{rx(f):.1f}" y="{RY+30}" text-anchor="middle" font-size="10">{NOMBRES[idx]}{octava}</text>')
for f in FILAS + COLS:
    out.append(f'<line x1="{rx(f):.1f}" y1="{RY-34}" x2="{rx(f):.1f}" y2="{RY}" stroke="#235" stroke-width="2"/>')
    out.append(f'<text x="{rx(f):.1f}" y="{RY-38}" text-anchor="middle" font-size="10" fill="#235">{f}</text>')
out.append(f'<line x1="{rx(1094):.1f}" y1="{RY-26}" x2="{rx(1094):.1f}" y2="{RY}" stroke="#888" stroke-width="1.5" stroke-dasharray="3,2"/>')
out.append(f'<text x="{rx(1094):.1f}" y="{RY-30}" text-anchor="middle" font-size="10" fill="#777">1094</text>')
# llaves de 21:19
out.append(f'<text x="{RX0}" y="{RY+60}" font-size="11" fill="#444">Cada raya de la regla es un semitono (100 cents). El paso entre tonos vecinos del teclado es 21:19, 173 cents:</text>')
out.append(f'<text x="{RX0}" y="{RY+76}" font-size="11" fill="#444">ni un semitono ni un tono. Solo dos tonos caen sobre una tecla del piano, 697 (Fa5) y 1.477 (Fa#6), a 4 cents;</text>')
out.append(f'<text x="{RX0}" y="{RY+92}" font-size="11" fill="#444">los otros seis quedan entre dos teclas.</text>')
out.append(f'<text x="{RX0}" y="{RY+124}" font-size="11" fill="#777">Cuentas: teclado.py. Ventanas y diagonales: L. Schenker, "Pushbutton Calling with a Two-Group</text>')
out.append(f'<text x="{RX0}" y="{RY+140}" font-size="11" fill="#777">Voice-Frequency Code", Bell System Technical Journal 39(1), enero de 1960, fig. 5.</text>')
out.append("</svg>")
print("\n".join(out))
