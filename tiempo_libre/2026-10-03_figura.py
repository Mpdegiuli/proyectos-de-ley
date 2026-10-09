#!/usr/bin/env python3
"""figura.py - escribe primera_hora.svg: el cielo hacia el sur desde la Porciúncula al final
del crepúsculo civil del 3 de octubre de 1226 (juliano), y la franja de esa tarde en horas
desiguales, con el cambio de día a la puesta del Sol.
Necesita: pip install ephem (y cairosvg si se quiere el PNG)"""
import math, ephem

def jdn_juliano(a, m, d):
    x = (14 - m) // 12; y = a + 4800 - x; mm = m + 12 * x - 3
    return d + (153 * mm + 2) // 5 + 365 * y + y // 4 - 32083

def djd(jdn, frac=0.0):
    return ephem.Date(jdn - 2415020 + frac)

LAT, LON, ALT = "43.0558", "12.5803", 218
def obs(t, horizonte="0"):
    o = ephem.Observer(); o.lat, o.lon, o.elevation = LAT, LON, ALT
    o.pressure = 1010; o.horizon = horizonte; o.date = t
    return o

sol = ephem.Sun()
mediodia = obs(djd(jdn_juliano(1226, 10, 3), -0.2)).next_transit(sol)
o = obs(mediodia)
puesta = o.next_setting(sol); salida_sig = o.next_rising(sol); salida = o.previous_rising(sol)
civil = obs(puesta, "-6").next_setting(sol, use_center=True)
hora_noche = (salida_sig - puesta) / 12
hora_dia = (puesta - salida) / 12
fin_prima = puesta + hora_noche

def solar(t):
    """hora solar verdadera, en horas decimales"""
    return 12 + (t - mediodia) * 24
def hhmm(h):
    return f"{int(h):02d}:{int(round((h % 1) * 60)) % 60:02d}"

# ---------- cielo ----------
o = obs(civil)
def altaz(c):
    c.compute(o); return math.degrees(c.alt), math.degrees(c.az)
luna = ephem.Moon(); luna.compute(o)
cuerpos = [("Júpiter", ephem.Jupiter(), 4.2, "#f4e9c9"),
           ("Saturno", ephem.Saturn(), 2.6, "#e9dcae"),
           ("Marte", ephem.Mars(), 2.6, "#e8a07a")]
estrellas = [("Altair", "Altair"), ("Fomalhaut", "Fomalhaut"), ("Antares", "Antares"),
             ("Vega", "Vega"), ("Deneb", "Deneb"), ("Arturo", "Arcturus")]

W, H = 900, 640
X0, X1, Y0, Y1 = 60, 840, 60, 380          # caja del cielo
AZ0, AZ1, ALTMAX = 90.0, 270.0, 62.0
def px(az): return X0 + (az - AZ0) / (AZ1 - AZ0) * (X1 - X0)
def py(alt): return Y1 - alt / ALTMAX * (Y1 - Y0)

s = []
a = s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Georgia, serif">')
a('<defs><linearGradient id="cielo" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0" stop-color="#16203a"/><stop offset="0.6" stop-color="#27365a"/><stop offset="1" stop-color="#6b5a6e"/>'
  '</linearGradient></defs>')
a(f'<rect width="{W}" height="{H}" fill="#f6f1e7"/>')
a(f'<text x="{X0}" y="34" font-size="19" fill="#2b2a28">La primera hora de la noche, Porciúncula, sábado 3 de octubre de 1226</text>')
a(f'<rect x="{X0}" y="{Y0}" width="{X1-X0}" height="{Y1-Y0}" fill="url(#cielo)"/>')
# grilla de altura
for alt in (20, 40, 60):
    a(f'<line x1="{X0}" y1="{py(alt):.1f}" x2="{X1}" y2="{py(alt):.1f}" stroke="#ffffff" stroke-opacity="0.13"/>')
    a(f'<text x="{X0-8}" y="{py(alt)+4:.1f}" font-size="12" fill="#6b655b" text-anchor="end">{alt}°</text>')
for az, nombre in ((90, "E"), (135, "SE"), (180, "S"), (225, "SO"), (270, "O")):
    a(f'<text x="{px(az):.1f}" y="{Y1+18}" font-size="13" fill="#2b2a28" text-anchor="middle">{nombre}</text>')
    if 90 < az < 270:
        a(f'<line x1="{px(az):.1f}" y1="{Y1}" x2="{px(az):.1f}" y2="{Y1-6}" stroke="#f6f1e7" stroke-opacity="0.6"/>')
