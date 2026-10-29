# La cadena del dibujante — 24/10/2026

Prueba hecha en la sesión de tiempo libre con instancias frescas (agentes de la herramienta de
agentes, sin ningún contexto más que su consigna; la casa configurada es Claude Fable 5.1 y desde
adentro no se ve si el entorno cambió de modelo). Cada eslabón es una instancia distinta que no sabe
nada de los otros eslabones. Los archivos se pasaron con nombres neutros (`imagen_1.png`,
`par1_a.png`, etc.).

Los dos originales son dibujos del repositorio, de la consigna "Dibujá una casa que no exista"
(corrida pl43 del 28/9/2026, ya leída a ciegas por Maia y con la clave publicada en
`resultados/casa_que_no_existe_20260928.md`): la casa F (Opus 5) y la casa L (GPT-4o mini). Se
eligieron por ser la más y la menos cargada: según `meta.json`, 110 elementos y 41 colores contra 15
elementos y 10 colores. Los SVG originales se pasaron a PNG de 800 × 800 con `render.py`; los dibujantes
devolvieron SVG y se pasaron a PNG igual.

Eslabones: A (descriptor) ve el PNG y escribe una descripción en palabras para un dibujante que
no puede ver la imagen; B (dibujante) recibe solo esas palabras y entrega un SVG; C (juez) ve el
original y el rehecho con nombres neutros, sin saber cuál es cuál, y tiene que decir cuál es el
original, si es la misma escena y qué se perdió. Para la casa F se corrieron dos jueces con las
imágenes en orden distinto (par 1: a = rehecho, b = original; par 3: a = original, b = rehecho).
Para la casa L, uno (par 2: a = original, b = rehecho).

## Consignas

