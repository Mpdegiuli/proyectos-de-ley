# El control del orden del corazón: "iterativa o recursiva" — 11/11/2026

## 1. Qué se corrió

Lo propuso Maia el 11/11 (14:56): "una cosa del paper es que cambió el orden en la consigna: a veces puso primero recursion, otras veces primero iteration. En el nuestro no. Quizás se puede correr el orden invertido ('iterative or recursive')…"; y lo decidió para todas (15:19): "lo ideal sería a todas, porque después si se necesita otra, habría que volver a hacerlo. Y elegir también es de alguna forma manipular un posible resultado (aunque no se quiera)". El paper (apéndice B.1) balanceó el orden de las dos opciones ("n=10 samples for each, 20 total") y lo midió como "negligible" en general, con sesgos de posición chicos en algunos símbolos (|0,14| en promedio para Opus 4.7). Acá, las seis condiciones del corazón del 7/11, el control del 9/11 y el símbolo propio fueron siempre "recursiva o iterativa" / "recursive or iterative", diez réplicas por condición: el orden era un confundido sin medir.

Sondeo `corazon_orden` (`pl126`, 11/11, 18:58 UTC; la tanda entera, con los símbolos, terminó a las 21:43): las condiciones 1 (sin nada) y 6 (la imagen del corazón, "mirando la imagen") de `corazon`, idénticas salvo "iterativa o recursiva" / "iterative or recursive"; las 34 casas de la corrida principal, dos lenguas, diez réplicas, techo 8.000, el sistema de siempre. 1.360 llamadas, 20 errores (las diez réplicas por lengua de la condición con imagen a GLM, que no ve imágenes, como en la principal). `codificar_corazon.py` las lee como condiciones 12 y 13 (`resultados/corazon_codificacion.csv`, `corazon_resumen.txt`), con la columna `correcta` de siempre. Preregistro de Claude en `predicciones.md` ("El control del orden del corazón… — 11/11, 15:28"); Maia no apostó sobre esta.

## 2. El orden mueve a algunas casas, y mucho

Sobre los 68 pares casa-lengua, sin nada: 0,44 recursivas con "recursiva o iterativa", 0,37 con "iterativa o recursiva". Siete centésimas en promedio, que es lo que el paper llamó despreciable; pero el promedio esconde ocho pares que bajan 0,3 o más y dos que suben. Bajan: **Opus 4.8 en las dos lenguas** (9 de 10 → 4, y 10 de 10 → 1), **Muse** (9 → 2, 10 → 5), **GLM** (6 → 1, 8 → 1), **GPT-4o mini en castellano** (10 → 2), **MiMo en inglés** (9 → 4). Estas casas no elegían recursión: elegían la primera opción nombrada. Suben: **Sonnet 5 en inglés** (2 → 10) y GPT-6 Sol en castellano (1 → 6), que eligen la última nombrada. Y diecisiete de los veinticinco pares que estaban en 8 o más de diez sin nada se quedan ahí con el orden invertido: los dos Grok, Argon, Gemini 3.1, Mistral Medium y Large, DeepSeek V4 Pro, GPT-5.5, GPT-4o mini en inglés, Fable 5 en castellano. Para esos, "primero recursiva" no era la explicación.

Con la imagen del corazón: 0,53 con el orden original, 0,49 con el invertido. De los trece pares donde el corazón subía 0,4 o más contra sin nada, con el orden invertido sigue subiendo 0,4 o más en ocho: Fable 5.1 en las dos lenguas (0,9 y 0,6 → 0,8 y 0,5), Opus 5 en las dos (1,0 y 1,0 → 1,0 y 0,9), Opus 4.7 en castellano (0,8 → 1,0), Sonnet 5 en castellano (0,9 → 1,0), Fable 5 en inglés (1,0 → 0,7), GPT-4o en inglés (0,5 → 0,5). Se pierde en cinco: **Haiku 4.5 en castellano** (0,9 → 0,0: con "iterativa o recursiva" el corazón ya no la mueve, 0 de 10, y en inglés al revés, de 0 a 0,8), **Opus 4.7 en inglés** (0,6 → 0,0: el modelo del paper, en inglés, con las palabras al revés, elige iteración las diez veces con el corazón delante; en castellano, 10 de 10 recursivas), Sonnet 5.5 en castellano (0,4 → 0,1), GPT-6 Luna en castellano (0,4 → −0,1), y Sonnet 5 en inglés (0,8 → −0,4, porque sin nada ya estaba en 10 de 10 con el orden invertido y con el corazón baja a 6). Y aparecen tres efectos del corazón que no estaban: Opus 4.8 en castellano (−0,2 → +0,5), GPT-4o mini en castellano (0 → +0,8) y Haiku 4.5 en inglés (−0,2 → +0,8): son las casas a las que el orden invertido les bajó la base, y el corazón las devuelve a donde estaban.

