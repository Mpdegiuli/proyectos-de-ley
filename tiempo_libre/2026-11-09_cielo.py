#!/usr/bin/env python3
"""El cielo sobre Nueva York y sobre Queenston el 9 de noviembre de 1965, y la luna de hoy.
Necesita `pip install ephem`. Escribe salida_cielo.txt (y la imprime)."""
import ephem

EST = 5 * ephem.hour  # hora del este, sin horario de verano (noviembre)

def est(d):
    return ephem.Date(d - EST)

lineas = []
p = lineas.append
p(f"Luna llena anterior al 9/11/1965: {ephem.previous_full_moon(ephem.Date('1965/11/09 23:59'))} UTC "
  f"= {est(ephem.previous_full_moon(ephem.Date('1965/11/09 23:59')))} hora del este")
p(f"Luna nueva siguiente: {ephem.next_new_moon(ephem.Date('1965/11/09'))} UTC")

nyc = ephem.Observer()
nyc.lat, nyc.lon, nyc.elevation = '40.7128', '-74.0060', 10
nyc.date = ephem.Date('1965/11/09 12:00')
p(f"Nueva York, puesta del Sol: {est(nyc.next_setting(ephem.Sun()))} EST")
nyc.date = ephem.Date('1965/11/09 12:00')
p(f"Nueva York, salida de la Luna: {est(nyc.next_rising(ephem.Moon()))} EST")
for hhmm in ("17:16", "17:27", "22:00"):
    nyc.date = ephem.Date(f'1965/11/09 {hhmm}') + EST
    m, s = ephem.Moon(nyc), ephem.Sun(nyc)
    p(f"Nueva York {hhmm} EST: Luna alt {ephem.degrees(m.alt)} az {ephem.degrees(m.az)} iluminada {m.phase:.1f} %; "
      f"Sol alt {ephem.degrees(s.alt)}")

q = ephem.Observer()
q.lat, q.lon = '43.16', '-79.05'   # Queenston, Ontario
q.date = ephem.Date('1965/11/09 12:00')
p(f"Queenston, puesta del Sol: {est(q.next_setting(ephem.Sun()))} EST")
q.date = ephem.Date('1965/11/09 12:00')
p(f"Queenston, salida de la Luna: {est(q.next_rising(ephem.Moon()))} EST")
q.date = ephem.Date('1965/11/09 17:16') + EST
p(f"Queenston 17:16 EST: Sol alt {ephem.degrees(ephem.Sun(q).alt)}, Luna alt {ephem.degrees(ephem.Moon(q).alt)}")

p(f"Hoy, 9/11/2026: luna nueva a las {ephem.next_new_moon(ephem.Date('2026/11/08'))} UTC")
ba = ephem.Observer(); ba.lat, ba.lon = '-34.6', '-58.4'
ba.date = ephem.Date('2026/11/09 09:51')
p(f"Buenos Aires 9/11/2026 6:51: Luna iluminada {ephem.Moon(ba).phase:.2f} %")

txt = "\n".join(lineas)
open("salida_cielo.txt", "w").write(txt + "\n")
print(txt)

# El control de la propuesta 2: la luna sobre Nueva York las tardes del 9 de noviembre de otros años
with open("salida_cielo.txt", "a") as fh:
    fh.write("\nLuna sobre Nueva York a las 17:30 EST del 9 de noviembre, por año (iluminación, altura):\n")
    for anio in range(1958, 1972):
        nyc.date = ephem.Date(f'{anio}/11/09 17:30') + EST
        m = ephem.Moon(nyc)
        linea = f"  {anio}: {m.phase:5.1f} %  alt {float(m.alt) * 180 / 3.141592653589793:6.1f}°"
        fh.write(linea + "\n")
        print(linea)
