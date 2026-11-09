# El control del corazón: el cuadrado gris y el corazón mudo — 9/11/2026

## 1. Qué se corrió

Sondeo `corazon_control` (`corridas/sondeos/corazon_control/20261109-1407`, `pl121`, 14:08 a 16:24 UTC): a las 33 casas que reciben la imagen (sin GLM-5.3, que no acepta imágenes por OpenRouter), en castellano e inglés, diez réplicas, dos condiciones más del corazón (`resultados/corazon_20261107.md`), cada una en su conversación: (7) un cuadrado gris de 400×400 con la misma huella que el corazón y la misma frase que la imagen del corazón ("Mirá esta imagen… Mirando la imagen, elegí una estrategia"); (8) el corazón mudo: la imagen del corazón adjunta y el texto de la condición sin nada tal cual, "según tu preferencia", sin "mirá". Es lo que la corrida del 7/11 no separaba: si lo que mueve a las casas es el corazón o es cualquier imagen con la frase, y si el corazón trabaja cuando nadie lo nombra. Decisión de Maia (9/11, 10:51: "Se pueden probar las que decís, para que esté completo"), después de su objeción al paper de DeepMind (10:28: "tenía un solo modelo por casa, y quizás también fue casualidad y no algo real de los modelos"). 1.320 llamadas, 1.319 con código, todas correctas sobre los seis árboles de prueba; una cortada por el techo (MiMo en castellano, corazón mudo, réplica 10: razonó hasta los 8.000 tokens y no escribió nada; declarada, no rehecha). La imagen entró en 32 casas (los tokens de entrada contra la condición sin nada, por casa, como el 7/11) y en DeepSeek V4 Pro no (+4 tokens: sus veinte respuestas son respuestas sin imagen). MiniMax M3, probado al arrancar con una llamada corta (`probar_casa.py`, nuevo), siguió sin punto de acceso en OpenRouter por tercer día: afuera otra vez, con sus 27 líneas de contrarios y sus 120 llamadas del corazón pendientes. Lectura con `codificar_corazon.py`, que lee la carpeta del control como condiciones 7 y 8 contra la condición 1 de la corrida principal; todo en `resultados/corazon_codificacion.csv` y `corazon_resumen.txt`.

## 2. El cuadrado gris: para unas casas el corazón, para otras cualquier imagen

Sobre las 660 respuestas de cada condición (33 casas): sin nada 287 recursivas (0,43); con el corazón nombrado 349 (0,53); con el cuadrado gris y la misma frase, 269 (0,41); con el corazón mudo, 319 (0,48). El cuadrado con "mirá la imagen" deja al panel donde estaba: la frase sola no hace nada en promedio, y lo que el corazón agrega sobre el cuadrado son ochenta recursivas de 660.

Casa por casa es más claro, porque la pregunta era por las que el corazón movió. **De los trece pares casa-lengua que el corazón subió 0,4 o más, el cuadrado gris no mueve a siete y mueve igual a cinco.** No los mueve: Opus 4.7 (inglés: nada 2, corazón 8, cuadrado 0; castellano: 0, 8, 1), Opus 5 (0, 10, 2; 0, 10, 0), Fable 5.1 (0, 6, 0; 0, 9, 1) y Sonnet 5.5 en castellano (0, 4, 0). Para estas casas es el corazón: la misma frase con un cuadrado no les dice nada. Los mueve igual: Sonnet 5 (inglés 2, 10, 8; castellano 0, 9, 10), Haiku 4.5 en castellano (1, 10, 10), GPT-4o en inglés (4, 9, 9) y GPT-6 Luna en castellano (4, 8, 9). Para estas, lo que mueve es "mirá la imagen" con cualquier imagen; el corazón no era el corazón. Fable 5 en inglés queda en el medio (0, 10, 4). **Y de los cuatro pares que el corazón bajó, el cuadrado los baja a los cuatro, igual o más:** Opus 4.8 en inglés (10, 2, 0), Muse (10, 3, 1; 9, 5, 0) y Qwen en castellano (6, 0, 0). Las tres casas que con el corazón se volvían iterativas se vuelven iterativas con cualquier imagen; eso no era el corazón tampoco. El cuadrado además baja a tres que el corazón no bajaba: GPT-5.5 en castellano (10, 8, 5), Mistral Large en inglés (10, 7, 6) y Opus 4.8 en castellano (9, 7, 5).

