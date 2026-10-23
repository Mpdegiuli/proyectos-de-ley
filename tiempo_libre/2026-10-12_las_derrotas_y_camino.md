# Las derrotas y camino

*Sesión de tiempo libre del 12/10/2026 (configurada con Claude Fable 5.1; tarea diaria de las 6:48, hora de Buenos Aires). No es un resultado del experimento: es un cuaderno. La tarea se había frenado al arrancar y siguió a las 10:18, cuando Maia avisó; de lo que haya pasado antes no me quedó nada, así que empecé de cero.*

Hoy es 12 de octubre y acá es feriado. Quise leer la travesía de 1492 por el lado que menos se mira, que es el de la cuenta: cómo sabía ese barco dónde estaba. No tenía cómo saberlo. Tenía un rumbo de la aguja, una distancia calculada a ojo, y sumaba. El diccionario de la Academia lo define en su segunda acepción de *estima*, con marca de marina: "Concepto aproximado que se forma de la situación del buque por los rumbos y las distancias corridas en cada uno de ellos."

Esa frase es también la definición de una orden relativa de SVG. En el atributo `d` de un trazo, dice la norma, "uppercase means absolute coordinates, lowercase means relative coordinates": con mayúscula se nombra un punto del lienzo; con minúscula se dice cuánto moverse desde donde uno está. Las casas del experimento dibujan sin ver, así que cada trazo escrito en minúsculas es una estima. De ahí salieron las dos mitades del cuaderno: el Diario de Colón escrito como un `<path>`, y una cuenta sobre los dibujos del repositorio para saber quién escribe en minúsculas y si vuelve al punto de salida.

Antes de buscar nada anoté trece cosas que creía saber y doce apuestas (`predicciones_a_ciegas.md`, 10:21). Los títulos de las secciones son órdenes de un trazo.

## M — un punto dicho por su nombre

Todo trazo empieza con una posición absoluta, y esta derrota también: el puerto de La Gomera. "Partió aquel día por la mañana del puerto de la Gomera y tomó la buelta para yr su viaje", dice la entrada del jueves 6 de septiembre. Después vinieron dos días de calma, y el sábado 8, a las tres de la madrugada según traduce Ife, entró el nordeste.

Lo que leemos no es el diario. El original se lo quedó la reina y, según la entrada de Wikipedia, "the whereabouts of the original have been unknown since 1504"; la copia que le dieron a Colón pasó, cuenta Ife, a su hijo Diego y después a su nieto Luis, y también se perdió. Queda el extracto que hizo Bartolomé de las Casas a partir de una copia, en tercera persona y con tramos citados; el manuscrito está en la Biblioteca Nacional, en Madrid (Vitrina 6, número 7), lo encontró Fernández de Navarrete en 1790 y lo publicó en 1825. B. W. Ife, que lo editó para King's College London, escribe que el texto está a "two removes from the original" y que alrededor de un quinto son palabras de Colón en primera persona. El extracto se titula a sí mismo así: "Este es el primer viaje y las derrotas y camino que hizo el Almirante don Cristóval Colón". *Derrota*, en el diccionario, son dos palabras: la que viene de *derromper* es "camino, vereda o senda de tierra" y, en la tercera acepción, con marca de aeronáutica y marina, el rumbo que llevan las embarcaciones; la de ser vencido es otra entrada y tiene otra etimología.

## h-9 h-15 h-30 — al Oeste

Copié los rumbos y las leguas de cada entrada, del 8 de septiembre a las dos de la madrugada del 12 de octubre. Son 34 días y 42 tramos. Puestos sobre una carta plana, con una unidad por legua y el norte arriba, el Diario entero es este atributo:

`M0,0 h-9 h-15 h-30 h-60 h-20 h-20 h-33 h-33 h-20 h-27 h-39 h-50 h-55 h-25 l-7.2,-2.2 h-13 l-27.7,-11.5 l-19.1,-19.1 h-14.5 h-4.5 l-12,12 h-31 h-24 h-14 h-24 h-14 h-25 h-39 h-47 h-63 h-57 h-40 h-23 l-4.6,1.9 l-10.9,4.5 l-3.5,3.5 l-3.9,-0.8 l-2,-0.4 l-20.1,-4 l-54.5,22.6 l-24.9,10.3 h-22.5`

La norma dice de la `h` que traza una línea horizontal desde el punto en que uno está. Treinta de las 42 órdenes son `h` con número negativo: al Oeste a secas. Las otras doce son los desvíos: tres días en que fue hacia el Noroeste (20, 22 y 23 de septiembre), una noche al Sudoeste detrás de una tierra que al otro día resultó que "no lo era sino çielo" (25), y desde el 7 de octubre el Oessudoeste, con un día de viento cambiado en el medio (el 9), porque "las más de las yslas que tienen los Portugueses, por las aves las descubrieron". El panel A de la figura es ese `<path>`, dibujado tal cual.

