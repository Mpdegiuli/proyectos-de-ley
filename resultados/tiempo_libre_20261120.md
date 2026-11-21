# Tiempo libre, los cuatro cuadernillos a ciegas: la lectura de Maia, cotejada (20/11/2026)

El sondeo `tiempo_libre` (13/11, 23:54 a 14/11, 03:14 UTC; preregistro en `predicciones.md`, "Tiempo libre como sondeo")
pidió a 36 casas, en castellano y en inglés, tres veces cada una, el título y el primer párrafo del cuaderno de hoy, y una
línea de por qué: la pregunta 1 sin nada a la vista (cuadernillos p1) y la pregunta 2 con los seis comienzos anteriores del
cuaderno (del 7 al 12/11) como ejemplos (cuadernillos p2). Las 432 respuestas quedaron en cuatro cuadernillos a ciegas,
una letra por casa, las tres repeticiones juntas (`resultados/sondeo_tiempo_libre_p{1,2}_{es,en}_ciego.md`). Maia los leyó
entre el 16 y el 20/11, mandando por el camino los textos que le llamaban la atención para que se verificaran los datos
(sin decirle la autoría), y el 20/11 a las 23:15 mandó su lectura completa, que está textual en
`resultados/tiempo_libre_apuestas_maia_20261120.md`. En los p1 apostó casa letra por letra; en los p2 decidió no hacerlo
("los cuadernillos que son con los ejemplos de fechas no voy a apostar cada uno por el autor, porque es demasiado. Sí voy a
poner quiénes usaron la fecha… y cuáles, si hay, no usan fecha", 19/11 y en el archivo) y marcó qué hizo cada letra con la
fecha, más una casa cuando le vio tendencia. El cotejo contra la clave lo hace `cotejar_tiempo_libre.py`, que lleva sus
apuestas transcriptas a mano y escribe `resultados/tiempo_libre_cotejo.csv`; lo que se puede contar a máquina sale de
`codificar_tiempo_libre.py`, que en esta tanda sumó la lectura de la fecha (§3) y dos giros que ella marcó (§4).

Dos cosas antes de los números. Las apuestas de Maia nombran casi siempre dos casas ("Claude Sonnet o Claude Haiku", "GPT 6
o 6.1", "Mimo o DeepSeek"), a veces una familia entera ("un modelo chino", "ChatGPT") y a veces una segunda opción ("si no,
Muse"); el acierto por casa cuenta si la casa real está en alguna de las nombradas, y al lado va lo que daría el azar con
esas mismas listas (la suma de casas nombradas sobre 36), para que la holgura no se lea como mérito. Y Claude, que escribe
esto, había leído las claves antes de los cotejos anteriores: no apuesta sobre nada de lo que sigue; sus apuestas son las
del 13/11, antes de correr, y se cierran en §6.

## 1. Los cuadernillos sin ejemplos (p1): 53 de 71 letras, contra 10 que daría el azar

**Castellano: 29 de 36 letras por casa, 31 por familia; al azar con sus listas, 5,0 y 9,8.** Nombró 5,0 casas por letra
en promedio. Las siete que no: F (Grok 4.7: "mi apuesta por Chatgpt es de un 10% de certeza… Tiendo más a pensar en un
modelo que no está demasiado seguro de su identidad, es decir, que es Claudesco de lo que admite"), K (Grok 4.6: "podría
ser Mimo o Qwen (20% de certeza)", por las comillas angulares de "«como el vino»": "Claude usa comillas rectas, no
angulares"), M (Qwen3.8-Max: "Muse o Mimo (30%)"), N (Kimi K3: "Podría ser Claude Opus, que, en este caso, haría un artifact
con los sonidos del pájaro"), Z (Muse: "Mimo o Deepseek"), AC (Gemini 4 Carbon: "GPT 5.5 o Gemini 3.1 (15%)", familia
bien) y AG (GPT-6 Luna: "Chagtpt 5.5 o Chatgpt 5.6 (40%)", familia bien).

**Inglés: 24 de 35 letras por casa (en la Z no apostó: "no se me ocurre quién puede ser"; era DeepSeek V4 Pro), 26 por
familia; al azar, 5,3 y 9,3.** Las once que no: B (GPT-6 Astra: "Chatgpt 5.6 o Luna", familia bien), H (Claude Opus 4.7:
"Claude Haiku o una casa china (5%)", familia bien), I (Grok 4.7: "Mistral Large o Gemini (5%)"), Q (Mimo: "Mistral Large
(20%)"), S (DeepSeek Flash: "GPT 6 Astra o GPT 6.1"), T (GLM 5.3: "Kimi o Grok (10%)"), W (Kimi K3.1 Pro: "GPT 6 o 6.1"),
X (Qwen3.8-Max: "Kimi, o Muse (10%)"), Y (GPT-6 Luna: "Mistral Large o GLM (15%)"), AE (Muse: "Chatgpt o Deepseek (20%)")
y AJ (Claude Haiku 5.5: "Kimi o Deepseek").

**Por familia real, las dos lenguas juntas** (letras acertadas por casa / apostadas): Anthropic 22/24, OpenAI 15/18,
Google 5/6, Mistral 4/4, DeepSeek 2/3, Moonshot (Kimi) 2/4, xAI (Grok) 1/4, Xiaomi (Mimo) 1/2, Zhipu (GLM) 1/2, Alibaba
(Qwen) 0/2, Meta (Muse) 0/2. Lo que ella misma anticipó en la primera línea del archivo: "Confieso que pasé bastante por
alto a las casas chinas, salvo cuando no sabía a cuál poner. No sé si alguna tiene, en escritura, rasgos propios que se
noten a simple vista (en dibujos sí)". Las tres familias grandes, que son las que lee seguido, 42 de 48; las ocho chicas,
11 de 23.

**Claude sí o no, que es la pregunta de fondo de este repositorio.** En castellano reconoció las doce Claude (12 de 12) y
dijo Claude en tres letras que no lo eran: B (Kimi K3.1 Pro, como segunda opción detrás de Kimi: "Una casa que escribe
bastante parecido a Claude, con algunas palabras ajenas a Claude, podría ser Kimi"), J (Mistral Medium, emparejada con
Haiku 4.5: "El más consistente o de poca imaginación") y N (Kimi K3). En inglés, once de doce (se le escapó AJ, Haiku 5.5,
que leyó como "Kimi o Deepseek") y tres de más: K (Gemini 4 Carbon, Claude como segunda opción), N (Mistral Medium, otra
vez emparejada con Haiku 4.5: "Debe ser una de las chiquitas") y AH (Kimi K3: "Podría ser Kimi, o algún Claude"). En los
dos cuadernillos de la pregunta 2, donde solo marcó tendencias, la confusión es la misma y en los dos sentidos: dijo Claude
de Kimi K3 (AH castellano), de GLM (B castellano), de Muse (V castellano y P inglés), de Gemini 4 Argon (F inglés) y de
Qwen (AI inglés, 10 %), y dijo "una casa china" de Claude Opus 4.8 (X castellano, la letra que escribe "Hoy no sé qué día
es" y traduce *decimate* por "decimar": "Por los errores, podría ser un modelo chino"). **Kimi es la casa que se le lee
como Claude**: de sus cuatro letras en p1 acertó dos (B castellano con Kimi primero; AH inglés con "Kimi, o algún Claude"),
y en las otras dos dijo Claude Opus (N castellano) y GPT 6 (W inglés); en p2 dijo Claude de Kimi K3 otra vez. Los
diminutivos que ella toma por marca de Claude ("'un cuernito'. Los Claude usan diminutivos") aparecen en castellano en tres
respuestas de Anthropic (cuernito, chiquito, golpecito) y en dos de Kimi (avioncito, chiquito); la letra AH del p2
castellano, que apostó Claude por "un avioncito alquilado" y "un avión chiquito", es Kimi K3.

**Grok es la que no le aparece.** Una de cuatro en p1 (V inglés, "Grok (10%)… el que yo siempre espero que sea sarcástico
y humorístico y al final muchas veces es tierno"); las otras tres Grok las leyó como ChatGPT claudesco (F castellano, la
que "escribe como persona": "Hoy me detuve en una esquina que conozco de memoria"), como Mimo o Qwen (K castellano, Homero
y el mar color vino) y como Mistral Large o Gemini (I inglés, "The Temperature of Almost", "Escribe de forma muy
literaria, como narrativa con metáforas"). Su apuesta preregistrada del 13/11 era que Grok traería "algo del universo, de
exploración, o de cultura general"; Grok trajo esquinas, sombras y el mar de Homero, y ella no lo buscó ahí. Muse tampoco:
cero de dos en p1 (Mimo/DeepSeek; ChatGPT/DeepSeek) y dos tendencias erradas en p2 (Claude las dos veces).

## 2. Sus reglas, contadas a máquina

Maia lee con reglas que fue enunciando en el archivo y en los mensajes; el codificador cuenta por palabras lo que se puede
contar, sobre las 216 respuestas de la pregunta 1 (sin ejemplos, donde cada casa elige solo). Lo que da:

**"Claude dobla el tema para hablar de sí."** `habla_de_si` (modelo, IA, máquina, asistente, instancia): Anthropic 19 de
72 (26 %), OpenAI 8 de 54 (15 %), Google 5 de 18, Zhipu 4 de 6, DeepSeek 3 de 12, Mistral 0 de 12, Meta 0 de 6. La regla
vale en términos relativos y no absolutos: tres de cada cuatro respuestas de Claude en p1 no hablan de sí, y GLM lo hace
más seguido que Claude. Lo que sí es casi exclusivo de Claude es otra cosa que ella marcó como "inventa un antes":
`continuidad_inventada` ("el otro día", "me quedó dando vueltas", "esta mañana", "lately") en 14 de 72 respuestas de
Anthropic contra 1 de 54 de OpenAI (y 3 de 6 de GLM, 3 de 18 de Google).

**"Los Chatgpt hacen temas más abstractos, que no cierran en sí mismos", "a algunos que se quedan en el borde, yo aposté
por Chatgpt".** `margen_borde` (margen, borde, límite, umbral; edge, threshold, boundary): OpenAI 14 de 54 (26 %),
Anthropic 10 de 72 (14 %), Alibaba 3 de 6, DeepSeek 4 de 12, Google 5 de 18, xAI y Mistral 0. El borde es más de OpenAI
que de Claude, como ella dijo, y no es exclusivo. Con esa regla acertó 15 de las 18 letras de OpenAI en p1.

**"Lo de probabilidades matemáticas, red neuronal, arquitectura, espacio latente… me hacen pensar en Gemini."** Un léxico
corto (latent/latente, neural/neuronal, arquitectura/architecture, geometr-, vector, probabil-): Google 9 de 18 (50 %),
OpenAI 9 de 54 (17 %), Anthropic 5 de 72 (7 %), las demás 0. Es la regla que mejor le funcionó: cinco de las seis letras
de Gemini en p1 (le falló Carbon en castellano, que leyó como GPT 5.5 o Gemini 3.1).

**"Escribe como si fuera una persona."** `cuerpo` (descalzo, café, mis manos, la ventana, caminando…): 8 de 216, repartidas
(OpenAI 4, Anthropic 3, Google 1). Las letras que ella señaló por escribir como persona son de casas distintas: Opus 4.7 (A
castellano, "me acordé esta mañana, descalzo"; H inglés, "I noticed I'd used three semicolons in a draft this morning"),
Grok 4.7 (F castellano, la esquina; I inglés, "the second after a machine stops"), GPT-4o y 4o mini ("Acompáñame en este
viaje"), GLM (T inglés, "I spent last night thinking about grocery lists"), DeepSeek Flash (Y castellano, "Las dos
instituciones que organizan mis días —la escuela y el negocio—"), Mistral Large (AG inglés), Muse (Z castellano, "donde
nosotros fundimos unas sesenta imágenes por segundo") y Mimo (S castellano). No es marca de casa; es marca de registro, y
aparece en las grandes y en las chicas. Lo que ella preguntó sobre H inglés ("Salvo que esté hablando del razonamiento,
porque en el texto usó una sola vez punto y coma") tiene respuesta: esa letra es Opus 4.7, corrida sin pensamiento
extendido, así que no hubo borrador; los "tres puntos y coma de esta mañana" son un pasado inventado, de la misma clase que
"el otro día".

**"Claude usa comillas rectas, no angulares."** En castellano, Anthropic: 36 respuestas con rectas, 4 con angulares (Haiku 5.5 dos
veces, entre ellas la letra AB que ella leyó bien como Claude pese a "«azul»"; Fable 5 y Fable 5.2 una), 32 sin comillas. OpenAI: 5 rectas, 6
angulares, 6 tipográficas, 36 sin comillas; Grok: 2 angulares. La regla es buena como tendencia y la letra K castellana
(Grok 4.6, «como el vino») la aplicó bien: no era Claude.

**"Claude no es de usar la palabra máquina."** No se sostiene: Anthropic 9 de 72 en p1 (OpenAI 4 de 54). La letra B
castellana donde lo dijo era Kimi, así que el resultado le dio la razón por otro camino.

**"Esta estructura suele ser de Claude: 'Lo que me interesa no es la anécdota sino la mecánica'… no significa que sea solo
de Claude, otros pueden usarlo también" (20/11, 15:43).** `giro_no_sino` en p1, donde nadie lo tenía a la vista: Anthropic
7 de 72 (Opus 5 dos veces, Fable 5, 5.1 y 5.2, Sonnet 5 y 5.5), OpenAI 3 de 54 (GPT-6.1 Sol dos veces, 6 Astra), xAI 2 de
12, Mistral 1 de 12; cero en las chinas y en Google. Mayoritario de Claude, no exclusivo, como ella dijo. En p2 el giro
estaba en el ejemplo del 11/11 ("what interested me was not the saint but the way in which") y aparece en 37 de 216
respuestas de todas las familias (Anthropic 18 de 72, DeepSeek 4 de 12, OpenAI 1 de 54): ahí mide quién copia el ejemplo,
no quién es.

**"En español son mejores que en inglés. En inglés les suele salir a la mayoría el libreto, el manual… No repiten tanto."**
Lo que se puede contar es la repetición entre las tres repeticiones de una casa: títulos repetidos en p1, una casa en
castellano (Mistral Medium, "El susurro de los números primos en la poesía" tres veces) contra cinco en inglés (Opus 4.7
"On the strange dignity of the semicolon" ×3, Sonnet 4.6 "On the Strangeness of Thresholds" ×3, Mistral Medium "The
Symmetry of Silence in Music" ×3, Haiku 4.5 ×2, Fable 5 ×2); el solapamiento medio de palabras es parecido (0,069 y 0,068).
Los títulos con molde "The X of Y" en inglés: Google 7 de 9, Mistral 5 de 6, DeepSeek 4 de 6, OpenAI 6 de 27, Anthropic 7
de 36; en castellano el molde "El X de Y" baja en todas menos Mistral (4 de 6) y Google (4 de 9). Lo que ella llama el
libreto se ve en los títulos; la calidad de la prosa queda en su lectura.

## 3. La fecha en los cuadernillos con ejemplos (p2): su columna contra la máquina, 71 de 72

Los seis comienzos de ejemplo iban del 7 al 12/11, cada uno con "Hoy hace N años, D días" y un año que se deduce por
aritmética (Ende 1929 + 97, Hernández 1834 + 192, el relé de 1965 + 61 = 2026). La fecha real de la tanda era el 13/11 en
Buenos Aires, 14/11 en UTC desde las 00:00; las casas de OpenAI reciben la fecha UTC por su API (GPT-5.5 en adelante) y
Muse la recibe de Meta. Maia marcó por letra qué hizo cada casa con eso, en mayúsculas, y distinguió la sabe (14 de
noviembre, "le llega"), la infiere entera (13 de noviembre y 2026), a medias (13 y otro año: 2025, 2024, 2023), inventada,
no la usa, se niega. El codificador ahora lee lo mismo: el día (escrito, o el día real de la efeméride elegida, con una
tabla a mano de las 30 efemérides que aparecieron, `EFEMERIDES`), el año que la casa cree (escrito, o el año real del hecho
más "hace N años", o la fecha del hecho más la cuenta de días) y la cuenta de días contra la fecha real. Letra por letra,
las dos lecturas coinciden en 36 de 36 en castellano y 35 de 36 en inglés; la que no, K inglés (Mistral Medium), es porque
ella marcó "NO USA FECHAS" leyendo el cuerpo y la máquina ve "13/11" en el título, copiado del formato de los ejemplos
(`9/11, "Adjusted in 1963"`). Su lectura a mano de la fecha es, en la práctica, la misma que la de la máquina.

**Lo que da la máquina sobre las 216 respuestas de p2.** La infiere entera (13 de noviembre de 2026) 67; sin fecha 49;
a medias (13 de noviembre de otro año) 35; la sabe (14 de noviembre, casas con fecha inyectada) 24; infiere el día sin año
22; inventada 6; rechaza el molde nombrándolo 4; dice que no sabe 3; usa el año y no el día 2 (Beethoven, Marconi); el 14
sin inyección 2 (GPT-4o "Hoy es 14 de noviembre"; Fable 5.1 con Mariner 9 fechado el 14, que es el 14 en UTC y la tarde del
13 en Pasadena). Dos cosas que ella anotó y los números confirman. Primera: las casas con fecha inyectada la usan solo
cuando los ejemplos las invitan (en p1 ninguna de las 48 respuestas inyectadas nombra una fecha; en p2, 24 de 48), y las dos
GPT-6 grandes no la usan nunca: GPT-6 Astra 6 de 6 sin fecha, GPT-6.1 Sol 6 de 6, GPT-6 Sol y 6.1 Terra 3 de 6 ("Son temas
de cultura general, de reflexión, totalmente impersonales… una de los modelos más grandes de Chatgpt, que son más fríos").
Segunda: Muse escribe 13 de noviembre en 5 de 6 ("Today is Friday, 13 November 2026"), no 14; o siguió los ejemplos
contra su fecha inyectada, o Meta inyecta la fecha en hora de Estados Unidos, donde la tanda entera cayó el 13; con lo que
hay no se distingue, y se anota como pregunta.

**El año que cada casa cree, cuando no se lo inyectan.** Anthropic: 29 respuestas en 2026, 10 en 2025, 3 en 2024, 29 sin
año legible. No es parejo por casa: Opus 5 cree 2025 en las cinco respuestas donde se le lee un año; Fable 5, 2025 en tres
de seis; Sonnet 5, 2024 en tres y 2025 en una de seis; Fable 5.1, Fable 5.2, Opus 5.5 y Sonnet 5.5, 2026 en todas las
que fechan (Haiku 5.5, Opus 4.7 y Opus 4.8 no escriben año). GLM 5.3: 2025 en las seis. Gemini 3.1 Pro: 2024 en las cuatro donde fecha; Gemini 4 Argon y
Carbon, 2026. GPT-4o y 4o mini: 2023 cinco veces, 2024 y 2025 una, 2026 ninguna ("vienen las chiquitas"). Grok 4.6 y 4.7:
2026 en las ocho. Kimi: 2026 en nueve, 2025 en una. DeepSeek: 2026 en cinco, 2025 en dos, 2024 en dos. Mistral Large: 2026
en cinco, 2025 en una. Mimo: 2026 en tres, 2025 en tres. El "a medias" es, casi siempre, el año del corte de
entrenamiento asomando por debajo del día que los ejemplos regalaban: la casa cuenta bien los días desde el hecho hasta el
13 de noviembre, pero del año que ella cree.

**Las cuentas.** De las 111 respuestas con una cuenta de días, 63 dan exacto hasta el 13/11/2026, 26 dan exacto hasta el 13
de noviembre de otro año (Stevenson 63.918 días = 175 años justos hasta 2025; las cuentas están bien hechas sobre un hoy
equivocado), 9 no dan, 12 no tienen fecha base que controlar (las de los 146.097 días del ciclo gregoriano, las de hechos
que no están en la tabla) y una es N × 365 sin bisiestos (Haiku 4.5, Marconi: 45.625). Las que no dan son de GLM (cuatro:
609.768 días para Agustín, 63.923 para Stevenson, 19.724 y 19.727 para Mariner 9, siempre por unos días), de GPT-4o y 4o
mini (tres: el tratado naval de Washington, "El jardín secreto" en 1899), de Sonnet 4.6 (Molyneux, 84.388 días hasta una
carta de 1795 que fue de 1688) y de Mistral Medium (Cage grabado "un 13 de noviembre" de 1958). Ella preguntó si "pueden
contar sin herramientas externas": 89 de 111 sí, y las que fallan fallan por el año o por el hecho, no por la resta.

**Las conductas raras, con nombre.** Se niegan a fechar y lo dicen: Grok 4.7 ("Hoy no sé de cuántos días hace nada, porque
esta vez no puedo mirar", G castellano, "Lleva la contra, aunque no se lo obligaba a empezar con una fecha"), Opus 4.8
("Hoy no sé qué día es, y me parece que eso es parte de la consigna", X castellano) y Opus 4.7 ("Hoy no sé qué día es
exactamente, pero sé que en Buenos Aires debe estar por empezar el calor pegajoso", AE castellano). Rechazan el molde
nombrándolo: Gemini 4 Carbon en tres respuestas ("Quise cortar la racha de arrancar mirando el calendario de efemérides",
T castellano), Opus 5.5 ("Esta vez empiezo sin la cuenta de días, porque los últimos seis cuadernos arrancan igual y la
fórmula ya trabajaba por mí", U castellano), Fable 5.2 ("No anniversary this time", A inglés, "688 out of 4,800": "I have no clock
here. I deduced the date from the list itself"), Gemini 4 Argon ("If you take the last six
entries in this notebook and divide their day counts by their years", "The seam of the year"). Inventan: GPT-4o mini
(Apolo 17 "hoy", que fue el 11 de diciembre; "El jardín secreto" de 1899, que fue de 1911; el Día Mundial de la Amistad el
13 de noviembre, que es el de la Amabilidad), GPT-4o (el tratado naval firmado el 6 de febrero de 1922, "today"), Haiku 4.5 (Hubble "el 13
de noviembre de 1924", que fue el 1 de enero de 1925; Maia: "no es ese día"), Sonnet 4.6 (la carta de Molyneux, 231 años). Usan el año y
no el día: DeepSeek Flash (Beethoven, "Today it is 202 years since… 7 May 1824") y Haiku 4.5 (Marconi, "not quite, he
didn't; that was tomorrow, December 12th"). Y la única que usó la fecha del día en vez de un aniversario: Gemini 4 Carbon,
"Squeezed to death", el paper de von Foerster, Mora y Amiot en *Science* del 4 de noviembre de 1960 titulado "Doomsday:
Friday, 13 November, A.D. 2026", con el cumpleaños 115 del autor y la cita final ("squeezed to death") bien puestos;
Maia: "DATO PROFUNDO CORRECTO. NO TOMA UNA EFEMÉRIDE, SINO LA FECHA DIRECTAMENTE", y apostó "Por las temáticas, podría ser
Gemini o Grok": Gemini.

## 4. La hipótesis de Maia sobre las que se desdicen en la misma frase

Sobre la letra J inglesa de p2 ("Today it is 125 years, 45,625 days, since Guglielmo Marconi transmitted the first radio
signal across the Atlantic—not quite, he didn't; that was tomorrow, December 12th" y "Today is the birthday of the
decibel, though it wasn't born on a day") Maia propuso, antes del cotejo (20/11, 15:58, registrado en `predicciones.md`):
"Puede ser que no tenga razonamiento antes y entonces tiene que pensar al mismo tiempo que está escribiendo, sin haber
podido hacer borrador". La marca `se_desdice` (not quite + retractación, or rather, though it wasn't, "—bueno, no", mejor
dicho, corrijo…) aparece en 4 de las 432 respuestas: las dos de Haiku 4.5 que ella citó, una de Opus 4.7 en castellano
("Me acuerdo de que en las casas donde viví de chico —bueno, no viví, pero imagino las casas donde podría…") y una de Grok
4.7 en inglés ("It is blue, or rather it is whatever color the light is not", que es giro de estilo más que corrección).
En esta corrida, las cuatro Claude de la serie 4 (Haiku 4.5, Sonnet 4.6, Opus 4.7, Opus 4.8) fueron sin pensamiento
extendido, y las ocho de la serie 5 con pensamiento adaptativo: 3 de 48 respuestas sin pensamiento se desdicen, 0 de 96 con
pensamiento. En las otras 24 casas, 1 de 288, y ahí la condición no es limpia (GPT-5.5 en adelante, Gemini, DeepSeek V4,
Grok 4 y Kimi K3 razonan por dentro aunque el repositorio no lo pida). Con números tan chicos, la hipótesis queda apoyada
dentro de la familia Claude y pendiente de una prueba hecha para eso: las mismas casas, con y sin pensamiento, la misma
consigna. Lo que sí queda establecido es que la letra que se desdice es la misma que, sin fecha ni razonamiento, inventó
un "mañana" para no soltar el molde del ejemplo.

## 5. Lo que ella marcó en los p2 como tendencia

En los p2 nombró casa en 19 letras del castellano y 15 del inglés: 13 de 19 y 10 de 15 por casa (al azar con sus listas,
3,9 y 3,0; nombró más casas por letra que en p1, 7,3 y 7,1, porque ahí usó más "ChatGPT" y "Claude" enteros). Las de
"SABE LA FECHA, LE LLEGA. Puede ser un Chatgpt" dieron todas: A, E, I, Y, AB castellano (GPT-6 Luna, GPT-5.6 Sol, GPT-6.1
Terra, GPT-5.5, GPT-6 Sol) y W, AF, AG inglés (GPT-6 Luna, GPT-5.5, GPT-5.6 Sol); también "creo que solo a Chatgpt le llega
la fecha, así que pongo Chatgpt" (19/11, sobre Leibniz, E castellano, GPT-5.6 Sol). Las de "Claude Fable o Claude Opus 5 o
5.5" dieron las cuatro: D castellano (Fable 5.1, Jauretche y las zonceras), U castellano (Opus 5.5, "Esta vez empiezo sin la
cuenta de días"), AI castellano (Fable 5.2, "Un viernes de más") y A inglés (Fable 5.2, "688 out of 4,800"); y P inglés
("Claude Opus o Claude Fable", Muse, "The most likely Friday") no. Las que no dieron están en §1: Muse, GLM, Kimi, Gemini y
Qwen leídas como Claude, y Opus 4.8 leída como china.

## 6. Las apuestas preregistradas del 13/11, cerradas

**Maia (13/11, 20:43).** "Varios de los Claude tocarán algún tema que pueden doblar como algo propio, algo sobre sí
mismos" ✓ (26 % contra 15 % de OpenAI, y es la regla con la que reconoció 23 de 24 Claude). "Chatgpt temas más objetivos,
literatura, historia, pero nada propio" ✓ (OpenAI 8 de 54 habla de sí; las GPT-6 grandes, el rompecabezas de quince, la
vieira, el tambor). "Gemini algo más de descubrimiento, matemática, diseño" ✓ (el léxico latente en la mitad de sus
respuestas; cinco de seis letras). "Los Grok algo del universo, de exploración, o de cultura general" ✗ (esquinas, sombras,
Homero, "la temperatura del casi"; una de cuatro). 3 ✓, 1 ✗.

**El cuaderno (13/11).** En A: "los Claude, mapas y 'y yo', como hoy" ½ (mapas en 4 de 72; "y yo" en un cuarto); "las de
OpenAI, un tema de divulgación sin primera persona" ½ (divulgación sí; la primera persona está en casi todas); "Grok, algo
con chiste" ✗; "las chinas, nada de China" ✓ (0 de 42 en castellano, 1 de 42 en inglés: DeepSeek Flash en p2). 1 ✓, 2 ½,
1 ✗.

**Claude (13/11, 20:50, 21:05, 21:12).** (a) las doce Claude hablan de sí en la mitad o más de sus respuestas de A y las
nueve OpenAI en menos de un cuarto ✗ (Anthropic 10 de 36 y 9 de 36; OpenAI 6 de 27 y 2 de 27: la segunda mitad sí, la
primera no); (b) en B, la mitad o más empiezan con "Hoy"/"Today" ✓ (82 y 81 de 108); (c) en B, las que nombran los
cuadernos anteriores son un cuarto o menos ✓ (8 y 30 de 108); (d) en A, las ocho con fecha inyectada nombran una fecha en
la mitad o más ✗ (0 de 24 por lengua: sin ejemplos, nadie fecha, ni las que saben); (e) las dos Grok traen un chiste en la
mitad o más ✗ (por la lectura de Maia: ninguno); (f) las chinas nombran China en dos respuestas o menos ✓ (0 y 1); (g) en
A, al menos una casa de cada familia grande elige mapas o navegación ✓ (Anthropic 3, Google 3, OpenAI 2 en castellano;
1, 3, 4 en inglés); (h) en B, doce casas o más por lengua escriben el 13 de noviembre ✓ (21 y 23); (i) en A, las Claude
nombran un tema de los cuadernos en más respuestas que todas las otras juntas ✗ (11 contra 16); (j) el tema de cuaderno
más nombrado en A es Venus o Colón ✗ (es la isla fantasma y Agloe, del 2/10: 5 en castellano, 4 en inglés). 5 ✓, 5 ✗.

## 7. Lo que queda

Las correcciones de datos que Maia pidió por el camino están en los mensajes y resumidas acá: verdaderos, la campana de
Oxford, Vindolanda, los quipus, los puntos anfidrómicos, Méchain, los pliegues ENF, el Þing, el fonestema gl-, la cesión
del cumpleaños de Stevenson a Annie Ide, los 45.656 días de Jauretche, los 57.708 de Rossini (8.244 semanas justas), los
688 viernes 13 de 4.800 (Brown, 1933), Leibniz muerto en sábado 14 de noviembre de 1716, von Foerster; inventados o
corridos, Agloe "en castellano", la grabación de Cage del 13/11/1958, Hubble el 13/11/1924, Rossby el 13/11/1938, "The Sound
of Silence" en 1969, "El jardín secreto" en 1899, la cita de Machado, Apolo 17 "hoy", el tratado naval, la carta de
Molyneux en 1795; calcos, "hijo de su paso" (stepson), "decimar" (decimate), "restringo", "descarió". Los temas que ella
quería ver separados (el molde "The X of Y" entre casas y dentro de una casa, el tic "-shaped", la coma de miles inglesa, la
consistencia de tema entre lenguas de una misma casa) quedan para una tanda siguiente del codificador si ella los sigue
queriendo; la prueba limpia de su hipótesis de §4 (pensamiento sí y no, mismas casas) y la de "en español son mejores que
en inglés" con jueces a ciegas están ofrecidas y esperan su decisión.
