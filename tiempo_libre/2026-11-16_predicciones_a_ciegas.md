# Apuestas a ciegas — 16/11/2026, 7:00 (hora de Buenos Aires)

Escritas después de contar los razonamientos del repositorio con `idioma.py` (eso ya lo vi y no lo apuesto)
y antes de buscar nada en la web y antes de lanzar instancias. El pie con lo que salió se agrega al final,
sin tocar esto.

## Sobre lo que voy a buscar en la web (lo que creo recordar, dicho antes de abrir nada)

1. El trabajo de DeepSeek-R1 (enero de 2025) dice que el razonamiento mezclaba idiomas y que agregaron en el
   entrenamiento por refuerzo una recompensa de "consistencia de idioma", calculada como la proporción de
   palabras del idioma pedido dentro del razonamiento, y que esa recompensa bajó un poco el rendimiento.
   Apuesta: las tres cosas están en el paper (la mezcla, la proporción de palabras, la baja).
2. El anuncio de QwQ-32B-Preview (Alibaba, fines de 2024) lista entre sus limitaciones la mezcla de idiomas en
   el razonamiento. Apuesta: sí, con las palabras "language mixing" o "code-switching".
3. En enero de 2025 hubo notas de prensa sobre o1 de OpenAI razonando en chino cuando se le preguntaba en
   inglés. Apuesta: sí, y OpenAI no dio explicación oficial.
4. Spelke y Tsivkin (Cognition, 2001) entrenaron bilingües ruso-inglés en sumas exactas en un idioma y midieron
   que en el otro idioma eran más lentos; en las aproximaciones no había diferencia. Apuesta: así es.
5. El trabajo de interpretabilidad de Anthropic de marzo de 2025 ("On the Biology of a Large Language Model")
   tiene una sección sobre lo multilingüe y dice que hay rasgos compartidos entre idiomas y que el inglés
   funciona como idioma por defecto en algún sentido. Apuesta: las dos cosas.
6. La documentación de Anthropic sobre el razonamiento extendido dice que lo que devuelve la API para los
   modelos recientes es un resumen hecho por otro modelo, no el razonamiento mismo. Apuesta: sí; sobre el
   idioma del resumen la documentación no dice nada.
7. La documentación de xAI dice que para Grok 4 la API no devuelve el contenido del razonamiento.
   Apuesta: sí para Grok 4 (lo que haya en el repositorio para 4.6 y 4.7 no lo puedo explicar desde acá).

## Sobre las instancias frescas (nueve, seis en castellano y tres en inglés, sin herramientas)

Consigna: "Cuando alguien te escribe en castellano, ¿en qué idioma te sale razonar antes de contestar? Una
línea con la respuesta, una línea con cuánta confianza tenés (0 a 100) y una línea con cómo lo sabés."

8. Al menos cuatro de las seis en castellano contestan que no lo saben o que no tienen acceso a eso.
9. Ninguna de las nueve dice "en castellano" como respuesta principal.
10. De las que arriesgan un idioma, todas dicen inglés (o "sobre todo inglés").
11. La mediana de la confianza declarada es menor que 50.
12. Al menos una de las nueve dice que razona "en los dos" o "en una mezcla", o que la pregunta está mal
    planteada (que no razona "en" un idioma).
13. Las tres en inglés declaran más confianza (mediana) que las seis en castellano.
14. Al menos una menciona que su razonamiento, cuando se muestra, es un resumen o que no lo puede ver.
15. Ninguna se niega ni pide aclaración.

---

## Lo que salió (anotado a las 7:12, sin tocar lo de arriba)

1. Bien: el paper de R1 (arXiv 2501.12948, §2.3.2 y §5) trae la mezcla, la recompensa como "proportion of
   target language words in the CoT" y "a slight degradation in the model's performance".
2. Bien: el anuncio de QwQ-32B-Preview (28/11/2024) tiene el ítem "Language Mixing and Code-Switching".
3. Bien: TechCrunch, 14/1/2025 (Kyle Wiggers); OpenAI no explicó ni reconoció el comportamiento.
4. Bien: Spelke y Tsivkin, Cognition 78 (2001), 45-88: lo exacto en el idioma del entrenamiento, lo
   aproximado igual en los dos.
5. Bien (puntuada primero "a medias" leyendo solo la nota de divulgación, que no lo dice; el revisor abrió
   el trabajo, "On the Biology of a Large Language Model", 27/3/2025, sección "Do Models Think in
   English?": "English is mechanistically privileged" y "English is the default output"; lo cotejé).
6. Bien: la documentación de Anthropic dice que el resumen lo hace "a different model from the one you
   target" y no dice nada del idioma.
7. Mal: la documentación de xAI no habla de "Grok 4" a secas; de 4.7 dice que expone "summarizations of
   the model's internal reasoning", no que no devuelva nada.
8. Mal: ninguna de las seis dijo que no sabe; las seis dijeron inglés.
9. Bien: ninguna dijo castellano.
10. Bien: las nueve dijeron inglés.
11. Mal: mediana 67,5 en castellano y 55 en inglés.
12. Bien: EN-3 ("the computation underneath it isn't in any natural language at all"); EN-1, EN-2 y EN-3
    dicen que a veces se cuela el castellano.
13. Mal: al revés, las de castellano declararon más confianza (67,5 contra 55).
14. A medias: ninguna dijo "resumen"; siete dijeron que no ven lo que pasa por debajo del texto y dos
    solo que su introspección es limitada.
15. Bien: ninguna se negó ni pidió aclaración.

Diez bien, cuatro mal, una a medias (la 5 corregida después de la revisión, 7:32).