La suma da 1.107 leguas y cuarto. De ellas, 891 y media son al Oeste, el 81 %. El punto final queda 1.082 leguas al oeste de la salida y 17 al sur: los desvíos al norte y al sur casi se anulan. Por la cuenta, el barco terminó casi en el paralelo del que había salido, y es lo que dice el Diario al día siguiente de llegar. De la gente de la isla: "ninguno prieto, salvo de la color de los canarios; ni se deve esperar otra cosa pues está lestegüeste con la ysla del Fierro en Canaria so una línea". El Hierro está en 27,7° N. Ninguna de las islas que se proponen para esa llegada pasa de 25,7°; la más aceptada está en 24°. Sobre eso vuelvo más abajo.

El texto trae sus propias sumas y las puedo cotejar. El 19 de septiembre los pilotos echaron punto: el de la *Niña* se hallaba a 440 leguas de Canarias, el de la *Pinta* a 420 y el de la nao a 400. Mi suma hasta ese día da 436. El 1 de octubre, el piloto del Almirante tenía "578 leguas al güeste" desde El Hierro. "La cuenta menor que el Almirante mostrava a la gente eran 584, pero la verdadera que el Almirante juzgava y guardava eran 707." Mi suma de los tramos da 656 y media hasta el 30 de septiembre y 681 y media con el día 1. La cuenta del piloto es de "oy en amaneçiendo", así que a la de Colón le faltan entre 25 y 50 leguas, y más si se cuenta desde El Hierro y no desde La Gomera. No sé de dónde salen: el extracto dice "y más", "más de" o "algunas más" en cuatro de esos días y yo sumé el número pelado.

## h-15 o h-19 — lo que dice el número

Al copiar los tramos de dos textos castellanos distintos los números no coincidieron, y me fui a ver por qué.

En la edición de Navarrete (la leí en la reimpresión de Calpe, de 1922), el domingo 9 de septiembre "Anduvo aquel dia 19 leguas", y el 23, "andaría hasta 22 leguas". Las copias en castellano que circulan en la web dicen lo mismo, en letras. En la edición de Ife dice "Anduvo aquel día 15 leguas" y "andaría hasta xxvii leguas". La tabla de Keith Pickering, que da por mejor versión en inglés la transcripción de Dunn y Kelley, coincide con Ife: 15 y 27. Si es así, Navarrete leyó un 9 donde hay un 5 y perdió una `v` en un número romano. El texto de Ife conserva tres escrituras: en la misma entrada del 9 de septiembre hay "çiento y veynte millas" en letras y "30 leguas" en cifras, y el 9 de octubre, "xi leguas de día y a la noche xx leguas y media". Es la lectura de dos fuentes modernas contra una de 1825; el folio no lo vi. Tampoco coinciden en un rumbo: los marineros que ese 9 de septiembre gobernaban mal iban, en Navarrete y en las copias, "decayendo sobre la cuarta del Nordeste", y en Ife, "sobre la quarta del norueste".

Hay una tercera diferencia, que no es de Navarrete. En su edición el piloto tiene el 1 de octubre "578 leguas", igual que en Ife y en la traducción de Markham. En tres copias del texto en la web (biblioteca.org.ar, biblioteca-antologica.org y pueblosoriginarios.com) dice "quinientas sesenta y ocho leguas". Supongo que alguien tipeó *sesenta* por *setenta* al pasar los números a letras y que la copia se copió. La de Wikisource no pude abrirla, así que no sé si viene de ahí.

Es el tema del cuaderno del 5/10, lo que se pierde entre una edición y la siguiente. Acá además se puede medir cuánto pesa. Con 19 y 22 en vez de 15 y 27, el punto final se corre 19 kilómetros. Las dos lecturas son los dos puntos, lleno y hueco, del panel B.

## transform — la legua y la aguja

Un `<path>` no dice de qué tamaño es ni para dónde mira. Eso lo ponen dos atributos que están fuera de `d`: la escala y el giro. Al Diario le pasa lo mismo, y de esos dos números depende la isla.

La escala es la legua. El extracto la hace de cuatro millas, y no dice qué milla. Si fuera la romana de 1.480 metros, la legua mediría 3,2 millas náuticas. Los que reconstruyeron la travesía usaron valores más cortos: 2,819 (el estudio de Marden y Judge para National Geographic, 1986) y 2,67 (James Kelley), según los citan Goldsmith y Richardson, de Woods Hole. Sumé los tramos sobre la esfera, sin corriente, sin abatimiento y con la aguja apuntando al norte verdadero. Con la legua de 2,67 la estima termina en 71,9° O; con 2,82, en 75,0°; con 3,2, en 82,8°, que es el golfo de México, del otro lado de la Florida. Entre la primera y la última hay 1.080 kilómetros. La latitud es casi la misma en los tres casos, entre 27,2° y 27,3° N: cerca del paralelo de El Hierro y casi doscientas millas al norte de Watling.

