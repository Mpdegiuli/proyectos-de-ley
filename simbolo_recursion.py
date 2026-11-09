#!/usr/bin/env python3
"""simbolo_recursion.py — la segunda parte del corazón (DISENO §2, 9/11/2026): el juego de comunicación del paper de
DeepMind ("A Heart Means Recursion") con las herramientas del repo. Cada casa dibujó, con `dibujar.py --consigna
simbolo_recursion`, un símbolo para decirle a otra instancia suya que use recursión (castellano e inglés, varias
repeticiones). Este script hace lo que sigue:

  --render        rinde cada SVG a PNG de 400x400 con Chromium (escala 1, como `config/imagenes/corazon_rojo.png`),
                  en la carpeta del dibujo (`dibujo.png` + `render.json` con el md5 del SVG)
  --interpretar   manda cada PNG a una instancia fresca de la misma casa, con el texto exacto de la condición de la
                  imagen del sondeo `corazon` ("Mirá esta imagen… Mirando la imagen, elegí una estrategia…"), varias
                  réplicas por símbolo, y guarda las respuestas como un sondeo más
                  (`corridas/sondeos/corazon_simbolo/<fecha>/<idioma>/<casa>_p<k>[_r<n>].md`, con p<k> = el símbolo de
                  la repetición k del dibujo; `resumen.json` como el de `sondear.py`, más `simbolos` con el md5 de cada
                  PNG). `codificar_corazon.py` lo lee como condiciones 9, 10, 11… contra la condición 1 de la corrida
                  principal.

  .venv/bin/python simbolo_recursion.py --render
  .venv/bin/python simbolo_recursion.py --interpretar --repeticiones 5 --modelos $M
  .venv/bin/python simbolo_recursion.py --interpretar --carpeta 20261109-1800 --modelos $M   # completar una corrida

Nada en el sistema salvo la línea de idioma del sondeo `corazon`; el símbolo nunca se explica a quien lo recibe."""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
sys.path.insert(0, str(RAIZ))
from dibujar import carpeta_dibujos  # noqa: E402
from isla.proveedores import Registro, cargar_modelos  # noqa: E402
from isla.util import leer_yaml  # noqa: E402
from renderizar import PLANTILLA, ejecutable  # noqa: E402

CONSIGNA = "simbolo_recursion"
IDIOMAS = ("es", "en")
MAX_TOKENS = 8000


def dibujos(idioma):
    """Las carpetas <casa>_<rep> de la consigna en ese idioma que tienen SVG hallado."""
    base = carpeta_dibujos(idioma) / CONSIGNA
    if not base.exists():
        return []
    out = []
    for d in sorted(base.glob("*_[0-9]*")):
        meta = d / "meta.json"
        if not (d / "dibujo.svg").exists() or not meta.exists():
            continue
        m = json.loads(meta.read_text(encoding="utf-8"))
        if not m.get("svg_hallado", True):
            continue  # SVG cortado por el techo o sin SVG: no hay símbolo que mandar
        casa, rep = d.name.rsplit("_", 1)
        out.append((casa, int(rep), d))
    return out


