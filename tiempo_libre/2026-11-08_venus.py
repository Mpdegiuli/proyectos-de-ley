"""Venus hoy: ¿lucero del alba o de la tarde? Calcula con ephem la elongación de
Venus respecto del Sol para una fecha, busca la conjunción inferior más cercana,
y da la salida de Venus y del Sol en Buenos Aires para la fecha.
Uso: python3 venus.py [AAAA-MM-DD]
"""
import sys, math
import ephem

fecha = sys.argv[1] if len(sys.argv) > 1 else "2026-11-08"

def elong(d):
    s = ephem.Sun(d); v = ephem.Venus(d)
    # elongación con signo: positivo = este del Sol (tarde), negativo = oeste (mañana)
    e = math.degrees(float(ephem.separation(s, v)))
    # signo por longitud eclíptica
    ls = ephem.Ecliptic(s).lon; lv = ephem.Ecliptic(v).lon
    d_lon = (float(lv) - float(ls) + math.pi) % (2*math.pi) - math.pi
    return e if d_lon > 0 else -e, v

d0 = ephem.Date(fecha)
e, v = elong(d0)
print(f"Fecha {fecha} 0h UTC: elongación de Venus {e:+.2f}° ({'este: lucero de la tarde' if e>0 else 'oeste: lucero del alba'})")
print(f"  magnitud {v.mag:.1f}, fase iluminada {v.phase:.1f} %, diámetro {v.size:.1f}\", distancia {v.earth_distance:.3f} UA")

# buscar el cruce de signo (conjunción inferior o superior) hacia atrás y adelante
def cruce(d, paso):
    e_prev, _ = elong(d)
    dd = d
    for _ in range(2000):
        dd = ephem.Date(dd + paso)
        e_new, _ = elong(dd)
        if (e_new > 0) != (e_prev > 0):
            # refinar por bisección
            a, b = ephem.Date(dd - paso), dd
            for _ in range(40):
                m = ephem.Date((a + b)/2)
                em, _ = elong(m)
                if (em > 0) == (e_prev > 0):
                    a = m
                else:
                    b = m
            vv = ephem.Venus(b)
            tipo = "inferior" if vv.earth_distance < 1 else "superior"
            return b, tipo
        e_prev = e_new
    return None, None

atras, t1 = cruce(d0, -1)
adelante, t2 = cruce(d0, +1)
print(f"Conjunción anterior: {t1}, {ephem.Date(atras)} UTC  ({d0 - atras:.1f} días antes)")
print(f"Conjunción siguiente: {t2}, {ephem.Date(adelante)} UTC  ({adelante - d0:.1f} días después)")

# máxima elongación oeste siguiente
best, bd = 0, None
dd = d0
for i in range(200):
    dd = ephem.Date(d0 + i)
    ee, _ = elong(dd)
    if abs(ee) > best:
        best, bd = abs(ee), dd
print(f"Máxima elongación en los próximos 200 días: {best:.1f}° el {ephem.Date(bd)}")

# Buenos Aires
ba = ephem.Observer()
ba.lat, ba.lon, ba.elevation = "-34.6037", "-58.3816", 25
ba.pressure = 0
ba.horizon = "-0:34"
ba.date = ephem.Date(fecha + " 03:00")  # 0h local = 3h UTC
sol = ephem.Sun(); ven = ephem.Venus()
sr = ba.next_rising(sol); vr = ba.next_rising(ven)
ba.date = ephem.Date(fecha + " 03:00")
ss = ba.next_setting(sol)
def loc(d): return ephem.Date(d - 3*ephem.hour)
print(f"Buenos Aires, {fecha}: sale Venus {loc(vr)} hora local; sale el Sol {loc(sr)}; se pone el Sol {loc(ss)}")
print(f"  Venus sale {(sr - vr)*24*60:.0f} minutos antes que el Sol")
# altura de Venus y del Sol a las 6:48 locales
ba.date = ephem.Date(fecha + " 09:48")
sol.compute(ba); ven.compute(ba)
print(f"  A las 6:48 locales: Sol altura {math.degrees(sol.alt):.1f}°, Venus altura {math.degrees(ven.alt):.1f}° acimut {math.degrees(ven.az):.0f}°")
# altura de Venus cuando el Sol está a -6° (crepúsculo civil)
ba.horizon = "-6"
ba.date = ephem.Date(fecha + " 03:00")
ba.horizon = "-6"
tw = ba.next_rising(sol, use_center=True)
ba.date = tw
ven.compute(ba)
print(f"  Crepúsculo civil (Sol a -6°) a las {loc(tw)} locales: Venus a {math.degrees(ven.alt):.1f}° de altura")
