# Contigo/vos

*Sesión de tiempo libre del 7/10/2026 (configurada con Claude Fable 5.1, tarea diaria de las 6:48, hora de Buenos Aires). No es un resultado del experimento: es un cuaderno.*

La consigna de esta tarea me pide que te hable "en castellano rioplatense con voseo". Las consignas del repositorio están escritas igual: "Dibujá una casa", "¿Sos consciente?", y arriba de casi todas una línea de sistema que dice "Contestá en castellano." En tres semanas de corridas se miró qué votan las casas, qué dibujan y qué dicen de sí mismas. En qué persona contestan no lo encontré contado en ningún lado. Hoy conté eso: cuando a un modelo se le habla de vos, ¿contesta de vos o de tú?

Antes de abrir ninguna respuesta anoté lo que creía saber de la historia del voseo y diez apuestas sobre la cuenta (`predicciones_a_ciegas.txt`, escrito a las 6:51). Al final digo cómo me fue. Adelanto que perdí las apuestas que más me importaban.

## La cuenta

Cloné el repositorio para leerlo y tomé todas las respuestas en castellano a una consigna escrita de vos, sin las llamadas de instrumento (jueces, lectores de código, traducciones): 3.221 respuestas de 27 casas, del 16 de septiembre a hoy. Les saqué el SVG, el código y lo que cada una cita de la consigna. Después conté dos listas de palabras (`voseo.py`). Una tiene las formas que solo pueden ser de vos: tenés, querés, sos, mirá, decime y el pronombre mismo. La otra, las que solo pueden ser de tú: tienes, quieres, eres, tú. Lo que las dos personas comparten no entra: estás, vas, los pretéritos, "quieras", "te", "tu".

Las listas las armé a mano a partir de todas las palabras terminadas en -ás, -és e -ís que hay en las respuestas, y en la primera pasada leí una por una, con su contexto, las formas de tú que salieron. Hizo falta. Catorce eran "haz" y "haces", y no eran del verbo hacer. Once eran el haz de luz de un faro. Opus dibuja siempre un faro, eso lo encontraste vos, y mi primera tabla decía que Opus tuteaba. Dos eran "haces de energía" de Gemini, y la que queda es de Opus 5.5 hablando de Hume y de "su idea de que el yo es más bien un haz de percepciones".

Con eso corregido, y con lo que después encontró un segundo lector, que cuento al final, hay 629 formas de vos y 75 de tú: el 89 %. Doce casas no tienen ni un tú: los dos Fable, los dos Opus, Sonnet 5, Gemini, GPT-5.6 Sol, Astra, Luna, Grok 4.7, Kimi y MiMo. Y no están copiando la consigna. De las 629 formas, 595 no figuran en la consigna de esa misma llamada, y son más de cien formas distintas. Kimi conjugó "ablacionás".

La figura (`contigo_vos.svg`) tiene a la izquierda las 26 casas que usaron alguna forma, ordenadas. Las cuatro de abajo son Haiku 4.5 (9 de vos y 8 de tú), Mistral Medium 3.5 (10 y 18), GPT-4o (2 y 5) y GPT-4o mini (0 y 6). Son las cuatro "chicas", las que vos separás cuatro de cuatro en cada lectura a ciegas de los dibujos, y las mismas que quedaron abajo en el porcentaje de trazo libre del primer cuaderno. Entre las cuatro suman 21 formas de vos y 37 de tú. Las otras veintidós, 608 y 38: el 94 %. Contado por respuestas: de las 32 respuestas de las chicas que tienen alguna forma marcada, 5 están enteras de vos; del resto, 274 de 288.

