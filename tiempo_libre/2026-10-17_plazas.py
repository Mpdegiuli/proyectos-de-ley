#!/usr/bin/env python3
"""plazas.py — cuánta gente entra, por el método de Jacobs, en los espacios del eje
Plaza de Mayo – Avenida de Mayo – Plaza del Congreso. No lee nada: las superficies
están escritas acá con su fuente, y el programa solo multiplica.

Superficies (m²):
  Plaza de Mayo, espacio público antes de la obra de 2018 ........ 19.343  (Diario de Cuyo 29/5/2018; es.wikipedia)
  Plaza de Mayo, espacio público desde 2018 ...................... 23.665  (ídem)
  Plaza de Mayo con las calles que la rodean ..................... 30.000  (Chequeado, con DaftLogic)
  Avenida de Mayo, 1,5 km × 30 m de fachada a fachada ............ 45.000  (largo y ancho: en.wikipedia; la cuenta es mía)
  Avenida de Mayo, "alrededor de 17 mil" ......................... 17.000  (Chequeado; coincide con la calzada sola: 1,3-1,5 km × 12-13 m)
  Conjunto Plaza del Congreso + Mariano Moreno + Lorea ........... 30.000  (en.wikipedia: "3 hectare")
  Plaza del Congreso con calles .................................. 50.000  (Chequeado)

Densidades (personas por m²): 1, 2 y 4 son las que usan Chequeado y La Nación (Jacobs
en metros); 5 la agregó La Nación para la Plaza de Mayo el 23/4/2024.
Las de Jacobs en pies cuadrados por persona (10, 4,5 y 2,5) se convierten abajo.
"""

PIE2 = 0.09290304  # m² por pie cuadrado

def n(x):
    """número con punto de miles, como se escribe acá"""
    return f'{x:,.0f}'.replace(',', '.')

print('Jacobs en pies cuadrados por persona -> personas por m²')
for pies in (10, 4.5, 2.5):
    print(f'  {pies:>4} ft²/persona = {pies*PIE2:.3f} m²/persona = {1/(pies*PIE2):.2f} personas/m²')
print()

ESPACIOS = [
    ('Plaza de Mayo (antes de 2018)', 19343),
    ('Plaza de Mayo (desde 2018)', 23665),
    ('Plaza de Mayo con calles (Chequeado)', 30000),
    ('Avenida de Mayo, fachada a fachada', 45000),
    ('Avenida de Mayo, calzada (Chequeado)', 17000),
    ('Congreso: las tres plazas', 30000),
    ('Congreso con calles (Chequeado)', 50000),
]
DENS = (1, 2, 4, 5)

print(f'{"espacio":<40}{"m²":>8}' + ''.join(f'{d:>10}/m²' for d in DENS))
for nombre, m2 in ESPACIOS:
    print(f'{nombre:<40}{n(m2):>8}' + ''.join(f'{n(m2*d):>13}' for d in DENS))
print()

EJES = [
    ('Plaza de Mayo sola (desde 2018)', 23665),
    ('Plaza + Avenida de Mayo (fachadas)', 23665 + 45000),
    ('Plaza + Avenida + Congreso (tres plazas)', 23665 + 45000 + 30000),
    ('Lo mismo con calles (Chequeado)', 30000 + 45000 + 50000),
]
print('Capacidad de los ejes, de 2 a 4 personas por m²:')
for nombre, m2 in EJES:
    print(f'  {nombre:<42} {n(m2):>8} m²: {n(2*m2):>8} a {n(4*m2):>8}')
print()

print('Qué superficie hace falta para cada cifra de 1945 (a 4/m², la máxima de Jacobs, y a 2/m²):')
for etiqueta, c in (('15.000 (mediodía, Perfil)', 15000), ('100.000 (Grimson, piso)', 100000),
                    ('200.000 (Grimson, techo)', 200000), ('250.000 (Golzman)', 250000),
                    ('300.000 (la que circula)', 300000), ('1.000.000 (La Época)', 1000000)):
    print(f'  {etiqueta:<28} {n(c/4):>10} m² a 4/m²   {n(c/2):>10} m² a 2/m²')