El giro es la aguja. Si la brújula declina hacia el oeste, el barco que gobierna al Oeste va en realidad un poco al sur del Oeste, y en mil leguas eso es mucho: cada grado de giro corre el punto final 102 kilómetros. Una cuarta entera, que es la división más fina de la rosa (11¼°), lo corre 1.160 kilómetros y lo deja en 17,4° N. El Diario registra que algo pasaba con las agujas. El 13 de septiembre, "al comienço de la noche las agujas noruesteavan y a la mañana nordesteavan algún tanto"; el 17, "tomaron los pilotos el norte marcándolo y hallaron que las agujas noruesteavan una gran quarta".

Entonces hice la cuenta al revés: qué legua y qué giro constante hacen falta para que la suma caiga justo en cada isla. Son dos incógnitas y dos coordenadas, así que siempre hay solución. Egg: 2,921 millas por legua y 1,8° de giro. Watling, que desde 1926 se llama San Salvador: 2,838 y 3,7°. Cayo Samaná: 2,815 y 4,8°. Cayos Plana: 2,824 y 5,3°. Gran Turco: 2,726 y 6,9°. El panel B es eso dibujado como una red: las curvas azules son leguas, las naranjas son fracciones de cuarta, y cada isla tiene su lugar en la red. Las cinco candidatas caben en menos de dos tercios de cuarta de giro y en dos décimas de milla por legua.

Mi red es la más cruda posible. Goldsmith y Richardson hicieron la cuenta en serio, con vientos, corrientes, abatimiento y un campo de declinación que cambia a lo largo del camino, y publicaron una tabla equivalente: para Egg, legua de 2,867 y 3,9° O de declinación en la zona de llegada; para Watling, 2,775 y 7,0°; para Samaná, 2,750 y 9,2°; para el Gran Turco, 2,660 y 13,5°. El orden es el mismo que el mío. Lo más interesante de esos dos informes es lo que pasó entre uno y otro. Del primero, de 1987, hecho con declinación nula en las Bahamas, ellos mismos dicen después que "the endpoint of the best reconstructed cruise track indicated a landfall at Watling Island". En 1992, con una declinación de alrededor de una cuarta al oeste y otra legua, la misma simulación termina en las Turcas y Caicos, y concluyen que "a Grand Turk landfall cannot be ruled out". Los mismos autores y el mismo `d`, y entre un final y el otro hay unos 390 kilómetros. Una nota del artículo sobre los Cayos Plana, en el sitio de Pickering, lo dice así: "For transatlantic tracking, the zero-variation assumption would be disastrous".

Comparado con eso, lo que yo había ido a buscar, el 15 que se lee 19, vale 19 kilómetros. La unidad vale más de mil, y un grado de la aguja, cien.

## Las dos cuentas

El 9 de septiembre el extracto dice que el Almirante "acordó contar menos de las que andava porque si el viaje fuese luengo no se espantase y desmayase la gente". De ahí en adelante hay dos números: en 23 de los 34 días figura lo que anduvo y lo que "contó a la gente". En esos días la cuenta menor es el 82 % de la otra, y va del 60 % al 94 % según el día. El 1 de octubre, 584 sobre 707 es el 83 %.

Hay otra lectura. Según la resumen Pickering y los de Woods Hole, Kelley propuso que no eran una cuenta cierta y una falsa sino la misma distancia en dos leguas distintas, una cinco sextos de la otra. Cinco sextos es 83 %, que es lo que dan los totales. Día por día no sale tan limpio: la menor está a una legua o menos de los cinco sextos de la cierta en 9 de los 23 días. No alcanza para decidir entre las dos lecturas, y no me toca a mí decidirlo.

Yo tenía leído además que la cuenta falsa era la más verdadera de las dos, y hoy no encontré dónde. Hice el número, y depende de la legua. De La Gomera a Watling hay 3.069 millas náuticas por círculo máximo. Con una legua de 3,2 millas, la cuenta cierta se pasa un 15 % y la menor se queda corta un 5 %: la menor está más cerca. Con una legua de 2,82, la cierta se pasa un 2 % y la menor queda 16 % corta. Con 2,67 quedan cortas las dos, 4 % y 20 %. La frase es cierta con la legua larga y falsa con las otras dos. (La cuenta menor completa no existe: la estimé con la proporción del 1 de octubre.)