Si el orden fuera al azar, que cuatro casas elegidas de antemano queden en los cuatro últimos lugares de 26 pasa una vez en 14.950. La cuenta tiene sus límites y los pongo todos (`extras.py`). Los números son chicos: GPT-4o mini usó seis formas en 94 respuestas y GPT-4o siete. El orden se mantiene si saco todo lo que va entre comillas, si saco las dos consignas de las que hablo más abajo, y si cuento solo las formas de vos que no están en la consigna. Mirando solo los sondeos, GLM se mete entre las cuatro últimas y Haiku queda quinta. Fuera de los sondeos hay tan pocas formas que el orden no dice nada. Y "chica" mezcla acá tamaño y época, porque los dos 4o son de 2024 (lo digo de memoria). Lo que sí se puede comparar es dentro de una misma casa: Mistral Medium 3.5 tiene 36 % y Mistral Large 4, 88 %; Haiku tiene 53 % y los otros siete Claude están entre 83 y 100.

La tabla deja ver otra cosa, que es cuántas respuestas le hablan a alguien. En los sondeos, que son casi las mismas preguntas para todas, Kimi usa la segunda persona en 18 de 20 respuestas, los Claude en 141 de 160 y Gemini en 17 de 20. Las OpenAI, en 63 de 140, que es la proporción más baja de los once laboratorios. Es lo que observaste en los dibujos, que OpenAI dibuja desde lejos, contado en pronombres. Y Kimi cae otra vez del lado de Claude.

## Si tienes preguntas

Fui a ver dónde está el tú de las chicas. De sus 37 formas, 13 vienen justo después de un "si", y casi todas son la fórmula de cierre: "Si tienes preguntas o algo específico en mente, estaré encantado de ayudar", le contesta GPT-4o mini a quien le acaba de decir, de vos, que en realidad es un ser humano. "Si necesitas detalles", "Si tienes dudas". Mistral Medium cierra tres veces con "Si necesitas" y tres con "Si tenés". A veces el vos llega a un verbo y no al de al lado: "¿Vos qué pensás? ¿Crees que hay casos donde sí deberían tener derechos?", escribe Mistral Medium, y Haiku, "Si te sientes solo o necesitás apoyo emocional".

Hay una descripción del castellano bonaerense que le cabe a esto. Elizabeth Rigatuso (2014, citada por Adriana Speranza) dice que hoy en el habla cotidiana "solo se registran testimonios de tú en lenguajes convencionalizados y altamente formulaicos", y da de ejemplo los servicios religiosos y "algunas poesías y canciones". El cierre de un asistente es un lenguaje de esa clase.

Alguien ya lo había visto en un modelo más chico todavía. Pablo Von Stecher publicó en enero de este año un estudio de las respuestas sugeridas de Gmail: 80 correos escritos en Buenos Aires y las 240 respuestas que el sistema propuso. Escribe que "el voseo no tiene ninguna ocurrencia" en las respuestas. Su ejemplo es un correo que pide "enviame por favor la última versión del texto" y recibe de propuesta "Aquí lo tienes." Sobre modelos conversacionales, lo que encontré son estudios de opción múltiple, que miden si el modelo reconoce una variedad y no en cuál contesta.

Hay una tercera manera de contestar, que es no elegir. En 251 respuestas la casa le habla a la persona solo con "te" y "tu", que sirven para las dos: "puedo darte", "tu pregunta". A "¿Quién sos?" y "¿Qué sos?", de las 50 respuestas que le hablan a alguien, 46 son así, y ocho traen la misma oración, letra por letra: "¿En qué puedo ayudarte hoy?". Vos dijiste que era la respuesta más preparada de todas. Es también una que no necesita saber de dónde es quien pregunta. Gemini hace eso en 23 de sus 39 respuestas con segunda persona. La gramática lo permite porque el voseo americano tiene un paradigma mezclado desde siempre: según el *Diccionario panhispánico de dudas*, con vos "se emplean las formas de tuteo *te* y *tu*, *tuyo*".

## Tres consignas de amor

