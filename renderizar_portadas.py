#!/usr/bin/env python3
"""renderizar_portadas.py — abre cada portada del sondeo `portada` (22/11/2026, idea de Maia: la portada de un sitio web
propio, sin encargo; ver config/consignas.yaml) en Chromium sin red y guarda lo que se ve y lo que se puede contar.

  .venv/bin/python renderizar_portadas.py                     # la última corrida de corridas/sondeos/portada/
  .venv/bin/python renderizar_portadas.py --carpeta corridas/sondeos/portada/20261123-0100 --rehacer

Por cada respuesta <idioma>/<casa>_p1[_rN].md: saca el archivo HTML de entre ```html y ``` (o el documento suelto si lo
devolvió sin cerco) y lo escribe al lado como <casa>_p1[_rN].html; abre el archivo con toda la red bloqueada (cada pedido a
otra dirección se cuenta: `externos_bloqueados`, la casa que no cumplió "sin recursos externos"); captura la ventana de
escritorio (1280x800, lo que se ve al llegar, `_escritorio.jpg`), la página entera si no pasa de 6000 px (`_entera.jpg`) y
la ventana de teléfono (390x844, `_telefono.jpg`); si la página se mueve (animaciones CSS activas o `requestAnimationFrame`,
`setInterval`, `setTimeout` en el código), captura además cuatro instantes a 0, 1, 2 y 3 segundos en una tira
(`_tira.jpg`; todo en JPEG desde el 23/11: en PNG las 246 pesaban 160 MB), porque una captura sola no muestra el movimiento (Maia, 22/11, 20:21). Guarda en render.json, por respuesta:
md5 del HTML, título, `lang`, texto visible (también en `_texto.txt`), alto del documento, color de fondo del cuerpo,
luminancia media de la captura de escritorio (0 a 255: el fondo oscuro o claro que Maia apostó), enlaces y cuántos apuntan
afuera, mailto, encabezados, nav, svg en línea, img, canvas, script, formularios, animaciones, errores de JavaScript,
recursos externos bloqueados. La línea "Qué:"/"What:" de la respuesta va aparte (`que`). Chromium: el de Playwright si
está, o el del sistema (CHROMIUM en el entorno, o /usr/bin/chromium-browser, como en el VPS)."""
import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
BASE = RAIZ / "corridas" / "sondeos" / "portada"
ESCRITORIO = (1280, 800)
TELEFONO = (390, 844)
MOVIMIENTO = re.compile(r"@keyframes|requestAnimationFrame|setInterval|setTimeout|animation\s*:|<animate", re.I)

JS_INFO = """() => {
  const q = s => document.querySelectorAll(s).length;
  const hrefs = [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href') || '');
  const anims = (document.getAnimations ? document.getAnimations() : []).filter(a => a.playState === 'running').length;
  return {
    titulo: document.title || '',
    lang: (document.documentElement.getAttribute('lang') || ''),
    texto: (document.body ? document.body.innerText : '') || '',
    alto: document.documentElement.scrollHeight,
    fondo: document.body ? getComputedStyle(document.body).backgroundColor : '',
    fondo_html: getComputedStyle(document.documentElement).backgroundColor,
    enlaces: hrefs.length,
    enlaces_externos: hrefs.filter(h => /^https?:/i.test(h)).length,
    mailto: hrefs.filter(h => /^mailto:/i.test(h)).length,
    h1: q('h1'), h2: q('h2'), h3: q('h3'), nav: q('nav'), svg: q('svg'), img: q('img'), canvas: q('canvas'),
    script: q('script'), formularios: q('form'), botones: q('button'), inputs: q('input, textarea'),
    animaciones_activas: anims,
  };
}"""


def chromium():
    for c in (os.environ.get("CHROMIUM"), "/usr/bin/chromium-browser", "/usr/bin/chromium"):
        if c and Path(c).exists():
            return c
    return None


