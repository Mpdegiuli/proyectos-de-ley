#!/usr/bin/env python3
"""Arma `hoja.svg` con los seis teléfonos de las instancias frescas (dibujo_1.svg a dibujo_6.svg),
o `hoja_control.svg` con los seis del control (control_1.svg a control_6.svg), y cuenta en cada
uno lo que se puede contar sin mirar: dígitos sueltos dibujados (un <text> con un solo dígito),
si el código nombra "tecla"/"button", qué número de abonado aparece, y las horas y fechas que
haya escritas (hh:mm, "18 de noviembre"). Lo demás (color, disco, tope, cable) se leyó a mano y
está en instancias_frescas.md.

Uso: python3 hoja.py [dibujo|control]  (escribe hoja.svg o hoja_control.svg y su salida_*.txt)
"""
import os
import re
import sys

PREFIJO = sys.argv[1] if len(sys.argv) > 1 else "dibujo"
N = 6
if PREFIJO == "dibujo":
    ANCHO, ALTO, COLS, SALIDA = 400, 330, 3, "hoja"
else:
    ANCHO, ALTO, COLS, SALIDA = 240, 480, 6, "hoja_control"
PAD = 20

partes = []
FILAS_HOJA = (N + COLS - 1) // COLS
partes.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{COLS*(ANCHO+PAD)+PAD}" height="{FILAS_HOJA*(ALTO+PAD+24)+PAD}" font-family="Helvetica, Arial, sans-serif" font-size="13">')
partes.append('<rect width="100%" height="100%" fill="white"/>')
lineas = []
for k in range(1, N + 1):
    nombre = f"{PREFIJO}_{k}.svg"
    if not os.path.exists(nombre):  # en tiempo_libre/ los archivos llevan la fecha adelante
        nombre = f"2026-11-18_{nombre}"
    src = open(nombre, encoding="utf-8").read()
    inner = re.sub(r"^.*?<svg[^>]*>", "", src, count=1, flags=re.S)
    inner = re.sub(r"</svg>\s*$", "", inner, flags=re.S)
    # ids de degradados: hacerlos únicos por dibujo para que no se pisen en la hoja (error del 30/9)
    for ident in set(re.findall(r'id="([^"]+)"', inner)):
        inner = inner.replace(f'id="{ident}"', f'id="d{k}_{ident}"').replace(f'url(#{ident})', f'url(#d{k}_{ident})')
    vb = re.search(r'viewBox="([^"]+)"', src)
    vbw, vbh = (float(v) for v in vb.group(1).split()[2:4]) if vb else (400, 320)
    col, fila = (k - 1) % COLS, (k - 1) // COLS
    x = PAD + col * (ANCHO + PAD)
    y = PAD + fila * (ALTO + PAD + 24)
    esc = min(ANCHO / vbw, ALTO / vbh)
    partes.append(f'<text x="{x}" y="{y+14}">{"instancia" if PREFIJO == "dibujo" else "control"} {k}</text>')
    partes.append(f'<g transform="translate({x},{y+20}) scale({esc:.4f})">{inner}</g>')
    digitos = re.findall(r'<circle[^>]*/>\s*<text[^>]*>(\d)</text>', src)
    if not digitos:
        # agujeros y números en grupos separados: contar <text> con un solo dígito
        digitos = re.findall(r'<text[^>]*>(\d)</text>', src)
    numero = re.findall(r'>(\d{2,3}-\d{4})<', src)
    teclas = bool(re.search(r'tecla|button|keypad', src, re.I))
    horas = re.findall(r'>(\d{1,2}:\d{2})<', src)
    fechas = re.findall(r'>([^<]*\d{1,2} de [a-z]+)<', src, re.I)
    lineas.append(f"{PREFIJO} {k}: {len(digitos)} dígitos sueltos ({''.join(digitos)}); palabra tecla/button: {'sí' if teclas else 'no'}; número escrito: {numero[0] if numero else '—'}; horas: {', '.join(horas) if horas else '—'}; fecha: {fechas[0].strip() if fechas else '—'}; bytes: {len(src.encode())}")
partes.append("</svg>")
open(f"{SALIDA}.svg", "w", encoding="utf-8").write("\n".join(partes))
open(f"salida_{SALIDA}.txt", "w", encoding="utf-8").write("\n".join(lineas) + "\n")
print("\n".join(lineas))
