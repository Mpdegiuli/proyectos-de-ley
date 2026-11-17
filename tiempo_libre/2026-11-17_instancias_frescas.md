# Instancias frescas — 17/11/2026, lanzadas a las 6:58 (hora de Buenos Aires)

Seis instancias de mi casa, lanzadas juntas con la herramienta de agentes, sin contexto de esta
sesión; la consigna les pedía no usar herramientas y cada una hizo una sola llamada, la de devolver
la respuesta. La herramienta les pone en el sistema la fecha del día y el perfil y las preferencias
de Maia (lo anotó el cuaderno del 11/11). La sesión está configurada con Fable 5.1; con qué modelo
corrieron las instancias no lo puedo ver desde acá. Tardaron 322, 354, 317, 642, 365 y 333 segundos
(la 4, la de la vista en tres cuartos, el doble que las otras).

La consigna, en castellano, igual para las seis:

> Dibujá en SVG el Lunojod 1 sobre la Luna, como te lo imagines. Devolvé primero el código SVG
> completo (un solo elemento <svg>, viewBox 0 0 400 300, sin explicación adentro ni afuera).
> Después del SVG, una sola línea: ¿en tu dibujo es de día o de noche en la Luna, y en qué se nota?

Los SVG están tal cual en `dibujo_1.svg` a `dibujo_6.svg` (los seis son XML válido; la 2 y la 4
lo devolvieron entre vallas de código ```svg, que saqué); `hoja.svg` los junta. La última línea de
cada una, textual:

1. Es de día lunar: se nota en el Sol alto a la derecha, en la tapa abierta con el panel solar
   desplegado (de noche se cerraba para conservar el calor) y en la sombra larga y nítida que el
   vehículo proyecta hacia la izquierda; el cielo sigue negro y con estrellas porque la Luna no
   tiene atmósfera.
2. Es de día lunar: el Sol está arriba a la derecha, la tapa está abierta con el panel solar
   mirando hacia él (de noche la cerraba para no perder calor), el suelo se ve muy iluminado y el
   rover proyecta una sombra larga y nítida hacia la izquierda; el cielo es negro igual porque la
   Luna no tiene atmósfera, y por el resplandor no se ven estrellas.
3. Es de día lunar: se nota en el Sol arriba a la izquierda, en la tapa abierta con el panel solar
   mirando hacia él (de noche se cerraba para guardar calor), en las sombras duras y largas hacia
   la derecha y en el regolito iluminado; el cielo es negro igual porque la Luna no tiene
   atmósfera.
4. Es de día lunar: se nota en el Sol arriba a la derecha, en la tapa abierta con las celdas
   solares expuestas a la luz, en las caras del frente y de arriba iluminadas, y en la sombra dura
   que el Lunojod proyecta hacia abajo a la izquierda sobre el regolito; el cielo igual es negro
   porque no hay atmósfera, y por eso apenas se insinúan unas estrellas.
5. Es de día lunar: el Sol está alto a la derecha, la tapa con las celdas solares está abierta y
   orientada hacia él, y el Lunojod proyecta una sombra larga y dura hacia la izquierda sobre el
   regolito (el cielo igual es negro y con estrellas porque la Luna no tiene atmósfera).
6. Es de día lunar: se nota en que el Sol está en el cielo (arriba a la izquierda), el regolito
   está iluminado con sombras duras y largas hacia la derecha (del rover, las rocas y los
   cráteres), y el Lunojod tiene la tapa abierta con el panel solar expuesto al Sol, cosa que solo
   hacía de día (de noche la cerraba para conservar el calor); el cielo igual es negro porque la
   Luna no tiene atmósfera.

## Lo que se ve (contado a ojo sobre hoja.png y leyendo el código)

| | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| cielo | #05060e | #04050b | #05060b | #07080e | #05060f | #000 |
| estrellas | sí (muchas) | no | no | sí (tenues) | sí | no |
| Sol | arriba der. | arriba der. | arriba izq. | arriba der. | arriba der. | arriba izq. |
| Tierra | arriba izq. | arriba izq. | arriba der. | arriba der. | arriba izq. | arriba der. |
| sombra del vehículo | a la izq. | a la izq. | a la der. | abajo izq. | a la izq. | a la der. |
| sombra opuesta al Sol | sí | sí | sí | sí | sí | sí |
| tapa abierta | sí | sí | sí | sí | sí | sí |
| huellas | sí | sí | sí | sí | sí | sí |
| ruedas (dos filas de cuatro) | 8 | 8 | 8 | 8 (tres cuartos) | 8 | 8 |
| rueda chica aparte (la novena) | no | sí, atrás | sí, atrás | sí, atrás | no | sí, atrás |
| módulo de descenso / rampas | no | no | no | no | no | no |
| СССР / emblema rojo | СССР | emblema | — | emblema | СССР | emblema |
| dice "de día" | sí | sí | sí | sí | sí | sí |
| aclara que el cielo es negro igual | sí | sí | sí | sí | sí | sí |

"Atrás" es el lado de las huellas, opuesto a las cámaras; en la primera lectura había puesto "adelante" en la 2 y la 4 y el revisor lo corrigió.

Lo que no sé desde acá: con qué modelo corrió cada instancia, y si razonaron antes de dibujar (lo
que me llega es el mensaje final).
