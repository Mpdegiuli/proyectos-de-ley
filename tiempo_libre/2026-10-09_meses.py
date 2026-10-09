#!/usr/bin/env python3
"""meses.py — ¿en qué día cae el día del hangul?

Reconstruye, con lunas nuevas calculadas (PyEphem), los meses lunares que importan:
  - el mes 12 del año gyehae (1443/44), el del "este mes el rey hizo las 28 letras";
  - el mes 9 del año byeongin (1446), el del "este mes se terminó el Hunminjeongeum";
  - el mes 9 de 1926, el del primer festejo.
y pasa los días a los dos calendarios, juliano y gregoriano (proléptico antes de 1582).

El día 1 de un mes lunar es el día civil en que cae la luna nueva. Uso la hora local
media de Seúl (longitud 126,98° E = UT + 8 h 28 min) para el siglo XV y UT + 9 h para
1926. Un calendario histórico podía diferir en un día del cálculo moderno: por eso
comparo además con el día sexagesimal que traen los Anales, que fija el día sin
depender de ninguna luna.

Uso: python3 meses.py        (necesita: pip install ephem)
"""
import math
import ephem

TRONCOS = "甲乙丙丁戊己庚辛壬癸"
RAMAS = "子丑寅卯辰巳午未申酉戌亥"
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]


