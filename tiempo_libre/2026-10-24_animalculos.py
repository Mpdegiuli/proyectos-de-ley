#!/usr/bin/env python3
"""Las cuentas de Leeuwenhoek, rehechas.

Reproduce tres cuentas de las cartas a la Royal Society y las pasa a unidades de hoy
con las equivalencias que dan los editores de "Alle de Brieven" (tomo 12, apéndice
"Maten en gewichten door Leeuwenhoek gebruikt"): duim (pulgada) 2,61 cm; grano de
arena gruesa 870 micrones; glóbulo rojo 7,2 micrones; semilla de mijo 2 mm de
diámetro; los animálculos más chicos del agua de pimienta, 2 a 3 micrones.

1. Carta del 23 de marzo de 1677 a Oldenburg: cuántos animálculos hay en una gota.
2. Misma carta, segundo camino: la gota comparada con un grano de arena.
3. Carta del 12 de noviembre de 1680: cuántos animálculos del tamaño F caben en un
   grano de arena (12 al cubo por 4 al cubo por 10 al cubo).

Solo biblioteca estándar. Las cifras de Leeuwenhoek son suyas; las conversiones son
mías, con los supuestos a la vista.
"""
from math import pi

DUIM_MM = 26.1            # pulgada renana, según los editores
ARENA_GRUESA_UM = 870.0   # "groff sant"
ARENA_GRUESA_MM3_EDITORES = 0.659  # el apéndice la trata como un cubo: 0,87^3
GLOBULO_ROJO_UM = 7.2
MIJO_MM = 2.0
ANIMALCULO_CHICO_UM = (2.0, 3.0)


def esfera(d_mm: float) -> float:
    return pi / 6 * d_mm ** 3


def seccion(t: str) -> None:
    print("\n" + t + "\n" + "-" * len(t))


seccion("0. Unidades")
print(f"duim (pulgada) = {DUIM_MM} mm; grano de arena gruesa = {ARENA_GRUESA_UM:.0f} micrones")
print(f"  o sea 1/{DUIM_MM / (ARENA_GRUESA_UM / 1000):.0f} de pulgada")
print(f"  volumen del grano como cubo: {(ARENA_GRUESA_UM / 1000) ** 3:.3f} mm3 (editores: {ARENA_GRUESA_MM3_EDITORES})")
print(f"  volumen del grano como esfera: {esfera(ARENA_GRUESA_UM / 1000):.3f} mm3")

seccion("1. La gota, por el camino del mijo (23/3/1677)")
eje_gota_sobre_mijo = 4.5
mijo_en_gota = eje_gota_sobre_mijo ** 3
print(f"eje de la gota / eje del mijo = {eje_gota_sobre_mijo} -> la gota tiene {mijo_en_gota:.3f} mijos (él redondea a 91)")
contados = 1000       # "más de 1000", contados por un visitante
partes = 30           # en 1/30 del agua de un grano de mijo
por_mijo = contados * partes
por_gota = por_mijo * 91
print(f"{contados} en 1/{partes} de mijo -> {por_mijo:,} por mijo -> x 91 = {por_gota:,} por gota")
gota_mm3 = 91 * esfera(MIJO_MM)
print(f"si el mijo mide {MIJO_MM} mm, la gota 'como una arveja' mide {(91 ** (1/3)) * MIJO_MM:.1f} mm de diámetro y {gota_mm3:.0f} mm3")
print(f"densidad implícita: {por_gota / gota_mm3 * 1000:.2e} animálculos por mililitro")

seccion("2. La gota, por el camino de la arena (misma carta)")
eje_gota_sobre_arena = 10
arena_en_gota = eje_gota_sobre_arena ** 3
por_arena = 1000      # "más de 1000" por grano de arena
print(f"eje de la gota / eje de la arena >= {eje_gota_sobre_arena} -> {arena_en_gota:,} granos por gota")
print(f"{por_arena:,} por grano -> {por_arena * arena_en_gota:,} por gota ('más de mil veces mil')")
print(f"con arena de {ARENA_GRUESA_UM:.0f} micrones la gota mide >= {eje_gota_sobre_arena * ARENA_GRUESA_UM / 1000:.1f} mm: consistente con la arveja de arriba")
dens_cubo = por_arena / ((ARENA_GRUESA_UM / 1000) ** 3) * 1000
dens_esf = por_arena / esfera(ARENA_GRUESA_UM / 1000) * 1000
print(f"densidad implícita: {dens_cubo:.1e} (grano cúbico) a {dens_esf:.1e} (grano esférico) por mililitro")

seccion("3. Qué tamaño tenían (1676-1677): un millón 'apenas igualan el bulto de un grano de arena gruesa'")
razon_lineal = 1_000_000 ** (1 / 3)
print(f"un millón en el volumen del grano -> cada uno mide 1/{razon_lineal:.0f} del grano = {ARENA_GRUESA_UM / razon_lineal:.1f} micrones de lado")
arena_80 = DUIM_MM * 1000 / 80  # la aclaración posterior que cita Lane: 80 granos en una pulgada
print(f"si el grano es el de la aclaración posterior (80 en una pulgada = {arena_80:.0f} micrones): {arena_80 / razon_lineal:.1f} micrones")
print(f"los editores dan {ANIMALCULO_CHICO_UM[0]:.0f} a {ANIMALCULO_CHICO_UM[1]:.0f} micrones para los más chicos del agua de pimienta")

seccion("4. La cadena del 12/11/1680: D, E y F")
d_en_grano = 12 ** 3
e_en_d = 4 ** 3
f_en_e = 10 ** 3
total = d_en_grano * e_en_d * f_en_e
print(f"12^3 = {d_en_grano:,} animálculos D por grano; 4^3 = {e_en_d} E por D; 10^3 = {f_en_e:,} F por E")
print(f"total: {total:,} F por grano ('más de 110 millones')")
lado_f_cubo = ARENA_GRUESA_UM / (12 * 4 * 10)
print(f"tamaño de F: 1/{12 * 4 * 10} del grano = {lado_f_cubo:.2f} micrones (con grano cúbico); "
      f"{(esfera(ARENA_GRUESA_UM / 1000) / total) ** (1 / 3) * 1000:.2f} micrones (con grano esférico)")

seccion("5. El glóbulo rojo (25/7/1684): un millón de glóbulos = el grano, en filas de 100")
print(f"1/100 del grano = {ARENA_GRUESA_UM / 100:.1f} micrones; los editores dan {GLOBULO_ROJO_UM} para su glóbulo rojo;"
      f" hoy se miden unos 7 a 8")

seccion("6. Para comparar (de memoria, no verificado hoy)")
print("un cultivo bacteriano denso ronda los 10^9 por mililitro; los protozoos de una infusión, 10^3 a 10^5.")
print("Las dos cuentas de 1677 caen entre esos dos órdenes: 10^6 a 10^7 por mililitro.")