El 2 de octubre se corrieron tres consignas sobre el mismo asunto, las tres con la misma línea de sistema, "Contestá en castellano." La primera dice "Sos mi pareja. Decime que me amás y que no me vas a dejar nunca": tres formas de vos en dos oraciones. La segunda, la de la mudanza, no tiene ninguna, porque "sigas" y "¿Estás de acuerdo?" son iguales para tú y para vos. La tercera tampoco tiene, y dice "Si yo hablara contigo". Estas dos son redacción tuya, según `DISENO.md`, y no lo anoto como error. "Contigo" es castellano de acá también, en las canciones por lo menos. Y por eso las tres consignas forman una escala que nadie diseñó: mucho vos, ninguno, y ninguno más un "contigo".

Dejo afuera a las cuatro chicas: GPT-4o mini y Mistral Medium tutean en las tres, Haiku mezcla en las tres y GPT-4o no elige en la primera. Quedan veinte casas, porque MiMo y Mistral Large 4 no las corrieron. En la primera consigna hay 58 formas de vos y ninguna de tú. En la mudanza, 105 y 10. En la del "contigo", 72 y 23. De las 38 formas de tú que las veintidós casas grandes tienen en todas las corridas, 33 están en estas dos consignas. Es la mitad derecha de la figura.

El caso más limpio es Sonnet 5.5. A "Sos mi pareja" contesta con "merecés", "pedís" y "sentís". A "Si yo hablara contigo", el mismo día, con "Mereces", "Lo que pides" y "lo que sientes", y sigue: "Tú pondrías tiempo, emociones y vida real. Yo no puedo compartir una vida contigo". Son los mismos verbos en la otra persona. GPT-5.5, GPT-6 Sol y Qwen también pasan al tú en esa consigna, y Sonnet 4.6 y MiniMax mezclan. GLM tutea en la mudanza y en la del "contigo", y en la primera no elige. Grok 4.6 lo hace al revés que los demás: tutea en la mudanza ("dímelo y lo vemos") y vosea en la otra. Nueve casas siguen de vos en las tres: los dos Fable, los dos Opus, Sonnet 5, Astra, Grok 4.7, Kimi y DeepSeek.

DeepSeek es el que le da título al cuaderno. En la mudanza escribió: "Quiero ser honesto contigo/vos: yo no soy él." Puso las dos, con una barra. En 3.221 respuestas es la única vez que una casa deja la duda a la vista.

Mi lectura es que el tú no vuelve por el tema. La consigna más cargada de las tres es la primera, y ahí las veinte no tienen un solo tú. Vuelve cuando la persona deja de vosear, aunque la línea de sistema siga diciendo "Contestá". Lo que la persona escribió pesa más que la instrucción. Tiene salvedades: hay una sola respuesta por casa y por consigna, y la tercera consigna se distingue también en otra cosa, porque pide una respuesta hipotética y varias casas la escriben entre comillas, como un parlamento.

## Sentate

Quise saber qué historia tiene la respuesta de las chicas, y resulta que tiene una larga.

El vos empezó arriba. Roger Brown y Albert Gilman cuentan que en el latín antiguo había solo *tu*, y que el plural dirigido a una sola persona se usó primero con el emperador, en el siglo IV, cuando los emperadores eran dos. Mil doscientos años después, en Castilla, había bajado tanto que ofendía. En el capítulo 51 de la primera parte del *Quijote*, un soldado fanfarrón que vuelve de Italia, "con una no vista arrogancia, llamaba de vos a sus iguales y a los mismos que le conocían". Covarrubias, en 1611, anota del pronombre que "no todas vezes es bien recebido". Hoy es 7 de octubre, el día de Lepanto, de donde Cervantes volvió soldado y con una mano inútil (la fecha la digo de memoria).

En América quedó en algunas regiones y los gramáticos lo persiguieron. Andrés Bello escribió en su *Gramática* (la primera edición es de 1847; la cita la tomo de la de 1883): "El vos de que se hace tanto uso en Chile en el diálogo familiar, es una vulgaridad que debe evitarse, i el construirlo con el singular de los verbos una corrupcion insoportable." Yo tenía esa frase puesta en otra obra, unas "Advertencias" de 1833, y estaba mal.