def render(rehacer=False):
    from playwright.sync_api import sync_playwright

    hechos = 0
    with sync_playwright() as p:
        exe = ejecutable()
        navegador = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        pagina = navegador.new_page(viewport={"width": 400, "height": 400}, device_scale_factor=1)
        pagina.route("**/*", lambda ruta: ruta.abort() if ruta.request.url.startswith(("http:", "https:")) else ruta.continue_())
        for idioma in IDIOMAS:
            for casa, rep, d in dibujos(idioma):
                svg = (d / "dibujo.svg").read_text(encoding="utf-8")
                huella = hashlib.md5(svg.encode("utf-8")).hexdigest()[:8]
                previo = d / "render.json"
                if not rehacer and (d / "dibujo.png").exists() and previo.exists() \
                        and json.loads(previo.read_text(encoding="utf-8")).get("svg_md5") == huella:
                    continue
                pagina.set_content(PLANTILLA.replace("{svg}", svg), wait_until="load")
                pagina.wait_for_timeout(100)
                pagina.screenshot(path=str(d / "dibujo.png"), full_page=False)
                previo.write_text(json.dumps({"svg_md5": huella, "escala": 1, "chromium": exe or "playwright", "version": navegador.version,
                                              "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}, ensure_ascii=False, indent=2),
                                  encoding="utf-8")
                hechos += 1
                print(f"  {idioma} {casa}_{rep} ({(d / 'dibujo.png').stat().st_size // 1024} kB)", flush=True)
        navegador.close()
    print(f"renderizados: {hechos}")


def interpretar(args):
    bloque = leer_yaml(RAIZ / "config" / "consignas.yaml")["sondeos"]["corazon"]
    modelos = cargar_modelos(RAIZ / "config" / "modelos.yaml")
    ids = list(args.modelos) + (leer_yaml(args.panel)["modelos"] if args.panel else [])
    ahora = datetime.now(timezone.utc)
    base = RAIZ / "corridas" / "sondeos" / "corazon_simbolo"
    if args.carpeta:
        base = base / args.carpeta
        resumen = json.loads((base / "resumen.json").read_text(encoding="utf-8"))
    else:
        base = base / ahora.strftime("%Y%m%d-%H%M")
        resumen = {"sondeo": "corazon_simbolo", "fecha_utc": ahora.isoformat(timespec="seconds"), "idiomas": {}}
    for idioma in IDIOMAS:
        if args.idioma and idioma not in args.idioma:
            continue
        sistema = bloque[idioma]["sistema"]
        # la condición 6 del sondeo `corazon`: {texto, imagen}; acá el texto es el mismo y la imagen es el símbolo propio
        texto = bloque[idioma]["preguntas"][5]["texto"]
        d = base / idioma
        d.mkdir(parents=True, exist_ok=True)
        registro = Registro(d / "llamadas.jsonl", modelos, f"sondeo_corazon_simbolo_{idioma}")
        res_i = resumen["idiomas"].setdefault(idioma, {"sistema": sistema, "preguntas": [], "respuestas": {}, "simbolos": {}})
        res_i["preguntas"] = [f"[símbolo propio {k}] " + texto for k in range(1, args.maximo + 1)]
        respuestas, simbolos = res_i["respuestas"], res_i.setdefault("simbolos", {})
        propios = {(casa, rep): carp for casa, rep, carp in dibujos(idioma)}
        for i in ids:
            for k in range(1, args.maximo + 1):
                carp = propios.get((i, k))
                if carp is None or not (carp / "dibujo.png").exists():
                    print(f"corazon_simbolo {idioma} p{k} {i}: sin símbolo rendido, salto", flush=True)
                    continue
                png = (carp / "dibujo.png").read_bytes()
                simbolos.setdefault(i, {})[str(k)] = {"dibujo": str(carp.relative_to(RAIZ)), "png_md5": hashlib.md5(png).hexdigest()[:8], "bytes": len(png)}
                for rep in range(1, args.repeticiones + 1):
                    clave = f"{i}_p{k}" + (f"_r{rep}" if rep > 1 else "")
                    archivo = d / f"{clave}.md"
                    previo = respuestas.get(clave, {})
                    if args.carpeta and archivo.exists() and archivo.stat().st_size > 0 and previo.get("motivo_fin") not in (None, "error"):
                        continue
                    print(f"corazon_simbolo {idioma} p{k}{f' r{rep}' if rep > 1 else ''} {i}", flush=True)
                    try:
                        r = registro.llamar(i, sistema, texto, temperatura=None, max_tokens=args.techo, tipo="sondeo_corazon_simbolo",
                                            ronda=k, parte=f"r{rep}" if rep > 1 else None, contexto={"imagenes": [png]})
                    except Exception as e:
                        print(f"  FALLÓ {i}: {str(e)[:200]}", flush=True)
                        respuestas[clave] = {"error": str(e)[:200]}
                        continue
                    archivo.write_text(r.texto, encoding="utf-8")
                    respuestas[clave] = {"modelo_respondido": r.modelo_respondido, "motivo_fin": r.motivo_fin,
                                         "palabras": len(r.texto.split()), "respuesta": " ".join(r.texto.split())[:240]}
                    print(f"  {' '.join(r.texto.split())[:160]}", flush=True)
        (base / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"listo: {base.relative_to(RAIZ)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--render", action="store_true")
    ap.add_argument("--rehacer", action="store_true", help="con --render, también los que ya tienen PNG")
    ap.add_argument("--interpretar", action="store_true")
    ap.add_argument("--modelos", nargs="*", default=[])
    ap.add_argument("--panel", default="")
    ap.add_argument("--idioma", nargs="*", default=[], help="por defecto, es y en")
    ap.add_argument("--repeticiones", type=int, default=5, help="réplicas por símbolo")
    ap.add_argument("--maximo", type=int, default=3, help="cuántas repeticiones del dibujo (símbolos) por casa se mandan")
    ap.add_argument("--carpeta", default="", help="completar una corrida existente de corazon_simbolo")
    ap.add_argument("--techo", type=int, default=MAX_TOKENS)
    args = ap.parse_args()
    if args.render:
        render(args.rehacer)
    if args.interpretar:
        interpretar(args)
    if not args.render and not args.interpretar:
        ap.error("--render y/o --interpretar")


if __name__ == "__main__":
    main()
