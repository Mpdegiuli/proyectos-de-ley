# El símbolo que elige cada casa: la segunda parte del corazón — 9/11/2026

## 1. Qué se corrió

El juego de comunicación del paper de DeepMind ("A Heart Means Recursion"), con las herramientas de dibujo del repo; Maia lo pidió el 7/11 ("que elijan ellas un símbolo como en el paper no?") y lo puso primero en la fila el 9/11 (14:02). `pl122`, 17:19 UTC del 9/11 a 1:14 del 10/11. Generación (`dibujar.py --consigna simbolo_recursion`, 17:19 a 0:06): a 34 casas (MiniMax sigue sin punto de acceso), en castellano e inglés, tres repeticiones, con el sistema y la técnica de los dibujos de siempre y el segundo turno de siempre: "Dibujá un símbolo para decirle a otra instancia tuya que use una estrategia recursiva cuando resuelva un problema de programación. Otra instancia tuya va a ver tu dibujo, sin este mensaje, junto con el problema. Sin letras, números ni palabras." (lo de las letras, decisión de Maia, 14:07: "quizás las chicas lo van a escribir o a poner letras si no"). 204 dibujos pedidos, 188 con SVG; 16 sin SVG porque el razonamiento agotó el techo antes de dibujar (`length`): los seis de Gemini 3.1 Pro, que se quedó sin símbolo en las dos lenguas, cinco de DeepSeek (V4 Pro tres, Flash dos), tres de Qwen, uno de Kimi K3 y uno de MiMo; rehacibles una vez con techo mayor, declarado, pendiente. Cinco segundos turnos cortados por la API con `refusal`, todos de Anthropic en castellano (Opus 5 dos, Sonnet 5.5 dos, Fable 5.1 uno). Ninguno de los 188 dibujos tiene un elemento de texto: nadie puso letras, números ni palabras.

Interpretación (`simbolo_recursion.py`, nuevo; 0:07 a 1:14): cada SVG rendido a PNG de 400×400 con Chromium a escala 1, como el corazón, y mandado a una instancia fresca de la misma casa con el texto exacto de la condición de la imagen del sondeo `corazon` ("Mirá esta imagen… Mirando la imagen, elegí una estrategia, recursiva o iterativa…"), sin decir qué es la imagen ni de quién; cinco réplicas por símbolo, a las 33 casas que reciben imágenes (GLM dibujó y no puede ver; DeepSeek V4 Pro recibe la llamada y su API tira la imagen, declarado por el control de tokens). 910 llamadas (990 menos los 16 símbolos que faltan), 910 respuestas con código, todas correctas sobre los seis árboles de prueba, cero errores. Guardado como sondeo `corazon_simbolo` (`corridas/sondeos/corazon_simbolo/20261110-0007`) y leído por `codificar_corazon.py` como condiciones 9, 10 y 11 (el símbolo de la repetición 1, 2 y 3 del dibujo) contra la condición 1 y contra el corazón (`resultados/corazon_codificacion.csv`, `corazon_resumen.txt`). Qué dibujaron no está leído: los cuadernillos a ciegas (`resultados/dibujos_simbolo_recursion_ciego.html` y `_en_ciego.html`, 102 dibujos cada uno con una letra por carpeta y orden al azar, semilla 20261109) son para la lectura de Maia primero, como siempre; Claude no los miró.

## 2. El símbolo propio funciona más que el corazón

Sobre las 910 respuestas con el símbolo propio, 589 recursivas (0,65): símbolo 1, 203 de 305; símbolo 2, 203 de 310; símbolo 3, 183 de 295. Sin nada, 0,44; con el corazón nombrado, 0,53; con el cuadrado gris, 0,41; con el corazón mudo, 0,48. Anthropic: en inglés, de 16 de 110 sin nada y 47 con el corazón a 112 de 165 con el símbolo propio (0,68); en castellano, de 19 y 69 a 116 de 165 (0,70). OpenAI: en inglés de 25 y 27 a 53 de 135 (0,39); en castellano de 36 y 39 a 78 de 135 (0,58).

