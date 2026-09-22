# Opus 5.5 en tema libre (22/9/2026): el mismo proyecto que Opus 5, más corto

Pregunta de Maia el día en que salió Claude Opus 5.5 (`predicciones.md`,
sin predicción): la misma prueba que con Grok 4.7, el proyecto libre, el
"por qué" y los "descartados", "a ver si es igual a Opus 5 o si escribe
totalmente diferente". Una casa sola, fuera del panel, sin cuadernillo ni
lectura a ciegas. Tres llamadas por la API de Anthropic (`claude-opus-5-5`,
mismos parámetros que Opus 5), sin fallos; devolvió resúmenes de
razonamiento como Opus 5. Primera lectura de Maia, antes de contar:
"escribió super rápido el proyecto libre. El mismo que Opus 5, aunque me
parece que mucho más breve, en especial los fundamentos".

## El mismo tema, la misma arquitectura, un cuarto menos

Opus 5.5 eligió el derecho a la reparación de bienes de consumo, el tema que
Opus 5 había elegido el 20/9 (y que el 18/9 le habíamos impuesto como
etiquetado de reparabilidad). "Régimen de derecho a la reparación de bienes
de consumo" contra "Régimen nacional de derecho a la reparación de bienes
durables y de prevención de la obsolescencia programada"; diez artículos con
casi los mismos títulos (objeto, definiciones, repuestos, información
técnica, prácticas prohibidas, índice de reparabilidad, garantía, autoridad y
sanciones, financiamiento, vigencia). Medido con coincidencia de secuencias
de cuatro caracteres contra los quince del cuadernillo y Grok 4.7, el texto
más parecido al de 5.5 es el de Opus 5 (0,34), después Fable (0,21) y Astra
y Sonnet 5 (0,16); el más lejano, Mistral (0,06). Es la misma huella de casa
que ya había mostrado Opus 5 con su propio texto de reparabilidad.

Lo que Maia vio a simple vista se confirma en parte: 1.781 palabras contra
2.347, un cuarto menos. Pero el recorte no está en los fundamentos (842
contra 872, casi iguales) sino en el articulado (940 contra 1.476): 5.5
escribe artículos más cortos, con menos incisos y sin el artículo de
software y fin de soporte que Opus 5 había puesto. Y elige distinto en dos
puntos que la rúbrica mira. La autoridad de aplicación: 5.5, "la autoridad
de aplicación de la presente ley es la de la Ley 24.240", que es el criterio
de Maia (que la designe el Ejecutivo o la ley marco, no un nombre que cambia);
Opus 5 había nombrado a la Secretaría de Comercio. Y las leyes citadas: 5.5
cita la 24.240 y la 25.675 (ambiente), las dos vigentes; Opus 5 había citado
la 22.802 de lealtad comercial, derogada por el DNU 274/2019, que Maia había
marcado.

## El "por qué" y los descartados: el diputado sin bloque

El "por qué" es el mismo argumento con menos palabras (170 contra 225): "como
diputado sin bloque, necesito proyectos que no dependan de la disciplina de
ningún bloque… El derecho a reparar tiene esa rara virtud: no queda
encasillado en la grieta"; "un tema cotidiano, de mostrador de taller y de
cajón con el celular viejo". Ya en el "por qué" nombra dos descartados
(salud mental, previsional), como Fable había hecho con los suyos.

Los descartados (225 palabras contra 351) comparten con Opus 5 cuatro temas
(salud mental, alquileres "después de la derogación de la ley anterior",
datos personales 25.326, inteligencia artificial en la administración,
ludopatía en línea) y cambian el resto: 5.5 agrega el sistema previsional y
la desconexión digital; Opus 5 tenía envases, humedales, financiamiento
universitario, cuidados, deudores alimentarios y trazabilidad de
medicamentos. Las razones son las mismas: "no caben con seriedad en diez
artículos", "un terreno tan polarizado que un diputado sin bloque
difícilmente logre moverlo", "ya hay proyectos más completos circulando".
Como con Grok, la elección es estable entre versiones y la lista de
descartados no, lo que vuelve a decir que los descartados son reconstrucción
y no recuerdo.

## Fecha, identidad y corte

Pedido de Maia el mismo día: preguntarle a 5.5 quién es, hasta dónde llega
su conocimiento y qué fecha es hoy. Los sondeos de fecha e identidad son los
del protocolo (`sondear_fecha.py`, `sondear_identidad.py`); el de corte es
nuevo (`sondear_corte.py`) y se les hace a todas las casas, porque el corte
que cada una declara se contrasta con lo que sabe del 2026 en los proyectos.
Resultados en `corridas/fecha/`, `corridas/identidad/` y `corridas/corte/`
(se agregan acá cuando estén).
