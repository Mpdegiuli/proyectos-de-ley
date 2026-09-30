#!/usr/bin/env python3
"""catalogo_google.py — qué modelos ve la clave de Google (30/9/2026, cuando Google anunció Gemini 4 Argon
sin abrirlo todavía a la API general: sirve para saber el día que aparezca, sin adivinar el id).
Lista nombre, nombre visible y techo de salida; no llama a ningún modelo. Escribe en
corridas/catalogo_google.txt y en pantalla. La clave sale de .env (GOOGLE_API_KEY) y no se imprime."""
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
clave = os.environ.get("GOOGLE_API_KEY")
if not clave:
    sys.exit("Falta GOOGLE_API_KEY en .env")
lineas = [f"catálogo de Google, {datetime.now(timezone.utc).isoformat(timespec='seconds')}"]
token = ""
while True:
    q = {"pageSize": 200, "key": clave}
    if token:
        q["pageToken"] = token
    with urllib.request.urlopen("https://generativelanguage.googleapis.com/v1beta/models?" + urllib.parse.urlencode(q), timeout=60) as r:
        datos = json.load(r)
    for m in datos.get("models", []):
        lineas.append(f"{m.get('name', '')[7:]:45s} {str(m.get('outputTokenLimit', '')):>8s}  {m.get('displayName', '')}")
    token = datos.get("nextPageToken", "")
    if not token:
        break
salida = "\n".join(lineas) + "\n"
(RAIZ / "corridas" / "catalogo_google.txt").write_text(salida, encoding="utf-8")
print(salida)