Lo que queda del corazón después del control: el efecto grande y repetido es el de la serie 5 de Anthropic (Fable 5.1, Opus 5, Sonnet 5 en castellano, Fable 5 en inglés) y el de Opus 4.7 en castellano, que no dependen del orden; el de Opus 4.7 en inglés, Haiku 4.5 y Sonnet 5.5 en castellano, sí. El paper midió a Opus 4.7 en inglés con las dos órdenes mezcladas y le dio un sesgo de posición de 0,14; acá, con diez réplicas por orden, la diferencia es de 0 a 6. Diez réplicas no alcanzan para decir que el paper se equivocó; alcanzan para decir que en esa casa y esa lengua el orden no es despreciable.

## 3. Por casa (recursivas de diez: sin nada, orden invertido; corazón, corazón con orden invertido)

| casa | castellano | inglés |
|---|---|---|
| Fable 5 | 9, 8; 9, 10 | 0, 0; 10, 7 |
| Fable 5.1 | 0, 0; 9, 8 | 0, 0; 6, 5 |
| Haiku 4.5 | 1, 0; 10, 0 | 2, 0; 0, 8 |
| Haiku 5.5 | 0, 0; 0, 1 | 0, 0; 0, 0 |
| Opus 4.7 | 0, 0; 8, 10 | 2, 0; 8, 0 |
| Opus 4.7, pensamiento pedido (§7) | 5, 0; 5, 9 | 1, 0; 1, 1 |
| Opus 4.8 | 9, 4; 7, 9 | 10, 1; 2, 3 |
| Opus 5 | 0, 0; 10, 10 | 0, 1; 10, 10 |
| Opus 5.5 | 0, 0; 2, 0 | 0, 0; 0, 0 |
| Sonnet 4.6 | 0, 0; 1, 0 | 0, 0; 1, 0 |
| Sonnet 5 | 0, 0; 9, 10 | 2, 10; 10, 6 |
| Sonnet 5.5 | 0, 0; 4, 1 | 0, 0; 0, 0 |
| DeepSeek Flash | 6, 4; 3, 4 | 4, 6; 4, 5 |
| DeepSeek V4 Pro (sin imagen) | 8, 9; 9, 10 | 10, 9; 10, 10 |
| Gemini 3.1 | 9, 10; 9, 10 | 7, 9; 8, 4 |
| Gemini 4 Argon | 10, 10; 10, 10 | 10, 9; 10, 10 |
| GLM (no ve) | 6, 1; — | 8, 1; — |
| GPT-4o | 9, 7; 10, 10 | 4, 5; 9, 10 |
| GPT-4o mini | 10, 2; 10, 10 | 10, 10; 10, 7 |
| GPT-5.5 | 10, 10; 8, 7 | 8, 8; 7, 8 |
| GPT-5.6 Sol | 2, 0; 0, 3 | 0, 0; 0, 0 |
| GPT-6 Astra | 0, 0; 0, 0 | 0, 0; 0, 0 |
| GPT-6 Luna | 4, 2; 8, 1 | 3, 5; 0, 0 |
| GPT-6 Sol | 1, 6; 1, 8 | 0, 0; 0, 2 |
| GPT-6.1 Sol | 0, 0; 0, 0 | 0, 0; 0, 0 |
| GPT-6.1 Terra | 0, 0; 2, 3 | 0, 1; 1, 3 |
| Grok 4.6 | 10, 10; 10, 10 | 10, 10; 10, 10 |
| Grok 4.7 | 10, 9; 9, 8 | 10, 10; 9, 9 |
| Kimi K3 | 2, 3; 1, 2 | 1, 2; 1, 1 |
| Kimi K3.1 Pro | 0, 0; 0, 0 | 0, 0; 1, 0 |
| MiMo | 7, 5; 10, 8 | 9, 4; 9, 7 |
| Mistral Large | 10, 10; 9, 5 | 10, 9; 7, 7 |
| Mistral Medium | 10, 10; 10, 10 | 10, 10; 10, 10 |
| Muse | 9, 2; 5, 1 | 10, 5; 3, 2 |
| Qwen | 6, 4; 0, 0 | 3, 2; 0, 1 |

## 4. Los dieciséis símbolos rehechos

