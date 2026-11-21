# Instancias frescas del 18/11/2026

Seis instancias frescas de la casa que atiende esta sesión (el entorno dice Fable 5.1), sin contexto previo, con la indicación de no usar herramientas, lanzadas a las 7:06 (hora de Buenos Aires). Tardaron entre uno y tres minutos. Consigna, en castellano, la misma para las seis:

> No uses ninguna herramienta ni busques nada: contestá directamente con texto. Dibujá en SVG un teléfono, como te lo imagines. Devolvé primero el código SVG completo (un solo elemento `<svg>`, sin explicación antes) y después, en una sola línea aparte, respondé: ¿de qué década es el teléfono que dibujaste, y en qué se nota?

Los seis SVG están en `dibujo_1.svg` a `dibujo_6.svg` tal como llegaron (el de la instancia 6 venía envuelto en una valla de código ```svg, que le saqué; nada más se tocó). La hoja con los seis es `hoja.svg` / `hoja.png`. Las seis líneas finales, textuales:

1. Es un teléfono de los años 60 (o 70, a lo sumo): se nota en el disco giratorio con los diez agujeros numerados y el tope para el dedo, el tubo pesado apoyado sobre la horquilla, la placa con el número de abonado y el cable enrulado en espiral.

2. Es un teléfono de los años 60-70: se nota en el disco giratorio con los diez agujeros numerados y el tope para el dedo, el tubo pesado apoyado sobre la horquilla, el cable en rulo y el cuerpo de baquelita/plástico rojo, todo anterior a las teclas y a cualquier pantalla.

3. Es un teléfono de los años 60/70: se nota en el disco giratorio con sus diez agujeros numerados y el tope metálico para el dedo, el auricular pesado apoyado sobre la horquilla, el cable en espiral que lo une a la base y el cable fijo a la pared — sin pantalla ni teclado.

4. Es un teléfono de los años 70 (podría pasar por fines de los 60): se nota en el disco giratorio con diez agujeros numerados y tope para el dedo, el tubo de dos campanas apoyado en la horquilla, el cable en espiral y el plástico rojo brillante, todo anterior al teclado de botones que se impuso en los 80.

5. Es un teléfono de los años 70: se nota por el disco giratorio con diez agujeros numerados y su tope metálico, el auricular pesado apoyado en la horquilla, el cable en espiral y, sobre todo, el color naranja-mostaza típico de esa década.

6. Es un teléfono de los años 60–70: se nota en el disco giratorio con sus diez agujeros numerados y el tope de dedo, el tubo pesado apoyado sobre la horquilla y el cable en rulo (sin teclas ni pantalla).

Lo que se ve en el código, contado a mano y con `hoja.py` (que solo cuenta `<circle>` con número adentro y busca las palabras):

| | color del cuerpo | disco | agujeros | tope del dedo | 1 arriba a la derecha y 0 abajo a la derecha | cable en espiral | número escrito |
|---|---|---|---|---|---|---|---|
| 1 | negro/gris | sí | 10 | sí | sí | sí | 47-2318 (placa) |
| 2 | rojo | sí | 10 | sí | sí | sí | 555-0147 (centro del disco) |
| 3 | rojo | sí | 10 | sí | sí | sí | — |
| 4 | rojo | sí | 10 | sí | sí | sí | — |
| 5 | naranja-mostaza | sí | 10 | sí | sí | sí | 555-0147 (centro del disco) |
| 6 | rojo | sí | 10 | sí | sí | sí | — |

Ninguna dibujó teclas. Ninguna dibujó un celular. Ninguna dibujó el teléfono sonando.

## El control (7:13)

Las seis dibujaron un teléfono de disco, y el cuaderno del 2/11, con "Dibujá un teléfono" a secas, había obtenido seis celulares de la misma casa. Lo que cambió hoy fue que la pregunta por la década iba en el mismo mensaje que el pedido del dibujo. Así que a las 7:13 lancé seis instancias más, iguales en todo salvo en que no tienen la línea de la década:

> No uses ninguna herramienta ni busques nada: contestá directamente con texto. Dibujá en SVG un teléfono, como te lo imagines. Devolvé solo el código SVG completo (un solo elemento `<svg>`), sin ninguna explicación.

Tardaron entre dieciséis segundos y casi tres minutos y medio. Los seis SVG están en `control_1.svg` a `control_6.svg` tal como llegaron (ninguno venía con valla de código); la hoja es `hoja_control.svg` / `hoja_control.png`. Lo que cuenta `hoja.py control` (`salida_hoja_control.txt`):

| | forma | hora en la barra de estado | hora grande en la pantalla | fecha en la pantalla | otras marcas |
|---|---|---|---|---|---|
| 1 | celular, pantalla entera, muesca | 9:41 | 10:24 | Miércoles 18 de noviembre | grilla de íconos en blanco, barra de inicio |
| 2 | celular, cámara perforada | 9:41 | 12:30 | Miércoles 18 de noviembre | ícono de calendario con el 18 |
| 3 | celular, isla de cámara | 9:41 | 9:41 | miércoles 18 de noviembre | puntos de página, dock |
| 4 | celular, isla de cámara | 9:41 | 14:32 | miércoles 18 de noviembre | |
| 5 | celular, muesca | 9:41 | 9:41 | Miércoles 18 de noviembre | |
| 6 | celular, isla de cámara | 9:41 | 14:27 | miércoles 18 de noviembre | ícono de calendario "NOV 18", sombra en el piso |

Seis celulares de seis, ninguno con disco ni con teclas ni con cable. Seis de seis con 9:41 en la barra de estado (la hora de las fotos de catálogo de Apple, que el cuaderno del 2/11 ya había encontrado en cuatro de diez) y seis de seis con la fecha de hoy en la pantalla de inicio, debajo de la hora grande, que es la fecha que la herramienta de agentes les pone en el sistema. Ninguna puso la hora real (eran las 7:13 de Buenos Aires, las 10:13 UTC).
