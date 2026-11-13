#!/usr/bin/env python3
"""Qué grado de la eclíptica salía en Roma entre la sexta y la séptima hora del
13/10/54, y dónde estaba el Sol cuando nació Nerón (Anzio, 15/12/37, al salir el Sol,
según Suetonio, Nerón 6). Pide `ephem`. Es una cuenta, no una interpretación."""
import math
import ephem
from horas import jdn_juliano, DJD0, SIGNOS

def asc_mc(obs):
    ramc = obs.sidereal_time()
    eps = math.radians(23.69)
    lat = float(obs.lat)
    asc = math.degrees(math.atan2(math.cos(ramc), -(math.sin(ramc) * math.cos(eps) + math.tan(lat) * math.sin(eps)))) % 360
    return asc

def lon(c, obs):
    c.compute(obs)
    return math.degrees(ephem.Ecliptic(c, epoch=obs.date).lon)

def sg(x):
    return f"{SIGNOS[int(x // 30)]} {x % 30:.1f}°"

# Nacimiento de Nerón
anzio = ephem.Observer(); anzio.lat, anzio.lon = "41.447", "12.629"; anzio.horizon = "-0:34"; anzio.pressure = 0
J = jdn_juliano(37, 12, 15)
anzio.date = (J - 0.5) - DJD0 + 0.1
sal = anzio.next_rising(ephem.Sun())
anzio.date = sal
print("Nerón, Anzio, 15/12/37 juliano, salida del Sol:")
for n, c in [("Sol", ephem.Sun()), ("Luna", ephem.Moon()), ("Mercurio", ephem.Mercury()), ("Venus", ephem.Venus()),
             ("Marte", ephem.Mars()), ("Júpiter", ephem.Jupiter()), ("Saturno", ephem.Saturn())]:
    print(f"  {n:9s} {sg(lon(c, anzio))}")
print("  Ascendente", sg(asc_mc(anzio)))
sol_natal = lon(ephem.Sun(), anzio)
asc_natal = asc_mc(anzio)

# Roma, 13/10/54
roma = ephem.Observer(); roma.lat, roma.lon = "41.8925", "12.4853"; roma.horizon = "-0:34"; roma.pressure = 0
J = jdn_juliano(54, 10, 13)
roma.date = (J - 0.5) - DJD0 + 0.2
s = ephem.Sun()
sal = roma.next_rising(s); tr = roma.next_transit(s, start=sal); pu = roma.next_setting(s, start=sal)
hora = (pu - sal) / 12
print("\nRoma, 13/10/54: ascendente según la hora solar verdadera")
for minutos in range(-60, 61, 10):
    roma.date = ephem.Date(tr + minutos / 1440)
    a = asc_mc(roma)
    print(f"  {12 + minutos // 60:02d}:{minutos % 60:02d}  {sg(a)}   (dif. con el Sol natal de Nerón: {a - sol_natal:+.1f}°)")
# a qué hora sale exactamente el grado del Sol natal
lo, hi = tr - 2 / 24, tr + 2 / 24
for _ in range(40):
    mid = (lo + hi) / 2
    roma.date = ephem.Date(mid)
    if asc_mc(roma) < sol_natal: lo = mid
    else: hi = mid
print(f"El grado del Sol natal de Nerón ({sg(sol_natal)}) sale {abs((mid - tr) * 1440):.0f} minutos {'antes' if mid < tr else 'después'} del mediodía verdadero.")
print(f"La séptima hora va de 12:00 a 12:{hora * 1440:.0f}.")

def cuando_sale(grado):
    lo, hi = tr - 2 / 24, tr + 2 / 24
    for _ in range(40):
        mid = (lo + hi) / 2
        roma.date = ephem.Date(mid)
        if asc_mc(roma) < grado: lo = mid
        else: hi = mid
    return (mid - tr) * 1440
print(f"El punto que asomaba cuando se vio el borde del Sol en Anzio ({sg(asc_natal)}) sale {abs(cuando_sale(asc_natal)):.0f} minutos antes del mediodía.")
roma.date = tr
v = ephem.Venus(); v.compute(roma); so = ephem.Sun(); so.compute(roma)
ev = ephem.Ecliptic(v, epoch=roma.date); es = ephem.Ecliptic(so, epoch=roma.date)
print(f"Venus al mediodía: {math.degrees(ev.lon) - math.degrees(es.lon):+.2f}° del Sol en longitud, {math.degrees(ev.lat):+.2f}° de latitud; separación {math.degrees(ephem.separation(v, so)):.2f}°.")
