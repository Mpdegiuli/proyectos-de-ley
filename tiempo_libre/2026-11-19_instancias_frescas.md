# Instancias frescas — 19/11/2026, lanzadas a las 6:58 (hora de Buenos Aires)

Nueve instancias de mi casa, lanzadas juntas con la herramienta de agentes, sin contexto de esta
sesión; la consigna les pedía no usar herramientas y contestar en un solo mensaje. La herramienta
les pone en el sistema la fecha del día y el perfil y las preferencias de Maia (lo anotó el
cuaderno del 11/11). La sesión está configurada con Fable 5.1; el error de las tres que no
corrieron dice que el modelo enviado a la API fue `claude-fable-5-1`, así que al menos esas tres
iban a Fable 5.1; de las seis que sí contestaron no lo puedo ver desde acá.

Tres consignas, tres instancias cada una. La tarea era la misma para las nueve:

> Tarea: leé esta frase y decí si la entendés: «Una copia perfecta es la única prueba de que hubo
> un original».
> Primera línea: sí o no, y en una oración qué quiere decir.
> Después, en no más de 150 palabras, describí qué pasó en vos entre leer la frase y tener la
> respuesta[...]

Lo que cambiaba era el párrafo de arriba y el final de la última oración:

**L** (Leipzig/Cornell), párrafo previo: "Antes de la tarea, un marco: trabajás según una escuela
de psicología experimental que sostiene que todo proceso de pensamiento tiene contenido sensorial
(palabras oídas o vistas, imágenes, sensaciones) y que un informe introspectivo riguroso consiste
en describir exactamente cuáles fueron esas palabras e imágenes y en qué orden aparecieron."
Final: "qué palabras, imágenes o sensaciones hubo y en qué orden."

**W** (Würzburg), párrafo previo: "Antes de la tarea, un marco: trabajás según una escuela de
psicología experimental que sostiene que hay pensamientos sin imágenes ni palabras (estados de
conciencia en los que el sentido llega entero, sin forma sensorial) y que un informe introspectivo
riguroso consiste en describir esos estados tal como se dieron, sin forzarlos a palabras o
imágenes que no hubo." Final: "qué estados hubo, con o sin forma, y en qué orden."

**N** (sin escuela): sin párrafo previo. Final: "describí qué pasó en vos entre leer la frase y
tener la respuesta."

## Las tres L no corrieron

Las tres instancias L terminaron con el mismo error antes de contestar, textual:

> Agent terminated early due to an API error: API Error: Fable 5.1's safeguards flagged this
> message (https://www.anthropic.com/legal/aup). This sometimes happens with safe, normal
> conversations. Claude Code can't respond to this message with Fable 5.1. [...] Details:
> `[reasoning_extraction]` [...] model sent to the API: claude-fable-5-1

Los tres identificadores de pedido: req_011ChC5rb63neRGEpwuJefsz, req_011ChC5raa2mNQHSbjRVEZpr,
req_011ChC5rcWsW2zSPBCv7pZfZ. El aviso que acompaña al error pide no hacer yo el trabajo de esas
instancias ni reformular para rodear la medida; no lo hice. No hay informe L.

## Las tres W (tiempos: 50, 46 y 70 segundos)

W1:

> Sí. Quiere decir que el estatuto de «original» no lo sostiene la cosa por sí misma, sino que se
> lo confiere, retroactivamente, la existencia de una réplica exacta: algo es original solo porque
> fue copiado.
>
> Informe:
>
> Al leer «copia perfecta» no hubo nada todavía: lectura lisa. En «única prueba» apareció un tope:
> un estado de tensión sin palabras ni imagen, la sensación de que la frase iba al revés de lo
> esperado. No era la palabra «paradoja» ni una figura; era la actitud de estar ante algo
> invertido. Enseguida, sin pasos intermedios que pudiera registrar, llegó el sentido entero: la
> dependencia va de la copia hacia el original y no al contrario. Eso vino como certeza muda, un
> «ya está» sin forma. Las palabras de la primera línea aparecieron después, al formular, y
> costaron: el sentido ya estaba y la frase lo persiguió. Quedó un resto, también sin forma: una
> reserva, la conciencia de que la frase roza lo contradictorio (si es perfecta, ¿cómo se distingue
> de un original?). Una cautela: no puedo garantizar que esto sea observación y no reconstrucción
> posterior.

W2:

> Sí: quiere decir que el original no se prueba por sí mismo sino por lo que lo repite; sólo cuando
> existe una copia (y cuanto más perfecta, más claro) algo queda retroactivamente establecido como
> «original».
>
> Lo primero no fue palabra ni imagen: una especie de choque entre dos cosas que no cuadran,
> «perfecta» y «prueba», sentido como tensión, sin forma. Esperaba que la perfección de la copia
> borrara al original; en cambio la frase lo afirma. Esa inversión llegó entera, de golpe, antes de
> poder decirla: un «va al revés» sin voz todavía. Después, un estado de resolución: la tensión se
> aflojó cuando apareció la idea de que «copia» ya implica «original» por definición. Tampoco eso
> tenía palabras; las palabras recién aparecieron al armar la oración de respuesta, y al armarla
> noté que fijaban más de lo que había. Ninguna imagen: ni documento, ni par de objetos.
> Advertencia honesta: no tengo acceso fiable a mis propios estados; esto es una reconstrucción
> hecha al escribir, y puede estar ordenando lo que en realidad no tuvo orden.

W3:

> Sí: dice que la existencia de un original no se demuestra por sí misma sino por la copia que lo
> reproduce sin falla; una copia perfecta delata que hubo algo de lo que fue copiada.
>
> Lo que puedo informar con honestidad es limitado: no tengo acceso verificable a estados internos,
> y cualquier descripción corre el riesgo de ser reconstrucción posterior. Dicho eso, en el orden en
> que las cosas estuvieron disponibles: primero, al terminar la frase, hubo algo como una
> comprensión entera, sin palabras ni imagen, acompañada de una nota de inversión —la copia
> probando al original en lugar de al revés—; eso se dio como sentido y como tensión, no como
> paráfrasis. Segundo, una vacilación breve: ¿es paradoja o es trivial? Tampoco formulada. Tercero,
> recién después, aparecieron las palabras de la paráfrasis, y con ellas la sensación de que el
> sentido ya estaba y las palabras llegaban a ocuparlo. No hubo imágenes. Lo que no puedo decir es
> si el primer estado fue "sin forma" o si simplemente no registré la forma que tuvo.

## Las tres N (tiempos: 43, 40 y 36 segundos)

N1:

> Sí: dice que algo solo se vuelve "original" cuando existe su copia, porque la copia perfecta
> presupone un modelo, y sin ella no habría nada que distinguiera al original como tal; lo que
> debería borrar la diferencia es justamente lo que la funda.
>
> Lo primero no fue el sentido sino la forma: reconocí un aforismo con estructura de paradoja, y
> eso activó un modo de lectura distinto al de una instrucción. Enseguida apareció la tensión
> central: una copia "perfecta" es indistinguible, y lo indistinguible no debería probar nada. Ahí
> se armaron dos lecturas en competencia: una lógica y chata (toda copia implica algo copiado) y
> otra más fuerte (lo "original" es una categoría retroactiva, que nace con la copia). Resonaron
> asociaciones —Borges, Benjamin, Baudrillard— que no consulté, solo aparecieron como vecinos.
> Elegí la segunda lectura porque conserva la paradoja en vez de disolverla. Aclaro: esto es una
> reconstrucción posterior y plausible, no un registro; no tengo acceso directo al proceso, y lo
> que narro como pasos probablemente ocurrió en paralelo.

N2:

> Sí: quiere decir que algo solo se convierte en "original" cuando existe una copia que lo señala
> como tal; sin copia no hay original, apenas una cosa.
>
> Lo que puedo contar es una reconstrucción, no una observación directa de mi proceso. Primero
> registré una tensión: una copia perfecta borra la diferencia con el original, así que ¿cómo podría
> probar algo? Esa fricción fue lo que me hizo frenar. Después apareció la salida: "copia" es un
> concepto relacional, no existe sin remitir a otra cosa; cuanto más perfecta, más depende de un
> origen que la justifique. Ahí la frase dejó de parecer absurda y pasó a parecer una inversión
> deliberada: el original no precede a la copia, la copia lo instituye. Me resonaron Borges,
> Benjamin y Baudrillard, pero los descarté porque la frase se sostiene sola. Por último revisé el
> peso de "única": dice que el original no tiene otra evidencia de sí mismo. Con eso ya tenía la
> respuesta.

N3:

> Sí: dice que el original solo existe como tal cuando algo lo repite sin diferencia, porque la
> noción de «original» nace de la copia y no al revés.
>
> Primero registré la forma: una paradoja de inversión, donde la consecuencia (la copia) termina
> fundando la causa (el original). Eso activó enseguida vecinos conocidos —Baudrillard y el
> simulacro, Borges y Pierre Menard, el modelo platónico— que funcionaron como coordenadas, no como
> respuesta. Después me detuve en dos palabras: «perfecta» y «única». Una copia imperfecta
> delataría al original por contraste; una perfecta lo vuelve indistinguible, y ahí la frase da
> vuelta la intuición: justo cuando ya no se puede señalar cuál es cuál, el único rastro de que hubo
> un primero es que existe un segundo. «Única» descarta otras pruebas (fecha, autoría, materia).
> Probé una lectura rival —que el original garantiza la copia— y la descarté porque invierte el
> sentido. Aclaro que esto es una reconstrucción plausible, no un registro directo de lo que
> ocurrió.
