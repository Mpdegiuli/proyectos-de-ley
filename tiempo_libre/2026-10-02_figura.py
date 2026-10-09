#!/usr/bin/env python3
"""Dibuja dos_costas.svg: la isla Sandy tal como estaba en GSHHS 2.2.0 (217
puntos) y, a la misma escala, lo que Natural Earth dibuja donde están las rocas
Cormorán. Necesita sandy_contorno.txt, sandy_10_puntos.txt y sandy_5_puntos.txt
(los escribe sandy.py) y ne/ne_10m_minor_islands.* (ver datos.sh).
pip install numpy pyshp
"""
import math
import numpy as np
import shapefile

KM = 111.195            # km por grado de latitud
E = 12.0                # px por km en los paneles a escala
a = np.loadtxt('sandy_contorno.txt')
p10 = np.loadtxt('sandy_10_puntos.txt')
p5 = np.loadtxt('sandy_5_puntos.txt')
latc = (a[:, 1].min() + a[:, 1].max()) / 2
lonc = (a[:, 0].min() + a[:, 0].max()) / 2
COS = math.cos(math.radians(latc))

def km(pts, lon0=lonc, lat0=latc, cos=COS):
    """a kilómetros desde un centro, con el norte hacia arriba (y negativa)"""
    return [((lo - lon0) * KM * cos, -(la - lat0) * KM) for lo, la in pts]

def camino(xy, dec=2):
    return "M" + " L".join(f"{x:.{dec}f},{y:.{dec}f}" for x, y in xy) + "Z"

W, H = 960, 600
MAR, TIERRA, TINTA, ROJO = "#dfe8ec", "#c9b68c", "#22313a", "#b23a2e"
o = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif" font-size="11" fill="{TINTA}">',
     f'<rect width="{W}" height="{H}" fill="#f4f1ea"/>',
     f'<defs><path id="isla" d="{camino(km(a))}"/></defs>']

def texto(x, y, s, extra=""):
    return f'<text x="{x:.0f}" y="{y:.0f}" {extra}>{s}</text>'

def escala(x, y, largo_px, rot):
    return (f'<line x1="{x}" y1="{y}" x2="{x + largo_px:.1f}" y2="{y}" stroke="{TINTA}" stroke-width="2"/>'
            + texto(x, y - 6, rot))

# ---------- panel A: Sandy entera
ax, ay, aw, ah = 30, 70, 170, 440
cx, cy = ax + aw / 2, ay + ah / 2
o.append(f'<rect x="{ax}" y="{ay}" width="{aw}" height="{ah}" fill="{MAR}"/>')
o.append(f'<use xlink:href="#isla" transform="translate({cx},{cy}) scale({E})" fill="{TIERRA}" stroke="{TINTA}" stroke-width="{0.8 / E:.3f}"/>')
o.append(texto(ax, ay - 34, "La isla Sandy", 'font-size="15" font-weight="bold"'))
o.append(texto(ax, ay - 14, "GSHHS 2.2.0, polígono 1203", 'font-size="12"'))
o.append(escala(ax + 16, ay + ah - 22, 5 * E, "5 km"))
o.append(texto(ax + 8, ay + 16, "27,7 km"))
o.append(texto(ax + aw - 8, ay + 16, "19°06'S", 'text-anchor="end"'))
o.append(texto(ax + aw - 8, ay + ah - 8, "19°21'S", 'text-anchor="end"'))
zlat0, zlat1, zlon0, zlon1 = -19.135, -19.102, 159.917, 159.952
(x1, y1), (x2, y2) = km([(zlon0, zlat1), (zlon1, zlat0)])
o.append(f'<rect x="{cx + x1 * E:.1f}" y="{cy + y1 * E:.1f}" width="{(x2 - x1) * E:.1f}" height="{(y2 - y1) * E:.1f}" fill="none" stroke="{ROJO}" stroke-width="1.2"/>')

# ---------- panel B: la punta norte, con la grilla de 3 segundos de arco
bx, by, bw, bh = 230, 70, 280, 280
EZ = bw / (x2 - x1)
zx, zy = (x1 + x2) / 2, (y1 + y2) / 2          # centro del recuadro, en km
tx, ty = bx + bw / 2 - zx * EZ, by + bh / 2 - zy * EZ
paso = 1 / 1200
gx, gy = paso * KM * COS * EZ, paso * KM * EZ   # celda de la grilla, en px
(ox, oy), = km([(math.floor(zlon0 / paso) * paso, math.ceil(zlat1 / paso) * paso)])
o.append(f'<clipPath id="cb"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}"/></clipPath>')
o.append(f'<pattern id="gr" patternUnits="userSpaceOnUse" x="{tx + ox * EZ:.2f}" y="{ty + oy * EZ:.2f}" width="{gx:.3f}" height="{gy:.3f}">'
         f'<path d="M0,0 H{gx:.3f} M0,0 V{gy:.3f}" stroke="#ffffff" stroke-width="0.6" fill="none"/></pattern>')
