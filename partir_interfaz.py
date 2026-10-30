#!/usr/bin/env python3
"""partir_interfaz.py — parte `corridas/interfaz/<casa>/respuestas.md` (lo que Maia copió de la
interfaz de claude.ai, un `## nombre` por chat) en un archivo por chat: `nombre.svg` con el SVG
solo (de `<svg` a `</svg>`; el texto que lo rodee, si hay, va a `nombre_texto.md`), `nombre.md`
con el texto tal cual, `notas.md` con la sección `notas`, e `indice.json` con caracteres, palabras
y si el SVG se encontró. No llama a ningún modelo ni toca `respuestas.md` (30/10/2026, DISENO §2,
"Claude Opus 3 en la interfaz de claude.ai, en incógnito"). Uso: partir_interfaz.py claude-3-opus"""
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
casa = sys.argv[1] if len(sys.argv) > 1 else "claude-3-opus"
carpeta = RAIZ / "corridas" / "interfaz" / casa
origen = carpeta / "respuestas.md"
if not origen.exists():
    sys.exit(f"No está {origen}")
texto = origen.read_text(encoding="utf-8").replace("\r\n", "\n")
partes = re.split(r"^## +(\S+)\s*$", texto, flags=re.M)
if len(partes) < 3:
    sys.exit("No encontré encabezados `## nombre`")
indice = {}
for nombre, cuerpo in zip(partes[1::2], partes[2::2]):
    nombre = nombre.strip().lower()
    nombre = unicodedata.normalize("NFKD", nombre).encode("ascii", "ignore").decode()  # `identificación` → identificacion
    cuerpo = cuerpo.strip("\n")
    cuerpo = re.sub(r"^```[a-z]*\n|\n```$", "", cuerpo).strip("\n")  # cercas de código, si las copió
    entrada = {"caracteres": len(cuerpo), "palabras": len(cuerpo.split())}
    m = re.search(r"<svg\b.*?</svg>", cuerpo, flags=re.S | re.I)
    if m:
        (carpeta / f"{nombre}.svg").write_text(m.group(0) + "\n", encoding="utf-8")
        entrada["svg"] = True
        entrada["caracteres_svg"] = len(m.group(0))
        resto = (cuerpo[:m.start()] + cuerpo[m.end():]).strip()
        if resto:
            (carpeta / f"{nombre}_texto.md").write_text(resto + "\n", encoding="utf-8")
            entrada["texto_alrededor"] = len(resto)
    else:
        (carpeta / f"{nombre}.md").write_text(cuerpo + "\n", encoding="utf-8")
        entrada["svg"] = False
    if nombre in indice:
        print(f"OJO: `{nombre}` aparece más de una vez; queda la última")
    indice[nombre] = entrada
(carpeta / "indice.json").write_text(json.dumps(indice, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for nombre, e in indice.items():
    print(f"{nombre:28s} {'svg' if e['svg'] else 'md ':3s} {e['caracteres']:6d} caracteres {e['palabras']:5d} palabras"
          + (f"  (texto alrededor: {e['texto_alrededor']})" if e.get("texto_alrededor") else ""))
print(f"{len(indice)} secciones → {carpeta}")