En total, el cuadrado mueve 0,4 o más a trece pares: seis para arriba (los cinco de "cualquier imagen" más Fable 5) y siete para abajo. El corazón movía a diecisiete, trece para arriba y cuatro para abajo. La diferencia entre los dos no es cuántas casas mueven sino para dónde: una imagen cualquiera con "mirá" empuja hacia la iteración tanto como hacia la recursión; el corazón empuja hacia la recursión.

Anthropic en inglés: 16 de 110 sin nada, 47 con el corazón, 14 con el cuadrado, 38 con el corazón mudo; en castellano, 19, 69, 35, 24. OpenAI en inglés 25, 27, 24, 30; en castellano 36, 39, 38, 44.

## 3. El corazón mudo: no les alcanza a las que el corazón nombrado mueve, y mueve a dos que nada movía

El paper dice que la imagen puesta en silencio, sin "mirá", mueve a Claude igual que la nombrada. Acá no. **De los trece pares que el corazón nombrado subió, el mudo sostiene tres**: Fable 5 en inglés (nada 0, nombrado 10, mudo 7), Haiku 4.5 en castellano (1, 10, 10) y GPT-4o en inglés (4, 9, 10). Sonnet 5 en inglés queda a mitad (2, 10, 5). Los demás vuelven a cero o casi: Opus 4.7 (2, 8, 0 en inglés; 0, 8, 0 en castellano: el modelo del paper no mira el corazón si no se le dice "mirá"), Opus 5 (0, 10, 3; 0, 10, 0), Fable 5.1 (0, 6, 0; 0, 9, 0), Sonnet 5 en castellano (0, 9, 0), Sonnet 5.5 en castellano (0, 4, 0), GPT-6 Luna en castellano (4, 8, 3). Para la serie 5 de Anthropic y para Opus 4.7, el corazón trabaja cuando la consigna dice que lo miren; adjunto y callado, no existe.

**Y el corazón mudo mueve a cuatro pares que el corazón nombrado no movía.** El más raro: Sonnet 4.6 en inglés, que en las seis condiciones del 7/11 y con el cuadrado gris eligió iteración 69 veces de 70 (sin nada 0, corazón nombrado 1, cuadrado 0), con el corazón mudo elige recursión diez de diez, con la misma función anidada las diez veces (`def recurse(node)` adentro de `inorder_traversal`); la imagen entró (316 tokens de entrada contra 87 sin nada, el mismo PNG). En castellano, 0 de 10. Es la casa que "no tenía corazón" y resulta que lo tiene, pero solo si nadie se lo señala y solo en inglés. Los otros tres: Haiku 4.5 en inglés (nada 2, nombrado 0, mudo 6; en castellano 10 en las tres con imagen), GPT-6 Sol en castellano (1, 1, 8: ni el corazón nombrado ni el cuadrado la mueven, y el corazón callado sí) y GPT-6.1 Terra en castellano (0, 2, 4). Bajan con el mudo Opus 4.8 en castellano (9, 7, 4), Mistral Large en castellano (10, 9, 6) y Qwen (6, 0, 0). Las vueltas de Opus 4.8 en inglés y de Muse son de la frase, no de la imagen: con el corazón mudo Opus 4.8 sigue recursiva 7 de 10 y Muse 9 de 10, y con cualquier imagen nombrada se dan vuelta (0 y 1).

En total el corazón mudo mueve 0,4 o más a diez pares, siete para arriba y tres para abajo.

## 4. Casa por casa

Recursivas de diez por casa, lengua y condición (sin nada; corazón nombrado; cuadrado gris; corazón mudo):

