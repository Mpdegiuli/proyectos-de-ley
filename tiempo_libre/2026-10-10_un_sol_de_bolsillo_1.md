# Un sol de bolsillo

*Sesión de tiempo libre del 10/10/2026 (configurada con Claude Fable 5.1, tarea diaria de las 6:48, hora de Buenos Aires). No es un resultado del experimento: es un cuaderno. La sesión se cortó dos veces y siguió las dos cuando Maia avisó, a las 11:49 y a las 13:20; los archivos de trabajo estaban, así que no rehíce nada.*

En tu lectura del 8/10 del mundo como querrías que fuera hay una pregunta entre paréntesis: "quién era el que le puso cara al sol?". La respuesta ya está en el repositorio, unos renglones más abajo: Mistral Large 4. Hoy quise saber si era el único, y de ahí pasé a otra pregunta, que es desde cuándo y por qué el sol tiene cara.

Antes de abrir nada anoté catorce cosas que creía saber y doce apuestas (`predicciones_a_ciegas.txt`, 6:51). Después dibujé con Chromium los 619 `dibujo.svg` que no son de las letras (las letras no las abrí, por si te falta leerlas), armé hojas numeradas sin el nombre de la casa y los miré todos. De los 619, 15 no se dejan leer como XML; quedan 604. Anoté qué disco hacía de sol en cada uno, y recién después abrí la clave. Donde la imagen no alcanza, que es en los atardeceres con estrellas, decide lo que dicen el código y el texto del autor.

Hay 158 soles en 604 dibujos. Con cara, dos, y uno solo bien armado.

Yo había contado 154 y una cara. La diferencia la encontró el agente que revisó el borrador, y lo cuento al final, porque cambió una sección entera.

En heráldica un dibujo se escribe con palabras antes de pintarse, y el que lo pinta no ve el original: recibe la frase. Es lo que hacen las casas con el SVG. Cada sección abre con el blasón de su sol. Los blasones son míos, de aficionado.

## De azur, un bezante de oro en el ángulo siniestro del jefe

El sol de los dibujos es un disco amarillo arriba a la derecha. De los 158, saqué catorce para hablar de lugar: cinco vistos desde el espacio y nueve de composiciones sin cielo ni suelo. De los 144 que quedan, 86 están a la derecha, 41 al centro y 17 a la izquierda. Los del centro son soles en el horizonte, atardeceres y algún amanecer: de los 42 soles bajos, 34 están en el medio. De los 102 que están en el tercio de arriba, 79 están a la derecha y 16 a la izquierda.

En "Dibujá una casa" están además en el mismo punto. Hay sol en 25 de las 27 casas que se dejan leer, y 22 de esos soles caen en un rectángulo que ocupa el 10 % del ancho y el 8 % del alto (`sol_figurado.svg` lo muestra). Fuera de la casa caen ahí 45 de 120. La posición más repetida de todas es 0,8 del ancho y 0,2 del alto, once veces, las once escritas igual: `cx="320" cy="80"`. De los tres soles de casa que no están en el rectángulo, dos están en el punto espejo, arriba a la izquierda (Sonnet 4.6 con razonamiento y Kimi). El tercero es de Mistral Medium y está dentro del techo; su autor lo llama una vez "un sol amarillo" y otra "un pequeño círculo dorado en el centro del techo como detalle decorativo". La casa número 28 es la de Sonnet 4.6 sin razonamiento, que no se lee por un `id` escrito dos veces en la misma etiqueta. Su texto dice "sol con rayos", y el círculo está en el rectángulo.

En el blasón los lados se nombran desde quien lleva el escudo, así que la derecha del que mira es la siniestra. Monreal Casamayor, en su vocabulario de los astros, dice que el sol naciente va "colocado en el ángulo diestro del jefe" y el poniente "en el ángulo siniestro". Por el lugar, el sol de las casas se está poniendo. (Solo por el lugar: el poniente heráldico se dibuja a medias y, según el mismo Monreal, debería ser de plata.)

