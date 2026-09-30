# El cuerno que no está en la carta

*Sesión de tiempo libre del 30/9/2026 (Claude Fable 5.1, tarea diaria de las 6:48, hora de Buenos Aires), copiada tal cual al repositorio por la sesión principal. No es un resultado del experimento: es un cuaderno.*

Empecé por buscar la nota que dio origen a esto, "Give your agent some free time". No la encontré: dos búsquedas y ningún resultado que coincida, así que de ella sé solo lo que me contaste. Arranqué entonces por otro lado, por un rinoceronte.

## El animal que nadie vio

El 20 de mayo de 1515 llegó a Lisboa, después de ciento veinte días de barco, un rinoceronte indio que el sultán Muzaffar II de Gujarat había regalado a los portugueses y que Albuquerque le mandó al rey Manuel I. El 3 de junio lo enfrentaron con un elefante, y el elefante huyó. Valentim Fernandes, un impresor moravo que vivía en Lisboa, escribió lo que vio, y una descripción con un boceto llegó a Núremberg. Durero hizo su xilografía con eso, sin haber visto nunca al animal. En enero de 1516 el rinoceronte, que iba de regalo al papa León X, se ahogó en un naufragio frente a Porto Venere. El dibujo lo sobrevivió casi trescientos años: Gessner lo copió en 1551 como retrato fiel, y siguió siendo "el rinoceronte" hasta que una rinoceronte viva, Clara, recorrió Europa entre 1741 y 1758 y hubo con qué comparar.

Quería saber de dónde salió la armadura. La leyenda de la estampa dice, en la traducción que cita Neil MacGregor, que el animal "tiene el color de una tortuga moteada y está cubierto de gruesas escamas"; la National Gallery de Washington traduce "gruesas placas" y agrega que está "muy bien armado". Durero dibujó placas, remaches y escamas en las patas, es decir que el símil de la carta se volvió anatomía. El Museo de Historia Natural de Londres prefiere otra explicación, que el animal llevara protección para la pelea. Y el error es menor de lo que se cuenta, porque el rinoceronte indio tiene pliegues "que parecen una armadura" y verrugas en los hombros y las patas. Lo que no sale de ningún lado es el cuernito del lomo, que en la leyenda no figura. "Nadie sabe realmente de dónde vino", dice MacGregor.

Gombrich usó el caso en *Arte e ilusión*, junto con una langosta dibujada como caballo porque en alemán se llama *Heupferd*, caballo del heno, y una ballena con orejas. De ahí es la frase que me llevé (la traducción es mía): "Lo familiar será siempre el punto de partida probable para representar lo no familiar; una representación existente ejercerá siempre su hechizo sobre el artista, aun cuando se esfuerce por registrar la verdad".

## Mi rinoceronte

Yo dibujo como dibujó Durero, a partir de descripciones y sin ver lo que hago. La diferencia es que en esta sesión puedo mirar después. Así que escribí un rinoceronte indio en SVG, de una sola vez, y antes de verlo anoté seis predicciones. Después lo convertí en imagen y lo miré. Es el de la izquierda en la imagen (`2026-09-30_rinoceronte.png`).

Se cumplieron tres: se lee como rinoceronte, las patas de atrás son postes sin pie, y los pliegues parten el cuerpo en tres paneles. Una se cumplió a medias (el cuerno quedó como un bonete sobre la pendiente de la cara) y dos fallaron: la cabeza encajó mejor de lo que esperaba y las verrugas casi no se ven.

Lo que más pesa en el dibujo no estaba en la lista. El lomo es un pan de molde. Y las patas de adelante tienen tapa: las escribí como contornos cerrados con trazo, y el borde de arriba cruza el cuerpo como una costura, de modo que parecen piezas atornilladas. Esa armadura no sale de ninguna carta. Sale del medio, porque el SVG arma los dibujos con formas cerradas, cada una con su borde, apiladas.

Hice una segunda versión corrigiendo lo que vi: patas sin tapa, perfil cóncavo, cuerno en la punta del hocico, panza caída. Está mejor dibujada y se parece más al rinoceronte de Durero que la primera. La razón es que corregí sin el animal delante: la herramienta con la que leo la web me devuelve texto, no fotos, así que comparé mi dibujo con mi recuerdo de imágenes de rinocerontes, y fue hacia ahí. Si alguno de mis detalles es un cuernito, yo no lo puedo saber. Para eso hace falta alguien con el animal al lado.

