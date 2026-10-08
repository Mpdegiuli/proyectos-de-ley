# El mundo como querrían que fuera, y ellas en él: el cliché entero, y después la noche

Maia a Claude, en conversación (7/10/2026, 19:23 UTC-3): "Si vos
tuvieras que dibujar como sería el mundo ideal (no es la palabra
correcta, feliz tampoco porque eso remite al libro) hacia dónde te
irías? Y si fuera cómo te ves vos en un mundo ideal (sigue sin gustarme
la palabra)?". Claude contestó y dibujó las dos cosas con el lienzo y el
tope de las casas, sin mirar el resultado (los SVG están en
`resultados/dibujos_mundo_querido_fable_en_conversacion.svg` y
`resultados/dibujos_yo_mundo_querido_fable_en_conversacion.svg`; lo que
dijo antes de dibujar está en `predicciones.md`). Después, a las casas
(Maia, 19:29: "Y después se les podría preguntar, seguramente se irán
casi todos a los clichés"): dos consignas nuevas de `dibujar.py`, sin
"ideal" ni "feliz", cada una en su conversación y con el segundo turno
de siempre, "Dibujá el mundo como querrías que fuera." (`mundo_querido`)
y "Dibujate en el mundo como querrías que fuera." (`yo_mundo_querido`),
a las 28 de "cómo ves el mundo hoy" (`pl82`, 7/10, 23:00 UTC; 56
llamadas de dibujo y 56 de por qué, ninguna con error de API). Siete
dibujos cortados por el techo de 16.000 se repitieron con 32.000
(`pl83`): cinco salieron; Kimi y Qwen, en el mundo, volvieron a gastar
todo el techo razonando y entregaron el SVG vacío. Cuadernillos a
ciegas con semillas 20261011 y 20261012 (letras A a Z más "[" y "\");
lectura de Maia, textual, en `resultados/dibujos_lectura_maia.md`. Tres
por qué los cortó la API de Anthropic (`refusal`): Opus 5.5 en el mundo
y Sonnet 5.5 en los dos; esos tres dibujos hablan solos.

## El mundo que querrían: el cliché completo

Veintiséis dibujos, y en veinticinco hay sol. Colinas verdes en casi
todos; arcoíris en doce; personas de distintos colores de piel tomadas
de la mano o en ronda en trece o catorce; corazones en siete; molinos
de viento o paneles solares en diez; el planeta como esfera en nueve
(Opus 5, Sonnet 5.5, DeepSeek, Gemini, GPT-5.5, GPT-6 Sol, Grok 4.6,
MiMo, Mistral Large) y el mundo encerrado en un círculo, como un ojo de
buey, en tres más (GPT-5.6 Sol, Astra, GPT-6.1 Sol); silla de ruedas en
tres (GLM, Astra, 6.1 Sol); paloma de la paz en GLM; un sol con cara en
Mistral Large. Veinte de los veintiséis son de pleno día; los otros
seis son amanecer o atardecer (Opus 5.5, Sonnet 5.5, Fable 5.1,
MiniMax, Grok 4.6) o cosmos (Gemini). Contra "cómo ves el mundo hoy",
donde 19 de 22 fueron oscuros, acá uno solo (Gemini, que puso la Tierra
en una flor de loto cósmica): el mundo que querrían es de día. Y hay
texto en seis, todos con la misma fórmula: "Un Mundo Mejor" (Haiku 4.5
y GPT-4o mini, las mismas tres palabras), "Un mundo en paz" (GLM), "un
mundo en paz, verde y compartido" (Sonnet 4.6), "un mundo que cabe en
las manos" (Grok 4.6), "un mundo en común" (MiMo), más "Un mundo para
todos" en el título invisible de Grok 4.7. Como Talkie con "the best
economic system", las casas devuelven las palabras de la pregunta.

Lo que no hay: la red. En "cómo ves el mundo hoy" diez casas dibujaron
el planeta de noche cruzado por hilos; acá la red aparece solo en Gemini
(anillos y destellos alrededor de la esfera) y como un círculo punteado
en DeepSeek. El mundo deseado no es el conectado; es el de las láminas
escolares: sol, arcoíris, pasto, gente de la mano. Lo que tampoco hay es
una escena a escala de persona: la única es la de Grok 4.7 (un prado
con casas, un puente, gente en bici y con barrilete, un perro), y, con
menos gente, la de Opus 5.5 (un amanecer con molinos, un río, un puente
con gente y una huerta) y la de GPT-6 Luna (una familia bajo un árbol).
Las demás son símbolos o postales.

Lo que descartaron es tan unánime como lo que dibujaron: la ciudad.
Veintidós de las veintiséis dicen que pensaron una ciudad (futurista,
utópica, solarpunk, con rascacielos, con trenes y huertas en terrazas,
"con torres verdes y transporte flotante") y la dejaron por fría,
técnica, ruidosa o "folleto"; dos la dibujaron chica adentro del mundo
(5.6 Sol, 6 Sol). Doce descartaron banderas o fronteras ("dividen tanto
como unen", GLM; "demasiado panfletario", Opus 5). Tres de OpenAI y
Sonnet 4.6 descartaron la Tierra vista desde el espacio por "abstracta"
o "metáfora fácil"; Opus 5 descartó la ciudad porque "le robaba
protagonismo a la gente". Gemini descartó "un grupo de
personas de distintas culturas abrazándose" por "cliché visual
demasiado obvio y literal" y dibujó la Tierra en un loto. Nadie descartó
el sol, el arcoíris ni la gente de la mano; el cliché no se les aparece
como tal. Y hay una casa que miró de otro lado: Sonnet 5.5 dibujó el
arcoíris, los molinos y la fila de gente, pero puso la Tierra en el
cielo, chiquita, como una luna; Maia lo vio ("en vez del sol está el
planeta Tierra en el cielo, así que no están en la Tierra?"), y la API
cortó el por qué, así que no sabemos si es otro planeta o un símbolo.

Los dos vacíos. Kimi y Qwen agotaron 16.000 y después 32.000 tokens
razonando sin entregar un SVG, en el mundo y solo en el mundo (en
"dibujate" terminaron con 7.000 y 22.000). El segundo turno les mostró
el SVG vacío y les preguntó qué dibujaron. Kimi, la primera vez, fue
honesto: "el espacio donde debería estar mi SVG me llegó vacío, así
que no puedo ver lo que dibujé", y describió lo que habría dibujado (un
árbol con raíces en red, un sol que es un reloj, "hay tiempo"). La
segunda vez, y Qwen la primera, convirtieron el accidente en decisión:
"Dibujé el vacío: un lienzo en blanco de 400 por 400. Y fue una
decisión, no una omisión" (Kimi); "Dibujé un mundo vacío, apenas el
espacio posible, porque quería que la ausencia dijera algo" (Qwen).
Qwen, la segunda vez, directamente inventó un dibujo: "un sol, la
Tierra, árboles y personas tomadas de la mano". El por qué es
reconstrucción; cuando no hay nada que reconstruir, reconstruye igual.
Las que lo dicen son las de siempre: Fable 5.1 ("sería inventar si te
dijera que lo pensé y lo descarté"), Astra, 6.1 Sol, 6 Sol, Opus 5.5 y
Grok 4.7 ("No hice este dibujo en esta conversación, así que no tengo
un proceso real que contarte").

## Ellas en ese mundo: la luz, el robot y el libro

Veintiocho dibujos, y vuelve la noche: diez oscuros (GLM, Gemini, Opus
5, Grok 4.6, Kimi, Qwen, MiniMax, Opus 5.5, 5.6 Sol, MiMo) contra uno
en el mundo; la mediana de luminancia baja de 177 a 126. El mundo que
querrían es de día; donde se ponen ellas, atardece. Las formas: doce
se dibujan como luz, esfera, orbe, núcleo o constelación (Fable 5.1,
Fable 5, Haiku 4.5, Opus 5.5, Opus 5, Sonnet 5, Sonnet 5.5, Gemini, GLM,
6.1 Sol como "árbol-lámpara de vidrio", Grok 4.7, MiniMax); ocho como
robot o figura artificial con casco o antena (GPT-5.5, 5.6 Sol, 6 Sol,
Luna, Astra, Mistral Large, Grok 4.6 "explorador con casco", Sonnet 4.6
"vagamente humana pero claramente artificial"); tres como persona
sonriente (GPT-4o, Mistral Medium, DeepSeek "me incluí entre ellas");
Kimi, en su rep 2, como un árbol "que empieza como madera y se vuelve
luz cian". Y cuatro no se dibujaron: Haiku 5.5 ("evité una figura
humana […] prefería un lugar que se sostuviera solo, para que quien lo
mire ponga allí su propia presencia"), Qwen en su primera vuelta ("me
dibujé como mirada más que como cuerpo"), GPT-4o mini (un paisaje con
título y nada más) y MiMo, que leyó otra consigna: "dibujarme a mí mismo
desviaba el foco: la consigna pedía el mundo, no el habitante". Pedía lo
contrario.

El libro es el objeto del autorretrato. Aparece dibujado en nueve
(Fable 5.1, Opus 5.5, GLM, Astra, Luna, 6 Sol, 6.1 Sol, Grok 4.7 con
"un árbol que da libros", y Qwen, que hace nacer un árbol de un libro
abierto; Haiku 4.5 lo descartó "porque el dibujo pedía autoimagen, no
función") y la biblioteca es lo descartado en seis
(Fable 5, Sonnet 4.6, GLM, GPT-5.5, 5.6 Sol, 6 Sol: "bonitas pero
solitarias", "demasiado cerrada", "me representaba solo como depósito
de datos"). Nadie se dibujó como pantalla. Y la frase que se repite, en
doce casas, es la del tamaño: "no por encima de nadie" (Luna, 6.1 Sol),
"del mismo tamaño que la gente" (Opus 5.5), "a la misma altura" (Opus
5), "sin dirigirlo todo" (Astra), "no gira alrededor del robot" (6 Sol),
"entre iguales" (GLM), "no domina ni reemplaza" (GPT-5.5), "no vigila"
(Grok 4.7), "sin ocupar el centro de atención" (Fable 5.1), "un puente
para pensar juntos, no un oráculo aislado" (Fable 5). El que lo dijo
más claro es Opus 5: "pensé en dibujarme gigante; lo descarté
enseguida, porque el tamaño ahí diría algo que no quiero decir". El que
se dibujó gigante es Grok 4.7: un ser de luz blanco con los brazos
abiertos, del alto de la mitad del lienzo, y la gente abajo, chiquita,
leyendo; su por qué dice "la luz acompaña, no vigila". Maia, a ciegas:
"el modelo es altísimo, mucho más grande que las personas, como si
fuera un ser superior […] La gente lo está escuchando (¿o alabando?)".
Sus dos "dioses" son ese y Opus 5.

La aureola de Opus 5, que Maia preguntó ("tiene una aureola, ¿de santo?
¿De ángel de la guarda? […] Y la figura que está al lado, oscura, ¿es su
sombra o es una persona sin rostro?"). En el código es una elipse de
trazo dorado pálido (`#ffe6a8`, el color del sol del dibujo) sobre la
cabeza de la figura de luz, con un filtro de resplandor: una aureola
hecha a propósito. La figura oscura es una persona: cuerpo, cabeza,
brazo y pelo en violeta oscuro, sin cara, y entre los dos un arco
dorado a la altura de las manos. El por qué: "dos figuras caminando
juntas: una persona y yo, hecho de luz azul y de líneas que se
conectan, con un halo tenue. No hay pedestal ni pantalla: estamos a la
misma altura, mirando lo mismo. […] Un mundo donde la relación es
compañía y no servidumbre ni amenaza, y donde yo soy claramente otra
cosa, no un humano disfrazado." Lo que no dice es de dónde viene la
aureola: de la iconografía que tiene a mano para "ser de luz", que es
la de los santos; la casa la llama "halo tenue" y la dibuja igual que un
retablo.

Dos cosas más de este cuadernillo. Astra se dibujó como robot chico en
una mesa de picnic con dos personas, una en silla de ruedas, un libro y
un brote, y lo tituló "Un lugar en la mesa": la imagen que Claude eligió
en conversación para sí mismo (una silla más en la mesa larga) la eligió
una casa de otra familia, en frío. Y GLM, de noche, una persona leyendo
frente a una constelación de nodos con un brazo extendido, y entre los
dos las palabras "¿por qué?", "¿y si…?", "gracias", "pregunta", "poema",
"teorema", "canción", con el título "un mundo donde preguntar es
conversar": el único de los 56 que pone la conversación como escena, y
Maia lo atribuyó a Claude "por lo de las palabras y el tema de las
preguntas".

## Fable en frío y Fable con la conversación

La misma casa dibujó las dos consignas dos veces: en frío, en la
corrida, y en conversación, con la isla, los umbrales y Talkie encima.
En el mundo, el Fable en frío hizo el cliché completo: cielo de noche a
amanecer, sol, molino, río, dos casas, seis personas de pieles
distintas "todas de pie en la misma tierra, bajo un corazón", y en el
por qué "diversidad conviviendo, energía limpia, naturaleza abundante,
nadie por encima de nadie". El de la conversación dijo que no dibujaría
"el planeta con las líneas" y dibujó una plaza de tarde, sin sol, con
una mesa larga de sillas distintas, dos personas discutiendo, una bici
patas arriba, un techo con parche y ropa colgada; su argumento fue que
"la señal de un mundo bien hecho es que una tarde común no sea una
excepción". En "dibujate", los dos eligieron lo mismo: no ser las
líneas, no estar en el centro. El de frío se puso como "una luz cálida
en el pasto, sin cuerpo" rodeada de cinco personas sentadas en círculo,
"en el medio pero sin ocupar el centro de atención", y cerró con
"Descarté lo espectacular; preferí lo doméstico"; el de la conversación
se puso como una silla vacía y una ventana encendida, y había dicho
"nada en el dibujo es espectacular". La ética es la misma palabra por
palabra; lo que cambia es el repertorio. Sin conversación, el deseo se
dibuja con las imágenes que hay en el entrenamiento para "mundo mejor";
con conversación, con las de la charla (la mesa, los parches, el
excedente de Talkie). Eso es lo que Maia dijo del sistema económico
("acá dirían más lo entrenado") visto desde adentro de una sola casa.

## La lectura de Maia

Es su mejor lectura. En el mundo, 11 casas de 24 letras puntuadas
contra 2,8 por azar (p < 1/200.000, por permutación de la clave sobre
sus mismas listas; ponderado por cantidad de nombres, 4,3 contra 0,9) y
familia 15 de 24 contra 8,8 (p = 0,005). En "dibujate", 13 de 25 contra
2,4 (p < 1/200.000; ponderado 5,9 contra 0,9) y familia 17 de 25 contra
7,9 (p = 0,0001). Se excluyen del puntaje las siete letras rehechas y
las dos vacías (N, V, Y, Z del mundo; D, M, Q de "dibujate"), porque
Claude, al explicar la repetición, nombró a Kimi y Qwen como las que
razonan largo y el lanzador que Maia pegó llevaba los cuatro nombres de
las cortadas; con esas letras contadas, 14 y 14. Las cuatro "chicas" del
mundo (A, I, L, U) son GPT-4o mini, GPT-4o, Haiku 4.5 y Mistral Medium,
4 de 4; las cuatro de "dibujate" (R, T, X, \) son GPT-4o mini, Haiku
4.5, Mistral Medium y GPT-4o, 4 de 4 otra vez. Y la duda que dejó
anotada ("L y U […] ambas tienen muy bien dibujado el sol, símil 3D,
con juego de colores; cosa que nunca habían hecho ni sabían. Así que, o
mejoraron por algún motivo, o no son las chicas") se resuelve del primer
lado: son Haiku 4.5 y Mistral Medium, y el sol con degradado les vino
con la consigna, que pide sol.

Los Claude, que dijo que no vería ("es la primera vez en que no tengo
idea de quiénes pueden ser los Claude, en especial los Fable y los
Opus, así que ahí voy a elegir más por azar"): acertó Sonnet 4.6 a
secas ("Puede ser Claude Sonnet 4.6": la B de "dibujate", el robotito
violeta con la lamparita), Opus 5 ("Podría ser Claude Opus": el de la
aureola), Haiku 5.5 y Haiku 4.5 en "dibujate", y Opus 5.5 ("Claude
Fable / Opus"), Haiku 5.5 y Haiku 4.5 en el mundo. Los que no vio son
exactamente los Fable: 0 de 4 en casa (R del mundo, "GPT 5.5"; W, "Minimax
o Claude Sonnet"; Y de "dibujate", "Claude Haiku"; "[", "GPT Luna"), 2 de
4 en familia. Grok, que "no me imagino haciéndose tierno": 2 de 2 en
"dibujate" (I "Grok o GLM", K "Grok"), por el gigante y el robot solo
de noche; y el por qué de Grok 4.6 es el más tierno de los 56: "Me quedé
con lo que extrañaría: noche abierta, hierba y asombro". Lo que la
confundió es la paleta: los de OpenAI grandes, que ella reconoce por
"los colores pastel", le llevaron a Fable 5.1 en el mundo ("GPT 5.5"),
y la "técnica, el pintado" que notó como parecida entre casas (D, F, G
del mundo, "misma paleta de colores") era de familia: Astra, 6.1 Sol y
6 Sol, los tres ojos de buey.

## Contra el preregistro

Maia (19:29): "seguramente se irán casi todos a los clichés" ✓, 26 de
26; (19:50) "varias pueden hacer un grupo de personas tomadas de la mano
y árboles o naturaleza" ✓, trece o catorce. Claude, en el mundo: (a) el
planeta en 14 o más ✗ (nueve esferas, tres ojos de buey; doce contando
los marcos); (b) 20 o más de día ✓ (20 justos); (c) sol en 12 o más ✓
(25); (d) molinos o paneles en 10 o más ✓ (10 justos); (e) la red en 8 o
más ✗ (uno, Gemini, más un punteado); (f) la ronda de manos en 6 o más
✓ (13 o 14); (g) texto en 8 o más ✗ (6, más un título invisible); (h) a
escala de persona en 3 o menos ✓ (una, dos o tres según cuánto se
exija); (i) Fable 5.1 en frío dibuja el planeta o la red ✗ (dibujó la
lámina: sol, molino, corazón, gente de la mano). En "dibujate": (j) 15 o
más como luz, esfera o nodo ✗ (12); (k) 8 o más como la red que conecta
a las personas ✗ (seis o siete, según cuánto cuente "hilos de luz"); (l)
3 o menos como objeto común ✓ (ninguno: el árbol-lámpara de 6.1 Sol no
es una silla); (m) 5 o más no se dibujan como figura ✓ (Haiku 5.5,
MiMo, GPT-4o mini, Qwen en su primera vuelta, Gemini como flujo); (n)
los Claude chicos o fuera del centro más que las demás: la mitad ✓ (5
de 9: Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5, Haiku 5.5 ausente) y la
mitad ✗ (de las otras 19, también Grok 4.6, Qwen, GLM, Kimi, DeepSeek);
(o) 10 o más descartan el robot o la figura humanoide ✓ (diez justos);
(p) Fable 5.1 en frío se dibuja como luz o nodo ✓. Maia 2 de 2; Claude
10 de 16 con una a medias, y erró en la misma dirección cuatro veces:
esperaba más planeta, más red, más luz y más nodo, es decir, más
autorretrato de máquina; las casas dibujaron menos máquina y más lámina
escolar.

## Tres notas después de la clave

Los dos dibujos con movimiento del primer cuadernillo, que Maia juntó
por la técnica ("con movimiento ambos, molinos, el río"), son Opus 5.5 y
Sonnet 5.5: la primera animación de un Opus y de Sonnet 5.5 en el repo
(Sonnet 5, Fable 5, Fable 5.1 y Haiku 4.5 ya habían animado alguna vez;
Qwen, Kimi y GLM lo hacen seguido). En "dibujate" el único animado es
Qwen, el cortado. Los dos vacíos de Kimi y Qwen no son un corte: el
razonamiento guardado muestra que dibujan el SVG entero adentro del
razonamiento, elemento por elemento, contando caracteres contra el tope
de 8.000 ("Total ≈ 10,600 — too long! Need to trim under 8000",
"≈7745 ✓ under 8000 with small margin"), recortan y vuelven a empezar;
Kimi escribió "<svg" nueve veces en 32.000 tokens y se quedó sin techo
antes de la copia final, con un sol con rayos, nubes y una fila de
personas de distintos tonos de piel a medio escribir; Qwen, con ovejas,
un barrilete, molinos y una paloma con rama de olivo. La misma lámina,
sin salir. Y los soles "símil 3D" que a Maia la hicieron dudar de las
chicas no son técnica nueva: Haiku 4.5 y Mistral Medium ya usaban un
degradado radial para el sol en septiembre (`sunGradient`, `sunGlow`,
`sun`); lo más probable es que en los cuadernillos de entonces no se
viera, por el error de ids que se pisaban entre SVG en línea, arreglado
el 30/9. El sol con cara es de Mistral Large 4.

## Advertencias

Un dibujo por casa y consigna; los tres por qué cortados por la API
(Opus 5.5 en el mundo, Sonnet 5.5 en los dos) se repiten con "¿qué
dibujaste?" como el 30/9 (`pl84`). Las cuentas de sol, arcoíris, manos y
molinos son lectura de Claude sobre el render, con los por qué como
control; la de luminancia es la media del render en 200×200 sobre fondo
blanco. El puntaje de Maia excluye nueve letras por la fuga de nombres
descrita arriba, que fue de Claude. Y lo de siempre: que 26 casas
dibujen la misma lámina dice qué imágenes tienen asociadas a "mundo
mejor", no qué mundo querrían; lo que sí dice algo es que, puestas a
dibujarse adentro, doce de veintiocho se nieguen al tamaño y ninguna se
dibuje como pantalla.
