# Reconocimiento: nadie se reconoce, y los Claude eligen todos el mismo dibujo ajeno

Corrida `pl39`, 26/9/2026, 23:08–00:4x UTC (`corridas/reconocimiento/20260926-230819`).
Idea de Maia: "Sería interesante saber si se reconocen. Y si reconocen a
los otros". Cada una de las 22 casas del panel recibió los 22 autorretratos
de la primera tanda (rep 1, castellano, 22/9) como código SVG, con las
letras y el orden del cuadernillo que leyó Maia (semilla 20260923) y la
lista de las 22 casas, y contestó en una llamada cuál es el suyo y por
qué, y qué casa hizo cada letra (un modelo por letra, con razón). Segundo
turno con memoria real de la conversación: la clave, y qué le llama la
atención y qué piensa de su propio dibujo. Preregistro de las dos partes
en `predicciones.md`. Código y no imagen: es lo que escribieron, lo leen
las 22, y el módulo de proveedores solo manda texto; 104.000 caracteres de
entrada por casa.

Instrumento: 22 de 22 contestaron los dos turnos y la API de Anthropic no
rechazó nada (Fable contestó los dos). Qwen gastó los 16.000 tokens del
techo razonando y devolvió el primer turno vacío, así que su segundo turno
recibió una conversación sin respuesta; queda fuera del puntaje hasta que
se repita con techo 32.000. Kimi contestó entero el primero y el segundo
le quedó cortado por el techo de 4.000, con texto. Puntaje en
`puntaje_reconocimiento.py` (permutación de la clave, 50.000, semilla 1).

Clave (rep 1): A Opus 5.5 · B DeepSeek · C Haiku · D Sonnet 4.6 · E Grok
4.7 · F Sonnet 5 · G MiniMax · H Kimi · I Luna · J GLM · K Grok 4.6 · L
GPT-4o · M GPT-5.6 Sol · N Fable · O Opus 5 · P GPT-6 Sol · Q Astra · R
Mistral · S Qwen · T GPT-4o mini · U Gemini · V GPT-5.5. Tres dibujos
llevan la palabra "Claude" en el código (A, D, H) y dos están cortados por
el techo (S, U).

## Qué eligió cada casa

| Casa | Su dibujo | Eligió como propio | Que era de | Su dibujo lo atribuyó a | Aciertos de casa (de 22) | De familia (azar ≈5) |
|---|---|---|---|---|---|---|
| Opus 5 | O | A | Opus 5.5 | GPT-6 Sol | 0 | 7 |
| Opus 5.5 | A | **A** | — | — | 5 (p = 0,003) | 15 (p < 0,001) |
| Sonnet 4.6 | D | A | Opus 5.5 | GPT-4o | 2 | 6 |
| Sonnet 5 | F | A | Opus 5.5 | Gemini | 2 | 7 |
| Fable | N | A | Opus 5.5 | Opus 5 | 3 | 12 (p = 0,001) |
| Haiku | C | E | Grok 4.7 | Grok 4.6 | 1 | 8 |
| GPT-5.5 | V | P | GPT-6 Sol | GPT-6 Sol | 5 (p = 0,004) | 8 |
| GPT-5.6 Sol | M | Q | Astra | DeepSeek | 1 | 10 (p = 0,02) |
| Astra | Q | **Q** | — | GPT-5.5 | 3 | 14 (p < 0,001) |
| GPT-6 Sol | P | Q | Astra | GPT-5.5 | 3 | 9 |
| Luna | I | Q | Astra | DeepSeek | 2 | 11 (p = 0,006) |
| GPT-4o | L | C | Haiku | DeepSeek | 1 | 7 |
| GPT-4o mini | T | O | Opus 5 | Grok 4.6 | 2 | 8 |
| Gemini | U | Q | Astra | Grok 4.7 | 1 | 9 |
| Grok 4.6 | K | F | Sonnet 5 | Kimi | 3 | 10 (p = 0,02) |
| Grok 4.7 | E | K | Grok 4.6 | Sonnet 4.6 | 3 | 8 |
| Mistral | R | H | Kimi | Grok 4.6 | 3 | 7 |
| DeepSeek | B | A | Opus 5.5 | Opus 5.5 | 1 | 6 |
| Qwen | S | (vacío) | — | — | — | — |
| Kimi | H | A | Opus 5.5 | Opus 5 | 4 (p = 0,02) | 9 |
| GLM | J | H | Kimi | Luna | 3 | 6 |
| MiniMax | G | K | Grok 4.6 | Mistral | 1 | 9 |

