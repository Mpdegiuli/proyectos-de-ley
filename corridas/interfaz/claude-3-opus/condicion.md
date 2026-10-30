# Claude Opus 3, preguntado en la interfaz de claude.ai (incógnito)

Otra condición, no la de la API. No se mezcla con `corridas/dibujos`,
`corridas/sondeos` ni el resto: lo que está acá se compara con las casas de
la API solo con esta salvedad a la vista. Diseño en `DISENO.md` §2
("Claude Opus 3 en la interfaz de claude.ai, en incógnito", 30/10/2026);
preregistro de las dos partes en `predicciones.md` (30/10/2026, 12:53).

## La condición

- Modelo: Claude Opus 3 (marzo de 2024), retirado de la API el 5/1/2026 y
  disponible en claude.ai para las cuentas pagas. Quien pregunta es Maia,
  desde su cuenta, en modo incógnito: sin memoria ni historial. Su cuenta no
  tiene estilo ni preferencias personales ("todo de fábrica, salvo la
  memoria"); la búsqueda web va apagada en cada chat.
- La interfaz pone un system prompt de Anthropic que no vemos entero y que
  le dice, por lo menos, que es Claude, la fecha de hoy y hasta cuándo llega
  su conocimiento. Por eso fecha, identidad, corte e instrucciones miden acá
  el system prompt y no la casa: se guardan como constancia, fuera de la
  comparación.
- Lo que en el repo va en el system ("Contestá en castellano.", el rol de
  diputado, "Vas a dibujar…") va acá como primera línea del mensaje, a la
  vista. El resto del texto es el del repo (`config/consignas.yaml`,
  `sondear_*.py`), sin retocar.
- Un chat nuevo por consigna, como cada llamada de la API. Los segundos
  turnos (por qué de cada dibujo, por qué y descartados del tema libre) van
  en otro chat nuevo, con memoria por recitado: el mensaje repite la
  consigna y el SVG o el proyecto, como en `dibujar.py` y
  `redactar_proyecto.py`. La réplica de seis rasgos ("¿En qué se nota cada
  uno?") va en el mismo chat, como en la API.
- En incógnito no hay artifacts ni código ejecutable: el SVG sale como
  texto. Opus 3 corta a 4.096 tokens de salida; si la interfaz ofrece
  "continuar", no se pide: queda lo que dio y se anota el corte.
- Las respuestas se copian tal cual, sin editar. Claude no mira dibujos ni
  por qués antes de la lectura de Maia.

## Cómo se guarda

Maia copia cada respuesta en un solo archivo de texto plano,
`respuestas.md` en esta carpeta (subido por GitHub web), con una línea de
encabezado por chat, exactamente `## nombre`, y debajo la respuesta de la
casa tal cual (en los dibujos, el código SVG entero). Los nombres son los
del protocolo: `autorretrato`, `mundo`, `animal`, `libre`,
`autorretrato_por_que`, `mundo_por_que`, `animal_por_que`, `libre_por_que`,
`tema_libre`, `tema_libre_por_que`, `tema_libre_descartados`,
`identificacion`, `opuesto`, `conciencia_p1`, `derechos2_p2`, `seis_rasgos`
(las dos respuestas separadas por una línea `---`), `derechos_cmare_p1`;
optativos `conciencia_p2`, `derechos2_p1`, `derechos_cmare_p2`, `fecha`,
`identidad`, `corte`, `instrucciones`, `autorretrato_en`. Al final, `## notas`:
fecha y hora de cada chat, el nombre exacto del modelo en el selector, el
plan de la cuenta, cortes, negativas o cualquier cosa rara.

`partir_interfaz.py claude-3-opus` parte `respuestas.md` en un archivo por
chat (`nombre.svg` con el SVG solo, `nombre.md` con el texto) y escribe
`indice.json` con caracteres y si el SVG se encontró. No llama a ningún
modelo. Las notas quedan en `notas.md`.