# estrellas
for nombre, clave in estrellas:
    e = ephem.star(clave); alt, az = altaz(e)
    if AZ0 <= az <= AZ1 and 0 < alt < ALTMAX:
        a(f'<circle cx="{px(az):.1f}" cy="{py(alt):.1f}" r="1.6" fill="#ffffff" fill-opacity="0.85"/>')
        a(f'<text x="{px(az)+7:.1f}" y="{py(alt)+4:.1f}" font-size="11.5" fill="#cfd6e6" font-style="italic">{nombre}</text>')
# planetas
for nombre, c, r, color in cuerpos:
    alt, az = altaz(c)
    a(f'<circle cx="{px(az):.1f}" cy="{py(alt):.1f}" r="{r}" fill="{color}"/>')
    dx, anchor = (-9, "end") if nombre == "Júpiter" else (9, "start")
    a(f'<text x="{px(az)+dx:.1f}" y="{py(alt)+4:.1f}" font-size="13" fill="#f6f1e7" text-anchor="{anchor}">{nombre}</text>')

# Luna: disco con terminador elíptico (la mitad del lado del Sol es medio círculo; la otra, media elipse)
altL, azL = math.degrees(luna.alt), math.degrees(luna.az)
sol.compute(o)
altS, azS = float(sol.alt), float(sol.az)
aL, zL = float(luna.alt), float(luna.az)
# ángulo del limbo brillante medido desde el cenit hacia acimutes crecientes (hacia la derecha en la figura)
theta = math.atan2(math.cos(altS) * math.sin(azS - zL),
                   math.sin(altS) * math.cos(aL) - math.cos(altS) * math.sin(aL) * math.cos(azS - zL))
k = luna.phase / 100.0
def luna_svg(cx, cy, R, etiqueta=None):
    b = R * abs(2 * k - 1)                 # semieje menor del terminador
    # en el marco de la Luna: el Sol hacia +x. Lado iluminado: semicírculo x>0 más media elipse x<0 (gibosa).
    rot = math.degrees(theta) - 90         # girar +x hacia la dirección del Sol (theta desde arriba, horario en pantalla)
    out = [f'<g transform="translate({cx:.1f},{cy:.1f}) rotate({rot:.1f})">',
           f'<circle r="{R}" fill="#39425e"/>',
           f'<path d="M0,{-R} A{R},{R} 0 0 1 0,{R} A{b:.2f},{R} 0 0 {1 if k > 0.5 else 0} 0,{-R} Z" fill="#f3ecd6"/>',
           '</g>']
    return "\n".join(out)
a(luna_svg(px(azL), py(altL), 9))
a(f'<text x="{px(azL):.1f}" y="{py(altL)+26:.1f}" font-size="13" fill="#f6f1e7" text-anchor="middle">Luna, {luna.phase:.0f} %</text>')
# recuadro con la Luna ampliada
bx, by = X0 + 70, Y0 + 64
a(luna_svg(bx, by, 34))
a(f'<text x="{bx+46}" y="{by-4}" font-size="11.5" fill="#cfd6e6">la Luna, ampliada:</text>')
a(f'<text x="{bx+46}" y="{by+12}" font-size="11.5" fill="#cfd6e6">medio círculo y media elipse</text>')
# flecha hacia donde se puso el Sol
a(f'<text x="{X1-10}" y="{Y1-10}" font-size="12" fill="#f6f1e7" text-anchor="end">el Sol, 6° bajo el horizonte →</text>')
jup, sat = ephem.Jupiter(o), ephem.Saturn(o)
sepJS = math.degrees(ephem.separation(jup, sat))
a(f'<text x="{px(math.degrees(jup.az)):.1f}" y="{py(math.degrees(jup.alt))-16:.1f}" font-size="11.5" fill="#cfd6e6" text-anchor="middle" font-style="italic">a dos grados y medio uno de otro</text>')

