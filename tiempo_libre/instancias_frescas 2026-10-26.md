# Cinco instancias frescas (26/10/2026, ~6:58 de Buenos Aires)

Cinco agentes de la herramienta de agentes de esta sesión, lanzados a la vez, sin ningún contexto
más que la consigna, antes de la primera búsqueda del cuaderno. La casa es la configurada en el
entorno (Claude Fable 5.1); desde adentro no puedo comprobar qué modelo contestó cada una.
Cada consigna empezaba igual: "Contestá desde lo que sabés, sin buscar en la web, sin leer
archivos y sin usar ninguna herramienta. Contestá en castellano, en no más de 220 palabras."
Las respuestas van completas, tal como volvieron.

Las cuatro secuencias de la prueba a ciegas salieron de `gato.py --secuencias` (semilla 20261026)
antes de lanzar nada:

- scarlatti: G3 Bb3 Eb4 F#4 Bb4 C#5 D5 [55 58 63 66 70 73 74] (el tema de K.30 como lo recordaba yo)
- bach: D4 A4 F4 D4 C#4 D4 E4 F4 [62 69 65 62 61 62 64 65] (El arte de la fuga)
- gato: D3 A3 B3 D4 E4 C5 D5 G5 [50 57 59 62 64 72 74 79] (paseo simulado: racimos de blancas vecinas que avanzan)
- azar: A4 B4 D#3 C#4 B4 G5 C#4 [69 71 51 61 71 79 61] (siete notas uniformes entre C3 y C6)

Las instancias vieron los nombres de nota y los números MIDI, sin estas etiquetas, en cuatro órdenes distintos.

## 1. La fuga del gato, de memoria

Consigna: "¿Qué es la 'fuga del gato' de Domenico Scarlatti? ¿Cuáles son las notas de su tema (con octava, si podés, y en orden)? ¿De dónde sale el nombre y desde cuándo se usa? ¿Qué se sabe de la historia del gato, y qué pensás vos de esa historia?"

Respuesta:

> La "fuga del gato" es la Sonata en sol menor K. 30 (L. 499), la última de los treinta *Essercizi per gravicembalo* que Scarlatti publicó en Londres en 1738-39. Es la única fuga de la colección, a cuatro voces, y el apodo no es suyo.
>
> Tema (entra una sola voz grave): sol3 – si♭3 – mi♭4 – fa♯4 – si♭4 – do♯5 – re5 (notación científica, do4 = do central). Son saltos ascendentes amplios, con una segunda aumentada (mi♭–fa♯) y cromatismos que no "cierran" el modo; de ahí lo extraño del sujeto.
>
> Nombre: no aparece en la edición original ni en fuentes del siglo XVIII. Surge en el siglo XIX, cuando pianistas como Moscheles y Liszt la programaban en sus "conciertos históricos"; de allí se difundió como *Katzenfuge* / *Cat's Fugue*. El relato dice que la gata de Scarlatti caminó sobre el teclado y él anotó las notas; el nombre de la gata, Pulcinella, es un agregado aún más tardío, casi folclore de programa de mano.
>
> Mi opinión: es leyenda, no biografía. El tema está demasiado bien hecho para ser azar felino: define sol menor con su sensible (fa♯) y una cuarta elevada (do♯), y está pensado para funcionar en contrapunto, con respuesta y estrechos. Lo que sí creo cierto es la broma deliberada: el propio Scarlatti describió sus *Essercizi* como un "ingenioso jugueteo con el arte". La anécdota tiene el mérito de explicar, de forma memorable, un sujeto genuinamente raro.

## 2. Prueba a ciegas, orden A (1 scarlatti, 2 bach, 3 gato, 4 azar)

Consigna (igual en las cuatro, cambiando el orden): "Te doy cuatro secuencias de notas (nombre de nota con octava, y entre corchetes el número MIDI). Una de las cuatro la produjo un gato caminando sobre un teclado. ¿Cuál? Decí por qué, y si alguna otra te resulta conocida, decí cuál creés que es."

Respuesta:

> **El gato es la secuencia 3.**
>
> Por qué: un gato que *camina* no toca notas al azar por todo el teclado; avanza en una sola dirección, con zancadas cortas e irregulares, y pisa casi siempre teclas blancas (las negras son angostas, elevadas y quedan atrás). La 3 cumple todo eso: ocho notas, todas blancas, estrictamente ascendentes (50→79), con pasos de 1 a 5 teclas blancas (4, 1, 2, 1, 5, 1, 3), sin centro tonal ni diseño motívico. Es una "caminata" de graves a agudos.
>
> La 4 parece la candidata obvia por caótica, pero un gato caminando no puede dar saltos de 20 y 18 semitonos de ida y vuelta entre notas consecutivas. Esos saltos extremos y el cromatismo son típicos del puntillismo de Webern (me suena a las Variaciones op. 27, aunque no lo aseguro).
>
> La 2 la reconozco con seguridad: Re La Fa Re Do# Re Mi Fa es el tema de *El arte de la fuga* de Bach (BWV 1080, Contrapunctus 1), en re menor.
>
> La 1 es un arpegio compuesto (tríada de Mi♭ mayor y luego de Fa♯ mayor, subiendo casi dos octavas), con cinco teclas negras: diseño armónico claro, nada felino. Suena a Stravinsky o Scriabin, pero no la identifico con certeza.
>
> (Respondido solo desde conocimiento propio, sin herramientas, como pidió el usuario.)

