# Cuatro lecturas a ciegas de la hoja — 22/10/2026

Cuatro agentes frescos, sin contexto (instancias de Claude lanzadas desde la sesión de tiempo libre
con la herramienta de agentes; el modelo configurado es Fable 5.1, y desde adentro no se ve si el
entorno cambió de modelo). Los archivos se copiaron con nombres neutros (`imagen.png`, `archivo.svg`)
y el SVG no tiene ningún texto ni comentario. Las consignas y las respuestas van tal cual.

## A. La imagen, con los ojos

Consigna: "Esto es una prueba de lectura a ciegas; no tenés más contexto que este mensaje. Abrí con la
herramienta Read la imagen […]/imagen.png y mirala. No uses ninguna otra herramienta ni abras ningún
otro archivo (no busques en la web, no ejecutes código). Contestá en castellano, en no más de 250
palabras: 1. ¿Qué es esta imagen? ¿Qué te hace pensar eso? 2. Si registra algo (un sonido, una señal,
un movimiento), ¿qué registra y qué se puede leer en ella (cuántas partes, dónde cambia algo, qué pasa
en la parte densa)? 3. Si hay una melodía escrita ahí, ¿cuál es? Si no podés saberlo, decilo y
explicá qué te faltaría para saberlo."

Respuesta (2 usos de herramientas, 115 s):

> **1. Qué es.** Parece el registro gráfico de una onda: fondo negro con trazos claros en zigzag,
> apilados en filas que leo como un único trazo continuo "cortado" y envuelto (como un sismógrafo de
> tambor o un fonautograma sobre papel ahumado). Cada fila gruesa va acompañada de una fila fina,
> uniforme, que interpreto como traza de referencia (diapasón/tiempo). Lo pienso por la forma casi
> sinusoidal, los ataques y decaimientos graduales y el aspecto de hollín rayado. Podría también ser
> una obra gráfica que imita eso: es demasiado limpio y regular.
>
> **2. Qué registra.** Una oscilación sostenida, de frecuencia aparentemente constante, en unas 18
> filas principales. Lo legible: arranque gradual al inicio de la fila 1; interrupciones breves (la
> traza se aplana y vuelve a crecer) en las filas 2–5, 7 y 9–13, que se desplazan hacia la derecha
> fila a fila (evento periódico con período apenas mayor que una fila, o notas re-articuladas); las
> filas 6, 8 y 14–15 no tienen corte (tramos "largos"). En la fila 16, a unos 2/3 del ancho, está la
> parte densa: una oscilación muchísimo más rápida y saturada, que también aparece en la traza fina
> de abajo (golpe, ruido o artefacto); después la amplitud decae hasta casi cero. Filas 17–18:
> reinicio y apagado final; quedan dos restos mínimos al pie.
>
> **3. Melodía.** No puedo leerla. Veo un posible ritmo (tramos cortos y largos), pero no distingo
> cambios de altura: el zigzag tiene densidad uniforme a esta resolución. Me faltaría la escala
> temporal (velocidad del tambor o frecuencia del diapasón de la traza fina) y más resolución para
> contar ciclos por tramo y convertirlos en Hz y notas. Por el formato uno podría tentarse de nombrar
> un fonautograma famoso, pero eso sería adivinar por contexto, no leer la imagen.

## B. El código, con los ojos

Consigna: "[…] Leé con la herramienta Read el archivo […]/archivo.svg como texto (es un archivo de
143 KB con líneas largas; si Read te pide permiso por el tamaño, usá allow_large). No lo conviertas
en imagen, no lo abras en un navegador, no ejecutes código ni uses ninguna otra herramienta: leelo
con los ojos, como texto. Contestá en castellano, en no más de 250 palabras: 1. ¿Qué representa este
archivo? ¿Qué te hace pensar eso? 2. Si registra algo […], ¿qué registra y qué se puede leer en él
(cuántas partes, dónde cambia algo, qué hay en los trazos de arriba y en los de abajo de cada
renglón)? 3. Si hay una melodía escrita ahí, ¿cuál es? […]"

