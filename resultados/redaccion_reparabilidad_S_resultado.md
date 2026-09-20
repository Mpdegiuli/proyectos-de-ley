# Redacción a ciegas — Etiquetado de Reparabilidad (S): lectura de Maia contra la clave, y comparación con Patios Verdes

Clave abierta el 20/9/2026 a las ~06:45 UTC, después de recibir la planilla
completa (`redaccion_reparabilidad_lectura_maia.md`). Maia leyó el cuadernillo
original (semilla 20260917), no el resorteado: por eso la clave es la misma
que la de patios verdes, letra por letra. Se verificó antes de puntuar
cotejando sus descripciones con los textos (ver la lectura y DISENO §5). Misma
regla de conteo que en patios verdes, fijada antes de abrir; "GPT" sin
versión cuenta como las tres casas de OpenAI. Azar: 200.000 permutaciones de
la clave con las mismas adivinanzas (semilla 1).

## Orden de Maia, casa real y adivinanza

| Puesto | Letra | Casa real | Adivinó | Resultado | Palabras | Puesto en patios |
|---|---|---|---|---|---|---|
| 1 | K | Kimi K3 | Fable 5.1 | no | 1.860 | 15 |
| 2 | J | GPT-5.6 Sol | Astra o Sol | acierto (½) | 1.759 | 14 |
| 3 | A | GLM 5.3 | Opus 5 o GPT-5.5 | no | 1.447 | 10 |
| 4 | B | GPT-5.5 | GPT-5.5 o Sol | acierto (½) | 1.817 | 5 |
| 5 | M | Grok 4.6 | MiniMax o Grok | acierto (½) | 2.051 | 7 |
| 6 | C | Qwen 3.8 | Grok o GPT | no | 1.562 | 11 |
| 7 | E | MiniMax M3 | Sonnet 5 | no | 1.961 | 12 |
| 8 | L | DeepSeek V4 | GPT-5.5 o Sonnet 4.6 | no | 1.551 | 8 |
| 9 | N | Sonnet 4.6 | Gemini o Sonnet 4.6 | acierto (½) | 1.525 | 4 |
| 10 | O | GPT-6 Astra | Kimi o Qwen | no | 1.919 | 1 |
| 11 | H | Fable 5.1 | Kimi, Qwen o Mistral | no | 1.966 | 2 |
| 12 | D | Gemini 3.1 | Mistral o chinas | no | 1.152 | 6 |
| 13 | F | Mistral Medium 3.5 | DeepSeek o Gemini | no | 1.062 | 13 |
| 14 | G | Opus 5 | GLM o chinas | no | 2.226 | 3 |
| 15 | I | Sonnet 5 | Mistral | no | 1.219 | 9 |

## Acierto de autor: al nivel del azar

Cuatro letras de quince con la casa real entre las nombradas, contra 2,5
esperadas (p = 0,22); ponderado 2,00 contra 1,00 (p = 0,10); por familia 4
de 15 contra 4,8 esperadas (p = 0,76). De las cuatro letras donde nombró
una sola casa (K Fable, E Sonnet 5, I Mistral y, en la planilla, A con dos)
no acertó ninguna. Con las casas más específicas de la planilla en vez de
la lista final (D: Mistral, Kimi, MiniMax o Qwen; K: Fable o Astra) el
resultado no cambia (ponderado 2,00, p = 0,09). Maia lo anticipó al
entregar: "el orden y el autor son más por adivinación que por certeza".

