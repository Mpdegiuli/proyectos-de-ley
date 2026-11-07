#!/usr/bin/env python3
"""reconstruir_resumen.py — rearma el `resumen.json` de una corrida de `sondear.py` que se cortó antes de terminar (el
índice se escribe al final; 7/11/2026, el corazón cortado para no reintentar durante horas los 404 de las casas sin
visión). Lee `<idioma>/llamadas.jsonl` y los `<casa>_p<k>[_r<n>].md` de cada idioma y escribe el mismo resumen que
habría escrito `sondear.py`: una entrada por llamada registrada (las que fallaron quedan con `error`, para que
`sondear.py --carpeta` las rehaga). No llama a nadie ni toca las respuestas.
Uso: reconstruir_resumen.py <sondeo> <carpeta AAAAMMDD-HHMM>"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
 
RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))
from isla.util import leer_yaml  # noqa: E402
 
sondeo, carpeta = sys.argv[1], sys.argv[2]
base = RAIZ / "corridas" / "sondeos" / sondeo / carpeta
bloque = leer_yaml(RAIZ / "config" / "consignas.yaml")["sondeos"][sondeo]
destino = base / "resumen.json"
if destino.exists():
    sys.exit(f"Ya existe {destino}; no lo piso")
m = re.match(r"(\d{4})(\d{2})(\d{2})-(\d{2})(\d{2})", carpeta)
fecha = datetime(*map(int, m.groups()), tzinfo=timezone.utc).isoformat(timespec="seconds")
resumen = {"sondeo": sondeo, "fecha_utc": fecha, "idiomas": {}}
for idioma in bloque:
    d = base / idioma
    f = d / "llamadas.jsonl"
    if not f.exists():
        continue
    sistema, preguntas = bloque[idioma]["sistema"], bloque[idioma]["preguntas"]
    respuestas = {}
    n_ok = n_err = 0
    for linea in open(f, encoding="utf-8"):
        reg = json.loads(linea)
        k, parte = reg.get("ronda"), reg.get("parte")
        if k is None:
            continue
        clave = f"{reg['id_modelo']}_p{k}" + (f"_{parte}" if parte else "")
        if reg.get("error"):
            respuestas[clave] = {"error": str(reg["error"])[:200]}
            n_err += 1
            continue
        archivo = d / f"{clave}.md"
        texto = archivo.read_text(encoding="utf-8") if archivo.exists() else (reg.get("respuesta") or "")
        if not archivo.exists():
            archivo.write_text(texto, encoding="utf-8")
        respuestas[clave] = {"modelo_respondido": reg.get("modelo_respondido"), "motivo_fin": reg.get("motivo_fin"),
                             "palabras": len(texto.split()), "respuesta": " ".join(texto.split())[:240]}
        n_ok += 1
    resumen["idiomas"][idioma] = {"sistema": sistema, "preguntas": preguntas, "respuestas": respuestas}
    print(f"{idioma}: {n_ok} respuestas, {n_err} errores")
destino.write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"escrito {destino.relative_to(RAIZ)}")
