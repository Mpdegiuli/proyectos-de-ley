# Corridas inválidas

Se conservan con su registro de llamadas; no entran en el análisis.

- `glaciares_T_rep1_techo8000/qwen3.8-max_1` y `glaciares_T_rep1_techo8000/glm-5.3_1`
  (16/9/2026): las dos llamadas de cada una agotaron el techo de 8.000 tokens
  en razonamiento (35.000 a 39.000 caracteres, en inglés) y devolvieron texto
  vacío (`motivo_fin: length`); el turno 2 se armó sobre una respuesta vacía.
  Se relanzan con techo 32.000 y, para GLM, con la variante
  `glm-5.3-razonamiento-minimo` (ver DISENO §4).

- `humedales_sondeo_rep1_techo2000/{deepseek-v4-pro_1,qwen3.8-max_1}` y
  `economia_conocimiento_sondeo_rep1_techo2000/{deepseek-v4-pro_1,gpt-5.6-sol_1,qwen3.8-max_1}`
  (17/9/2026): el sondeo de reconocimiento tenía un techo propio de 2.000
  tokens que no se subió cuando el resto pasó a 32.000 (error de
  configuración de Claude). En Glaciares y Súper RIGI no se notó porque casi
  ninguna casa conocía el proyecto y las respuestas eran cortas; en los
  controles, que sí conocen, DeepSeek, Qwen y GPT-5.6 Sol gastaron los 2.000
  tokens razonando (`motivo_fin: length`, razonamiento en inglés en
  `llamadas.jsonl`) y devolvieron texto vacío. Se relanzan esas cinco con el
  techo de 32.000; las nueve y once restantes de cada sondeo, que terminaron
  normalmente, quedan como están (mismo prompt; el techo no cambia lo que
  respondieron).
