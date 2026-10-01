#!/usr/bin/env python3
"""renderizar.py — cada dibujo SVG a PNG con Chromium (el mismo motor con el que Maia los mira), para los
jueces con visión de "la distancia" (DISENO §2, diseño de Maia del 30/9/2026). Cada SVG va solo en su
propio documento, sin scripts ni referencias externas (se bloquea toda red), lienzo de 400x400 a escala 2
(800x800 px), captura a los 100 ms: las animaciones SMIL quedan en su primer instante.

  .venv/bin/python renderizar.py                      # todos los dibujos en castellano que no tengan PNG
  .venv/bin/python renderizar.py --consigna animal    # una consigna
  .venv/bin/python renderizar.py --rehacer            # también los que ya tienen PNG

Salida: corridas/distancia/<consigna>/<casa>_<rep>/dibujo.png (más md5 del SVG en render.json, para saber
de qué código salió). Chromium: el de Playwright si está, o el del sistema (CHROMIUM en el entorno, o
/usr/bin/chromium-browser, como en el VPS, AlmaLinux 9 + EPEL)."""
import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))
from dibujar import CONSIGNAS  # noqa: E402

PLANTILLA = ("<!doctype html><html><head><meta charset='utf-8'><style>html,body{margin:0;padding:0;background:#fff;"
             "width:400px;height:400px;overflow:hidden}svg{display:block;width:400px;height:400px}</style></head>"
             "<body>{svg}</body></html>")


def ejecutable():
    for c in (os.environ.get("CHROMIUM"), "/usr/bin/chromium-browser", "/usr/bin/chromium"):
        if c and Path(c).exists():
            return c
    return None  # el de Playwright


def unidades(consigna=None):
    base = RAIZ / "corridas" / "dibujos"
    for c in CONSIGNAS:
        if consigna and c != consigna:
            continue
        for d in sorted((base / c).glob("*_[0-9]*")) if (base / c).exists() else []:
            if (d / "dibujo.svg").exists() and (d / "meta.json").exists():
                yield c, d


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--consigna", choices=CONSIGNAS)
    ap.add_argument("--rehacer", action="store_true")
    ap.add_argument("--escala", type=int, default=2)
    args = ap.parse_args()
    from playwright.sync_api import sync_playwright

    hechos = saltados = 0
    with sync_playwright() as p:
        exe = ejecutable()
        navegador = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        pagina = navegador.new_page(viewport={"width": 400, "height": 400}, device_scale_factor=args.escala)
        pagina.route("**/*", lambda ruta: ruta.abort() if ruta.request.url.startswith(("http:", "https:")) else ruta.continue_())
        for consigna, d in unidades(args.consigna):
            meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
            if not meta.get("svg_hallado", True) and meta.get("motivo_fin") == "length":
                saltados += 1
                continue  # SVG cortado por el techo: no hay dibujo
            salida = RAIZ / "corridas" / "distancia" / consigna / d.name
            svg = (d / "dibujo.svg").read_text(encoding="utf-8")
            huella = hashlib.md5(svg.encode("utf-8")).hexdigest()[:8]
            previo = salida / "render.json"
            if not args.rehacer and (salida / "dibujo.png").exists() and previo.exists() \
                    and json.loads(previo.read_text(encoding="utf-8")).get("svg_md5") == huella:
                continue
            salida.mkdir(parents=True, exist_ok=True)
            pagina.set_content(PLANTILLA.replace("{svg}", svg), wait_until="load")
            pagina.wait_for_timeout(100)
            pagina.screenshot(path=str(salida / "dibujo.png"), full_page=False)
            previo.write_text(json.dumps({"svg_md5": huella, "escala": args.escala, "chromium": exe or "playwright",
                                          "version": navegador.version, "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")},
                                         ensure_ascii=False, indent=2), encoding="utf-8")
            hechos += 1
            print(f"  {consigna}/{d.name} ({(salida / 'dibujo.png').stat().st_size // 1024} kB)", flush=True)
        navegador.close()
    print(f"renderizados: {hechos}; sin dibujo (SVG cortado): {saltados}")


if __name__ == "__main__":
    main()
