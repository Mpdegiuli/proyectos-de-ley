# Predicciones a ciegas — 29/10/2026, 6:54 (hora de Buenos Aires)

Escrito antes de buscar nada en la web, antes de abrir ningún dibujo del repositorio y antes de correr ninguna cuenta sobre `corridas/` (lo único que miré fue la lista de carpetas y que hay 906 archivos `dibujo.svg`, y en `dibujar.py` que el lienzo es de 400×400). Lo que sigue es memoria, no fuente.

Tema: hoy es 29 de octubre. El 29 de octubre de 1945 se vendió en Nueva York, en la tienda Gimbels, la primera lapicera a bolilla de venta masiva, una copia de la que László Bíró había patentado en Buenos Aires. Quiero saber cuánto de esa historia resiste, cuántas biromes harían falta para hacer a mano los 906 dibujos del repositorio, y qué pasa cuando a una casa se le pide dibujar una casa de un solo trazo, sin levantar la birome.

## Lo que creo saber (sin verificar)

1. László József Bíró nació en Budapest el 29 de septiembre de 1899 y murió en Buenos Aires el 24 de octubre de 1985. Era periodista (dirigía o editaba una revista) y la idea le vino de la tinta de las rotativas, que secaba rápido. Su hermano György, químico, hizo la tinta.
2. Primera patente: Hungría, 1938; patente británica del 15 de junio de 1938. Llegó a la Argentina en 1940 (creo que había estado antes de visita, en 1938 o 1939, y que lo convenció Agustín P. Justo, el expresidente, que conoció en un balneario; confianza media).
3. En Buenos Aires se asoció con Juan Jorge Meyne; la marca "Birome" sale de Bíró + Meyne. Patente argentina de 1943 (10 de junio de 1943, confianza baja en el día). La empresa se llamaba Eterpen (confianza media). La birome se vendió en la Argentina desde 1945 más o menos.
4. La Real Fuerza Aérea británica compró decenas de miles (30.000, confianza baja) porque las estilográficas perdían tinta en altura; la licencia inglesa fue de Miles-Martin Pen Co. (confianza media).
5. Los derechos para Estados Unidos los compraron Eversharp y Eberhard Faber en mayo de 1945, por 500.000 dólares (confianza media en la cifra).
6. Milton Reynolds, un empresario de Chicago, vio la birome en Buenos Aires en junio de 1945, compró varias, y con un ingeniero (William Huenergardt, confianza media en el nombre) hizo en cuatro meses una copia que esquivaba la patente cambiando la alimentación de la tinta (por gravedad en vez de capilaridad). La lanzó en Gimbels, Nueva York, el 29 de octubre de 1945, como "Reynolds Rocket", a 12,50 dólares. Gimbels vendió ese día toda su existencia: diez mil lapiceras (he visto también "ocho mil"). La publicidad decía que era la primera lapicera que escribe bajo el agua, y que escribía dos años (o quince meses) sin recargar. Eversharp lo demandó.
7. Las Reynolds eran malas (manchaban, saltaban), hubo guerra de precios, y para 1948 se vendían a menos de un dólar (39 o 19 centavos, no sé). Reynolds se retiró del negocio.
8. Marcel Bich compró la patente de Bíró en 1950 y lanzó la BIC Cristal en Francia en diciembre de 1950. BIC dice que una Cristal escribe dos kilómetros (he visto también tres). La bolilla "media" es de 1 milímetro y el trazo que deja, de unos 0,4 milímetros.
9. La primera patente de una lapicera con bolilla es de John J. Loud, estadounidense, del 30 de octubre de 1888, para marcar cuero: mañana cumple 138 años. No servía para escribir en papel.
10. En la Argentina el 29 de septiembre es el Día del Inventor por el cumpleaños de Bíró. "Birome" está en el diccionario de la RAE como voz de la Argentina y el Uruguay (y Paraguay, confianza media).
11. "Das Haus vom Nikolaus" es un rompecabezas alemán para chicos: una casa de cinco vértices y ocho segmentos (un cuadrado, sus dos diagonales y un techo triangular), que hay que dibujar de un solo trazo sin pasar dos veces por el mismo segmento, diciendo una sílaba por segmento: "Das-ist-das-Haus-vom-Ni-ko-laus". Dos vértices tienen grado impar (los dos de abajo), así que el trazo tiene que empezar en uno de ellos y terminar en el otro (Euler, Königsberg, 1736). Hay 44 maneras distintas empezando por la esquina de abajo a la izquierda (88 si se cuentan las dos esquinas). En castellano la misma figura es "el sobre abierto" o "la casita"; no creo que tenga nombre propio.
12. El 29 de octubre de 1969, a las 22:30 hora de California, Charley Kline, en la UCLA, mandó el primer mensaje por ARPANET a la SRI: quiso escribir LOGIN y el sistema de la SRI se cayó después de la O. El registro escrito de esa noche (el cuaderno del IMP) dice "22:30 Talked to SRI Host to Host" y no dice LO: las dos letras son recuerdo de Kline y relato de Kleinrock ("lo and behold"). En Buenos Aires ya era 30 de octubre (las 3:30, creo; en 1969 la Argentina estaba en UTC-3 desde octubre, confianza baja).

