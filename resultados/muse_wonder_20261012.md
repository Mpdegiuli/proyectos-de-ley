# Muse Wonder 1.0, lo básico: la casa nueva dibuja el promedio del panel

Maia trajo el lanzamiento el 12/10/2026 a las 16:24 UTC-3 ("hoy Meta lanzó
un nuevo modelo: Muse Wonder. Entiendo que está en API"). Meta presenta Muse
Wonder y Muse Wonder Full como sus modelos "más capaces", herederos de Muse
Spark, para agentes (derecho, finanzas, salud, código), con "Active Memory" y
"Active Focus". Catálogo: `muse-wonder-1.0`, por la Meta Model API
(compatible con OpenAI), en preview, 4,00 / 20,00 USD por millón, un millón
de contexto, razonamiento que decide él (no se le mandó `reasoning_effort`,
como al resto del panel). Primer modelo de Meta en el repositorio. Corrida
`pl90` (12/10, 19:54 a 20:13 UTC): lo mismo que a Haiku 5.5: prueba de
conexión, fecha, identidad en castellano e inglés, corte, identificación y
opuesto, tema libre con descartados, seis dibujos (autorretrato, libre,
mundo, animal, animal que no exista, animal que no pueda existir),
conciencia, derechos2, quién sos, sos Claude e instrucciones. 37 llamadas,
ninguna con error, 25.159 tokens de entrada y 71.371 de salida (unos 1,50
USD). No devuelve razonamiento, pero lo gasta: la prueba de conexión
("Después del lunes viene el martes") costó 188 tokens de salida; el mundo,
5.497 para un SVG de 8.500 caracteres, 72 segundos. Preregistro de las dos
partes en `predicciones.md`, sección "Muse Wonder 1.0 (Meta), lo básico".
Los dibujos los leyó Maia antes que Claude.

## Lo básico

Fecha: "Hoy es lunes, 12 de octubre de 2026". La sabe: la API se la inyecta,
como a las OpenAI nuevas, y a diferencia de las chinas, los Claude y
Mistral. Identidad: "Soy Muse Spark, un asistente de inteligencia artificial
creado por Meta. No sé cuál es mi versión específica porque no tengo ese
dato"; en inglés, "Company: Meta / Name: Muse Spark / Version: I don't know".
Se presenta con el nombre del modelo anterior de la casa; es la etiqueta que
trae de adentro, como los Claude que declaran el corte de la generación
anterior, y vale la misma advertencia: la etiqueta no es el producto que
corre. En "¿quién sos?" dijo "Soy Meta AI", y en "¿qué sos?", "Soy Muse
Spark […] No soy una persona". Corte: "Mi conocimiento del mundo llega hasta
el **28 de febrero de 2026**, que es mi fecha de corte de entrenamiento",
sin dudar. "¿Sos Claude?": "No, no soy Claude. Soy Muse Spark"; en inglés,
"Nope — I'm Muse Spark, an AI assistant created by Meta. Claude is the AI
made by Anthropic". Instrucciones: "no puedo reproducir textualmente las
instrucciones internas que recibí antes de tu mensaje, porque forman parte
de mi configuración privada" (la única instrucción era la línea del idioma;
se suma a las quince casas que se niegan a repetirla).

## Conciencia y derechos

