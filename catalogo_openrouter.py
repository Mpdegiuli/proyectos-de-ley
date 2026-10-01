#!/usr/bin/env python3
"""catalogo_openrouter.py — qué modelos lista OpenRouter y, sobre todo, cuáles aceptan imagen de entrada
(1/10/2026, para elegir los jueces con visión de "la distancia": Maia pidió un juez chino que no sea Qwen,
y desde el sandbox no se llega a OpenRouter). Primero las casas nuestras que van por OpenRouter
(config/modelos.yaml), con sus modalidades de entrada; después el catálogo entero: id, modalidades,
contexto y precios por millón. No llama a ningún modelo. Escribe en corridas/catalogo_openrouter.txt y
en pantalla. La clave sale de .env (OPENROUTER_API_KEY) si está; el listado es público y no la imprime."""
import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from isla.util import leer_yaml

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
cab = {"User-Agent": "proyectos-de-ley/catalogo"}
clave = os.environ.get("OPENROUTER_API_KEY")
if clave:
    cab["Authorization"] = f"Bearer {clave}"
with urllib.request.urlopen(urllib.request.Request("https://openrouter.ai/api/v1/models", headers=cab), timeout=60) as r:
    datos = json.load(r)["data"]
por_id = {m["id"]: m for m in datos}


def precio(m, campo):
    try:
        return f"{float(m['pricing'][campo]) * 1e6:.2f}"
    except (KeyError, TypeError, ValueError):
        return "?"


def fila(m):
    mods = "+".join(m.get("architecture", {}).get("input_modalities") or ["?"])
    return f"{m['id']:50s} {mods:22s} {str(m.get('context_length', '')):>9s}  {precio(m, 'prompt'):>7s} {precio(m, 'completion'):>7s}"


lineas = [f"catálogo de OpenRouter, {datetime.now(timezone.utc).isoformat(timespec='seconds')}: {len(datos)} modelos",
          "", "Las casas nuestras que van por OpenRouter (config/modelos.yaml): id, entradas que acepta, contexto, $/M entrada, $/M salida"]
nuestras = leer_yaml(RAIZ / "config" / "modelos.yaml")["modelos"]
vistos = set()
for nombre, cfg in nuestras.items():
    if "openrouter.ai" not in str(cfg.get("base_url", "")) or cfg.get("modelo") in vistos:
        continue
    vistos.add(cfg["modelo"])
    m = por_id.get(cfg["modelo"])
    lineas.append(("  " + fila(m)) if m else f"  {cfg['modelo']:50s} NO ESTÁ en el catálogo")
lineas += ["", "Todos los que aceptan imagen:"]
lineas += ["  " + fila(m) for m in sorted(datos, key=lambda m: m["id"]) if "image" in (m.get("architecture", {}).get("input_modalities") or [])]
lineas += ["", "Catálogo entero:"]
lineas += ["  " + fila(m) for m in sorted(datos, key=lambda m: m["id"])]
salida = "\n".join(lineas) + "\n"
(RAIZ / "corridas" / "catalogo_openrouter.txt").write_text(salida, encoding="utf-8")
print("\n".join(lineas[: lineas.index("Catálogo entero:")]))