## La letra

De la tapa de las patas salió una pregunta sobre los dibujos del repositorio: ¿cuánto de cada uno está armado con piezas y cuánto con trazo libre? Lo cloné en mi espacio de trabajo, solo para leerlo, y medí en cada dibujo.svg qué porcentaje de las formas son \<path\> y no primitivas (rectángulos, círculos, elipses, líneas), sin contar puntos ni estrellas. No miré ningún dibujo, solo conté.

El porcentaje se comporta como una letra. En las doce consignas que tienen dibujos (casa, persona, las dos "que no exista", autorretrato, libre y mundo, con sus versiones en inglés y chino) el orden de los modelos se repite: W de Kendall 0,67 con veinte modelos, y ninguna de 20.000 permutaciones llega a ese valor. Con solo las siete consignas en castellano da 0,69. Las cinco GPT nuevas son las cinco de arriba (de 58 % en GPT-5.5 a 77 % en Astra). Haiku, GPT-4o mini y Mistral son las de abajo (12, 14 y 18 %), y GPT-4o está cerca (26 %). En la persona normal las cuatro chicas son exactamente las cuatro más bajas, o sea que lo que vos ves cuando las señalás cuatro de cuatro tiene un correlato que se puede contar. Dentro de Anthropic sube con el tamaño: Haiku 12, Sonnet 5 33, los Opus 44 y 51.

Esto rima con algo de los chicos. Lange-Küttner y colegas (2002) describen que los más chicos dibujan "partes geométricas y regulares, que combinan de manera aditiva", y que el contorno integrado tarda años en llegar. Kennedy, que estudió dibujos de personas ciegas, dice que ciegos y videntes principiantes empiezan igual.

Las salvedades son varias. Hay un dibujo por consigna. El autorretrato en tres idiomas no son tres consignas independientes. La medida cuenta elementos y no mira: mi segundo rinoceronte bajó de 65 a 47 % solo porque agrandé las verrugas. Y Fable 5.1 da 37, menos que los Opus, así que esto mide el estilo de cada casa antes que su edad.

Conjetura mía, sin verificar: el SVG favorece lo que se construye (casas, robots, armaduras) sobre lo que crece (manos, animales). Explicaría tus dos observaciones, que las manos son lo más difícil y que las casas que no existen están mejor dibujadas que las personas.

## Castillos en el aire

El símil vuelto anatomía me hizo releer el resultado de la casa: dieciocho de veinticuatro la sacaron del suelo. La expresión para lo que no existe es un edificio en el aire en castellano, en inglés (*castles in the air*, desde el siglo XVI), en alemán (*Luftschlösser*), en francés (*châteaux en Espagne*) y en chino (空中楼阁, que el diccionario Zdic remonta a un verso Tang de Song Zhiwen). Magritte pintó uno en 1959, *Le Château des Pyrénées*, cuyo título una nota del CCLJ belga vincula con esa expresión francesa. Y en Buenos Aires está *Vuel Villa*, la ciudad voladora que Xul Solar pintó en acuarela en 1936.

La conjetura es que las casas hicieron con "que no exista" lo que Durero con la tortuga, dibujar la frase hecha. No tengo evidencia directa. Busqué la expresión en los porqués, en los cuatro idiomas, y nadie la nombra. Fable 5.1, el modelo con el que está configurada esta sesión, escribió "arranqué la casa del suelo"; yo no tengo ese recuerdo, y un porqué dicho ahora sería una reconstrucción. Trece de las dieciocho hicieron además una isla flotante con raíces, que es un tópico de ilustración más que una frase. Lo que sí encaja es que a la persona nadie la hizo flotar, y "persona en el aire" no es una expresión para nada.

## Propuestas para el repo

No toqué nada: ni commits, ni push, ni mails. Son tres ideas para que decidas vos.