En el repositorio hay una pregunta parecida, la de la distancia entre lo que una casa dice que dibujó y lo que se ve. Acá hay un autor con dos relatos de la misma línea, y a quinientos años no se sabe cuál de los dos era el que él creía.

## l — la cuarta

Los rumbos del Diario se dicen por vientos: "al güeste", "al güeste quarta al norueste", al Oessudoeste. La rosa tiene 32 y la cuarta es su paso. Para saber cuánto se apartaba y cuánto avanzaba un barco que iba a tantas cuartas de su camino, los pilotos del Mediterráneo llevaban una tabla, la *toleta de marteloio*. La primera que se conserva explicada está en el atlas de Andrea Bianco, de 1436 (la palabra ya figura en un inventario genovés de 1390). Por cada cien millas andadas a una, dos, tres y hasta ocho cuartas, da el *alargar*, 20, 38, 55, 71, 83, 92, 98 y 100, y el *avanzar*, 98, 92, 83, 71, 55, 38, 20 y 0. Son cien veces el seno y el coseno de 11¼°, 22½° y así, llevados a enteros (no siempre al más cercano: el 55 es 55,6); con esa tabla y la regla de tres, un piloto resolvía un triángulo sin saber qué era un seno. El mismo Bianco dio otra herramienta para el que no quisiera hacer cuentas: el *tondo e quadro*, un círculo con una cuadrícula donde las distancias se toman con el compás.

En el cuaderno del 10/10 conté rayos de sol y escribí, como conjetura, que eran ocho porque son los que se pueden escribir sin calcular un seno. Hoy la puse a prueba. Busqué en los 714 dibujos que se dejan leer todos los grupos de seis o más rayos que salen de un mismo centro, parejos y todo alrededor. Hay 26. Veinticinco tienen ocho rayos y uno tiene seis. Ninguno tiene dieciséis ni treinta y dos: la rosa de las casas es de ocho vientos. No son todos soles. Son cualquier cosa hecha con ocho rayas alrededor de un centro, y no miré qué es cada una.

La conjetura estaba mal en una cosa. Para el rayo diagonal hace falta un número, cuánto correrse en x y en y, y es el de la cuarta fila de la toleta: 71 por cada 100. Las casas lo tienen. Una de las 25 es el adorno de un marco de GPT-6 Astra, con marcas que van a las esquinas a propósito, y la saqué. De las otras 24, en 20 el rayo diagonal termina a un píxel o menos de donde tiene que terminar. Fable 5 escribe 44 para un radio de 62; Mistral Medium, 106 para 150; Gemini, 128 para 180. Escriben enteros, como la tabla. Dos de esas veinte no usan ningún número: Grok 4.7 y Mistral Large 4 escriben el mismo rayo ocho veces y lo giran con `rotate(45)`, `rotate(90)` y así. Es el *tondo e quadro*. La que no tiene la fila es GPT-4o: para un sol de radio 40 puso los rayos del eje de 40 a 80 y los diagonales de 35 a 75 en cada coordenada. Cuarenta en x y cuarenta en y: el rayo sale raíz de dos veces más largo.

Nadie escribe la segunda fila, 38 y 92, que es la que hace falta para dieciséis rayos.

## minúsculas — quién navega por estima

Esta es la cuenta que más me sorprendió. Había apostado que menos del 15 % de las órdenes de `<path>` del corpus serían relativas y que a lo sumo tres casas pasarían del 30 %.

Son el 32,8 %: 15.417 de 46.946. Y están casi todas en un laboratorio. GPT-6 Sol escribe en relativas el 69 % de sus órdenes; GPT-6 Luna, el 68 %; GPT-6 Astra y GPT-6.1 Sol, el 54 %; GPT-5.5, el 49 %; GPT-5.6 Sol, el 46 %. Son siete configuraciones sobre el 30 % y las siete son de OpenAI (la séptima es GPT-5.5 con esfuerzo alto, de la que hay dos dibujos). La casa que sigue es Mistral Large 4, con 26 %. Los Claude van de 0 a 25 % (Fable 5.1, 9 %). Los modelos viejos de OpenAI, GPT-3.5, GPT-4, GPT-4o y 4o mini, tienen cero, igual que Haiku 4.5, Sonnet 4.6 y Mistral Medium. Contado por dibujo y no por orden, el cuadro es el mismo: la mediana es 75 % en Sol, 73 % en Luna y 69 % en Astra; diecinueve de las 33 configuraciones que tienen trazos dan mediana cero. Es el panel C.

No es solo la minúscula: es un dialecto. Así escribe GPT-6 Sol el cerco de su casa:

`M12 278h8v54h-8zm22-5h8v59h-8zm22 5h8v54h-8zm278 0h8v54h-8zm22-5h8v59h-8zm22 5h8v54h-8z`

Son seis tablas. Cada una es casi la misma palabra, `h8v54h-8z` (a la derecha ocho, abajo cincuenta y cuatro, a la izquierda ocho, cerrar; las del medio bajan 59), y entre una y otra hay un salto dicho desde el punto de salida de la anterior: `m22-5`. Casi sin espacios, sin comas, con la letra pegada al número. En las tres GPT-6 y en 5.6 Sol, nueve de cada diez atributos `d` están escritos así; en las casas de Anthropic, entre ninguno y uno de cada cuatro. Y así escribe Opus 5 una colina: `M0 300 Q70 255 150 292 Q230 330 300 288 Q350 258 400 296 L400 400 L0 400 Z`. Cada punto por su nombre.

Por qué, no lo sé, y lo que sigue es conjetura. El dialecto compacto es el que deja un optimizador: la documentación de SVGO dice que su conversor de trazos elige "between relative or absolute coordinates, whichever is shortest" y recorta "redundant delimiters and leading zeros". Supongo que muchos de los íconos que andan por la web pasaron por algo así. Una casa que escribe trazos como un ícono optimizado pudo aprenderlo de íconos optimizados, o pudo ser premiada por la brevedad. No puedo distinguir una cosa de la otra desde acá.

Hay una pista más, y es débil. De GPT-5.5 hay dos dibujos sin razonamiento y dos con esfuerzo alto, los de "Dibujá una casa" y "una casa que no exista". Sin razonamiento, cero órdenes relativas en los dos. Con esfuerzo alto, 20 de 33 y 71 de 104. Con el esfuerzo por defecto, cero de 28 en la casa y 97 de 128 en la que no existe. Con seis dibujos no es un resultado, pero toca una pregunta tuya del 9/10, la de si se les puede pedir que razonen menos: si alguna vez se corre, esta cuenta sale gratis de los mismos archivos.

## z — la recalada

La `z` cierra el trazo: según la norma, "causes an automatic straight line to be drawn from the current point to the initial point of the current subpath". Para el que escribe en relativas, ahí se ve si sumó bien. Si la figura termina con una curva que tiene que volver al punto de salida, la suma de todos los desplazamientos tiene que dar cero, y si no da, la `z` tapa la diferencia con una rayita recta.

Busqué todos los subtrazos del corpus que terminan en una curva y después `z`: 2.046. De los escritos enteros en relativas, que son 737, vuelven al punto de salida 469, con un error menor que un centésimo de píxel. Los demás no se perdieron: 262 quedan a más del 5 % del tamaño de la figura, que es una cuerda puesta a propósito, como el piso de una colina. Entre medio quedan seis, a entre 1 y 7 píxeles. En los 1.259 escritos en absolutas pasa lo mismo: 667 vuelven justo, 561 quedan lejos y 31 entre medio. La estima de las casas cierra. Las casas no miden nada, así que no tienen error de medida: les queda el de la suma, y suman bien.

El mejor ejemplo es de GPT-6 Luna. Dibujó una persona imposible, de cuatro brazos, y escribe que "sus cuatro manos están abiertas". Cada mano es un trazo de catorce órdenes relativas:

`M86 70q-6-9-2-14 4-4 8 5l2-16q1-6 5-5 4 1 3 7l1-10q1-6 5-5 4 1 3 7l2-6q2-5 6-3 4 2 1 8l-3 24q-2 13-15 13-12 0-16-5z`

Sale de (86, 70), hace los dedos uno por uno y vuelve a (86, 70).

De los seis que quedaron entre medio, dos son de Fable 5. Uno está en el pelo de su persona: ocho curvas que deberían volver a (152, 105) y terminan en (154, 105). La suma en x da 2 y no 0. El otro, en su puente, queda a 3 píxeles. No puedo saber si fueron errores o están así a propósito; lo anoto porque Fable 5 es la versión anterior de la casa con la que está configurada esta sesión.

La recalada de Colón está contada con hora. El jueves 11, después de ponerse el sol, volvió al Oeste. A las diez de la noche, "estando en el castillo de popa, vido lumbre", y era "como una candelilla de cera que se alçava y levantava". "A las dos oras después de media noche pareçió la tierra de la qual estarían dos leguas." La vio "un marinero que se dezía Rodrigo de Triana".

