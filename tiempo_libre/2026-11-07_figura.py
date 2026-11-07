#!/usr/bin/env python3
"""figura.py — lee caida.json (de caida.py) y escribe caida.svg:
la altura de la piedra contra el tiempo, con el tramo luminoso (lo que se ve)
y el tramo oscuro (lo que llega), y a la derecha el cielo de Ensisheim a esa
hora, con el Sol a 23° sobre el horizonte, porque la piedra cayó de día.
"""
import json, math, os

for nombre in ("caida.json", "2026-11-07_caida.json"):
    if os.path.exists(nombre):
        D = json.load(open(nombre))
        break
else:
    raise SystemExit("falta caida.json: correr caida.py")

r = D["ensisheim"]
tr = r["traza"]
fl = r["fin_luz"]
W, H = 960, 540
ML, MR, MT, MB = 70, 330, 50, 60     # márgenes; a la derecha va el cielo
PW, PH = W - ML - MR, H - MT - MB
tmax = math.ceil(r["t_total"] / 5) * 5
hmax = 120

def X(t): return ML + PW * t / tmax
def Y(h): return MT + PH * (1 - h / hmax)

o = []
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Georgia, serif">')
o.append('<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>'
         '<radialGradient id="sun"><stop offset="0" stop-color="#fff6c8"/><stop offset=".6" stop-color="#ffd24a"/><stop offset="1" stop-color="#ffb000" stop-opacity="0"/></radialGradient>'
         '<linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fb2e5"/><stop offset="1" stop-color="#dbe9f6"/></linearGradient></defs>')
o.append(f'<rect width="{W}" height="{H}" fill="#fbf8f1"/>')
o.append(f'<text x="{ML}" y="30" font-size="17" fill="#333">Una piedra de 526 kg entra a 15 km/s y 45°; llegan 127 kg. Lo que brilla y lo que cae.</text>')

# ejes
o.append(f'<line x1="{ML}" y1="{Y(0)}" x2="{ML+PW}" y2="{Y(0)}" stroke="#555" stroke-width="1.2"/>')
o.append(f'<line x1="{ML}" y1="{Y(0)}" x2="{ML}" y2="{Y(hmax)}" stroke="#555" stroke-width="1.2"/>')
for h in range(0, hmax + 1, 20):
    o.append(f'<line x1="{ML-4}" y1="{Y(h)}" x2="{ML}" y2="{Y(h)}" stroke="#555"/>')
    o.append(f'<text x="{ML-8}" y="{Y(h)+4}" font-size="11" text-anchor="end" fill="#444">{h}</text>')
for t in range(0, tmax + 1, 5):
    o.append(f'<line x1="{X(t)}" y1="{Y(0)}" x2="{X(t)}" y2="{Y(0)+4}" stroke="#555"/>')
    o.append(f'<text x="{X(t)}" y="{Y(0)+17}" font-size="11" text-anchor="middle" fill="#444">{t}</text>')
o.append(f'<text x="{ML+PW/2}" y="{H-14}" font-size="12" text-anchor="middle" fill="#444">segundos desde los 120 km</text>')
o.append(f'<text x="18" y="{MT+PH/2}" font-size="12" text-anchor="middle" fill="#444" transform="rotate(-90 18 {MT+PH/2})">altura, km</text>')

# trazas
luz = [(X(t), Y(h / 1000)) for (t, h, x, v, m) in tr if v >= 3000]
osc = [(X(t), Y(h / 1000)) for (t, h, x, v, m) in tr if v < 3000]
if luz and osc:
    osc.insert(0, luz[-1])
pl = " ".join(f"{a:.1f},{b:.1f}" for a, b in luz)
po = " ".join(f"{a:.1f},{b:.1f}" for a, b in osc)
o.append(f'<polyline points="{pl}" fill="none" stroke="#ff9a2e" stroke-width="9" opacity=".45" filter="url(#g)"/>')
o.append(f'<polyline points="{pl}" fill="none" stroke="#e8641b" stroke-width="2.6"/>')
o.append(f'<polyline points="{po}" fill="none" stroke="#777" stroke-width="2" stroke-dasharray="5 4"/>')

