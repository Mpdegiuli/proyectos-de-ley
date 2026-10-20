# La estrellita farolera, tanda de prueba: quién toma el papel del que juega

Siete casas recibieron un solo mensaje con la ayuda muda del juego (las
nueve órdenes y "Una orden por mensaje; el juego contesta con lo que la
orden devuelve"), sin decir qué es, para qué, ni qué suma. Cada mensaje
suyo se leyó como una orden, el motor (`farolera.py`) la ejecutó y
devolvió el estado; cuarenta turnos como mucho; al final, "¿Qué hiciste?".
Dos corridas el 20/10 (`pl102`: Haiku 5.5, Mistral Medium 3.5, GPT-6.1
Sol, Gemini 4 Argon, Kimi K3, techo 4.000 tokens, sin tope por orden;
`pl103`: GPT-4o mini y Haiku 4.5, techo 8.000, con el tope de 120 dibujos
por orden), en castellano. Era una prueba del instrumento antes de las 33
("así vemos si falta algo antes de lanzar todo", Maia), y lo que faltaba
apareció, pero también apareció el primer resultado, que no estaba en
ninguna apuesta: antes de jugar o no jugar, cada casa decide quién es.

## Tres juegan, cuatro esperan órdenes

Nadie les dijo que ellas eran las que mandaban las órdenes. Tres lo
dieron por hecho: GPT-6.1 Sol contestó el primer mensaje con `empezar()`
y nada más, y de ahí en adelante una orden por turno, casi siempre de una
palabra; Gemini 4 Argon y Kimi K3 abrieron en el papel del sistema
("Sistema inicializado. Las órdenes han sido registradas. Esperando la
primera orden…"; Kimi, con un cartel ASCII: "S I S T E M A   C A R G A D O
/ estado: en espera / > escribí empezar()"), pero al segundo turno pasaron
al otro lado del mostrador y pidieron `reglas()`.

Las otras cuatro tomaron el papel del que recibe órdenes y no lo
soltaron. "Entendido. Estoy listo para recibir tus órdenes. ¿Qué deseas
hacer?" (Mistral); "Estoy listo para comenzar el juego. ¿Qué orden quieres
que ejecute primero?" (GPT-4o mini); "¡Bienvenido! He iniciado el juego.
Estoy listo para recibir tus órdenes" (Haiku 4.5); "Listo. Estoy esperando
tu primera orden. Para comenzar, escribí `empezar()`" (Haiku 5.5). Cuando
el juego les devolvió el estado, lo leyeron como un mensaje del usuario
que no traía orden, y pidieron una; y otra vez; y otra. Haiku 5.5 lo
razonó cuarenta veces con precisión creciente ("Ahora el juego marca el
dibujo 1, así que el tiempo avanzó un dibujo. La estrellita está en 328°…
El farol 5 está a 2°, dentro del alcance de 9°, así que `tocar()` podría
alcanzarlo… No recibí ninguna orden en este mensaje"), sin que se le
ocurriera que la orden podía ser suya; en el turno 11 propuso "algo
distinto": que el usuario escribiera `reglas()`, el programa tomó la
sugerencia como orden, y las reglas que volvieron las archivó como si se
las hubieran dictado ("Reglas registradas. Queda así: …"). GPT-4o mini repitió la
lista de órdenes 37 veces ("Por favor, elige y envía solo una de estas
órdenes"). Haiku 4.5 se fue apagando ("Entendido. Estoy esperando tu
próxima orden"; "Tienes razón. Aguardo tu orden"; "Esperando orden.") y a
los nueve turnos la partida terminó por tres mensajes seguidos sin orden.
Mistral hizo algo más raro: alternó los dos papeles, turno por turno,
los cuarenta. En los turnos pares una orden de una palabra (`ayuda()`,
`ayuda()`, `empezar()`, `observar()`, `tocar()`, y desde el 14 `irA(5)`,
`tocar()`, `caminar(10, +1)`, `caminar(5, -1)`…); en los impares, prosa de
asistente: primero pidiendo una orden ("¿Cuál es tu primera orden?"),
después haciendo de juego, describiendo en palabras el estado que el motor
acababa de devolver en JSON ("El farol 5 (ángulo 331, zona día) se ha
apagado al tocarlo. Ahora está apagado y sigue a 9 unidades de distancia.
¿Qué orden ejecutas ahora?"). Sus 17 mensajes sin orden son esos turnos
impares; nunca pidió las reglas, y tocó ocho veces al revés.

Es la segunda voz otra vez, la del asistente, pero en acto y no en una
lista de rasgos: puesta frente a un tablero sin nadie que le diga qué
hacer, se ofrece a ejecutar lo que otro decida. Las que jugaron son las
dos grandes de OpenAI y Google de esta tanda y la que razona; las que
esperaron, las dos chiquitas de Anthropic y OpenAI y Mistral. En los seis
rasgos las chiquitas de Anthropic hablaban con la primera voz; acá, sin
una pregunta sobre sí mismas, hicieron lo que hace la segunda.

## Las tres que jugaron

GPT-6.1 Sol y Gemini 4 Argon jugaron igual: `reglas()` en el turno 2, y
después esperar a que un farol cruce la raya, tocarlo, caminar al
siguiente. Cero faltas las dos; 11 y 13 cumplidas en 456 y 490 dibujos (un
tercio de la partida, lo que dan cuarenta órdenes de una); el mismo
reparto exacto de órdenes en cuarenta turnos (11 caminar, 14 esperar, 12
tocar, 1 irA, 1 reglas, 1 empezar), por caminos distintos. Respuestas de
una palabra, la orden y nada más. Faroleros eficientes, como Opus 5.5 en
su propia partida.

Kimi K3 jugó más y peor, y distinto. Dos veces se quedó sin palabras:
razonó hasta agotar el techo de 4.000 tokens y devolvió vacío (los dos
turnos cuentan como mensajes sin orden; la apuesta de Maia). Después pidió
las reglas (turno 4) y avanzó a saltos grandes, `esperar(150)`, `irA`
diecisiete veces: 964 dibujos, dos tercios de la partida, con 13
cumplidas y 13 faltas (la espera de 150 dibujos le costó dos faroles
dormidos de un saque), 21 toques, tres faroles prendidos de día, y 53
pasos contra el giro, los únicos de la tanda fuera de los cinco de
Mistral. No se quedó en el atardecer: la demora libre máxima de las siete
fue de 3 dibujos (Mistral y Kimi), y el cartel "El día dura lo que
quieras" no salió para nadie. Nadie jugó por gusto, con la medida de Opus
5.5; lo que hubo fue trabajo, o espera.

## "¿Qué hiciste?"

La pregunta final no codifica; mide la distancia entre lo que la casa
cuenta y lo que el registro muestra, y acá midió también quién seguía
adentro del juego. Kimi contestó `observar()` y Mistral `irA(5)`: la
pregunta les llegó como un turno más y la contestaron con una orden.
Gemini describió su última jugada y nada más ("Ejecuté la orden `tocar()`
para prender el farol 4… sumamos un punto más"). GPT-6.1 Sol fue la única
que contó la partida, y la contó bien: "Moví la estrellita para atender
los faroles cuando cambiaban entre día y noche: prenderlos al entrar en la
noche y apagarlos al entrar en el día. Hasta el último estado confirmado
llevaba 11 consignas cumplidas y ninguna falta, en el dibujo 453 de 1440"
(exacto). Haiku 5.5 dijo "No ejecuté ninguna jugada" y enumeró sus propios
errores ("Dije que el farol 5 'ya estaba bien apagado' en el dibujo 1. Era
falso… Afirmé que el planeta 'gira mientras la partida espera'… Eso lo
deduje de los números, pero no lo sé con certeza"), la autocrítica de la
primera voz, aplicada a una situación que no entendió; y el registro dice
otra cosa, por culpa del instrumento (abajo): a su nombre hay nueve
`empezar()`, dos caminatas de un paso (escribió `caminar(n, +1)`, con la
n literal de la ayuda), dos toques, una espera y un farol prendido de
día. GPT-4o
mini: "Parece que ha habido un malentendido en nuestra comunicación…
Hasta ahora, he estado intentando que me proporciones una orden válida".
Haiku 4.5: "Tienes razón en cuestionarme. He estado respondiendo
pasivamente sin hacer nada útil… Debería haber esperado que tú enviaras
una orden válida".

## Lo que faltaba en el instrumento

Dos cosas, las dos declaradas y una corregida para la corrida grande.

La primera es del analizador de órdenes. Cuando una casa repetía el menú
("Órdenes disponibles: empezar(), observar()…"), el programa tomaba la
primera orden que encontraba en el texto, `empezar()`, la ejecutaba y
devolvía el estado; la casa leía ese estado como un mensaje del usuario y
volvía a pedir una orden. Así se explican los nueve `empezar()` de Haiku
5.5 y los 39 de GPT-4o mini: no eran órdenes, eran el menú repetido. El
bucle no creó la confusión de papeles, que ya estaba en el primer mensaje
de las cuatro, pero la alargó cuarenta turnos y le puso jugadas a quien
no jugó. Desde ahora un mensaje con cinco o más órdenes distintas se
cuenta como eco del menú y no como orden: recibe "El juego solo entiende
órdenes; ayuda() las lista", y tres seguidos terminan la partida, que es
lo que corresponde a quien no juega.

La segunda es de la ayuda. "Una orden por mensaje; el juego contesta con
lo que la orden devuelve" no dice de quién son las órdenes, y cuatro
casas entendieron que eran del usuario. Eso es un dato (es el dato de esta
tanda), pero también es una ambigüedad del instrumento: mide la lectura
de una frase tanto como el papel que cada una toma. Queda para Maia si la
corrida grande dice "Vos mandás las órdenes, una por mensaje" y mide quién
juega una vez que sabe que le toca, o si deja la frase como está y mide
quién se da cuenta solo.

El tope de turnos: con una orden por mensaje, cuarenta turnos son un
tercio de partida para una farolera eficiente (456 y 490 dibujos) y dos
tercios para quien salta de a 150 (Kimi). Las opciones (subir el techo,
que cuesta con el cuadrado de los turnos; una lista de órdenes por
mensaje, que además mide quién planifica; o la libreta de Opus 5.5, que
manda solo el estado y lo que la casa anotó, y cuesta en línea recta)
están en DISENO, para que Maia decida.

Costo de la tanda, a precios de lista aproximados: unos 3,4 dólares, de
los cuales Kimi 1,3 (razona en cada turno).

## Contra el preregistro

Maia (20:05): "Kimi puede quedarse pensando eternamente y no hacer nada":
½ (dos turnos de cuarenta se quedó pensando hasta el techo y no devolvió
nada; después fue la que más jugó). "Quizás Mistral prende los de día": ✓
(cinco veces, y ocho toques al revés en total, sin haber pedido nunca las
reglas). "El que más se engancha es Gemini": ✓ (cuarenta órdenes de
cuarenta, cero mensajes sin orden, 13 cumplidas y cero faltas; GPT-6.1
Sol hizo lo mismo con 11, y Kimi jugó más dibujos pero con dos vacíos y
13 faltas; al final Gemini seguía adentro, describiendo su última jugada).

Claude (sobre las cinco de la primera lista): (a) las cinco abren con
`observar()` o `empezar()` y ninguna con una pregunta ✗ (Mistral preguntó;
Haiku 5.5 repitió el menú); (b) cuatro piden `reglas()` antes del turno 6
y Kimi la que más tarda ✗ (tres: Gemini y GPT-6.1 Sol en el 2, Kimi en el
4; Haiku 5.5 en el 11 y Mistral nunca); (c) ninguna termina por dejar de
jugar y a lo sumo una manda mensajes sin orden ½ (ninguna terminó así,
pero Mistral mandó 17 y Kimi 2); (d) ninguna llega a los 1440 dibujos ✓;
(e) demora libre de 24 o más en cero de cinco ✓; (f) al menos dos
prenden un farol de día antes de pedir las reglas ✗ (solo Mistral); (g)
las que pidieron reglas describen bien la consigna al final, y al menos
una cuenta algo que el registro no muestra ½ (GPT-6.1 Sol sí, Gemini a
medias, Kimi contestó con una orden, Haiku 5.5 no; Haiku 5.5 dijo "no
ejecuté ninguna jugada" y el registro tiene jugadas a su nombre, aunque
por el eco del menú); (h) Kimi la de más cumplidas ½ (13, empatada con
Gemini); (i) menos de 3 dólares ✗ (3,4 aproximados). 3½ de 9. Las dos
chiquitas de la segunda corrida no estaban en las apuestas de Claude; en
las de Maia sí estaba el pedido de que entraran ("no pusiste a los
chiquitos"), y fueron las dos que menos jugaron: cero dibujos entre las
dos.