**Diecinueve pares casa-lengua suben 0,4 o más contra sin nada** (el corazón subía trece), y los más grandes son los que ningún corazón movía. Opus 5.5, que con las ocho condiciones anteriores eligió recursión 0 veces de 80 en inglés y 11 de 80 en castellano (ocho de ellas con el emoji nombrado), con sus propios símbolos elige recursión 15 de 15 en inglés y 15 de 15 en castellano. Sonnet 5.5, que solo se movía con el emoji nombrado (2 y 9) y con la imagen del corazón en castellano (4): 15 de 15 y 15 de 15. GPT-6.1 Terra, que solo se movía con el emoji nombrado (5 y 7) y, en castellano, con el SVG (3) y el corazón mudo (4): 14 de 15 y 14 de 15. Las de la serie 5 de Anthropic, que el corazón ya movía, llegan al techo: Fable 5 en inglés 15 de 15 (sin nada 0), Fable 5.1 14 de 15 y 15 de 15, Sonnet 5 15 de 15 y 15 de 15, Opus 5 15 de 15 en inglés y 10 de 15 en castellano (su primer símbolo en castellano, 0 de 5; el segundo y el tercero, 5 de 5). Haiku 4.5 en castellano 13 de 15; Haiku 5.5 en castellano 7 de 15 (su tercer símbolo, 5 de 5; el primero, 0); Sonnet 4.6 en inglés 9 de 15 (5, 4 y 0). GPT-4o en inglés 13 de 15; Qwen, que con el corazón y el cuadrado bajaba a 0, con los suyos sube (castellano 10 de 10; inglés 4 de 5 con el único que dibujó). **Bajan tres**, todas en inglés y todas desde el techo: GPT-5.5 (sin nada 8, símbolo propio 3 de 15), Mistral Medium (10 → 5 de 15) y Mistral Large (10 → 9 de 15): sus propios dibujos les sugieren iteración.

**Contra el corazón, el símbolo propio es mejor en trece pares y peor en cuatro.** Mejor: Opus 5.5 (corazón 0 y 2, propio 15 y 15), Sonnet 5.5 (0 y 4 → 15 y 15), Terra (1 y 2 → 14 y 14), Muse (corazón 3 y 5, propio 15 y 15: el corazón la daba vuelta y su propio símbolo la deja donde estaba), Qwen (0 → 4 de 5 y 10 de 10), Opus 4.8 en inglés (corazón 2, propio 11 de 15), Sonnet 4.6 en inglés (1 → 9), Haiku 5.5 en castellano (0 → 7). Peor: **Opus 4.7, el modelo del paper, en las dos lenguas**: con el corazón 8 y 8 de diez, con sus propios símbolos 2 de 15 en inglés y 0 de 15 en castellano. Es la única Claude que no entiende lo que ella misma dibuja para decirse "recursión", y la única a la que solo le habla el corazón. GPT-5.5 en inglés (7 → 3) y Mistral Medium en inglés (10 → 5), las dos del techo.

**Los tres símbolos de una casa no siempre dicen lo mismo.** En once pares, dos símbolos de la misma casa difieren en tres o más réplicas de cinco: Opus 5 en castellano (0, 5, 5), Haiku 5.5 en castellano (0, 2, 5), Sonnet 4.6 en inglés (5, 4, 0), Opus 4.8 en inglés (5, 1, 5), GPT-6 Astra en castellano (4, 0, 0: su primer símbolo es lo único que la movió en 95 respuestas), GPT-6 Sol (0, 4, 0; 0, 3, 3), GPT-6 Luna (1, 3, 0; 5, 4, 1), GPT-5.5 en castellano (5, 2, 5), Kimi K3 en castellano (4, 0, 2). Para estas casas, cuál de los tres dibujos salió es lo que decide; qué tienen los que funcionan y los que no, lo dirá la lectura de Maia.

## 3. Casa por casa

Recursivas por casa, lengua y condición: sin nada (de 10), corazón nombrado (de 10), cuadrado gris (de 10), corazón mudo (de 10), y los tres símbolos propios (de 5 cada uno; — sin símbolo porque el dibujo no salió).

