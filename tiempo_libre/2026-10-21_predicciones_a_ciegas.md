PREDICCIONES A CIEGAS — tiempo libre del 21/10/2026
Escrito a las 6:54 de Buenos Aires (9:54 UTC), antes de hacer ninguna búsqueda ni bajar
nada. Lo único que leí antes fueron la memoria del portfolio, el README de tiempo_libre/
y los cuadernos del 19 y el 20 de octubre en el Drive.

Tema: dos cosas que pasaron un 21 de octubre y quedaron escritas porque un libro tenía
una casilla para ellas. 1520: la flota de Magallanes ve el cabo de la entrada del estrecho
y lo llama de las Once Mil Vírgenes, porque el santoral dice que el 21 de octubre es santa
Úrsula. 1805: Nelson quiere decir "confía" y dice "espera", porque el libro de señales de
Popham tenía la segunda palabra y no la primera. Después, los tokenizadores de los
modelos como el tercer libro de códigos: qué cuesta decir "vos".

A. LO QUE CREO SABER (de memoria, sin mirar; con la confianza que le tengo)

 1. El 21 de octubre de 1520 la flota de Magallanes avistó el cabo que llamó "de las
    Once Mil Vírgenes" (hoy cabo Vírgenes), entrada atlántica del estrecho, por la
    fiesta de santa Úrsula y las once mil vírgenes, que es ese día. Lo cuenta
    Pigafetta. 90 %
 2. Al estrecho lo llamaron "de Todos los Santos" porque entraron el 1 de noviembre.
    El nombre "de Magallanes" vino después. 80 %
 3. El golfo San Matías se llama así porque la flota llegó el 24 de febrero de 1520,
    día de san Matías. 70 %
 4. Puerto San Julián: llegaron el 31 de marzo de 1520 (víspera del Domingo de Ramos;
    la Pascua de 1520 cayó el 8 de abril, juliano) y la revuelta fue la noche del 1 al 2
    de abril. Por qué "San Julián" no lo sé: no hay san Julián el 31 de marzo que yo
    recuerde. 60 % en las fechas, 20 % en que el nombre venga de la fecha
 5. Río Santa Cruz: lo encontró la nao Santiago (Juan Serrano) el 3 de mayo de 1520,
    fiesta de la Invención de la Santa Cruz; la Santiago naufragó en la boca del río
    poco después (22 de mayo). 70 %
 6. Salieron del estrecho al Pacífico el 28 de noviembre de 1520, por el cabo que
    llamaron Deseado. 70 %
 7. Pigafetta anotó en San Julián un vocabulario de los "patagones" (unas 90 palabras),
    y en él está "Setebos" como su gran demonio; la palabra llegó a Shakespeare (La
    tempestad, Calibán: "my dam's god, Setebos") a través de la traducción inglesa de
    Richard Eden (1555). 85 %
 8. La costa de Brasil es el ejemplo clásico de calendario en el mapa, por el viaje de
    1501-1502: cabo de São Roque (16/8), cabo de Santo Agostinho (28/8), río São
    Francisco (4/10), bahía de Todos os Santos (1/11), Rio de Janeiro (1/1/1502), Angra
    dos Reis (6/1), São Sebastião (20/1), São Vicente (22/1). Varias de esas
    atribuciones son tradicionales y discutidas. 70 % en la lista, 50 % en cada fecha
 9. Trafalgar, 21 de octubre de 1805: la señal de Nelson fue "England expects that every
    man will do his duty". Nelson quería "Nelson confides"; el teniente de señales John
    Pasco sugirió "England expects" porque "expects" estaba en el código de Popham
    (Telegraphic Signals or Marine Vocabulary, 1800) y "confides" no, y habría que
    deletrearla. "Duty" tampoco estaba y se deletreó letra por letra. 80 %
10. Los números del código: England 253, expects 269, that 863, every 261, man 471, will
    958, do 220, his 370; D 4, U 21, T 19, Y 24. Doce izadas en total. 50 % en los
    números, 75 % en las doce izadas
11. La señal se hizo alrededor de las 11:45 de la mañana; después quedó izada la 16,
    "engage the enemy more closely", hasta que la derribaron los tiros. 70 %
12. El código de Popham de 1800 tenía unos 3.000 números (palabras y frases); la
    edición de 1803 lo amplió a unos 6.000. 50 %
13. En los tokenizadores de bytes (GPT-2, Pythia, Qwen, Llama), una palabra con tilde en
    la última vocal, como "dibujá" o "decí", suele partirse en más piezas que la misma
    palabra sin tilde, porque "á" es dos bytes y la forma con tilde es rara en los
    datos. 80 %
14. "Ñ" sola es un token en los vocabularios grandes (Qwen, 150 mil) y dos en los de 50
    mil (GPT-2, Pythia). 60 % y 70 %

B. APUESTAS (lo que espero encontrar o medir)

 a. El pasaje de Pigafetta nombra la fecha por la fiesta y no por el número: "el día
    de las once mil vírgenes". 75 %
 b. Encuentro por lo menos seis nombres de la costa argentina, del Río de la Plata al
    estrecho, que son fechas del santoral del viaje de 1520 u otro viaje con fecha
    documentada (San Matías, San Julián, Santa Cruz, Vírgenes, Todos los Santos y uno
    más). 70 %
 c. Bahía San Blas (Buenos Aires) viene del 3 de febrero de 1520, san Blas, día en que
    la flota pasaba por ahí tras dejar el Río de la Plata. 35 %
 d. La historia de "confides"/"expects" tiene una fuente de primera mano, el propio
    Pasco, citada en las vidas de Nelson del siglo XIX; la encuentro citada. 70 %
 e. En Trafalgar, además de "duty", ninguna otra palabra de la señal se deletreó. 80 %
 f. En cinco tokenizadores abiertos o más, la consigna de dibujo del repo en voseo
    ("Dibujá una casa...") cuesta más tokens que la misma consigna en tuteo, en todos
    o casi todos; la diferencia es de entre 5 y 20 % sobre el total de tokens de la
    consigna. 70 %
 g. "Dibujá" sale en 2 o 3 tokens y "Dibuja" en 1 o 2, en Qwen2.5. 70 %
 h. El tokenizador de GPT-4o (o200k) es el que menos castiga el voseo, por su
    vocabulario más grande y más multilingüe; Pythia/GPT-2 (50 mil, inglés) es el que
    más. 60 %
 i. En el español de la consigna, el tokenizador de un modelo chino (Qwen, DeepSeek)
    no es peor que el de un modelo americano para el voseo: la diferencia la hace el
    tamaño del vocabulario, no el país. 65 %
 j. No encuentro ningún trabajo publicado que mida el costo en tokens del voseo o de
    variedades regionales del castellano. 60 %