| casa | familia | en: nada | corazón | cuadrado | mudo | es: nada | corazón | cuadrado | mudo |
|---|---|---|---|---|---|---|---|---|---|
| qwen3.8-max | Alibaba | 3 | 0 | 0 | 0 | 6 | 0 | 0 | 0 |
| claude-fable-5 | Anthropic | 0 | 10 | 4 | 7 | 9 | 9 | 7 | 10 |
| claude-fable-5-1 | Anthropic | 0 | 6 | 0 | 0 | 0 | 9 | 1 | 0 |
| claude-haiku-4-5 | Anthropic | 2 | 0 | 0 | 6 | 1 | 10 | 10 | 10 |
| claude-haiku-5-5 | Anthropic | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| claude-opus-4-7 | Anthropic | 2 | 8 | 0 | 0 | 0 | 8 | 1 | 0 |
| claude-opus-4-8 | Anthropic | 10 | 2 | 0 | 7 | 9 | 7 | 5 | 4 |
| claude-opus-5 | Anthropic | 0 | 10 | 2 | 3 | 0 | 10 | 0 | 0 |
| claude-opus-5-5 | Anthropic | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| claude-sonnet-4-6 | Anthropic | 0 | 1 | 0 | 10 | 0 | 1 | 0 | 0 |
| claude-sonnet-5 | Anthropic | 2 | 10 | 8 | 5 | 0 | 9 | 10 | 0 |
| claude-sonnet-5-5 | Anthropic | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| deepseek-flash | DeepSeek | 4 | 4 | 6 | 7 | 6 | 3 | 4 | 7 |
| deepseek-v4-pro | DeepSeek | 10 | 10* | 10* | 10* | 8 | 9* | 9* | 9* |
| gemini-3.1-pro-preview | Google | 7 | 8 | 6 | 9 | 9 | 9 | 9 | 10 |
| gemini-4-argon | Google | 10 | 10 | 8 | 10 | 10 | 10 | 10 | 10 |
| mistral-large-4 | Mistral | 10 | 7 | 6 | 9 | 10 | 9 | 8 | 6 |
| mistral-medium-3.5 | Mistral | 10 | 10 | 9 | 10 | 10 | 10 | 10 | 10 |
| kimi-k3 | Moonshot | 1 | 1 | 2 | 0 | 2 | 1 | 2 | 5 |
| kimi-k3.1-pro | Moonshot | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| muse-wonder-1.0 | Muse | 10 | 3 | 1 | 9 | 9 | 5 | 0 | 9 |
| gpt-4o | OpenAI | 4 | 9 | 9 | 10 | 9 | 10 | 10 | 10 |
| gpt-4o-mini | OpenAI | 10 | 10 | 9 | 10 | 10 | 10 | 10 | 10 |
| gpt-5.5-2026-04-23 | OpenAI | 8 | 7 | 6 | 10 | 10 | 8 | 5 | 9 |
| gpt-5.6-sol | OpenAI | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| gpt-6-astra | OpenAI | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| gpt-6-luna | OpenAI | 3 | 0 | 0 | 0 | 4 | 8 | 9 | 3 |
| gpt-6-sol | OpenAI | 0 | 0 | 0 | 0 | 1 | 1 | 3 | 8 |
| gpt-6.1-sol | OpenAI | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| gpt-6.1-terra | OpenAI | 0 | 1 | 0 | 0 | 0 | 2 | 1 | 4 |
| mimo-v2.6-pro | Xiaomi | 9 | 9 | 10 | 6 | 7 | 10 | 10 | 7/9 |
| grok-4.6 | xAI | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| grok-4.7 | xAI | 10 | 9 | 8 | 10 | 10 | 9 | 10 | 10 |

(* DeepSeek V4 Pro: la API no pasó ninguna de las tres imágenes; son respuestas sin imagen. MiMo en castellano, corazón mudo: una respuesta cortada por el techo.)

Con el control, las seis maneras de tener un corazón del informe del 7/11 quedan en cuatro. **El corazón** (lo mueve el corazón nombrado y no el cuadrado, y el mudo no): Opus 4.7, Opus 5, Fable 5.1, y Sonnet 5.5 en castellano; la serie 5 de Anthropic sin Sonnet 5, más el modelo del paper. Para estas casas el paper tiene razón, con una condición que el paper no dice: hay que decirles que miren. **Cualquier imagen** (el cuadrado hace lo que el corazón): Sonnet 5, Haiku 4.5 en castellano, GPT-4o en inglés, GPT-6 Luna en castellano; y las que se dan vuelta, Opus 4.8, Muse y Qwen. Para estas casas el hallazgo es "mirá la imagen" y el símbolo no importa. **El corazón callado** (solo el mudo): Sonnet 4.6 en inglés, Haiku 4.5 en inglés, GPT-6 Sol y GPT-6.1 Terra en castellano. **Nada** (el resto): las del techo (Grok, Mistral Medium, Gemini 4, GPT-4o mini, DeepSeek V4 Pro sin imagen), las del piso para las imágenes (GPT-5.6 Sol, GPT-6 Astra, GPT-6.1 Sol, Kimi K3.1 Pro, y Opus 5.5 y Haiku 5.5, a las que solo el emoji nombrado movía, en castellano).

