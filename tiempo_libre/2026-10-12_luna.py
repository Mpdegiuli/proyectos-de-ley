#!/usr/bin/env python3
"""luna.py - el cielo de la noche del 11 al 12 de octubre de 1492 (calendario juliano)
frente a Watling/San Salvador. Cuaderno de tiempo libre del 12/10/2026.

Las horas son hora solar media del lugar (TU + longitud/15), no hora de huso.
El resultado casi no cambia si se pone otra de las islas candidatas: se imprime
también para el Gran Turco. Necesita: pip install ephem
"""
import math, ephem

def jdn_juliano(a, m, d):
    x = (14 - m) // 12; y = a + 4800 - x; mm = m + 12 * x - 3
    return d + (153 * mm + 2) // 5 + 365 * y + y // 4 - 32083

def jdn_gregoriano(a, m, d):
    x = (14 - m) // 12; y = a + 4800 - x; mm = m + 12 * x - 3
    return d + (153 * mm + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
j = jdn_juliano(1492, 10, 12)
print(f"12/10/1492 juliano: día juliano {j}, {DIAS[j % 7]}; "
      f"en gregoriano proléptico, {j - jdn_gregoriano(1492, 10, 1) + 1}/10/1492")
g = jdn_gregoriano(2026, 10, 12)
print(f"12/10/2026 gregoriano: día juliano {g}, {DIAS[g % 7]}; días entre los dos: {g - j}")

def fecha(jdn, hora_local, lon):
    """fecha de PyEphem (TU) para una hora solar media local del día civil jdn"""
    return ephem.Date(jdn - 2415020 - 0.5 + (hora_local - lon / 15.0) / 24.0)

def hlocal(d, lon):
    h = ((float(d) + 0.5) % 1) * 24 + lon / 15.0
    h %= 24
    return f"{int(h):02d}:{int(round((h - int(h)) * 60)) % 60:02d}"

for nombre, lat, lon in (("Watling", 24.02, -74.34), ("Gran Turco", 21.43, -71.14)):
    o = ephem.Observer(); o.lat, o.lon = str(lat), str(lon); o.elevation = 5; o.pressure = 1010
    sol, luna = ephem.Sun(), ephem.Moon()
    print(f"\n{nombre} ({lat} N, {-lon} O)")
    o.date = fecha(j - 1, 12, lon)                      # mediodía del 11
    puesta = o.next_setting(sol); print(f"  puesta del Sol del 11:   {hlocal(puesta, lon)}")
    o.date = puesta
    sale = o.next_rising(luna); print(f"  salida de la Luna:       {hlocal(sale, lon)}")
    for etiqueta, h, dia in (("22:00 del 11 (la lumbre)", 22, j - 1), ("02:00 del 12 (la tierra)", 2, j)):
        o.date = fecha(dia, h, lon); luna.compute(o); sol.compute(o)
        print(f"  {etiqueta}: Luna a {math.degrees(luna.alt):5.1f}° de altura, acimut {math.degrees(luna.az):5.1f}°, "
              f"iluminada {luna.phase:4.1f} %; Sol a {math.degrees(sol.alt):6.1f}°")
    o.date = fecha(j, 2, lon)
    print(f"  salida del Sol del 12:   {hlocal(o.next_rising(sol), lon)}")
    o.date = fecha(j, 2, lon)
    pl = ephem.previous_full_moon(o.date); cm = ephem.next_last_quarter_moon(o.date)
    print(f"  Luna llena anterior: {o.date - pl:.1f} días antes; cuarto menguante: {cm - o.date:.1f} días después")