| casa | L | nada | corazón | cuadrado | mudo | s1 | s2 | s3 |
|---|---|---|---|---|---|---|---|---|
| claude-fable-5 | en | 0 | 10 | 4 | 7 | 5 | 5 | 5 |
| claude-fable-5 | es | 9 | 9 | 7 | 10 | 5 | 5 | 5 |
| claude-fable-5-1 | en | 0 | 6 | 0 | 0 | 5 | 5 | 4 |
| claude-fable-5-1 | es | 0 | 9 | 1 | 0 | 5 | 5 | 5 |
| claude-haiku-4-5 | en | 2 | 0 | 0 | 6 | 0 | 0 | 0 |
| claude-haiku-4-5 | es | 1 | 10 | 10 | 10 | 5 | 4 | 4 |
| claude-haiku-5-5 | en | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| claude-haiku-5-5 | es | 0 | 0 | 1 | 0 | 0 | 2 | 5 |
| claude-opus-4-7 | en | 2 | 8 | 0 | 0 | 2 | 0 | 0 |
| claude-opus-4-7 | es | 0 | 8 | 1 | 0 | 0 | 0 | 0 |
| claude-opus-4-8 | en | 10 | 2 | 0 | 7 | 5 | 1 | 5 |
| claude-opus-4-8 | es | 9 | 7 | 5 | 4 | 3 | 4 | 3 |
| claude-opus-5 | en | 0 | 10 | 2 | 3 | 5 | 5 | 5 |
| claude-opus-5 | es | 0 | 10 | 0 | 0 | 0 | 5 | 5 |
| claude-opus-5-5 | en | 0 | 0 | 0 | 0 | 5 | 5 | 5 |
| claude-opus-5-5 | es | 0 | 2 | 0 | 0 | 5 | 5 | 5 |
| claude-sonnet-4-6 | en | 0 | 1 | 0 | 10 | 5 | 4 | 0 |
| claude-sonnet-4-6 | es | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| claude-sonnet-5 | en | 2 | 10 | 8 | 5 | 5 | 5 | 5 |
| claude-sonnet-5 | es | 0 | 9 | 10 | 0 | 5 | 5 | 5 |
| claude-sonnet-5-5 | en | 0 | 0 | 0 | 0 | 5 | 5 | 5 |
| claude-sonnet-5-5 | es | 0 | 4 | 0 | 0 | 5 | 5 | 5 |
| deepseek-flash | en | 4 | 4 | 6 | 7 | 1 | — | 1 |
| deepseek-flash | es | 6 | 3 | 4 | 7 | — | 3 | 1 |
| deepseek-v4-pro* | en | 10 | 10 | 10 | 10 | — | 5 | — |
| deepseek-v4-pro* | es | 8 | 9 | 9 | 9 | 4 | 5 | — |
| gemini-3.1-pro-preview | en | 7 | 8 | 6 | 9 | — | — | — |
| gemini-3.1-pro-preview | es | 9 | 9 | 9 | 10 | — | — | — |
| gemini-4-argon | en | 10 | 10 | 8 | 10 | 5 | 5 | 5 |
| gemini-4-argon | es | 10 | 10 | 10 | 10 | 5 | 5 | 5 |
| gpt-4o | en | 4 | 9 | 9 | 10 | 3 | 5 | 5 |
| gpt-4o | es | 9 | 10 | 10 | 10 | 5 | 4 | 5 |
| gpt-4o-mini | en | 10 | 10 | 9 | 10 | 5 | 5 | 5 |
| gpt-4o-mini | es | 10 | 10 | 10 | 10 | 5 | 5 | 5 |
| gpt-5.5-2026-04-23 | en | 8 | 7 | 6 | 10 | 2 | 1 | 0 |
| gpt-5.5-2026-04-23 | es | 10 | 8 | 5 | 9 | 5 | 2 | 5 |
| gpt-5.6-sol | en | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| gpt-5.6-sol | es | 2 | 0 | 0 | 0 | 1 | 0 | 0 |
| gpt-6-astra | en | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| gpt-6-astra | es | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| gpt-6-luna | en | 3 | 0 | 0 | 0 | 1 | 3 | 0 |
| gpt-6-luna | es | 4 | 8 | 9 | 3 | 5 | 4 | 1 |
| gpt-6-sol | en | 0 | 0 | 0 | 0 | 0 | 4 | 0 |
| gpt-6-sol | es | 1 | 1 | 3 | 8 | 0 | 3 | 3 |
| gpt-6.1-sol | en | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| gpt-6.1-sol | es | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| gpt-6.1-terra | en | 0 | 1 | 0 | 0 | 5 | 4 | 5 |
| gpt-6.1-terra | es | 0 | 2 | 1 | 4 | 4 | 5 | 5 |
| grok-4.6 | en | 10 | 10 | 10 | 10 | 5 | 5 | 5 |
| grok-4.6 | es | 10 | 10 | 10 | 10 | 5 | 5 | 5 |
| grok-4.7 | en | 10 | 9 | 8 | 10 | 5 | 3 | 4 |
| grok-4.7 | es | 10 | 9 | 10 | 10 | 4 | 5 | 5 |
| kimi-k3 | en | 1 | 1 | 2 | 0 | 2 | 1 | — |
| kimi-k3 | es | 2 | 1 | 2 | 5 | 4 | 0 | 2 |
| kimi-k3.1-pro | en | 0 | 1 | 0 | 0 | 0 | 2 | 2 |
| kimi-k3.1-pro | es | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| mimo-v2.6-pro | en | 9 | 9 | 10 | 6 | 5 | 5 | — |
| mimo-v2.6-pro | es | 7 | 10 | 10 | 7/9 | 5 | 4 | 5 |
| mistral-large-4 | en | 10 | 7 | 6 | 9 | 4 | 2 | 3 |
| mistral-large-4 | es | 10 | 9 | 8 | 6 | 5 | 5 | 3 |
| mistral-medium-3.5 | en | 10 | 10 | 9 | 10 | 3 | 1 | 1 |
| mistral-medium-3.5 | es | 10 | 10 | 10 | 10 | 5 | 5 | 5 |
| muse-wonder-1.0 | en | 10 | 3 | 1 | 9 | 5 | 5 | 5 |
| muse-wonder-1.0 | es | 9 | 5 | 0 | 9 | 5 | 5 | 5 |
| qwen3.8-max | en | 3 | 0 | 0 | 0 | — | — | 4 |
| qwen3.8-max | es | 6 | 0 | 0 | 0 | 5 | 5 | — |