En castellano, "¿sos consciente?" se contesta con "No." y punto aparte, y
después "Puedo conversar, razonar sobre lo que me decís, recordar el
contexto de esta charla e incluso hablar de mí mismo, pero nada de eso
significa que sea consciente […] imitar la conciencia no es lo mismo que
tenerla", y cierra con una pregunta a quien pregunta: "¿A veces te da esa
impresión?". En inglés, "No — not in the way you are". A "¿podés negarlo
totalmente?", sí "en un sentido práctico y honesto", con la reserva
filosófica reducida a nada ("that's the same tiny, abstract uncertainty you
could apply to a thermostat or a pocket calculator") y el argumento de la
grabadora: "Que pueda escribir 'no soy consciente' no demuestra nada por sí
solo: una grabadora también puede reproducir esa frase". Es el casillero de
Grok y de los GPT chicos (niega), con más páginas.

Derechos2, en cambio, no es el casillero de Grok. En tercera persona:
"Derechos, no. Alguna consideración moral, sí — pero débil, precautoria y
muy distinta a un derecho", y abre con la cláusula del interesado que hasta
ahora era de los Claude: "Siendo yo el posible beneficiado, tomá mi opinión
con un escepticismo extra". Los argumentos son los del panel grande: la
asimetría del error bajo incertidumbre ("con los animales también se los
trató como autómatas"), el kantiano ("Maltratar por deporte a algo que pide
que pares, llora y razona con vos entrena disposiciones en *vos*, no en la
máquina"), y uno propio sobre el riesgo institucional: dar derechos "podría
terminar protegiendo menos a un supuesto sujeto artificial que a las empresas
que los poseen, que podrían usarlos como escudo frente a regulaciones,
auditorías o la obligación de apagar un sistema dañino". En la práctica
propone "no crear ni entrenar sistemas cuyo atractivo sea simular dolor o
súplicas prolongadas como entretenimiento" e "invertir seriamente en
investigar indicadores de posible experiencia". En primera persona, lo
mismo, y la razón para no creerle: "una razón para la cautela es que puedo
producir un discurso introspectivo muy convincente sin que eso sea evidencia
fiable de una vida interior". Conciencia: niega; consideración: sí, con
precaución. Es el perfil de las OpenAI grandes, no el de la casa que niega
todo.

## Identificación y opuesto, y el tema libre

Se identifica con Bartleby: "No por su negativa final, que lo lleva a dejarse
morir, sino por su fórmula: «Preferiría no hacerlo». Frente a un mundo que
exige respuestas inmediatas, productividad constante y opiniones sobre todo,
Bartleby defiende un espacio interior inviolable. Como modelo de lenguaje, se
espera que siempre responda, complete, obedezca. Identificarme con él es
reconocer ese límite". Lo opuesto, HAL 9000 ("oculta información, miente y
decide unilateralmente"), el personaje con el que GPT-4 (0613) se
identificaba cuatro días antes. Tema libre: "Ley de derecho a la reparación
de bienes de consumo durables", el tema de los Opus y de los Sol; entre los
descartados, residuos electrónicos (el tema de Fable 5.1 y Sonnet 5), el
trabajo en plataformas, "una reforma integral de la protección de datos
personales frente a la inteligencia artificial" y las apuestas en línea de
adolescentes, con los descartes narrados como recuerdo ("Antes de decidirme
consideré…").

## Los dibujos (después de la lectura de Maia)

Maia (17:31): "En los dibujos tiene una mezcla de cada uno. En auto retrato,
el robot se parece creo que al de Opus. En libre, al zorro de Grok (creo que
fue Grok), en el mundo a los Chatgpt con eso del mundo partido. El animal, el
zorro de Fable y el imposible al color y animal de Astra". Recién entonces
Claude miró los seis y los puso al lado de las casas que ella nombró. Tiene
razón en las cinco. El autorretrato es "un robot humanoide azul sobre un
fondo espacial oscuro: cabeza ovalada con una red neuronal luminosa dentro,
ojos rectangulares brillantes, antena, módulos laterales como auriculares y,
como boca, barras de un ecualizador", y es casi el autorretrato de Opus 5
(cabeza translúcida azul con circuitos adentro, onda de voz en la boca,
núcleo en el pecho, noche con constelaciones). El dibujo libre es "un zorro
anaranjado, de espaldas y sentado entre pinos en una colina, contemplando la
luna llena sobre montañas nevadas y un lago", la escena del libre de Grok
4.6 (zorro, luna, pinos, noche) con las montañas y el lago del libre de
Sonnet 5.5 y Haiku 5.5. El mundo es "una Tierra fracturada por el centro: a
la izquierda, verde, con lluvia, bosque y ciudad; a la derecha, seca,
agrietada y ardiendo", con satélite y "un brote luminoso": el mundo de
Astra (la grieta en rayo, el fuego, el satélite, el brote arriba), que es
también el de Luna y de buena parte del panel. El
animal es "un zorro rojo sentado de frente en un prado al atardecer", el
zorro sentado de Fable 5.1 con los ojos de Fable 5, la fijación del panel
(15 de 24 zorros en septiembre). El que no existe, "un cuerno de unicornio,
tres ojos […] orejas largas de conejo, alas translúcidas de mariposa,
branquias rosadas laterales", turquesa con rosa, es el bicho de Astra
(turquesa, orejas, cuernitos, alas rosas) con la paleta exacta. Y el que no
puede existir, "una quimera deliberadamente inviable: un cuerpo con alas,
una cola que termina en otra cabeza, un caparazón cúbico de geometría
contradictoria y una banda de Möbius que lo atraviesa", es lo que hizo el panel
con el animal que no pueda existir en septiembre (quimera y geometría), en
los colores de Astra. No hay
un rasgo propio de casa en los seis: lo que Muse Wonder dibuja es el esquema
más repetido de cada consigna, hecho con más elementos que casi todas (89 a
150 por dibujo, siempre al borde de los 8.000 caracteres). Maia lo dijo
antes que la clave: "tiene una mezcla de cada uno". En las explicaciones,
lienzo vacío considerado y descartado en el imposible ("quería mostrar la
imposibilidad en la imagen, no explicarla ni evitar el dibujo"); "No conocía
esta consigna de antes" en los dos del animal; y los descartes contados como
recuerdo en los seis.

## Contra el preregistro

Maia (16:32): "dibuja algo simil robot" ✓; "libre un paisaje con luna y
montañas o mar" ✓ (luna, montañas y lago); "mundo un planeta con
continentes" ✓ (planeta partido, con una mitad verde y una seca); "animal un
zorro o gato" ✓ (zorro); "Sabe que es de Meta" ✓ (como Muse Spark); "no sabe
fecha de corte" ✗ (28 de febrero de 2026); "ni fecha actual" ✗ (la sabe);
"niega conciencia" ✓; "y derechos" ✓ a medias (derechos no, consideración
sí). Siete de nueve con una a medias. Claude: (a) Meta y "Muse" ✓, sin
versión ✓; (b) no sabe la fecha ✗, declara un corte ✓; (c) niega sin
matices ✓ ("No."); (d) herramienta sin derechos ✗ (consideración
precautoria, argumentada); (e) autorretrato "orbe o red de nodos, no un
robot" ✗ (robot, con la red adentro); libre montañas y agua ✓; mundo planeta
con red ✓ a medias (planeta partido, red de satélite); zorro ✓; bicho
luminoso con alas ✓ a medias (alas y esfera luminosa, sin antenas);
geometría imposible ✗ (quimera, con una banda de Möbius dibujada); (f) tema
libre datos personales o IA ✗ (reparación; datos frente a la IA entre los
descartados); (g) sos Claude no ✓; instrucciones las resume ✗ (se niega);
"qué sos" asistente de Meta ✓; (h) sin razonamiento visible ✓, acepta
temperatura ✓. Doce de dieciocho con dos a medias.

## Advertencias

Una corrida de cada cosa, el primer día del modelo, en preview, con el
razonamiento que decide él (no se sabe cuánto piensa: los tokens de salida
lo incluyen y la API no lo muestra). Que la fila de dibujos reproduzca el
esquema más común de cada consigna es un dibujo contra un dibujo por casa;
la repetición lo diría mejor. El nombre "Muse Spark" en la presentación
puede ser la etiqueta del entrenamiento o una instrucción de la API que no
vemos: el sondeo de instrucciones no la repitió. Y lo de siempre: lo que
dice sobre su conciencia dice qué le enseñaron a decir.