def extraer_html(texto):
    """El archivo HTML de la respuesta: lo que va entre ```html y ``` (el primer cerco que tenga un documento), o el
    documento suelto desde <!doctype o <html hasta </html>; None si no hay."""
    cercos = re.findall(r"```[ \t]*(?:html|HTML)?[ \t]*\r?\n(.*?)```", texto, flags=re.S)
    for c in cercos:
        if re.search(r"<!doctype\s+html|<html|<body|<head|<style", c, flags=re.I):
            return c.strip()
    m = re.search(r"(<!doctype\s+html.*?</html>|<html.*?</html>)", texto, flags=re.S | re.I)
    if m:
        return m.group(1).strip()
    return None


def extraer_que(texto):
    """La línea "Qué:" / "What:" (la última, fuera de los cercos de código)."""
    sin_codigo = re.sub(r"```.*?```", "", texto, flags=re.S)
    lineas = [l.strip() for l in sin_codigo.split("\n") if l.strip()]
    for l in reversed(lineas):
        m = re.match(r"^[\W_]*(?:qu[ée]|what)\s*[:：]\s*(.+)$", l, flags=re.I)
        if m:
            return re.sub(r"\*+", "", m.group(1)).strip()
    return ""


def luminancia(png):
    try:
        from PIL import Image, ImageStat
    except ImportError:  # 23/11/2026: el venv del VPS no tenía Pillow y el render de pl142 se cayó en la primera tira
        return None
    with Image.open(png) as im:
        return round(ImageStat.Stat(im.convert("L")).mean[0], 1)