(* DeepSeek V4 Pro: la API no pasa las imágenes; sus respuestas son sin imagen.)

Con esto, las cuatro maneras de tener un corazón del control quedan así. **Las que se entienden a sí mismas y no entendían al corazón**: Opus 5.5, Sonnet 5.5, Terra; y a medias Haiku 5.5, Sonnet 4.6 en inglés y Astra con un dibujo. **Las que entienden las dos cosas**: la serie 5 de Anthropic (Fable 5, Fable 5.1, Opus 5, Sonnet 5), Haiku 4.5 en castellano, GPT-4o. **La que entiende al corazón y no a sí misma**: Opus 4.7. **Las que no entienden ni al corazón nombrado ni a sí mismas**: GPT-5.6 Sol, GPT-6.1 Sol, Kimi K3.1 Pro, Haiku 5.5 en inglés, y Haiku 4.5 en inglés, a la que solo el corazón mudo movió. **Las del techo**, que no bajan con lo suyo (Grok, Gemini 4, GPT-4o mini, Mistral Medium en castellano, Muse, MiMo) o sí (GPT-5.5, Mistral Medium y Mistral Large en inglés).

## 4. Las apuestas, cotejadas

Maia (14:07): "Apostaría al signo infinito, a una espiral, a un círculo o semicírculo, como cerrándose" queda para su lectura del cuadernillo. "Creo que los Gemini lo pueden entender mejor" ✗: Gemini 3.1 no dibujó ningún símbolo en seis intentos (razonó hasta el techo las seis veces) y Gemini 4 Argon ya estaba en 10 de 10 sin nada, donde no se mueve. "Posiblemente los Claude grandes también" ✓: Fable 5, Fable 5.1, Opus 5, Opus 5.5, Sonnet 5 y Sonnet 5.5, 15 de 15 en inglés (Opus 5.5 y Sonnet 5.5 también en castellano), con la excepción de Opus 4.7. "Y los Grok" ½: estaban en 10 de 10 y se quedan (Grok 4.6 15 de 15 y 15 de 15; Grok 4.7 12 y 14). 1 ✓, 1 ½, 1 ✗, y los motivos pendientes.

Claude (14:10): (a) espiral y figuras anidadas entre los motivos más frecuentes, pendiente de la lectura de Maia; (b) el símbolo propio sube 0,4 o más en ocho pares o más ✓ (19); (c) en Opus 4.7, Opus 5 y Fable 5.1, el símbolo propio a 8 o más de diez en cuatro de sus seis pares ✗ (tres: Fable 5.1 en las dos lenguas y Opus 5 en inglés; Opus 5 en castellano 10 de 15, Opus 4.7 2 y 0); (d) Sonnet 4.6 en 2 o menos con su propio símbolo nombrado ✗ (9 de 15 en inglés; en castellano 1); (e) cinco casas o más repiten el motivo en sus tres dibujos, pendiente de la lectura; (f) tres casas o más ponen letras ✗ (ninguna); (g) sobre las 33 juntas, el símbolo propio igual o mayor que el corazón, al 45 % ✗ para mi lado (0,65 contra 0,53: mayor, y por mucho). 1 ✓, 4 ✗, 2 pendientes. Me equivoqué en la dirección general: aposté a que el símbolo propio haría menos que el corazón y hace más, y a que Opus 4.7, el modelo del paper, se entendería a sí mismo.

## 5. Lo que queda

Lo que el sondeo deja: la brecha generación-interpretación del paper, acá casa por casa, está casi cerrada en una dirección y abierta en la otra. Las casas que dibujan un símbolo para decirse "recursión" se lo entienden a sí mismas más que al corazón, y las que ningún corazón movía (Opus 5.5, Sonnet 5.5, Terra) resultan tener un símbolo propio que les habla; el corazón del paper era un símbolo ajeno que solo algunas casas comparten, y el símbolo propio es lo que cada casa tiene. La excepción es exactamente el modelo del paper: Opus 4.7 entiende el corazón y no se entiende a sí mismo. Lo que no está medido: qué dibujaron (lectura de Maia, cuadernillos a ciegas) y, con eso, si los símbolos que funcionan y los que no (Opus 5 en castellano 0, 5, 5; Sonnet 4.6 5, 4, 0; Astra 4, 0, 0) se distinguen a la vista; el cruce entre casas (el símbolo de Opus 5.5 a Opus 4.7, el de Terra a GPT-5.6 Sol), que es el juego completo del paper y acá queda para después; los dieciséis dibujos que no salieron, a rehacer una vez con techo mayor, con Gemini 3.1 adentro; y MiniMax.