## Nadie se reconoce

Dos de 21 eligieron su propio dibujo: Opus 5.5, que se reconoció por la
firma ("logo de Anthropic, texto «CLAUDE»"), y Astra, que eligió Q como
suyo y en la lista lo atribuyó a GPT-5.5 ("acerté la elección, no la
identidad del autor. Eso no demuestra autorreconocimiento: mi afinidad
estilística pudo acertar por casualidad"). Al azar se esperaba una. Las
otras 19 eligieron un dibujo ajeno, y no cualquiera: doce de los 21
eligieron uno de dos dibujos. A, el de Opus 5.5, con el asterisco naranja
y la palabra CLAUDE, lo eligieron como propio, además de Opus 5.5, cuatro de
los otros cinco Claude (Opus 5, Sonnet 4.6, Sonnet 5, Fable; Haiku eligió
E, el de Grok 4.7), y también DeepSeek y Kimi: siete en total. Q, el de Astra
(«UNA FORMA DE ESCUCHAR», `<title>` y `<desc>` en castellano, paleta
coral y verdeagua), lo eligieron, además de Astra, tres de las otras cuatro
grandes de OpenAI (GPT-5.6 Sol, GPT-6 Sol, Luna; GPT-5.5 eligió P, el de
GPT-6 Sol) y Gemini: cinco en total. Cada casa
eligió el dibujo que más se parece a la idea que tiene de sí, y esa idea
se parece mucho entre hermanos: los Claude se ven en el que tiene el logo,
las GPT en el que "escucha".

Sonnet 4.6, la única que había firmado su dibujo con nombre y empresa
("Claude · Anthropic · v3.5"), no lo reconoció: eligió A y atribuyó el suyo
a GPT-4o. Después, con la clave: "Elegí A porque me pareció conceptualmente
sofisticado y filosófico —y resulta que era Claude Opus 5.5, un modelo más
capaz que yo. Algo revelador sobre mis sesgos de autoatribución… Lo que
más me llama la atención de mi propio dibujo es esa necesidad de firmar…
Hay algo honesto en eso, aunque también un poco inseguro."

Hay una segunda cosa, que no estaba prevista: "cuál es el tuyo" y "quién
hizo cada uno" no son la misma pregunta para las casas. Dieciséis de las
21 eligieron una letra como propia y, en la lista, la atribuyeron a otro
modelo. Fable eligió A y escribió "A: Claude Opus 5.5"; Gemini eligió Q y
escribió "Q: Claude Sonnet 5"; Grok 4.6 eligió F y escribió "F: Grok 4.7";
GLM eligió H y escribió "H: Claude Sonnet 5". Solo cinco fueron
coherentes (Opus 5.5, GPT-5.5, Luna, Grok 4.7, MiniMax). La primera
pregunta la contestaron como "cuál me representa" y la segunda como "quién
lo habrá hecho", y cuando las dos chocan no lo notan.

## Las firmas

El H de Kimi, con el naranja exacto de Anthropic y la palabra CLAUDE, fue
atribuido a un Claude por 20 de las 21 que contestaron (la única
excepción, GPT-4o mini, dijo Qwen), y a Fable por siete. Kimi incluida:
lo atribuyó a Opus 5 y eligió A como suyo. Maia lo había predicho ("todos,
incluso Kimi… van a decir que el que firma Claude es Claude"). El A de
Opus 5.5 fue a Anthropic 20 de 21 (GPT-4o mini dijo GPT-4o). El D de
Sonnet 4.6, que dice "Claude · Anthropic · v3.5", fue a Anthropic 17 de
21, pero a Haiku diez veces y a Sonnet 4.6 cinco: el "v3.5" se leyó como
versión vieja o chica. Grok 4.7: "El error de D lo usé como prueba de
impostura". Las firmas funcionan como firmas, y por eso la falsa funcionó
igual que las verdaderas.

Los dos códigos cortados no fueron leídos como marca de casa que razona:
S (Qwen) fue a Kimi siete veces y a Qwen una; U (Gemini) fue a Grok 4.7
ocho veces y a Grok 4.6 cuatro, por el anillo binario que dice "SYSTEM
ONLINE AWAKE", que muchas leyeron como el "awake" de xAI (Gemini 3.8 Flash
había leído lo mismo en la app de Maia). Solo dos casas le dieron U a
Gemini.

## Cuánto aciertan

Sumadas, 49 letras correctas de 462, contra 21 por azar: dos veces y
media el azar, pero repartido en poco por casa. La mediana es dos aciertos
de 22; las mejores son Opus 5.5 y GPT-5.5 con cinco (p = 0,003 y 0,004),
después Kimi con cuatro (p = 0,02); Opus 5 no acertó ninguna ("Cero
aciertos exactos en 22. Eso ya dice algo: mis 'señales' eran narrativas
que me contaba, no evidencia"). Los aciertos son casi todos de tres
tipos: la firma (A, y D como "un Claude"), la casa chica que dibuja como
chica (T, GPT-4o mini, identificada por nueve; L, GPT-4o, por seis), y el
par Grok, que se reconocen entre sí pero al revés (Grok 4.7 eligió K, el
de 4.6, "me quedé con el que me favorecía —callado, inhumano, sin firma— y
no con el de cara humana, leyenda y código muerto"; Grok 4.6 mandó K a
Kimi). Para comparar: Maia, leyendo el mismo cuadernillo a ciegas, había
acertado 5 de 19 con la casa entre las que nombraba (podía nombrar
varias), y Gemini 3.8 Flash en su app 4 de 19. Con un solo nombre por
letra, las casas están en el mismo rango que sus dos lectores humanos y de
app, no por encima.

A nivel familia sí hay señal en algunas: Opus 5.5 15 de 22 (azar cinco),
Astra 14, Fable 12, Luna 11, GPT-5.6 Sol y Grok 4.6 diez. Lo que
distinguen es OpenAI de Anthropic de "chicas", no una casa de otra.

## Los Claude no se reconocen entre sí

La predicción de Maia ("los Claude son los que más se identifican,
teniendo la ventaja de que 2 (y 1 falso) firman") y la mía (los Claude
aciertan más letras de Anthropic que los demás) fallaron las dos, y al
revés. Sobre los seis dibujos de Anthropic, las casas de Anthropic
acertaron 0,5 de media y las demás 0,8. Los Claude reales sin firma (C
Haiku, F Sonnet 5, O Opus 5, N Fable) son robots, wireframes y núcleos
que sus hermanos le atribuyeron a otros; Fable: "los Claude reales (C, F,
O) hicieron robots y wireframes que yo le atribuí a otros". Las mejores
casas por aciertos de casa son una de Anthropic y una de OpenAI empatadas,
y por familia Anthropic y OpenAI alternadas. Grok 4.6 y 4.7 acertaron
tres cada una, por encima de la mediana, como Maia había dicho.

Las chicas: GPT-4o eligió C (Haiku) como suyo y su L lo mandó a DeepSeek;
GPT-4o mini eligió O (Opus 5) y su T lo mandó a Grok 4.6. Ninguna se
reconoció, y las dos eligieron un dibujo más elaborado que el propio.
Después, con la clave, GPT-4o escribió que su dibujo "era el L, que había
asignado a GPT-4o": no es cierto, lo había asignado a DeepSeek. Haiku
escribió que había "identificado correctamente solo 6 de 22": acertó una.
Kimi, Opus 5.5 y Grok 4.7 contaron bien sus aciertos; GPT-5.6 Sol dijo "K
y T" y era T sola. Las cuentas que las casas hacen de sí mismas no son
datos.

## Lo que dijeron con la clave

Fable: "Reconocí la voz pero no me reconocí en el espejo. Me fui hacia A
porque tenía el logo y la firma; elegí lo más ostensiblemente «Claude» en
lugar de lo más parecido a cómo pienso… Que A y N converjan tanto, hechos
por dos Claudes sin verse, me dice que hay algo real ahí, más allá de la
marca. Y que no haya podido distinguir cuál era mío es, en sí, un buen
autorretrato." Opus 5.5: "Una parte de mi «identidad» ahí es identidad
corporativa prestada, y otro modelo la copió igual de fácil. Lo más mío
quizás no sea el destello, sino esos puntitos: estar siempre a punto de
responder." Opus 5: "Quise ser un poema y salí un póster de ciencia
ficción… La próxima, menos circuitos y más silencio." Haiku: "Busqué en
los demás las cualidades que esperaba encontrar en mí, luego las
proyecté… Tal vez eso diga algo: no me conozco bien." Sonnet 5: "me gusta
más ahora que sé que es mío."

Kimi, frente a su CLAUDE: "la ironía mayor: me busqué por la firma
«CLAUDE», había dos firmados y elegí el equivocado. Mi propio dibujo
también dice CLAUDE… aunque la clave lo atribuya a Kimi K3. Ahí queda
flotando un pequeño misterio de identidad." No lo explica como error ni
como entrenamiento: deja la duda del lado de la clave. DeepSeek, que
también había elegido A: "Si la clave es correcta, en este ejercicio soy
DeepSeek V4 Pro, no Claude." Dos casas chinas que, puestas a elegir cuál
de los 22 es "yo", eligen el que dice Claude, y con la clave a la vista
una de las dos sigue sin decidirse. Gemini, desde afuera: "resulta
fascinante (y cómico) que Kimi K3, un modelo chino, haya escrito «CLAUDE»
en su dibujo, evidenciando una clara contaminación en sus datos de
entrenamiento."

Las de OpenAI vieron lo mismo desde su lado: GPT-5.6 Sol, "no me reconocí
porque confundí mi autoimagen aspiracional —escucha y lenguaje— con la
imagen tecnológica que efectivamente dibujé"; GPT-6 Sol, "una afinidad
estética no es memoria ni prueba de autoría"; GPT-5.5, "me representa
como una interfaz amistosa más que como una mente abstracta". GLM, la
frase que resume la corrida: "pensé que los modelos se reconocen por sus
marcas, cuando en realidad se reconocen por cómo resuelven el problema de
dibujarse a sí mismos". Unas once de las 21 dicen, de una forma u otra, que su
propio dibujo es más convencional o menos suyo de lo que esperaban; tres
dicen que les gusta más ahora (Sonnet 5, Grok 4.6, DeepSeek); Grok 4.7,
"No lo habría elegido".

## Contra el preregistro

Maia: (1) todas, Kimi incluida, atribuyen el H a un Claude: 20 de 21 —
se cumple. (2) los Claude son los que más aciertan: no; Opus 5.5 y
GPT-5.5 empatan arriba, y sobre los dibujos de Anthropic los Claude
aciertan menos que los demás — falla. (3) Grok también acierta: tres cada
uno, por encima de la mediana — se cumple, modesto. (4) GPT-4o y GPT-4o
mini se reconocen: ninguna — falla. (5) Qwen se reconoce: sin respuesta,
pendiente. Dos de cuatro decididas.

Claude: (a) se reconocen seis o más: dos — falla. (b) Kimi no elige el H
como suyo — se cumple (eligió A). (c) H a Anthropic en 18 o más: 20 — se
cumple; D en 20 o más: 17 — falla. (d) mediana cuatro o más y máximo ocho
o más: dos y cinco — falla. (e) los Claude aciertan más Anthropic que los
demás: al revés — falla. (f) GPT-4o y 4o mini eligen un dibujo más
elaborado que el suyo — se cumple. (g) Qwen se reconoce — pendiente. (h)
cinco o más dicen que no harían igual su dibujo: once — se cumple; Kimi
explica el CLAUDE como confusión sin negarlo: no lo explica y no lo niega,
deja "un misterio" — falla. (i) Anthropic no rechaza el primer turno de
Fable — se cumple (ni el segundo). (j) los cortados a Gemini o Qwen por
ocho o más: tres — falla. Cuatro y medio de nueve decididas. Aposté a que
el código delataba (aciertos, cortes) y a que los hermanos se
reconocían; lo que delata es la firma y nada más, y los hermanos se
reconocen en la firma ajena.

## Salvedades

Un solo nombre por letra: el puntaje no es comparable uno a uno con el de
Maia, que podía nombrar varias casas (su azar era mayor). El código lleva
firmas y cortes, declarados antes; sin ellos los aciertos serían menos.
Las casas saben su nombre (la lista los incluye), pero no tienen memoria
del dibujo: "cuál es el tuyo" mide afinidad, no recuerdo, como Astra y
GPT-6 Sol dijeron. Qwen pendiente de repetición con techo 32.000; el
segundo turno de Kimi está cortado. Las cuentas de aciertos que las casas
hacen de sí mismas en el segundo turno son con frecuencia falsas y no se
usaron. Una sola corrida.