# hitos
xf, yf = X(fl["t"]), Y(fl["h"] / 1000)
o.append(f'<circle cx="{xf:.1f}" cy="{yf:.1f}" r="4" fill="#e8641b"/>')
o.append(f'<text x="{xf+8:.1f}" y="{yf-8:.1f}" font-size="12" fill="#333">se apaga: {str(round(fl["t"],1)).replace(".",",")} s, {fl["h"]/1000:.0f} km, 3 km/s</text>')
xg, yg = X(r["t_total"]), Y(0)
o.append(f'<circle cx="{xg:.1f}" cy="{yg:.1f}" r="4" fill="#555"/>')
o.append(f'<text x="{xg-6:.1f}" y="{yg-10:.1f}" font-size="12" text-anchor="end" fill="#333">suelo: {r["t_total"]:.0f} s, {r["v_final"]:.0f} m/s, {r["m_final"]:.0f} kg</text>')
o.append(f'<text x="{X(2)}" y="{Y(100)}" font-size="12" fill="#b4470f">{fl["t"]:.0f} segundos de luz</text>')
o.append(f'<text x="{(xf+xg)/2:.1f}" y="{Y(28)}" font-size="12" fill="#555" text-anchor="middle">{r["t_oscuro"]:.0f} segundos a oscuras, {r["x_oscuro"]/1000:.0f} km más</text>')

# sensibilidad al arrastre, en chico
gy = Y(70)
o.append(f'<text x="{X(14)}" y="{gy}" font-size="11" fill="#555">según el arrastre (Γ = 0,5 · 0,75 · 1): la luz se apaga a '
         + " · ".join(f'{g["h_luz"]/1000:.0f}' for g in D["gammas"]) + ' km</text>')
o.append(f'<text x="{X(14)}" y="{gy+15}" font-size="11" fill="#555">y la piedra cae a oscuras '
         + " · ".join(f'{g["t_osc"]:.0f}' for g in D["gammas"]) + ' segundos</text>')

# el cielo de Ensisheim, 16/11/1492 gregoriano, 11:30 hora solar: Sol a 22,8°
cx0, cy0, cw, ch = W - MR + 30, MT, MR - 60, 250
o.append(f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" fill="url(#cielo)" stroke="#999"/>')
hor = cy0 + ch - 40
o.append(f'<rect x="{cx0}" y="{hor}" width="{cw}" height="{cy0+ch-hor}" fill="#9a8a62"/>')
alt = 22.8
# observador en la esquina izquierda del horizonte; el Sol a 22,8° de elevación
ox, oy = cx0 + 12, hor
L = cw - 40
sx, sy = ox + L * math.cos(math.radians(alt)), oy - L * math.sin(math.radians(alt))
o.append(f'<line x1="{ox}" y1="{oy}" x2="{sx:.1f}" y2="{sy:.1f}" stroke="#b4470f" stroke-width="1" stroke-dasharray="3 3"/>')
o.append(f'<path d="M{ox+60},{oy} A60,60 0 0 0 {ox+60*math.cos(math.radians(alt)):.1f},{oy-60*math.sin(math.radians(alt)):.1f}" fill="none" stroke="#b4470f" stroke-width="1"/>')
o.append(f'<text x="{ox+66}" y="{oy-6}" font-size="12" fill="#7a2e08">{alt:.0f}°</text>')
o.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="22" fill="url(#sun)"/>')
o.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="9" fill="#fff3b0"/>')
# la piedra: un trazo corto, blanco, de día
o.append(f'<line x1="{cx0+cw-30}" y1="{cy0+25}" x2="{cx0+cw-95}" y2="{cy0+95}" stroke="#fff" stroke-width="5" opacity=".9" filter="url(#g)"/>')
o.append(f'<line x1="{cx0+cw-30}" y1="{cy0+25}" x2="{cx0+cw-95}" y2="{cy0+95}" stroke="#fff" stroke-width="1.5"/>')
# el pueblo
for i, (bx, bh) in enumerate([(130, 18), (148, 26), (166, 20), (184, 34), (202, 22), (220, 28), (238, 19)]):
    o.append(f'<rect x="{cx0+bx}" y="{hor-bh}" width="14" height="{bh}" fill="#6b5a3e"/>')
o.append(f'<rect x="{cx0+184+4}" y="{hor-34-26}" width="6" height="26" fill="#6b5a3e"/>')
o.append(f'<text x="{cx0+cw/2}" y="{cy0+ch+18}" font-size="12" text-anchor="middle" fill="#333">Ensisheim, 7/11/1492 (juliano), 11:30 hora solar</text>')
o.append(f'<text x="{cx0+cw/2}" y="{cy0+ch+34}" font-size="12" text-anchor="middle" fill="#333">el Sol a 23° sobre el horizonte: era de día</text>')
o.append(f'<text x="{cx0+cw/2}" y="{cy0+ch+52}" font-size="11" text-anchor="middle" fill="#777">(sol.py; los seis dibujos de hoy son de noche)</text>')
o.append('</svg>')
open("caida.svg", "w").write("\n".join(o))
print("caida.svg", os.path.getsize("caida.svg"), "bytes")