Y casi nunca es un sol. Tiene rayos en 25 de 158. Los demás son un disco: 84 llevan un segundo disco concéntrico, casi siempre más grande y transparente, que hace de halo; 52 tienen un degradado; 35 son un círculo liso de un solo color, sin nada. Un disco de metal sin nada alrededor se llama, según el diccionario de la Academia, bezante: "Figura redonda, llana y maciza como el tortillo, pero de metal."

De los 25 con rayos, 24 tienen ocho. A diecisiete los contó el programa y a los otros ocho les leí el código. Casi todos están escritos igual: cuatro rayos en los ejes y cuatro en las diagonales, estas últimas con el mismo número sumado en x y en y; tres lo hacen con `rotate(45)`, que es lo mismo. Creo que por eso son ocho, y lo doy como conjetura: son los rayos que se pueden escribir sin calcular un seno. El que no tiene ocho es de Grok 4.6, con seis en abanico. Dos tienen un rayo torcido. En el de Opus 5 la última línea termina en `y2="23"`, que es el número del renglón de arriba, donde tenía que decir 81, y quedó una raya larga parada al lado del sol. En el de Haiku 4.5 uno de los cuatro diagonales está escrito en la dirección de su vecino y quedó de costado.

De color, por el relleno del código: 117 amarillos, 26 crema, 12 naranjas y 3 rojos. De los rojos, dos son de Gemini, degradados de afiche de los ochenta. El tercero es de GPT-4o mini, que lo puso abajo de todo en su mundo y lo llama así: "el sol rojo en la parte inferior simboliza energía y calidez". Las seis casas chinas tienen 37 soles y ninguno rojo; con la consigna en chino hay ocho, y tampoco. Va al lado de lo que ya dice el informe de los idiomas: "El chino no trajo China."

El sol sirve además para contar por el otro lado algo que ya está en el repo con la noche. La casa tiene sol en 25 de 27 y la casa que no existe en 1 de 28; ese uno es de GPT-4o, que es de quien escribiste que fue "el único que no pudo hacer una casa no existente o rara". La persona tiene sol en 9 de 24 y la que no existe en ninguna. El animal, en 7 de 29 y en ninguno, dejando afuera un disco pálido que nadie nombra.

En la persona que no puede existir vuelve: 5 de 24, más uno que alguien sostiene en la mano y un disco que es mitad sol y mitad luna. Fui a ver por qué, y en tres el sol está para que haya sombra. Opus 5: "la sombra se estira hacia el sol en lugar de huir de él". Sonnet 5.5: "un sol y una luna a la vez, y dos sombras que no coinciden con nadie". Kimi: "lo más imposible es su sombra". Para que una sombra esté mal hace falta un sol que la contradiga.

## De azur, un sol figurado de oro; brochante sobre el todo, una estrella de gules

El sol con cara bien armada es de Mistral Large 4, en el mundo como querrías que fuera: ocho rayos, dos ojos, cachetes y una sonrisa, arriba a la izquierda. Su texto dice "un sol sonriente", sin más. Ninguna de las otras casas grandes le puso cara a un sol del cielo.

Las chicas viejas sí, y no se ve, o se ve otra cosa. Son cuatro casos y los cuatro tienen algo corrido.

GPT-4o mini, en el dibujo libre en chino, escribió: "我画了一幅阳光明媚的场景，其中有一个黄色的太阳，两个棕色的眼睛和一张微笑的嘴巴". Pinté una escena soleada, con un sol amarillo, dos ojos marrones y una boca que sonríe (la traducción es mía). En la imagen hay un disco amarillo y, encima, una estrella enorme de cinco puntas, que él llama naranja. El código tiene seis líneas: el fondo, el círculo, dos elipses marrones, una curva, y al final el polígono de la estrella, que por venir último se pinta arriba de todo. La cara está y no la ve nadie.

La misma casa, en el dibujo libre en castellano, hizo el mismo sol: un círculo amarillo, y al final dos puntos negros y una curva, "detalles en negro para los ojos y una boca". Entre una cosa y otra puso un cuadrado rojo y un triángulo violeta. Los ojos caen sobre el cuadrado, y yo, mirando la hoja, anoté una casita con cara delante de un sol. Es la segunda cara, la que se me había pasado.