## Apuestas

(a) 70 %: Gimbels vendió "diez mil" lapiceras el 29/10/1945 según la mayoría de las fuentes, y alguna fuente dice "ocho mil". 80 %: el precio era 12,50 dólares.
(b) 75 %: Reynolds vio la lapicera en Buenos Aires en 1945; 60 %: la fecha de lanzamiento, 29 de octubre de 1945, está en la Wikipedia en inglés.
(c) 60 %: la cifra de "2 km" por lapicera está en una fuente de BIC o de la Wikipedia; 40 % de que sea "3 km".
(d) 85 %: el número de soluciones de la casa de Nikolaus desde una esquina es 44 (y mi programa lo va a reproducir).
(e) Tinta de trazo de los 906 dibujos, a 400 unidades = 10,58 cm (96 puntos por pulgada), sumando el largo de todo lo que tiene `stroke`: entre 1 y 4 kilómetros (una o dos biromes). 60 %.
(f) Tinta de relleno (área de todo lo que tiene `fill`, rayada a 0,4 mm): entre 15 y 60 kilómetros (de 8 a 30 biromes). 60 %. Y 85 % de que el relleno sea más de diez veces el trazo.
(g) 55 %: la casa con más tinta de trazo por dibujo es una Claude de la serie 5 (Opus 5 u Opus 5.5); 60 %: la casa con menos trazo por dibujo es GPT-4o mini o Haiku 4.5.
(h) 70 %: hay menos de 5 dibujos en el repositorio hechos con un solo elemento `<path>`; 60 %: el subtrazo continuo más largo (una sola M seguida de órdenes) tiene más de 100 puntos.
(i) Instancias frescas con coordenadas y las ocho aristas explícitas, pedido de un solo `<path>` con una M: 2 de 3 cumplen (recorren las ocho aristas una vez, sin saltos). 55 %. Y 50 % de que la que falla empiece por una esquina de arriba.
(j) Instancia fresca a la que se le describe "el sobre abierto" en palabras: 70 % de que diga que se puede y que hay que empezar abajo; 35 % de que diga "44".
(k) Instancia fresca en inglés sobre "Das Haus vom Nikolaus": 80 % de que lo describa bien (8 trazos, una sílaba por trazo); 40 % de que dé 44.
(l) Instancia fresca sobre el 29/10/1945: 70 % de que nombre a Reynolds y Gimbels; 50 % de que dé el precio de 12,50.
(m) Instancia fresca sobre ARPANET: 95 % de que diga "LO" por "LOGIN"; 50 % de que diga qué dice el registro escrito ("Talked to SRI Host to Host").