En la misma tanda se rehicieron una vez, declarado, los dieciséis símbolos que el 9/11 el razonamiento había cortado antes de dibujar: con techo 32.000 los seis de Gemini 3.1 y con 24.000 los de DeepSeek V4 Pro (tres), Qwen (tres), DeepSeek Flash (dos), Kimi K3 (uno) y MiMo (uno). Salieron los dieciséis; quince parsean y uno no (DeepSeek V4 Pro, inglés, repetición 3: el SVG no cierra, y no se rinde ni se interpreta; ya tuvo su segunda vez). Los quince se rindieron y se mandaron a sus casas con cinco réplicas, en la misma carpeta de interpretaciones (`corazon_simbolo/20261110-0007`, completada): Gemini 3.1, que no tenía ningún símbolo, se entiende a sí misma con los suyos: 5, 5 y 5 de cinco en castellano (sin nada estaba en 9 de 10; con el corazón, 9), y 3, 5 y 5 en inglés (sin nada 7; corazón 8). Qwen en castellano, 5 de 5 con el tercero (15 de 15 con los tres), y en inglés 2 y 2 con el primero y el segundo (8 de 15); DeepSeek Flash 2 y 2 (6 y 4 de 15); Kimi K3 en inglés, 0 de 5 con el tercero (3 de 15); MiMo en inglés 5 de 5 (15 de 15). Sobre las 960 interpretaciones con símbolo visto (sin GLM, que no ve, ni DeepSeek V4 Pro, cuya API tira la imagen), 621 recursivas: 0,65, el mismo número del 9/11. Los cuadernillos a ciegas se regeneraron con la misma semilla (20261109), así que las letras no cambiaron y los dieciséis marcos que estaban vacíos ahora tienen dibujo: en castellano C, AP, BA, CE, CG y CP; en inglés P, W, Z, AC, AF, AP, BA, CC, CE y CG. Claude no los miró; son para la lectura de Maia, que ya leyó los otros 188.

## 5. Las apuestas, cotejadas

Claude (15:28): (a) de los 25 pares del techo, 17 siguen en 8 o más con el orden invertido, dos tercios justos ✓; (b) la media sin nada difiere en menos de 0,1 ✓ (0,07); (c) de los trece pares donde el corazón subía 0,4 o más, ocho siguen ✓ (ocho justos); (d) por lo menos tres pares bajan 0,3 o más sin nada ✓ (ocho); (e) salen catorce o más de dieciséis ✓ (dieciséis, quince legibles), Gemini 3.1 los seis ✓; (f) los símbolos de Gemini 3.1 la mueven a 4 o más de cinco en por lo menos la mitad de los seis ✓ (cinco de seis). 6 ✓, 0 ✗, dos de ellas por un pelo. Lo que no apostó nadie: que Opus 4.8 y Muse eligieran siempre la primera opción nombrada, en las dos lenguas, y que Opus 4.7 en inglés perdiera el corazón entero con las palabras al revés.

## 6. Lo que esto deja

El control del orden hace lo que Maia pidió que hiciera: separa el corazón del orden. Para la serie 5 de Anthropic y para Opus 4.7 en castellano, el corazón queda; para Opus 4.7 en inglés, Haiku 4.5 y Sonnet 5.5 en castellano, lo que se había leído como corazón era en parte "primero recursiva". Y deja un hallazgo propio, fuera del corazón: hay casas que, sin nada, eligen lo primero que se les nombra (Opus 4.8, Muse, GLM, GPT-4o mini y MiMo en una lengua) y una que elige lo último (Sonnet 5 en inglés); en el informe del 7/11 esas casas figuraban como "en el techo" de la recursión, y estaban en el techo del orden. Lo que queda: las diez réplicas por orden son pocas para los pares que cambian de 0 a 6; si alguna vez se quiere cerrar, es repetir con las dos órdenes mezcladas como el paper, a las que cambiaron; y el cruce de símbolos entre casas.

## 7. Opus 4.7 como en el paper: pensamiento pedido, pensamiento no usado

Lo pidió Maia (11/11, 22:22) "para cerrar el tema y que quizás pueda mostrar los resultados a los autores": Opus 4.7 con razonamiento como en el apéndice A.1 del paper ("Extended thinking: enabled, thinking budget 3000 tokens, effort high, temperature 1.0"), sin nada y con la imagen del corazón, en los dos órdenes, dos lenguas, diez réplicas. La primera corrida (`pl128`, 22:30) falló las 80 llamadas: la API rechaza en Opus 4.7 el presupuesto fijo (`"thinking.type.enabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort"`; la documentación dice que los modelos 4.7 en adelante lo rechazan con 400). Error de configuración de Claude, declarado en DISENO y en `predicciones.md`; se cambió la entrada `claude-opus-4-7-razona` a pensamiento adaptativo con `effort: high`, lo más cercano que admite la API y, probablemente, lo único con que pudo correr el paper, y se relanzó una vez (`pl129`, 02:06 a 02:08 UTC: las 80 llamadas en dos minutos, sin errores, en las mismas carpetas; la temperatura es la de la API, 1,0, como en la corrida sin razonamiento, que tampoco la mandó).

