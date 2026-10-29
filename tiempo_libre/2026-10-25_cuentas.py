#!/usr/bin/env python3
"""Cuentas del cuaderno del 25/10/2026: fechas julianas y las sesenta millas.

Solo biblioteca estándar. Salida: salida_cuentas.txt (por stdout).
"""
from math import asin, cos, radians, sin, sqrt

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def jdn_juliano(anio: int, mes: int, dia: int) -> int:
    """Día juliano (JDN) de una fecha del calendario juliano (proléptico).
    Fórmula de Fliegel y Van Flandern para el calendario juliano."""
    a = (14 - mes) // 12
    y = anio + 4800 - a
    m = mes + 12 * a - 3
    return dia + (153 * m + 2) // 5 + 365 * y + y // 4 - 32083


def jdn_gregoriano(anio: int, mes: int, dia: int) -> int:
    a = (14 - mes) // 12
    y = anio + 4800 - a
    m = mes + 12 * a - 3
    return dia + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045


def dia_semana(jdn: int) -> str:
    return DIAS[jdn % 7]  # JDN % 7 == 0 es lunes


def haversine_km(lat1, lon1, lat2, lon2) -> float:
    r = 6371.0
    p1, p2 = radians(lat1), radians(lat2)
    dp, dl = radians(lat2 - lat1), radians(lon2 - lon1)
    h = sin(dp / 2) ** 2 + cos(p1) * cos(p2) * sin(dl / 2) ** 2
    return 2 * r * asin(sqrt(h))


print("1. Fechas (calendario juliano, el de Inglaterra hasta 1752)")
muerte = jdn_juliano(1400, 10, 25)
alquiler = jdn_juliano(1399, 12, 24)
cobro = jdn_juliano(1400, 6, 5)
print(f"   25/10/1400 fue {dia_semana(muerte)} (JDN {muerte})")
print(f"   24/12/1399 (alquiler) fue {dia_semana(alquiler)}")
print(f"   5/6/1400 (último cobro) fue {dia_semana(cobro)}")
print(f"   del alquiler a la muerte: {muerte - alquiler} días "
      f"({(muerte - alquiler) / 365.25:.2f} años)")
print(f"   del último cobro a la muerte: {muerte - cobro} días")
print(f"   el alquiler de 53 años vencía el 24/12/1452; Chaucer usó "
      f"{(muerte - alquiler) / (53 * 365.25) * 100:.1f} % del plazo")
sueno = jdn_juliano(1383, 12, 10)
print(f"   10/12/1383 (la fecha del sueño, si el año es 1383) fue {dia_semana(sueno)}")
for anio in (1379, 1380, 1381, 1382, 1384):
    print(f"   10/12/{anio} fue {dia_semana(jdn_juliano(anio, 12, 10))}")
hoy_g = jdn_gregoriano(2026, 10, 25)
print(f"   25/10/2026 gregoriano es JDN {hoy_g}, {dia_semana(hoy_g)}; "
      f"han pasado {hoy_g - muerte} días desde el 25/10/1400 juliano "
      f"({(hoy_g - muerte) / 365.2425:.2f} años)")
# El 25 de octubre juliano de 2026 cae 13 días después en el gregoriano
jul_2026 = jdn_juliano(2026, 10, 25)
print(f"   el 25/10/2026 juliano es el JDN {jul_2026}, o sea "
      f"{jul_2026 - hoy_g} días después del 25/10/2026 gregoriano (7 de noviembre)")

print()
print("2. Sesenta millas")
for nombre, metros in (("milla terrestre de hoy (1593)", 1609.344),
                       ("milla de 5.000 pies", 1524.0),
                       ("milla romana (mille passus, 1.480 m aprox.)", 1480.0)):
    print(f"   60 × {nombre}: {60 * metros / 1000:.1f} km")
# Southwark (Tabard Inn, aprox.) y la catedral de Canterbury
d = haversine_km(51.5020, -0.0905, 51.2798, 1.0830)
print(f"   Southwark–Canterbury en línea recta: {d:.1f} km = {d / 1.609344:.1f} millas de hoy")
# Westminster–Canterbury
d2 = haversine_km(51.4993, -0.1273, 51.2798, 1.0830)
print(f"   Westminster–Canterbury en línea recta: {d2:.1f} km = {d2 / 1.609344:.1f} millas de hoy")

print()
print("3. El poema")
print("   2.158 versos conservados (Fairfax 16 y Bodley 638); el ejemplar de Caxton terminaba en el 2.094:")
print(f"   faltaban {2158 - 2094} versos; Caxton agregó 12 propios.")
print(f"   La casa de los rumores ocupa los versos 1.918 a 2.158: {2158 - 1918 + 1} versos, "
      f"{(2158 - 1918 + 1) / 2158 * 100:.1f} % del poema.")