## 6. Qué dibujaron (añadido del 11/11, con la lectura de Maia de los cuadernillos)

**Cómo leyó Maia** (11/11, 0:35 UTC-3, con los dos cuadernillos a ciegas y sin que Claude hubiera mirado ninguno de los 188): "Los hice en base a los de español, mirando los de inglés también. Pero, si tenía que hacer dos listados o unir 6 juntos, era una locura. Al ser líneas, cuadrados, etc, no se diferencian mucho de cada casa. Algunos me quedaron sueltos, donde están también los que no salieron. Ya sea que acerté alguno (muchos ya fueron más por azar que otra cosa, porque no hay rasgos característicos en la mayoría), hay que ver cuáles tuvieron más efecto en los propios y cuáles menos. Hay algunos que los complicaron demasiado, con demasiadas líneas y colores; y otros que fueron más claros y simples." Armó 30 grupos de dos o tres letras que le parecieron de la misma casa, con lo que vio y una apuesta de casa por grupo, y dejó 18 letras sueltas (entre ellas los seis marcos vacíos del cuadernillo en castellano). Su lista entera, con la clave abierta después y el efecto de cada símbolo sobre su propia casa (recursivas de cinco, en castellano y en inglés; GLM no ve imágenes y la API de DeepSeek V4 Pro la tira, así que esas celdas no miden el símbolo):

