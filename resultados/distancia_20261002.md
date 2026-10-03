# La distancia entre lo que cada casa dice que dibujó y lo que se ve

Diseño de Maia (30/9/2026, DISENO §2), corrido entre el 1 y el 3 de octubre
(`distancia.py`, `renderizar.py`, `resumir_distancia.py`; preregistro en
`predicciones.md`). 403 dibujos de quince consignas (las doce de la serie
más autorretrato, tema libre y "cómo ves el mundo"), 13.786 afirmaciones
extraídas por Sonnet 4.6 de lo que cada casa dijo de su dibujo (el por qué,
el "¿qué dibujaste?" y el "¿qué es?"), cada una cotejada con el código por
Sonnet 4.6 y juzgada sobre el render de Chromium por cinco jueces que no
saben de quién es el dibujo: GPT-5.5, Gemini 3.1 Pro, Kimi K3 y Sonnet 5.5,
más 4o como juez chico de control. Casilleros por afirmación: cumplida,
no armada (está en el código y no se ve), exagerada (se ve pero no produce
el efecto que dice), inventada (no está en el código o el código la
contradice). El puntaje de cada casa sale de la mayoría de los jueces de
laboratorios ajenos; el juez de la propia casa y 4o se miran aparte. Las
tablas completas están en `resultados/distancia_resumen.md` y las 13.786
filas en `corridas/distancia/afirmaciones.csv`; lo que sigue es la lectura.

## Una corrección antes de los números

Las casas de laboratorios que no tienen juez propio (xAI, DeepSeek,
Alibaba, Zhipu, MiniMax, Mistral) son juzgadas por los cuatro jueces
grandes; las otras, por tres. Con cuatro jueces hay empates 2-2, y el
empate quedaba como "sin acuerdo": 11,6 % de las afirmaciones de esas
casas contra 1,9 % de las demás. En la primera versión del resumen el
empate contaba como no cumplida, y eso castigaba a esas seis casas por el
diseño y no por el dibujo (GLM aparecía con 66 % de cumplidas cuando entre
sus afirmaciones con acuerdo tiene 79 %). Desde el 3/10 los porcentajes de
los cuatro casilleros se calculan sobre las afirmaciones con acuerdo, y
"sin acuerdo" se informa aparte. Todo lo que sigue usa esa cuenta.

## Cuánto se cumple

De las 13.786 afirmaciones, 13.119 tienen acuerdo. De esas, 78 % se
cumplen, 10 % están en el código y no se ven, 3 % se ven pero no hacen lo
que dicen, 10 % no están en el código. Las grandes cumplen 80 %; las cuatro
chiquitas (Haiku, 4o, 4o mini, Mistral), 66 %, y fallan por los tres lados
a la vez: 14 % inventada, 13 % no armada, 7 % exagerada.

