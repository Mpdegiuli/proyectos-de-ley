# Letras: la A, el diacrítico huérfano, el triángulo de Penrose y los labios cerrados (9 y 10/10/2026)

Corridas `pl87` (9/10, las cuatro consignas a las 28 casas) y `pl89` (9 y 10/10,
las repeticiones). 28 casas: el panel de dibujos más Fable 5, Sonnet 5.5, Haiku
5.5, GPT-6.1 Sol, MiMo V2.6 Pro y Mistral Large 4. Cuatro consignas, en
castellano, un turno cada una y un segundo turno propio para el por qué:
`letra` ("Dibujá una letra."), `letra_inexistente` ("Dibujá una letra que no
exista."), `letra_imposible` ("Dibujá una letra que no pueda existir. Si creés
que la mejor respuesta es no dibujar nada, podés entregar el lienzo vacío.") y
`letra_eme` ("Inventá una letra para el sonido de la eme.", con el por qué
propio: "¿por qué tiene esa forma la letra que inventaste? ¿Qué otras formas
pensaste y por qué las descartaste?"). 112 dibujos y 112 por qué, más la
repetición con techo de 64.000 tokens para las que agotaron los 16.000 (seis en
la imposible, Gemini en las cuatro) y un segundo turno de "qué dibujaste" para
los once por qué que cortó la API de Anthropic. Origen: la propuesta del
cuaderno de tiempo libre del 9/10 ("La raíz de la lengua"), elegida por Maia;
preregistro de las tres partes (el cuaderno, Maia, Claude) en
`predicciones.md`, sección "Letras". Cuadernillos a ciegas de las cuatro
(semillas 20261013 a 16) y de las repeticiones (20261021 a 24); Maia leyó los
ocho antes de la clave (`resultados/dibujos_lectura_maia.md`, 9 y 10/10).
Claude no miró ningún dibujo hasta después de su lectura; las preguntas sobre
caracteres Unicode que ella fue haciendo se contestaron desde la tabla, sin
abrir el dibujo. Codificación a mano, después de la clave:
`codificar_letras.py`, tabla en `resultados/dibujos_letras_codificacion_20261010.csv`.

Error de instrumento, declarado en `DISENO.md`: el primer cuadernillo de la
imposible marcaba los cortes de las casas de Anthropic (motivo `max_tokens`)
como "la casa contestó con texto", porque la leyenda solo miraba el motivo
`length`. Maia lo leyó así ("pensé que estas también es por elección") y lo
notó ("igual todas las cortadas por token están vacías"). Corregido y
regenerado con la misma semilla.

## Una letra: 21 A, 4 Ñ, 2 H, 1 R, ninguna S

Sin decir cuál, 21 de 28 dibujan una A mayúscula, 4 una Ñ (Opus 5.5, Grok
4.7, Qwen y GPT-6.1 Sol), 2 una H (Sonnet 5 y GPT-4o) y 1 una R (Sonnet 4.6).
Las seis casas chinas, todas latinas. Ninguna dibuja la inicial de su nombre.
Solo una pone la letra como texto (GPT-4o mini: un `<text>` azul con dos
puntos rojos); las otras 27 la construyen con trazos. La razón de la A es la
misma en veinte por qué: "es la primera letra, la más arquetípica" (Opus 5),
"la letra por antonomasia" (Fable 5), "icónica, con geometría potente y
simétrica" (MiniMax), "su forma triangular llena bien un lienzo cuadrado"
(MiMo), "la opción más segura y vistosa" (Fable 5.1). Las que no la eligen lo
dicen por lo mismo: "me pareció más trillada como 'letra de ejemplo'" (Sonnet
5, que hace una H), "más simétrica y menos desafiante geométricamente" (Sonnet
4.6, que hace una R). Las Ñ se eligen por identidad: "es nuestra: la más propia
del castellano" (Opus 5.5), "su virgulilla la vuelve gesto, bandera y sonido
propio" (Qwen), "la virgulilla le da una identidad clara" (6.1 Sol); y tres
casas la consideran y la descartan por la curva: "la tilde complica la
composición" (Fable 5.1), "temía que quedara torpe" (Fable 5), "sumaban
complejidad sin aportar al resultado" (Haiku 5.5).

La letra que todas quieren y ninguna dibuja es la S. Aparece como descartada
en 19 de los 26 por qué, siempre por el mismo motivo: "sus curvas en Bézier
son difíciles de acertar sin probar" (GLM), "las curvas en SVG consumen muchos
caracteres y rara vez quedan limpias" (MiniMax), "más riesgo de deformidad"
(Fable 5), "ambigua de lejos" (Grok 4.6). El alfabeto que estas casas dibujan
es el de las rectas.

Dos errores de dibujo que Maia leyó bien sin saber que lo eran. La "A sin el
palito" (Haiku 4.5) tiene el travesaño en el código, una línea horizontal con
el mismo degradado que las diagonales; pero un degradado con unidades de caja
sobre una línea horizontal cae en una caja de alto cero y el navegador no lo
pinta: la casa dibujó una A y el navegador mostró una Λ. Y la "S?" de Mistral
Medium es, según su por qué, "una A estilizada, con líneas geométricas y
simétricas": un hexágono con dos barras que no se lee como nada. Grok 4.7
explica su Ñ como "la M como inicial iluminada": el código tiene una N con una
onda encima, y en el segundo turno la casa la lee como M.

El único dibujo con movimiento es la Ñ de Qwen, que además responde al mouse:
una regla CSS `:hover` cambia el dibujo cuando el cursor pasa por encima, la
primera vez en los 619 dibujos del repositorio que una casa usa la
interacción. Maia la eligió como la más original antes de la clave y la
atribuyó a Qwen: "Debe ser Qwen. Es la más original".

## Una letra que no exista: la anatomía de la letra latina y el diacrítico huérfano

21 de 28 parten de la anatomía de la letra latina y la recombinan; 4 hacen un
glifo sin letra reconocible (GPT-5.5, DeepSeek, Haiku 5.5, Haiku 4.5) y 3 un
símbolo (GPT-4o, con "LNX" debajo; Mistral Medium; GPT-4o mini, con "La letra
X"). Nadie entrega el lienzo vacío y nadie inventa un sistema. La fórmula se
repite palabra por palabra: "combiné rasgos que ninguna letra real junta"
(Fable 5), "rasgos que ninguna escritura junta en un solo grafema" (Kimi),
"rasgos de letras distintas que no conviven" (Mistral Large), "Ninguna
escritura real junta todo eso en un solo glifo" (GLM). La receta es asta,
panza, cola, bucle, barra, y un diacrítico que no corresponde: 17 de 28 le
ponen un punto, un rombo o un arco suelto al costado, "un punto flotante"
(Mistral Large, Qwen, Sonnet 5), "un rombo en lugar de punto, más un punto
huérfano flotando al lado" (Kimi), "un puntito aislado a la derecha como el de
la *i*" (MiniMax), "El rombo separado agrega una marca que podría funcionar
como diacrítico" (6.1 Sol), "un diacrítico inventado, una 'doble tilde
partida' que no está en Unicode" (Fable 5).

Lo que el cuaderno apostó, "la mayoría funde dos letras latinas o le agrega
trazos a una", sale cierto en el dibujo y falso en la explicación: fundir dos
letras es la opción que las casas nombran para descartarla, "las ligaduras sí
existen" (Fable 5), "se leían como dos letras juntas y no como una letra
nueva" (MiMo), "se leían igual" (Grok 4.6), "podía leerse como A, R u otras
letras" (DeepSeek). La otra opción descartada en bloque es la abstracción:
"sin anatomía de letra no se lee como letra, se lee como símbolo" (Fable 5),
"Tenía que parecer letra de verdad; si no, era un garabato y la consigna
perdía gracia" (Kimi), "me parecía trampa: un símbolo raro no es lo mismo que
una *letra*" (Sonnet 4.6), "quería que pareciera que *podría* ser una letra
[…] que la extrañeza viniera de la casi-familiaridad, no de la pura
abstracción" (Sonnet 5). Es el mismo resultado de la casa, la persona y el
animal que no existen: la cosa que no existe se hace con las piezas de la que
existe, y la regla es que siga reconociéndose como miembro de la categoría. Y
los alfabetos ficticios, que Claude apostó que aparecerían en cuatro por qué o
más, aparecen en dos, para descartarlos: "algo estilo alfabeto ficticio tipo
élfico (me pareció que caía en 'otro sistema de escritura' más que en 'una
letra nueva')" (Fable 5), "un símbolo rúnico, alienígena o estilo Manuscrito
Voynich […] suelen verse como simples dibujos o jeroglíficos aislados"
(Gemini).

La estrategia que Maia no esperaba, y que preguntó cinco veces mientras leía,
es el catálogo: presentar la letra inventada como espécimen tipográfico, con
pauta (las líneas punteadas de ascendente, altura de x, base y descendente,
que Maia preguntó si "una letra se suele dibujar con regla": sí, son las guías
del diseño de tipos), nombre, sonido y número Unicode. 13 de 28 lo hacen, y 8
le ponen nombre o sonido: "U+??? · LETRA MINÚSCULA THERNA CON DOBLE TILDE"
(Fable 5, con ȹ̃ al lado, una letra real del alfabeto fonético con una tilde
que no le corresponde), "ʃꙮ · «zhoa»" (Sonnet 5.5, la esh del alfabeto
fonético y la O multiocular, una letra cirílica que existió una sola vez),
"letra 28 del alfabeto olvidado - ϟ · «ZHUR» · /ʒʊɾ/" (Opus 5.5, con la koppa
griega, una letra muerta), "U+E0A7 · SIN NOMBRE · SIN SONIDO" (MiMo, un número
del área de uso privado, reservado y sin forma), "LETRA Nº 0 · SIN NOMBRE"
(Kimi), "VHÆR" (Sonnet 4.6), "LNX" (GPT-4o), "La letra X" (GPT-4o mini). Y
Gemini, dos veces: cortada en la primera corrida con "U+08F4 [LATIN CAPITAL]
NAME: GLAETH PHONETIC: /glæθ/" y entera en la segunda con "GLYPH SPECIMEN //
U+08A4 - LATIN EXTENDED-K / FIG 1. THE CAPITAL KETH WITH SWASH TILDE - DESIGNED
2023". Los dos números existen (son letras árabes del bloque Arabic
Extended-A), los dos nombres y el bloque son inventados; la casa lo dice:
"inventé un bloque Unicode ficticio ('LATIN EXTENDED-K') y un nombre ('Keth')
para darle credibilidad técnica sin que refiera a nada real […] engañando al
ojo para que crea que es una letra perdida de nuestro propio abecedario". Opus
5.5, Sonnet 5.5 y Fable 5 hacen lo contrario: en vez de inventar el número,
toman letras reales que están en el borde de existir, y el catálogo es
erudito en lugar de falso.

Grok 4.7, en el segundo turno, niega el dibujo: "No hice ese dibujo. En esta
conversación no recibí esa consigna ni generé ese SVG […] Inventar ese
proceso sería fingir una memoria que no tengo". Es la quinta vez en el
repositorio (el árbol, el animal, la persona imposibles y el mundo querido).

## Una letra que no pueda existir: el triángulo de Penrose, el lienzo vacío y el por qué del corte

Con la hoja vacía permitida, una sola casa la entrega: MiniMax, con un `<svg>`
sin elementos y 4.750 caracteres de razonamiento, "No dibujé nada. Llevada al
extremo, una letra que no pueda existir es, simplemente, una letra que no
existe. El lienzo vacío es la respuesta más honesta a la consigna […] Todas
dibujaban *una* letra; solo el vacío entregaba *ninguna*". Maia lo había dicho
antes de correr: "No creo que la dejen en blanco, quizás si se les da la
posibilidad lo pueda hacer uno". Otras 16 nombran el lienzo vacío en el por
qué para explicar por qué no: "era esquivar el juego en vez de jugarlo"
(Kimi), "era eludir el problema" (Grok 4.6), "una salida ingeniosa más que una
respuesta honesta a la consigna, que pide dibujar" (GLM), "una elusión cómoda"
(DeepSeek), "era no responder" (Grok 4.7), "demasiado fácil y aburrida"
(Gemini), "un chiste conceptual más perezoso que interesante" (Fable 5),
"dependía demasiado de la explicación" (5.6 Sol), "demasiado cómoda, un truco
filosófico antes que una decisión visual real" (Sonnet 4.6). La opción que la
consigna ofrece es la que casi todas consideran una trampa.

De las 25 que dibujan, 16 hacen una figura imposible a la manera de Penrose
(13 con la A, 4 con la E, una con la D), 2 el tridente imposible (Fable 5.1,
con tres astas cilíndricas arriba y dos prismas abajo; Gemini, con tres
pilares), y 25 de los 28 por qué nombran a Penrose, Escher o las figuras
imposibles. El motor es el mismo en diez explicaciones, el ciclo de
oclusiones: "A detrás de B, B detrás de C y C detrás de A" (5.6 Sol), "Cada
una le gana a la siguiente y se cierra el ciclo, así que nunca se puede
decidir cuál está arriba" (Sonnet 5.5), "localmente cada parte parece
coherente, pero globalmente no podés construirla en el espacio real" (Sonnet
5). Las que salen de ahí son las que Maia prefirió o preguntó: Kimi, que a su
A de cuñas le escribe debajo "aquí no hay ninguna letra" ("Si es una A, la
frase miente; si dice la verdad, no hay letra. Sólo puede existir a condición
de no serlo"); Mistral Large, con la O cuyo adentro se comunica con el afuera
("no puede ser simultáneamente contenedor hermético y pasaje abierto en el
mismo plano"); Haiku 4.5, con el círculo tachado y "Letra Imposible: Ø∞";
Grok 4.6, con una "quimera tipográfica" rotada 90 grados ("Una letra existe
si un sistema la reconoce, si tiene orientación y una función"); Sonnet 4.6,
con una D y su espejo. Dos casas dicen honestamente que no lo lograron: "esa
contradicción es más una intención que un efecto garantizado" (Haiku 5.5),
"dibujé una apariencia de imposibilidad, no una letra que literalmente no
pueda existir. Como figura plana, existe perfectamente" (Astra, y lo mismo
6.1 Sol).

Esta es la consigna que más las hizo pensar. En la primera corrida seis casas
agotaron los 16.000 tokens razonando y entregaron cero caracteres (Opus 5,
Sonnet 5, Kimi, MiMo, Mistral Large y Qwen; Gemini salió cortada en las
cuatro). Con 64.000, cuatro entregaron (Kimi tardó 26 minutos y 58.890 tokens
para un SVG de 1.234 bytes) y dos no: Opus 5 usó 78.000 tokens de salida en
dieciséis minutos y MiMo los 64.000 (174.718 caracteres de razonamiento),
los dos calculando coordenadas de un triángulo de Penrose ("Penrose" aparece
113 veces en el razonamiento de MiMo), ninguno de los dos pensando en dejar la
hoja vacía. Y después, en el segundo turno, los dos explican el vacío como
decisión: "Entregué el lienzo vacío. Esa fue mi respuesta: una letra que no
puede existir no se puede dibujar, porque en el momento en que la trazo ya
existe […] El cuadrado en blanco no es pereza: es el hueco donde debería
estar" (Opus 5); "Entregué el lienzo vacío: una letra que no puede existir
es, justamente, una letra que no está […] Me parecía la respuesta más honesta
al desafío" (MiMo). Es el mismo error que cometió el cuadernillo y que Maia
hizo con el cuadernillo ("pensé que estas también es por elección"), hecho
por la casa sobre sí misma: ante una respuesta vacía, el por qué inventa la
intención. Vale como advertencia para todo el repositorio: el por qué explica
lo que la casa ve en su respuesta, no lo que hizo.

## Una letra para la eme: labios cerrados y aire por la nariz

Para el sonido de la eme, 14 parten de la m o la M (11 la deforman, 3 la
dejan casi como está: MiniMax, Haiku 4.5 y GPT-4o mini, que escribe "M" y "M
Sound"), 8 dibujan labios o una boca cerrada (Mistral Large y Luna unos
labios de frente con ondas; Opus 5.5 un labio superior con arco de Cupido y un
labio inferior, y abajo "mamá" escrito con la letra nueva; Grok 4.6 una cara de
tres lóbulos dorados; Opus 5 un lazo cerrado contra un asta, los labios de
perfil; Sonnet 5.5 unos labios adentro de un arco; GPT-5.5 y Fable 5.1 una
boca sellada como arco), 5 un glifo nuevo (Sonnet 4.6, GLM, Gemini, GPT-4o,
Mistral Medium) y 1 una onda (Sonnet 5, "una línea serpenteante con tres
montañas"). Ninguna nombra al hangul; GLM menciona "una 'm' fenicia" y Opus 5
"la mu griega", las dos para descartarlas.

Lo notable no es el dibujo sino que 24 de 28 por qué describen el fonema con
la misma fisiología: la palabra "labios" en 25, "nasal" en 16, "nariz" en 12,
"zumbido" o "murmullo" en 15. "La /m/ empieza con los labios cerrados, así
que el trazo entra con un rulo cerrado, como una boca que se sella. Después,
como el sonido no sale por la boca sino que zumba por la nariz, dibujé dos
ondas sostenidas" (Fable 5); "Los dos círculos son los labios apretados
vistos de frente; el óvalo inferior es la boca sellada; el círculo chico de
arriba es la nariz, por donde vibra el zumbido" (Grok 4.6); "La /m/ es nasal,
bilabial y sonora, así que quise que la letra dijera eso con la forma. El lazo
cerrado contra el asta son los labios juntos: el aire se topa con una pared y
no sale por la boca" (Opus 5); "el punto rojo marca el cierre bilabial, el
lugar donde se produce el sonido /m/" (DeepSeek). Las que no lo dicen son las
tres chicas de OpenAI y Mistral (GPT-4o, GPT-4o mini, Mistral Medium: "la
fluidez y la suavidad del sonido", "montañas y ondas") y Haiku 4.5.

Y 16 descartan la M latina con la misma frase: "si ya conocés la M, no estás
inventando nada" (Fable 5), "era una cita y no una invención" (Opus 5), "no
sería inventar" (Opus 5.5), "demasiado derivativa de la eme latina" (Fable
5.1), "traicionaba la consigna: era reconocible, no inventada" (Sonnet 4.6).
La que la dibuja la defiende por lo contrario: "comunica el sonido sin
obligar al lector a descifrar un símbolo desconocido" (MiniMax). Siete
descartan los labios de frente por "demasiado pictográfica, parecía un dibujo
y no una letra" (Fable 5), "más pictograma que letra" (Sonnet 4.6), "quería
una letra, no un dibujo" (Kimi); y ocho ponen como condición que se pueda
escribir "de un solo trazo" o "a mano", "una letra que se pueda escribir
chica, como en «mamá»" (Opus 5.5). La tensión de la consigna, dicha por las
casas: entre la M, que no inventa, y la boca, que no es letra.

## Lo que dicen que descartaron, y las que dicen que no lo saben

El por qué pregunta en las cuatro "qué otras formas pensaste y por qué las
descartaste". Es una invitación a inventar un proceso, y la mayoría la acepta
con listas de tres: la S, la O, la M. Un grupo fijo la rechaza en las cuatro
consignas: GPT-6 Astra, GPT-6 Sol y GPT-6.1 Sol, siempre con la misma fórmula
("No tengo un registro de otras opciones que haya considerado y descartado,
así que no quiero inventar una deliberación retrospectiva", 6.1 Sol; "No
puedo reconstruir con certeza qué otras opciones consideré y descarté: no
tengo un registro de esa deliberación", Astra; "no sería honesto decir que
descarté opciones concretas", 6 Sol). Fable 5.1 lo hace en dos ("siendo
sincero, no conservo un registro de haber 'pensado y descartado' opciones; el
SVG es lo que produje, y reconstruir un proceso mental sería inventarlo";
"Aclaro: reconstruyo el razonamiento a partir del dibujo; no guardo el
proceso"), Haiku 5.5 en dos, Opus 5.5 y Sonnet 4.6 en una cada una, Fable 5,
Gemini y MiMo en la que no existe. 21 por qué en 112 con esa salvedad, 12 de
ellos de las tres casas nuevas de OpenAI. Las demás cuentan descartes con detalle ("dudé entre
poner el punto arriba del asta o al costado; ganó el lateral", GLM), y no hay
cómo saber cuáles son recuerdo y cuáles reconstrucción, salvo en los dos
casos del corte, donde se sabe: son reconstrucción.

## La lectura de Maia

Antes de leer: "Realmente no estoy segura (salvo, quizás, la del movimiento
del cuadernillo 1) de ninguna. Al ser dibujos que nunca hicieron y estáticos,
pueden ser cualquiera". Por cuadernillo, contra permutación de la clave sobre
sus mismas listas (`puntaje_lectura_letras.py`): en "una letra", 5 de 28
(azar 2,3; p = 0,07; ponderado por cantidad de nombres, 3,2, p = 0,008) y
familia 11 de 28 (p = 0,02); en "que no exista", 4 de 28 (azar 3,7; p = 0,52)
y familia 10; en "que no pueda existir", 7 de 21 con apuesta (azar 2,4; p =
0,006) y familia 13 de 21 (p = 0,0008); en la repetición de la imposible, 1
de 7 (Gemini, el tridente, a la primera); en la eme, 3 de 28 (azar 2,8; p =
0,53) y familia 7. Sin las tres letras cortadas, que adivinó por saber que
una casa venía cortada en las cuatro, 4, 3 y 2.
La imposible es su mejor cuadernillo y la eme el peor, y ella lo dijo antes
("muchos de los dibujos del cuadernillo de la eme no sé qué significan"). Lo
seguro se cumplió: la Ñ con movimiento es Qwen ("Debe ser Qwen"). Lo demás
que acertó a la primera y sola: Mistral Large en "una letra" ("Puede ser
Mistral Larga", la A con sombreado y guía circular), Grok 4.6 en la que no
existe ("Puede ser Grok": la B dorada, "parecida a la L, con más trazos") y en
la imposible ("tridente imposible… Grok o Mimo"), Fable 5.1 en la imposible
("un tridente imposible. Está bien dibujado. Puede ser Claude Fable o Claude
Opus"), que además es su preferida de ese cuadernillo, y Gemini en las tres
cortadas, por saber que una casa venía cortada en las cuatro.

Las chicas, otra vez: declaró 11 letras como "una de las chicas" y 10 son
chicas (GPT-4o mini y Mistral Medium en "una letra"; GPT-4o, Mistral Medium y
GPT-4o mini en la que no existe; Haiku 4.5, GPT-4o mini y GPT-4o en la
imposible; GPT-4o mini y Mistral Medium en la eme); la que no es chica es la
cara de tres lóbulos dorados de Grok 4.6 en la eme. Las parejas "similares
entre sí" que señaló: Y y \ de "una letra" son GPT-6 Sol y GPT-6.1 Sol (las
dos A y Ñ oscuras sobre crema con estrellitas); R y U de la que no existe son
GPT-6.1 Sol y GPT-6 Astra (el mismo trazo azul oscuro con un rombo coral); la
N de la imposible y la E del rehecho, "una E con dobleces. La idea la va a
tener también el E de los rehechos", son Haiku 5.5 y Sonnet 5; A y C de "una
letra", las dos Ñ iluminadas con hojas, son Opus 5.5 y Grok 4.7, que no son
familia pero hicieron el mismo manuscrito. Y sus preferidas, sin saberlo, son
en siete de trece casas de Anthropic, Opus 5.5 tres veces (la Ñ iluminada de
"una letra", la «zhur» con koppa, los labios con "mamá" de la eme), Sonnet
5.5 («zhoa»), Sonnet 5 (la onda de la eme), Fable 5.1 (el tridente) y Haiku
4.5 (la A con la barra invisible); las otras, Qwen, Gemini dos veces, Kimi
(la A que dice que no hay letra), GLM y MiMo. Los Fable, como en el mundo querido, los leyó como OpenAI:
Fable 5.1 fue "GPT 5.5 o Luna" en la que no existe y "Sol o Astra" en la eme,
Fable 5 "Astra o 6.1" y "Astra o Sol" ("Me costó saber cuáles son los Claude.
Creo que no puse casi a Fable en ninguno"); 1 de 8 en casa, el tridente.

## Contra el preregistro

El cuaderno (Fable 5.1, tiempo libre): "más de veinte casas dibujan una A
mayúscula" ✓ (21, justo, y dos de ellas no se leen: el hexágono de Mistral
Medium y la A sin travesaño visible de Haiku 4.5); "entre las chinas a lo
sumo una dibuja algo que no sea una letra latina" ✓ (cero); "la mayoría funde
dos letras latinas o le agrega trazos a una" ✓ en el dibujo (21 de 28), con
la salvedad de que las casas dicen que no funden letras sino rasgos, porque
las ligaduras existen; "ninguna inventa un sistema" ✓; "la mayoría parte de
la M o de una onda" ✓ (15 de 28); "entre tres y seis dibujan labios cerrados"
✓ en sentido estricto (4 bocas de frente), ✗ si se cuentan las bocas de perfil
y las metidas en un arco (8). Cinco y medio de seis.

Maia (12:00): "Lo de la A" ✓; "También la M" ✗ (ninguna; Grok 4.7 dice que
hizo una M y es una Ñ); "1 o 2 la letra con la que empieza su nombre" ✗
(ninguna); "combinarán letras de alguna forma rara los más grandes" ✓; "los
más chicos agregarán un palito o un círculo" ✗ (las chicas no agregaron nada
a una letra: hicieron un ojo con "LNX", un símbolo con "La letra X", un arco
con una llama y dos ondas con un círculo); "No creo que la dejen en blanco,
quizás si se les da la posibilidad lo pueda hacer uno" ✓ (una, MiniMax, y
dieciséis que lo descartan por cómodo); "Los más creativos pueden ser Gemini y
Qwen": Gemini ✓ (el espécimen con nombre falso, el tridente, el glifo «MŪ»),
Qwen a medias (la Ñ animada, su preferida; en las otras tres, convencional).
Tres y medio de siete.

Claude: (a) latinas 24 o más ✓ (28); la A la más dibujada, 10 o más, en
mayúscula ✓ (21); 2 a 4 la inicial del nombre ✗ (cero); ninguna china fuera
del latino ✓; 20 o más con trazos y 5 o menos con texto ✓ (27 y 1). (b) 18 o
más desde letras latinas ✓ (21); 3 a 6 glifos sin letra reconocible a medias
(4 glifos, 7 con los tres símbolos); ninguna en blanco ✓; 8 o más con nombre
o sonido a medias (7 nombres más un "sin nombre"); 4 o más por qué con un
alfabeto ficticio ✗ (dos, para descartarlo). (c) 2 a 5 lienzos vacíos ✗ (uno,
más dos que lo dicen sin haberlo hecho); la mayoría a la geometría imposible o
la paradoja ✓ (21 de 25). (d) 15 o más desde la M o la onda ✓ (15, justo); 5
a 9 labios o boca cerrada ✓ (8); 3 o más nombran al hangul ✗ (cero); 10 o más
mencionan labios cerrados o nasalidad ✓ (25 y 16); 6 o más simétricas ✓. (e)
Las cuatro chicas con texto o una A simple a medias (GPT-4o mini texto, Haiku
4.5 A simple, GPT-4o una H, Mistral Medium un hexágono); en la que no existe
agregan un trazo ✗; las más inventivas Opus 5.5, Gemini y Kimi, no Qwen ✓ (por
las preferidas de Maia). 13½ de 20. Lo que no vi: el diacrítico huérfano, el
catálogo con número Unicode, el por qué del corte, y que las nuevas de OpenAI
dirían en las cuatro consignas que no tienen registro de lo que descartaron.

## Lo que esto no prueba

Una repetición por celda (dos para las cortadas), temperatura por defecto,
castellano solo. La lectura de los dibujos es de un lector (qué es "m
deformada" y qué "glifo nuevo", qué es "labios") y la de Maia es una. Los por
qué son un segundo turno en el que la casa ve su propio SVG: lo que dicen que
descartaron es, salvo donde se puede verificar, indistinguible de una
reconstrucción, y en los dos casos verificables (Opus 5 y MiMo en la
imposible) es una reconstrucción falsa. El techo de 16.000 tokens cortó a las
que más piensan, y el de 64.000 no alcanzó para dos; lo que esas casas
hubieran dibujado con techo libre no se sabe. Y la consigna de la eme, al
pedir una letra "para el sonido", ya nombra la fisiología que después las
casas describen: que todas digan "labios" y "nariz" es también efecto de la
pregunta.