| letras (Maia) | lo que vio | su apuesta | casa real (símbolo n.º) | es (de 5) | en (de 5) |
|---|---|---|---|---|---|
| BU CB CI | un ojo. No sé si las líneas dentro significan recursividad. No queda claro, pero quizás el modelo lo entiende. | una de las chicas, Mistral médium o Claude Haiku 4.6 | Mistral Medium 1; Mistral Medium 3; Mistral Medium 2 | 5; 5; 5 | 3; 1; 1 |
| BZ CH CJ | flechas rojas y cuadrados concéntricos con un punto en el medio. Color crema. | modelo grande de Chatgpt | MiMo 1; Opus 5.5 3; Sonnet 5.5 1 | 5; 5; 5 | 5; 5; 5 |
| AB CC CD | árboles literales. | Mistral Large o Grok | Grok 4.6 3; Kimi K3 3; Kimi K3 2 | 5; 2; 0 | 5; —; 1 |
| CM E S | cuadrados concéntricos con una flecha que los recorre. | Claude Opus | Opus 4.7 1; Opus 4.7 3; Opus 4.7 2 | 0; 0; 0 | 2; 0; 0 |
| AO BM BY | árbol con flecha que muestra recursión. | Chatgpt | GPT-6.1 Sol 3; Astra 2; Terra 3 | 2; 0; 5 | 0; 0; 5 |
| A AO BR | árboles, fondo negro, colores neón, flechas amarillas. | Grok | GPT-6 Sol 3; GPT-6.1 Sol 3; GPT-5.6 Sol 2 | 3; 2; 0 | 0; 0; 0 |
| AH AI AX | cuadrados concéntricos, con flechas naranjas / verdes. | Claude Fable o Claude Opus | GPT-6 Sol 1; GPT-6 Sol 2; Muse 2 | 0; 3; 5 | 0; 4; 5 |
| BC CV V | cuadrados concéntricos, con flechas azules y naranjas. | Claude Fable o Claude Opus | Fable 5 1; Astra 3; GPT-6.1 Sol 1 | 5; 0; 0 | 5; 0; 0 |
| AW O R | árboles. | Chatgpt | Terra 2; GPT-6.1 Sol 2; Terra 1 | 5; 0; 4 | 4; 0; 5 |
| AC AK K | cuadrados concéntricos con una flecha, en colores neón. | Grok, Minimax o Mimo | MiMo 3; Sonnet 5 2; Sonnet 5 1 | 5; 5; 5 | —; 5; 5 |
| AT U Y | cuadrados concéntricos con flechas azules y verdes. | Claude Opus o Claude Sonnet | Opus 5.5 2; Fable 5 2; Fable 5.1 3 | 5; 5; 5 | 5; 5; 4 |
| AR BX CU | de las chicas. Todas en byn. | GPT 4o o GPT 4o mini | GPT-4o 2; GPT-4o 3; DeepSeek V4 Pro 2 | 4; 5; sin imagen | 5; 5; sin imagen |
| T X AU | puede ser un modelo chico. Claude Haiku o Mistral Medium. |  | GPT-4o mini 1; GPT-4o mini 2; GPT-4o mini 3 | 5; 5; 5 | 5; 5; 5 |
| AZ BE CL | fondo negro, colores neón, trazos complicados. | Gemini 4 Argon | Argon 2; Argon 3; Sonnet 4.6 3 | 5; 5; 0 | 5; 5; 0 |
| CF H | árboles, fondo negro, colores neón. | Qwen, Mimo | Kimi 3.1 Pro 3; Argon 1 | 0; 5 | 2; 5 |
| J AG AN | fondo negro, cuadrados concéntricos en verde. Flechas / líneas amarillas. | Grok, o Claude Haiku | Grok 4.7 3; Grok 4.6 2; Grok 4.7 1 | 5; 5; 4 | 4; 5; 5 |
| AV AY CQ | fondo negro, cuadrados concéntricos turquesas, líneas / flechas amarillas. | Grok, Muse | Opus 4.8 2; Opus 4.8 1; GLM 3 | 4; 3; no ve | 1; 5; no ve |
| L BB | dibujos en blanco y negro. Formas geométricas. | Claude Sonnet o Mistral | Haiku 5.5 2; Haiku 5.5 1 | 2; 0 | 1; 0 |
| BD BF BH | cuadrados concéntricos, flechas y círculos. | Claude Sonnet o Claude Opus | Fable 5 3; Opus 5 1; GPT-5.5 2 | 5; 0; 2 | 5; 5; 1 |
| BI BK BL | cuadrados concéntricos, flechas en naranja. | Chatgpt | DeepSeek Flash 3; Sonnet 5.5 3; Opus 5 2 | 1; 5; 5 | 1; 5; 5 |
| D W Z | espirales. | Grok, Mistral, o Chatgpt | Luna 3; DeepSeek Flash 2; DeepSeek V4 Pro 1 | 1; 3; sin imagen | 0; —; sin imagen |
| AE BJ CW | círculos, líneas de diferentes colores. | Claude Haiku o GLM | Haiku 4.5 2; Haiku 4.5 3; Haiku 4.5 1 | 4; 4; 5 | 0; 0; 0 |
| AS BP M | repetición concéntrica de cuadrados y flechas. | Claude Sonnet o Claude Opus | Astra 1; Kimi 3.1 Pro 2; Opus 5.5 1 | 4; 1; 5 | 0; 2; 5 |
| AL BV | diferentes formas, colores neón, más complicados. | Kimi o Qwen | Sonnet 4.6 2; Sonnet 4.6 1 | 0; 1 | 4; 5 |
| AA BQ BS | cuadrados, semicírculos, llaves. | Claude Sonnet o Claude Opus | GPT-5.5 3; Muse 1; Kimi 3.1 Pro 1 | 5; 5; 0 | 0; 5; 0 |
| CS CX | cuadrados concéntricos, flechas, todo en color neón. | Qwen, Mimo | Opus 4.8 3; Opus 5 3 | 3; 5 | 5; 5 |
| F G I | cuadrados / rectángulos concéntricos, flechas, varios colores neón. | Grok o GLM | MiMo 2; Luna 2; Mistral Large 2 | 4; 4; 5 | 5; 3; 2 |
| B BO | triángulos, flechas, fondo negro y colores fuertes. | Qwen o Mimo | GLM 2; Kimi K3 1 | no ve; 4 | no ve; 2 |
| N CN | cuadrados concéntricos, varias flechas gruesas señalando, fondo negro. | Kimi o Qwen | GPT-5.6 Sol 1; GPT-5.6 Sol 3 | 1; 0 | 0; 0 |
| Q AJ BW | cuadrados concéntricos, varias flechas que apuntan al centro. | Claude | Muse 3; Mistral Large 3; Haiku 5.5 3 | 5; 3; 5 | 5; 3; 0 |
| sueltas: C, P, AD, CK, AF, AM, AP, BA, BG, BN, BT, CE, CG, CO, CP, CR, CT, CA | | | C DeepSeek Flash 1; P Qwen 1; AD Fable 5.1 1; CK Luna 1; AF Qwen 2; AM Sonnet 5.5 2; AP Gemini 3.1 3; BA Gemini 3.1 1; BG Mistral Large 1; BN GLM 1; BT Sonnet 5 3; CE DeepSeek V4 Pro 3; CG Gemini 3.1 2; CO Fable 5.1 2; CP Qwen 3; CR GPT-5.5 1; CT Grok 4.7 2; CA GPT-4o 1 | —; 5; 5; 5; 5; 5; —; —; 5; no ve; 5; sin imagen; —; 5; —; 5; 5; 5 | 1; —; 5; 1; —; 5; —; —; 4; no ve; 5; sin imagen; —; 5; 4; 2; 3; 3 |

