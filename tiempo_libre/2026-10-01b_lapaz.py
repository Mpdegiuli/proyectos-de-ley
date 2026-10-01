#!/usr/bin/env python3
"""En que dias del ano el Sol pasa al sur del cenit en La Paz (y entonces la sombra de un clavo
vertical gira como las agujas). Comparacion con Buenos Aires. Necesita: pip install ephem
Tiempo libre, 1/10/2026 (segunda sesion)."""
import ephem, math


def giro_del_dia(lat, lon, fecha_utc):
    o = ephem.Observer(); o.lat, o.lon, o.elevation = lat, lon, 0
    sol = ephem.Sun(); o.date = fecha_utc
    sal, pue = o.previous_rising(sol), o.next_setting(sol)
    pts = []
    for k in range(1, 48):
        o.date = ephem.Date(sal + (pue - sal) * k / 48.0); sol.compute(o)
        al, az = float(sol.alt), float(sol.az)
        e, n, u = math.cos(al) * math.sin(az), math.cos(al) * math.cos(az), math.sin(al)
        pts.append((-e / u, -n / u))
    # angulo total barrido por la sombra, con signo (positivo = antihorario visto desde arriba, norte arriba)
    tot = 0.0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        tot += math.atan2(x1 * y2 - x2 * y1, x1 * x2 + y1 * y2)
    o.date = sal; tr = o.next_transit(sol); o.date = tr; sol.compute(o)
    return math.degrees(tot), math.degrees(sol.az), math.degrees(sol.alt)


for nombre, lat, lon, huso in [("La Paz", "-16.4958", "-68.1335", 16), ("Buenos Aires", "-34.6037", "-58.3816", 15)]:
    prev, horario = None, 0
    d0 = ephem.Date(f"2026/1/1 {huso}:00")
    cambios = []
    for k in range(365):
        d = ephem.Date(d0 + k)
        g, az, alt = giro_del_dia(lat, lon, d)
        s = "horario" if g < 0 else "antihorario"
        if s == "horario": horario += 1
        if prev and s != prev:
            cambios.append((d.datetime().strftime("%d/%m"), s, round(alt, 1)))
        prev = s
    print(nombre, "- dias con giro horario en 2026:", horario, "- cambios:", cambios)
for f in ["2026/6/21 16:00", "2026/10/1 16:00", "2026/12/21 16:00"]:
    print("La Paz", f[:10], "giro %.0f grados, Sol al mediodia en acimut %.0f, altura %.1f" % giro_del_dia("-16.4958", "-68.1335", f))


# alrededor del 6/11/2025, cuando el reloj de la Asamblea volvio al sentido convencional
for dia in range(3, 12):
    g, az, alt = giro_del_dia("-16.4958", "-68.1335", f"2025/11/{dia} 16:00")
    print(f"La Paz {dia}/11/2025: giro {g:+.0f} grados ({'horario' if g < 0 else 'antihorario'}), Sol al mediodia a {alt:.1f} grados, acimut {az:.0f}")
