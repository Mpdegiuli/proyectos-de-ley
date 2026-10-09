#!/usr/bin/env python3
"""sabado.py - cuentas del cuaderno de tiempo libre del 3/10/2026.

1. Qué día de la semana fue el 3 de octubre de 1226 (calendario juliano) y cuántos
   días pasaron hasta el 3 de octubre de 2026 (gregoriano).
2. A qué hora se puso el Sol en la Porciúncula ese día y cuánto duraba la hora
   desigual de la noche (la primera hora de la noche de la carta de fray Elías).
3. Cómo estaba la Luna esa noche.

Necesita: pip install ephem
"""
import math
import ephem

# ---------- 1. calendario ----------
def jdn_juliano(a, m, d):
    """Número de día juliano de una fecha del calendario juliano."""
    x = (14 - m) // 12
    y = a + 4800 - x
    mm = m + 12 * x - 3
    return d + (153 * mm + 2) // 5 + 365 * y + y // 4 - 32083

def jdn_gregoriano(a, m, d):
    x = (14 - m) // 12
    y = a + 4800 - x
    mm = m + 12 * x - 3
    return d + (153 * mm + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

j1226 = jdn_juliano(1226, 10, 3)
g2026 = jdn_gregoriano(2026, 10, 3)
g1226 = jdn_gregoriano(1226, 10, 3)   # el 3/10/1226 si el calendario gregoriano se extendiera hacia atrás
print("1. Calendario")
print(f"   3/10/1226 juliano     : día juliano {j1226}, {DIAS[j1226 % 7]}")
print(f"   3/10/2026 gregoriano  : día juliano {g2026}, {DIAS[g2026 % 7]}")
print(f"   días entre los dos    : {g2026 - j1226} = {(g2026 - j1226) // 7} semanas y {(g2026 - j1226) % 7} días")
print(f"   800 años gregorianos  : {g2026 - g1226} días = {(g2026 - g1226) // 7} semanas y {(g2026 - g1226) % 7} días")
print(f"   desfase juliano-gregoriano en 1226: {j1226 - g1226} días")
# en qué fecha gregoriana de 2026 se cumplen 800 años trópicos (misma posición del Sol)
print(f"   el 3/10/1226 juliano es el {j1226 - jdn_gregoriano(1226, 10, 1) + 1}/10/1226 en gregoriano proléptico")

# en qué siglos el desfase es múltiplo de 7 (para ver si la coincidencia de día es rara)
print("   desfase por siglo (1 de marzo del año X00 al 28 de febrero de X00+100):")
for siglo in range(0, 2200, 100):
    d = jdn_juliano(siglo + 50, 6, 1) - jdn_gregoriano(siglo + 50, 6, 1)
    marca = "  <- múltiplo de 7" if d % 7 == 0 else ""
    print(f"     {siglo:4d}-{siglo+99:4d}: {d:3d} días{marca}")

# ---------- 2. Sol ----------
# Porciúncula (Santa Maria degli Angeli): 43°03'21"N 12°34'49"E, unos 218 m
LAT, LON, ALT = "43.0558", "12.5803", 218

def djd(jdn, frac=0.0):
    """Fecha de PyEphem (días desde 1899-12-31 12:00 TU) a partir de un día juliano."""
    return ephem.Date(jdn - 2415020 + frac)

def observador(fecha):
    o = ephem.Observer()
    o.lat, o.lon, o.elevation = LAT, LON, ALT
    o.pressure = 1010
    o.date = fecha
    return o

sol = ephem.Sun()
lon_h = float(LON) / 15.0     # hora local media = TU + lon/15

def hms(d):
    """hora local media (no de huso) en h:mm a partir de una fecha de PyEphem en TU"""
    h = ((d + 0.5) % 1) * 24 + lon_h
    h %= 24
    return f"{int(h):02d}:{int(round((h % 1) * 60)) % 60:02d}"

def sol_del_dia(jdn):
    o = observador(djd(jdn, 0.0))           # mediodía TU del día
    transito = o.next_transit(sol, start=djd(jdn, -0.2))
    o.date = transito
    puesta = o.next_setting(sol)
    salida_sig = o.next_rising(sol)
    o.date = transito
    salida = o.previous_rising(sol)
    return salida, transito, puesta, salida_sig

print()
print("2. Sol en la Porciúncula")
for etiqueta, jdn in (("3/10/1226 (juliano)", j1226), ("3/10/2026 (gregoriano)", g2026)):
    salida, transito, puesta, salida_sig = sol_del_dia(jdn)
    noche = (salida_sig - puesta) * 24
    dia = (puesta - salida) * 24
    hora_noche = noche / 12 * 60
    fin_prima = ephem.Date(puesta + (salida_sig - puesta) / 12)
    # hora verdadera (solar aparente): mediodía = tránsito
    def solar(d):
        h = 12 + (d - transito) * 24
        return f"{int(h):02d}:{int(round((h % 1) * 60)) % 60:02d}"
    print(f"   {etiqueta}")
    print(f"     día de {dia:5.2f} h, noche de {noche:5.2f} h; hora de la noche: {hora_noche:4.1f} min")
    print(f"     puesta del Sol         : {solar(puesta)} hora solar verdadera ({hms(puesta)} hora local media)")
    print(f"     fin de la primera hora : {solar(fin_prima)} hora solar verdadera")
    # crepúsculo civil
    o = observador(puesta); o.horizon = "-6"
    civil = o.next_setting(sol, use_center=True)
    print(f"     fin del crepúsculo civil: {solar(civil)} ({(civil - puesta) * 24 * 60:4.1f} min después de la puesta)")
    if jdn == g2026:
        # hora oficial italiana (CEST = TU+2)
        def cest(d):
            h = ((d + 0.5) % 1) * 24 + 2
            return f"{int(h):02d}:{int(round((h % 1) * 60)) % 60:02d}"
        print(f"     en hora oficial (TU+2): puesta {cest(puesta)}, fin de la primera hora {cest(fin_prima)}")
        # y en Buenos Aires (TU-3)
        def bsas(d):
            h = ((d + 0.5) % 1) * 24 - 3
            return f"{int(h % 24):02d}:{int(round((h % 1) * 60)) % 60:02d}"
        print(f"     en hora de Buenos Aires (TU-3): puesta {bsas(puesta)}, fin de la primera hora {bsas(fin_prima)}")

# ---------- 3. Luna ----------
print()
print("3. Luna sobre la Porciúncula, noche del 3/10/1226")
salida, transito, puesta, salida_sig = sol_del_dia(j1226)
luna = ephem.Moon()
for etiqueta, t in (("a la puesta del Sol", puesta),
                    ("al final de la primera hora", ephem.Date(puesta + (salida_sig - puesta) / 12))):
    o = observador(t)
    luna.compute(o)
    sol.compute(o)
    elong = math.degrees(ephem.separation(luna, sol))
    print(f"   {etiqueta}: iluminada {luna.phase:4.1f} %, altura {math.degrees(luna.alt):5.1f}°, "
          f"acimut {math.degrees(luna.az):5.1f}°, a {elong:5.1f}° del Sol")
o = observador(puesta)
print(f"   luna nueva anterior : {ephem.previous_new_moon(puesta)} TU")
print(f"   luna llena siguiente: {ephem.next_full_moon(puesta)} TU")
print(f"   luna llena anterior : {ephem.previous_full_moon(puesta)} TU")
print(f"   luna nueva siguiente: {ephem.next_new_moon(puesta)} TU")
edad = puesta - ephem.previous_new_moon(puesta)
print(f"   edad de la Luna a la puesta: {edad:4.1f} días")
o = observador(puesta)
try:
    print(f"   la Luna se pone: {(o.next_setting(luna) - puesta) * 24:4.1f} h después que el Sol")
except Exception as e:
    print("   ", e)
o = observador(puesta)
print(f"   la Luna sale   : {(o.next_rising(luna) - puesta) * 24:4.1f} h después de la puesta del Sol")
# planetas a la vista al final del crepúsculo civil
o = observador(puesta); o.horizon = "-6"
civil = o.next_setting(sol, use_center=True)
o = observador(civil)
print("   al final del crepúsculo civil:")
for cuerpo in (ephem.Venus(), ephem.Jupiter(), ephem.Saturn(), ephem.Mars(), ephem.Mercury()):
    cuerpo.compute(o)
    print(f"     {cuerpo.name:8s} altura {math.degrees(cuerpo.alt):6.1f}°, acimut {math.degrees(cuerpo.az):5.1f}°, magnitud {cuerpo.mag:4.1f}")

# ---------- 4. controles ----------
print()
print("4. Controles")
mc = jdn_juliano(1215, 6, 15); mg = jdn_gregoriano(2015, 6, 15)
print(f"   Carta Magna: 15/6/1215 juliano fue {DIAS[mc % 7]}; 15/6/2015 gregoriano fue {DIAS[mg % 7]}")
# solo saltos de 400 u 800 años, para que la única diferencia sea el desfase juliano-gregoriano
for a_, m_, d_, a2 in ((1066, 10, 14, 1866), (1321, 9, 14, 2121), (1492, 10, 12, 1892)):
    print(f"   {d_}/{m_}/{a_} juliano fue {DIAS[jdn_juliano(a_, m_, d_) % 7]}; "
          f"{d_}/{m_}/{a2} gregoriano fue {DIAS[jdn_gregoriano(a2, m_, d_) % 7]}  (desfase {jdn_juliano(a_, m_, d_) - jdn_gregoriano(a_, m_, d_)} días)")
# equinoccios de otoño
eq1226 = ephem.next_autumn_equinox(djd(jdn_juliano(1226, 9, 1)))
eq2026 = ephem.next_autumn_equinox(ephem.Date("2026/9/1"))
print(f"   equinoccio de 1226: {eq1226} TU (fecha juliana); el 3/10 a mediodía estaba {djd(j1226) - eq1226:4.1f} días después")
print(f"   equinoccio de 2026: {eq2026} TU; el 3/10 a mediodía está {djd(g2026) - eq2026:4.1f} días después")
# qué fecha gregoriana de 2026 tiene el Sol donde estaba el 3/10/1226 juliano
s = ephem.Sun(); s.compute(djd(j1226, 0.2)); lon1226 = math.degrees(ephem.Ecliptic(s, epoch=djd(j1226, 0.2)).lon)
for d in range(1, 20):
    t = ephem.Date(f"2026/10/{d} 16:48")
    s.compute(t); l = math.degrees(ephem.Ecliptic(s, epoch=t).lon)
    if abs(l - lon1226) < 0.5:
        print(f"   longitud del Sol a la puesta del 3/10/1226: {lon1226:.2f}°; la misma el {d}/10/2026 ({l:.2f}°), {DIAS[jdn_gregoriano(2026,10,d) % 7]}")

# la hora octava de Buenos Aires hoy (cuaderno del 1/10) y la primera hora de la noche de Asís, en hora de Buenos Aires
ba = ephem.Observer(); ba.lat, ba.lon, ba.elevation = "-34.6037", "-58.3816", 25
ba.date = "2026/10/3 15:00"
sal = ba.previous_rising(sol); pue = ba.next_setting(sol)
h = (pue - sal) / 12
def art(d):
    x = ((d + 0.5) % 1) * 24 - 3
    return f"{int(x % 24):02d}:{int(round((x % 1) * 60)) % 60:02d}"
print(f"   Buenos Aires hoy: sale {art(sal)}, se pone {art(pue)}; hora octava de {art(ephem.Date(sal + 7*h))} a {art(ephem.Date(sal + 8*h))}")