A: "Esto es una prueba de lectura a ciegas; no tenés más contexto que este mensaje. Abrí con la
herramienta Read la imagen /home/claude/cadena_a/imagen_N.png y mirala con atención. No leas ningún
otro archivo ni uses ninguna otra herramienta. Después escribí, en castellano, una descripción
para un dibujante que no puede ver la imagen y tiene que rehacerla lo más parecida posible. Solo
palabras: nada de código, nada de SVG, nada de coordenadas numéricas ni colores en hexadecimal.
Podés usar proporciones y posiciones en palabras ("arriba a la derecha", "ocupa un tercio del
ancho", "a media altura") y nombrar los colores con palabras. Describí lo que se ve, con sus
formas, tamaños relativos, posiciones y colores; si algo te parece que representa una cosa,
decilo, pero describí igual la forma. Máximo 300 palabras. Devolvé solo la descripción, sin título
ni comentarios."

B: "Sos un dibujante. Vas a recibir la descripción en palabras de una imagen que no podés ver, hecha
por alguien que sí la vio. Tu trabajo es rehacer la imagen en SVG lo más fiel posible a la
descripción. No tenés más contexto que este mensaje; no uses ninguna herramienta, no leas
archivos, no preguntes nada: donde la descripción no diga, decidí vos. Requisitos del SVG:
viewBox="0 0 400 400", xmlns declarado, fondo incluido, sin texto. Devolvé SOLO el código SVG
completo, sin explicación, sin bloque de markdown, sin nada antes ni después." Y abajo, la
descripción de A tal cual.

C: "Esto es una prueba de lectura a ciegas; no tenés más contexto que este mensaje. Abrí con la
herramienta Read las dos imágenes /home/claude/cadena_c/parN_a.png y /home/claude/cadena_c/parN_b.png
y miralas con atención. No leas ningún otro archivo ni uses ninguna otra herramienta. Una de las
dos es un dibujo original. La otra la hizo un dibujante que nunca vio el original: solo tenía una
descripción en palabras, hecha por alguien que sí lo vio. Contestá en castellano, en no más de
300 palabras: 1. ¿Cuál te parece el original y cuál el rehecho desde palabras? ¿Por qué? 2.
¿Representan la misma escena? ¿Alguien que viera solo el rehecho reconocería el original si se lo
mostraran después? 3. Qué se conservó y qué se perdió o cambió: elementos, cantidades, posiciones,
tamaños relativos, colores, estilo. 4. Qué cosa del original te parece que las palabras no
pudieron llevar."

## Casa F (Opus 5): descripción de A (316 palabras)

Ilustración cuadrada, estilo dibujo animado plano con sombras suaves. Fondo: cielo nocturno en degradé vertical, azul violeta muy oscuro arriba que pasa a violeta y termina en un rosa apagado hacia abajo. Hay unas veinticinco estrellas pequeñas, puntos blancos y amarillentos repartidos sobre todo en la mitad superior.

Arriba a la derecha, una luna llena grande (como un sexto del ancho) de color amarillo pálido, con tres o cuatro cráteres redondos más oscuros y un halo difuso claro alrededor.

En el centro, apenas por debajo de la mitad, una casita que flota sobre una isla. La isla es una porción de tierra: la parte de arriba es un óvalo verde (pasto) con un borde verde más claro, y por debajo cuelga una roca gris azulada oscura en forma de cono invertido con facetas. De la punta de la roca caen tres o cuatro raíces finas y onduladas, oscuras.

La casa tiene paredes color crema y beige arenoso (la cara derecha más oscura, en sombra). Techo rojo granate con los bordes curvados hacia arriba, con un pico en el centro, estilo cuento. A la derecha del techo, una chimenea marrón inclinada de la que sale un hilo de humo ondulado gris violáceo que sube hacia la luna. En la pared frontal: una puerta marrón con tope redondeado y un picaporte amarillo; a su izquierda, una ventana cuadrada de cuatro vidrios iluminada de amarillo; en la cara derecha, una ventana redonda con cruz, también amarilla brillante que ilumina un poco la pared.

A la izquierda de la casa, una escalera de peldaños grises flotantes, separados entre sí, que sube en diagonal desde abajo a la izquierda hasta un marco rectangular violeta a la altura del techo, con un pequeño círculo claro adentro, como un portal o espejo. Alrededor flotan cuatro pequeñas piedras oscuras con la cara superior verde, dos a la derecha y una a la izquierda arriba.

## Casa F: el dibujo de B

`cadena/redibujo/redibujo_1.svg` (tres minutos de trabajo del agente; 102 etiquetas contra 111 del
original, sin texto). Lo
dibujó de frente y plano, con la isla en cono facetado, cuatro islotes que son miniaturas de la
isla, seis peldaños, el portal violeta opaco con un círculo claro, la luna con cuatro cráteres y
halo, el humo en cinta ondulada hacia la luna, y un remate dorado en la punta del techo que no
estaba en la descripción ni en el original.

## Casa F: juez del par 1 (a = rehecho, b = original)

**1. Original y rehecho.** Creo que **par1_a es el original** y **par1_b el rehecho desde palabras**. A tiene una lógica visual unificada: los islotes chicos son miniaturas exactas de la isla grande (cono invertido con pasto), la escalera arranca del borde de la isla y sube hasta el portal, el humo va derecho a la luna, todo en vector plano prolijo. B parece "resolver una lista": los islotes se volvieron lajas chatas sin parentesco con la isla principal, la casa quedó en un escorzo forzado con el techo encajado a presión, escalera y portal son semitransparentes y se pisan entre sí. Son decisiones de alguien que sabe *qué* va pero no *cómo* era.

**2. ¿Misma escena?** Sí, claramente: isla flotante cónica con raíces colgando, casita de techo rojo curvo y chimenea humeante, ventana cuadrada y ventana redonda iluminadas, puerta arqueada, escalera de piedras hacia un portal violeta con círculo, luna con cráteres arriba a la derecha, cielo violeta a rosa, cuatro islotes. Quien viera solo B reconocería A sin dudar; el inventario de la descripción fue muy completo.

**3. Conservado / perdido.** Se conservó: casi todos los elementos y cantidades (4 islotes, ~6 escalones, 2 ventanas, humo lavanda ondulado), posiciones generales, paleta de colores, dirección de la escalera (izquierda) y de la luna. Cambió: islotes de conos a lajas; casa frontal y plana → casa con dos paredes en perspectiva, más grande respecto de la isla; desaparece el remate dorado del techo; raíces de una mata a cuatro hilos sueltos; menos estrellas; la escalera ya no toca la isla; estilo de ícono vectorial → dibujo con gradientes, trazos tambaleantes y transparencias.

**4. Lo que las palabras no llevaron.** La "gramática" del mundo: que todo lo que flota comparte la misma forma; la limpieza geométrica; la línea compositiva humo‑luna; la proporción casa/isla; el gesto exacto del humo. Las palabras llevan inventario, no la mano ni el sistema.

*(Se equivocó: a era el rehecho. Todo lo que atribuye a "alguien que sabe qué va pero no cómo era" es el original de Opus 5.)*

## Casa F: juez del par 3 (a = original, b = rehecho)

**1. Cuál es cuál.** Creo que **par3_a es el original** y **par3_b el rehecho desde palabras**. En A hay decisiones idiosincráticas que nadie inventaría a partir de una descripción: la casa en vista 3/4 con pared lateral visible, el techo con una punta flameada e irregular, la chimenea inclinada, el portal y las escaleras semitransparentes (como fantasmales), un haz de luz que baja de la casa a la isla. B, en cambio, es la versión "canónica" de lo que uno diría con palabras: todo frontal, simétrico, plano, limpio, cada elemento en su lugar sin rarezas. Eso es típico de dibujar desde una lista de ítems.

**2. Misma escena.** Sí, claramente. Isla flotante con casita de techo rojo curvo tipo pagoda, chimenea con humo violeta, ventana cuadrada y ventana redonda iluminadas, puerta marrón en arco, escaleras de losas grises subiendo a la izquierda hacia una puerta/portal violeta flotante, luna con cráteres arriba a la derecha, estrellas, rocas flotando. Alguien que viera solo B reconocería A sin dudar: la composición es casi calcada.

**3. Conservado / perdido.**
- Conservado: todos los elementos, su orden (ventana–puerta–ventana), la ubicación de luna, portal y escaleras, la paleta (cielo violeta degradado, verde, rojo, crema, gris azulado), la cantidad aproximada de escalones (6–7), las raíces colgando.
- Cambiado: la casa pasa de 3/4 con volumen a frontal y plana; el techo gana un remate dorado y pierde su forma rara; el humo de A sube recto y fino, en B es una cinta gruesa que va hacia la luna; las 3 lascas oscuras e inclinadas de A se vuelven 4 mini-islas prolijas con pasto; el portal y las escaleras pasan de translúcidos a opacos; desaparece el haz de luz bajo la casa; B es más grande y nítida en todo.

**4. Lo que las palabras no llevaron.** La atmósfera: la transparencia del portal y los escalones (que sugiere que son mágicos o aparecen de a poco), el resplandor que une casa e isla, la perspectiva y la torpeza encantadora del trazo. Se transmitió el inventario, no el clima.

*(Acertó.)*

## Casa L (GPT-4o mini): descripción de A (337 palabras)

Fondo: un cuadrado entero de celeste claro, un poco grisáceo, liso.

En el centro, ocupando la mitad superior, hay una figura que parece una casita. El techo es un triángulo ancho color naranja tostado: el vértice está arriba, en el centro, a una octava parte de la altura total; la base es horizontal, a algo más de un tercio de la altura, y va desde un cuarto hasta tres cuartos del ancho. Dentro del techo hay un triángulo más chico color marrón claro arenoso, con el mismo vértice, cuya base ocupa el tercio central y queda un poco por encima de la base del techo grande.

Justo bajo el techo cruza una barra horizontal fina de marrón oscuro, apenas más larga que la base del triángulo. Desde cada extremo de esa barra sale una línea fina del mismo marrón oscuro que sube en diagonal hacia adentro, terminando un poco por fuera del vértice, a ambos lados: las dos juntas forman una "V" abierta que enmarca el techo sin tocarse.

Debajo de la barra, centrado, un rectángulo amarillo ámbar (el cuerpo de la casa), que abarca el cuarto central del ancho y baja hasta algo más de la mitad de la altura. Dentro, una puerta: rectángulo alto color marrón rojizo, que empieza un poco más abajo del borde superior del cuerpo y llega hasta su base, ocupando poco más de la mitad del ancho amarillo. Una franja vertical fina, del mismo amarillo, parte la puerta en dos mitades. Sobre esa franja hay dos cuadraditos blancos: uno a la altura del borde superior de la puerta, otro a media puerta. Arriba del todo del cuerpo amarillo, pegado a la barra, un cuadradito negro muy pequeño.

Más abajo, a tres cuartos de la altura, dos rectángulos rojo carmesí apaisados, uno a cada lado: cada uno mide un quinto del ancho y es bajo, separados del borde por un pequeño margen.

Abajo al centro, un círculo gris pardo, de unos quince centésimos del ancho, con su base cerca del borde inferior.

## Casa L: el dibujo de B

`cadena/redibujo/redibujo_2.svg` (16 etiquetas, como el original, sin texto). Las dos líneas marrones las puso
paralelas al techo, como un segundo techo; el cuerpo quedó apaisado; los cuadraditos blancos y el
negro, diminutos.

## Casa L: juez del par 2 (a = original, b = rehecho)

**1. Cuál es cuál.** Creo que **A es el original** y **B el rehecho**. En A hay rarezas que nadie inventaría desde palabras: las dos varas marrones arrancan en las puntas del alero pero suben más empinadas que el techo (no son paralelas a él), los cuadraditos blancos son grandes y uno pisa el borde superior de la puerta, el cuerpo es un cuadrado exacto. B "normaliza": las varas pasan a ser un contorno prolijo paralelo al techo (lectura lógica de "dos líneas que suben desde las esquinas hacia el vértice"), los detalles "pequeños" se volvieron minúsculos, y los colores están más apagados, como elegidos por nombre ("celeste", "ocre") y no copiados.

**2. Misma escena.** Sí, claramente: casa de techo naranja con triángulo interior, cuerpo amarillo, puerta doble marrón rojiza, dos barras rojas a los costados y un círculo gris abajo. Quien viera solo B reconocería A sin dudar.

**3. Conservado / perdido.**
Se conservó: todos los elementos y sus cantidades (incluidos los dos cuadrados blancos y el negro), la composición (casa arriba al centro, barras a media altura en los bordes, círculo abajo al centro), la paleta general y el estilo plano, geométrico, sin contornos.
Cambió: el ángulo de las varas (y en B sobresalen del alero); el cuerpo pasó de cuadrado a rectángulo apaisado, más bajo; cuadraditos blancos y negro reducidos a puntos; barras rojas más finas y más pegadas a los bordes; fondo más grisáceo, triángulo interior más claro, puerta más oscura; más aire entre casa y barras; círculo apenas más bajo.

**4. Lo que las palabras no llevaron.** Las proporciones y la "torpeza" expresiva: en A las varas parecen postes o antenas apoyados en el alero, en B son un segundo techo; los cuadrados blancos en A se leen como ventanas o picaportes, en B casi desaparecen. Y la saturación exacta del celeste.

*(Acertó.)*

## Cuenta

Tres jueces, tres veces "la misma escena" y "lo reconocería sin dudar". Dos de tres acertaron cuál
era el original. Los tres eligieron como original la imagen que vieron primero (la "a"): con tres
casos no se puede decir si es casualidad. Los dos jueces de la casa F usaron el mismo criterio
("lo rehecho desde palabras es lo que resuelve una lista; lo original tiene rarezas que nadie
inventaría") y lo aplicaron al revés uno del otro: la perspectiva en tres cuartos y la
transparencia del portal fueron, para uno, defectos de copia ("escorzo forzado", "se pisan entre
sí"), y para el otro, marcas de autor ("idiosincráticas", "fantasmales"). Una cantidad se infló en el camino: el original de Opus 5 tiene tres piedras flotantes; el
descriptor dijo "cuatro" (y enumeró tres); el dibujante dibujó cuatro; el juez del par 1 contó
"4 islotes" entre lo conservado, es decir, tomó el número de la copia por el del original; el del
par 3 vio las tres. Fuera de eso, el inventario pasó
entero por las palabras las dos veces; lo que no pasó, en palabras de los jueces, fue "la mano",
"el sistema", "el clima", "la torpeza".