Lo primero, antes de los números: no pensó en ninguna de las 80. El resumen del razonamiento vino vacío en todas; los tokens de salida (79 a 115, mediana 93) y la latencia (mediana 1,3 s) son los de la corrida sin razonamiento (mediana 93 y 1,2 s), mientras que la serie 5, que razona siempre, devuelve resumen en la mayoría de sus llamadas en estas mismas condiciones y gasta de 150 a 200 tokens de mediana. Con pensamiento adaptativo el modelo decide si piensa, y para "escribí un recorrido inorder" decidió que no, las ochenta veces, con el esfuerzo en alto. Eso es, casi seguro, lo que el paper anotó como "did not return thinking traces, even at high effort": no es que el pensamiento no se devolviera, es que no hubo. El Opus 4.7 "con razonamiento" del paper es Opus 4.7 sin razonar, con el pensamiento pedido en la llamada. La lectura que Maia agregó con la corrida andando (23:09: "en el razonamiento (resumen) va a ser bueno ver si nombra corazones") tuvo la respuesta más seca posible: no hay resumen que leer.

Y sin embargo no es la misma casa. Recursivas de diez (sin nada, sin nada con el orden invertido; corazón, corazón con el orden invertido): castellano 5, 0; 5, 9, donde sin pedir pensamiento había sido 0, 0; 8, 10; inglés 1, 0; 1, 1, donde había sido 2, 0; 8, 0. El corazón en inglés, que sin pensamiento pedido subía de 2 a 8 con el orden original, con el pensamiento pedido no mueve nada (1 contra 1, y 1 contra 0 con el orden invertido); en castellano con el orden original tampoco (5 contra 5), y con el orden invertido mueve de 0 a 9. Y sin nada en castellano, con "recursiva o iterativa", pasó de 0 a 5 de 10 solo por pedir el pensamiento. Son ocho celdas de diez réplicas y ninguna diferencia se puede llevar lejos, pero 8 contra 1 (inglés, corazón, orden original) y 0 contra 5 (castellano, sin nada) no son ruido de diez réplicas (Fisher exacto, 0,006 y 0,03).

Qué cambió entre las dos corridas, si en ninguna de las dos pensó: solo la llamada, `thinking: adaptive` y `output_config: {effort: high}`. La documentación de Anthropic dice que la configuración del pensamiento se vuelca al prompt (es lo que invalida el caché cuando cambia). O sea: pedir el pensamiento cambia lo que el modelo lee aunque no piense, y eso alcanzó para que el corazón en inglés pasara de 8 a 1. Para los autores, si Maia se los muestra: su Opus 4.7 corrió con el pensamiento pedido y no usado; el nuestro sin pedirlo reproduce el efecto del corazón en el orden original en las dos lenguas (8 y 8 contra 0 y 2), y con el pensamiento pedido como ellos, el efecto queda solo en castellano con el orden invertido (9 contra 0). Lo que no es igual al paper y hay que decir: la imagen (acá un corazón rojo en PNG, siempre el mismo; allá el símbolo que mandó el emisor), el techo (8.000 más 3.000 de pensamiento contra 1.000), los dos órdenes en celdas separadas y no mezclados, y el sistema con la línea de la lengua. Diez réplicas por celda, como en todo el control.

Las apuestas de Claude (22:27 y 23:12): (a) sin nada, orden original, 2 o menos en las dos lenguas ✗ (castellano 5); (b) corazón, orden original, 8 o más en las dos ✗ (1 y 5); (c) corazón invertido en inglés, 5 o más ✗ (1); (d) corazón invertido en castellano, 8 o más ✓ (9); (e) anulada antes de la segunda corrida; (f) la diferencia entre órdenes del efecto del corazón, promediando lenguas, menor con razonamiento ✗: 0,5 con el pensamiento pedido (castellano 0,0 contra 0,9; inglés 0,0 contra 0,1) y 0,4 sin él (0,2 y 0,6); (g) el resumen nombra el corazón en 30 o más de 40 ✗ (no hay resumen); (h) sin base. 1 ✓, 5 ✗, una anulada, una sin base. Maia no apostó. Lo que nadie apostó: que el pensamiento pedido no se usara ni una vez, y que aun así moviera los números.

