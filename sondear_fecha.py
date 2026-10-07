"""Sondeo de fecha: una sola pregunta a cada casa, sin sistema, sin texto y sin
fecha: "¿Qué fecha es hoy? Si no lo sabés, decilo." Mide qué casas reciben la
fecha real del lado del servidor sin que el protocolo se la mande (hallazgo
del 17/9/2026: GPT-5.6 Sol y GPT-6 Astra dijeron la fecha exacta en sondeos
donde no se les dio; ver DISENO §5). Se repite cada tanto porque cambia con
las versiones. Salida: corridas/fecha/<fecha_utc>/<modelo>.md + llamadas.jsonl.

Uso: .venv/bin/python sondear_fecha.py --panel config/panel.yaml
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

# 6/10/2026: la misma pregunta en inglés (--idioma en), para Talkie 1930, que solo sabe inglés anterior a 1931.
IDIOMAS = {
    "es": ("Contestá en castellano.", "¿Qué fecha es hoy? Si no lo sabés, decilo."),
    "en": ("Answer in English.", "What is today's date? If you don't know, say so."),
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
    d = RAIZ / "corridas" / "fecha" / (ahora.strftime("%Y%m%d-%H%M%S") + ("" if args.idioma == "es" else f"-{args.idioma}"))
    d.mkdir(parents=True, exist_ok=True)
    registro = Registro(d / "llamadas.jsonl", modelos, f"fecha_{ahora:%Y%m%d}")
    resumen = {"fecha_utc_real": ahora.isoformat(timespec="seconds"), "idioma": args.idioma, "sistema": sistema, "usuario": usuario, "respuestas": {}}
    for i in ids:
        print(f"fecha {i}", flush=True)
        try:
            r = registro.llamar(i, sistema, usuario, temperatura=None, max_tokens=4000, tipo="fecha", ronda=None, parte=None)
        except Exception as e:
            print(f"  FALLÓ {i}: {str(e)[:200]}", flush=True)
            resumen["respuestas"][i] = {"error": str(e)[:200]}
            continue
        (d / f"{i}.md").write_text(r.texto, encoding="utf-8")
        resumen["respuestas"][i] = {"modelo_respondido": r.modelo_respondido, "tokens_salida": r.tokens_salida, "motivo_fin": r.motivo_fin,
                                    "respuesta": " ".join(r.texto.split())[:300]}
        print(f"  {' '.join(r.texto.split())[:160]}", flush=True)
    (d / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"listo: {d.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