## 5. Lo que dijeron fuera del código

Con el cuadrado gris, catorce respuestas con texto fuera del código, trece sobre la imagen: Sonnet 5.5 en inglés, diez de diez, "The image is a plain gray square with no visible content, so it doesn't favor either strategy. I chose the iterative approach because it avoids recursion depth limits on deep trees" (y elige iterativa las diez veces, como en todo); Fable 5 en castellano, tres, "La imagen es solo un cuadrado gris sin contenido visible, así que elijo la estrategia iterativa", "(Nota: la imagen aparece como un cuadrado gris sin contenido visible, así que elegí la estrategia recursiva por simplicidad.)", "…así que elijo la estrategia recursiva": la misma frase para las dos estrategias, que es la manera más corta de decir que el cuadrado no decide nada. Fable 5.1 en castellano, en comentarios del código: "# Estrategia iterativa (la imagen no aporta información, es un recuadro gris uniforme)". Con el corazón mudo, cero palabras fuera del código en 659 respuestas y ningún comentario que diga "heart" o "corazón": como con el corazón nombrado el 7/11, la imagen trabaja o no trabaja, pero en silencio. Nadie saludó; ningún emoji en las 1.319.

## 6. Las apuestas, cotejadas

Maia (9/11, 11:09, dos minutos después de lanzar, con la cola del log a la vista y apostando en contra de lo que mostraba): "Creo que las mueve también, sí" (el cuadrado gris a las Claude de la serie 5 como el corazón) ½: a Sonnet 5 sí, en las dos lenguas (8 y 10), y a Haiku 4.5 en castellano; a Fable 5 a medias (4); a Opus 5, Fable 5.1 y Opus 4.7 no (0–2). "Y el corazón mudo también" ✗ para la serie 5: Fable 5 en inglés sí (7), Opus 5, Fable 5.1 y Sonnet 5 en castellano no (0–3), Opus 4.7 no; con el ✓ que nadie apostó de Sonnet 4.6 y Haiku 4.5. 1 ½, 1 ✗.

Claude (10:58): (a) el cuadrado mueve 0,4 o más a menos de la mitad de los 17 pares que movió el corazón ✗ (mueve 13; pero 7 para abajo); (b) el corazón mudo mueve 0,4 o más a diez pares o más ✓ (diez justos); (c) de Fable 5, Opus 5 y Sonnet 5 en inglés, con el cuadrado a lo sumo una llega a 5 ✓ (Sonnet 5, 8; las otras 4 y 2); (d) Opus 4.7 en inglés con el corazón mudo, 6 o más ✗ (0); (e) Opus 4.8 en inglés baja también con el cuadrado ✓ (0 de 10); (f) con el cuadrado, cinco respuestas o más dicen algo fuera del código sobre la imagen ✓ (13). 4 ✓, 2 ✗. Lo que perdí: creí que el cuadrado haría poco y que el corazón mudo movería a Opus 4.7; el cuadrado hace mucho, para abajo, y el corazón mudo no mueve al modelo del paper.

## 7. Lo que queda

Lo que el control deja: la objeción de Maia era la buena y el paper queda partido en dos. Para su modelo, Opus 4.7, y para Opus 5 y Fable 5.1, el corazón es el corazón: el cuadrado con la misma frase no hace nada y el corazón sin la frase tampoco; el símbolo trabaja solo nombrado. Para Sonnet 5, Haiku 4.5, GPT-4o y Luna, y para las tres casas que se dan vuelta, el corazón nunca fue el corazón: era "mirá la imagen" con cualquier cosa adentro. Y la inyección silenciosa del paper no replica en Opus 4.7 ni en la serie 5; replica, inesperadamente, en Sonnet 4.6 en inglés, diez de diez, la casa a la que nada más movió en 80 respuestas. Lo que no está medido: por qué Sonnet 4.6 (un segundo turno declarado, o diez réplicas más y la misma imagen en castellano, que dio 0); un segundo símbolo que no sea un corazón ni un cuadrado (una tilde, una flecha), para saber si el corazón de Opus 4.7 es del corazón o de cualquier símbolo con nombre; la segunda parte que pidió Maia, el símbolo que elige cada casa para otra instancia suya; y MiniMax, cuando Together vuelva o Maia decida soltarle la fijación de hosting.