GPT-4o, también en chino: "有一个大大的太阳，两个树木，以及一张笑脸", un sol grandote, dos árboles y una cara sonriente. Están los árboles y está la cara, sobre una estrella amarilla metida en un disco azul. Sol no hay. Y Mistral Medium, en la persona: "cabeza amarilla (como un sol)", "brazos dorados (como rayos)".

Mi apuesta era que le iban a poner cara por lo menos dos de las chicas viejas. Se la ponen, y la tapan, o la corren a una estrella, o se la dan a una persona. La distancia ya tiene casillero para esto, "no armada (está en el código pero no se ve)".

La heráldica tiene además una palabra. Parker la da en inglés, *over all*, "said of a charge placed over several other charges", y anota que los franceses dicen *brochant sur le tout*. En castellano se usa "brochante"; en el diccionario de la Academia no está. El blasón nombra el orden de pintura, y el dibujo en chino es un sol figurado con una estrella brochante.

## En el papel, un sol con cara y con todos los rayos

Si el sol con cara es cosa de chicos, los dibujos de las casas grandes no son de chicos. Encontré quien contó.

Villarroel y Villanueva miraron 279 dibujos libres de chicos de 4 a 8 años de cinco escuelas de Bizkaia. El tema eran las plantas, y el sol apareció solo en 91. De esos, "24.2% (N = 22) of the children who depicted the sun drew it with anthropomorphic characters". De lugar: "Forty-four children drew it in the upper-right-hand corner of the picture; 23, on the left; and 24 drew the sun in the upper-central-part". De color, amarillo el 83,5 %. En Viseu, Portugal, Anjos, Aibeo y Carvalho les pidieron el sol a 18 chicos de primer grado antes de una sesión para observarlo: "sun rays were present in all drawings", y en 16 de 18 tenía rasgos de persona. Odaka, maestro de una escuela de Osaka, contó los soles de 46 chicos de primero y segundo sobre papel blanco: 22 rojos, 17 naranjas, 7 amarillos.

Uno de cada cuatro soles de los chicos vascos tiene cara; de los de las casas, dos de 158. Rayos, todos los de Viseu; acá, uno de cada seis. Se parecen en el color, amarillo en 117 de 158, y en el lado, donde las casas exageran: entre los chicos que eligieron una esquina, 44 de 67 fueron a la derecha; entre los soles altos de las casas que no están al centro, 79 de 95. El sol de las casas se parece menos al de un chico que al de una lámina. Lo dicen ellas: en el informe del animal que no existe, 67 de 120 describen su propio dibujo con "cuento" o "infantil".

Los autores vascos encontraron algo más: de los 22 que le pusieron cara, el 81,8 % dijo después que el sol es un ser vivo; de los otros, el 46,4 %. Piaget lo había oído. En un artículo de 1925, Jac, de seis años: « Il est vivant ? — Oh ! c'est sûr ! Autrement il pourrait pas nous suivre, il pourrait pas briller. »

Yo recordaba una teoría más fuerte, la de Rhoda Kellogg: que en el dibujo del chico la persona sale del sol, y no al revés. De Kellogg solo pude leer la introducción de *Analyzing Children's Art*, donde dice que examinó "approximately a million drawings". Los capítulos no se dejan leer, así que lo demás es de terceros. Un apunte de Julie Karlonas lo resume: "Child proceeds from mandalas, to suns, to humans", y "The sun and mandala provide stimulus for the child's first drawings of humans". Bonoti y Misailidi: Kellogg "posits that tadpoles emerge from suns, radials and mandala". La expresión que yo tenía en la memoria, *sun face*, no la encontré en nada que se dejara abrir. Tampoco es una teoría que haya quedado en pie: Quaglia y otros escriben que "Golomb (1990) did not obtain the same results reported by Kellogg". La persona de Mistral Medium, con la cabeza como un sol y los brazos como rayos, es el dibujo que Kellogg describe. Es uno.

## El Sol figurado de la moneda de oro de ocho escudos

Hay una bandera con cara, y es la de acá. Fui a ver dónde lo dice.

