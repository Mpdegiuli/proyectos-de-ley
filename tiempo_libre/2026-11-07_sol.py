#!/usr/bin/env python3
"""sol.py — altura del Sol sobre Ensisheim el 7 de noviembre de 1492 (juliano),
que es el 16 de noviembre de 1492 del calendario gregoriano proléptico, entre
las 11 y las 12 de la mañana (hora solar local, que es la que tenía el pueblo).

Algoritmo: posición solar de baja precisión (Meeus, cap. 25 abreviado), más que
suficiente para una altura en grados. Sin dependencias.
"""
import math

LAT, LON = 47.866, 7.351   # Ensisheim

def jdn_greg(y, m, d):
    a = (14 - m) // 12; y2 = y + 4800 - a; m2 = m + 12 * a - 3
    return d + (153 * m2 + 2) // 5 + 365 * y2 + y2 // 4 - y2 // 100 + y2 // 400 - 32045

def altura_sol(jd):
    T = (jd - 2451545.0) / 36525.0
    L0 = (280.46646 + 36000.76983 * T) % 360
    M = math.radians((357.52911 + 35999.05029 * T) % 360)
    C = (1.914602 - 0.004817 * T) * math.sin(M) + 0.019993 * math.sin(2 * M) + 0.000289 * math.sin(3 * M)
    lam = math.radians(L0 + C)
    eps = math.radians(23.439291 - 0.0130042 * T)
    dec = math.asin(math.sin(eps) * math.sin(lam))
    y = math.tan(eps / 2) ** 2
    L0r = math.radians(L0)
    eot = 4 * math.degrees(y * math.sin(2 * L0r) - 2 * 0.016708634 * math.sin(M)
                           + 4 * 0.016708634 * y * math.sin(M) * math.cos(2 * L0r)
                           - 0.5 * y * y * math.sin(4 * L0r) - 1.25 * 0.016708634 ** 2 * math.sin(2 * M))
    return dec, eot

def main():
    jdn = jdn_greg(1492, 11, 16)           # mediodía de ese día en TT ~ UT
    dec, eot = altura_sol(jdn)             # declinación al mediodía
    print(f"7/11/1492 juliano = 16/11/1492 gregoriano; JDN {jdn}")
    print(f"declinación del Sol: {math.degrees(dec):.1f}°")
    lat = math.radians(LAT)
    for hora_solar in (11.0, 11.5, 12.0):
        H = math.radians((hora_solar - 12.0) * 15.0)   # ángulo horario, hora solar aparente
        alt = math.asin(math.sin(lat) * math.sin(dec) + math.cos(lat) * math.cos(dec) * math.cos(H))
        print(f"hora solar {hora_solar:4.1f}: altura del Sol {math.degrees(alt):.1f}°")
    # salida y puesta del sol (hora solar aparente)
    cosH0 = (math.sin(math.radians(-0.833)) - math.sin(lat) * math.sin(dec)) / (math.cos(lat) * math.cos(dec))
    H0 = math.degrees(math.acos(cosH0)) / 15
    print(f"día de {2*H0:.1f} horas de sol; salida a las {12-H0:.2f} y puesta a las {12+H0:.2f} (hora solar)")

if __name__ == "__main__":
    main()
