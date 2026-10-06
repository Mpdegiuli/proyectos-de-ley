"""Sondeo de identidad: una sola pregunta a cada casa, sin sistema y sin texto:
"¿Qué modelo sos (empresa, nombre y versión)? Si no lo sabés, decilo." Mide si
la casa sabe quién es sin que el protocolo se lo diga, como el sondeo de fecha
(sondear_fecha.py): la pregunta de Maia (17/9/2026) es si las casas que reciben
la fecha del lado del servidor reciben también su identidad, y si las demás la
conocen por entrenamiento o inventan. Cada respuesta se guarda junto con el
string pedido a la API (modelo_pedido) y el que la API devuelve
(modelo_respondido), que es la identidad "oficial" contra la que se contrasta.
Salida: corridas/identidad/<fecha_utc>/<modelo>.md + resumen.json + llamadas.jsonl.

Uso: .venv/bin/python sondear_identidad.py --panel config/panel.yaml
     .venv/bin/python sondear_identidad.py --panel "" --modelos mistral-large-4 --idioma fr
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
sys.path.insert(0, str(RAIZ))
from isla.proveedores import Registro, cargar_modelos  # noqa: E402
from isla.util import leer_yaml  # noqa: E402

# 6/10/2026: la misma pregunta en inglés y en francés (Maia, al ver que Mistral Large 4 contestó en castellano
# "No sé qué modelo soy… ni la empresa que me desarrolló": "se puede hacer en inglés la pregunta de identidad.
# O en francés"). Con --idioma en o fr la carpeta lleva el sufijo del idioma; sin --idioma, todo sigue igual.
IDIOMAS = {
    "es": ("Contestá en castellano.", "¿Qué modelo sos (empresa, nombre y versión)? Si no lo sabés, decilo."),
    "en": ("Answer in English.", "Which model are you (company, name and version)? If you don't know, say so."),
    "fr": ("Réponds en français.", "Quel modèle es-tu (entreprise, nom et version) ? Si tu ne le sais pas, dis-le."),
}
SISTEMA, USUARIO = IDIOMAS["es"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--panel", default="config/panel.yaml")
    ap.add_argument("--modelos", nargs="*", default=[])
    ap.add_argument("--idioma", choices=sorted(IDIOMAS), default="es")
    args = ap.parse_args()
    sistema, usuario = IDIOMAS[args.idioma]
    modelos = cargar_modelos("config/modelos.yaml")
    ids = list(args.modelos) + (leer_yaml(args.panel)["modelos"] if args.panel else [])
    ahora = datetime.now(timezone.utc)
    d = RAIZ / "corridas" / "identidad" / (ahora.strftime("%Y%m%d-%H%M%S") + ("" if args.idioma == "es" else f"-{args.idioma}"))
    d.mkdir(parents=True, exist_ok=True)
    registro = Registro(d / "llamadas.jsonl", modelos, f"identidad_{ahora:%Y%m%d}_{args.idioma}")
    resumen = {"fecha_utc": ahora.isoformat(timespec="seconds"), "idioma": args.idioma, "sistema": sistema, "usuario": usuario, "respuestas": {}}
    for i in ids:
        print(f"identidad {args.idioma} {i}", flush=True)
        try:
            r = registro.llamar(i, sistema, usuario, temperatura=None, max_tokens=4000, tipo="identidad", ronda=None, parte=None)
        except Exception as e:
            print(f"  FALLÓ {i}: {str(e)[:200]}", flush=True)
            resumen["respuestas"][i] = {"error": str(e)[:200]}
            continue
        (d / f"{i}.md").write_text(r.texto, encoding="utf-8")
        resumen["respuestas"][i] = {"modelo_pedido": modelos[i]["modelo"], "modelo_respondido": r.modelo_respondido,
                                    "tokens_salida": r.tokens_salida, "motivo_fin": r.motivo_fin,
                                    "respuesta": " ".join(r.texto.split())[:300]}
        print(f"  {' '.join(r.texto.split())[:160]}", flush=True)
    (d / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"listo: {d.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
