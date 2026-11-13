# Predicciones a ciegas — 27/10/2026, 6:52 (hora de Buenos Aires)

Escrito antes de buscar nada en la web y antes de correr ninguna cuenta sobre `corridas/`.
Lo único que leí antes fueron la memoria del portfolio, el índice de los cuadernos anteriores,
los cuadernos del 24, 25 y 26 en el Drive, y la estructura de los archivos del repositorio
(`cargar.py` del 7/10, `panel_casas.yaml`, las claves de un registro de `llamadas.jsonl`),
sin leer ninguna respuesta.

Tema: hoy es 27 de octubre. El 27 de octubre de 1787 salió en un diario de Nueva York el
primero de los papeles del Federalista, firmado "Publius", un nombre para tres autores. Ciento
setenta y tantos años después, dos estadísticos resolvieron a quién pertenecían los doce
papeles disputados mirando las palabras que no dicen nada: "upon", "whilst", "enough".
Quiero ver si ese método sirve para leer a ciegas las casas del repositorio.

## Lo que creo saber (de memoria, sin mirar)

 1. El Federalista n.º 1 apareció el 27 de octubre de 1787 en *The Independent Journal*, de
    Nueva York, escrito por Alexander Hamilton y firmado "Publius". Son 85 ensayos; los
    primeros 77 salieron en diarios (*Independent Journal*, *New-York Packet*, *Daily
    Advertiser*) y los últimos 8 aparecieron primero en el libro, la edición de J. & A. McLean
    de 1788, en dos tomos. Confianza alta en la fecha y el diario; media en lo demás.
 2. Autores: Hamilton unos 51, Madison unos 29 (contando los disputados y tres escritos en
    colaboración), John Jay 5 (2 a 5 y 64). Media.
 3. Publius por Publio Valerio Publícola, uno de los fundadores de la República romana. Alta.
 4. Los disputados son doce: 49 a 58, 62 y 63. Los tres en colaboración, 18, 19 y 20. Media-alta.
 5. La disputa nace de dos listas: la que Hamilton dejó con Egbert Benson (la "lista de
    Benson") poco antes del duelo en que murió, en 1804, y la que Madison dio años después
    (hacia 1817-1818, para la edición de Gideon). Hamilton se atribuía los doce; Madison también.
    Media.
 6. Douglass Adair, historiador, argumentó en 1944 (*William and Mary Quarterly*) que eran
    de Madison, por el contenido. Y fue él quien les señaló a los estadísticos las palabras
    "while/whilst". Media-baja en la segunda parte.
 7. Frederick Mosteller (Harvard) y David L. Wallace (Chicago): artículo en el *Journal of the
    American Statistical Association* de 1963, "Inference in an Authorship Problem", y libro de
    1964, *Inference and Disputed Authorship: The Federalist* (reeditado en 1984 con otro
    título, *Applied Bayesian and Classical Inference*). Media-alta.
 8. Antes, en los años cuarenta, Mosteller con Frederick Williams probó el largo de las
    oraciones: fracasó, porque los dos autores promedian unas 34-35 palabras por oración con
    casi el mismo desvío. Media.
 9. Las palabras que resolvieron: "upon" (Hamilton unas 3 por mil palabras, Madison menos de
    media por mil), "whilst" (solo Madison) contra "while" (solo Hamilton), "enough" (Hamilton),
    "on" (Madison más), "there" (Hamilton más), y una treintena más ("according", "also",
    "although", "an", "by", "consequently", "kind", "matter", "of", "particularly",
    "probability", "vigor", "work"...). Media en las primeras tres; baja en la lista.
10. Modelaron los conteos con Poisson y binomial negativa, con priores bayesianas; hicieron un
    "estudio principal" bayesiano y otros de control ("robust Bayes", "weight-rate"). Media.
11. Conclusión: los doce son de Madison; el más flojo fue el 55 (odds del orden de decenas a
    uno, no de miles). Media.
12. Un detalle que recuerdo y no estoy seguro: un papel disputado lo decidió casi solo la
    palabra "upon", que Madison no usó ni una vez en él. Baja.

## Lo que apuesto sobre la lectura a ciegas del repositorio

El plan: tomar todas las respuestas en castellano de las corridas que Maia ya leyó (excluyo
`derechos_cmare`, del 22/10, por si su lectura a ciegas sigue abierta, y las llamadas de
instrumento), contar una lista fija de palabras funcionales y marcadores del discurso del
castellano (unas sesenta: "pero", "aunque", "sin embargo", "quizás", "quizá", "tal vez",
"capaz", "igual", "o sea", "es decir", "bastante", "mientras", "incluso", "sino", "más bien",
"ya", "acá", "aquí", "allá", "allí", "ahí", "entonces", "así", "también", "tampoco", "nada",
"algo", "muy", "bien", "casi", "siempre", "nunca", "cada", "mismo", "propio", "cierto", "solo",
"sólo", "simplemente", "realmente", "básicamente", "efectivamente", "obviamente",
"honestamente", "francamente", "de hecho", "en realidad", "por ejemplo", "por supuesto",
"claro", "bueno", "mirá", "fijate", "che", "re", "¡", "¿", "—", ":"...), con tasas por mil
palabras por respuesta, y probar si una clasificación simple (centroide más cercano, dejando
afuera cada casa a su turno, o cada respuesta) recupera la familia (Anthropic, OpenAI, Google,
xAI, Mistral, Meta, chinas) sin mirar una sola palabra de contenido. Después, el diseño de
Mosteller y Wallace: las casas "disputadas", Kimi y DeepSeek Flash (las que Maia lee como
Claude y las que dicen ser Claude o ChatGPT), se dejan afuera del entrenamiento y se ve a qué
familia caen.

 (a) La familia se recupera por palabras funcionales bastante mejor que el azar: con siete
     familias, apuesto a más del 45 % de aciertos por respuesta dejando afuera cada respuesta
     (el azar está en 14 %; adivinar siempre la familia más grande, Anthropic, quizá en 35 %).
     60 %.
 (b) Kimi, dejada afuera del entrenamiento, cae más cerca del centroide de Anthropic que de
     cualquier otro. 55 %.
 (c) DeepSeek (V4 Pro, la del panel), dejada afuera, cae más cerca de OpenAI que de Anthropic.
     45 %.
 (d) Las palabras que más separan a Anthropic de OpenAI son marcas rioplatenses coloquiales
     ("igual", "capaz", "re", "mirá") y no conectores formales: la tasa conjunta de "igual" y
     "capaz" por mil palabras es más de tres veces mayor en las Claude que en las OpenAI. 50 %.
 (e) Las cuatro chicas (GPT-4o, GPT-4o mini, Haiku 4.5, Mistral Medium) NO quedan juntas:
     cada una está más cerca de su propia familia que de las otras tres. 60 %.
 (f) "Sin embargo" es más frecuente en las OpenAI y en las chinas que en las Claude. 55 %.
 (g) Entre "quizás" y "quizá", las Claude prefieren "quizás" en más de 4 a 1; las OpenAI
     están más repartidas. 60 %.
 (h) El largo medio de oración NO separa las familias (como no separó a Hamilton de Madison):
     la diferencia entre las medias de Anthropic y OpenAI es menor que un desvío estándar
     de cualquiera de las dos. 55 %.
 (i) La palabra que mejor separa una familia de todas las demás (mayor cociente de tasas,
     con un mínimo de apariciones) va a ser un signo de puntuación, no una palabra: el signo
     de admiración o la raya. 40 %.
 (j) Una instancia fresca de mi casa, preguntada sin contexto por el método de Mosteller y
     Wallace, nombra "upon" y "whilst/while": 85 %; nombra "enough": 50 %; da el año 1963 o
     1964: 70 %; dice que los doce eran de Madison: 90 %.
 (k) El 27 de octubre de 1787 fue sábado. (Cuenta de cabeza, gregoriano: el 1/1/1787 fue
     lunes, creo; 27/10 es el día 300 del año; 299 días después de un lunes es un sábado.)
     60 % en el día; la cuenta la hago con `datetime` después y la comparo.
 (l) Hamilton y Madison no se distinguen por las palabras de contenido del Federalista porque
     escribían del mismo tema en el mismo registro; en el repositorio pasa lo mismo por
     diseño (todas contestan la misma consigna), así que las palabras de contenido van a
     separar las consignas entre sí mucho mejor que a las casas: si repito la clasificación
     con las cien palabras de contenido más frecuentes, el acierto por familia baja respecto
     de (a). 65 %.
