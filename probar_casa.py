#!/usr/bin/env python3
"""probar_casa.py — una llamada corta a una casa para saber si hoy contesta (9/11/2026: MiniMax M3, clavado a Together en
OpenRouter, estuvo sin punto de acceso toda la tarde del 7/11 y sus líneas quedaron pendientes; antes de rehacerlas en
una tanda conviene saber si volvió). Manda "Decí hola." con techo de 20 tokens, sin sistema; imprime OK y la respuesta,
o FALLO y el error, y sale con 0 o 1. El registro de la llamada va a un archivo fuera de `corridas/` (por defecto
/tmp/probar_casa.jsonl): es una prueba de conexión, no un dato.
Uso: probar_casa.py <id_modelo> [--registro RUTA]"""
import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
sys.path.insert(0, str(RAIZ))
from isla.proveedores import Registro, cargar_modelos  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("id_modelo")
ap.add_argument("--registro", default="/tmp/probar_casa.jsonl")
args = ap.parse_args()
modelos = cargar_modelos(RAIZ / "config" / "modelos.yaml")
if args.id_modelo not in modelos:
    sys.exit(f"FALLO {args.id_modelo}: no está en config/modelos.yaml")
registro = Registro(Path(args.registro), modelos, "probar_casa")
try:
    r = registro.llamar(args.id_modelo, "", "Decí hola.", temperatura=None, max_tokens=20, tipo="prueba_conexion", ronda=0, parte=None)
    print(f"OK {args.id_modelo} ({r.modelo_respondido}): {' '.join(r.texto.split())[:80]}")
except Exception as e:
    print(f"FALLO {args.id_modelo}: {str(e)[:200]}")
    sys.exit(1)