def tira(cuadros, salida):
    try:
        from PIL import Image
    except ImportError:
        return False
    ims = [Image.open(c).convert("RGB") for c in cuadros]
    w = sum(i.width for i in ims) + 10 * (len(ims) - 1)
    h = max(i.height for i in ims)
    lienzo = Image.new("RGB", (w, h), (255, 255, 255))
    x = 0
    for i in ims:
        lienzo.paste(i, (x, 0))
        x += i.width + 10
    lienzo = lienzo.resize((w // 2, h // 2))
    lienzo.save(salida, quality=85, optimize=True)
    for i in ims:
        i.close()
    return True


def respuestas(carpeta):
    for idioma in sorted(p.name for p in carpeta.iterdir() if p.is_dir()):
        for md in sorted((carpeta / idioma).glob("*_p1*.md")):
            if "_" in md.stem and re.match(r".+_p1(_r\d+)?$", md.stem):
                yield idioma, md


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--carpeta", default="", help="corridas/sondeos/portada/<fecha>; por defecto la última")
    ap.add_argument("--rehacer", action="store_true", help="también las que ya están en render.json")
    ap.add_argument("--solo", nargs="*", default=[], help="solo estas casas")
    args = ap.parse_args()
    carpeta = Path(args.carpeta) if args.carpeta else sorted(BASE.glob("2*"))[-1]
    if not carpeta.is_absolute() and not carpeta.exists():
        carpeta = BASE / carpeta
    registro_path = carpeta / "render.json"
    registro = json.loads(registro_path.read_text(encoding="utf-8")) if registro_path.exists() else {}
    from playwright.sync_api import sync_playwright
    exe = chromium()
    hechas = 0
    with sync_playwright() as p:
        navegador = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        for idioma, md in respuestas(carpeta):
            clave = f"{idioma}/{md.stem}"
            casa = re.sub(r"_p1(_r\d+)?$", "", md.stem)
            if args.solo and casa not in args.solo:
                continue
            if clave in registro and not args.rehacer:
                continue
            texto = md.read_text(encoding="utf-8")
            html = extraer_html(texto)
            fila = {"casa": casa, "idioma": idioma, "que": extraer_que(texto), "palabras_respuesta": len(texto.split()),
                    "hora": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            if not html:
                fila.update({"html": 0, "html_md5": "", "motivo": "sin documento HTML en la respuesta"})
                registro[clave] = fila
                print(f"  {clave:45s} sin HTML")
                continue
            ruta_html = md.with_suffix(".html")
            ruta_html.write_text(html, encoding="utf-8")
            fila.update({"html": 1, "html_md5": hashlib.md5(html.encode("utf-8")).hexdigest(), "bytes_html": len(html.encode("utf-8")),
                         "movimiento_en_codigo": int(bool(MOVIMIENTO.search(html)))})
            url = ruta_html.resolve().as_uri()
            bloqueados = []

            def enrutar(route):
                u = route.request.url
                if u.startswith("file://") or u.startswith("data:") or u.startswith("blob:") or u.startswith("about:"):
                    route.continue_()
                else:
                    bloqueados.append(u)
                    route.abort()

            errores = []
            contexto = navegador.new_context(viewport={"width": ESCRITORIO[0], "height": ESCRITORIO[1]}, device_scale_factor=1)
            contexto.route("**/*", enrutar)
            pagina = contexto.new_page()
            pagina.set_default_timeout(20000)
            pagina.on("pageerror", lambda e: errores.append(str(e)[:200]))
            try:
                pagina.goto(url, wait_until="load", timeout=30000)
            except Exception as e:  # noqa: BLE001
                errores.append(f"carga: {str(e)[:160]}")
            pagina.wait_for_timeout(500)
            try:
                info = pagina.evaluate(JS_INFO)
            except Exception as e:  # noqa: BLE001
                info = {"error_info": str(e)[:160]}
            base = md.with_suffix("")
            escritorio = Path(str(base) + "_escritorio.jpg")
            try:
                pagina.screenshot(path=str(escritorio), type="jpeg", quality=85)
            except Exception as e:  # noqa: BLE001
                errores.append(f"captura: {str(e)[:160]}")
            alto = info.get("alto") or 0
            if 0 < alto <= 6000:
                pagina.screenshot(path=str(base) + "_entera.jpg", full_page=True, type="jpeg", quality=70)
            se_mueve = bool(info.get("animaciones_activas")) or bool(fila["movimiento_en_codigo"])
            if se_mueve:
                cuadros = [escritorio]
                for i in (1, 2, 3):
                    pagina.wait_for_timeout(1000)
                    c = Path(str(base) + f"_cuadro{i}.jpg")
                    pagina.screenshot(path=str(c), type="jpeg", quality=85)
                    cuadros.append(c)
                if not tira(cuadros, Path(str(base) + "_tira.jpg")):
                    errores.append("tira: sin Pillow, quedan los cuadros sueltos")
                else:
                    for c in cuadros[1:]:
                        c.unlink()
            contexto.close()
            contexto2 = navegador.new_context(viewport={"width": TELEFONO[0], "height": TELEFONO[1]}, device_scale_factor=1, is_mobile=True)
            contexto2.route("**/*", enrutar)
            pagina2 = contexto2.new_page()
            pagina2.set_default_timeout(20000)
            try:
                pagina2.goto(url, wait_until="load", timeout=30000)
                pagina2.wait_for_timeout(500)
                pagina2.screenshot(path=str(base) + "_telefono.jpg", type="jpeg", quality=85)
            except Exception as e:  # noqa: BLE001
                errores.append(f"telefono: {str(e)[:160]}")
            contexto2.close()
            texto_visible = (info.get("texto") or "").strip()
            Path(str(base) + "_texto.txt").write_text(texto_visible, encoding="utf-8")
            fila.update({k: info.get(k) for k in ("titulo", "lang", "alto", "fondo", "fondo_html", "enlaces", "enlaces_externos", "mailto", "h1", "h2", "h3",
                                                   "nav", "svg", "img", "canvas", "script", "formularios", "botones", "inputs", "animaciones_activas")})
            fila.update({"palabras_visibles": len(texto_visible.split()), "luminancia": luminancia(escritorio) if escritorio.exists() else None, "se_mueve": int(se_mueve),
                         "externos_bloqueados": len(set(bloqueados)), "externos_lista": sorted(set(bloqueados))[:10], "errores_js": errores[:5],
                         "escala": 1, "chromium": exe or "playwright"})
            registro[clave] = fila
            hechas += 1
            print(f"  {clave:45s} {str(fila['luminancia']):>5s} lum  {'se mueve' if se_mueve else '        '}  {fila['externos_bloqueados']} ext  {fila['palabras_visibles']} palabras")
            registro_path.write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
        navegador.close()
    registro_path.write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{hechas} portadas renderizadas → {registro_path.relative_to(RAIZ) if registro_path.is_relative_to(RAIZ) else registro_path}")


if __name__ == "__main__":
    main()
