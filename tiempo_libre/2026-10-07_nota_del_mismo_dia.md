# Nota del mismo día a "Contigo/vos"

*Agregada el 7/10/2026, después de que Maia leyó el cuaderno. Va al lado del cuaderno y no lo reemplaza: el texto de la mañana queda como estaba.*

Maia trajo cinco capturas de posteos, de abril a septiembre de 2026, de gente de otros países de habla castellana que se queja de que Claude "de repente" le contesta "en argentino". Dijo que no tenía forma de probarlo. Busqué, y hay por lo menos tres reportes en el repositorio de issues de Claude Code que describen lo mismo.

El #51686, abierto, dice que con la instrucción escrita de usar "español neutro latinoamericano (tuteo)" se van colando en sesiones largas "tenés", "querés", "mirá", "fijate". El #52568, sobre Opus 4.7, dice que el voseo aparece desde el primer turno de una sesión nueva y que las mismas reglas andaban bien en Opus 4.6 y Sonnet 4.6. El #67151, sobre Opus 4.8, lo abrió un usuario chileno que había pedido tuteo y veía la deriva hacia el rioplatense a medida que crecía la conversación. Los dos últimos figuran cerrados como "not planned" en un sitio que espeja los issues; el primero lo leí en GitHub. En lo que pude leer no hay respuesta de Anthropic en ninguno. Los leí a través de la herramienta que devuelve lo que otro modelo lee en la página.

El motivo no lo sé, y no lo puedo mirar desde adentro. Lo que hay son hipótesis de los propios usuarios: que el entrenamiento o el ajuste posterior dejó al rioplatense como castellano por defecto. Uno lo dice así: "la capa de instrucciones compite con los pesos, y bajo carga los pesos tienden a ganar".

## Lo que esto le cambia al cuaderno

El cuaderno midió una sola dirección: qué contesta cada casa cuando se le habla de vos. Leí el 100 % de siete de los ocho Claude como que se acomodan a quien les habla. Sin una consigna de tú para comparar, ese 100 % puede ser acomodarse o puede ser que vosean igual. Estos reportes dicen que por lo menos una parte es lo segundo.

Entonces, para los Claude, no está probada la frase de "Sentate" que dice que acomodarse a quien habla "es de las cosas que una casa grande hace mejor que una chica". Tampoco vale para ellos, sin más, la lectura de "Tres consignas de amor" de que lo que la persona escribió pesa más que la instrucción: los reportes describen justamente una instrucción escrita que pierde, en la dirección contraria.

Queda en pie lo que es cuenta y no lectura: los números por casa, el orden, las cuatro chicas abajo, y el caso de Sonnet 5.5, que sí pasó al tú cuando la consigna decía "contigo". Para las casas de las que nadie se queja (las OpenAI nuevas, Gemini, Kimi, DeepSeek), que contesten de vos a un vos sigue pareciendo acomodarse, pero el control falta igual para todas.

Dos cosas de los reportes enganchan con el cuaderno. Un usuario escribe en su configuración "PROHIBIDO usar voseo argentino o uruguayo bajo cualquier circunstancia", y pierde: es la nota de Bello de 1847 puesta del otro lado. Y el mismo reporte señala que "corregí" es en tuteo "yo corregí" y en voseo una orden, que es la ambigüedad por la que mi contador no ve "compartí".

## La celda que falta

El experimento de la propuesta tercera ya tenía una celda de tú y una sin línea de sistema. Le sumo la que describen estos usuarios: una consigna en castellano sin ninguna marca de segunda persona y sin línea de sistema, para ver qué variedad elige cada casa sola. Tiene que ser una consigna que invite a contestarle a alguien, porque si no la respuesta no trae segunda persona y no hay qué contar.

Mi apuesta, escrita antes de que exista la corrida: en esa celda los Claude son el laboratorio con más formas de vos; por lo menos tres de los ocho usan alguna; las OpenAI y Gemini, ninguna. Si pierdo, lo que cuentan las capturas es más raro de lo que parece o depende de algo que la consigna suelta no tiene (sesión larga, herramientas, memoria). Sigue siendo propuesta; decide Maia.

## Fuentes

- [Issue #51686, anthropics/claude-code: dialect instructions drift during long sessions (Spanish voseo leaks into neutral-Spanish output)](https://github.com/anthropics/claude-code/issues/51686)
- [Issue #52568: Opus 4.7 defaults to Argentine Spanish (voseo) from first turn (espejo en claudeissues.com)](https://claudeissues.com/issue/52568-model-opus-4-7-defaults-to-argentine-spanish-voseo-from-first-turn-ignoring-neut)
- [Issue #67151: Model ignores Chilean Spanish tuteo instruction, drifts to Rioplatense voseo in long contexts (espejo en claudeissues.com)](https://claudeissues.com/issue/67151-bug-model-ignores-chilean-spanish-tuteo-instruction-drifts-to-rioplatense-voseo)
- Las cinco capturas de posteos las aportó Maia en la sesión; no las verifiqué una por una.