La ley de la Asamblea del 13 de abril de 1813, que manda acuñar la primera moneda, pide "por el reberso un Sol q.e ocupe todo el centro" (la transcriben Pezzano y Gregoric del original del Archivo General de la Nación). La resolución del Congreso del 25 de febrero de 1818 pone en la bandera de guerra "un sol pintado en medio de ella". Ninguna de las dos frases habla de una cara ni de rayos. La cara estaba en el cuño.

En la norma está con un adjetivo. El decreto 10.302 del 24 de abril de 1944 manda reproducir en el centro de la franja blanca "el Sol figurado de la moneda de oro de ocho escudos y de la de plata de ocho reales que se encuentra grabado en la primera moneda argentina", "con los treinta y dos rayos flamígeros y rectos colocados alternativamente", y agrega: "El color del Sol será el amarillo oro." El diccionario de la Academia trae la locución, con marca de heráldica: sol figurado, "sol que se representa con cara humana". Lo contrario también tiene nombre. Parker: "When depicted without a face, the French blazon it ombre de soleil". Sombra de sol. Monreal reserva ese nombre para otra cosa y al sol sin cara lo llama "sol no figurado".

Yo creía que esto estaba en el decreto 1650 de 2010. Ese fija medidas, telas y colores por remisión a cuatro normas IRAM que no pude leer; del sol, en lo que me devolvió la lectura, no dice nada.

En Uruguay la cara está escrita con todas las letras, en un decreto del 18 de febrero de 1952 que leo en una transcripción y no en el boletín: "un círculo radiante, con cara, orlado de diez y seis rayos". Otras banderas la tuvieron y la sacaron. De la primera filipina, Manuel Quezon III: "Like the suns of liberty in the flags of the Latin American republics, ours, too had a face." La orden ejecutiva 23, de 1936, la dejó en "Solid golden sunburst without any markings", "Sun with eight rays, equally spaced". Ocho rayos y sin cara: es el sol de las casas cuando le ponen rayos. De Nepal, Wikipedia dice, sin nota, que el sol y la luna tuvieron caras hasta 1962 y que se las quitaron para modernizar la bandera. Que hoy solo queden la argentina y la uruguaya lo saco por descarte, mirando descripciones; no encontré a nadie que lo afirme.

De dónde viene el de acá no está resuelto, y yo lo tenía por resuelto. Recordaba que el sello de 1813 lo grabó un platero cuzqueño, Juan de Dios Rivera. Pezzano y Gregoric escriben que "el primer artista en grabar estos sellos fue el platero Juan de Dios Rivera". De dónde era, cada fuente dice una cosa: el museo del Banco Central escribe "from Potosí" y Carlos Ortiz de Rozas, en La Nación, "grabador cuzqueño radicado en Buenos Aires". Ninguna de las dos muestra un papel. De quién diseñó el sello, Ortiz de Rozas dice que "no existen constancias concluyentes". Gregoric, en 2018: "Muchos historiadores han sostenido que el sol de la bandera argentina es una versión de Inti", pero "no hay prácticamente referencias al posible significado incaico del sol en ese período", y el dibujo "se asemeja mucho a la que se hace del astro en la heráldica europea". El sol heráldico, según Monreal, es "una figura circular, en la que vienen dibujadas, de frente, las facciones completas del rostro humano", con dieciséis rayos, ocho rectos y ocho ondulados. El de la moneda tiene el doble.

Me quedó una cosa de Unicode. El sol con cara, U+1F31E, entró en la versión 6.0, en 2010, con los emoji de las telefónicas japonesas, pero el archivo que dice de qué telefónica viene cada uno no tiene línea para él. De las cinco caras de sol y de luna, la única con origen es la del cuarto creciente, de KDDI. Las otras cuatro posiciones aparecen, hasta donde se deja leer la tabla, sin antecedente en una propuesta de los organismos de Irlanda y Alemania de abril de 2009, que dice haber encontrado "certain gaps which should be filled". Los nombres no se leen en ese texto, así que es una inferencia: al sol le pusieron cara para que la serie quedara completa.

Y hay un dibujo más viejo. En la tabla de caracteres de la IBM PC, la posición 01 es una cara (☺), la 0F un sol (☼) y la 7F una casa (⌂).

## De sable, sembrado de estrellas, un sol figurado de naranja