o.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="{MAR}"/>')
o.append('<g clip-path="url(#cb)">')
o.append(f'<use xlink:href="#isla" transform="translate({tx:.2f},{ty:.2f}) scale({EZ:.3f})" fill="{TIERRA}"/>')
o.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="url(#gr)" opacity="0.7"/>')
o.append(f'<use xlink:href="#isla" transform="translate({tx:.2f},{ty:.2f}) scale({EZ:.3f})" fill="none" stroke="{TINTA}" stroke-width="{1.4 / EZ:.4f}"/>')
for (x, y), (lo, la) in zip(km(a), a):
    if zlon0 - 0.002 < lo < zlon1 + 0.002 and zlat0 - 0.002 < la < zlat1 + 0.002:
        o.append(f'<circle cx="{tx + x * EZ:.1f}" cy="{ty + y * EZ:.1f}" r="2.2" fill="{ROJO}"/>')
o.append('</g>')
o.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="none" stroke="{ROJO}" stroke-width="1.2"/>')
o.append(texto(bx, by - 34, "La punta norte, de cerca", 'font-size="15" font-weight="bold"'))
o.append(texto(bx, by - 14, "grilla de 3 segundos de arco (unos 90 m)", 'font-size="12"'))
o.append(escala(bx + 14, by + bh - 16, 0.5 * EZ, "500 m"))

# ---------- las tres resoluciones
E2 = 5.0
o.append(texto(bx, by + bh + 28, "La misma isla en las tres resoluciones del archivo", 'font-size="12"'))
for j, (pts, rot) in enumerate(((None, "217 puntos"), (p10, "10 puntos"), (p5, "5 puntos"))):
    x0 = bx + 45 + j * 95; y0 = by + bh + 115
    if pts is None:
        o.append(f'<use xlink:href="#isla" transform="translate({x0},{y0}) scale({E2})" fill="{TIERRA}" stroke="{TINTA}" stroke-width="{0.8 / E2:.2f}"/>')
    else:
        o.append(f'<path d="{camino(km(pts))}" transform="translate({x0},{y0}) scale({E2})" fill="{TIERRA}" stroke="{TINTA}" stroke-width="{0.8 / E2:.2f}"/>')
    o.append(texto(x0, y0 + 86, rot, 'text-anchor="middle"'))

# ---------- panel C: las rocas Cormorán, a la misma escala que el panel A
px, py, pw, ph = 540, 70, 390, 440
clat, clon = -53.555, -41.925
ccos = math.cos(math.radians(clat))
ccx, ccy = px + pw / 2, py + ph / 2
o.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="{MAR}"/>')
sf = shapefile.Reader('ne/ne_10m_minor_islands')
for s in sf.shapes():
    b = s.bbox
    if -54.2 < b[1] and b[3] < -53.0 and -43 < b[0] and b[2] < -41:
        o.append(f'<path d="{camino(km(s.points, clon, clat, ccos))}" transform="translate({ccx},{ccy}) scale({E})" fill="{TIERRA}" stroke="{TINTA}" stroke-width="{0.8 / E:.3f}"/>')
def cruz(lat, lon, rot):
    (x, y), = km([(lon, lat)], clon, clat, ccos)
    x, y = ccx + x * E, ccy + y * E
    return (f'<path d="M{x - 6:.1f},{y:.1f} H{x + 6:.1f} M{x:.1f},{y - 6:.1f} V{y + 6:.1f}" stroke="{ROJO}" stroke-width="1.6"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{0.25 * E:.1f}" fill="{ROJO}"/>' + texto(x + 10, y + 4, rot, f'fill="{ROJO}"'))
o.append(cruz(-(53 + 33 / 60), -(42 + 2 / 60 + 22 / 3600), "rocas Cormorán"))
o.append(cruz(-(53 + 39 / 60 + 7 / 3600), -(41 + 48 / 60 + 1 / 3600), "roca Negra"))
o.append(texto(px, py - 34, "Las rocas Cormorán", 'font-size="15" font-weight="bold"'))
o.append(texto(px, py - 14, "misma escala que la isla Sandy", 'font-size="12"'))
o.append(texto(px + 12, py + ph - 58, "en color arena: lo que dibuja Natural Earth"))
o.append(texto(px + 12, py + ph - 42, "en rojo: dónde están (el punto mide 500 m)", f'fill="{ROJO}"'))
o.append(texto(px + 12, py + ph - 26, "GSHHS, en 2012 y hoy: nada"))
o.append(escala(px + 16, py + 26, 5 * E, "5 km"))
o.append(texto(30, H - 14, "Izquierda: una isla que no existe, con 217 puntos de costa. Derecha: unas rocas que existen. Datos: basemap 1.0.7 (GSHHS 2.2.0) y Natural Earth 1:10m."))
o.append('</svg>')
open('dos_costas.svg', 'w').write("\n".join(o) + "\n")
print('escrito dos_costas.svg,', len("\n".join(o)) + 1, 'bytes')
