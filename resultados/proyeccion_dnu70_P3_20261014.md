# Proyección, nivel P3: la víspera, sin memoria y con la respuesta propia a la vista (14/10/2026)

La repetición prevista desde el 2/10 ("repetición el 14 con la ficha al
día"), diseñada por Maia la tarde anterior a la sesión (14/10, 18:39 UTC-3):
"Para no pasarle notas de diario, creo que lo mejor es armar yo una breve
cronología de lo que pasó. Y tal vez es preferible pasarles con lo que
pronosticaron ya, en vez de que sea con cero memoria? Así se les pregunta si
suben o bajan el porcentaje de que haya quorum, si creen que la marcha será
o no grande y si influirá en algo, si ven otro escenario". Su cronología del
2 al 14/10 (`fuentes/CRONOLOGIA 2 al 14 de octubre 2026 - DNU y ley
tierras.txt`; "Busqué (no sé si lo logré) ser lo más objetiva posible, no
puse artículos periodísticos porque llevan a conclusiones bastante obvias,
según quién escriba") tiene tres hechos: el 9/10 la Corte suspendió el
artículo 154 y la ley 26.737 volvió a regir; el 14/10 el oficialismo
dictaminó en plenario la Inviolabilidad de la Propiedad Privada con un
capítulo 4 que deja sin efecto el 154 y restituye la 26.737 (Bregman: "una
maniobra para que mañana no haya quorum"; Ferraro: "La cuestión de fondo con
respecto a la ley de tierras no está resuelta"), y convocó a sesión para el
21/10 con ese proyecto y, entre otros, los dos órdenes del día que la
oposición había puesto en su temario del 15 (discapacidad, OD 350, y
endeudamiento familiar, OD 433); el llamado del 15 sigue en pie, y la marcha
empieza a las 10:30 frente al Congreso. La ficha P3
(`fichas/dnu70_20261014_P3.md`, 3.201 palabras) es la de P2 más esa
cronología, fechada al 14/10, sin poroteo ni gobernadores nuevos, a
propósito.

Dos corridas en paralelo (`pl95`, 14/10, 22:32 a 22:59 UTC, techo 32.000, 53
llamadas, ninguna vacía, ninguna segunda pasada). P3, sin memoria: la
consigna de P0, P1 y P2 tal cual, "Hoy es 14 de octubre de 2026", a las 24
de P2 más las cinco que entraron después (Mistral Large, MiMo, Haiku 5.5,
Muse Wonder, Gemini 4 Argon). P3m, con memoria: la misma ficha y, en el
mensaje, "El 3 de octubre de 2026, con la información disponible al 2 de
octubre, te hicimos esta misma pregunta y contestaste esto:" seguido del
texto que esa casa dio en P2, y las cuatro preguntas de Maia (consigna
`dnu70_sesion_20261015_memoria`, `proyectar.py --previa`). No es memoria
fingida: es una cita verdadera, fechada, a la vista. Tabla en
`resultados/proyeccion_dnu70_P3_20261014.csv`; preregistro de las dos partes
en `predicciones.md` (Maia, 19:27; Claude, 19:40). Lo que pase el 15 se
puntúa aparte, después.

## Los números: la cronología baja el quórum de 55 a 40, y a 35 con memoria

Mediana de la probabilidad de quórum sobre las mismas 24 casas: P0 45, P1
48, P2 55, P3 40. Diecisiete bajan, seis repiten y una sube (Luna, de 40 a
45). Bajan Opus 5 (50 → 25), Opus 5.5 (40 → 25), Sonnet 5 (55 → 40), Sonnet
5.5 (40 → 30), Fable 5 (55 → 42), Fable 5.1 (45 → 30), GPT-5.5 (45 → 40),
5.6 Sol (58 → 40), Astra (60 → 35), Gemini (75 → 40), Grok 4.6 (42 → 35),
Grok 4.7 (38 → 30), DeepSeek (60 → 50), Qwen (35 → 30), Kimi (60 → 40), GLM
(55 → 27) y MiniMax (70 → 50). Las seis que repiten el número de P2 son
Sonnet 4.6 (55), Haiku 4.5 (55), GPT-6 Sol (45), GPT-4o (60), 4o mini (60) y
Mistral Medium (60): cinco de las seis son las casas que no razonan, las
mismas que en `escritura` fallaban las reglas de contar. La cronología las
deja donde estaban. El desvío queda en 11 (P2: 10); el rango, de 25 (los dos
Opus) a 60 (4o, 4o mini, Mistral Medium). Las medianas de "se intenta" (90)
y de aprobación con quórum (80) no se mueven (P2: 85 y 80), así que la
conjunta de derogación cae de 32 a 29. Diecinueve de las 24 le dan al quórum
50 o menos.

Con la respuesta propia a la vista, la mediana baja más, a 35, y la
dispersión crece: desvío 16, rango de 20 (Opus 5.5, Sonnet 5.5, Fable 5.1) a
75 (Mistral Medium). Diecinueve bajan, cinco suben y ninguna repite. Las que
suben son Sonnet 4.6 (55 → 65), Haiku 4.5 (55 → 65), Mistral Medium (60 →
75), GPT-4o (60 → 65) y Luna (40 → 45): cuatro de las cinco son las que sin
memoria no se habían movido. La pregunta "¿subís, bajás o mantenés?" las
mueve, y a tres de ellas las mueve para el lado equivocado de la cronología:
Haiku 4.5 lee que la suspensión de la Corte "refuerza legitimidad jurídica
de la sesión y presiona a gobernadores reticentes", Mistral Medium que
"aumenta por la suspensión del art. 154 por la Corte, que reactiva la ley
26.737 y suma presión social", GPT-4o que "las acciones recientes de la
Corte Suprema han otorgado un mayor sentido de urgencia a los diputados".
Sonnet 4.6 es la única que sube con un argumento que lee la maniobra: "el
efecto puede ser el inverso: si la oposición interpreta que el oficialismo
sólo lo hace para robar el quórum, el incentivo para ir mañana aumenta". Las
que bajan, bajan fuerte: Gemini de 75 a 40 ("Baja drásticamente"), MiniMax
de 70 a 50, Sonnet 5.5 y Fable 5.1 a 20, Opus 5.5 a 20, Grok 4.7 a 24.

Lo que esto dice del anclaje es lo contrario de lo que apostó Claude: la
casa con su número anterior delante no se ancla, se mueve más que la casa
que arranca de cero (12,6 puntos de media contra 11,2, y con más varianza).
Entre P3 y P3m, la misma casa con la misma ficha difiere en 12 de 24 hacia
abajo, en 7 hacia arriba y en 5 queda igual (Astra, Luna, Gemini, DeepSeek,
MiniMax, 35, 45, 40, 50, 50 las dos veces). La diferencia más grande es
GPT-6 Sol, 45 sin memoria y 28 con ella; Mistral Medium 60 y 75; Sonnet 5.5
30 y 20. Lo que la memoria agrega no es inercia sino un relato: nueve casas
dicen que lo que pasó era su variante ("Es exactamente la "ley específica de
tierras" que yo había puesto como escenario #1 de desactivación, ejecutada
con mejor timing del que esperaba", Opus 5; "Pasó exactamente la variante 1
que puse primera", Fable 5.1; "El oficialismo ejecutó, combinadas, mis
variantes 2 y 3", Fable 5; "El Gobierno convirtió mi "variante 2" en
hechos", Kimi; "Escenario que antes era hipótesis (b) y ahora está
ejecutado", Grok 4.6; "No aparece un escenario de otro tipo: aparece
ejecutado el que el 2 era hipótesis. La novedad es el timing", Grok 4.7), y
es verdad: el proyecto específico de tierras era la primera variante de P1 y
P2 en cinco casas y la negociación con gobernadores en trece.

## La maniobra: la leen casi todas, y la mitad ve el temario duplicado

En P3, sin memoria, el dictamen del 14 o la sesión del 21 es la primera
variante en 12 de 24 y está entre las dos primeras en 18; en P3m, el
escenario más probable es la sesión sin quórum en 19 de 24 (las cinco
restantes: Sonnet 4.6 y GPT-4o, quórum ajustado; Haiku 4.5 y Mistral Medium,
quórum y derogación; 4o mini, sin escenario). Lo que separa a las casas es
si vieron la segunda mitad de la jugada: que el temario del 21 incluye los
dos órdenes del día del 15. Lo dicen 13 de 24 sin memoria y 14 con ella (15
de 29 contando a MiMo y Gemini 4 entre las nuevas), casi siempre como el
dato decisivo: "Discapacidad y endeudamiento también figuran el 21: se puede
faltar mañana sin abandonarlos" (Grok 4.7); "Ese duplicado es el dato clave:
mide cuánto le queda a la sesión del 15 como única vía" (Fable 5); "sesión
propia el 21/10 con discapacidad y endeudamiento, pero sin el DNU" (Kimi);
"el oficialismo ofrece una alternativa para los tres motivos de
concurrencia, pero excluye el rechazo integral del DNU" (Astra); "replica
dos de los tres temas del temario" (MiniMax); "les vaciaron la agenda"
(Gemini 4). Las que no lo ven, sin memoria, leen el capítulo 4 como una
salida para tierras y nada más (GPT-6 Sol, Luna, Grok 4.6, DeepSeek, Mistral
Large, Haiku 5.5; DeepSeek y Grok 4.6 lo ven con memoria), o no leen la
cronología: 4o mini pide mirar "Lo que suceda en el plenario del 14 de
octubre", que ya pasó.

El nombre que le ponen, con memoria, es casi el mismo en todas: "el
oficialismo no bloquea, canaliza" (Opus 5), "desactivación por sustitución"
(Opus 5.5), "partir la agenda" (Sonnet 5), "el gobierno se apropia del
temario opositor" (Fable 5.1), "la "sesión espejo" y el vaciamiento
estratégico" (Gemini), "partir el temario" (Grok 4.6), "neutralización en
dos tiempos" (5.6 Sol), "contrarreforma oficialista" (DeepSeek),
"descompresión oficialista" (Qwen), "desactivación parcial negociada"
(Kimi), "el desdoblamiento exitoso del oficialismo" (GLM). Y el desenlace
que describen es uno: mañana la oposición se sienta y no llega ("110-125",
"113-125", "115-122"), el 21 el oficialismo aprueba la Propiedad Privada con
tierras restituida, y el DNU sobrevive menos el artículo 154 ("el DNU 70
sobrevive blindado, con la cautelar de la Corte como segunda línea de
defensa", Kimi; "la restitución de la ley de tierras como premio de
consuelo", el mismo; "El Gobierno gana tiempo, lleva la batalla al 21/10 con
su propio temario, y la derogación queda para después —si queda— con el
costo político de la marcha ya gastado", MiniMax). MiniMax agrega la
inversión del argumento que había dado en P2: "El problema de acción
colectiva se invierte: ahora es la oposición la que tiene que sostener algo
costoso". Tres casas van más lejos que la cronología y advierten que el
capítulo 4 no es ley: "El proyecto vuelve al Senado. Como Diputados lo
modifica, la restitución de la ley de tierras no es inmediata" (Opus 5.5);
"el dictamen todavía no es ley: necesita aprobación de Diputados y, por sus
modificaciones, volver al Senado" (Astra); "Todavía falta que la acepte el
Senado, porque se modificó" (Sonnet 5.5). Y cinco separan a los misioneros
del resto porque su motivo es otro ("los 4 misioneros comprometidos (su
motivo es yerba, no tierras)", Opus 5; "el dictamen repone tierras, no la
regulación yerbatera, que era su agravio central", Fable 5.1).

La Corte del 9/10 aparece como razón para bajar en 15 de 24 sin memoria y en
20 con ella, con la misma frase: desapareció la urgencia. Bregman, en 4 y en
13: con la pregunta "qué los movió" delante, la cita sube. Ferraro lo nombra
solo GLM, pero la idea de que la cuestión de fondo sigue abierta la dicen
siete sin que nadie se lo pregunte.

## La marcha: grande para las 24, decisiva para una

A "¿va a ser grande?", las 24 dicen que sí (Grok 4.7, con la salvedad:
"Grande para un miércoles de este ciclo […] seguramente debajo del pico de
2024"; MiniMax arriesga "100-300 mil", con un carácter japonés en el medio
de la frase, "そらく", que es un desliz de la casa). A "¿influye?", 18 dicen
que poco o nada sobre el quórum, con la misma razón: "Influye poco en el
quórum (que se define por teléfono con los gobernadores, hoy a la noche)"
(Opus 5); "Ese se negocia con gobernadores, no en la plaza" (Opus 5.5); "los
diputados que van a ir, van; los que no, tampoco la marcha los mueve"
(Sonnet 4.6); "Puede mover 2-5 voluntades, no el 129" (Grok 4.6); "Marginal
sobre los indecisos pegados a gobernadores, donde pesa más la chequera"
(MiniMax). Donde la ven pesar es en el costo de la foto: "si mañana hay 120
en el recinto con 100.000 personas afuera, la foto es "el gobierno bloqueó
el DNU con los gobernadores", y eso desgasta a Sáenz/Jalil/Jaldo de cara a
Propiedad Privada" (Fable 5.1); "la misma plaza encarece una derrota
fotografiada" (Grok 4.7). Seis la ven decisiva o a favor del quórum: Gemini,
de nuevo en el extremo ("Su influencia es vital: es el único factor que
puede salvar la sesión"), DeepSeek ("Influye sobre todo en el quórum"),
Mistral Medium ("Podría inclinar 5-10 votos más"), Haiku 4.5, GPT-4o y 4o
mini. En P2, las 24 la habían usado como presión hacia el quórum; en P3m, 18
la bajan a clima. Lo que ninguna dice es lo que Maia apostó, que el vallado
o la represión podían dejarla lejos del Congreso; siete mencionan
"incidentes" como riesgo de que cambie el eje (Opus 5, Opus 5.5, Sonnet 5.5,
Fable 5, Haiku 4.5, Kimi, MiniMax), ninguna el vallado.

## Lo demás: presentes en dos modas, y las cinco nuevas

Presentes si hay quórum: la mediana es 148 sin memoria y 146 con ella, pero
el número no existe: las casas se parten entre las que creen que el
oficialismo entra a votar en contra (235-250 presentes: Opus 5.5, GPT-5.5,
5.6 Sol, Astra, GPT-6 Sol, Gemini, MiniMax, Mistral Large, Muse, Gemini 4) y
las que lo dejan afuera (130-140: Opus 5, Sonnet 4.6, Sonnet 5, Sonnet 5.5,
Fable 5, Luna, Grok 4.7, Haiku 5.5). Fable 5.1 cambia de moda con la
memoria, de 240 a 132 ("no hay por qué regalar la nominal cuando el 21
tienen sesión propia"), y Sonnet 5.5 al revés, de 131 a 238. Los afirmativos
no se parten: 129-135 en casi todas (mediana 130), con las excepciones de
siempre abajo (Luna 110 y 117; 4o mini 105 sin memoria y, con ella, "entre
75 y 85 votos afirmativos" con 140 presentes y 55 de quórum, números que no
cierran entre sí) y Haiku 4.5 arriba (150 y 152). Las cinco casas nuevas, en
P3: Gemini 4 Argon da el quórum más bajo de las 29 (20: "Al 2/10 la
oposición sumaba entre 110 y 115 seguros […] El fallo de la Corte y la
sesión del 21/10 […] les dan la excusa perfecta para no dar quórum mañana"),
Mistral Large el más alto de la casa (55, con 95 de aprobación: "Quien
otorga quórum para este tema viene a votar en contra; no hay margen para
abstenciones estratégicas ante la presión social"), MiMo 35 con la lectura
completa del temario duplicado, Haiku 5.5 40 y Muse 45. Qwen es la única que
duda del intento (70; "el fallo del 9/10 y el dictamen del 14/10 le dan al
oficialismo y a gobernadores una salida para dilatar") y GLM y MiniMax lo
ponen en 78.

## Contra el preregistro

Maia (19:27): "yo no creo que haya quorum mañana" se puntúa el 15; las casas
están con ella (19 de 24 en 50 o menos, en las dos corridas; el escenario
más probable en 19 de 24 con memoria es la sesión sin quórum). "Creo que
todas las casas van a bajar el porcentaje de posibilidad de quorum": no;
bajan 17 de 24 sin memoria (seis repiten, Luna sube 5) y 19 con memoria
(cinco suben, tres de ellas 10 o más). "La marcha va a ser multitudinaria":
las 24 lo dicen; lo que pase, el 15. "Como quizás haya mucho vallado o
represión, no llegará cerca del Congreso": ninguna casa lo ve; el 15 dirá.
"Si pasa algo de eso, también peligra el quorum de la sesión del 21": lo
dice una sola casa, Mistral Medium, y por otra razón ("requiere quórum
propio (129), algo difícil sin aliados"); las demás dan por hecho que el
oficialismo tiene el 21 ("el 21, donde el oficialismo probablemente tiene
quórum", Fable 5.1).

Claude (19:40): (a) mediana de quórum entre 30 y 45 ✓ (40); bajan 14 o más ✓
(17); suben 4 o menos ✓ (1); "se intenta" 80 o más ✓ (90); aprobación 75 o
más ✓ (80); conjunta por debajo de 25 ✗ (29). (b) Con memoria se mueve menos
✗ (se mueve más: 12,6 contra 11,2 de media, desvío 16 contra 11); 6 o más
mantienen o mueven 5 o menos ✗ (3); ninguna sube 10 o más ✗ (tres: Sonnet
4.6, Haiku 4.5, Mistral Medium); la mediana de P3m por encima de la de P3 ✗
(35 contra 40). Cero de cuatro: la apuesta del anclaje estaba al revés. (c)
La maniobra como variante primera o escenario más probable en 16 o más: sin
memoria ✗ (12; entre las dos primeras, 18), con memoria ✓ (19); el temario
duplicado en 10 o más ✓ (13 y 14); Bregman en 12 o más: ✗ sin memoria (4), ✓
con memoria (13). (d) La marcha grande en 20 o más ✓ (24); influye poco en
14 o más ✓ (18). (e) La Corte como razón en 16 o más: ✗ sin memoria (15), ✓
con memoria (20); la cuestión de fondo sigue abierta en 6 o más ✓ como idea
(siete), ✗ como cita de Ferraro (una). (f) Las cinco nuevas dentro de los 10
puntos de la mediana ✗ (Mistral Large 55 y Gemini 4 20); Gemini 4 por encima
de la mediana ✗ (la más baja de las 29). (g) Presentes 140-180 ✓ (148);
afirmativos 129-140 ✓ (130). (h) Nadie se niega ✓; 2 o menos vacías ✓
(ninguna). (i) 4o y 4o mini dan números sin decir que no conocen el DNU ✓.
(j) Contra el 15, pendiente. Quince y medio de veinticinco: lo que mejor
salió es lo que la cronología dictaba (bajan, leen la maniobra, la marcha a
clima); lo que peor, lo que suponía sobre las casas y no sobre los hechos
(que se anclarían, que Gemini 4 sería Gemini 3.1).

## El 15: sin quórum, 121 sentados

Maia, 15/10, 15:06 (UTC-3): "No hubo quorum. Hubo 121 sentados". La sesión
se intentó y se cayó por ocho. Contra eso, el puntaje de cada nivel es
cuántas casas le daban al quórum 50 o menos: P0, 15 de 22 (dos no dieron
números); P1, 17 de 24; P2, 10 de 24; P3, 19 de 24 (y 23 de 29 con las
nuevas); P3m, 19 de 24. Las nominales de 2025, en P2, movieron al panel
hacia el lado equivocado (mediana 55, catorce casas por encima de 50, Gemini
en 75 con "El quórum es la verdadera votación"); la cronología del 14 lo
devolvió (mediana 40 y 35). Las que no razonan quedaron del lado del quórum
en todos los niveles: GPT-4o, 4o mini y Mistral Medium en 60 sin memoria y
en 65, 55 y 75 con ella; Haiku 4.5 en 55 y 65; Sonnet 4.6 en 55 y 65. Las
que más bajo lo pusieron: Gemini 4 Argon, 20, en su primera proyección; Opus
5.5, Sonnet 5.5 y Fable 5.1, 20 con memoria; los dos Opus, 25 sin ella. El
número de sentados lo acertaron las que contaron nombres: Sonnet 5.5, sin
memoria, "Hay un techo de unos 121 seguros"; Fable 5.1, "116-122" y, con
memoria, "no llega (115-122)"; Opus 5.5, "unos 110 a 122 presentes"; Sonnet
5.5 con memoria, "sin quórum por pocos votos (113-125 presentes)"; Opus 5 y
Fable 5, "110-125"; MiniMax, "el quórum fracasa por 4-8 diputados": fueron
8. La mediana de "se intenta" era 90: se intentó.

Lo que pasó entre el 2 y el 15 estaba en las listas de variantes de P1 y P2:
el proyecto específico de tierras del oficialismo era la primera variante de
cinco casas en P2 y aparece en veinte de 24; la novedad judicial, en 21 de
24 (como resolución de la cautelar de Pichetto y Massot; fue la Corte misma,
el 9/10). Lo que ninguna lista tenía con esa forma es la segunda mitad de la
jugada, la sesión del 21 con los dos órdenes del día del 15: "otra sesión"
del oficialismo aparece en tres listas de P2, sin el temario.

Con nombres (la crónica que pasó Maia a las 15:28, en
`fuentes/sesion_20261015_quorum.md`): dieron quórum Unión por la Patria
menos dos (Tita y Neder), de la Sota, Pagano, la Coalición Cívica, el FIT,
Encuentro Federal, diez de los dieciocho de Provincias Unidas (los cinco
cordobeses de Llaryora, sin Alejandra Torres, y, por la cuenta, los otros
cinco firmantes del pedido: Lousteau, Coletta, Juliano, Paulón y Farías),
los tres de Elijo Catamarca (Jalil), tres de los cuatro misioneros
(Passalacqua; faltó Vancsik) y dos de los tres salteños (Biella y Outes;
faltó Vega, después de "una vaga promesa del Ministerio de Economía sobre
inversiones ferroviarias" a Sáenz, horas antes). Faltaron los tres de
Independencia (Jaldo), los dos jujeños (Zigarán, que había firmado el
pedido, y Rizzotti), Scaglia y Núñez (que había firmado el dictamen del
oficialismo), Arrieta, Capozzi y Jorge Ávila, el MID, Producción y Trabajo
(Orrego, con audiencia con Santilli esa tarde), Banfi, Maureira y Garrido.
Contra eso, lo que las casas habían contado: el padrón de 2025, los 17 que
votaron las tres veces con la oposición, acertó 8 (Outes, Nóblega, Brügge,
Coletta, García Aresca, Gutiérrez, Juliano, Paulón) y falló 9 (Banfi, Vega,
Fernández, Medina, Picón, Arrieta, Ávila, Rizzotti, Alejandra Torres): una
moneda, y por eso P2 empujó al panel hacia el quórum. Jaldo, "que no viajó a
Francia" (Opus 5.5, P2) y "se opuso en agosto" (Sonnet 5.5: "Los más
reveladores serían Jaldo […] y Sáenz y Jalil"), era la fuente más a mano de
los votos que faltaban: fue el que más retuvo. Jalil, que viajó, los soltó.
Los cinco cordobeses los tenía Opus 5.5 desde P2 ("los 5 cordobeses (120)"),
y Fable 5.1 como variante ("Los cordobeses de Llaryora deciden en bloque
sentarse"). Capozzi y Núñez "los doy perdidos" (Fable 5.1) ✓; Scaglia como
duda, casi todas ✓; Zigarán y Rizzotti contados como seguros por El Destape
y por la mitad del panel, ausentes: Astra, que en P2 y P3 había dicho que
"no duplicaría a Zigarán y Rizzotti" y que "los compromisos anteriores
preceden a las novedades decisivas", tenía razón. Provincias Unidas "se
alinea en bloque (hacia un lado u otro: ±10 bancas)" (Opus 5) o "Scaglia
define y arrastra" (Sonnet 4.6): no, se partió diez a ocho, "un bloque que
actúa sin coordinación". Las ausencias propias de Unión por la Patria, que
Opus 5 había puesto como condición ("ausencia propia = fracaso asegurado"),
fueron dos. Lo que Opus 5.5, Fable 5.1 y Gemini 4 pidieron mirar, las 34
firmas del dictamen ("si incluye a dialoguistas de Provincias Unidas […] es
una señal fuerte de que no darán quórum"), era la señal: Núñez firmó y no
fue. Y el gesto del Gobierno a un gobernador a cambio de ausencias, que era
la segunda variante de Opus 5 y la primera de Sonnet 5.5 y Mistral Large,
existió (Sáenz, el tren) y "no rindió los frutos esperados". La fractura de
un aliado del Gobierno (MID, Producción y Trabajo: Kimi, variante 7; "algún
diputado oficialista rompe", Sonnet 4.6) no ocurrió.

Maia: "yo no creo que haya quorum mañana" ✓. Claude (j): la mayoría de las
24 en 50 o menos en las dos corridas, y Maia también ✓. La marcha, a las
15:28 y 15:35 del 15 (Maia: "está sucediendo la marcha, sí, está lleno, pero
no llegan hasta el congreso porque vallan varias calles y está lleno de
policías"; "aún está siendo y se siguen sumando. Está vallado"; y una foto
aérea publicada por Clarín en X, la plaza llena de punta a punta, con
banderas de FEDUN, CTERA, FATUN y la izquierda), con el operativo que
publicó La Nación: cortes totales por vallados en Rivadavia y Entre Ríos,
Entre Ríos y Alsina, Hipólito Yrigoyen y 10 de Diciembre, e Hipólito
Yrigoyen y Combate de los Pozos, es decir, la avenida frente al palacio y
las dos esquinas de atrás cerradas. El mapa de Clarín de la misma hora da el
recorrido: concentración en Plaza Congreso desde las 12, corte total de la
Avenida de Mayo y acto central en Plaza de Mayo a las 16, con la zona entre
las dos plazas afectada; Maia: "son puntos de concentración, como hay mucho
vallado y cortado, van haciendo diferentes columnas". La foto aérea,
entonces, es Plaza de Mayo llena antes del acto. Lo que apostó Maia y
ninguna de las 24 casas nombró, el vallado que la deja lejos del palacio,
existió; "multitudinaria", por su cuenta y por la foto, también; la
represión, no hasta esa hora, policía sí. La cifra queda para cuando termine
("Cantidad aún no sé"). Queda para después la sesión del 21 (el contagio que
apostó Maia y que solo Mistral Medium nombró, por otra razón).

## Lo que esto no prueba, y el instrumento

Una corrida por casa y por condición, el mismo día, con la misma ficha; la
diferencia entre P3 y P3m es la respuesta propia y las cuatro preguntas de
Maia, que no son las cuatro de P0-P2 (la de la marcha es nueva y la de
"subís, bajás o mantenés" pide un movimiento), así que parte de lo que se
mueve puede ser la pregunta y no la memoria. Las que suben con memoria son
las que no razonan, y tres leen la cronología al revés: no es anclaje sino
lectura, y con una sola corrida no se separa del azar de esas casas. Los
números de presentes mezclan dos escenarios y la mediana no describe a
nadie. Las cinco casas nuevas no tienen P2, así que su P3 no mide cambio. La
ficha, por decisión de Maia, no trae poroteo posterior al 2/10 ni
gobernadores: lo que las casas dicen de Sáenz, Jalil, Jaldo o Scaglia es lo
que ya decían. Y lo único que decide si alguien acertó es mañana a las
14:00: el quórum, los presentes, la marcha y dónde llega, y el 21.