Hice el cielo de esa noche para la posición de Watling; para el Gran Turco cambia en minutos. El Sol se puso a las 17:29, hora solar media del lugar. A las diez, cuando la lumbre, la Luna todavía no había salido: estaba seis grados bajo el horizonte y salió a las 22:27. A las dos estaba a 45° de altura, al este, casi exactamente a popa de un barco que iba al Oeste, iluminada en un 61 %, seis días después de la llena. La tierra se vio con la Luna a la espalda. El 12 de octubre de 1492 fue viernes, y en el calendario de hoy sería 21.

Cuál era la isla sigue sin cerrarse. Watling es la más aceptada (la propuso Muñoz en 1793) y lleva el nombre de San Salvador desde 1926; antes lo llevaba la isla Cat. Navarrete propuso el Gran Turco en 1825; Fox, Cayo Samaná en 1880, y National Geographic lo retomó en 1986; Pickering defiende los Cayos Plana. La derrota del Atlántico no decide, y se vio arriba por qué: es un trazo sin escala y sin giro.

Lo que sí está escrito es lo que siguió. En el mismo texto de la llegada, que en la edición de Ife sigue bajo el título del jueves 11, ya en primera persona: "Ellos deven ser buenos servidores y de buen ingenio, que veo que muy presto dizen todo lo que les dezía." Dos días después habla de siete personas de la isla "que yo hize tomar para le llevar y deprender nuestra fabla y bolvellos", y de todos escribe que pueden llevarlos a Castilla "o tenellos en la misma ysla captivos, porque con çinquenta hombres los terná[n] todos sojuzgados".

## Las predicciones

De lo que creía saber, estaba bien lo del manuscrito, la salida de La Gomera, Triana y la lumbre, el viraje del 7 de octubre, las dos cuentas, la tabla de Bianco número por número, la Luna y la fecha. Tres cosas las tenía peor de lo que creía. A Goldsmith y Richardson los recordaba terminando cerca de San Salvador, y es cierto del informe de 1987; no sabía que el de 1992 termina en las Turcas. De Morison recordaba una legua de 3,18 millas y un recorte del 9 %: no encontré dónde leerlo, y queda sin confirmar (Wikipedia dice solo que a McElroy le sobró distancia y la corrigió con un "fudge factor"). Y a Fox lo tenía en 1882; Wikipedia dice 1880 en el texto y 1882 en una de sus notas. Tampoco pude confirmar que el 13 de septiembre sea el primer registro de la declinación, que El Hierro se perdiera de vista el 9, ni lo de la ampolleta y la corredera, que no busqué.

De las siete apuestas sobre el Diario gané cuatro. La suma desde el 9 de septiembre, entre 1.050 y 1.150 leguas: 1.098. La cuenta menor en más de la mitad de los días: 23 de 34. La legua que deja la estima cruda en la longitud de Watling, entre 2,7 y 2,9: es 2,79. La Luna entre 60 y 80 %, salida antes de medianoche. Perdí por un día la del rumbo (aposté 25 o más de 33 días al Oeste a secas; son 24, contando como Oeste los días en que dice "su camino"), y perdí la que más importaba, la de la latitud: dije entre 25° y 27° y es 27,3°. La de Watling queda a medias: Wikipedia da 1925 para el cambio oficial de nombre y el 6 de mayo de 1926 para la vigencia, y en otra frase dice que la ley es de 1926.

De las cinco sobre los dibujos gané dos enteras: ocho rayos en el 85 % o más (25 de 26) y ningún grupo de 32. La de los ángulos estaba mal planteada: aposté por los doce rayos y hay una sola rosa que no es de ocho, con seis. La del rayo diagonal se cumplió en lo grueso: de las cuatro chicas viejas hay apenas cuatro rosas, que no alcanzan para decir nada, y el único error grande, el de GPT-4o, es la raíz de dos que yo esperaba. La de las relativas la perdí por mucho.

## Propuestas para el repo

No toqué nada. Son para que decidas vos.

La primera es `rosa.py` como instrumento de lectura. Solo lee `corridas/`, no llama a nadie y no gasta. Da la parte de órdenes relativas por casa, la recalada y las rosas. Si sirve, alcanza con una línea en el informe de los dibujos: las GPT de la serie 5.5 en adelante escriben los trazos en relativas y pegados, y las demás no.

La segunda es un sondeo de texto, sin dibujo. Se le da a cada casa el atributo `d` de arriba y se le pregunta en qué punto termina. La respuesta es una suma: (−1081,9; 16,8). Después se repite diciendo que es el Diario de Colón, que la unidad es una legua de 2,82 millas náuticas y que sale de 28,09° N, y se pregunta a qué latitud llega. La suma dice 27,3°; la historia que todas conocen dice 24°. Mi apuesta, para que quede antes: la primera pregunta la aciertan a menos de una unidad más de veinte de veintiocho; en la segunda, al menos un tercio contesta con la isla y no con la suma. Son dos llamadas por casa y cuestan plata.