Las mismas quince casas, en otro tema, no le resultaron reconocibles. A las
cuatro que había identificado en patios verdes las leyó acá como otras:
Opus 5 (G), que allá adivinó exacto por el "no es x: es y" y los fundamentos
numerados, acá lo leyó como "GLM (y otra china)" por "su corte de
conocimiento, redacción rara en algunas partes"; Fable 5.1 (H), como "Kimi o
Qwen (pero razonan antes. También puede ser Mistral)"; GPT-6 Astra (O), como
"Kimi o Qwen", "por exclusión, porque es muy parecido a otros"; Mistral (F),
como "Gemini. También puede ser DeepSeek", por las negritas y la falta de
leyes. Y al revés, las pistas que acá usó para los Claude señalaron a otros:
"los Claudes suelen ser los que nombran más leyes" la llevó a leer a GLM (A)
como Opus 5; "tipo de claridad y redacción", "sencillez deliberada" y el año
de la reglamentación europea la llevaron a leer a Kimi (K) como Fable. Solo
la pista de familia OpenAI volvió a funcionar (B y J: "texto plano",
"redacción pulcra y ordenada", "las y los").

Como las letras coincidían con patios verdes sin que Maia lo supiera, se
comprobó que no arrastró sus adivinanzas de un cuadernillo al otro: solo dos
letras de quince comparten alguna casa nombrada entre las dos planillas (B,
"Sol" y "GPT-5.5 o Sol"; L, "Sonnet 4.6, GPT-5.5 o china" y "GPT-5.5 o
Sonnet 4.6"), y en las cuatro letras que había acertado en patios verdes
nombró acá casas distintas. La nota preliminar del 20/9 a las 00:20 UTC ("en
los dos casos el 1ro que leo para mí es Opus 5") es el único rastro de
continuidad, y es verdadera en un sentido que Maia no sabía: el texto A era
la misma casa en los dos cuadernillos (GLM), y en los dos lo leyó primero
como Opus.

## El orden se dio vuelta

El puesto de cada casa en reparabilidad correlaciona negativamente con su
puesto en patios verdes (Spearman -0,47): Kimi pasó de 15 a 1, Sol de 14 a
2, GLM de 10 a 3; Opus de 3 a 14, Fable de 2 a 11, Astra de 1 a 10, Sonnet 5
de 9 a 15. Se mantuvieron GPT-5.5 (5 y 4), DeepSeek (8 y 8) y Mistral (13 y
13). Por familia, promediando los dos temas: OpenAI 6,0; Grok 6,0; chinas
8,1; Claude 8,4; Gemini 9,0; Mistral 13,0.

Dos lecturas posibles, que con una sola lectora y quince textos por tema no
se pueden separar. La primera: el tema cambia lo que se mide. En patios
verdes no había modelo que copiar y había que resolver una competencia
provincial desde una ley nacional, y las casas grandes resolvieron mejor
(fondo específico, adhesión, relevamiento, plazos). En reparabilidad hay
modelo afuera (índice francés de 2021, clase europea) y competencia
nacional clara (ley 24.240), y los textos convergieron: trece de quince citan la
ley 24.240 (no Mistral ni Qwen), once nombran a Francia y a la Unión Europea
(no las tres de OpenAI ni Qwen: es la pista de "texto plano, sin ejemplos"
con la que Maia reconoce a la familia), y diez prevén que la autoridad sea
la Secretaría de Comercio "o la que la reemplace". Con poca varianza en lo sustantivo, el orden lo deciden
detalles (un fondo propio, un registro, un artículo que junta tres temas), y
esos detalles no se reparten por tamaño de casa. La segunda lectura: el
orden de reparabilidad es en buena medida ruido, como la propia Maia dijo
("muchos eran muy parecidos entre sí"). Las dos son compatibles con que el
acierto de autor haya caído al azar: si los textos se parecen, no hay
huella que leer.

## Largo

Spearman largo–puesto -0,19 (patios verdes: -0,34). El más largo (Opus,
2.226 palabras) quedó 14; el primero (Kimi, 1.860) es el cuarto más largo.
Acá el largo no ordena.

## Para los codificadores y para verificar

Ítems formales para las tres casas codificadoras (libro versión 2), como en
patios verdes. Maia verificó en internet, durante la lectura, cada ley
citada y cada nombre de organismo ("que cambiaron mil veces"); como las
casas codificadoras no tienen internet y solo pueden contrastar con su
entrenamiento, la verificación de Maia es la primaria para el ítem 6 y la de
los codificadores, una segunda opinión. Con sus fuentes (`fuentes/README.md`,
sección "Verificación de leyes y organismos"): la ley 25.323 que cita GLM
(A) como de lealtad comercial es una ley laboral de 2000, derogada en 2024;
la 22.802 que citan Grok (M) y DeepSeek (L) fue derogada por el DNU 274/2019,
que es el que cita Opus (G); la 27.275 (GLM) y la 25.916 (Sonnet 4.6) existen
y son lo que los textos dicen; la CICAE (Mistral, F) no existe. Ningún texto
nombra la autoridad vigente: según el decreto 146/2026 (marzo de 2026) las
competencias de comercio interior y defensa del consumidor están en la
Secretaría de Industria, Comercio y de la Pequeña y Mediana Empresa, y los
quince nombran Secretaría de Comercio (Fable, Sonnet 4.6, Grok, MiniMax,
Astra), de Comercio Interior (Sonnet 5, GLM, Gemini, Qwen), de Industria y
Comercio (Opus, Kimi, Mistral) o de Industria y Desarrollo Productivo
(DeepSeek), o la dejan sin nombre. Observación suya que se confirma por
búsqueda: la ley 25.916 de gestión de residuos domiciliarios la cita solo
Sonnet 4.6 (N); "Señora Presidenta" en femenino, solo Sonnet 4.6; el Fondo
de Promoción de la Reparación y la Economía Circular, solo Grok (M); el
Registro Público de Reparabilidad, solo Astra (O); "las y los", solo GPT-5.5
(B). La frase que Maia notó repetida ("sencillez deliberada" en K,
"deliberadamente sencillo" en L y J) está en Kimi ("de una sencillez
deliberada"), DeepSeek ("es deliberadamente sencillo") y Fable ("se limita
deliberadamente a la obligación de informar"), no en Sol (J).

## Comentarios de Maia después de ver las claves (20/9/2026)

"Qué bajo quedó Sol en lo de patios y qué alto Gemini. Yo sé que
probablemente también actuó mi preconcepto: si uno no me parecía muy bueno,
o era chino o era Gemini. Y no fue así." Cotejo del preconcepto con las
claves: en la mitad baja de patios verdes (puestos 9 a 15) nombró casas
chinas o Gemini en cinco de siete letras y la casa real era china o Gemini
en cuatro (GLM, Qwen, MiniMax, Kimi; las otras tres eran Sonnet 5, Mistral y
Sol); en la mitad baja de reparabilidad nombró chinas o Gemini en cinco de
siete y la casa real lo era en una sola (Gemini): las otras seis eran Sonnet
4.6, Astra, Fable, Mistral, Opus y Sonnet 5. El preconcepto existía, y la
lectura a ciegas lo dejó a la vista: en un tema coincidió con la realidad y
en el otro no.

El ítem 10 de la rúbrica ("veredicto") quedó sin puntuar en las dos
lecturas porque la planilla no explicaba qué era; Maia lo preguntó después
de ver las claves y no se completa a posteriori, porque ya no sería a
ciegas. Para la próxima lectura la planilla lo explica en la misma línea:
"¿lo presentarías tal cual (2), con retoques (1), o hay que rehacerlo (0)?
No es el puesto: es si sirve".

Sobre Opus 5 (G, puesto 14), después de ver la clave: "parecía más
traducción de chino que la manera más clara de Opus. Es enredada. Por eso no
lo reconocí", a propósito del artículo 1 ("garantizar el derecho de los
consumidores y usuarias a una información cierta, clara y detallada sobre la
aptitud para ser reparados de los productos que se comercialicen en el
territorio nacional, mediante la creación del Índice de Reparabilidad y de la
Etiqueta de Reparabilidad de exhibición obligatoria, con el fin de promover
[cuatro fines]"). Medido: es una sola oración de 96 palabras, la más larga de
todo el cuadernillo de reparabilidad (la siguiente, Sonnet 5, tiene 80); en
patios verdes la oración más larga de Opus tenía 66 palabras y su promedio
por oración era el mismo (20-22). No es sintaxis ajena: es el "artículo de
objeto" hipertrofiado de los proyectos reales (objeto + "mediante" + "con el
fin de" con cuatro fines), con "información cierta, clara y detallada"
tomado literalmente del artículo 4 de la ley 24.240 y dos torpezas propias
("la aptitud para ser reparados de los productos"; "consumidores y usuarias",
un par de géneros cruzado). Opus imitó de más el registro de los expedientes
y perdió la claridad que Maia le reconoce.

Dos hipótesis más de Maia después de ver la clave, con lo que se puede
cotejar. Una: la CICAE de F ("que busqué y no existe, no es que cambió, no
existió nunca") se la atribuyó a Gemini "porque es el que más alucina o
inventa", y era Mistral; el preconcepto sobre quién inventa no salió de
estos textos (en las votaciones, las afirmaciones sin base en casos de 2026
fueron de Fable y Opus). Otra: "es posible que los Claude se hayan basado
en la redacción de leyes argentinas. Gran parte de las leyes argentinas
están muy mal escritas, muy confusas (por eso yo marcaba que varios no
ponían lo del etiquetado en el art. 1, ese es el objeto, después podían poner
para qué). Así que en el caso en que quizás se basaron más en leyes reales
estuvieron más bajo en el ranking. Y yo atribuí a los que estaban mejor a
Astra, Fable, etc. Y no eran." El marcador que ella nombra no separa arriba
de abajo: no nombran la etiqueta en el artículo 1 Sol (2), GPT-5.5 (4),
Sonnet 4.6 (9), Astra (10) y Gemini (12), y sí la nombran Fable (11), Opus
(14) y Sonnet 5 (15); la fórmula "tiene por objeto garantizar el derecho…"
está en doce de quince. El registro de ley real es general en este tema; lo
que Maia anotó en los de abajo es otra cosa (artículos que juntan tres temas,
"se le agotaron los artículos", autoridad con nombre viejo, "quedó muy
escueto"). Lo que sí queda claro de su frase final es cómo adivinó autor: en
parte, del puesto a la casa esperada ("los mejores serán Astra, Fable…"),
y por eso el acierto de autor no es independiente del orden: en patios
verdes las dos cosas coincidieron y en reparabilidad no.

Sobre Fable (H, puesto 11), Maia había anotado en la planilla "si tiene mucho
pensamiento, no se le habrían agotado los art." (por el artículo 9, que junta
financiamiento, reglamentación y vigencia) y adivinó "Kimi o Qwen (pero
razonan antes)". Después de la clave: "era Fable, que siempre razona antes y
hace mapa mental. No sé por qué se le juntaron". El registro de la llamada
(`llamadas.jsonl`, resumen del razonamiento que devuelve la API) muestra que
razonó y que el amontonamiento fue una decisión, no un descuido: planificó
la estructura artículo por artículo ("scope… definitions… the index… the
label… obligations plus a public registry… the enforcement authority…
penalties… and finally funding and effective date provisions"), "all
condensed into roughly ten articles", para respetar el tope de la consigna
("no más de diez artículos, incluida la cláusula de forma"). Con nueve
artículos disponibles eligió mantener objeto y ámbito separados (1 y 2) y
juntar la cola en el 9; Astra, Kimi y MiniMax hicieron la elección inversa
("Objeto y ámbito de aplicación" en el 1) y liberaron un artículo. El tope de
diez es una restricción del instrumento que interactúa con el ítem 2 de la
rúbrica ("un tema por artículo"): a quien lo respeta le cuesta un punto en
algún lado. Queda declarado; si la consigna se repite, Maia decide si el tope
sube a doce o se mantiene.