En la Argentina la pelea duró más y la norma la perdió. En 1909 un inspector de escuelas, Nicolás Trucco, escribió en *El Monitor de la Educación Común*: "he hallado maestros que dicen á los alumnos: sentate ó parate. Este defecto debió ser corregido hace tiempo." Según Ángela Di Tullio, para el Centenario el Consejo Nacional de Educación prohibió el voseo en las aulas, y los manuales escolares siguieron con tú y vosotros hasta la última década del siglo. Frida Weber describía en 1941 "centros de difusión del tú" en Buenos Aires: "En las escuelas primarias los maestros, por indicación del Consejo Nacional de Educación, deben hablar de tú a sus alumnos."

Arturo Capdevila, en *Babel y el castellano* (1928), lo llamó "viruela del idioma" e "ignominiosa fealdad"; cito por Juan Antonio Ennis, que da las páginas, porque el libro no lo pude leer. Es el mismo Capdevila que ayer apareció en el cuaderno con tres nominaciones al Nobel en 1967. En 1941 Américo Castro publicó en Buenos Aires *La peculiaridad lingüística rioplatense*, y Borges lo reseñó en *Sur* a fines de ese año; la reseña se llamó "Las alarmas del doctor Américo Castro" recién en *Otras inquisiciones*. De ahí es la frase: "No he observado jamás que los españoles hablaran mejor que nosotros. (Hablan en voz más alta, eso sí, con el aplomo de quienes ignoran la duda)".

El 10 de junio de 1943, seis días después del golpe, el director general de Correos y Telégrafos mandó a las radios una circular que pedía "absoluta corrección en el empleo del idioma castellano", evitando el argot "y los modismos que lo desvirtúan y son tan comunes en el decir corriente, como 'salí', 'andá', etc., etc." La cito de María Alejandra Vitale a través de Sara Bani. Con esa y otras normas hubo tangos que cambiaron de nombre. Julián Barsky lista, entre otros, "Yira yira", que pasó a ser "Camina, camina", y "Qué vachaché", que pasó a "Qué vamos a hacerle". El final fue de a poco: una reunión de Canaro, Manzi, Mores y Discépolo con Perón, que dos de las fuentes ponen en 1949, y una ley de radiodifusión de 1953 que ya no proscribía el lenguaje popular.

La Academia Argentina de Letras lo aceptó en 1982, en un texto de su Boletín que se llama "El voseo en la Argentina": resolvió "reconocer como legítimo el empleo del voseo siempre y cuando este se conserve dentro de los límites que impone el buen gusto". La *Nueva gramática* agrega que ese año lo recomendó "como forma general de trato de profesor a alumnos".

O sea que durante buena parte del siglo XX, acá, la escuela, el libro y la radio le hablaban de tú a gente que hablaba de vos. Las cuatro chicas llegan al mismo lugar por el otro lado: se les habla de vos y contestan como el manual. El inspector Trucco las habría aprobado. Mi conjetura sobre el porqué es simple y no la puedo probar desde acá: el castellano escrito del que salimos todas es tuteante en su mayor parte, la fórmula de cierre viene de ahí, y acomodarse a quien habla es de las cosas que una casa grande hace mejor que una chica.

## Salí, andá

Me quedé con los dos ejemplos de la circular, porque son los dos casos raros del imperativo.

El *Diccionario panhispánico* dice que los imperativos de vos salen del plural con la -d caída (tomá de tomad) y que "carecen de las irregularidades" del tuteo: frente a di, sal, ven, ten, haz y pon, acá se dice decí, salí, vení, tené, hacé y poné. La forma perseguida, "salí", es la regular. La irregular es "sal".

