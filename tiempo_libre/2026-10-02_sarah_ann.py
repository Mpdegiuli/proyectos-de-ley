#!/usr/bin/env python3
"""Eclipse total de Sol del 8 de junio de 1937 visto desde donde las cartas
ponían la isla Sarah Ann (4°00'N 154°22'O), desde la isla Malden (su original,
al sur del ecuador) y desde Canton, donde al final se observó.
Necesita: pip install ephem
"""
import math, ephem

LUGARES = [
    ("Sarah Ann (carta de Norie, 4°00'N)", 4.0, -(154 + 22/60)),
    ("Sarah Ann, la otra longitud que se cita (4°00'N 175°O)", 4.0, -175.0),
    ("Sarah Ann espejada (4°00'S, misma longitud)", -4.0, -(154 + 22/60)),
    ("'Sarah Island' del ballenero (3°58'S 154°30'O)", -(3 + 58/60), -(154.5)),
    ("Malden (4°01'S 154°56'O)", -(4 + 1/60), -(154 + 56/60)),
    ("Canton / Kanton (2°50'S 171°40'O)", -(2 + 50/60), -(171 + 40/60)),
]

def estado(obs, t):
    obs.date = t
    s, m = ephem.Sun(obs), ephem.Moon(obs)
    sep = float(ephem.separation((s.az, s.alt), (m.az, m.alt)))
    rs, rm = s.radius, m.radius
    return sep, float(rs), float(rm), float(s.alt)

# control: tres lugares de eclipses recientes, con la duración que recuerdo
# haber leído (no la verifiqué hoy): el método se pasa entre 6 y 9 segundos
CONTROL = [
    ("Madras, Oregón, 21/8/2017 (2 min 02 s)", 44.63, -121.13, '2017/8/21 17:00:00', '2017/8/21 17:40:00'),
    ("Mazatlán, 8/4/2024 (4 min 20 s)", 23.24, -106.42, '2024/4/8 17:50:00', '2024/4/8 18:30:00'),
    ("Dallas, 8/4/2024 (3 min 52 s)", 32.78, -96.80, '2024/4/8 18:20:00', '2024/4/8 19:00:00'),
    ("Canton, otro punto del atolón (2°46'S 171°43'O), 1937", -2.77, -171.72, '1937/6/8 18:40:00', '1937/6/8 19:40:00'),
]

def analizar(nombre, lat, lon, desde='1937/6/8 17:00:00', hasta='1937/6/9 00:30:00'):
    obs = ephem.Observer()
    obs.lat, obs.lon = str(lat), str(lon)
    obs.pressure = 0
    obs.elevation = 0
    t0 = ephem.Date(desde)
    paso = ephem.second
    mejor = None
    total = 0
    t = t0
    fin = ephem.Date(hasta)
    while t < fin:
        sep, rs, rm, alt = estado(obs, t)
        if alt > 0:
            if mejor is None or sep < mejor[0]:
                mejor = (sep, t, rs, rm, alt)
            if sep < rm - rs:
                total += 1
        t += paso
    sep, t, rs, rm, alt = mejor
    # magnitud: fracción del diámetro solar tapada
    mag = (rs + rm - sep) / (2 * rs)
    print(f"{nombre}")
    print(f"   máximo {ephem.Date(t)} UTC, Sol a {math.degrees(alt):.0f}° de altura")
    print(f"   Luna/Sol = {rm/rs:.4f}; magnitud {mag:.3f}; "
          + (f"TOTAL durante {total//60} min {total%60:02d} s" if total else "parcial"))

if __name__ == "__main__":
    for l in LUGARES:
        analizar(*l)
    print("-- control")
    for l in CONTROL:
        analizar(*l)
