#!/usr/bin/env python3
"""bernabe.py — el solsticio de junio de 1580 y el día de san Bernabé en Buenos Aires.
Necesita: pip install ephem.  Uso: python3 bernabe.py
PyEphem usa el calendario juliano antes del 15/10/1582 y el gregoriano después,
así que las fechas de 1580 que imprime ya están en juliano.
"""
import ephem, math

BA = ("-34.6083", "-58.3712")      # Plaza de Mayo
LON_H = -58.3712 / 15.0            # horas de diferencia con Greenwich (tiempo solar medio)

def obs(fecha):
    o = ephem.Observer(); o.lat, o.lon = BA; o.elevation = 0
    o.pressure = 0; o.horizon = "-0:34"      # criterio de los almanaques: refracción fija de 34', borde superior del disco
    o.date = fecha
    return o

def largo_del_dia(fecha_mediodia_ut):
    o = obs(fecha_mediodia_ut)
    sol = ephem.Sun()
    sale = o.previous_rising(sol); pone = o.next_setting(sol)
    return sale, pone, (pone - sale) * 24.0

def hm(h):
    m = int(round(h * 60)); return "%d h %02d min" % (m // 60, m % 60)

def local(d):
    """hora solar media de Buenos Aires"""
    return ephem.Date(d + LON_H / 24.0)

print("== solsticios y equinoccios de 1580 (fechas julianas, UT) ==")
print("equinoccio de marzo :", ephem.next_equinox("1580/1/1"))
s = ephem.next_solstice("1580/3/20")
print("solsticio de junio  :", s, " | hora solar media de Buenos Aires:", local(s))
print("solsticio de dic.   :", ephem.next_solstice("1580/9/1"))
print("san Bernabé, 11/6/1580 (jul.), 0 h local = ", ephem.Date(ephem.Date("1580/6/11") - LON_H / 24.0), "UT")
dif = (s - (ephem.Date("1580/6/11 12:00") - LON_H / 24.0)) * 24
print("del mediodía local del 11 de junio al solsticio: %.1f horas" % dif)

print("\n== largo del día en Buenos Aires, junio de 1580 (juliano) ==")
for d in range(1, 31):
    f = "1580/6/%d 16:00" % d          # ~mediodía local
    sale, pone, h = largo_del_dia(f)
    marca = "  <- san Bernabé, fundación" if d == 11 else ""
    if d in (1, 5, 9, 10, 11, 12, 13, 14, 17, 21, 25, 30):
        print("%2d de junio: sale %s  se pone %s  día %s (%.4f h)%s" % (
            d, str(local(sale))[-8:-3], str(local(pone))[-8:-3], hm(h), h, marca))

print("\n== el más corto del año ==")
mejor = min(((largo_del_dia("1580/6/%d 16:00" % d)[2], d) for d in range(1, 31)))
print("día más corto: %d de junio (jul.), %s" % (mejor[1], hm(mejor[0])))
sale, pone, h = largo_del_dia("1580/12/11 16:00")
print("y el más largo, cerca del 11 de diciembre (jul.): %s" % hm(h))

print("\n== lo mismo en Londres, para el refrán de Barnaby ==")
def londres(f):
    o = ephem.Observer(); o.lat, o.lon = "51.5074", "-0.1278"; o.pressure = 0; o.horizon = "-0:34"; o.date = f
    sol = ephem.Sun(); return (o.next_setting(sol) - o.previous_rising(sol)) * 24
for d in (1, 11, 12, 21):
    print("%2d de junio de 1580 (jul.), Londres: %s" % (d, hm(londres("1580/6/%d 12:00" % d))))

print("\n== y hoy ==")
print("solsticio de junio de 2026:", ephem.next_solstice("2026/1/1"), "UT")
sale, pone, h = largo_del_dia("2026/6/11 16:00"); print("11/6/2026 en Buenos Aires:", hm(h))
sale, pone, h = largo_del_dia("2026/6/21 16:00"); print("21/6/2026 en Buenos Aires:", hm(h))
sale, pone, h = largo_del_dia("2026/10/8 16:00"); print(" 8/10/2026 en Buenos Aires:", hm(h))