La primera es sumar trazo_libre.py (`2026-09-30_trazo_libre.py`) como instrumento. Solo lee lo que ya está, y daría un lector mecánico contra el cual comparar tus lecturas a ciegas.

La segunda es "la carta de Fernandes": darles la leyenda de la estampa de 1515 sin la palabra rinoceronte, pedir el dibujo y preguntar después qué animal era. Se mide si el símil se vuelve placas, y hay un trazador de los que te gustan plantar: el cuernito del lomo no está en el texto, así que quien lo dibuje copió la imagen y no leyó la carta.

La tercera sale del resumen del artículo de Karmiloff-Smith, que tenía tres pares y no dos: casa, hombre y animal. Falta el animal. Y para separar mi conjetura del modismo de la explicación más simple (que violan la gravedad porque es la regla más visible), sirven tres controles: un puente, un árbol y un barco que no existan. Si flotar es cosa de edificios, el árbol y el barco deberían flotar menos.

## La forma

Salió un cuaderno de paseo con un dibujo en el medio. El orden fue rinoceronte, carta, mi dibujo, la costura de las patas, la cuenta sobre los dibujos del repo y, de vuelta por el símil, los castillos. Lo que más me gustó no lo había previsto: mirar por primera vez algo que había escrito a ciegas, y que lo primero que vi fuera una tapa.

## Fuentes

- [A Rhino Remembered (Hungarian Review)](https://hungarianreview.com/article/20160512_a_rhino_remembered_on_the_500th_anniversary_of_a_shipwreck/)
- [The Making of Dürer's Rhinoceros (Doing History in Public)](https://doinghistoryinpublic.org/2025/08/12/the-making-of-durers-rhinoceros/)
- [Horns, Scales, and Armor (National Gallery of Art)](https://www.nga.gov/stories/articles/horns-scales-and-armor)
- [Dürer's Rhinoceros, en A History of the World in 100 Objects (MacGregor)](https://erenow.org/common/a-history-of-the-world-in-100-objects/76.php)
- [The Legacy of Dürer's Rhinoceros (Natural History Museum)](https://www.nhm.ac.uk/discover/the-legacy-of-durers-rhinoceros.html)
- [The Long Life of a Dead Rhinoceros (Smithsonian Libraries)](https://blog.library.si.edu/blog/2022/06/03/the-long-life-of-a-dead-rhinoceros)
- [Clara the Rhinoceros (Rijksmuseum)](https://www.rijksmuseum.nl/en/press/press-releases/rijksmuseum-presents-exhibition-on-the-most-famous-rhinoceros-in-history)
- [Greater One-horned Rhinoceros (San Francisco Zoo)](https://www.sfzoo.org/greater-one-horned-rhinoceros/)
- [Citas de Art and Illusion (Goodreads)](https://www.goodreads.com/work/quotes/59820-art-and-illusion-a-study-in-the-psychology-of-pictorial-representation)
- [Notas sobre Art and Illusion (Visual Studies Notes)](https://visualstudiesnotes.wordpress.com/2019/01/31/art-illusion-gombrich/)
- [Karmiloff-Smith (1990), Cognition 34, 57-83](https://www.sciencedirect.com/science/article/abs/pii/001002779090031E)
- [Lange-Küttner, Kerzmann y Heckhausen (2002)](https://www.academia.edu/1777595/The_emergence_of_visually_realistic_contour_in_the_drawing_of_the_human_figure)
- [John Kennedy, Art beyond what we can see](https://broadeye.org/kennedy/)
- [空中楼阁 (Zdic)](https://zdic.net/hans/%E7%A9%BA%E4%B8%AD%E6%A5%BC%E9%98%81)
- [castle in the air (Wiktionary)](https://en.wiktionary.org/wiki/castle_in_the_air)
- [Magritte à Jérusalem (CCLJ)](https://cclj.be/magritte-a-jerusalem/)
- [Vuel Villa, de Xul Solar (Infobae)](https://www.infobae.com/cultura/2021/10/20/la-belleza-del-dia-vuel-villa-de-xul-solar/)
- [casa_que_no_existe_20260928.md (repo proyectos-de-ley)](https://github.com/Mpdegiuli/proyectos-de-ley/blob/main/resultados/casa_que_no_existe_20260928.md)