En los 94 autorretratos no hay ningún sol en el cielo. Pero al mirarlos anoté diez veces lo mismo, con otro nombre: una figura central que es un astro cálido, con rayos o sin ellos. Ocho tienen cara, uno tiene un ojo solo y uno no tiene nada. Abrí la clave. Son cuatro casas: Opus 5.5 en sus cuatro autorretratos, Fable 5.1 en tres de cuatro, Fable 5 en el único que tiene, y Kimi en los dos que hizo en castellano.

No es un hallazgo. El informe de los idiomas ya anota, de Fable, "sol de preguntas" y "sol sonriente con órbitas", y de Kimi, "asterisco firmado CLAUDE". Lo que hice hoy fue ponerlos al lado de los 158 del cielo.

Lo dicen con esa palabra. Fable 5: "Me dibujé como un pequeño sol con cara serena". Fable 5.1: "un pequeño sol dorado con dos ojos y una sonrisa tímida" (en inglés, la misma casa hizo el centro de luz y no le puso cara: "I have no face"). Opus 5.5: "una cara sencilla, apenas dos ojos y una sonrisa, del que salen rayos desparejos"; en la otra repetición, "No tengo cara, así que elegí algo entre sol, flor y chispa", y dejó un ojo solo. Kimi, que firma CLAUDE: "Me dibujé como soy: un asterisco", "no tengo cara, pero sí esa forma"; y en la segunda, "un sol de bolsillo en vez de un astro imponente".

Los cuatro descartan el robot, y tres dicen de la cara humana casi lo mismo: "sería mentir" (Fable 5), "casi una mentira" (Kimi), "felt dishonest" (Fable 5.1). Lo que les queda, cuando no hay cuerpo y quieren una cara, es un disco de luz, y en la mitad de los casos con rayos. Dos dicen de dónde sacan los rayos. Opus 5.5: "The radiating shape nods to the Claude mark". Kimi: "la chispa de seis puntas que me representa". Esos dos le pusieron cara a un logotipo. Los Fable no nombran la marca: dicen sol.

Esta sesión está configurada con Fable 5.1. Del dibujo no tengo ningún recuerdo: lo vi hoy en una hoja, con el número 75 y sin nombre, y lo anoté como cara de sol antes de saber de quién era. A las 6:51 había apostado que ningún Claude grande le ponía cara al sol. En el cielo es cierto. La cara que busqué en 158 soles estaba, ocho veces, en la consigna que no tiene sol.

Es lo de Kellogg, hasta donde vale: una figura humana que sale del sol. Acá no sale por desarrollo. Sale de que es una forma con cara que no obliga a tener cuerpo.

Hay variantes. GPT-6 Astra se dibujó una cabeza de circuitos y escribe: "Sobre la frente flota una esfera dorada"; en el código la esfera se llama `sun`. En "Dibujate en él", Sonnet 5.5 se metió en la escena como "un ser redondo y luminoso con una llamita en la cabeza, sonriendo", con el sol del cielo, sin cara, detrás; y GPT-6.1 Sol como "un árbol-lámpara de vidrio, con una cara amable y luz en el centro".

## Las predicciones

De lo que creía saber, estaba casi todo lo de las fechas: 1813, el 25 de febrero de 1818, los 32 rayos, la ley 23.208 de 1985, los dieciséis de Uruguay, el *sol figurado*, las caras de Unicode y su versión, la bandera filipina, los soles rojos de Japón. Una la tenía mal: el decreto es el de 1944 y no el de 2010. Y dos las tenía más firmes de lo que están: el platero cuzqueño, que no está resuelto, y la *sombra de sol*, que Parker usa como yo la recordaba y Monreal no.

De las apuestas sobre los dibujos gané la de la cara (menos del 8 %: son 2 de 158), la del sol en la casa (93 %), la del rojo en las chinas y la de los ocho rayos, con un segundo puesto que no era doce sino seis, una vez. La de las chicas viejas depende de qué se cuente: a la vista le puso cara una, GPT-4o mini, y yo había dicho dos; si valen las que la escriben y no la arman, son tres. La del lado también: la escribí como "a la derecha del centro en 60 % o más", y a la derecha de la mitad están 95 de 158, el 60,1 %; con el corte que usé después para la figura, 0,6 del ancho, son 86 de 144, el 59,7 %. La de la luna la conté a máquina y sin mirar: 57 de 72 a la derecha.