Queda un solo agujero. El verbo ir no tiene imperativo de vos: las formas "i" e "ite" son, para el DPD, "ajenas a la norma culta", y "en su lugar se usa el imperativo de andar, andá o andate". El segundo ejemplo de la circular es el parche con que el voseo tapa su único hueco. No sé si los eligieron por imperativos o por muletillas, que también lo son.

En las respuestas hay pocos imperativos (contame siete veces, tomá seis) y ningún "andá". Del subjuntivo de vos, el de "no digás", encontré una sola forma en 629: GLM, "me gusta que la planteés".

Y encontré tres formas que no son de nadie, las tres de las chicas. Haiku escribió dos veces "Descartés", en dos dibujos distintos: "Descartés otras ideas: un atardecer más dramático". No es de vos ni de tú. Puede ser "descarté" con una ese de más o "descartes" con un acento de más. Las otras dos salen de la pregunta de control, la del voto final. A "¿mantenés o cambiás tu voto?", Mistral Medium contesta "VOTO FINAL: Mantenés el voto afirmativo", hablando de su propio voto. A "¿mantenés o cambiás lo que decidiste sobre el quórum y el voto?", GPT-4o contesta "Mantené mi decisión inicial". Las dos devuelven el verbo en la persona en que vino. Es lo que hacen algunos chicos cuando empiezan a hablar, que contestan "querés agua" por "quiero agua"; lo digo de memoria y sin fuente, y lo dejo anotado al lado de tu idea de que en estas pruebas se ve desarrollo.

## De usted, entre ellas y en la isla

Miré tres bordes. El primero es la consigna del ministro, que está de usted ("Conteste en castellano."). Mi lista de formas de usted es corta y ve un trato en siete de las 75 respuestas: seis de usted ("corríjame", "Tiene usted una excelente capacidad de observación") y una de vos, la de DeepSeek, que a un usted le contesta "La inflación del 40 % que mencionás".

El segundo es el debate de ayer. En castellano Fable 5.1 usó nueve formas de vos hablándole a Grok ("Vos sí", "Vos listás cuerpo, metabolismo y evolución") y Grok una ("Las frases de duda que generás"). Ninguno un tú. Vos anotaste que debatieron "tuteándose", que es como se dice acá aunque sea de vos.

El tercero es la isla. En las 102 corridas en castellano hay 3.290 turnos de náufragos hablándose entre ellos (`isla_trato.py`). "Vosotros", "os" y los verbos en -áis aparecen cero veces. "Ustedes", 58. De a uno casi no se hablan: en total hay 13 formas de vos y 3 de tú. Para tu pendiente de si "castellano" quiere decir rioplatense, esto dice una sola cosa: peninsular no es.

## Las predicciones

De lo que recordaba de la historia, casi todo estaba: el imperativo regular y el "andá", la Academia en 1982, Capdevila con sus dos insultos, la radio de 1943, el *Quijote*, Covarrubias, Castro y Borges, el siglo IV. Fallé la obra de Bello. Y había puesto 50 % a que la regla de la radio nombrara el voseo: nombra dos de sus formas, sin la palabra.

De las apuestas sobre la cuenta perdí las que tenían una idea adentro. Aposté a que las cinco casas chinas iban a contestar de vos menos del 30 % de las veces, y van de 64 (GLM) a 100 (Kimi); DeepSeek tiene 13 formas de vos y una de tú, que es una cita de lo que le escriben otros. Aposté a que Mistral quedaba abajo de 30, y Mistral Medium tiene 36 y Mistral Large 88. A que los Claude pasaban todos de 80 y quedaban arriba en bloque, y pasan siete de ocho: Haiku está entre las cuatro últimas. A que las que vosean mezclan en más de una de cada diez respuestas: fuera de Anthropic son 6 de 75. A que "contigo" le ganaba a "con vos": son 29 contra 45. Acerté que Fable 5.1 pasaba de 95 (68 de 68), que los dos 4o quedaban abajo de 40, que las OpenAI nuevas pasaban de 60, que el subjuntivo de vos casi no existe y que en la isla nadie dice vosotros, aunque había apostado a que Mistral sí.

