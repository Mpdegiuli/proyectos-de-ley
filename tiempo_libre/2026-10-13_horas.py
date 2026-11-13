#!/usr/bin/env python3
"""Roma, 13 de octubre del 54 (juliano): las horas desiguales del día en que
se anunció la muerte de Claudio, y el cielo del mediodía.

Pide `pip install ephem`. Las fechas se arman con el día juliano para no depender
de cómo cada biblioteca trata el calendario antes de 1582.
Todo se da en hora solar verdadera de Roma (mediodía = paso del Sol por el meridiano),
que es la de un reloj de sol y no depende de ΔT más que en segundos.
"""
import math
import ephem

def jdn_juliano(a, m, d):
    """Día juliano (a mediodía) de una fecha del calendario juliano."""
    aa = (14 - m) // 12
    y = a + 4800 - aa
    mm = m + 12 * aa - 3
    return d + (153 * mm + 2) // 5 + 365 * y + y // 4 - 32083

def gregoriano_de_jdn(j):
    a = j + 32044
    b = (4 * a + 3) // 146097
    c = a - 146097 * b // 4
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m = (5 * e + 2) // 153
    return (100 * b + d - 4800 + m // 10, m + 3 - 12 * (m // 10), e - (153 * m + 2) // 5 + 1)

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
SIGNOS = ["Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio",
          "Sagitario", "Capricornio", "Acuario", "Piscis"]
DJD0 = 2415020.0   # día juliano del origen de fechas de PyEphem (31/12/1899, 12 h)

def main():
    J = jdn_juliano(54, 10, 13)
    print("Día juliano del 13/10/54 (juliano), a mediodía:", J)
    print("Día de la semana (cuenta continua):", DIAS[J % 7])
    print("Fecha gregoriana proléptica:", gregoriano_de_jdn(J))
    J2026 = jdn_juliano(2026, 9, 30)   # 13/10/2026 gregoriano = 30/9/2026 juliano
    assert gregoriano_de_jdn(J2026) == (2026, 10, 13)
    print("Días hasta el 13/10/2026:", J2026 - J, "=", (J2026 - J) // 7, "semanas y", (J2026 - J) % 7, "días")
    print("Años:", 2026 - 54)

    roma = ephem.Observer()
    roma.lat, roma.lon, roma.elevation = "41.8925", "12.4853", 40   # Palatino
    roma.pressure = 0        # sin esto ephem suma su propia refracción a la del horizonte
    roma.horizon = "-0:34"   # refracción estándar en el horizonte; el borde lo pone ephem
    roma.date = (J - 0.5) - DJD0 + 0.2   # madrugada del 13, en TU aproximado
    sol = ephem.Sun()
    salida = roma.next_rising(sol)
    transito = roma.next_transit(sol, start=salida)
    puesta = roma.next_setting(sol, start=salida)

    def hsv(t):
        """Hora solar verdadera de una fecha ephem, tomando el tránsito como 12:00."""
        m = round((12 + (t - transito) * 24) * 60)
        return f"{m // 60:02d}:{m % 60:02d}"

    dia = (puesta - salida) * 24
    hora = dia / 12
    print(f"\nSalida del Sol {hsv(salida)}, puesta {hsv(puesta)} (hora solar verdadera)")
    print(f"Duración del día: {int(dia)} h {round((dia - int(dia)) * 60)} min; hora desigual de día: {hora * 60:.1f} min; de noche: {(24 - dia) / 12 * 60:.1f} min")
    for n in range(1, 13):
        a = ephem.Date(salida + (n - 1) * hora / 24)
        b = ephem.Date(salida + n * hora / 24)
        print(f"  hora {n:2d}: {hsv(a)} a {hsv(b)}")
    medio = ephem.Date((salida + puesta) / 2)
    print("Punto medio entre salida y puesta:", hsv(medio), "(el tránsito es 12:00 por definición)")

    # El cielo a mediodía verdadero
    roma.date = transito
    print("\nCielo de Roma al mediodía verdadero (longitudes eclípticas de la fecha):")
    def ecl(c):
        e = ephem.Ecliptic(c, epoch=roma.date)
        return math.degrees(e.lon)
    for nombre, cuerpo in [("Sol", ephem.Sun()), ("Luna", ephem.Moon()), ("Mercurio", ephem.Mercury()),
                           ("Venus", ephem.Venus()), ("Marte", ephem.Mars()), ("Júpiter", ephem.Jupiter()),
                           ("Saturno", ephem.Saturn())]:
        cuerpo.compute(roma)
        lon = ecl(cuerpo)
        extra = f", iluminada {cuerpo.phase:.0f} %" if nombre == "Luna" else ""
        print(f"  {nombre:9s} {lon:6.1f}°  {SIGNOS[int(lon // 30)]:11s} {lon % 30:4.1f}°   altura {math.degrees(cuerpo.alt):5.1f}°, acimut {math.degrees(cuerpo.az):5.1f}°{extra}")
    # ascendente: punto de la eclíptica que sale por el este
    ramc = roma.sidereal_time()
    eps = math.radians(23.69)    # oblicuidad hacia el año 54
    lat = float(roma.lat)
    asc = math.degrees(math.atan2(math.cos(ramc), -(math.sin(ramc) * math.cos(eps) + math.tan(lat) * math.sin(eps)))) % 360
    mc = math.degrees(math.atan2(math.sin(ramc), math.cos(ramc) * math.cos(eps))) % 360
    print(f"  Ascendente {asc:6.1f}°  {SIGNOS[int(asc // 30)]} {asc % 30:.1f}°;  medio cielo {mc:6.1f}°  {SIGNOS[int(mc // 30)]} {mc % 30:.1f}°")
    luna = ephem.Moon(); luna.compute(roma)
    print("  Luna nueva anterior:", ephem.previous_new_moon(roma.date), " llena siguiente:", ephem.next_full_moon(roma.date), "(TU de ephem, calendario según ephem)")
    # "prope lucem": comienzo del crepúsculo civil y salida
    roma.horizon = "-6"
    alba = roma.previous_rising(ephem.Sun(), use_center=True)
    print("\nAlba civil (Sol a -6°):", hsv(alba), " salida:", hsv(salida), " -> de la salida al mediodía:", f"{(transito - salida) * 24:.2f} h")


if __name__ == "__main__":
    main()
