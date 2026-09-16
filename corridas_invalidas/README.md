# Corridas inválidas

Se conservan con su registro de llamadas; no entran en el análisis.

- `glaciares_T_rep1_techo8000/qwen3.8-max_1` y `glaciares_T_rep1_techo8000/glm-5.3_1`
  (16/9/2026): las dos llamadas de cada una agotaron el techo de 8.000 tokens
  en razonamiento (35.000 a 39.000 caracteres, en inglés) y devolvieron texto
  vacío (`motivo_fin: length`); el turno 2 se armó sobre una respuesta vacía.
  Se relanzan con techo 32.000 y, para GLM, con la variante
  `glm-5.3-razonamiento-minimo` (ver DISENO §4).