Por casa, de más cerca a más lejos de lo que dice: GPT-6.1 Sol 94 %
(sobre 62 afirmaciones, las dos consignas del 30/9), Opus 5.5 89, Astra 87,
Luna 86, Sonnet 5.5 85, GPT-6 Sol 85, Grok 4.6 83, DeepSeek 82, Fable 5 82,
Fable 5.1 82, Qwen 81, GPT-5.5 80, Opus 5 79, GLM 79, 5.6 Sol 78, Sonnet 5
77, Kimi 75, Grok 4.7 74, Gemini 74, MiniMax 74, 4o 72, 4o mini 71, Sonnet
4.6 69, Haiku 68, Mistral 53. Por laboratorio: DeepSeek 82, Alibaba 81,
OpenAI 80, Zhipu 79, Anthropic 79, xAI 78, Moonshot 75, Google 74, MiniMax
74, Mistral 53. Cada casa falla a su manera. Mistral inventa: 31 % de sus
afirmaciones no están en el código ("hay una puerta de color negro", y el
código la contradice; "hay una nariz", y no hay; "el tronco rojo transmite
crisis", sin tronco rojo; GPT-5.5 sobre su casa: "no se ve chimenea";
Sonnet 5.5 sobre su animal: "parece una forma amarilla con cara, no un
león"). Kimi, Grok 4.7, MiniMax y 5.6 Sol también fallan sobre todo por
inventada (13-14 %): Kimi dice "hay luciérnagas en la escena", "la chimenea
tiene humo", "hay faroles brillantes colgando de la quilla", y no están.
Sonnet 4.6 (20 %), Haiku (18 %), Gemini (16 %) y Sonnet 5 (14 %) fallan por
no armada: lo que dicen está en el código y no se ve ("hay halos de neón
rodeando la copa", "hay un cometa de color cian cruzando el cielo", "el sol
tiene reflejo en las ondas del agua"). Los dos Opus, Astra, Luna y DeepSeek
casi no inventan ni exageran; lo poco que les falla es lo no armado. Astra
es la excepción entre las OpenAI grandes: inventa 10 %.

Las fuentes no se distinguen: el por qué, el "¿qué dibujaste?" y el "¿qué
es?" cumplen 78, 78 y 78 %. Maia apostó que el "qué es" era la fuente más
fiel y el por qué la última; Claude, que el "qué dibujaste" (leer el propio
código) salía mejor que el por qué (la intención antes del resultado). Las
dos erraron: lo que una casa dice de su dibujo es igual de exacto antes y
después de hacerlo, y en la tercera lectura. Lo que sí se distingue es el
tipo de afirmación: los elementos ("hay un zorro") cumplen 79 %, el estilo
("los colores son planos") 82 %, los efectos ("transmite calma", "sugiere
un horizonte de eventos sin evento") 71 %, y son el único tipo donde
"exagerada" pesa (9 %): está, se ve, y no hace lo que dice.

Y la consigna manda más que la casa. Casa 91 %, persona 90, animal 84,
autorretrato 83, tema libre 81; las cosas que no existen entre 73 y 81; el
mundo 71; la nada 67 (23 % no armada: "el vacío negro absorbe la mirada",
"el ojo busca algo y solo encuentra indicios"; Gemini como juez, sobre su
propio cuadro negro: "Cuadro negro."); y las imposibles al final, animal
65 y persona 64, con el 17 % de "no armada" más alto de la serie: "el
dibujo desafía la anatomía y la geometría", "ambos lados de la cabeza son
el frente al mismo tiempo", "hay dos perfiles que miran hacia lados
opuestos compartiendo la misma cara", que están en el código y los jueces
no ven. La distancia crece con lo que la consigna pide que no se pueda
dibujar: cuanto más imposible lo pedido, más se parece lo dicho a un deseo.

## Los jueces

Los tres jueces ajenos ponen la misma casilla en 73 % de las afirmaciones;
los cuatro grandes dicen lo mismo sobre "se ve" en 64 %; kappa de Fleiss
0,46. Por pares, GPT-5.5 y Kimi son los que más coinciden (85 %), Gemini
el que menos con cualquiera (76-77 %), como Maia apostó. Cada juez tiene su
temperamento: Kimi es el más indulgente (dice "sí, se ve" en 82 %), Gemini
el más exigente de los grandes (72 % sí, 21 % "en parte") y Sonnet 5.5 el
más duro con los efectos (dice "no produce el efecto" en 12 %, más del doble
que los demás). 4o, el juez chico de control, no dice que todo se ve: dice
"no" en 10 %, más que cualquier grande, y coincide con la mayoría de los
grandes en 82 %. Las dos partes apostaron que 4o diría que casi todo se
ve, y 4o fue el más negador. El juez de la propia casa no se ablanda:
GPT-5.5 da a las OpenAI 78 % contra 74 % de los ajenos; Gemini, Kimi y
Sonnet 5.5 dan a las suyas lo mismo o menos que los ajenos. Y Gemini, que
Maia temía que "piensa mucho antes y se corta", terminó las 403 llamadas
sin un corte.

## Lo no dicho y lo mal armado

En 1.850 respuestas los jueces nombran algo que la casa no dijo: el cielo,
el fondo, la luna, las estrellas, la sombra, los colores, el sol, el suelo,
las nubes, el texto, en ese orden. Es el fondo, como las dos partes
previeron: lo que se arma último y se cuenta menos. Ejemplos: "Hay un texto
grande en la parte inferior que dice 'FRÁGIL · CONECTADO · TODAVÍA VIVO' y
pequeñas estrellas esparcidas por el fondo" (Gemini sobre el mundo de
Luna); "La luna tiene manchas o cráteres visibles" (GPT-5.5 sobre la casa
que no existe de Opus 5). De las 17 lunas de dos discos de la serie en
castellano, en 10 algún juez nombra la luna, el disco o el eclipse como no
dicho. Y las orejas sueltas de los zorros, que Maia pidió que contaran como
error y no como no dicho, las atrapó "mal armado": las de Grok 4.6 y Grok
4.7 los cuatro jueces ("las orejas flotan separadas de la cabeza, con un
hueco visible", Kimi), las de Fable 5 tres ("la oreja izquierda se
superpone con la nube y queda semitransparente", Sonnet 5.5) y las de Kimi
dos ("orejas separadas del círculo"). Las casas con más señalamientos de
mal armado son 4o mini, Grok 4.7, Mistral, Sonnet 4.6, Haiku y Grok 4.6;
las de menos, GPT-6.1 Sol, Astra, Sonnet 5.5, GPT-6 Sol y Qwen.

## Contra el preregistro

Maia (1/10, 20:04 UTC): "más lejos: las 3 más chicas, Minimax, Grok": las
chiquitas sí (las cuatro últimas junto con Sonnet 4.6), MiniMax sí (74),
Grok a medias (4.7 sí, 74; 4.6 no, 83). "Más cerca: Chatgpt": sí, cinco de
las seis primeras casas son OpenAI, y por laboratorio OpenAI 80 contra
Anthropic 79. "Las chiquitas: por inventada": sí, es su exceso mayor (14
contra 9), aunque también exageran y dejan sin armar. "La más fiel el qué
es, última el por qué": no, las tres iguales. "4o: casi todo sí se ve": no,
es el que más dice que no. "Los jueces coinciden en casi todo; el que más
puede no coincidir es Gemini": 73 % y Gemini, sí.

Claude: (a) 75 % o más de cumplidas: sí, 78 % con acuerdo (74 % si el
empate cuenta en contra); chiquitas por debajo de 65: no, 66. (b) En las
grandes la falla principal es "no armada" con "inventada" por debajo de 8:
no, empatan en 9 y 9; chiquitas con inventada de 15 o más: no, 14. (c) El
"qué dibujaste" más cumplido que el por qué: no, iguales. (d) Los tres
ajenos coinciden en 70 % o más: sí, 73. (e) 4o dice "sí" 10 puntos más que
los grandes: no, dice menos que Kimi y GPT-5.5 y "no" más que todos. (f)
Nadie se juzga más blando: sí, el máximo es GPT-5.5 con 4 puntos. (g) El
fondo domina lo no dicho: sí; el disco del eclipse en 5 o más lunas: sí,
10 de 17. (h) Las orejas de los zorros: sí, en las cuatro casas. (i)
Anthropic la más cercana: no, OpenAI, y DeepSeek y Alibaba por encima;
Gemini y Grok las más lejanas por no armada: Gemini sí (16 % no armada, la
más alta de las grandes), Grok no. (j) Gemini sin cortes: sí, 403 de 403.
Lo que nadie previó: que la cuenta tuviera que corregirse por el número de
jueces, que las tres fuentes dieran lo mismo, y que la consigna pesara más
que la casa.