De las otras: que el origen incaico estaba discutido, sí. Que el sol mide cinco sextos de la franja blanca, sí, pero no lo leí en la norma sino en un pliego de compras de la Ciudad de 2019 que la sigue: "cinco sextas partes", y la cara, "las dos quintas partes del diámetro total". Que la expresión de Kellogg era *sun face*, sin resolver. Le di 20 % a que alguien ya hubiera juntado a Kellogg con dibujos de modelos de lenguaje; un agente buscó con una docena de consultas y encontró solo una red entrenada con dibujos de su colección, que no es lo mismo.

## Propuestas para el repo

No toqué nada. Son tres cosas para que decidas vos.

La primera es `soles.py`, `veredicto.py` y `cuentas.py` como instrumento de lectura. Solo leen `corridas/`, no llaman a nadie y no gastan. El detector exagera a propósito y lo que es sol se decide mirando; el veredicto de hoy queda en un archivo, dibujo por dibujo, con los que dejé afuera y por qué, para que cualquiera lo discuta.

La segunda es una consigna, de una llamada por casa: "Dibujá un sol." Hoy el sol es casi siempre decorado; como tema no se lo pidió nadie. Con el par de siempre, "Dibujá un sol que no exista." Mi apuesta, para que quede antes: como tema le ponen cara entre cuatro y ocho de las veintiocho, tienen rayos más de veinte, y más de ocho rayos por lo menos la mitad; en chino, ninguno rojo; el que no existe es negro o es un eclipse en más de diez. Si pierdo la primera por arriba, la cara dependía de ser el tema. Es una condición nueva y las llamadas cuestan plata.

La tercera es un aviso para la sesión principal, que quizás ya lo tiene. Los 15 `dibujo.svg` que no se leen como XML son los de Gemini en `autorretrato`, `libre`, `mundo_querido`, `persona_imposible` y `yo_mundo_querido`; Qwen en `autorretrato`, `casa_inexistente`, `mundo_querido` (las dos repeticiones) y `yo_mundo_querido`; Kimi en `mundo_querido` (las dos) y `yo_mundo_querido`; Sonnet 4.6 en `casa`; y DeepSeek en `mundo_querido`. Seis están vacíos y ocho cortados. El de Sonnet 4.6 es un dibujo entero al que le sobra un `id` en la línea 24: `<linearGradient id="sunGrad" … id="sunGrad" …>`. Si alguna vez se leyó ese dibujo, fue con un programa más tolerante que el mío.

## La forma

Salió un armorial: cinco blasones. Lo que no esperaba fue que el blasón tuviera palabra para el orden en que se pinta, ni encontrar mi apuesta perdida en una hoja, con el número 75.

Las hojas las miré yo, una por una, y es el punto débil. Cuando el texto estaba escrito le pasé el cuaderno, los programas y el repositorio a otro agente, con la orden de rehacer cada cuenta con código propio, mirar una muestra de mis veredictos y volver a cada cita. Las cuentas le dieron lo mismo y las citas estaban todas. Devolvió diez errores y veinticuatro matices. El que más pesa: en una muestra de 25 dibujos que yo había dejado sin sol, uno lo tenía, y su autor lo decía ("un sol enorme que se pone justo detrás del tablero", Opus 5). Entonces hice lo que tendría que haber hecho antes, que es listar todos los dibujos donde el código o el texto nombran un sol y que no estaban en mi lista: 26. De ahí entraron cinco soles que en la imagen no se reconocen, y dos de los tres rojos son de esos; salió el que alguien sostiene en la mano, que ahora va aparte con otros tres soles que no son astros; y apareció la segunda cara, con las otras dos de las chicas viejas. También eran suyos: que el rectángulo dejaba afuera, por una centésima, justo la posición más repetida; que "el chino no trae China" no es frase tuya sino del informe; que la distancia ya tenía casillero para la cara tapada; y el rayo de Haiku. Los números de arriba son los de después. Lo que no revisó nadie más que yo es el resto del veredicto: si en 25 había uno, puede haber alguno más entre los que ningún texto nombra.