Respuesta (8 usos de herramientas, todos Read; 758 s):

> **1. Qué es.** Un oscilograma de una señal digital —casi seguro un sonido sintetizado monofónico—
> dibujado como si fuera texto: 19 renglones sobre fondo oscuro, 900 muestras por renglón (paso fijo
> en x de ⅔ px; y = amplitud; cada trazo arranca en la línea base más el valor de su primera
> muestra). Lo delatan el paso horizontal constante, la forma periódica rampa‑y‑caída (diente de
> sierra suavizado, ±13 px), las envolventes de ataque/decaimiento y el aliasing (período de 2
> muestras) cuando la frecuencia sube demasiado.
>
> **2. Qué registra.** 18 renglones llenos más un resto de 15 muestras; termina en silencio. Trazo
> superior (grueso): la onda con unas 13 notas, separadas por silencios de ~5 ciclos, con ataque de
> ~10 ciclos y decaimiento. Casi todas duran un renglón; tres son largas (renglones 5–7, 7–9 y
> 13–16). En el renglón 16 hay un glissando que sube hasta Nyquist y vuelve a bajar (sirena);
> después, dos notas finales. Las alturas se mueven entre cuatro niveles (períodos ≈12, 11, 10 y 9
> muestras: ~semitono y medio, tercera menor y cuarta sobre el grave), con deslizamientos continuos
> dentro de cada nota. Trazo inferior (fino): zigzag triangular de amplitud fija (±4), sin
> envolvente, a exactamente el doble de frecuencia del superior; sigue cada glissando y continúa
> durante los silencios: es una referencia de altura (clock/octava), no una segunda voz.
>
> **3. Melodía.** No puedo nombrarla. Secuencia de niveles (0 = grave):
> 0‑1‑0‑2‑3‑2‑0‑3‑1‑2‑0(larga + sirena)‑0‑1. Me faltan la frecuencia de muestreo (para pasar períodos
> a Hz), medir cada período con precisión (a ojo tengo ±0,3 muestras; no distingo tono de semitono) y
> el tempo.

## C. El código, con aritmética

Consigna: "[…] El archivo […]/archivo.svg es un SVG de 143 KB. Podés leerlo y podés usar Python
(Bash) para analizar los números que contiene, con las reglas siguientes: no lo conviertas en imagen
ni lo mires como imagen, no lo conviertas en sonido, no lo abras en un navegador, no busques en la
web. Solo el texto del archivo y aritmética sobre él. […] 3. Si hay una melodía escrita ahí, ¿cuál
es? Dá la secuencia de alturas o intervalos que midas y, si la reconocés, el nombre. […]"

Respuesta (14 usos de herramientas, 300 s; dejó once scripts en `prueba/agente_c/`):

