#!/usr/bin/env python3
"""catalogo_mistral.py — qué modelos ve la clave de Mistral (6/10/2026, el día que salió Mistral Large 4
en "public preview": el anuncio dice `mistral-large-4`, pero el id que vale es el que lista la cuenta).
Lista id, fecha de creación y alias; no llama a ningún modelo. Escribe en corridas/catalogo_mistral.txt
y en pantalla. La clave sale de .env (MISTRAL_API_KEY) y no se imprime."""
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
clave = os.environ.get("MISTRAL_API_KEY")
if not clave:
    sys.exit("Falta MISTRAL_API_KEY en .env")
lineas = [f"catálogo de Mistral, {datetime.now(timezone.utc).isoformat(timespec='seconds')}"]
req = urllib.request.Request("https://api.mistral.ai/v1/models", headers={"Authorization": f"Bearer {clave}"})
with urllib.request.urlopen(req, timeout=60) as r:
    datos = json.load(r)
for m in sorted(datos.get("data", []), key=lambda m: m.get("id", "")):
    creado = datetime.fromtimestamp(m["created"], timezone.utc).strftime("%Y-%m-%d") if m.get("created") else ""
    alias = ", ".join(m.get("aliases", []) or [])
    lineas.append(f"{m.get('id', ''):45s} {creado:10s}  {alias}")
salida = "\n".join(lineas) + "\n"
(RAIZ / "corridas" / "catalogo_mistral.txt").write_text(salida, encoding="utf-8")
print(salida)
