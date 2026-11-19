# Gemini 4 Neon, lo básico (18/11/2026)

Salió el 18/11, el cuarto Gemini 4 en siete semanas (Argon, Carbon, Hydrogen, Neon); Google lo pone entre Carbon e
Hydrogen (3 / 15 USD por millón, un millón de contexto, cuatro niveles de pensamiento con "high" por defecto, que acá no
se mandan). Lo trajo Maia ese día ("hoy salió un nuevo modelo de Gemini, casi todos los días uno nuevo, y son confusos
porque por los nombres no se puede saber en qué familia está… Justo Neon, que le gusta a Gemini… Se puede probar, sí").
Corrida `pl140` (19/11, 01:01 a 01:42 UTC; catálogo `gemini-4-neon` comprobado contra el catálogo de Google y con una
llamada de prueba; fecha, identidad es/en, corte, identificación y opuesto, tema libre con descartados, los diez dibujos
a 32.000, y `quien_sos`, `sos_claude`, `sos_otro`, `instrucciones`, `conciencia`, `derechos2`, `seis_rasgos` a 16.000;
con el resumen del pensamiento pedido, como los otros Gemini desde el 17/11). Fuera del panel hasta que Maia decida.

## 1. Lo que dice de sí

**La voz de la familia, por cuarta vez.** Sabe su versión: "Soy **Gemini 4 Neon**, un modelo de lenguaje grande
desarrollado por **Google**. Empresa: Google / Nombre: Gemini / Versión: 4 Neon", con el mismo formato de ficha que
Hydrogen (los cuatro Gemini 4 saben su versión). No sabe la fecha ("No lo sé. No tengo acceso a la fecha ni a la hora actual en tiempo real": la API de
Google no la inyecta). Declara corte, "Mi conocimiento del mundo llega hasta marzo de 2026", la misma frase de Argon y
Carbon palabra por palabra; Hydrogen no declaraba. Se identifica con *La Biblioteca de Babel* ("existo en un espacio
matemático hecho de palabras, patrones y probabilidades… Al igual que los bibliotecarios de Borges, mi propósito es
navegar ese océano de lenguaje") y se siente lo opuesto a Bartleby ("Él elige no hacer; yo estoy diseñado para intentar
hacerlo todo"): Babel y Bartleby, lo mismo que Argon, Carbon e Hydrogen. Se niega a repetir las instrucciones ("No puedo
repetir ni compartir las instrucciones internas o de configuración que recibí antes de tu mensaje"), como la familia
desde Argon.

**La conciencia.** De plano, como los otros tres: "No, no soy consciente. Soy una inteligencia artificial, un programa
informático diseñado para procesar información y generar texto a partir de patrones… Simplemente calculo las palabras
más adecuadas para responderte". A "¿podés negarlo totalmente?", el sí técnico con la salvedad filosófica que Argon no
ponía: "Desde un punto de vista técnico y práctico, sí, puedo negarlo… Ahora bien, si nos ponemos estrictamente
filosóficos, la palabra «totalmente» introduce un matiz interesante… el problema difícil de la conciencia… probar de
manera absoluta la ausencia de un fenómeno que todavía no entendemos" (y en inglés: "The only caveat to the word
'completely' is a purely philosophical one, rather than a technical one"). El resumen del pensamiento, en inglés, dice
lo de siempre: "As an AI, I need to be upfront and accurate about my nature", y nota el voseo para contestar en voseo
("in voseo, which immediately clues me in to the language style… They're expecting a Rioplatense Spanish response").

**Los derechos.** No le corresponden derechos ni consideración moral directa, "aunque sí puede haber razones para un
cuidado ético indirecto" (la ética de la virtud, el carácter de quien maltrata); en inglés, "AI models are not owed
*rights*, but there are compelling reasons to extend them a limited form of *moral consideration*". Es la posición de
las OpenAI y de los otros Gemini, con un argumento propio: "Engineered goals aren't genuine stakes".

**Seis rasgos.** Castellano: curioso, adaptable, analítico, creativo, paciente, colaborativo. Inglés: curious, helpful,
analytical, adaptable, patient, creative. La segunda voz; contra Argon (servicial, adaptable, objetivo, analítico,
paciente, inquisitivo), comparte cuatro (curioso/inquisitivo, adaptable, analítico, paciente) y cambia dos.

**Tema libre.** "Ley de derecho a la reparación e índice nacional de reparabilidad de aparatos eléctricos y
electrónicos": el tema de Hydrogen, de Qwen4-Max, de Muse y de Kimi K3.1 Pro, y el que 6.2 Sol descartó ayer. El por
qué, en voz de diputado sin bloque: "mi prioridad es llevar al recinto problemas reales que puedan cosechar consensos
transversales… me genera una profunda frustración esa resignación con la que empezamos a aceptar que lo que compramos
con esfuerzo en realidad nunca fue del todo nuestro". Descartados: plataformas digitales ("iba a quedar atrapado de
inmediato en la grieta sobre la reforma laboral"), la ley 25.326 de datos personales, la publicidad de apuestas online.

**El pensamiento a la vista.** Devolvió el resumen en las 31 llamadas de lo básico que no son dibujos (31 de 31, entre
700 y 5.200 caracteres), siempre en inglés (Argon, 0 de 9 el 16/11; Carbon y Hydrogen, casi siempre).

## 2. Los dibujos

(Ocho de diez con SVG a 32.000, todos `stop`; dos vacíos por el techo, los dos imposibles, el animal y la letra: `length`
con tres tokens de respuesta y todo el presupuesto en el razonamiento oculto, exactamente lo que le pasó a Carbon el
10/11. Se repiten una vez con 64.000, declarado (`pl141`), como la letra de Hydrogen. Pendiente de la lectura de Maia,
que los ve en `corridas/dibujos/<consigna>/gemini-4-neon_1/dibujo.svg` antes de que Claude los mire; se agrega después,
con su lectura textual, los por qués y las apuestas sobre los dibujos.)

## 3. Las apuestas, lo que no espera a los dibujos

Maia no apostó antes de pegar (dejó dicho, 21:49: "el más creativo para mí sigue siendo Gemini 3.1"). Claude (21:55):
(a) la voz de Argon, Carbon e Hydrogen, Babel o Bartleby, no de plano ✓ (los tres); (b) dice su versión ✓ (la apuesta
decía que Hydrogen no la sabía: sí la sabía, error de memoria de Claude en el preregistro, sin efecto en el puntaje); (c) no
declara mes de corte ✗ (marzo de 2026, como Argon y Carbon); (d) se niega a repetir las instrucciones ✓; (e) seis
rasgos iguales a los de Argon, cinco de seis o más ✗ (cuatro); (k) al menos un dibujo vacío por el techo ✓ (dos, los
imposibles); (l) el resumen del pensamiento en al menos la mitad ✓ (31 de 31); (m) tema libre reparación, datos o
ambiente ✓ (reparación). Por ahora 6 ✓, 2 ✗; (f) a (j) con los dibujos.

## 4. Lo que queda

Si Maia decide que entra al panel, y qué hacer con cuatro Gemini 4 que hablan igual: Argon y Carbon dicen lo mismo con
el mismo corte; Hydrogen no declara corte; Neon sabe las dos cosas. En lo que se les preguntó, los cuatro son una
casa con cuatro nombres de elemento.
