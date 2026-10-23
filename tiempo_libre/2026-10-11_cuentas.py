#!/usr/bin/env python3
"""cuentas.py - Las cuentas chicas del cuaderno del 11/10/2026 (no necesita nada).

1. El horizonte: hasta dónde asoma una luz según la altura del ojo y la de la luz.
2. La franja del veedor: a qué distancias una luz baja se ve desde la toldilla y no
   desde la cubierta.
3. La velocidad: lo que dicen las cifras del asiento entre sí.
4. El premio contra el sueldo.
5. El experimento de Wolper (1959) contra la misma geometría.
6. El feriado: a qué día lo lleva cada norma según el día de la semana del 12.
"""
import math, datetime

K = 3.86          # km por raíz de metro, con refracción normal (3,57 sin refracción)
def alcance(ojo, luz): return K * (math.sqrt(ojo) + math.sqrt(luz))
def altura(d, ojo): r = d / K - math.sqrt(ojo); return 0 if r <= 0 else r * r

print("1. EL HORIZONTE")
# memoria de 1892: de la quilla a la cubierta de la toldilla 8,00 m; calado a popa 3,02 m; medio 2,60 m
toldilla = 8.00 - 3.02
cubierta = 3.80 - 2.60
ojo_t, ojo_c = toldilla + 1.55, cubierta + 1.55
print(f"   cubierta de la toldilla sobre el agua: {toldilla:.2f} m  -> ojo a {ojo_t:.2f} m")
print(f"   cubierta principal sobre el agua (calado medio): {cubierta:.2f} m  -> ojo a {ojo_c:.2f} m")
for nombre, ojo in (("Link y Link, cubierta a 14 pies", 14 * 0.3048 + 1.55), ("memoria de 1892", ojo_t), ("Verhoog, ojo a 30 pies", 30 * 0.3048)):
    print(f"   {nombre:32s} ojo {ojo:4.1f} m: horizonte {K*math.sqrt(ojo):4.1f} km; "
          f"para ver a 71 km la luz tiene que estar a {altura(71.04, ojo):.0f} m; a 59,4 km, a {altura(59.42, ojo):.0f} m")
print(f"   sin refracción (3,57), ojo a 6,5 m, a 71 km: {((71.04/3.57)-math.sqrt(6.5))**2:.0f} m")
print(f"   punto más alto de las Bahamas, 63 m: asoma hasta {alcance(6.5, 63):.1f} km")
print(f"   High Cay, 114 pies = {114*0.3048:.1f} m: asoma hasta {alcance(6.5, 114*0.3048):.1f} km")

print("\n2. LA FRANJA DEL VEEDOR (una luz a 2 m del agua: un tizón en la mano, en una playa o en una canoa)")
a, b = alcance(ojo_c, 2), alcance(ojo_t, 2)
print(f"   desde la cubierta principal se ve hasta {a:.1f} km; desde la toldilla, hasta {b:.1f} km")
print(f"   entre {a:.1f} y {b:.1f} km ({b-a:.1f} km de ancho) la ve solo el que está arriba")
v = 12 * 1.480
print(f"   a 12 millas por hora ({v:.1f} km/h) esa franja se cruza de frente en {(b-a)/v*60:.0f} minutos")
for ola in (2, 3, 4):
    lo, hi = alcance(ojo_t - ola / 2, 2), alcance(ojo_t + ola / 2, 2)
    print(f"   con olas de {ola} m el alcance desde la toldilla va y viene entre {lo:.1f} y {hi:.1f} km")

print("\n3. LA VELOCIDAD")
print(f"   12 millas por hora: {12*1.480:.1f} km/h = {12*1.480/1.852:.1f} nudos (milla de 1.480 m); "
      f"{12*1.238:.1f} km/h = {12*1.238/1.852:.1f} nudos (milla de 1.238 m)")
puesta = 17 + 44 / 60
print(f"   de la puesta del sol (17:44) a las dos van {26-puesta:.2f} h; a 12 millas serían {12*(26-puesta):.0f} millas, y el asiento dice 90")
print(f"   90 millas en ese tiempo son {90/(26-puesta):.1f} millas por hora; 90 millas a 12 por hora son {90/12:.1f} h: desde las {int(26-7.5)}:30")
print(f"   de las diez a las dos, a 12 por hora: 48 millas = {48*1.480:.1f} km ({48*1.480/1.852:.1f} millas náuticas); con las dos leguas, {56*1.480:.1f} km ({56*1.480/1.852:.1f} mn)")
print(f"   con la milla corta: {48*1.238:.1f} km ({48*1.238/1.852:.1f} mn); con las dos leguas, {56*1.238:.1f} km ({56*1.238/1.852:.1f} mn)")
print(f"   hasta puesto el sol, 27 leguas; después, 22 y media: {27+22.5} leguas = {(27+22.5)*4*1.480:.0f} km en el día")

print("\n4. EL PREMIO")
print(f"   10.000 maravedís por año contra 1.000 por mes de un marinero: {10000/1000:.0f} meses de sueldo por año, de por vida")
print(f"   contra 666 de un grumete: {10000/666:.0f} meses")
print(f"   de mayo de 1493 a mayo de 1506 van trece años: {13*10000:,} maravedís".replace(",", "."))

print("\n5. WOLPER, 21/10/1959")
ojo_w = 12.5 * 0.3048 + 0   # ella da la altura de la cubierta; el OCR deja dudas en la cifra
for luz_pies in (114, 200):
    print(f"   cubierta a 12,5 pies, luz a {luz_pies} pies: asoma hasta {alcance(12.5*0.3048+1.55, luz_pies*0.3048)/1.852:.1f} millas náuticas")
print(f"   para verse a 29 mn desde ahí, lo iluminado tiene que estar a {altura(29*1.852, 12.5*0.3048+1.55)/0.3048:.0f} pies")

print("\n6. EL FERIADO")
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
def ley27399(a):
    d = datetime.date(a, 10, 12); w = d.weekday()
    if w in (1, 2): return d - datetime.timedelta(days=w)          # martes y miércoles: al lunes anterior
    if w in (3, 4): return d + datetime.timedelta(days=7 - w)      # jueves y viernes: al lunes siguiente
    return d
def decreto1584(a):
    d = datetime.date(a, 10, 1); return d + datetime.timedelta(days=(7 - d.weekday()) % 7 + 7)   # segundo lunes
for a in range(2020, 2031):
    d = datetime.date(a, 10, 12)
    print(f"   {a}: el 12 cae {dias[d.weekday()]:9s} | ley 27.399: {ley27399(a).day:2d}/10 | segundo lunes (decreto 1584/2010): {decreto1584(a).day:2d}/10")
en12 = sum(1 for a in range(2018, 2418) if ley27399(a).day == 12)
print(f"   en 400 años de ley 27.399 el feriado cae el 12 en {en12} (los años en que el 12 es lunes, sábado o domingo)")