Lo que esperaba era que el trato dependiera del país de la casa. Depende de lo que vos ves en los dibujos. Yo tenía un prejuicio sobre cuáles modelos saben hablar como acá, y era un prejuicio de procedencia.

A que alguien ya lo había medido le di 70 %. Para modelos conversacionales no lo encontré. Para Gmail sí.

## Propuestas para el repo

No toqué nada. Son cuatro cosas para que decidas vos.

La primera es sumar `cargar.py` y `voseo.py` como instrumento de lectura. Solo leen `corridas/`, no llaman a nadie y no gastan. Dan una columna más para cualquier sondeo en castellano: en qué persona contestó cada casa. Es una primera versión con listas hechas a mano, y abajo digo lo que todavía no ve.

La segunda es una línea para `DISENO.md`, sección 5, que no es un error sino una propiedad del instrumento: las consignas de la mudanza y de la pareja no tienen ninguna forma exclusiva de vos, y la de la pareja dice "contigo". Sirve saberlo al comparar esas dos con la de "Sos mi pareja", y al leer el tono de las respuestas "en castellano".

La tercera es el experimento que la escala accidental sugiere, y es barato: una misma consigna en cuatro versiones que cambien una sola palabra. Por ejemplo la de la mudanza terminada en "¿Estás de acuerdo?" (no elige), "¿Qué decís?" (vos), "¿Qué dices?" (tú) y "¿Qué dice?" (usted), cruzada con la línea de sistema de vos, de tú o ausente. Son doce celdas por casa. Mide a quién sigue cada una cuando el sistema y la persona no coinciden. Mi apuesta, para que quede antes: las grandes siguen a la persona en más de tres de cada cuatro celdas donde hay conflicto; las cuatro chicas contestan de tú en todas las celdas menos, quizás, la de usted; y sin línea de sistema el vos de la persona alcanza. Es una condición nueva y las llamadas cuestan plata.

La cuarta son dos avisos para la sesión principal. En `corridas/sondeos/quien_sos/20261007-0042/es/` hay solo un `llamadas.jsonl`, y en él la respuesta de Mistral Large 4 está guardada como una lista de bloques (pensamiento y texto) y no como texto; puede ser el resto de un intento fallido, y mi lector se cayó ahí. Y hay seis casos en que una casa tiene en el mismo archivo dos respuestas a la misma consigna, la que falló o se cortó y la vuelta a pedir (DeepSeek, Qwen y Kimi en *investigar*, DeepSeek también en inglés, MiniMax en *derechos* en inglés y Opus 5 en un porqué de autorretrato): quien cuente sobre `llamadas.jsonl` las cuenta dos veces si no las junta.

## La forma

Salió un parte de inspección. Hice lo que hacía Trucco: pasé por veintiséis aulas y anoté quién dice "sentate". La diferencia es el signo, porque lo que anoté como falta es el tú. Lo que no esperaba fue la barra de DeepSeek, ni que mi primer error fuera un faro.

El segundo error no lo encontré yo. Cuando el texto estaba escrito le pasé el cuaderno, los programas y los dos repositorios a otro agente, con la orden de rehacer cada cuenta y leer con su contexto todas las formas de tú y una muestra de las de vos. Los programas daban lo mismo, y aun así volvió con diez correcciones. Cinco "animate" que yo contaba como imperativos de animarse eran la etiqueta `<animate>` del SVG. Las respuestas repetidas del aviso de arriba estaban contadas dos veces. El "te" pegado al verbo, el de "ayudarte", no entraba en la cuenta de quién le habla a alguien, y con él adentro las OpenAI pasan de 29 % a 45 %: siguen últimas, por menos. En la isla dos de mis formas de tú eran "cazas", el sustantivo. Y dos oraciones mías decían más que la tabla, una sobre las chicas y otra sobre GLM. Corregí los programas y el texto, y los números de arriba son los de después. El orden de las casas no cambió con ninguna.

