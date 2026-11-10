"""Los dos luceros de Van Gogh, calculados: Venus sobre Saint-Rémy-de-Provence
(43.79 N, 4.83 E) al alba del 2 de junio de 1889 (carta 777, La noche estrellada) y al
anochecer del 20 de abril de 1890 (la conjunción Venus-Mercurio que se cita para
Camino con ciprés y estrella), con la Luna. Fechas gregorianas. Sin dependencias
aparte de ephem.
"""
import math, ephem

def obs(fecha_utc):
    o = ephem.Observer()
    o.lat, o.lon, o.elevation = "43.79", "4.83", 100
    o.pressure = 0
    o.date = fecha_utc
    return o

def estado(nombre, cuerpo, o):
    cuerpo.compute(o)
    return f"{nombre}: altura {math.degrees(cuerpo.alt):5.1f}°, acimut {math.degrees(cuerpo.az):5.1f}°, mag {cuerpo.mag:.1f}"

def elong(d):
    s, v = ephem.Sun(d), ephem.Venus(d)
    e = math.degrees(float(ephem.separation(s, v)))
    ls, lv = ephem.Ecliptic(s).lon, ephem.Ecliptic(v).lon
    return e if ((float(lv) - float(ls) + math.pi) % (2*math.pi) - math.pi) > 0 else -e

print("== Alba del 2 de junio de 1889 en Saint-Rémy (hora local ≈ UTC+0:19) ==")
# crepúsculo civil de la mañana: Sol a -6°
o = obs("1889/06/01 22:00")
o.horizon = "-6"
t = o.next_rising(ephem.Sun(), use_center=True)
o.horizon = "0"; o.date = t
print("Sol a -6° a las", ephem.Date(t + 19*ephem.minute), "hora local media")
print("  ", estado("Venus", ephem.Venus(), o))
print("  ", estado("Luna ", ephem.Moon(), o), f"(fase {ephem.Moon(o.date).phase:.0f} %)")
print(f"   elongación de Venus {elong(t):+.1f}° ({'tarde' if elong(t) > 0 else 'alba'})")

print("\n== Anochecer del 20 de abril de 1890 en Saint-Rémy ==")
o = obs("1890/04/20 12:00")
o.horizon = "-6"
t = o.next_setting(ephem.Sun(), use_center=True)
o.horizon = "0"; o.date = t
print("Sol a -6° a las", ephem.Date(t + 19*ephem.minute), "hora local media")
for n, c in (("Venus", ephem.Venus()), ("Mercurio", ephem.Mercury()), ("Luna ", ephem.Moon())):
    print("  ", estado(n, c, o))
v, m = ephem.Venus(o.date), ephem.Mercury(o.date)
print(f"   separación Venus-Mercurio {math.degrees(float(ephem.separation(v, m))):.1f}°; fase de la Luna {ephem.Moon(o.date).phase:.0f} %")
print(f"   elongación de Venus {elong(t):+.1f}° ({'tarde' if elong(t) > 0 else 'alba'})")