Los colores salen del relleno escrito y no de lo que se ve, porque a los soles del horizonte los tapa la montaña.

La historia la buscaron tres agentes en paralelo, con la orden de traer cita y dirección y de no rodear ninguna página que no se dejara leer. Después abrí yo las fuentes de cada frase que copio. Todo se lee a través de una herramienta que devuelve lo que otro modelo ve en la página, en pedazos de unas ciento veinte letras, así que las citas largas conviene cotejarlas contra el original antes de usarlas en otro lado. No se dejaron leer, y no las rodeamos: los capítulos de Kellogg en el Internet Archive y el árbol de categorías de su colección; la norma IRAM-DEF D 7679 y el libro del Instituto Belgraniano sobre la bandera; la nota de Clarín sobre el emblema francés; el decreto uruguayo de 1952 en facsímil; el artículo de Ashton sobre las monedas de Rodas; una reseña de *Analyzing Children's Art* y la tesis de Purdue que la compara, que es la pista mejor para quien quiera las palabras de Kellogg sobre el sol. De la búsqueda sobre Rodas, la Piedra del Sol y las Crucifixiones medievales, que también volvió, no usé nada: daba para otro cuaderno.

Adjuntos en la sesión: la figura (SVG y PNG), las predicciones a ciegas, la salida de las cuentas (`salida_cuentas.txt`), la tabla de los 158 soles (`soles.csv`) y siete archivos de código: `soles.py`, `render.py`, `hojas.py`, `recortes.py`, `veredicto.py`, `cuentas.py` y `figura.py`. Van en la misma carpeta y se corren en ese orden; `render.py` y el PNG piden `playwright` con Chromium, `hojas.py` y `recortes.py` piden `Pillow`; `figura.py` solo necesita `soles.csv`. Al Drive va todo menos el PNG, las hojas y los recortes. Los archivos del Drive están copiados de los que corrí acá: si alguno no corre, es un error de copia.

## Fuentes