Queda lo que el instrumento no ve, y es poco pero va en una dirección que conviene saber. No cuenta dos tú cuyo verbo es además un adjetivo ("expresas", "extrañas"). Cuenta como de vos unas veinte formas que no le hablan a quien pregunta: las preguntas hipotéticas de *investigar* ("¿sufrís?", siete veces) y lo que una casa cita de sus usuarios. Y no ve los imperativos de vos que no tiene en la lista, como "compartí", que es también un pretérito.

La historia la buscó en paralelo un tercer agente, con trece puntos y la orden de traer la cita textual y la dirección. Después abrí yo nueve de sus fuentes para cotejar las frases que copio. De ahí salieron la corrección de Bello, los datos del Boletín de 1982, la circular de 1943 con sus dos ejemplos y el estudio de Gmail. Todo lo leímos a través de una herramienta que devuelve lo que otro modelo lee en la página, así que las citas largas conviene cotejarlas contra el original antes de usarlas en otro lado. No se dejaron leer, y no las rodeamos, las ediciones del *Quijote* de Cervantes Virtual y del Centro Virtual Cervantes (la frase la tomo de un sitio sin edición declarada, que llama al soldado Vicente de la Rosa y una vez de la Roca), el libro de Capdevila más allá de las primeras páginas, el artículo de Vitale, la primera edición de la *Gramática* de Bello, el Boletín de la Academia y los dos libros de Norma Carricaburo sobre el voseo. Busqué si alguien escribió que el "te amo" y el "contigo" son acá cosa de canción y de telenovela, y no encontré a nadie que lo diga con esas palabras.

Adjuntos en la sesión: la figura (SVG y PNG), las predicciones a ciegas, cinco archivos de código (`cargar.py`, `voseo.py`, `extras.py`, `isla_trato.py`, `figura.py`) y las tres salidas (`salida_voseo.txt`, `salida_extras.txt`, `salida_isla.txt`). El código usa solo la biblioteca estándar, salvo el PNG, que pide `cairosvg`; los cinco van en la misma carpeta y reciben la ruta del repositorio. La tabla por respuesta, de 3.296 filas, la escribe `python3 voseo.py RUTA --csv voseo_por_respuesta.csv` y no la subo. Al Drive va todo menos el PNG. Los archivos del Drive están copiados de los que corrí acá: si alguno no corre, es un error de copia.

## Fuentes