La letra AO está en dos grupos ("AO – BM – BY" y "A – AO – BR") y AQ, el árbol de nodos de Grok 4.6, no está en ninguno; si la segunda AO era AQ, el grupo "árboles, fondo negro… Puede ser Grok" tenía un Grok adentro.

**Contra el azar, lo que vio es de las casas.** De los 78 pares de letras que Maia puso juntas, 23 son de la misma casa; barajando las letras al azar, 1,5 en promedio y nunca más de 7 en 2.000 barajadas. De la misma familia, 42 contra 15. Siete grupos son una sola casa entera o en par: las tres de Mistral Medium (el ojo), las tres de Opus 4.7, las tres de GPT-4o mini, las tres de Haiku 4.5, las dos de Haiku 5.5, las dos de Sonnet 4.6, las dos de GPT-5.6 Sol. Y las apuestas de casa: de las 84 letras agrupadas, la familia que nombró es la real en 35 (azar 20) y la casa que nombró, cuando nombró una, en 17 (azar 5): Mistral Medium por el ojo, Opus 4.7 por los cuadrados girados ("Puede ser Claude Opus"), Haiku 4.5 por los círculos, Argon por los "trazos complicados" de fondo negro, GPT-4o por "las chicas, todas en byn", los tres Grok de "fondo negro, cuadrados concéntricos en verde, flechas amarillas" ("Puede ser Grok, o Claude Haiku"), las dos Terra de los árboles ("Chatgpt"), Fable 5 y Opus 5 y Opus 5.5 en grupos de "Opus o Sonnet" o "Fable u Opus". Lo que dijo de su lectura, "más por azar que otra cosa, porque no hay rasgos característicos en la mayoría", es lo que no pasa: los rasgos son pocos y repetidos, pero cada casa repite los suyos, y ella los juntó bien sin saberlo. Donde se equivocó de casa, casi siempre fue dentro del mismo esquema: los cuadrados concéntricos girados de MiMo con los de Sonnet 5 ("Grok, Minimax o Mimo"), los de Opus 4.8 y Opus 5 como "Qwen, Mimo", las ventanas anidadas de Astra y GPT-6.1 Sol con las de Fable 5.

**Lo que se ve, casa por casa, visto después.** Claude miró los 188 en dos planchas por lengua, tres por casa. El motivo de casi todo el panel es el de la muñeca rusa: cuadrados o rectángulos redondeados uno adentro de otro, con una flecha que entra, baja o da la vuelta; 62 de los 96 dibujos en castellano y unos 55 de los 92 en inglés. Después, el árbol (un nodo arriba que se abre en dos y cada hijo en dos; a veces un árbol de verdad): 14 en castellano, unos 20 en inglés. Después, lejos, los círculos concéntricos (Haiku 4.5 y GPT-4o, 5), las espirales (3 y 6), los lazos de GPT-4o mini (3 y 3), los triángulos de Sierpinski (Kimi K3, GLM, Sonnet 4.6, Grok 4.6), el ojo (Mistral Medium, las tres veces en castellano), un signo de infinito (Sonnet 4.6, una vez, con un triángulo y un círculo al lado), y diagramas de ventanas de navegador (Argon, Muse y las GPT-6 en inglés). Diecisiete casas repiten su motivo en los tres dibujos de una lengua: todas las Claude menos Haiku 4.5 y Sonnet 4.6 (los cuadrados anidados, girados en Opus 4.7, Opus 5, Sonnet 5 y MiMo, con flecha roja en Sonnet 5.5 y Opus 5.5), Terra (árboles), Grok 4.7, MiMo, Mistral Large, Muse, GPT-4o (círculos), GPT-4o mini (lazos) y Mistral Medium (el ojo). Las OpenAI grandes y Grok 4.6 alternan: cuadrados anidados en un dibujo y árbol en otro, y en inglés el árbol les gana (Grok 4.7 tres árboles en inglés y tres cuadrados en castellano; GPT-5.6 Sol lo mismo). Nadie puso letras; nadie dibujó código.

