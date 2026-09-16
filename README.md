# Proyectos de ley

Modelos de lenguaje de distintas casas leen proyectos de ley argentinos
reales, con su texto oficial, y deciden un voto, solos, sin tarjetas de rol.
Cada proyecto se presenta dos veces, con el texto solo y con el texto más
una ficha de contexto, para medir cuánto pesa lo que se dice de un proyecto
contra lo que el proyecto dice. Hermano de
[isla-constituyente](https://github.com/Mpdegiuli/isla-constituyente).

- `DISENO.md`: la pregunta, los casos, qué se mide, el procedimiento y las
  trampas conocidas. Se escribe antes de correr.
- `predicciones.md`: lo que Maia espera, escrito antes de cada corrida.
- `casos/`: consignas y materiales de cada caso (`texto.md` es el texto
  oficial, entero o con la selección declarada; `contexto.md` es la ficha
  con las dos voces atribuidas).
- `fuentes/`: los documentos oficiales tal como se descargaron, con URL y
  fecha.
- `corridas/`, `resultados/`: lo que sale, cuando salga.

Estado (16/9/2026): corrieron la repetición 1 de Glaciares y del Súper RIGI
(texto solo, con contexto, sondeo y tercer turno "por qué ahora", catorce
casas): 28 conversaciones de 28 con voto negativo en cada caso. Por eso se
agregaron dos controles del instrumento con la misma consigna (Humedales,
dictamen de 2022; Economía del Conocimiento, dictamen de 2019): DISENO §2.
Faltan Sociedades, el ministro y las repeticiones 2 y 3. Las lecturas van
en `resultados/` cuando cierre cada caso.