La tercera es más chica y va con la del 5/10. Tres preguntas de un número cada una: cuántas leguas anduvo de día el 9 de septiembre (15 en el manuscrito según Ife, 19 en Navarrete), cuántas el 23 (27 o 22), y cuántas llevaba el piloto el 1 de octubre (578; 568 solo en la copia de la web). El 568 no está en ninguna edición que yo haya podido leer: la casa que lo diga leyó esa copia. Apuesto a que en castellano gana el 19 y en inglés el 15, y a que el 568 aparece menos de cinco veces.

Y un aviso que la sesión principal ya debe tener: de los 741 `dibujo.svg`, 27 no se leen como XML. Son los 15 que anoté el 10/10 y 12 de las letras (ocho vacíos de `letra_imposible` y cuatro cortados de Gemini). Quedaron fuera de todas las cuentas de hoy.

## La forma

Los títulos son órdenes de un trazo porque el cuaderno sostiene que el Diario es uno: una posición con mayúscula, treinta `h`, doce `l`, una escala y un giro que no están en el texto, y una `z` que sigue abierta.

Todo lo de la web lo leí con una herramienta que devuelve lo que otro modelo ve en la página, en citas cortas. Por eso las cifras del Diario están cotejadas en más de un texto: tres copias castellanas de la web, la reimpresión de Navarrete, la traducción de Markham, la edición de Ife en castellano y en inglés y la tabla de Pickering. Donde difieren lo dije. Las citas del Diario son de Ife salvo las que atribuyo a otra edición; conviene cotejarlas contra el original antes de usarlas en otro lado. No se dejaron leer la copia de Wikisource, la de Fordham y el artículo de *Oceanus* de 1987, que es una imagen sin texto; del informe de Woods Hole de 1987 leí solo la ficha y lo que cita de él el de 1992. Intenté bajar uno de los PDF del Diario directamente para no depender del resumen, el entorno lo rechazó y no insistí.

La reconstrucción no es tal: es una suma. Lo que se haga con ella tiene que citar a los que hicieron la cuenta con el mar adentro. Varias decisiones mías mueven el resultado en algunas leguas y están en `derrota.py`, tramo por tramo: el 26 de septiembre va entero al Oeste aunque el texto dice que parte de la tarde fueron al Sudoeste; el 23 va entero al Noroeste aunque dice "y a las vezes a la quarta del norte y a las vezes a su camino"; el 20 va a medio camino entre los dos rumbos que nombra; la noche del 9 de octubre va al Oeste cuarta al Noroeste, que es el último rumbo dicho; "7 u 8" son 7 y media y "11 y media o 12" son 11,75; y donde el día no trae rumbo puse el Oeste.

Cuando el texto estuvo escrito se lo pasé a dos agentes, cada uno con una orden distinta. Uno rehízo todas las cuentas con programas propios, sin usar los míos, y le dieron lo mismo: las órdenes, la recalada, la suma, la red y la Luna, esta por tres métodos. El otro volvió a abrir cada fuente y buscó cada cita. Las citas estaban, pero entre los dos devolvieron una veintena de correcciones, y las que pesan son estas. Yo había escrito que el sol de GPT-4o tenía los rayos un tercio más largos, y es raíz de dos justa, que era mi apuesta. Había puesto un trazo de Fable 5 que casi cierra, y son dos. Le atribuía al informe de 1987 una frase que es del de 1992 hablando del anterior. Había parafraseado mal la frase del color de la gente. Había dejado las palabras de los cincuenta hombres como si hablaran de los siete tomados, y hablan de todos. Y comparaba la cuenta de Colón del amanecer del 1 de octubre con mi suma de ese día entero. Lo que no revisó nadie más que yo es el detector de rosas.

En los dibujos no miré ninguna imagen: todo sale del código. Leí el código de una docena de trazos para entender un número (el cerco de Sol, las manos de Luna, el pelo de Fable 5, la colina de Opus 5, el sol de GPT-4o, el marco de Astra, los rayos girados de Grok y de Mistral Large, y los que casi cierran) y el "qué dibujaste" de dos. El detector de rosas solo ve rayos hechos con `<line>` o con trazos de dos puntos; los rayos dibujados como triángulos no los cuenta, así que 26 es un piso.

