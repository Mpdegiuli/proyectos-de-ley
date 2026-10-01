#!/usr/bin/env python3
"""cielo.py — la Luna de verdad, calculada con PyEphem, para comparar con las lunas dibujadas.
Para un lugar y una hora da: fracción iluminada, altura y acimut de la Luna y del Sol, y hacia dónde
apunta el limbo iluminado visto por quien mira (ángulo desde arriba, en sentido horario: 90 = derecha,
180 = abajo, 270 = izquierda). Borrador de una sesión de tiempo libre (1/10/2026)."""
import ephem, math, sys
LUGARES = {'Buenos Aires': ('-34.6037', '-58.3816', -3), 'San Francisco': ('37.7749', '-122.4194', -7),
           'Londres': ('51.5074', '-0.1278', 1), 'Quito': ('-0.1807', '-78.4678', -5)}


def mirar(lugar, utc):
    lat, lon, _ = LUGARES[lugar]
    o = ephem.Observer(); o.lat, o.lon, o.pressure, o.date = lat, lon, 0, utc
    m, s = ephem.Moon(o), ephem.Sun(o)
    daz = s.az - m.az
    rumbo = math.degrees(math.atan2(math.sin(daz) * math.cos(s.alt),
                                    math.cos(m.alt) * math.sin(s.alt) - math.sin(m.alt) * math.cos(s.alt) * math.cos(daz))) % 360
    return dict(k=m.phase / 100, alt=math.degrees(m.alt), az=math.degrees(m.az), sol_alt=math.degrees(s.alt),
                sol_az=math.degrees(s.az), rumbo=rumbo, elong=math.degrees(m.elong))


def local(lugar, utc): return ephem.Date(ephem.Date(utc) + LUGARES[lugar][2] * ephem.hour)


if __name__ == '__main__':
    print('Fases (UTC):')
    d = ephem.Date('2026/9/20')
    for nombre, f in (('llena', ephem.next_full_moon), ('menguante', ephem.next_last_quarter_moon),
                      ('nueva', ephem.next_new_moon), ('creciente', ephem.next_first_quarter_moon)):
        print(f'  {nombre:10s}', f(d))
    print('\nHoy, 1/10/2026, 6:48 de Buenos Aires (09:48 UTC):')
    r = mirar('Buenos Aires', '2026/10/1 09:48'); print('  ', {k: round(v, 1) if k != 'k' else round(v, 3) for k, v in r.items()})
    o = ephem.Observer(); o.lat, o.lon, _ = LUGARES['Buenos Aires']; o.date = '2026/10/1 03:00'
    print('   sale el Sol:', local('Buenos Aires', o.next_rising(ephem.Sun())), '  se pone la Luna:', local('Buenos Aires', o.next_setting(ephem.Moon())))
    # control del signo: un creciente vespertino en Londres tiene la luz abajo a la derecha (rumbo entre 90 y 180)
    print('\nLa luna de las máquinas: k cerca de 0,30 y luz abajo a la izquierda (rumbo cerca de 234).')
    for lugar in LUGARES:
        print(f'  {lugar}:')
        t = ephem.Date('2026/10/1 00:00')
        while t < ephem.Date('2026/11/12'):
            r = mirar(lugar, t)
            # cielo oscuro o crepúsculo (Sol bajo el horizonte), Luna a más de 8 grados de altura
            if r['sol_alt'] < -6 and r['alt'] > 8 and 0.22 <= r['k'] <= 0.38:
                print(f"     {str(local(lugar, t))[:16]} hora local  k={r['k']:.2f}  altura {r['alt']:4.0f}  acimut {r['az']:4.0f}  rumbo de la luz {r['rumbo']:4.0f}")
            t = ephem.Date(t + ephem.hour)