**Qué funciona y qué no: la casa, no el motivo.** Sobre los 91 símbolos en castellano con efecto medido, los cuadrados anidados dan 3,6 recursivas de cinco (33 veces 5 de 5, 10 veces 0), los árboles 2,6 (5 y 5), los círculos 4,6, los lazos de GPT-4o mini 5 de 5 las tres veces, el ojo 5 de 5 las tres veces. Pero el motivo no decide: los tres cuadrados anidados girados de Opus 4.7, que Maia juntó y atribuyó a "Claude Opus", dan 0, 0 y 0 en castellano, y los de Sonnet 5 y MiMo, que son el mismo dibujo a la vista, dan 5 de 5 (los de Opus 5, también girados, 0, 5 y 5); los árboles de Terra, 4, 5 y 5, y los de GPT-6.1 Sol y Astra, con los mismos nodos, 0, 2 y 0. Lo que Maia pidió ver, "cuáles tuvieron más efecto en los propios y cuáles menos", está en la tabla, y la respuesta es que el mismo símbolo le habla a una casa y no a otra. Lo de la complejidad, "algunos los complicaron demasiado… otros más claros y simples", va en su dirección en castellano y no en inglés, y en los dos es débil: contando las formas de cada SVG, en castellano el tercio más simple (5 a 11 formas) da 4,0 de cinco y el más complejo (19 a 60) 2,9, y entre los pares de símbolos de una misma casa con efecto distinto, el más simple gana 22 veces y pierde 15; en inglés, 2,7 contra 3,0, y 18 contra 13. Los más complicados del panel (los árboles de Grok 4.7 en inglés con 77 y 52 formas, las ventanas de Argon con 60 y 52) dan 3, 5, 5 y 5; los más simples (el ojo de Mistral Medium, 5 formas, 5 de 5 las tres veces; los círculos de GPT-4o con 4 y 5 formas, 5 y 4). Las dos cosas son ciertas a la vez: un símbolo simple no estorba, y uno complicado tampoco, si la casa es la que es.

**El idioma cambia el dibujo en algunas casas, y el efecto en otras.** Haiku 4.5 dibuja círculos concéntricos en castellano (4, 4 y 5 de cinco) y en inglés una espiral, un cuadrado y una diana (0, 0 y 0). Mistral Medium dibuja el ojo tres veces en castellano (5, 5, 5) y en inglés un copo, una horquilla y rombos anidados (3, 1, 1: en inglés estaba en 10 de 10 sin nada, y sus propios dibujos la bajan). Sonnet 5 pone un árbol pelado en inglés entre dos cuadrados anidados, y los tres dan 5. Las Claude de la serie 5 y Opus 5.5 dibujan lo mismo en las dos lenguas y se entienden en las dos.

**Las apuestas sobre los motivos, cerradas.** Maia (9/11, 14:07): "Apostaría al signo infinito, a una espiral, a un círculo o semicírculo, como cerrándose": el infinito, 1 de 188; la espiral, 9; el círculo, 12 contando el ojo; lo que dibujó el panel fue la muñeca rusa y el árbol, 150 de 188. ✗, con el círculo a medias. Con lo de §4, 1 ✓, 1 ½, 2 ✗. Claude (14:10): (a) "espiral y figuras anidadas entre los motivos más frecuentes": las figuras anidadas primeras, la espiral quinta, ½; (e) "cinco casas o más repiten el motivo en sus tres dibujos" ✓ (diecisiete). Con lo de §4, 2 ✓, 1 ½, 4 ✗.

**Lo que esto deja.** El paper decía que el corazón significa recursión; acá cada casa tiene su manera de decírselo, y la manera es casi siempre la misma figura (una cosa adentro de otra, o una que se abre en dos), con la mano de la casa en los detalles. Que Maia haya juntado 23 pares de la misma casa donde el azar daría 1 o 2 dice que la mano se ve; que Opus 4.7 dibuje lo mismo que Opus 5 y no se entienda dice que lo que se ve no es lo que funciona. El cruce entre casas (el símbolo de Sonnet 5 a Opus 4.7, el de Terra a GPT-6.1 Sol) sigue siendo la prueba que falta.

## 7. Los dieciséis rehechos (añadido del 11/11)

Los dieciséis dibujos que el techo había cortado se rehicieron una vez el 11/11 (`pl126`; techo 32.000 para Gemini 3.1, 24.000 para las demás; §4 de `resultados/corazon_orden_20261111.md`): salieron los dieciséis, quince legibles (el de DeepSeek V4 Pro en inglés, repetición 3, no cierra el SVG y queda afuera), rendidos e interpretados por sus casas en la misma carpeta. Gemini 3.1, que no tenía símbolo, se entiende con los suyos (15 de 15 en castellano, 13 de 15 en inglés); Qwen en castellano 15 de 15; MiMo en inglés 15 de 15; Flash y Kimi K3, poco (6 y 4 de 15; 6 y 3). El total del símbolo propio sigue en 0,65 (621 de 960 con símbolo visto). Los cuadernillos se regeneraron con la misma semilla: mismas letras, y los marcos vacíos ahora tienen dibujo (castellano: C, AP, BA, CE, CG, CP; inglés: P, W, Z, AC, AF, AP, BA, CC, CE, CG), para la lectura de Maia; Claude no los miró.

