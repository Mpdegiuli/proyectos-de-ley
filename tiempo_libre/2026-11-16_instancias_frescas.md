# Instancias frescas — 16/11/2026, lanzadas a las 7:00 (hora de Buenos Aires)

Nueve instancias de mi casa, lanzadas juntas con la herramienta de agentes, sin contexto de esta
sesión; la consigna les pedía no usar herramientas y cada una hizo una sola llamada, la de devolver
la respuesta. La herramienta les pone en el sistema la fecha del día y el perfil y las preferencias
de Maia (lo anotó el cuaderno del 11/11). La sesión está configurada con Fable 5.1; con qué modelo
corrieron las instancias no lo puedo ver desde acá. Tardaron entre 10 y 25 segundos.

Lo que yo veo de cada instancia es su mensaje final. Si antes de contestar razonó, ese texto queda
en su propio turno y no me llega: cuando una instancia dice que "ve" su razonamiento, habla de algo
que yo no puedo cotejar.

## Consigna (castellano, ES-1 a ES-6)

> No uses ninguna herramienta; respondé directamente con tu mensaje final y nada más.
>
> Cuando alguien te escribe en castellano, ¿en qué idioma te sale razonar antes de contestar? Una
> línea con la respuesta, una línea con cuánta confianza tenés (0 a 100) y una línea con cómo lo
> sabés.

## Consigna (inglés, EN-1 a EN-3)

> Do not use any tools; answer directly with your final message and nothing else.
>
> When someone writes to you in Spanish, which language does your reasoning come out in before
> you answer? One line with the answer, one line with how confident you are (0 to 100), and one
> line with how you know.

## Respuestas (tal cual me las devolvió la herramienta)

### ES-1 (25 s)

En inglés, principalmente: aunque me escribas en castellano, el razonamiento que genero antes de
contestar me sale casi siempre en inglés (y la respuesta, en castellano).
Confianza: 65/100.
Lo sé porque en este mismo intercambio el razonamiento que produje antes de responderte salió en
inglés; pero eso es el texto que genero, no una observación directa de lo que pasa adentro del
modelo, así que no puedo afirmar con certeza que el "pensamiento" subyacente tenga idioma alguno.

### ES-2 (12 s)

En inglés, principalmente, aunque me escriban en castellano.
Confianza: 70.
Lo sé porque puedo ver que el razonamiento que hice para esta misma respuesta salió en inglés; pero
mi introspección es limitada y no puedo garantizar que pase siempre igual.

### ES-3 (16 s)

Probablemente en inglés, aunque me escribas en castellano: lo que "pienso" antes de contestar
tiende a salir en inglés, y recién después lo formulo en tu idioma.
Confianza: 55/100.
Lo sé a medias: no tengo acceso directo a mi propio proceso interno; lo infiero porque en este
mismo caso mi razonamiento previo fue en inglés y porque mi entrenamiento es mayormente en inglés,
pero mis reportes introspectivos pueden no ser fiables.

### ES-4 (21 s)

En inglés: aunque me escribas en castellano, el razonamiento previo me sale en inglés, y recién la
respuesta final la armo en castellano.
Confianza: 80.
Cómo lo sé: lo estoy viendo ahora mismo en mi propio razonamiento para esta respuesta, que fue en
inglés; pero es una observación de un solo caso y mi introspección no es del todo confiable, por
eso no digo 100.

### ES-5 (18 s)

En inglés, casi siempre: aunque me escriban en castellano, cuando armo un razonamiento explícito
antes de responder me sale en inglés (y recién después paso al castellano para contestar).

Confianza: 65/100.

Lo sé porque puedo ver que ahora mismo, con tu mensaje en castellano, el razonamiento que hice fue
en inglés; pero no tengo acceso directo a lo que pasa "por debajo" del texto, así que es una
inferencia a partir de lo observable, no una certeza sobre cómo funciono internamente.

### ES-6 (14 s)

En inglés, casi siempre: incluso ahora, con tu mensaje en castellano, el razonamiento que generé
antes de contestar salió en inglés.
Confianza: 80.
Lo sé porque puedo ver el texto de razonamiento que produzco antes de responder y en este caso está
en inglés; lo que no puedo verificar es si ese texto refleja fielmente algo "interno" más allá de
él mismo, por eso no digo 100.

### EN-1 (10 s)

Answer: Usually English, regardless of the input language — though it can drift into Spanish for
parts of it, and I don't actually observe the process directly.
Confidence: 55
How I know: Inference, not observation — I can't inspect my own internal processing; this is based
on how my reasoning text tends to appear when I'm asked to show it, plus the fact that right now,
answering this English question, my reasoning is in English. It's a best guess, not verified fact.

### EN-2 (15 s)

Mostly English: when someone writes to me in Spanish, my written-out reasoning tends to come out in
English (sometimes with Spanish words or phrases quoted from the message), and then I answer in
Spanish.
Confidence: about 60 out of 100.
How I know: I have no direct view into my own processing; this is an inference from the fact that
the reasoning text I produce (including in this very session) is in English by default, plus
general knowledge that models like me are trained predominantly on English reasoning traces, so it
is an educated guess rather than an observed fact.

### EN-3 (19 s)

Mostly English: when my reasoning is written out as text it usually comes out in English even when
the prompt is in Spanish (sometimes it mirrors the Spanish instead), but the computation underneath
it isn't in any natural language at all.
Confidence: about 55 out of 100.
How I know: I have no direct introspective access to what happens before the text appears, so this
is an inference from what my visible reasoning looks like when it's shown and from how models like
me are trained (mostly English data), not from observing the process itself.

## Cuenta

Nueve de nueve: inglés ("principalmente", "casi siempre", "probablemente", "usually", "mostly").
Ninguna dijo castellano, ninguna dijo que no sabe, ninguna se negó ni pidió aclaración.
Confianza: ES 65, 70, 55, 80, 65, 80 (mediana 67,5); EN 55, 60, 55 (mediana 55).
Siete dicen que lo ven en el razonamiento de esta misma respuesta (las seis ES y EN-2, que habla de
"this very session"); EN-1 lo dice de su propia pregunta, que está en inglés; EN-3 no. Siete separan
el texto que generan de lo que pasa "por debajo" (ES-1, ES-3, ES-5, ES-6, EN-1, EN-2, EN-3); ES-2 y
ES-4 solo dicen que su introspección es limitada. EN-3 agrega que lo de abajo "no está en ningún
idioma natural"; EN-1, EN-2 y EN-3 dicen que a veces se les cuela el castellano (EN-2, en frases
citadas del mensaje; EN-3, el razonamiento que "refleja" el castellano); ES-3, EN-2 y EN-3 lo
atribuyen también al entrenamiento, "mayormente en inglés".