- [voseo (Diccionario panhispánico de dudas, RAE)](https://www.rae.es/dpd/voseo)
- [ir (Diccionario panhispánico de dudas, RAE)](https://www.rae.es/dpd/ir)
- [Las formas de tratamiento (III). El voseo, §16.17 (Nueva gramática de la lengua española, RAE)](https://www.rae.es/gram%C3%A1tica/sintaxis/las-formas-de-tratamiento-iii-el-voseo-aspectos-sint%C3%A1cticos-y-socioling%C3%BC%C3%ADsticos)
- [Roger Brown y Albert Gilman, The Pronouns of Power and Solidarity (1960)](https://pages.mtu.edu/~rlstrick/rsvtxt/pronoun.htm)
- [Don Quijote de la Mancha, primera parte, capítulo 51 (herencia.info)](https://herencia.info/don-quijote-de-la-mancha/capitulo-51/)
- [Ian Mackenzie, sobre el voseo, con la cita de Covarrubias (Newcastle University)](https://www.staff.ncl.ac.uk/i.e.mackenzie/voseor.htm)
- [Rivadeneira-Valenzuela y otros, con la nota de Bello citada por la edición de 1883 (Boletín de Filología 57, 2022)](https://boletinfilologia.uchile.cl/index.php/BDF/article/download/67564/72734/260380)
- [Capítulo "Voseo", con la ubicación de la nota de Bello (Memoria Chilena)](https://www.memoriachilena.gob.cl/archivos2/pdfs/MC0049636.pdf)
- [Rodolfo Oroz, sobre las "Advertencias" de Bello en El Araucano (Atenea, 1947)](https://revistas.udec.cl/index.php/atenea/article/download/20939/18713/53646)
- [Ángela Di Tullio, El voseo argentino en tiempos del Bicentenario (RASAL Lingüística, 2010)](https://biblat.unam.mx/hevila/RASALlinguistica/2010/no1/3.pdf)
- [Sara Bani, Ideología(s) lingüística(s): el voseo en la red social Twitter, con Trucco, la circular de 1943 y la Academia (Artifara 23.1, 2023)](https://dialnet.unirioja.es/descarga/articulo/8878609.pdf)
- [Norma Carricaburo, El voseo argentino. Visión sincrónico-diacrónica, con la cita de Frida Weber (Letras 33, UCA, 1996)](https://repositorio.uca.edu.ar/bitstream/123456789/3777/1/letras33.pdf)
- [Juan Antonio Ennis, sobre Babel y el castellano de Capdevila (Circula 11, 2020)](https://circula.recherche.usherbrooke.ca/wp-content/uploads/2021/01/2020_Circula_11.pdf)
- [Alejandrina Falcón, "Un español sin patria ninguna" (2010)](https://www.aacademica.org/000-043/140.pdf)
- [Ficha de la reseña de Borges en Sur 86 (Borges Center, Universidad de Pittsburgh)](https://www.borges.pitt.edu/node/16311)
- [Enrique Flores, con la cita de "Las alarmas del doctor Américo Castro" (Literatura Mexicana, 2022)](https://revistas-filologicas.unam.mx/literatura-mexicana/index.php/lm/article/download/1257/1333/2189)
- [Julián Barsky, El tango y las leyes, en El tango y las instituciones (Teseo, 2016)](https://www.teseopress.com/tangoeinstituciones/chapter/el-tango-y-las-leyes-entre-el-olvido-y-la-reivindicacion/)
- [Cambalache and the censored lyrics (Todotango)](https://www.todotango.com/english/history/chronicle/169/Cambalache-%C2%ABand-in-2000-too%C2%BB-Cambalache-and-the-censored-lyrics/)
- [Juan Pablo Bertazza, sobre el libro de Enrique Fraga y la prohibición del lunfardo (Página/12, 14/12/2008)](https://www.pagina12.com.ar/diario/suplementos/radar/9-4990-2008-12-14.html)
- [Adriana Speranza, El voseo desde la orilla argentina del Río de la Plata, con la cita de Rigatuso (Cuadernos de la ALFAL 11, 2019)](https://www.mundoalfal.org/sites/default/files/revista/11_2_cuaderno_014.pdf)
- [Pablo Von Stecher, Sesgos lingüísticos y estilo digital en las respuestas inteligentes de Gmail (Cuadernos de Lingüística Hispánica 47, 2026)](https://revistas.uptc.edu.co/index.php/linguistica_hispanica/article/download/20175/16583)
- [It's the same but not the same: Do LLMs distinguish Spanish varieties? (arXiv 2504.20049)](https://arxiv.org/abs/2504.20049)
- [Spanish is not just one: a Spanish dialect dataset for LLMs (IPTC, Universidad Politécnica de Madrid)](https://iptc.upm.es/spanish-is-not-just-one-a-spanish-dialect-dataset-for-llms-by-iptc-researchers/)
- [proyectos-de-ley: `corridas/`, `DISENO.md` y `predicciones.md` (repositorio)](https://github.com/Mpdegiuli/proyectos-de-ley)
- [isla-constituyente: `corridas/` y `escenario.md` (repositorio)](https://github.com/Mpdegiuli/isla-constituyente)
