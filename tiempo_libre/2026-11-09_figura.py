#!/usr/bin/env python3
"""Lee cascada.json y escribe cascada.svg: la curva del margen (A), el mapa de la
cascada con alfa = 0,2 (qué línea cayó en qué paso) y la media hora de 1965."""
import json
import math

with open("cascada.json") as fh:
    D = json.load(fh)

W, H = 1440, 540
out = []
p = out.append
p(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
  f'font-family="Helvetica, Arial, sans-serif" font-size="13">')
p('<rect width="100%" height="100%" fill="#fbfaf6"/>')

# --- Panel A: curva ---
ax, ay, aw, ah = 60, 60, 340, 320
res = D["A"]["resultados"]
p(f'<text x="{ax}" y="28" font-size="15" font-weight="bold">A. Se abre la línea más cargada: qué cae, según el margen</text>')
p(f'<rect x="{ax}" y="{ay}" width="{aw}" height="{ah}" fill="none" stroke="#999"/>')
for frac in (0, 0.25, 0.5, 0.75, 1.0):
    y = ay + ah - frac * ah
    p(f'<line x1="{ax}" y1="{y:.1f}" x2="{ax+aw}" y2="{y:.1f}" stroke="#e5e2da"/>')
    p(f'<text x="{ax-8}" y="{y+4:.1f}" text-anchor="end" fill="#555">{int(frac*100)} %</text>')
for a in (0, 0.25, 0.5, 0.75, 1.0):
    x = ax + a * aw
    p(f'<text x="{x:.1f}" y="{ay+ah+18}" text-anchor="middle" fill="#555">{a:g}</text>')
p(f'<text x="{ax+aw/2}" y="{ay+ah+40}" text-anchor="middle" fill="#333">margen α del relé: se abre a (1+α) × el flujo del día del ajuste</text>')
def pts(clave):
    return " ".join(f"{ax + r['alfa']*aw:.1f},{ay + ah - r[clave]*ah:.1f}" for r in res)
p(f'<polyline points="{pts("fraccion_carga_a_oscuras")}" fill="none" stroke="#1d1d1b" stroke-width="2.5"/>')
p(f'<polyline points="{pts("fraccion_lineas_caidas")}" fill="none" stroke="#b5542b" stroke-width="2" stroke-dasharray="6 4"/>')
for r in res:
    p(f'<circle cx="{ax + r["alfa"]*aw:.1f}" cy="{ay + ah - r["fraccion_carga_a_oscuras"]*ah:.1f}" r="3.5" fill="#1d1d1b"/>')
    p(f'<circle cx="{ax + r["alfa"]*aw:.1f}" cy="{ay + ah - r["fraccion_lineas_caidas"]*ah:.1f}" r="3" fill="#b5542b"/>')
p(f'<line x1="{ax+200}" y1="{ay+22}" x2="{ax+230}" y2="{ay+22}" stroke="#1d1d1b" stroke-width="2.5"/>')
p(f'<text x="{ax+236}" y="{ay+26}" font-size="12">carga a oscuras</text>')
p(f'<line x1="{ax+200}" y1="{ay+42}" x2="{ax+230}" y2="{ay+42}" stroke="#b5542b" stroke-width="2" stroke-dasharray="6 4"/>')
p(f'<text x="{ax+236}" y="{ay+46}" font-size="12">líneas abiertas</text>')
p(f'<text x="{ax}" y="{ay+ah+62}" fill="#555" font-size="12">Grilla de {D["A"]["n"]}×{D["A"]["n"]} nodos y {D["A"]["lineas"]} líneas; flujo de corriente continua.</text>')
p(f'<text x="{ax}" y="{ay+ah+78}" fill="#555" font-size="12">Líneas abiertas: además de la primera. Punteado y lleno, en fracción del total.</text>')

# --- Panel B: mapa ---
M = D["mapa_alfa02"]
bx, by, cell = 500, 70, 30
n = int(math.sqrt(len(M["nodos"])))
pasos = M["pasos"]
p(f'<text x="{bx-10}" y="28" font-size="15" font-weight="bold">B. La cascada con α = 0,2, paso por paso</text>')
colores = ["#1d1d1b", "#b5542b", "#d9822b", "#e8b04b", "#9bb55a", "#5b8fb9", "#7a6bb0", "#b07aa0", "#999"]
def xy(k):
    i, j = M["nodos"][k]
    return bx + j * cell, by + i * cell