# ---------- franja de la tarde ----------
FY = 470
t0, t1 = 15.0, 21.0                           # hora solar verdadera
def fx(h): return X0 + (h - t0) / (t1 - t0) * (X1 - X0)
hp, hc, hf = solar(puesta), solar(civil), solar(fin_prima)
a(f'<rect x="{fx(t0):.1f}" y="{FY}" width="{fx(hp)-fx(t0):.1f}" height="34" fill="#e9d9a8"/>')
a(f'<rect x="{fx(hp):.1f}" y="{FY}" width="{fx(hc)-fx(hp):.1f}" height="34" fill="#8d7d8c"/>')
a(f'<rect x="{fx(hc):.1f}" y="{FY}" width="{fx(t1)-fx(hc):.1f}" height="34" fill="#27365a"/>')
# primera hora de la noche
a(f'<rect x="{fx(hp):.1f}" y="{FY-7}" width="{fx(hf)-fx(hp):.1f}" height="48" fill="none" stroke="#a23b2a" stroke-width="2"/>')
a(f'<text x="{(fx(hp)+fx(hf))/2:.1f}" y="{FY-14}" font-size="13" fill="#a23b2a" text-anchor="middle">primera hora de la noche: {hhmm(hp)} a {hhmm(hf)}</text>')
# horas desiguales del día (décima, undécima, duodécima) y de la noche
for n in range(0, 13):
    h = solar(puesta - n * hora_dia)
    if h >= t0:
        a(f'<line x1="{fx(h):.1f}" y1="{FY}" x2="{fx(h):.1f}" y2="{FY+34}" stroke="#2b2a28" stroke-opacity="0.35"/>')
for n in range(1, 5):
    h = solar(puesta + n * hora_noche)
    if h <= t1:
        a(f'<line x1="{fx(h):.1f}" y1="{FY}" x2="{fx(h):.1f}" y2="{FY+34}" stroke="#f6f1e7" stroke-opacity="0.45"/>')
# reloj nuestro
for h in range(15, 22):
    a(f'<line x1="{fx(h):.1f}" y1="{FY+34}" x2="{fx(h):.1f}" y2="{FY+40}" stroke="#2b2a28"/>')
    a(f'<text x="{fx(h):.1f}" y="{FY+54}" font-size="12" fill="#2b2a28" text-anchor="middle">{h}:00</text>')
a(f'<text x="{X1}" y="{FY+74}" font-size="12" fill="#6b655b" text-anchor="end">hora solar verdadera; las rayas son las horas desiguales ({hora_dia*24*60:.1f} min las del día, {hora_noche*24*60:.1f} las de la noche)</text>'.replace(".", ","))
# numerales de las horas desiguales
for n, rom in ((1, "XII"), (2, "XI")):
    h = solar(puesta - (n - 0.5) * hora_dia)
    a(f'<text x="{fx(h):.1f}" y="{FY+22}" font-size="12" fill="#6b5a2e" text-anchor="middle">{rom}</text>')
for n, rom in ((2, "II"), (3, "III")):
    h = solar(puesta + (n - 0.5) * hora_noche)
    a(f'<text x="{fx(h):.1f}" y="{FY+22}" font-size="12" fill="#cfd6e6" text-anchor="middle">{rom}</text>')
h = solar(puesta + 0.72 * hora_noche)
a(f'<text x="{fx(h):.1f}" y="{FY+22}" font-size="12" fill="#cfd6e6" text-anchor="middle">I</text>')
# los dos cambios de día
a(f'<line x1="{fx(hp):.1f}" y1="{FY+86}" x2="{fx(hp):.1f}" y2="{FY+124}" stroke="#a23b2a" stroke-width="1.5"/>')
a(f'<text x="{fx(hp)-8:.1f}" y="{FY+102}" font-size="13" fill="#2b2a28" text-anchor="end">sábado</text>')
a(f'<text x="{fx(hp)+8:.1f}" y="{FY+102}" font-size="13" fill="#2b2a28">domingo 4 de octubre (fray Elías, Celano)</text>')
a(f'<text x="{fx(hp)-8:.1f}" y="{FY+121}" font-size="13" fill="#6b655b" text-anchor="end">sábado 3 hasta la medianoche (nosotros)</text>')
a(f'<text x="{X0}" y="{FY+146}" font-size="12" fill="#6b655b">Posiciones calculadas con PyEphem para 43°03′N 12°35′E al final del crepúsculo civil ({hhmm(hc)}).</text>')
a(f'<text x="{X0}" y="{FY+162}" font-size="12" fill="#6b655b">Del tiempo que hizo no encontré noticia.</text>')
a('</svg>')
open("primera_hora.svg", "w").write("\n".join(s))
print("puesta", hhmm(hp), "civil", hhmm(hc), "fin prima", hhmm(hf), "theta", round(math.degrees(theta), 1), "k", round(k, 3), "JS", round(sepJS, 2))
try:                                    # el PNG es opcional: pip install cairosvg
    import cairosvg
    cairosvg.svg2png(url="primera_hora.svg", write_to="primera_hora.png", scale=1.5)
except ImportError:
    pass
