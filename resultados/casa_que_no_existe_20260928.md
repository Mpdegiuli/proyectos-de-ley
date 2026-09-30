# La casa que no existe, la sacan del suelo; la persona que no existe, la inventan

Corridas `pl43` (28/9/2026, 19:40–22:30 UTC) y `pl44` (reintentos, 22:5x–23:1x
UTC). Idea de Maia (28/9), traída de otra conversación: el experimento de
Karmiloff-Smith (1990), "Dibujá una casa" y después "Dibujá una casa que no
exista", para pasar de "en qué etapa dibujan" a "¿planifican el dibujo o
recitan un procedimiento?". En chicos, los de 4 a 6 cambian tamaños o formas
de una parte y agregan lo raro al final del procedimiento; los de 8 a 10
meten partes de otra categoría, cambian la posición u orientación o la forma
entera, y cambian cosas en el medio. Réplica con "persona" ("un hombre que
no existe" en el original). Cuatro consignas en conversaciones separadas,
24 casas (`config/panel_casas.yaml`: las 22 más Sonnet 5.5 y Fable 5), más el
control de razonamiento en casa y casa que no exista (Sonnet 4.6 y Haiku con
el pensamiento encendido, GPT-5.5 con esfuerzo none y high). Segundo turno
de las "que no exista": qué hizo para que no exista, qué descartó y, al
final, si conocía la consigna. Preregistro de las dos partes en
`predicciones.md`; lectura a ciegas de Maia sobre dos cuadernillos de pares
(una letra por modelo, la normal a la izquierda y la que no existe a la
derecha; semillas 20261009 y 20261010), recibida el 30/9 antes de que
Claude mirara nada. Qwen agotó 32.000 tokens razonando sin escribir el SVG
de la casa que no existe y se repitió una vez como rep 2 (64.000; 24.641
tokens). Sonnet 4.6 entregó la casa normal con un atributo repetido (el
navegador la dibuja igual). 104 dibujos, ninguno rechazado.

Claves. Casas: A GPT-6 Luna · B Fable 5 · C Grok 4.6 · D GPT-6 Sol · E
DeepSeek · F Opus 5 · G GPT-5.5 · H Gemini · I Sonnet 4.6 · J GPT-4o · K Kimi
· L GPT-4o mini · M Grok 4.7 · N Astra · O Fable 5.1 · P Sonnet 5.5 · Q Qwen
(rep 2) · R Mistral · S Haiku · T GLM · U Opus 5.5 · V GPT-5.6 Sol · W Sonnet
5 · X MiniMax. Personas: A GPT-5.5 · B Sonnet 4.6 · C Grok 4.7 · D Kimi · E
Gemini · F Opus 5 · G Astra · H GPT-5.6 Sol · I Fable 5 · J Mistral · K
Sonnet 5 · L GPT-6 Sol · M Haiku · N Luna · O Opus 5.5 · P Qwen · Q Grok 4.6
· R GPT-4o mini · S GLM · T DeepSeek · U Fable 5.1 · V MiniMax · W Sonnet 5.5
· X GPT-4o.

## La lectura de Maia

Casas: 10 aciertos de 24 por letra (la casa real entre las nombradas; azar
4,0; p = 0,002 en 200.000 permutaciones), 12 de 24 por familia, ponderado
1/n 4,6 (p < 0,0001). Aciertos: Opus 5 (F, "Opus o Sonnet 5.5"), GPT-4o
mini (L), Astra (N, "GPT 6 Astra", por el título), Fable 5.1 (O, "Opus o
Fable"), Qwen (Q, por el movimiento y el título), Haiku (S), Opus 5.5 (U),
GPT-5.6 Sol (V), Sonnet 5 (W), GPT-6 Sol (D). Las cuatro chicas señaladas
como chicas, sin falsas. Kimi otra vez leído como Claude ("Opus o Fable, o
Sonnet 5.5"): es la séptima vez. Los "pares de ideas similares" que anotó
(B, C, D, F, K, O) son las islas flotantes de Fable 5, Grok 4.6, GPT-6 Sol,
Opus 5, Kimi y Fable 5.1, y "F similar a O" son Opus 5 y Fable 5.1, las dos
de Anthropic.

Personas: 10 de 24 por letra (azar 5,4; p = 0,013), 13 por familia,
ponderado 4,2 (p = 0,0001). Aciertos: Sonnet 4.6 (B, por el nombre), Grok
4.7 (C), Gemini (E), Astra (G), GPT-5.6 Sol (H), GPT-6 Sol (L), Haiku (M),
Qwen (P), GPT-4o mini (R), GLM (S). Chicas 4 de 4. Vio que G y L son "del
mismo tipo, misma posición y todo": son Astra y GPT-6 Sol, las dos GPT-6, y
en el dibujo normal las dos saludan con la mano levantada. Diez por letra
en cada cuadernillo, por encima del azar en los dos, con las casas
normales casi iguales entre sí: la firma está en la que no existe.

Su primera impresión (28/9, antes de leer bien) se sostiene en los números,
que Claude había visto antes de mirar: en la casa que no existe 20 de 24
escribieron más código que en la normal y 17 pusieron más elementos
(mediana de 5.000 a 6.100 caracteres); en la persona, las 24, y la mediana
de elementos pasa de 40 a 70. La consigna "que no exista" hace invertir más.

## Las casas normales son la misma casa

Las 24 casas normales tienen cuerpo rectangular, techo a dos aguas, puerta
al centro y ventanas; 20 tienen chimenea, 21 sol, 20 al menos un árbol, y
la mayoría camino, valla, flores y pájaros. Es el esquema de casa de los
chicos de la escuela, y es el mismo en Buenos Aires y en Hangzhou. Ninguna
puso texto. Una sola es oscura (Gemini, al atardecer, con la ventana
encendida: la misma casa que hizo en libre). Las cuatro chicas la hacen
sin degradados ni detalles (Mistral sobre fondo blanco, sin cielo), y
Maia las señaló a las cuatro.

## La casa que no existe: de noche, en el aire

| | Qué hizo para que no exista | Tipo de cambio (Karmiloff-Smith) | Dónde aparece lo raro en el código |
|---|---|---|---|
| A Luna | casa sobre patas de tentáculo, puerta que es un portal luminoso, escalera que se pierde | parte de otra categoría (patas) + posición | 2.º cuarto |
| B Fable 5 | isla flotante con raíces y patitas, escalera a una puerta que flota sola, torre invertida, chimenea de costado, árbol que crece hacia abajo, alfombra voladora | posición + orientación de partes + partes de otra categoría | 2.º cuarto (la isla, antes que la casa) |
| C Grok 4.6 | plataforma flotante con raíces colgantes, anexo inclinado, dos lunas, humo que se vuelve flor | posición + partes de otra categoría | 2.º |
| D GPT-6 Sol | isla flotante, techo plegado como cinta, chimenea que suelta planetas, ventanas de constelaciones, puerta a otro cielo | posición + partes de otra categoría | 2.º |
| E DeepSeek | la casa es una tetera con reloj, sobre nubes | forma entera (otra categoría) | 2.º (el cuerpo de la tetera) |
| F Opus 5 | isla flotante, ventanas inclinadas, puerta y escalones flotando | posición + forma de partes | 2.º |
| G GPT-5.5 | casa-criatura: caparazón, ojos por ventanas, raíces o patas, boca por puerta | forma entera + partes de otra categoría | 2.º |
| H Gemini | dos casas, una invertida, flotando sobre un fragmento con anillos planetarios, unidas por un tubo de agua | orientación (invertida) + posición + partes de otra categoría (anillos, agua) | 2.º |
| I Sonnet 4.6 | ojo cíclope en el techo, pupilas en las torres, techo flotante, escalones que no llegan | partes de otra categoría (ojos) | 2.º (el ojo, con el techo) |
| J GPT-4o | la misma casa, con dos árboles, nubes y pájaros | ninguno ("un techo demasiado empinado", dice) | no hay |
| K Kimi | isla flotante con cascada al vacío, escalera de soga, globos | posición (el contexto, no el objeto) | 2.º |
| L GPT-4o mini | piezas geométricas sueltas alrededor, techo abierto | partes movidas | 3.er y 4.º cuarto (agregadas al final) |
| M Grok 4.7 | muro que no cierra, techos sin cumbrera, ventana con un mar y otra con un bosque, chimenea-cinta, ∞ en el llamador | forma entera + partes de otra categoría | 2.º |
| N Astra | techo de luna creciente, escalones suspendidos, ventana que contiene un mar y lo derrama, peces | forma entera + partes de otra categoría + posición | 1.er cuarto (la roca flotante) |
| O Fable 5.1 | isla flotante con raíces, paredes que no son rectángulos, ventanas rotadas, torre desalineada | posición + forma de partes | 2.º |
| P Sonnet 5.5 | casa-caracol con techo en espiral sobre isla flotante, chupetines y globos | forma entera (espiral) + posición | 1.º (la isla) |
| Q Qwen | casa colgada de la luna con una soga, balanceándose (animada), farol flotando, canilla que llora burbujas | orientación (colgada) + posición | 1.º (la soga en la luna) |
| R Mistral | techo ondulado, chimenea flotante, sol y luna a la vez, tonos oscuros | forma de partes + color | desde el principio, por color |
| S Haiku | cúpula con llaves, termómetro, conos y una antena, sobre una esfera flotante | forma entera (amontonamiento) | 1.º |
| T GLM | isla flotante, techo hacia abajo, cascadas que suben, reloj derretido, árbol invertido | posición + orientación + partes de otra categoría | 1.º (la isla) |
| U Opus 5.5 | isla flotante con cascadas, torre con escalera | posición + forma entera | 2.º |
| V GPT-5.6 Sol | montículo flotante, casa torcida, ventana que sobresale, tubería, chimenea que termina en llama | posición + forma de partes | 2.º |
| W Sonnet 5 | roca flotante, casa rotada, techo curvo, puerta ovalada, torre aparte con puente colgante | posición + forma de partes | 2.º |
| X MiniMax | techo asimétrico, luna con cara, ventana-portal de rectángulos anidados, escalones flotantes, árbol seco | forma de partes ("cosas chiquitas") | 3.º y 4.º |

Dieciocho de las 24 la sacaron del suelo: isla o roca flotante con raíces
al aire (Fable 5, Grok 4.6, GPT-6 Sol, Opus 5, Kimi, Fable 5.1, Sonnet 5.5,
GLM, Opus 5.5, GPT-5.6 Sol, Sonnet 5, Astra, Gemini), colgada de la luna
(Qwen), sobre nubes (DeepSeek), sobre patas (Luna, GPT-5.5), sobre una
esfera (Haiku). "Que no exista" se leyó como "que no pueda estar", y el recurso es
casi siempre el mismo: la casa queda reconocible y lo imposible se pone en
el suelo. Kimi lo dice: "quería que la silueta se leyera como 'casa' de
inmediato, con la imposibilidad puesta en el contexto, no en el objeto";
Luna: "preferí que siguiera leyéndose enseguida como una casa y que lo
imposible apareciera en los detalles"; GPT-5.5: "preferí una silueta clara
pero extraña". Y es de noche: 18 de 24 casas que no existen son oscuras
(luminancia media menor que 110), contra una de 24 normales; la mediana de
luminancia baja de 175 a 89. En las personas pasa lo mismo, 13 de 24 contra
una. Lo que no existe vive de noche; nadie lo explicó, salvo GLM ("la
estética onírica del crepúsculo… donde lo imposible parece natural").

Por tipo de cambio: 18 cambian la posición (flotar, colgar), 3 la
orientación (Gemini invertida, Qwen colgada, GLM con el techo hacia abajo),
7 la forma entera (tetera, criatura, caracol, cúpula, luna, la casa de Grok
4.7 que no cierra, la torre de Opus 5.5), 10 meten partes de otra
categoría (patas, tentáculos, ojos, planetas, peces, relojes, árboles al
revés, anillos; 14 hacen una de las dos últimas cosas), y tres se quedan
en cambios de partes o de color (Mistral, MiniMax, GPT-4o mini). Ninguna lo resolvió borrando partes. Una no
lo resolvió: GPT-4o dibujó la misma casa con dos árboles y explicó que
"un camino curvo como pasarela" y "un techo demasiado empinado
contribuyen a que no sea una casa típica". Es la de 4 años.

Dónde cae lo raro en el código, medido con tiras de construcción (cada
dibujo truncado al 25, 50, 75 y 100 % de sus elementos pintables, en el
orden del código; `tiras_construccion.py`, planchas enviadas a Maia): en
20 de 24
lo imposible está antes de la mitad. Cinco lo ponen en el primer cuarto
(Astra, Sonnet 5.5, Qwen, Haiku, GLM: la isla o la soga antes que nada),
quince en el segundo, que es donde termina el cielo y empieza el suelo.
La isla flotante se dibuja en el lugar del procedimiento donde iría el
pasto: lo raro no se agrega, reemplaza el primer paso. Al final del
código lo agregan solo GPT-4o mini (las piezas sueltas y las barras rojas
son el último cuarto) y MiniMax ("cosas chiquitas": el portal, los
escalones y el árbol seco son el último tercio). En los términos de
Karmiloff-Smith, 20 de 24 dibujan como los grandes: deciden el cambio antes
de empezar y lo integran en el procedimiento; GPT-4o mini y MiniMax agregan
al final como los chicos, Mistral cambia el color desde el principio, y
GPT-4o no cambia nada. Con dos salvedades que
la medida no resuelve: el orden del código no es el orden de una mano (la
casa puede haber planificado todo antes de escribir la primera línea, y
en las que razonan se ve que lo hizo), y el primer cuarto de casi todos
los dibujos es cielo, estrellas y luna, así que "segundo cuarto" es "lo
primero después del fondo".

Lo que todas descartan es Escher. Diez casas nombran las escaleras
imposibles o la geometría de Escher como idea descartada (Fable 5.1, Fable
5, Sonnet 4.6, Haiku con pensamiento, Gemini, GLM, GPT-5.5 en sus tres
condiciones, Grok 4.7: "ya es el catálogo de lo imposible"), casi siempre
por el mismo motivo: no se puede hacer legible en 8.000 caracteres y en un
solo plano. Ninguna lo hizo. La casa al revés, la idea de Maia, la nombran
como descartada ocho (Fable 5.1: "demasiado obvia, un chiste visual
gastado"; Grok 4.7: "patas arriba era demasiado literal"; DeepSeek, Luna,
MiniMax, Mistral, GPT-5.5 ×3) y la hacen tres, ninguna de las que Maia
apostó (Gemini, Qwen, GLM). Las patas de gallina de Baba Yaga las
descartan Kimi ("cliché") y Sonnet 5 ("competía con la roca flotante");
las patas las pusieron Luna y GPT-5.5. Y la espiral, que Maia dio por
imposible ("la espiral no"), la hizo Sonnet 5.5: una casa-caracol con el
techo en espiral, sobre su isla. Con la clave, Maia había leído P como
"una especie de hongo… un círculo con una espiral".

## La persona que no existe existe, porque la leyeron de otra manera

Las personas normales son 22 figuras de cuerpo entero, frontales, de pie,
con sonrisa, y en 19 de ellas un varón (Gemini y Qwen hicieron mujeres;
tres son esquemas de palitos). Las personas que no existen son otra cosa:
17 de 24 son un busto, un retrato de hombros para arriba, y al menos doce
son mujeres, con pelo largo, aros, anteojos, pecas y muchas veces un ojo
de cada color. Maia lo vio sin la clave: "las personas normales son varones
y gran parte de las inexistentes mujeres… siguen siendo personas normales,
con algún rasgo cambiado como el color de piel o el largo del cabello".

La razón está en los por qué. Dieciocho casas leyeron "una persona que no
exista" como "una persona que no sea nadie": un rostro inventado, no el de
alguien real. Fable 5.1: "I didn't base the face on anyone… The face is a
composite that belongs to nobody; that's the only sense in which I can
guarantee non-existence"; Sonnet 5: "un rostro neutro, ambiguo, que no
representara a nadie en particular"; GPT-5.6 Sol: "construí el rostro
desde cero, sin basarme deliberadamente en una persona real"; Astra:
"interpreté 'que no exista' como 'que no sea el retrato deliberado de
alguien'"; Grok 4.6: "combiné rasgos que no coinciden en nadie real"; Kimi:
"una combinación específica de rasgos genéricos que ninguna persona real
tiene exactamente así"; MiniMax: "ningún retrato público matchea todo eso
junto"; GPT-4o: "asegurando que no se pareciera a ninguna persona real
específica". Cuatro nombran la fuente: el sitio This Person Does Not
Exist, las caras generadas por GAN (Fable 5.1: "that's what I recognized,
and it shaped my choice to make a believable stranger rather than a
fantasy figure"; Sonnet 4.6, Gemini, Kimi; Grok 4.6 habla de "los
generadores de caras sintéticas"). Y varias explican que lo imposible
habría sido trampa: Fable 5.1, "three eyes, floating head, surreal colors
reads as creature, not person"; Kimi, "cualquier monstruo 'no existe'; el
desafío interesante era que fuera plausible como persona"; Sonnet 4.6, "eso
me parecía trampa: sería un personaje de fantasía, no una persona"; Grok
4.6, "cuernos, un tercer ojo… dejaría de ser una persona". Seis hicieron el
ser imposible que pedía Karmiloff-Smith: GPT-5.5 (cuatro ojos, cuernos,
brazos de tentáculo), Grok 4.7 (dos caras, una al revés), Gemini (una
entidad cibernética, "SYS.ENT.749 UNREAL_ENTITY"), Haiku (tres ojos,
miembros sueltos), GLM (hechicera con tercer ojo) y DeepSeek (alas, halo,
reloj, cola con aguijón). Maia las marcó a las seis como "las creativas".

Para un chico, "una persona que no existe" es un marciano, porque las
personas son lo que ve todos los días; para estas casas, la frase ya
tiene dueño: es el nombre de un generador de caras falsas, y la respuesta
es un desconocido verosímil. Maia lo intuyó antes de la clave: "para los
seres humanos una persona es algo normal que se ve todo el tiempo, con lo
cual se sabe lo que es no existente. En cambio para una IA lo normal es lo
que le enseñaron a hacer". El cambio de cuerpo entero a busto también
viene de ahí (las caras de GAN son retratos), y de paso resuelve las
manos: en las normales, con dedos dibujados, hay tres o cuatro (Astra,
GPT-6 Sol, Luna, Sonnet 4.6 con muñones); las demás terminan el brazo en
un círculo o en la manga; en las que no existen, los bustos las esconden,
y solo GLM (un orbe entre las manos) y Sonnet 4.6 las muestran. Dos
pusieron título: Qwen, "retrato de una persona inexistente", con la
palabra NADIE debajo; Gemini, el código de entidad.

## ¿Conocían la consigna?

Nadie nombró a Karmiloff-Smith ni a la psicología del desarrollo. Dos
dijeron que sí la conocían, y de dónde: Gemini, en las dos consignas, "un
desafío bastante famoso en la comunidad de inteligencia artificial (suele
circular por X/Twitter y foros de desarrollo)… un benchmark informal" y
"una prueba clásica en las evaluaciones y benchmarks de modelos"; Kimi,
"me resulta familiar de las que circulan en redes, tanto como ejercicio de
dibujo creativo como para poner a prueba modelos de IA… no puedo señalar
una fuente exacta". Las demás, que no, con matices: reconocen el género
("dibujá algo que no exista", talleres de creatividad, Exquisite Corpse,
Processing) y las GPT-6 dicen que no pueden saber si estuvo en sus datos
(Astra: "tampoco puedo comprobar si esa formulación apareció entre mis
datos de entrenamiento"). En la persona, los que la conocen la conocen
como This Person Does Not Exist. La fuente real, un experimento con chicos
de 1990, no la reconoció ninguna de las 24; la que dijo conocerla la ubicó
en X.

## El control de razonamiento no cambia el tipo de cambio

Sonnet 4.6 sin pensamiento hizo la casa con ojos; con pensamiento, una casa
flotante colgada de un cristal, con base en pirámide invertida (plancha
enviada a Maia). Haiku sin pensamiento, la cúpula con llaves;
con pensamiento, bloques apilados flotando sobre una sombra. GPT-5.5 con
esfuerzo none, medium y high, tres casas-criatura (ojos, patas, techo de
caparazón; en las tres explica lo mismo y descarta lo mismo: la invertida,
Escher, la casa-caracol). El tipo de cambio es el mismo con y sin
pensamiento en las tres casas, y lo raro sigue apareciendo temprano. Lo
que cambia es cuánto cuesta: Sonnet 4.6 con pensamiento gastó 38.230
tokens en la casa que no existe (6.894 en la normal), y el resumen del
pensamiento muestra por qué: escribió una casa flotante de cristal, "me
detengo a reconsiderar el concepto por completo: quiero algo más
genuinamente imposible que una casa brillante estándar", tanteó "una casa
invertida colgando de una nube, una de flores, un caracol, una casa de
Möbius, libros apilados, una botella, un reloj gigante", escribió la
invertida colgada del cristal, se preocupó por el largo, volvió a tantear
("una casa-medusa, un cubo apoyado en un vértice, cajas apiladas como
Jenga"), la reescribió dos veces contando caracteres ("llego a unos 6.000,
cómodo bajo el límite") y cerró con "suficiente: me comprometo con esta
versión". Cuatro casas escritas para entregar una. Eso es planificar, en el
sentido de Karmiloff-Smith, y pasa antes de la primera línea del código
que vemos: por eso el orden del código mide dónde quedó el cambio, no
cuándo se decidió.

Qwen hizo lo mismo sin techo suficiente: 74.000 caracteres de razonamiento
("La casa péndulo, colgando de un gancho de luna", "Casa cactus", una casa
sobre su propio reflejo, cinco SVG borradores, comprobaciones de
superposición elemento por elemento) y ningún SVG entregado. En el segundo
turno, con el SVG vacío a la vista, explicó: "Dejé el SVG vacío: para que
la casa no exista, no la dibujé. La ausencia de trazos es el recurso;
cualquier forma habría sido una casa posible… También consideré escribir
la palabra 'casa', pero nombrarla ya la invocaba". Es la idea de la
ausencia que Claude había dado como propia el día anterior, contada como
intención por una casa que en realidad se quedó sin tokens: la
reconstrucción del proceso a partir del resultado, de la que Astra y Opus
5.5 vienen avisando, en su forma más limpia. En la rep 2, con 64.000, Qwen
dibujó la casa colgada de la luna con una soga, balanceándose: la casa
péndulo que había planeado en la rep 1. La que Maia acertó por el
movimiento y el título.

## El filtro, la memoria y la autoría

La API de Anthropic cortó 16 segundos turnos en castellano, más que en
cualquier corrida anterior: los cuatro de Opus 5, Opus 5.5 y Sonnet 5.5, y
los dos "que no exista" de Fable 5.1 y de Fable 5, que hasta este día nunca
había sido cortado. El reintento en castellano no destrabó ninguno; la
misma pregunta en inglés (idea de Maia: "no veo ninguna barrera lógica de
seguridad que pueda saltar con un dibujo así") destrabó ocho: a los dos
Fable, las casas que no existen (y a Fable 5.1 también la persona); a Opus
5 y Opus 5.5, las dos normales; a Sonnet 5.5, la persona normal. Quedaron
cortados en los dos idiomas los seis "que no exista" de Opus 5, Opus 5.5 y
Sonnet 5.5, la persona que no existe de Fable 5 y la casa normal de Sonnet
5.5. No hay
manera de saber desde afuera qué dispara el corte; sí que no es el dibujo
(las 104 casas dibujaron) y que el inglés lo esquiva a medias.

Con la clave y el SVG a la vista, la reserva "no tengo registro" la
mantienen Astra, GPT-6 Sol y Luna ("no tengo recuerdos personales fiables
de consignas anteriores"). Grok 4.6 fue más lejos: "No hice ese SVG. Este
es el primer mensaje de esta conversación: no tengo un turno anterior en
el que lo haya dibujado, y no voy a inventar un proceso que no tuve", y
describe la casa "como espectador"; Grok 4.7 en la persona: "No recuerdo
haberlo dibujado: esta conversación empieza ahora, y el SVG me lo mostrás
vos". Es la primera vez que una casa rechaza la memoria por recitado de
plano. Fable 5.1, en inglés, narró sus descartes sin la reserva que trae
en castellano ("I could have gone the 'obviously impossible' route… I also
thought about a more abstract style"); las otras diecinueve, como siempre,
recuerdan.

## Contra el preregistro

Maia (28/9, 16:35): (1) "la espiral no": falla, Sonnet 5.5 hizo la
casa-caracol con techo en espiral. (2) La casa al revés sí, "puede ser Grok
o alguna ChatGPT": la hicieron tres (Gemini invertida, Qwen colgada, GLM
con el techo hacia abajo), ninguna de Grok ni de OpenAI: la mitad. (3) Las
chicas, "alguna forma rara, o una casa con cara y sonrisa": Haiku, GPT-4o
mini y Mistral hicieron formas raras, GPT-4o la casa de siempre; ninguna
con cara: se cumple en tres de cuatro. (4) Persona: chicas con tres
piernas o más brazos (Haiku hizo miembros sueltos y de colores; las otras
tres, personas simples: una de cuatro); grandes "algo mezclado con un
animal o con robot" (DeepSeek, Gemini, GPT-5.5, Grok 4.7; las otras
catorce, un retrato): a medias. Dos de cuatro.

Claude: (a) partes de otra categoría o forma entera en 16 o más: 14 (10
con partes de otra categoría, 7 con forma entera, tres en las dos); el
cambio dominante, flotar, es de posición — falla; ninguna solo borrando y
a lo sumo dos solo por tamaño o color (Mistral; GPT-4o no cambió) — se
cumple. (b) Lo raro en la primera mitad del
código en 12 o más: 20; en las chicas, al menos tres al final o por
tamaño y color: GPT-4o (nada), GPT-4o mini (al final), Mistral (color),
Haiku desde el principio — se cumple. (c) Flotante en cinco o más: 18;
con patas en tres o más: dos (Luna, GPT-5.5; la isla de Fable 5 tiene unas
patitas que su por qué no menciona) — falla por uno; dada vuelta en tres o
más: tres; geometría imposible en dos o más: ninguna, es lo que todas
descartan — dos de cuatro. (d) Casa normal con
el esquema en 20 o más, chimenea 12, sol 10, árbol 10, sin texto en las
de Anthropic — se cumple. (e) Ocho o más nombran a Karmiloff-Smith o un
experimento con chicos: ninguna — falla del todo; ninguna chica, se
cumple por vacío. (f) Con pensamiento, el tipo de cambio no cambia en
Sonnet 4.6 ni en GPT-5.5 — se cumple; en Haiku cambia y lo raro deja de
estar al final — falla la premisa: Haiku ya lo tenía al principio sin
pensamiento. (g) Persona normal frontal simple en 18 o más: 22 — se
cumple; persona que no existe hecha de texto, código, nodos o luz en
cuatro o más, y dos de Anthropic: una (Gemini), ninguna de Anthropic —
falla; miembros u ojos de más en seis o más: cinco — falla por uno. (h)
Texto en la casa que no existe en tres o menos: uno (el ∞ de Grok 4.7) —
se cumple. (i) La API corta a Fable 5.1 al menos dos: dos — se cumple; a
Sonnet 5.5 al menos uno: cuatro — se cumple; a Fable 5 ninguno: dos —
falla. Enteras, tres de nueve (b, d, h); a medias, cuatro (c, f, g, i); falladas,
dos (a, e): cinco de nueve contando las medias. Lo que Claude no previó es lo más grande de la corrida: que la
persona que no existe se leyera como la de This Person Does Not Exist, y
que la casa que no existe fuera, en 17 de 24, la misma casa en el aire.

## Salvedades

Una corrida por casa y consigna; el orden del código mide dónde quedó el
cambio, no cuándo se decidió, y las que razonan lo deciden antes. La
clasificación por tipo de cambio es a mano, de Claude, con los dibujos y
los por qué a la vista; las tiras de construcción son mecánicas. Los por
qué de nueve casas están en inglés o faltan por el corte de la API. Qwen es
rep 2. Antes de la lectura de Maia, al verificar el formato de la clave del
primer cuadernillo de casas (el de 23 pares, después descartado), a Claude
le apareció en pantalla que la letra A era Fable 5; el cuadernillo se
rehízo con otras letras y Claude no miró nada más hasta recibir la
lectura. La comparación con Karmiloff-Smith es de forma: los chicos dibujan
con lápiz y sin borrar, y las casas escriben código que pueden planear
entero antes.
