#!/usr/bin/env python3
"""conjuncion.py - Júpiter y Saturno en 1226 y la Luna del 3 de octubre.
Necesita: pip install ephem"""
import math, ephem

def jdn_juliano(a, m, d):
    x = (14 - m) // 12; y = a + 4800 - x; mm = m + 12 * x - 3
    return d + (153 * mm + 2) // 5 + 365 * y + y // 4 - 32083

def djd(jdn, frac=0.0):
    return ephem.Date(jdn - 2415020 + frac)

def sep(t):
    j, s = ephem.Jupiter(), ephem.Saturn()
    j.compute(t); s.compute(t)
    return math.degrees(ephem.separation(j, s)), j, s

# mínimo de separación a lo largo de 1226
t0 = djd(jdn_juliano(1226, 1, 1))
mejor = (99, None)
for k in range(0, 365 * 24):
    t = ephem.Date(t0 + k / 24)
    d, j, s = sep(t)
    if d < mejor[0]:
        mejor = (d, t)
d, t = mejor
sol = ephem.Sun(); sol.compute(t)
j = ephem.Jupiter(); j.compute(t)
print(f"mínimo de 1226: {d*60:.1f} minutos de arco, el {ephem.Date(t)} TU (fecha juliana), "
      f"a {math.degrees(ephem.separation(j, sol)):.0f}° del Sol, en {ephem.constellation(j)[1]}")

# la noche del 3 de octubre de 1226, final del crepúsculo civil en la Porciúncula
o = ephem.Observer(); o.lat, o.lon, o.elevation = "43.0558", "12.5803", 218
o.date = djd(jdn_juliano(1226, 10, 3), 0.0)
puesta = o.next_setting(ephem.Sun())
o.date = puesta; o.horizon = "-6"
civil = o.next_setting(ephem.Sun(), use_center=True)
o.horizon = "0"; o.date = civil
j, s, l, m = ephem.Jupiter(o), ephem.Saturn(o), ephem.Moon(o), ephem.Mars(o)
print(f"3/10/1226, fin del crepúsculo civil:")
print(f"  Júpiter-Saturno: {math.degrees(ephem.separation(j, s)):.2f}°  ({ephem.constellation(j)[1]} / {ephem.constellation(s)[1]})")
print(f"  Luna-Júpiter   : {math.degrees(ephem.separation(l, j)):.1f}°;  Luna en {ephem.constellation(l)[1]}, {l.phase:.0f} % iluminada")
print(f"  Luna: altura {math.degrees(l.alt):.0f}°, acimut {math.degrees(l.az):.0f}°")
print(f"  Júpiter: altura {math.degrees(j.alt):.0f}°, acimut {math.degrees(j.az):.0f}°, mag {j.mag}")
print(f"  Saturno: altura {math.degrees(s.alt):.0f}°, acimut {math.degrees(s.az):.0f}°, mag {s.mag}")
print(f"  Marte  : altura {math.degrees(m.alt):.0f}°, acimut {math.degrees(m.az):.0f}°, mag {m.mag}")
# estrellas brillantes
for nombre in ("Vega", "Arcturus", "Altair", "Deneb", "Antares", "Fomalhaut", "Capella"):
    e = ephem.star(nombre); e.compute(o)
    print(f"  {nombre:9s}: altura {math.degrees(e.alt):5.1f}°, acimut {math.degrees(e.az):5.1f}°")

# control: la conjunción del 21/12/2020
t0 = ephem.Date("2020/12/1")
mejor = (99, None)
for k in range(0, 31 * 24):
    t = ephem.Date(t0 + k / 24)
    d, _, _ = sep(t)
    if d < mejor[0]: mejor = (d, t)
print(f"control 2020: mínimo {mejor[0]*60:.1f}' el {ephem.Date(mejor[1])} TU")

# dónde está la Luna hoy, 3/10/2026, a la puesta del Sol en Asís
o = ephem.Observer(); o.lat, o.lon, o.elevation = "43.0558", "12.5803", 218
o.date = "2026/10/3 12:00"
puesta = o.next_setting(ephem.Sun()); o.date = puesta
l = ephem.Moon(o)
print(f"hoy 3/10/2026 a la puesta en Asís ({puesta} TU): Luna {l.phase:.0f} % iluminada, altura {math.degrees(l.alt):.0f}°")
print("  luna nueva anterior:", ephem.previous_new_moon(puesta), " llena anterior:", ephem.previous_full_moon(puesta))
o.date = puesta
print("  la Luna sale", round((o.next_rising(ephem.Moon()) - puesta) * 24, 1), "h después de la puesta")
