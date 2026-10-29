#!/usr/bin/env python3
"""Las lunas de Marte de Swift (1726) contra las de Hall (1877).

Cuaderno de tiempo libre del 28/10/2026. Solo biblioteca estándar.

Datos de Swift (Gulliver, parte III, cap. 3): dos satélites, el interior a tres
diámetros del centro de Marte, el exterior a cinco; períodos de diez horas y
veintiuna y media; "los cuadrados de los tiempos periódicos están casi en la
misma proporción que los cubos de las distancias".

Datos reales (Wikipedia, "Moons of Mars" y "Deimos (moon)", leídos hoy):
Fobos, semieje 9.377 km, período 7,66 h (uso 7,6538 h = 0,31891 días, el período sidéreo de la hoja de datos planetarios de la NASA);
Deimos, semieje 23.457,5 km, período 30,2984 h.
Marte: radio medio 3.389,5 km (diámetro 6.779 km), GM = 4,2828e13 m³/s²,
rotación sidérea 24 h 37 min 22,7 s = 24,6229 h. Estos tres los tengo de memoria
(hoja de datos planetarios de la NASA); el cuaderno dice cuáles son.
"""
import math

# --- Swift -----------------------------------------------------------------
D_KM = 6779.0            # diámetro medio de Marte, km
GM_MARS = 4.2828e13      # m³/s²
T_ROT_H = 24.6229        # rotación sidérea de Marte, horas
G = 6.674e-11
M_MARS = GM_MARS / G
M_EARTH = 5.972e24

swift = [("interior", 3.0, 10.0), ("exterior", 5.0, 21.5)]
hall = [("Fobos", 9377.0 / D_KM, 7.6538), ("Deimos", 23457.5 / D_KM, 30.2984)]

print("1. La tercera ley de Kepler en los números de Swift")
for nombre, a, t in swift:
    print(f"   {nombre}: a = {a} diámetros, T = {t} h, a³/T² = {a**3/t**2:.5f}")
k1 = 27 / 100
k2 = 125 / 21.5**2
print(f"   diferencia entre las dos razones: {100*abs(k1-k2)/k1:.2f} %")
t2 = 10 * (5 / 3) ** 1.5
print(f"   si el interior tarda 10 h a 3 diámetros, el exterior a 5 tarda 10·(5/3)^(3/2) = {t2:.3f} h")
print("   en medias horas: 20 y 43; 5³·20² = %d y 3³·43² = %d (la observación es de mathpages.com)" % (125 * 400, 27 * 43 * 43))
for nombre, a, t in hall:
    print(f"   {nombre}: a = {a:.3f} diámetros, T = {t} h, a³/T² = {a**3/t**2:.5f}")

print()
print("2. La masa de Marte que piden los números de Swift")
for nombre, a, t in swift:
    a_m = a * D_KM * 1000
    t_s = t * 3600
    gm = 4 * math.pi**2 * a_m**3 / t_s**2
    print(f"   {nombre}: GM = {gm:.3e} m³/s², {gm/GM_MARS:.2f} veces la real; masa = {gm/G:.2e} kg = {gm/G/M_EARTH:.2f} masas terrestres")
print(f"   (Marte real: GM = {GM_MARS:.4e}, masa {M_MARS:.3e} kg = {M_MARS/M_EARTH:.3f} masas terrestres)")

print()
print("3. Por dónde salen: período sinódico visto desde el suelo de Marte")
print(f"   rotación sidérea de Marte: {T_ROT_H} h")
def sinodico(t_orb):
    # 1/P = 1/T_orb - 1/T_rot ; positivo = la luna le gana a la rotación: sale por el oeste
    x = 1 / t_orb - 1 / T_ROT_H
    return (1 / x if x else float("inf"))
for grupo, lista in (("Swift", swift), ("Hall", hall)):
    for nombre, a, t in lista:
        p = sinodico(t)
        lado = "oeste" if p > 0 else "este"
        print(f"   {grupo:5s} {nombre:9s}: T = {t:7.4f} h {'<' if t < T_ROT_H else '>'} día marciano -> sale por el {lado}; de salida a salida {abs(p):.1f} h = {abs(p)/24:.2f} días")

print()
print("4. La órbita estacionaria del Marte real")
a_sync = (GM_MARS * (T_ROT_H * 3600) ** 2 / (4 * math.pi**2)) ** (1 / 3) / 1000
print(f"   a = (GM·T²/4π²)^(1/3) = {a_sync:,.0f} km = {a_sync/D_KM:.3f} diámetros = {2*a_sync/D_KM:.2f} radios")
print(f"   la luna interior de Swift está a 3 diámetros: a {100*(3*D_KM-a_sync)/a_sync:+.1f} % de esa órbita")
t_at_3d = 2 * math.pi * math.sqrt((3 * D_KM * 1000) ** 3 / GM_MARS) / 3600
print(f"   una luna a 3 diámetros del Marte real tardaría {t_at_3d:.2f} h (Swift dice 10)")
t_at_5d = 2 * math.pi * math.sqrt((5 * D_KM * 1000) ** 3 / GM_MARS) / 3600
print(f"   una a 5 diámetros, {t_at_5d:.2f} h (Swift dice 21,5)")

print()
print("5. Fechas")
def jdn_juliano(y, m, d):
    a = (14 - m) // 12
    y2 = y + 4800 - a
    m2 = m + 12 * a - 3
    return d + (153 * m2 + 2) // 5 + 365 * y2 + y2 // 4 - 32083
def jdn_gregoriano(y, m, d):
    a = (14 - m) // 12
    y2 = y + 4800 - a
    m2 = m + 12 * a - 3
    return d + (153 * m2 + 2) // 5 + 365 * y2 + y2 // 4 - y2 // 100 + y2 // 400 - 32045
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
j = jdn_juliano(1726, 10, 28)
g = jdn_gregoriano(2026, 10, 28)
print(f"   28/10/1726 (juliano, el calendario de Londres): JDN {j}, {dias[j % 7]}; en gregoriano, 8/11/1726")
print(f"   días hasta el 28/10/2026: {g - j:,}")
h = jdn_gregoriano(1877, 8, 12)
print(f"   del 28/10/1726 al 12/8/1877 (Hall ve Deimos): {h - j:,} días = {(h - j)/365.2425:.1f} años")