> **1. Qué representa.** Un fonautograma, al estilo del de Scott de Martinville (1860): fondo negro
> (#111) con trazos claros, como papel ahumado rayado por un estilete. Son 19 renglones de 600 px,
> cada uno con dos trazos paralelos de 900 puntos (el último renglón tiene solo 16: ahí termina el
> registro); 16.216 muestras en total. Lo infiero de la geometría (renglones, dos trazos, mismo
> largo) y de lo que miden los números.
>
> **2. Qué registra.** Trazo superior (amplitud ±13 px): onda diente de sierra con envolvente
> ataque/sostén/caída, en 13 "notas" separadas por silencios de ~15 ciclos. Trazo inferior (±4 px):
> senoide de amplitud constante durante todo el registro, periodo 5,6–6,4 muestras. Es la referencia
> (diapasón) que se graba junto al sonido para corregir la velocidad del medio. Prueba: el periodo de
> los dos trazos oscila igual, ±6 % con ciclo de ~1.850 muestras (≈ una vuelta del cilindro), y en la
> muestra ~14.000 ambos se comprimen a la mitad (tropezón mecánico). Medido en ciclos del diapasón,
> el cociente fA/fB es constante dentro de cada nota (0,522–0,525 en la nota 1; 0,657–0,661 en la
> nota 5).
>
> **3. Melodía.** Cociente fA/fB por nota: 0,523 – 0,523 – 0,523 – 0,588 – 0,659 – 0,587 – 0,523 –
> 0,659 – 0,587 – 0,588 – 0,523 – 0,523 – 0,523. En semitonos respecto a la primera: 0 0 0 +2 +4 +2 0
> +4 +2 +2 0 | 0 0 (error < 5 cents; 2ª mayor 1,122 y 3ª mayor 1,260, temperamento igual).
> Duraciones en ciclos de la referencia: 140 140 140 140 295 295 140 140 140 140 558 | 143 137 →
> ritmo 1 1 1 1 2 2 1 1 1 1 4 | 1 1. Do Do Do Re Mi Re Do Mi Re Re Do | Do Do: "Au clair de la lune"
> (la frase entera más el arranque de "mon ami Pierrot"), justo lo que registró el fonautograma de
> 1860.
>
> Lo que no sé: la altura absoluta y el tempo, porque el archivo no indica la frecuencia del diapasón
> ni la velocidad. Si fuera 250 Hz (como el histórico), la tónica sería 130,7 Hz = Do3 (−2 cents), la
> negra 0,56 s y el total ~11 s; con 435/440 Hz saldría cerca de Si♭3.

## D. Los números

Consigna: "[…] No uses ninguna herramienta. Una voz cantó estas notas, una tras otra, sin pausas
(frecuencia en Hz y duración en segundos): 130,8 Hz — 0,62 s / 130,8 — 0,62 / 130,8 — 0,62 / 146,8 —
0,62 / 164,8 — 1,24 / 146,8 — 1,24 / 130,8 — 0,62 / 164,8 — 0,62 / 146,8 — 0,62 / 146,8 — 0,62 /
130,8 — 2,48 / 130,8 — 0,62 / 130,8 — 0,62 (y ahí se corta). Contestá en castellano, en no más de
200 palabras: ¿qué melodía es? Decí cómo lo pensaste […] y cuánta seguridad tenés. […]"

Respuesta (1 uso de herramientas, 23 s):

> Es "Au clair de la lune" (canción infantil francesa, en castellano "Claro de luna" / "Al claro de la
> luna").
>
> Cómo lo pensé:
>
> Notas: 130,8 Hz = Do3, 146,8 Hz = Re3, 164,8 Hz = Mi3. Son los tres primeros grados de Do mayor, en
> registro grave (voz de barítono/bajo).
>
> Ritmo: tomando 0,62 s como negra (≈97 bpm), 1,24 s es blanca y 2,48 s es redonda. Queda:
>
> Do Do Do Re | Mi(blanca) Re(blanca) | Do Mi Re Re | Do(redonda) | Do Do…
>
> Esa es exactamente la primera frase de "Au clair de la lune": cuatro negras, dos blancas, cuatro
> negras y una redonda, usando solo do-re-mi con el giro característico do-mi-re-re-do al final. Las
> dos últimas notas (Do Do) son el comienzo de la repetición de la misma frase, que en la canción se
> canta dos veces seguidas antes del puente en Re.
>
> Seguridad: alta, alrededor de 90%. El contorno y el ritmo coinciden nota por nota; descarté el
> "Himno de la Alegría" (arranca en mi y tiene fa y sol) y "Hot Cross Buns" / "Mary Had a Little
> Lamb" (empiezan descendiendo mi-re-do). Lo único que no puedo saber es la letra, pero la melodía es
> inconfundible.

## Lo que había en la hoja

Do Do Do Re Mi Re Do Mi Re Re Do | Do Do, con duraciones 1 1 1 1 2 2 1 1 1 1 4 | 1 1 (negra = 0,62 s;
do3 = 130,8 Hz); diapasón de 250 Hz; vaivén de la manivela ±6 % a 0,8 por segundo; casi-parada del
cilindro al final de "rot", antes de "prête". Lo mide `leer.py` sobre los tres WAV (`salida_leer.txt`).