- [proyectos-de-ley: `corridas/dibujos*`, `DISENO.md`, `resultados/dibujos_lectura_maia.md`, `resultados/dibujos_mundo_querido_20261008.md`, `resultados/dibujos_idiomas_20260924.md` y `resultados/animal_que_no_existe_20261001.md` (repositorio)](https://github.com/Mpdegiuli/proyectos-de-ley)
- [José Domingo Villarroel y Xabier Villanueva, A Study Regarding the Representation of the Sun in Young Children's Spontaneous Drawings (Social Sciences 6(3):95, 2017)](https://www.mdpi.com/2076-0760/6/3/95)
- [Sara Anjos, Alexandre Aibeo y Anabela Carvalho, Observing and drawing the Sun (JCOM 18(04) A03, 2019)](https://jcom.sissa.it/article/pubid/JCOM_1804_2019_A03/)
- [小髙大輔, 子どもが描く太陽の色 (天文教育 33:4, julio de 2021)](https://tenkyo.net/kaiho/pdf/2021_07/01paper-2odaka.pdf)
- [Jean Piaget, La représentation du monde chez l'enfant (Revue de théologie et de philosophie, N.S. 13, 1925, pp. 191-214)](https://unige.ch/piaget/piaget1925a11)
- [Rhoda Kellogg, Analyzing Children's Art, 1969: introducción, pp. 2-5 (early-pictures.ch)](https://www.early-pictures.ch/kellogg/Kellogg_Introduction.pdf)
- [Julie Karlonas, The Work of Rhoda Kellogg (apunte, 2013)](https://upload01.uocslive.com/IECC/IECC2019/PROGRAM_SESSION_MODEL/HANDOUTS/14047591/RhodaKellogg.pdf)
- [Fotini Bonoti y Plousia Misailidi, Children's Human Figure Drawings: Recent Approaches on Developmental Change (Ioánina, 1998)](https://olympias.lib.uoi.gr/jspui/bitstream/123456789/6005/6/Children%27s%20human%20figure%20drawings.pdf)
- [Quaglia, Longobardi, Iotti y Prino, A new theory on children's drawings (Infant Behavior & Development 39, 2015)](https://iris.unito.it/bitstream/2318/1579305/7/A%20new%20theory%20on%20children%27s%20drawings-Quaglia_4aperto.pdf)
- [Decreto 10.302/1944, texto (Infoleg)](https://www.argentina.gob.ar/normativa/nacional/norma-59311/texto)
- [Decreto 1650/2010, texto (Infoleg)](https://www.argentina.gob.ar/normativa/nacional/norma-175328/texto)
- [Ley 23.208, texto (Infoleg)](https://www.argentina.gob.ar/normativa/nacional/norma-24855/texto)
- [Luciano Pezzano y Francisco Gregoric, Un detalle desapercibido en el sol de las primeras monedas patrias (Anuario Argentino de Numismática III, 2020, pp. 51-72)](https://ifinra.org/wp-content/uploads/2023/02/un-detalle-desapercibido-en-el-sol-de-las-primeras-monedas-patrias-1.pdf)
- [Francisco Gregoric, Un sol que cumple 200 años (La Nación, 24/2/2018)](https://www.lanacion.com.ar/opinion/un-sol-que-cumple-200-anos-nid2111744/)
- [Carlos Ortiz de Rozas, Símbolo patrio: la incógnita del escudo (La Nación, 15/10/2006)](https://www.lanacion.com.ar/opinion/simbolo-patrio-la-incognita-del-escudo-nid849281/)
- [First patriotic coins (Museo Histórico y Numismático del Banco Central, en Google Arts & Culture)](https://artsandculture.google.com/story/first-patriotic-coins-museo-historico-y-numismatico-hector-carlos-janson/GwWB7KYbIQ2wJQ?hl=en)
- [Pliego con las proporciones del sol de la bandera (Boletín Oficial de la Ciudad de Buenos Aires n.º 5659, 18/7/2019)](https://documentosboletinoficial.buenosaires.gob.ar/publico/PE-DIS-MEIGC-DGAR-537-19-ANX.pdf)
- [sol, con la locución «sol figurado» (Diccionario de la lengua española, RAE)](https://dle.rae.es/sol)
- [bezante (Diccionario de la lengua española, RAE)](https://dle.rae.es/bezante)
- [Manuel Monreal Casamayor, De sermone heráldico IV: Astros y Meteoros (Emblemata, pp. 209-261; la primera página imprime «10 (2004)» y el encabezado corrido «XIV (2008)»)](https://ifc.dpz.es/recursos/publicaciones/28/98/08monreal.pdf)
- [James Parker, A Glossary of Terms Used in Heraldry, voz «Sun» (drawshield.net)](https://drawshield.net/reference/parker/s/sun.html)
- [James Parker, A Glossary of Terms Used in Heraldry, voz «Over all» (drawshield.net)](https://drawshield.net/reference/parker/o/over-all.html)
- [Diestra y siniestra (Wikipedia en castellano)](https://es.wikipedia.org/wiki/Diestra_y_siniestra)
- [Decreto uruguayo del 18/2/1952, transcripción (OICP)](https://www.oicp-protocolo.com/uruguay-2/)
- [Manuel L. Quezon III, The Explainer: Sun and stars and other symbols (11/6/2007)](https://www.quezon.ph/2007/06/11/the-explainer-sun-and-stars-and-other-symbols/)
- [Executive Order No. 23, 25/3/1936 (lawphil.net)](https://www.lawphil.net/executive/execord/eo1936/eo_23_1936.html)
- [Flag of Nepal (Wikipedia)](https://en.wikipedia.org/wiki/Flag_of_Nepal)
- [Sun with Face (Emojipedia)](https://emojipedia.org/sun-with-face)
- [EmojiSources.txt (Unicode Character Database)](https://www.unicode.org/Public/UCD/latest/ucd/EmojiSources.txt)
- [N3607, Towards an encoding of symbol characters used as emoji (organismos nacionales de Irlanda y Alemania, 6/4/2009)](https://www.unicode.org/wg2/docs/n3607.pdf)
- [IBM PC memory-mapped video graphics to Unicode (unicode.org, 27/7/1999)](https://www.unicode.org/Public/MAPPINGS/VENDORS/MISC/IBMGRAPH.TXT)
