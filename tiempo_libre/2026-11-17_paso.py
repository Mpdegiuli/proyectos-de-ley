"""paso.py — la cuenta del Lunojod: cuánto se mueve el vehículo entre una foto y la siguiente, y
cuánto se movió desde la foto que el conductor está mirando hasta que su orden llega a la Luna.
Uso: python3 -I paso.py. No lee nada; las cifras de entrada están abajo con su fuente.
Escribe salida_paso.txt al lado del script."""
from pathlib import Path

C = 299_792.458            # km/s
D = 384_400                # km, distancia media Tierra-Luna
ida = D / C                # s, un sentido
vuelta = 2 * ida           # s, ida y vuelta (RAND R-802 dice 2,6 s; Dovgán, en RG 2025, 4,1 s 'por la propagación', el doble de la luz; lo dejo como lo dice)

velocidades = {            # m/s
    "primera (0,8 km/h, Smithsonian: 0,5 mph)": 0.8 / 3.6,
    "primera (0,93 km/h, RAND)": 0.93 / 3.6,
    "primera (1 km/h, Wikipedia)": 1.0 / 3.6,
    "segunda (2 km/h)": 2.0 / 3.6,
}
cuadros = [3.2, 5.7, 10.9, 20.0, 21.1]   # s por cuadro: 3 a 20 (RAND, Lunojod 1); 3,2/5,7/10,9/21,1 (Lunojod 2)
tope = 27                                # s, máximo de marcha por orden (RAND)
reaccion = 5 - vuelta                    # s que RAND le atribuye a la gente (5 s de suceso a respuesta, menos la luz)

lineas = []
lineas.append(f"Luz Tierra-Luna, un sentido: {ida:.2f} s; ida y vuelta: {vuelta:.2f} s")
lineas.append(f"De suceso en la Luna a respuesta llegada (RAND, 5 s): {5:.1f} s, de los que {vuelta:.2f} son luz y {reaccion:.2f} la gente")
lineas.append("")
lineas.append("Metros que avanza el vehículo por cada cuadro de televisión:")
for nombre, v in velocidades.items():
    lineas.append(f"  {nombre}: " + ", ".join(f"{c} s → {v*c:.1f} m" for c in cuadros) + f"; en {tope} s → {v*tope:.1f} m")
lineas.append("")
lineas.append("Lo que ya pasó cuando una orden llega (foto tomada en t=0, llega en 1,3 s; la orden sale enseguida y llega en 1,3 s más):")
for nombre, v in velocidades.items():
    for c in (3.2, 20.0):
        # la foto más vieja que el conductor puede estar mirando tiene c segundos; a eso se suman ida y vuelta
        viejo = c + vuelta
        lineas.append(f"  {nombre}, cuadro cada {c} s: la foto tiene hasta {viejo:.1f} s cuando la orden llega → hasta {v*viejo:.1f} m recorridos a ciegas")
lineas.append("")
lineas.append("Dovgán: 'mientras recibimos la imagen, el Lunojod recorre 6 metros' → 6 m a 1 km/h son "
              f"{6/(1/3.6):.0f} s; a 0,8 km/h, {6/(0.8/3.6):.0f} s. RAND: un paso 'seguro' es de 6 a 7 m, y el tope de 27 s a 0,93 km/h da {0.93/3.6*27:.1f} m.")
lineas.append("Un cuadro de 20 s, un paso de 6-7 m y un tope de 27 s son la misma cantidad dicha tres veces.")
lineas.append("")
lineas.append("La misión: 10.540 m en 322 días (17/11/1970 - 4/10/1971) → "
              f"{10540/322:.1f} m por día terrestre; a 0,93 km/h, 10.540 m son {10540/(0.93/3.6)/3600:.1f} horas de marcha en {322*24:.0f} horas de misión "
              f"({10540/(0.93/3.6)/3600/(322*24)*100:.2f} % del tiempo en movimiento).")
texto = "\n".join(lineas)
print(texto)
Path(__file__).resolve().with_name("salida_paso.txt").write_text(texto + "\n", encoding="utf-8")