def jdn_de_gregoriano(a, m, d):
    x = (14 - m) // 12
    y = a + 4800 - x
    mm = m + 12 * x - 3
    return d + (153 * mm + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045


def jdn_de_juliano(a, m, d):
    x = (14 - m) // 12
    y = a + 4800 - x
    mm = m + 12 * x - 3
    return d + (153 * mm + 2) // 5 + 365 * y + y // 4 - 32083


def gregoriano(jdn):
    a = jdn + 32044
    b = (4 * a + 3) // 146097
    c = a - 146097 * b // 4
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m = (5 * e + 2) // 153
    return (100 * b + d - 4800 + m // 10, m + 3 - 12 * (m // 10), e - (153 * m + 2) // 5 + 1)


def juliano(jdn):
    c = jdn + 32082
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m = (5 * e + 2) // 153
    return (d - 4800 + m // 10, m + 3 - 12 * (m // 10), e - (153 * m + 2) // 5 + 1)


def sexagesimal(jdn):
    n = (jdn - 11) % 60          # 0 = 甲子; control: 1/1/2000 (JDN 2451545) = 戊午
    return TRONCOS[n % 10] + RAMAS[n % 12]


def semana(jdn):
    return DIAS[jdn % 7]          # JDN 0 fue lunes


def f(t):
    return "%d %s %d" % (t[2], MESES[t[1] - 1], t[0])


def jdn_local(fecha_ephem, horas_este):
    """Día civil (JDN) en que cae un instante, en una hora local UT + horas_este."""
    jd = ephem.julian_date(fecha_ephem) + horas_este / 24.0
    return int(math.floor(jd + 0.5))


def lunas_nuevas(jd_desde, n, horas_este):
    """n lunas nuevas a partir de un JD; devuelve el JDN local de cada una y la hora local."""
    out = []
    d = ephem.Date(jd_desde - 2415020.0)
    for _ in range(n):
        nm = ephem.next_new_moon(d)
        jd = ephem.julian_date(nm) + horas_este / 24.0
        hora = ((jd + 0.5) % 1.0) * 24
        out.append((jdn_local(nm, horas_este), hora))
        d = ephem.Date(nm + 1)
    return out


def longitud_sol(jdn, horas_este):
    """Longitud eclíptica aparente del Sol al mediodía local de ese día (grados)."""
    d = ephem.Date(jdn - 2415020.0 - horas_este / 24.0)
    s = ephem.Sun(d)
    ecl = ephem.Ecliptic(s, epoch=d)
    return math.degrees(ecl.lon) % 360


def mes(titulo, jd_aprox, horas_este, zhongqi, dias_pedidos):
    """Busca el mes lunar que contiene el punto solar 'zhongqi' (grados) cerca de jd_aprox."""
    lunas = lunas_nuevas(jd_aprox - 45, 4, horas_este)
    print("\n== %s ==" % titulo)
    for i in range(len(lunas) - 1):
        ini, hora = lunas[i]
        fin = lunas[i + 1][0] - 1
        l0, l1 = longitud_sol(ini, horas_este), longitud_sol(fin, horas_este)
        contiene = ((zhongqi - l0) % 360) <= ((l1 - l0) % 360)
        if not contiene:
            continue
        largo = fin - ini + 1
        print("luna nueva: %s juliano = %s gregoriano, %04.1f h local  ->  día 1 del mes"
              % (f(juliano(ini)), f(gregoriano(ini)), hora))
        print("el mes tiene %d días; el Sol pasa por %d° dentro del mes" % (largo, zhongqi))
        for dia in dias_pedidos:
            if dia > largo:
                print("  día %2d: no existe (mes de %d días)" % (dia, largo))
                continue
            j = ini + dia - 1
            print("  día %2d: %-12s juliano | %-12s gregoriano | %-9s | %s"
                  % (dia, f(juliano(j)), f(gregoriano(j)), semana(j), sexagesimal(j)))
        return ini, largo
    print("no encontré el mes")
    return None, None


if __name__ == "__main__":
    SEUL = 126.98 / 15.0   # horas al este de Greenwich, hora local media

    # control de las fórmulas
    assert sexagesimal(2451545) == "戊午"
    assert gregoriano(jdn_de_juliano(1582, 10, 5)) == (1582, 10, 15)
    assert semana(jdn_de_gregoriano(2026, 10, 9)) == "viernes"

    print("Diferencia juliano -> gregoriano:")
    for a in (1226, 1443, 1446, 1582, 1926):
        j = jdn_de_juliano(a, 10, 1)
        g = gregoriano(j)
        print("  1 oct %d juliano = %s gregoriano" % (a, f(g)))

    # mes 12 de gyehae (Sejong 25): contiene dahan, Sol en 300°
    mes("Mes 12 de 1443 (Sejong 25)", jdn_de_juliano(1444, 1, 10), SEUL, 300, [1, 15, 29, 30])
    # mes 9 de byeongin (Sejong 28): contiene sanggang, Sol en 210°
    mes("Mes 9 de 1446 (Sejong 28)", jdn_de_juliano(1446, 10, 10), SEUL, 210, [1, 10, 29, 30])
    # mes 9 de 1926
    mes("Mes 9 de 1926", jdn_de_gregoriano(1926, 10, 20), 9.0, 210, [1, 10, 29, 30])
    # mes 9 de 2026, por curiosidad: cuándo caería hoy el festejo lunar
    mes("Mes 9 de 2026", jdn_de_gregoriano(2026, 10, 20), 9.0, 210, [1, 10, 29, 30])

    print("\nFechas fijas:")
    for nombre, j in (("9 oct 1446 gregoriano", jdn_de_gregoriano(1446, 10, 9)),
                      ("15 ene 1444 gregoriano", jdn_de_gregoriano(1444, 1, 15)),
                      ("28 oct 1446 gregoriano", jdn_de_gregoriano(1446, 10, 28)),
                      ("29 oct 1446 gregoriano", jdn_de_gregoriano(1446, 10, 29)),
                      ("4 nov 1926 gregoriano", jdn_de_gregoriano(1926, 11, 4)),
                      ("9 oct 2026 gregoriano", jdn_de_gregoriano(2026, 10, 9))):
        print("  %-24s = %-12s juliano | %-9s | %s | JDN %d"
              % (nombre, f(juliano(j)), semana(j), sexagesimal(j), j))

    # Los diez días. El 29 del mes 9 de 1446 es el día 甲午 de los Anales.
    j = jdn_de_juliano(1446, 10, 19)
    assert sexagesimal(j) == "甲午"
    print("\nEl 29 del mes 9 de 1446 (día 甲午) en cada cuenta:")
    print("  juliano:                         %s" % f(juliano(j)))
    print("  gregoriano proléptico (+9 días): %s" % f(gregoriano(j)))
    print("  juliano + 10 días (la diferencia de 1582, llevada sin cambio a 1446): %s"
          % f(juliano(j + 10)))
    print("  diferencia entre las dos cuentas en 1446: %d días; en 1582: %d días"
          % (jdn_de_juliano(1446, 10, 19) - jdn_de_gregoriano(1446, 10, 19),
             jdn_de_juliano(1582, 10, 19) - jdn_de_gregoriano(1582, 10, 19)))

    # La luna de mañana: el mismo instante cae en dos días civiles distintos.
    print("\nLuna nueva de octubre de 2026:")
    nm = ephem.next_new_moon("2026/10/5")
    print("  UT:              %s" % nm)
    print("  Pekín  (UT+8):   %s" % ephem.Date(nm + 8 * ephem.hour))
    print("  Seúl   (UT+9):   %s" % ephem.Date(nm + 9 * ephem.hour))

    # El mes 12 de 1443 y las dos fechas del norte
    print("\nLas dos fechas del norte dentro del mes 12 de 1443 (30 dic 1443 a 28 ene 1444 gregoriano):")
    ini = jdn_de_juliano(1443, 12, 21)
    for nombre, g in (("9 ene 1444 gregoriano", (1444, 1, 9)), ("15 ene 1444 gregoriano", (1444, 1, 15))):
        jj = jdn_de_gregoriano(*g)
        print("  %s = día %d del mes 12 lunar (%s)" % (nombre, jj - ini + 1, sexagesimal(jj)))

    a = jdn_de_gregoriano(1446, 10, 9)
    b = jdn_de_gregoriano(2026, 10, 9)
    print("\nDel 9 oct 1446 al 9 oct 2026: %d días = %d semanas y %d días; %.1f lunaciones"
          % (b - a, (b - a) // 7, (b - a) % 7, (b - a) / 29.530589))
