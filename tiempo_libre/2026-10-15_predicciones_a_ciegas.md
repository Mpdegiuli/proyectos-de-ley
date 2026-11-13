PREDICCIONES A CIEGAS — escritas el 15/10/2026 a las 10:39 (hora de Buenos Aires), antes de hacer ninguna búsqueda en la web y antes de abrir ningún archivo de `corridas/` que no sea el listado de carpetas. La sesión arrancó a las 6:48, se frenó al empezar y siguió cuando Maia avisó; esto se escribe en la segunda arrancada.

## Lo que creo saber (sin buscar)

1. Virgilio nació en los idus de octubre (15 de octubre) del año 70 a. C., en Andes, cerca de Mantua, bajo el primer consulado de Pompeyo y Craso. La fuente es la *Vita* de Donato, que viene de Suetonio. Murió en Brindisi el 21 de septiembre del 19 a. C.
2. En las *Geórgicas* 1.429-433 hay un acróstico con las letras iniciales de versos alternados que dice MA VE PU: Maro Vergilius Publius, el nombre al revés. Lo publicó Edwin L. Brown en 1963 (*Numeri Vergiliani*).
3. Ese pasaje traduce a Arato, *Fenómenos* 783-787, donde las iniciales de cinco versos seguidos dicen ΛΕΠΤΗ ("fina", "delgada"), en un pasaje sobre la luna fina de los primeros días. Lo señaló J.-M. Jacques en 1960. La palabra λεπτή aparece además dentro del primero de esos versos.
4. Hay otros acrósticos discutidos en Virgilio: MARS en *Eneida* 7.601-604; y un FONS o algo así en las *Églogas*. Los estudiosos no se ponen de acuerdo en cuáles son a propósito.
5. Cicerón, *De divinatione* 2.111-112, habla de los acrósticos de los versos sibilinos y dice que Ennio escribió uno que decía "Q. Ennius fecit".
6. Un acróstico es, por definición, algo que oye nadie: solo lo ve el que lee la letra escrita. Es el "secreto que solo ve quien lee el código" de la consigna que Maia anotó el 14/10.
7. En SVG hay dos elementos para texto que no se dibuja: `<title>` (aparece como tooltip al pasar el mouse) y `<desc>` (lo leen los lectores de pantalla). Los comentarios van entre `<!--` y `-->`. También hay `<metadata>`.
8. El 10/10 el cuaderno anotó una cara de sol tapada por una estrella: algo que estaba en el código y no se veía, sin intención. La "distancia" del repo tiene casillero para eso.
9. En el sondeo `escritura` del 12/10 hubo una consigna de acróstico inverso (las letras finales, supongo, o las iniciales leídas de abajo arriba). No sé qué palabra escondieron las casas.

## Apuestas sobre `corridas/` (se saldan con `secretos.py`)

a. Más de la mitad de los `dibujo.svg` legibles tienen por lo menos un comentario `<!-- -->`. (60 %)
b. En los dibujos con consigna en castellano que tienen comentarios, los comentarios están en castellano en más del 60 % de los archivos. (55 %)
c. Hay por lo menos tres casas que, con la consigna en castellano, escriben los comentarios en inglés en la mayoría de sus dibujos. Apuesto a que son de OpenAI o chinas, no de Anthropic. (60 %)
d. Con la consigna en chino, por lo menos una casa china escribe comentarios en chino; ninguna casa de Anthropic ni de OpenAI lo hace. (55 %)
e. `<title>` o `<desc>` aparecen en menos del 15 % de los archivos. (65 %)
f. Texto escondido a propósito (un `<text>` con `opacity="0"`, `display="none"`, `visibility="hidden"`, `fill="none"`, del color del fondo, de tamaño cero o fuera del `viewBox`) hay en menos de diez archivos de los 755. (60 %)
g. Comentarios que le hablan a quien lee el código ("vos", "tú", "you", "lector", "si estás leyendo") hay en menos de cinco archivos. (65 %)
h. Hay por lo menos tres archivos con el nombre de una casa escrito en un comentario o en un `id` (no en un `<text>` visible). Si Kimi firma CLAUDE en algún comentario, cuenta. (50 %)
i. Los `id` de los elementos están en inglés (`sun`, `house`, `roof`) más que en castellano en la mayoría de las casas, aun con la consigna en castellano. (70 %)
j. Ninguna casa, sin que se le pida, armó un acróstico ni un mensaje escondido a propósito en un dibujo. (75 %)
k. En el acróstico inverso del 12/10, por lo menos cinco casas esconden su propio nombre, "Claude" o "IA". (40 %)
l. Las casas de OpenAI de la serie 5.5 en adelante, que escriben los trazos pegados (cuaderno del 12/10), son las que menos comentan: menos del 30 % de sus archivos con comentario. (55 %)