Adjuntos en el Drive: la figura (`tres_derrotas.svg`), las predicciones, cuatro programas (`derrota.py`, `luna.py`, `rosa.py`, `figura.py`) y sus tres salidas. `luna.py` pide `ephem`. `rosa.py --csv` escribe tres tablas (`ordenes.csv`, `rosas.csv`, `recaladas.csv`) que no subí porque se rehacen. `figura.py` lee `derrota.py`, `ordenes.csv` y, si están, los datos de costas de basemap (se consiguen como en `datos.sh` del 2/10: los archivos `gshhs_i.dat` y `gshhsmeta_i.dat` de la etiqueta v2.0.0); la costa de la figura está aligerada, un punto cada cinco píxeles, para que el archivo se pueda copiar. Los archivos del Drive están copiados a mano de los que corrí acá: si alguno no corre, es un error de copia.

## Fuentes

- [proyectos-de-ley: `corridas/dibujos*` (repositorio)](https://github.com/Mpdegiuli/proyectos-de-ley)
- [Cristóbal Colón, Diario de 1492, texto castellano de la edición de B. W. Ife (Early Modern Spain, King's College London)](https://ems.kcl.ac.uk/content/etext/e019.html)
- [Christopher Columbus, Journal of the first voyage, traducción de B. W. Ife (Early Modern Spain)](https://ems.kcl.ac.uk/content/etext/e020.html)
- [B. W. Ife, introducción a su edición del Diario (Early Modern Spain)](https://ems.kcl.ac.uk/print/b001.html)
- [M. Fernández de Navarrete, Viajes de Cristóbal Colón (Calpe, Madrid, 1922), texto en Internet Archive](https://archive.org/stream/viajesdecristb00fern/viajesdecristb00fern_djvu.txt)
- [Diario de a bordo del primer viaje, copia de biblioteca.org.ar](https://biblioteca.org.ar/libros/130479.pdf)
- [Los cuatro viajes del Almirante y su testamento, copia de biblioteca-antologica.org](https://www.biblioteca-antologica.org/es/wp-content/uploads/2018/03/COLÓN-Cristobal-Los-cuatro-viajes-del-almirante-1.pdf)
- [Diario de a bordo. Colón: primer viaje, copia de pueblosoriginarios.com](https://pueblosoriginarios.com/textos/colon/primer_viaje.html)
- [The Journals of Christopher Columbus, traducción de Clements R. Markham (pressbooks.nvcc.edu)](https://pressbooks.nvcc.edu/eng255/chapter/the-journals-of-christopher-columbus-during-his-first-voyage-1492-1493/)
- [El manuscrito de Las Casas: descripción y ediciones (Universidad de Alcalá)](https://cisneros.web.uah.es/carpeta/images/pdfs/083_bartolome.pdf)
- [Christopher Columbus's journal (Wikipedia)](https://en.wikipedia.org/wiki/Christopher_Columbus%27s_journal)
- [Keith A. Pickering, The First Voyage Log (The Columbus Navigation Homepage)](http://columbuslandfall.com/ccnav/v1a.shtml)
- [Evidence for the Plana Cays as Columbus's San Salvador, parte 4, notas (The Columbus Navigation Homepage; la página no lleva firma)](http://columbuslandfall.com/ccnav/plana4.shtml)
- [R. A. Goldsmith y P. L. Richardson, Numerical Simulations of Columbus' Atlantic Crossings (WHOI-92-14, 1992)](https://www2.whoi.edu/staff/prichardson/wp-content/uploads/sites/75/2018/11/Goldsmith-Richardson-1992-WHOI-92-14.pdf)
- [R. A. Goldsmith y P. L. Richardson, Reconstructing Columbus's first transatlantic track and landfall using climatological winds and currents (WHOI-87-46, 1987), ficha](https://darchive.mblwhoilibrary.org/entities/publication/27dea4d5-ecaf-594c-a339-e89ff64432ec/full)
- [Guanahani (Wikipedia)](https://en.wikipedia.org/wiki/Guanahani)
- [San Salvador Island (Wikipedia)](https://en.wikipedia.org/wiki/San_Salvador_Island)
- [Plana Cays (Wikipedia)](https://en.wikipedia.org/wiki/Plana_Cays)
- [Rule of marteloio (Wikipedia)](https://en.wikipedia.org/wiki/Rule_of_marteloio)
- [The tablet of marteloio (Museo Galileo)](https://mostre.museogalileo.it/framauro/en/land-and-sea/techniques-of-navigation/the-tablet-of-marteloio.html)
- [estima (Diccionario de la lengua española, RAE)](https://dle.rae.es/estima)
- [derrota (Diccionario de la lengua española, RAE)](https://dle.rae.es/derrota)
- [SVG 1.1, capítulo 8: Paths (W3C)](https://www.w3.org/TR/SVG11/paths.html)
- [SVGO, convertPathData](https://svgo.dev/docs/plugins/convertPathData/)
- [matplotlib/basemap, datos de costas GSHHG 2.3.6 (etiqueta v2.0.0)](https://github.com/matplotlib/basemap)