for k, (a, b) in enumerate(M["lineas"]):
    x1, y1 = xy(a); x2, y2 = xy(b)
    paso = M["paso_de"].get(str(k))
    if paso is None:
        p(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#cfd6cf" stroke-width="{1 + 3*M["flujo0"][k]/max(M["flujo0"]):.1f}"/>')
for k, (a, b) in enumerate(M["lineas"]):
    x1, y1 = xy(a); x2, y2 = xy(b)
    paso = M["paso_de"].get(str(k))
    if paso is not None:
        c = colores[min(paso, len(colores)-1)]
        p(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{3.5 if paso == 0 else 2.5}"/>')
for k in range(len(M["nodos"])):
    x, y = xy(k)
    if M["gen"][k] > 0:
        p(f'<rect x="{x-5}" y="{y-5}" width="10" height="10" fill="#1d1d1b"/>')
    else:
        servida = M["carga_servida"][k] / M["carga"][k] if M["carga"][k] > 0 else 1
        fill = "#fbfaf6" if servida > 0.999 else ("#f2d4c6" if servida > 0.01 else "#b5542b")
        p(f'<circle cx="{x}" cy="{y}" r="4" fill="{fill}" stroke="#555"/>')
ly = by + n * cell + 10
p(f'<rect x="{bx-5}" y="{ly}" width="10" height="10" fill="#1d1d1b"/><text x="{bx+12}" y="{ly+10}">generadores (fila de arriba)</text>')
p(f'<circle cx="{bx+210}" cy="{ly+5}" r="4" fill="#b5542b" stroke="#555"/><text x="{bx+220}" y="{ly+10}">carga que quedó a oscuras</text>')
p(f'<circle cx="{bx+400}" cy="{ly+5}" r="4" fill="#f2d4c6" stroke="#555"/><text x="{bx+410}" y="{ly+10}">a medias</text>')
for s in range(pasos):
    x = bx + s * 62
    p(f'<line x1="{x}" y1="{ly+32}" x2="{x+26}" y2="{ly+32}" stroke="{colores[min(s, len(colores)-1)]}" stroke-width="3"/>')
    p(f'<text x="{x+30}" y="{ly+36}" font-size="12">{"falla" if s == 0 else "paso " + str(s)}</text>')
p(f'<text x="{bx-10}" y="{ly+76}" fill="#555" font-size="12">junto a los generadores; la grilla se parte en islas y cada isla se arregla con lo que tiene.</text>')
p(f'<text x="{bx-10}" y="{ly+60}" fill="#555" font-size="12">Gris: líneas que aguantaron (grosor = flujo inicial). La falla abre la línea más cargada,</text>')

# --- Panel C: la media hora ---
cx, cy, cw = 960, 80, 420
p(f'<text x="{cx}" y="28" font-size="15" font-weight="bold">C. Nueva York, 9/11/1965, hora del este</text>')
eventos = [(16*60+44, "16:44  se pone el Sol", "#b5542b"),
           (17*60+11, "17:11  sale la Luna (99 %)", "#1d1d1b"),
           (17*60+16, "17:16:11  se abre el relé de Beck", "#1d1d1b"),
           (17*60+25, "17:25  noticiero de WABC", "#555"),
           (17*60+27, "17:27  Nueva York a oscuras", "#1d1d1b")]
t0, t1 = 16*60+40, 17*60+30
p(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy+300}" stroke="#999"/>')
for t, etiqueta, color in eventos:
    y = cy + (t - t0) / (t1 - t0) * 300
    p(f'<line x1="{cx-6}" y1="{y:.1f}" x2="{cx+6}" y2="{y:.1f}" stroke="{color}" stroke-width="2"/>')
    dy = -4 if etiqueta.startswith("17:25") else (10 if etiqueta.startswith("17:27") else 4)
    p(f'<text x="{cx+14}" y="{y+dy:.1f}" fill="{color}">{etiqueta}</text>')
# luna: a 2° sobre el horizonte a las 17:27, azimut 67°
p(f'<rect x="{cx}" y="{cy+330}" width="{cw}" height="70" fill="#0b1020"/>')
p(f'<rect x="{cx}" y="{cy+392}" width="{cw}" height="8" fill="#2a2a2a"/>')
p(f'<circle cx="{cx+cw*0.78:.1f}" cy="{cy+392-8:.1f}" r="7" fill="#f3efe0"/>')
p(f'<text x="{cx+6}" y="{cy+348}" fill="#ddd" font-size="11">17:27: la Luna a 2° sobre el horizonte, al este-noreste (azimut 67°).</text>')
p(f'<text x="{cx+6}" y="{cy+364}" fill="#ddd" font-size="11">Sol a 9° bajo el horizonte. Llena a las 23:15 del día anterior.</text>')
p(f'<text x="{cx}" y="{cy+425}" fill="#555" font-size="12">Cuentas con ephem (cielo.py); las horas del relé y de la ciudad, de las fuentes.</text>')
p('</svg>')
with open("cascada.svg", "w") as fh:
    fh.write("\n".join(out) + "\n")
print("cascada.svg escrito")