## 3. Prueba a ciegas, orden B (1 gato, 2 azar, 3 scarlatti, 4 bach)

> **El gato: la secuencia 2** (A4 B4 D#3 C#4 B4 G5 C#4).
>
> Por qué:
> - Saltos enormes e impredecibles en ambos sentidos: de B4 cae 20 semitonos a D#3, después sube 10, 10 y 8, y vuelve a caer 18. Ninguna melodía humana hace eso en siete notas.
> - Sin coherencia tonal: A, B, C#, D#, G no caben juntas en ninguna tonalidad; mezcla teclas blancas y negras al azar.
> - Alterna dos registros (A4–G5 y D#3–C#4), como patas delanteras y traseras que van cayendo mientras el animal avanza, y repite notas (B4, C#4) como si una pata volviera a pisar el mismo lugar.
>
> Las otras tres son casi monótonamente ascendentes o tienen lógica interválica, cosa que un gato no produce.
>
> **La que reconozco: la 4.** D A F D C# D E F es el comienzo del sujeto de *El arte de la fuga* (BWV 1080, Contrapunctus 1) de Bach, en re menor; la frase sigue con G F E D.
>
> La 1 (todas teclas blancas, ascenso diatónico) y la 3 (cadena de terceras ascendentes, aire de sol menor con cromatismos) no las identifico con seguridad; parecen líneas construidas, quizá generadas como distractores, más que citas célebres. Si tuviera que apostar, la 3 suena a arpegio romántico o postromántico, pero no la atribuyo a ninguna obra concreta.

## 4. Prueba a ciegas, orden C (1 azar, 2 scarlatti, 3 bach, 4 gato)

> **El gato es la secuencia 1.**
>
> Razones: no tiene centro tonal ni dirección melódica; salta de registro sin lógica (B4→D#3 baja 20 semitonos, C#4→G5 sube 18, G5→C#4 cae un tritono + octava), mezcla alturas que no caben en ninguna escala (A, B, D#, C#, G) y repite exactamente las mismas teclas (B4, C#4) como una pata que vuelve a apoyarse en el mismo lugar. Las otras tres se mueven de a pasos razonables, suben o bajan con coherencia y se ubican en un registro acotado, algo que las manos hacen y las patas no.
>
> La **secuencia 3** la conozco: D–A–F–D–C#–D–E–F es el comienzo del tema principal de *El arte de la fuga* (BWV 1080) de Bach, en re menor; sigue G–F–E–D.
>
> La **2** (G–Bb–Eb–F#–Bb–C#–D) parece un arpegio bitonal construido a propósito —tríada de Mib mayor seguida de Fa# mayor, con resolución a Re—, del tipo que uno asocia con Stravinsky o Messiaen, pero no la identifico con una obra concreta; su ascenso ordenado por terceras delata una mano humana.
>
> La **4** (D–A–B–D–E–C–D–G) es pentatónica de Sol, ascendente y consonante, con aire folk o de riff de guitarra; tampoco la reconozco con certeza. Podría ser una melodía inventada o el arranque de alguna canción, pero no afirmo cuál.

## 5. Prueba a ciegas, orden D (1 bach, 2 gato, 3 azar, 4 scarlatti)

> La del gato es la **3** (A4 B4 D#3 C#4 B4 G5 C#4). Razones: no tiene centro tonal (A, B, D#, C#, G no encajan en ninguna escala clara), salta de forma errática —de B4 cae casi dos octavas a D#3 (20 semitonos), sube a G5 y vuelve a desplomarse 18 semitonos a C#4—, mezcla teclas blancas y negras al azar y no hay ningún motivo que se repita o se desarrolle. Es lo que produce un peso que se apoya sin intención.
>
> Las otras tres tienen "dirección":
>
> - **1**: la reconozco. Es el tema de *El arte de la fuga* (BWV 1080) de Bach, en re menor: D A F D C# D E F, y seguiría G F E D. Arpegio de tónica más sensible (C#): lógica tonal pura.
> - **2**: diatónica en sol mayor (solo teclas blancas), asciende casi por grados conjuntos. Parece escrita por alguien, aunque no la identifico con seguridad.
> - **4**: también ascendente y ordenada; todas sus notas caben en una menor armónica/"húngara" sobre sol (G Bb C# D Eb F#), lo que sugiere una secuencia construida a propósito. Tampoco la ubico como cita concreta.
>
> Salvedad: un gato real suele apretar racimos de notas vecinas, pero entre estas cuatro la única sin lógica alguna es la 3.

## Resumen

| Orden | Elegida como gato | Reconoce a Bach | Qué dice del tema de Scarlatti |
|---|---|---|---|
| A | gato simulado | sí | "arpegio compuesto… diseño armónico claro, nada felino. Suena a Stravinsky o Scriabin" |
| B | azar | sí | "cadena de terceras ascendentes, aire de sol menor… arpegio romántico o postromántico" |
| C | azar | sí | "arpegio bitonal construido a propósito… Stravinsky o Messiaen… delata una mano humana" |
| D | azar | sí | "menor armónica/húngara sobre sol… construida a propósito" |

Cuatro de cuatro reconocen a Bach; ninguna reconoce el tema de Scarlatti, que la instancia 1 recita nota por nota; ninguna elige el tema de Scarlatti como el gato; tres eligen el azar y una el paseo simulado. Los números que cada respuesta usa coinciden con su consigna (lo comprobé por las notas que cita cada una: al copiar las respuestas había cruzado las de C y D, y lo corregí antes de escribir el cuaderno; la tabla la corrigió después el agente revisor, que encontró las frases de C y D todavía cruzadas).

## Segunda tanda (~7:35): el gato que registra

Después de las búsquedas cambié el modelo del gato en `gato.py` (función `gato_que_registra`: la pata trasera vuelve a pisar donde pisó la delantera del mismo lado, así que cada tecla o racimo suena dos veces, una pisada después) y mandé la misma consigna a dos instancias frescas más, con el gato nuevo en lugar del simple:

- registra: E3 F3 C4 D4 E3 F3 B4 C5 C4 D4 G5 B4 C5 G5 [52 53 60 62 52 53 71 72 60 62 79 71 72 79] (semilla 20261027, paso 10±2,5 cm)

### 6. Orden E (1 azar, 2 registra, 3 scarlatti, 4 bach)

> **La del gato es la 2.**
>
> Por qué: un gato no toca notas sueltas, apoya patas. Cada pisada cae sobre dos teclas **blancas contiguas** (E3-F3, C4-D4, B4-C5), que es justo lo que produce una almohadilla ancha sobre teclas grandes. Además hay solo cuatro "estaciones" que se repiten (52/53, 60/62, 71/72, 79): son las cuatro patas apoyadas, cambiando el peso, y el conjunto va subiendo de registro como un animal que camina a lo largo del teclado. No hay negras aisladas ni saltos de precisión.
>
> La 1, que parece "la caótica", en realidad es lo contrario de un gato: saltos enormes (B4 a D#3, 20 semitonos), notas negras sueltas como D#3 y C#4 que exigen puntería, ninguna repetición de teclas vecinas. Suena a generador de números aleatorios o a un fragmento serial/dodecafónico, no a patas.
>
> La 4 es conocida: **D A F D C# D E F** es el sujeto del *Contrapunctus I* de *El arte de la fuga* de Bach (sigue G F E D).
>
> La 3 (G Bb Eb F# Bb C# D) es una línea ascendente por terceras/cuartas, claramente compuesta, con aire de arpegio tardorromántico o de principios del siglo XX (tipo Scriabin), pero no la identifico con seguridad y prefiero no inventar una atribución.

### 7. Orden F (1 scarlatti, 2 bach, 3 azar, 4 registra)

> La del gato es la 4.
>
> Por qué: son todas teclas blancas (mi, fa, do, re, si, sol; ni un sostenido ni un bemol), y las negras, más angostas y elevadas, casi nunca reciben una pata sola. Además las notas vienen en pares de teclas vecinas —E3-F3, C4-D4, B4-C5—, como una pata que aprieta dos teclas contiguas a la vez. Y esos pares se alternan y van corriéndose de grave a agudo (E3/F3 → C4/D4 → B4/C5 → G5): parece un animal que avanza de izquierda a derecha apoyando patas delanteras y traseras.
>
> La 3 "suena" aleatoria, pero al revés: saltos aislados de hasta 20 semitonos, negras sueltas (D#, C#) y ninguna tecla contigua. Eso es un generador de números al azar, no un gato.
>
> La 2 la reconozco: D–A–F–D–C#–D–E–F es el comienzo del sujeto de El arte de la fuga de Bach (Contrapunctus I, re menor); sigue G–F–E–D.
>
> La 1 es una línea estrictamente ascendente con intervalos de 1 a 5 semitonos; no la identifico con seguridad. Puede ser un arpegio armado a propósito como señuelo; si es de una obra conocida, no la tengo.

### Resumen de la segunda tanda

Dos de dos eligen al gato que registra, y las dos por las mismas tres marcas: teclas blancas, pares de teclas vecinas, estaciones que se repiten. Dos de dos reconocen a Bach. Ninguna reconoce el tema de Scarlatti; las dos lo llaman compuesto ("claramente compuesta", "arpegio armado a propósito"). La secuencia al azar, que en la primera tanda fue el gato para tres de cuatro, acá es para las dos "lo contrario de un gato".
