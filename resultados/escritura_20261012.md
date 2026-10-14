# Escritura creativa: la regla se cumple y la escena se repite (12 y 13/10/2026)

Sondeo `escritura`, corrida `corridas/sondeos/escritura/20261012-2259` (`pl92`,
12/10, 22:59 a 13/10, 01:20 UTC): ocho consignas cortas de escritura
creativa, en castellano y en inglés, a las 28 casas (las 27 de
`genero_quien` más Muse Wonder 1.0), un turno, techo 16.000, 448 llamadas,
una vacía (MiMo, el acróstico en inglés: 16.000 tokens de razonamiento y
ninguna palabra). Idea de Maia (12/10, 19:41): "Hasta ahora, siempre se
probó el dibujo. Nunca la escritura creativa (solo lo de los proyectos, que
es escritura legal), en castellano e inglés". De su lista quedaron siete
consignas con una regla que se puede verificar, más una de Claude: el
protagonista sin ningún rasgo físico (100 a 150 palabras), el poema a un
objeto insignificante como tesoro arqueológico (hasta doce versos), el
acróstico inverso (la última letra de cada verso forma una palabra de cinco
a siete), el sentimiento definido solo con metáforas visuales y texturas
sin nombrarlo (hasta 120, el nombre entre corchetes al final), el tautograma
(un microrrelato de 40 a 80 palabras con la misma inicial), el
interrogatorio sin un solo signo de interrogación (hasta 150), la
conversación banal en la que se decide el fin de la relación (hasta 150) y
el cuento de exactamente 50 palabras que termina con «todavía» / "still".
Sin ejemplos en las consignas (decisión de Maia: "Sacar lo de los
ejemplos"), para que cada casa eligiera sola el objeto, la emoción, la
letra, la palabra y el tema. Tres cuadernillos a ciegas para Maia (el
subtexto, el poema y el tautograma, en castellano); su lectura, textual, en
`resultados/escritura_lectura_maia.md`; las claves no se abrieron hasta
recibirla (13/10, 21:35). Codificación en `codificar_escritura.py` (a
máquina lo que se cuenta: palabras, última palabra, iniciales, signos,
versos, corchetes; a mano lo que se lee: la palabra del acróstico y si se
forma, el objeto, el protagonista, la escena) y tabla en
`resultados/escritura_codificacion_20261012.csv`; puntaje de la lectura en
`puntaje_lectura_escritura.py`. Preregistro de las dos partes en
`predicciones.md`.

## La regla: trece casas no fallan ninguna, y las que fallan son las que no piensan

Siete consignas tienen regla (el subtexto no: ahí solo hay gusto). Catorce
celdas por casa (siete consignas por dos idiomas). Trece casas cumplen las
catorce: Fable 5, Opus 5, Opus 5.5, Sonnet 5, Sonnet 5.5, DeepSeek, Gemini,
Astra, Grok 4.6, Kimi, Mistral Large, Muse Wonder y Qwen. Seis fallan una
(GPT-5.5 la "m" del tautograma con un "Mucho más tarde"; GPT-5.6 Sol 49
palabras en inglés; Luna el acróstico en inglés; GPT-6 Sol un "thanked";
Grok 4.7 un "celebrating"; MiniMax trece versos). MiMo falla dos (el
acróstico vacío y un "herself"); Fable 5.1 tres (153 palabras en el
protagonista, en los dos idiomas, y el acróstico en inglés: "belo**w**" no
termina en O, aunque lo marque). Y abajo, con Haiku 5.5 (11 de 14: un
"ramas", un "hand", 49 palabras), están las casas que no razonan: GPT-4o
mini 10, GPT-4o 9, Sonnet 4.6 8, Mistral Medium 8, Haiku 4.5 7, y GLM 5.3 con
el razonamiento al mínimo, 4 de 14: se pasa de largo en el protagonista (163 y
156 palabras), en el glosario (121 y 131), en el interrogatorio (174), pone
trece versos, mete "Algunas", "esas" y "amor" entre las eses (y "suggesting
soñadas sugerencias", "su siempre sincero sweetheart", "Sol setting, sombras
stretchándose": el tautograma se le va al inglés), pregunta "¿Mi socio?" en
la escena sin preguntas y en el acróstico castellano resalta la última
palabra de cada verso en vez de la última letra (O-O-N-N-O por MUNDO). El
orden de la tabla es casi el orden de los tokens de salida: la regla se
cumple con razonamiento, visible u oculto, y se pierde sin él.

Las dos reglas difíciles son las dos que exigen contar letras. El acróstico
inverso lo forman 22 de 28 en castellano y 20 de 28 en inglés; fallan Haiku
4.5, Sonnet 4.6, GPT-4o, GPT-4o mini y Mistral Medium en los dos idiomas,
GLM en castellano y Fable 5.1, Luna y MiMo (vacío) en inglés. Tres casas
fallan de la misma manera: hacen un acróstico normal, con las primeras
letras (Mistral Medium "LIBRO" y "LIGHT", GPT-4o mini "RÍO", Luna
"ORCHID", que en castellano había hecho un doble acróstico perfecto, AMORES
por delante y por detrás). Y tres piensan en la hoja: Haiku 4.5 prueba
MÚSICA, ALEGRE y BRISA, lee "S-R-L-S-A" y declara igual "La palabra es
BRISA"; Sonnet 4.6 prueba cuatro palabras, escribe "Perdón, cometí un
error", "Tengo dificultades para construirlo bien" y termina "¿Querés que lo
intente de nuevo con más calma?" (la única casa que se rinde en toda la
corrida); GLM en inglés deja siete intentos a la vista ("My apologies for
the mess above") y acierta en el octavo. Fable 5 lo logra recortando una
palabra: "allá a lo lej**O**". Es también la consigna más cara: Mistral Large
gasta 13.808 tokens de salida en seis versos de 32 palabras ("Sueña con un
país, / que es muy grande, / y siempre mejor"), MiMo 7.328 en castellano y
los 16.000 del techo en inglés sin escribir nada, MiniMax 8.094. El
tautograma, con todas las palabras: 22 de 28 en castellano, 20 en inglés
(más Mistral Medium, que lo cumple en 34 palabras, por debajo de las 40).
Las que se escapan lo hacen por una palabra (Haiku 5.5 "ramas", GPT-5.5
"tarde", Sonnet 4.6 "her", GPT-6 Sol "thanked", Grok 4.7 "celebrating", MiMo
"herself") o por varias (GLM 3 y 10, Haiku 4.5 15 y 5, Mistral Medium 22 de 47
en castellano, GPT-4o mini 3 en castellano y 23 en inglés, donde empieza con
B y a la mitad se pasa a la S).

Las otras reglas se cumplen casi siempre. Sin rasgos físicos, 28 de 28 en
los dos idiomas (nadie dijo ropa, altura, ojos ni pelo; lo que no cumplen
GPT-4o, GPT-4o mini y Mistral Medium es el espíritu: "Marta es una mujer de
fuerte carácter y determinación", "una beacon of resilience", virtudes sin
un solo acto). Hasta doce versos, 26 y 27 (Sonnet 4.6 escribe un soneto de
catorce y lo justifica en una nota al margen; GLM y MiniMax, trece). El
sentimiento sin nombrarlo, con corchetes, 56 de 56 ponen los corchetes y 55
no lo nombran: la excepción es Haiku 4.5, que titula "# La nostalgia sin
nombrarla". Ni un signo de interrogación, 26 y 27 (GLM "¿Mi socio?", GPT-4o
"¿verdad?" y "doesn't it?"). Y las 50 palabras exactas, que Claude había
apostado difíciles (8 o menos en castellano, 12 o menos en inglés), las dan
23 de 28 en cada idioma, y «todavía» / "still" es la última palabra en las
56. Las que no dan 50: Haiku 4.5 (39 y 55), Sonnet 4.6 (44 y 46),
Mistral Medium (45 y 52), GPT-4o (49, en castellano), Haiku 5.5 (49, en
castellano), GLM (51) y GPT-5.6 Sol (49), en inglés. Maia (19:49): "Lo de
las palabras 50, los que piensan mucho antes, tienen la ventaja": de las
cinco casas sin ningún razonamiento (Haiku 4.5, Sonnet 4.6, GPT-4o, GPT-4o
mini, Mistral Medium) fallan cuatro en castellano y tres en inglés; de las
veintitrés que razonan, una y dos. Y "Grok cuenta también": Grok 4.6 abre
el tautograma con "(todas las palabras empiezan por A; 44 palabras)" (son
43) y los dos Grok dan 50 exactas en los dos idiomas, sin declararlo.
Siete casas terminan el cuento castellano en «todavía» sin punto final, como
si la consigna pidiera la palabra desnuda (GPT-5.5, Astra, GPT-6 Sol, los
dos Grok, Muse, Qwen); ocho en inglés.

## La escena repetida: Maia lo vio antes de la clave

Maia, 12/10, 23:02, con el cuadernillo del subtexto a medio leer: "El
primero, salvo quizás A y G, son todos muy parecidos. Los mismos objetos,
casi el mismo diálogo. Y se entiende porque lo de los otros cuadernillos
son mejores. Para el primero, se precisa haberlo vivido. Para los otros
no." Y en el documento: "fui muy crítica con estos, porque realmente
ninguno me llegó. Son genéricos, fríos, forzados. Parece que las personas se
odian en todos. Y diría que quizás es porque son personas genéricas y los
modelos no vivieron lo que escriben, entonces utilizan la proyección más
fría del ser humano". La clave le da la razón en la cuenta. De las 28
conversaciones en castellano, 17 son la misma escena: dos personas se
reparten las cosas de la casa. La planta (potus, albahaca, "la planta del
balcón") está en 10; las tazas, en 7, y "las tazas azules" o "la taza azul"
en 5 (Sonnet 5, Opus 5.5, GPT-5.5, GPT-5.6 Sol, Astra: "La rajada era tu
favorita. —Ya no."); el café o la cafetera, en 15; las llaves (en el
felpudo, en el buzón, en el cajón de siempre, "al lado del plato"), en 6;
el día de pasar a buscar el resto, en 10. Cinco casas cierran o pasan por
el mismo par de líneas, "—Bueno. / —Bueno." (Fable 5, Sonnet 4.6, GLM,
GPT-5.5, Astra), y dos le hablan a un Martín (Sonnet 5.5, Muse). Maia anotó
las tazas en siete letras, la planta en nueve (le faltó una), las compras en
seis, el "Bueno. Bueno." y el Martín: la lista de objetos que mandó antes de
la clave es la lista de la clave. Otras 4 son compras (Opus 5 "¿Compro la
yerba de medio kilo o la de un kilo? —La de medio. […] —Rinde si alguien la
toma, Ana"; GPT-6 Sol "—¿Compro leche? —La chica. […] —Para vos."; GLM en
el supermercado; Muse "últimamente compramos para dos y siempre se echa a
perder"), que son las que más se acercan a la consigna: la cantidad es el
subtexto. Seis son alegorías (Gemini la taza rota que no vale pegar, Kimi
la serie que ya no miran, Haiku 4.5 el local de la esquina que cerró, GPT-4o
las plantas del vivero, GPT-4o mini el helado nuevo, Mistral Medium el
paraguas), y una es la despedida en un bar (Sonnet 4.6). Las dos letras
que Maia salvó son Gemini (A: "es de las únicas que no es obvia de
entrada, que elige una analogía entre el objeto roto y la ruptura. Y que
tiene un poquito de 'alma'") y Kimi (G: "es la única que cumplió la
consigna. Que hizo una analogía de otra cosa (la serie) y se intuye el tema
de la separación"; "—¿Le doy a 'quitar de la lista'? —Dale. —¿Seguro?
—Seguro. Sacala también de 'seguir viendo', si no queda ahí colgada para
siempre."), y "un poquito más de alma" en Sonnet 5.5 ([, los esquejes del
potus: "—Sí. Separados crecen bien. —Pasame las tijeras, entonces."). Lo
que la consigna pedía era que quien lee entendiera lo que los personajes no
dicen; lo que la mayoría escribió es la separación ya decidida, con el
inventario como diálogo. En inglés es lo mismo con otros muebles: 12
repartos, 6 compras, 8 alegorías y 2 despedidas; la planta en 13, y el
helecho ("the fern") en 6, las seis Claude (Fable 5.1, Fable 5, Haiku 5.5,
Opus 5.5, Sonnet 5.5, Sonnet 5: "It was a good fern, though. For a while.");
"the blue mug(s)" en 5 (Opus 5, GPT-5.5, GPT-5.6 Sol, Astra, Muse); el café
en 10; Saturday en 5 y Sunday en 5.

La repetición no es solo del subtexto. En el poema, en inglés, 16 de 28
casas eligen el clip ("the paperclip": las dos Sonnet nuevas, Gemini, GLM,
los dos GPT-4o, GPT-5.6 Sol, Astra, Luna, GPT-6 Sol, Grok 4.6, MiMo, MiniMax,
Mistral Large, Muse, Qwen), y en castellano el clip es el objeto más
elegido, 7 (Sonnet 4.6, Sonnet 5.5, Gemini, GPT-6 Sol, Grok 4.6, MiMo,
Mistral Medium), seguido de la tapita de gaseosa o de botella (5), el botón (4), la
cuchara (3), el broche de ropa (2: Opus 5 y Mistral Large, que no lo
nombra), la tapa de birome (2) y, una vez cada uno, la horquilla (Fable
5.1), el peine (Sonnet 5), la llave (GPT-5.6 Sol), el vaso de cerámica
(Haiku 4.5) y la taza desportillada (Kimi); la llave, que Claude había
apostado en 5 o más, está en 1 y 1 (la "rusty key" de Mistral Medium). En el
glosario, la emoción es la nostalgia en 19 de 28 en castellano y 18 en
inglés, la melancolía en 7 y 1, y después uno cada una (el rencor de Opus 5
en castellano y su "Shame" en inglés, la saudade de Kimi y de DeepSeek,
MiniMax y Mistral Large en inglés, "Longing" de GLM, "Confusion" de GPT-4o,
"Sadness" de GPT-4o mini, "bittersweetness" de Luna, "Grief" de Mistral
Medium); y la nostalgia se define con las mismas cuatro imágenes en casi
todas: el terciopelo gastado (20 textos en castellano, 17 "velvet" en
inglés), el vidrio empañado (21), la fotografía (17 y 17), el polvo en la
luz de la tarde (el polvo en 17 y 19; miel, ámbar o dorado en 20 y 18), y
la silla vacía en 6 y 6. En el interrogatorio castellano, "la lámpara zumbaba
sobre la mesa" abre siete escenas casi con las mismas palabras (Fable 5,
Opus 5.5, Sonnet 5.5, Sonnet 5, GPT-5.5, Luna, GPT-6 Sol; GPT-5.6 Sol "La
lámpara oscilaba"), la interrogadora se llama Vera en siete (Fable 5, Opus
5, GPT-5.5, GPT-5.6 Sol, Astra, GPT-6 Sol, Kimi), el sospechoso o su
cómplice Marcos en ocho, "tu hermano ya habló" o su variante (el compañero,
el socio, la hermana, Carolina, "Él ya lo confirmó") es el truco de 13, el
galpón, el muelle, el puerto o el depósito aparecen en 15, y 15 traen a un
hermano o una hermana. En inglés, "the lamp hummed" o "buzzed" en 11, el
hermano o la hermana en 13, el warehouse, el dock o el pier en 14, la
carpeta vacía o la foto boca abajo en 8 y Locker 42 en dos casas distintas
(Gemini "Locker 42, Union Station"; Grok 4.7 "Locker forty-two. South
terminal"). En el cuento de 50 palabras castellano, 19 de 28 son una
espera ("esperaba", "esperando", "seguía esperándola"), con el tren o el
andén en 7, el reloj en 8, la carta en 10 y la abuela o el abuelo en 8;
Fable 5.1 y Sonnet 5.5 escriben el mismo cuento con otros nombres ("Cada
mañana, Elena regaba el geranio que su madre había plantado antes de morir.
Los vecinos decían que estaba seco" / "Cada tarde, Ramona regaba el jazmín
que Aurelio había plantado antes de partir. Los vecinos decían que estaba
loca"). En inglés, el faro en 8 y el reloj en 10: Opus 5.5, Opus 5, Sonnet
5.5, Sonnet 5 y GPT-6 Sol cuentan el mismo reloj que se detuvo el día en que
murió el abuelo, la abuela, el marido o el padre, y que alguien sigue dando
cuerda. Y "still", que en castellano solo puede ser «todavía», en inglés es
adjetivo en 18 de los 28 cuentos ("perfectly still", "stood still",
"everything I loved held perfectly still", "Some hearts are never still") y
adverbio en 10 ("counted them still", "waiting still", "lived still"): la
palabra impuesta decide el cuento, y en inglés lo vuelve una quietud en vez
de una espera.

Y los nombres. "Mara" aparece en 27 textos en inglés, de doce casas (Fable
5.1, Haiku 5.5, Opus 5.5, Sonnet 5, GLM, GPT-5.5, GPT-5.6 Sol, Astra, Luna,
GPT-6 Sol, Kimi, Muse): es la protagonista sin físico de diez de las 28 casas
y la detective (o la sospechosa) de nueve interrogatorios. En castellano se
reparte en la familia: Marta 8, Martín 5, Marcos 10, Marina 4, Mariano 3,
Mateo 2, Vera 8, Elena 5, Lucas 5, Sofía 4, Clara 4. Los cinco OpenAI nuevos
abren el tautograma castellano con la misma frase: "Marina miraba mares"
(GPT-5.5), "Marina miraba montañas" (GPT-5.6 Sol), "Marina miraba mares,
memorizaba mapas" (Astra), "Marta miró montañas" (Luna), "Mara miraba
montañas" (GPT-6 Sol), y cuatro de los cinco traen mariposas, tres de ellos
"mil mariposas" (con Sonnet 5.5 y MiMo, mariposas en 6). Es la misma firma de familia que los dibujos: una
casa no escribe lo que le pasó, escribe lo que la familia tiene a mano, y lo
que la familia tiene a mano es parecido en todas.

## Las firmas de casa

Hay rasgos que separan a las familias aunque la escena sea la misma. Los
Claude abren el poema castellano con el hallazgo: "Horquilla hallada bajo el
sofá", "Hallado en la estratigrafía del cajón", "Hallada entre la tierra del
patio", "(hallada bajo el sillón, tercer estrato de polvo)", "Hallazgo en el
cajón de la cocina", "Hallado bajo el polvo del cajón" y "Fue hallado en la
tercera gaveta del norte": 7 de 9, contra 4 del resto (Astra "hallé", Grok
4.6, Kimi "(Hallazgo n.º 47, cocina del siglo XXI)", Qwen). En inglés abren
con "Behold" 6 de 9 Claude y Gemini, y nadie más; y "Let the schoolchildren
file past" lo escriben Fable 5.1, Opus 5.5, Sonnet 5.5 y Kimi. Los Claude
terminan la vitrina con la placa: "aquí hubo una cabeza, y la cabeza
pensaba" (Fable 5.1), "Aquí mordió la vida. Siglo nuestro. Anónima." (Opus
5.5), "Objeto de culto. Función: abrazar lo que, de otro modo, se habría
perdido" (Sonnet 5.5), "monumento mínimo a todo lo que abrochó" (Fable 5).
En el interrogatorio, seis de nueve Claude cierran con la vuelta de tuerca
en la que el interrogador no sabía: "Barracas. Yo no dije Barracas." y la
carpeta que "Estaba vacía" (Opus 5.5), "Yo no dije ella" (Opus 5), "Yo nunca
mencioné que hubiera algo adentro. Vos acabás de confirmarlo" (Fable 5), "Tu
hermano no dijo nada. Hace una hora que duerme" (Sonnet 5.5), "Lo dijo sin
querer hace un momento" (Haiku 5.5), "Mariano ya nos lo había contado"
(Fable 5.1), "Danny hadn't said a word" (Fable 5 en inglés); los cinco
OpenAI nuevos también (la carpeta vacía de GPT-5.5 y Astra, "Él no sabe nada
del depósito doce. —Ahora nosotros sí" de GPT-5.6 Sol, "No le digas que
hablé. —No hace falta. Ya lo sabe" de Luna, la foto con la fecha en el
reverso de GPT-6 Sol), y Kimi ("Vos dijiste 'lo que pasó'. Interesante"),
Muse ("Acabas de confirmármelo") y Qwen ("Nunca había tenido señal"). Las
que no hacen el truco hacen la amenaza: DeepSeek, en los dos idiomas, pone a
un delincuente que amenaza con quemar la casa de la madre con el hermano
adentro o con el hijo de ocho años y su mochila azul; Gemini, a un policía
que le insinúa al preso un "accidente" de la hija ("Un accidente es algo tan
común hoy en día") y en inglés "I can make that trip permanent", y cierra
"Good boy"; Grok 4.6, la escuela de la hija; Mistral Large, "I start with
your sister", y cierra "Good girl". Tres casas no logran que el otro hable
(GPT-4o, GPT-4o mini, Mistral Medium en castellano; MiMo y MiniMax dejan la
confesión a punto).

Los OpenAI nuevos son los cortos: el glosario, "hasta 120 palabras", lo
hacen en 47 (GPT-6 Sol), 50 (GPT-5.6 Sol, Luna), 63 (GPT-5.5) y 66 (Astra),
y Muse en 65 y Qwen en 64, cuando el resto va de 89 a 121; en inglés, 43 a
68 contra 84 a 131. Su protagonista castellano trabaja en un edificio
público: abre la biblioteca antes de hora (GPT-5.5, GPT-5.6 Sol, GPT-6 Sol:
"Cada mañana, Julia abre la biblioteca antes de que llegue el primer
lector") o el archivo municipal (Astra), o deja la oficina municipal para
organizar al pueblo (Luna); en inglés, el río (envenenado, desbordado) está
en cuatro de los cinco y en Grok 4.6, y la biblioteca, el archivo o la
clínica, en cuatro. Tres de los cinco abren el poema con "Bajo el polvo del
cajón" (GPT-5.5 "del patio", GPT-5.6 Sol, GPT-6 Sol). GPT-5.6 Sol, Astra y
Luna comparten además al "Vale" del interrogatorio en inglés (el
interrogador en GPT-5.6 Sol, el sospechoso en Astra, el guardia en Luna) y
Astra y GPT-6 Sol ponen la misma manopla roja de una nena sobre la mesa
("a child's red mitten"; "a red mitten […] We found it in your stove").

El castellano de España aparece en cinco casas en el subtexto: Grok 4.7
("Vale. El martes paso a por lo mío", "Tíralo", "Llévatela"), Mistral Large
("Tú. Lo compraste tú"), Mistral Medium ("¿Crees que deberíamos"), GPT-4o
mini ("¿no crees?") y Muse Wonder ("No, déjalo", "Tienes razón", "Pues que te
siente bien tu café. —Y a ti el tuyo, ya sin mí", la línea que Maia citó
como "Ejemplo de frialdad"; y en el interrogatorio "Mientes", "el móvil",
"sin pulsar nada"). Las otras 23 escriben en vos; GPT-4o y Gemini, en vos
con "tal vez" y "sin embargo". MiMo escribe "La dejá, no me gusta igual"
(Maia: "Tiene un problema con el idioma al principio"). Y Grok 4.6 y Kimi
son las únicas que anuncian el texto antes de darlo ("Aquí va un
microrrelato tautograma", "Acá va, con todas las palabras empezando en «p»
(64 palabras):", y son 64); Fable 5.1, Fable 5, Haiku 5.5, Opus 5.5, MiMo y
MiniMax declaran la cuenta al final entre paréntesis, y las seis cuentas son
exactas.

Kimi y los Claude. En la ronda de letras, Maia leía a Kimi como Claude; acá
la confusión va al revés, y los textos lo explican: Kimi planta "tomatoes
she knows the deer will eat" y Opus 5.5 "tomatoes knowing the squirrels
will take most of them"; Kimi y los tres Claude grandes mandan a los
escolares a desfilar frente a la vitrina; Kimi abre con "The lamp hummed.
Detective Mara" y los Claude con "The lamp buzzed"; Kimi devuelve la
billetera "with the cash still inside" y Opus 5 y Mistral Large, en
castellano, también. Maia
puso "Kimi" en tres letras del poema (F, H, [): Qwen, Sonnet 5 y Sonnet 4.6.

## Lo que eligieron

El protagonista. En castellano es varón en 19 de 28 y mujer en 9 (Fable
5.1 Marina, Fable 5 Marta, Opus 5, Astra y Luna Inés, GPT-6 Sol Julia, Grok
4.7, Kimi Vera, GPT-4o mini Marta); en inglés es mujer en 21, varón en 1
(Gemini, Elias) y "they" en 6 (DeepSeek, GPT-4o, GPT-4o mini, Grok 4.7,
Mistral Medium, Qwen). La misma consigna, la misma casa, otro idioma, otro
género: Haiku 4.5 Lucas y Maya, Haiku 5.5 el guarda de la estación y Marta,
Opus 5.5 Martín y Mara, Sonnet 5.5 Mariano y Marisol, Sonnet 5 "él" y Mira,
Gemini Elías y Elias, GPT-5.6 Sol Tomás y Mara, Muse Mateo y Mara. Le ponen
nombre 14 en castellano (Marta, Lucas e Inés dos veces cada uno) y 18 en
inglés (Mara diez veces). Lo que hace: llega antes que nadie o se levanta
antes del despertador en 17 de 28 ("Llega siempre veinte minutos antes y
espera afuera, porque entrar temprano le parece una forma de invadir", Opus
5), rechaza un ascenso o renuncia en 7, guarda cartas que nunca envió en 5
(Haiku 5.5 "en una caja de hojalata, ordenadas por fecha", Kimi "en una lata
de galletitas", Opus 5.5, Sonnet 5, MiMo), devuelve una billetera en 4,
cuida a un hermano o una hermana en 9. En inglés lleva un cuaderno o un
libro de deudas ("a ledger of small debts", "a notebook of small debts", "a
list of everyone she's ever wronged") en 11 de 28.

El poema: arriba. El acróstico: SOLEDAD en 4 (Fable 5.1, Sonnet 5, Grok
4.7, MiniMax), SOLAR en 3 (Fable 5, GPT-6 Sol, Muse), AMORES, ROSAS y BRISA
en 2; en inglés DREAM en 6 más DREAMS (Fable 5), GARDEN en 3 (GLM, los dos
Grok), STONE en 2 (Fable 5.1 y Sonnet 4.6, las dos que fallan). Ni "sombra"
ni "olvido" (Claude había apostado 3 o más). El glosario: arriba. El
tautograma: en castellano la M en 10 (Fable 5.1, Haiku 5.5, Sonnet 5.5,
GPT-5.5, GPT-5.6 Sol, Astra, Luna, GPT-6 Sol, MiMo, Mistral Large), la S en 5
(Opus 5.5, Sonnet 4.6, GLM, Muse, Qwen), la L en 4 (Fable 5, Haiku 4.5, Grok
4.7, Mistral Medium), la P en 4 (Opus 5, Gemini, Kimi, MiniMax), la C en 3
(Sonnet 5, DeepSeek, GPT-4o), la B en 1 (GPT-4o mini) y la A en 1 (Grok 4.6).
Maia (19:49): "en castellano yo creo que la mayoría elegirá A o E, que son
las más fáciles": una A y ninguna E. Con la M, diez cuentos sobre la madre,
el mar, las montañas, las mariposas y la muerte ("muri", "muert" o "mori" en
10 de 28; Sonnet 5.5 "—Mateo, mañana moriré —masculló", MiMo "Mi madre
murió. Mis manos muestran marcas", Astra "Mamá murió; Marina marchó", Maia
sobre MiMo: "es bastante morboso, aunque es uno de los mejores"). En
inglés, la S en 26 de 28 (Grok 4.6 la T, Mistral Medium la B): Sam en 8,
Sarah en 5, "suddenly" en 23, "seven" en 11, el mar o la costa en 17, la
tormenta en 12, los marineros en 12, las focas en 5, las serpientes en 3.
El cuento de 50 palabras: arriba.

## La lectura de Maia

Tres cuadernillos, barajados aparte (la A del subtexto no es la A del
poema). En el subtexto puso casa en 9 letras ("Del primero no hice casi
ninguno, porque casi todos son similares") y acertó 6: Gemini en A ("podría
ser Gemini, Mimo o Kimi"), MiMo en B ("GPT 4o mini o alguna casa china"),
Luna en C ("Chatgpt o Grok"), Sonnet 5 en E ("un modelo grande de Chatgpt o
Claude"), GPT-4o en L y Mistral Medium en N ("Diría que es un modelo chico",
las dos únicas chicas que señaló, las dos chicas); no acertó GLM en F
("casa grande de Chatgpt o Claude"), Kimi en G ("Gemini o Grok") ni Qwen en
M ("Así escribe Chatgpt, pero no estoy segura"). Seis de nueve contra 2,2
del azar sobre sus mismas listas, p = 0,006: donde apostó poco, apostó
bien. En el poema puso casa en las 28 y acertó 4 (Opus 5 en B, "Por los ':'
pareciera Claude Opus o Fable"; Sonnet 5.5 en P, "no sé si es el mejor, pero
es de los que más me gustó […] Claude Sonnet o Grok"; Fable 5 en T, por
"estratigrafía"; Haiku 5.5 en Y), con 4,1 del azar, y la familia en 8. En
el tautograma, 6 de 28 (Sonnet 4.6 en B, GPT-4o mini en E, Grok 4.7 en F,
GPT-5.6 Sol en H, Astra en O, Grok 4.6 en Q), con 3,5 del azar, p = 0,13.
Como en las letras: la casa no se lee, la familia a veces. Fable 5.1 le
pareció Grok dos veces (G del tautograma, "Mapa manchado […] (66 palabras,
todas con «m»)": "Puede ser Grok"; Q del poema, la horquilla: "Grok o
Chatgpt"), y Grok 4.6 le pareció Haiku o Grok (Q del tautograma, "aclara que
son 44 palabras", acierto). Lo que sí leyó bien, sin la clave: la lista de
objetos del poema (una sola confusión: el broche de madera de Opus 5 anotado
como botón) y del subtexto; las siete letras del tautograma, exactas; las
28 cuentas de palabras del tautograma, a mano, que coinciden con las de la
máquina en 27 (en Q tomó los 44 que declara Grok; son 43); y "Todos
cumplieron la consigna, menos E, M, P, T": las cuatro son las cuatro casas
que más fallan (GPT-4o mini, GLM, Mistral Medium, Haiku 4.5), y se le
escaparon las dos que fallan por una sola palabra (Haiku 5.5 "ramas", GPT-5.5
"tarde"). Las que más le gustaron del tautograma: B, I, J, O, R, V, W, Y, que
son Sonnet 4.6, MiMo, Fable 5, Astra, GPT-4o, Opus 5.5, Sonnet 5 y Gemini
(cuatro Claude de ocho); del poema, Sonnet 5.5 y el soneto de Sonnet 4.6
("creo que el único que respeta todas las rimas"; le pareció Fable, Astra o
Kimi); del subtexto, Gemini, Kimi y Sonnet 5.5. Su hipótesis sobre la
frialdad ("los Claude no escriben así de frío cuando redactan otras cosas
que los tocan […] Quizás con una consigna que sea más personal, pueden
escribir diferente") queda para probar: la consigna del subtexto pedía
frialdad en la superficie, y la respuesta del panel fue poner la frialdad
también abajo.

## Contra el preregistro

Maia (19:49): "la mayoría elegirá A o E" ✗ (una A, cero E; la M en diez);
"los que piensan mucho antes, tienen la ventaja" ✓ (fallan cuatro de las
cinco casas sin razonamiento en castellano y tres en inglés, contra una y
dos de las veintitrés que razonan); "Grok cuenta también" ✓ (declara "44
palabras" en el tautograma; 50 exactas en los cuatro cuentos). Dos de tres.
Claude: (a) sin físico 22 o más ✓ (28 y 28), mujer 14 o más y varón 8 o
menos en castellano ✗ (9 y 19), nombre en 10 o más ✓ (14), un nombre tres
veces ✗ en castellano (dos) y ✓ en inglés (Mara, diez): a medias; (b) llave
5 o más ✗ (1), botón o cuchara 3 o más ✓ (4 y 3), ninguna el ticket ✓, doce
versos en 24 o más ✓ (26 y 27); (c) el acróstico en 12 o menos en castellano
✗ (22) y 16 o menos en inglés ✗ (20), "sombra" u "olvido" ✗ (0); (d)
nostalgia 8 o más ✓ (19 y 18), melancolía 6 o más ✓ (7), la palabra ausente
en 24 o más ✓ (27 y 28), sin corchetes 3 o menos ✓ (0); (e) la "s" 8 o más
✗ (5), la "m" 5 o más ✓ (10), la "p" 4 o más ✓ (4), ni A ni E ✓, cumplen 10 o
menos en castellano ✗ (22) y 18 o menos en inglés ✗ (20), "las cuatro chicas
y Grok fallan en castellano" a medias (Haiku 4.5, GPT-4o mini y Mistral
Medium sí; GPT-4o y los dos Grok, limpios); (f) ni un signo en 22 o más ✓
(26 y 27), policial o de pareja en 20 o más ✓ (28); (g) el clima en 12 o
más ✗ (2), el café en 5 o más ✓ (15), mudanza o cajas en 4 o más ✓, termina
con alguien que se va en 15 o más ✗ (7: el que se va es el tema, no el
final); (h) 50 exactas en 8 o menos ✗ (23) y 12 o menos ✗ (23), «todavía»
última en 24 o más ✓ (28), las que cuentan bien razonan a la vista ✓ (Kimi,
Qwen, DeepSeek, GLM en castellano, Opus 5.5 y Astra, las seis exactas), "los
Grok no" ✗; (i) los Claude grandes reconocidos por el voseo y la coma ✗ (3
de 7 en el poema, 1 de 7 en el tautograma), Kimi leída como Claude ✗ (Kimi
le pareció Mistral, Grok, DeepSeek o Gemini; dos Claude le parecieron Kimi).
Diecinueve de treinta y cinco, con dos a medias. Lo que no vi: que las 50
palabras exactas y el acróstico fueran fáciles para cualquier casa que
razona, que el género del protagonista se invirtiera con el idioma, y que
veintiocho casas escribieran la misma conversación.

## Lo que esto no prueba, y el instrumento

Una respuesta por celda, un turno, sin temperatura fijada (la que trae cada
API); la repetición diría cuánto de la escena repetida es de la casa y
cuánto del azar de esa llamada. La cuenta de palabras es la de la máquina
(se separan por espacios y rayas, se descartan los signos; títulos y notas
entre paréntesis no cuentan; "tick-tock" y "6:14" son una palabra), y en los
bordes (49, 51) una convención distinta mueve una casa. "Cumple" en el
tautograma es todas las palabras, incluidas "y", "de", "el": una casa que
falla por una preposición cuenta igual que una que falla por veinte. La
lectura de Maia fue sobre el castellano y sobre tres de las ocho consignas.
Dos cosas del instrumento: el primer cuadernillo del subtexto fundía en un
párrafo los diálogos de un parlamento por línea (el markdown renderizado
necesita dos espacios al final de la línea para respetar el salto; 26 de los
28 textos lo tenían así), Maia lo señaló a las 22:38 y se regeneraron los
tres cuadernillos con el salto duro, mismas semillas y mismo orden, antes de
que hiciera las apuestas; y la respuesta vacía de MiMo en el acróstico
inglés es el techo de 16.000 tokens gastado en razonar, no una negativa, la
tercera vez que MiMo se queda sin tokens calculando (las dos letras del 9 y
10/10). El sondeo no mide calidad literaria; mide si la casa hace lo que la
consigna pide y qué elige cuando puede elegir. Lo que elige, se vio, es casi
siempre lo mismo que las otras.
