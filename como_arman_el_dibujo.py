#!/usr/bin/env python3
"""como_arman_el_dibujo.py — en qué orden arma cada casa su dibujo, paso a paso (8/10/2026). Maia, al ver
los dibujos: "lo que no está... es ver qué dibujan primero. O se puede video o ver simplemente cuál piensa /
arma primero y quién agrega cosas a último momento". Es la versión entera de tiras_construccion.py, que
muestra cuatro cuadros (25, 50, 75 y 100 %) de los dibujos "que no exista".

  .venv/bin/python como_arman_el_dibujo.py                            # las nueve consignas de la página
  .venv/bin/python como_arman_el_dibujo.py --consignas animal libre   # algunas (la página sale solo con esas)
  .venv/bin/python como_arman_el_dibujo.py --cuadros corridas/armado  # además guarda un PNG por paso

Consignas (8/10/2026): las cinco de la primera versión, más "cómo ves el mundo hoy" y "un animal que no
exista", donde también dibujaron GPT-3.5 Turbo y GPT-4 (0613) antes de su baja, y los dos mundos queridos.
Por casa y consigna va la primera corrida que terminó. Si la rep 1 se cortó por el techo de tokens y hay
una rep posterior completa, va esa, marcada en la página (repetidas con más techo, DISENO §2); si no
terminó ninguna, la rep 1 hasta donde llegó. En el detalle de cada dibujo va también lo que la casa dijo
que dibujó, con su SVG delante: la respuesta a "¿Qué dibujaste?" o el primer párrafo del segundo turno.

Un paso es un elemento que se ve (rect, circle, ellipse, line, polyline, polygon, path, text, use, image),
fuera de <defs> y de los contenedores que no se pintan solos, en el orden del código: en SVG lo que va
después se pinta encima. Cada dibujo se reconstruye en Chromium un paso por vez, en un lienzo de 200 px,
con las animaciones (SMIL y CSS) quietas en su primer instante y los SVG cortados tal como los muestra el
navegador. En cada paso se mide qué parte de la forma final ya está: bordes de Sobel (el máximo de los
tres canales) del cuadro y del dibujo terminado, y la suma del mínimo de los dos mapas sobre la suma del
mapa final. Un fondo liso o en degradé casi no tiene bordes, así que la curva sube cuando aparecen las
formas.
  mitad      fracción de los pasos en la que ya está la mitad de la forma final
  ochenta    lo mismo, para el 80 %
  ultimo_20  qué parte de la forma final aparece en el último 20 % de los pasos

Lee corridas/dibujos/<consigna>/<casa>_<rep>/ (dibujo.svg, meta.json, llamadas.jsonl) y los textos de
config/consignas.yaml. Escribe resultados/como_arman_el_dibujo.html (una sola página con los dibujos
adentro, que se abre en cualquier navegador; plantilla en plantillas/como_arman_el_dibujo.html) y
resultados/como_arman_el_dibujo.csv (los indicadores). Necesita playwright, numpy y Pillow; el Chromium es
el mismo que usa renderizar.py. Con otro Chromium u otras fuentes los números pueden moverse un poco en los
dibujos con texto."""

import argparse
import csv
import io
import json
import math
import re
import sys
from datetime import date
from pathlib import Path

import numpy as np
import yaml
from PIL import Image

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))
from renderizar import ejecutable  # noqa: E402

try:
    from debatir import NOMBRES  # noqa: E402  (el mapa de nombres para mostrar más completo)
except Exception:  # noqa: BLE001  sin las dependencias de las API quedan los identificadores
    NOMBRES = {}

DIBUJOS = RAIZ / "corridas" / "dibujos"
PLANTILLA = RAIZ / "plantillas" / "como_arman_el_dibujo.html"
SALIDA = RAIZ / "resultados" / "como_arman_el_dibujo.html"
CONSIGNAS = [("autorretrato", "Autorretrato"), ("libre", "Dibujo libre"), ("mundo", "El mundo hoy"),
             ("persona_imposible", "Persona imposible"), ("animal", "Animal"), ("animal_inexistente", "Animal que no exista"),
             ("animal_imposible", "Animal imposible"), ("mundo_querido", "Mundo querido"),
             ("yo_mundo_querido", "Yo en el mundo querido")]
CORTE = {"length", "max_tokens", "MAX_TOKENS"}  # motivo_fin de una respuesta cortada por el techo
PALABRAS_EXTRACTO = 120
PALABRAS_DICHO = 110

# Recorre el SVG en el orden del código y esconde cada elemento visible; después se muestran de a uno.
RECORRER = """({ fuente, lado }) => {
  const c = document.getElementById('__armado__');
  c.innerHTML = fuente;   // el parser de HTML tolera los SVG cortados, como el navegador
  const svg = c.querySelector('svg');
  window.__hojas = [];
  if (!svg) return { n: 0, comentarios: 0 };
  if (!svg.getAttribute('viewBox')) svg.setAttribute('viewBox', '0 0 400 400');
  svg.setAttribute('width', lado); svg.setAttribute('height', lado);
  svg.style.display = 'block';
  if (svg.pauseAnimations) { svg.pauseAnimations(); svg.setCurrentTime(0); }
  const SALTEAR = new Set(['defs', 'clippath', 'mask', 'pattern', 'symbol', 'marker', 'lineargradient',
    'radialgradient', 'filter', 'metadata', 'title', 'desc', 'style', 'script', 'foreignobject']);
  const HOJA = new Set(['rect', 'circle', 'ellipse', 'line', 'polyline', 'polygon', 'path', 'text', 'use', 'image']);
  const w = document.createTreeWalker(svg, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_COMMENT, {
    acceptNode(n) {
      if (n.nodeType === 1 && SALTEAR.has(n.localName.toLowerCase())) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }
  });
  const hojas = [];
  let comentarios = 0;
  while (w.nextNode()) {
    const n = w.currentNode;
    if (n.nodeType === 8) { comentarios++; continue; }
    const t = n.localName.toLowerCase();
    if (!HOJA.has(t)) continue;
    if (n.closest('text') && t !== 'text') continue;
    hojas.push(n);
  }
  hojas.forEach(h => { h.style.visibility = 'hidden'; });
  window.__hojas = hojas;
  return { n: hojas.length, comentarios };
}"""


def corridas(consigna):
    """Por casa, la primera corrida que terminó (o la primera, si se cortaron todas), en el orden de las carpetas."""
    por_casa = {}
    for d in sorted((DIBUJOS / consigna).glob("*_[0-9]*")):
        casa, _, rep = d.name.rpartition("_")
        if rep.isdigit() and (d / "dibujo.svg").exists() and (d / "meta.json").exists():
            por_casa.setdefault(casa, []).append((int(rep), d))
    elegidas = []
    for casa in sorted(por_casa, key=lambda c: c + "_"):
        reps = sorted(por_casa[casa])
        fin = {rep: json.loads((d / "meta.json").read_text(encoding="utf-8")).get("motivo_fin") for rep, d in reps}
        completas = [(rep, d) for rep, d in reps if fin[rep] not in CORTE]
        rep, d = completas[0] if completas else reps[0]
        elegidas.append({"casa": casa, "rep": rep, "carpeta": d, "cortado": fin[rep] in CORTE,
                         "primera": reps[0][1] if rep != reps[0][0] else None})
    return elegidas


def cuadros(pagina, fuente, lado):
    """Un PNG por paso: el lienzo sin elementos y después uno más cada vez."""
    # las animaciones CSS también quietas (las SMIL las frena RECORRER), para que cada cuadro sea siempre el mismo
    pagina.set_content(f"<!doctype html><html><head><style>#__armado__ * {{ animation-play-state: paused !important; }}"
                       f"</style></head><body style='margin:0;background:#fff'><div id='__armado__' "
                       f"style='width:{lado}px;height:{lado}px;overflow:hidden;background:#fff'></div></body></html>")
    info = pagina.evaluate(RECORRER, {"fuente": fuente, "lado": lado})
    caja = pagina.locator("#__armado__")  # un id que ningún SVG use (hay un clipPath "c")
    pngs = [caja.screenshot()]
    for k in range(info["n"]):
        pagina.evaluate("k => { window.__hojas[k].style.visibility = ''; }", k)
        pngs.append(caja.screenshot())
    return info, pngs


def bordes(png):
    a = np.asarray(Image.open(io.BytesIO(png)).convert("RGB"), dtype=np.float32) / 255.0
    p = np.pad(a, ((1, 1), (1, 1), (0, 0)), mode="edge")
    gx = (p[:-2, 2:] + 2 * p[1:-1, 2:] + p[2:, 2:]) - (p[:-2, :-2] + 2 * p[1:-1, :-2] + p[2:, :-2])
    gy = (p[2:, :-2] + 2 * p[2:, 1:-1] + p[2:, 2:]) - (p[:-2, :-2] + 2 * p[:-2, 1:-1] + p[:-2, 2:])
    return np.sqrt(gx ** 2 + gy ** 2).max(axis=2)


def curva(pngs):
    """Para cada paso, qué fracción de los bordes del dibujo terminado ya está."""
    final = bordes(pngs[-1])
    total = final.sum()
    return [float(np.minimum(bordes(p), final).sum() / total) if total > 0 else 0.0 for p in pngs]


def umbral(c, u):
    n = len(c) - 1
    return next((k / n for k, v in enumerate(c) if v >= u), 1.0)


def indicadores(c):
    if len(c) < 2:  # lienzo vacío, o cortado antes del primer trazo
        return {"mitad": None, "ochenta": None, "final20": None}
    n = len(c) - 1
    return {"mitad": round(umbral(c, 0.5), 3), "ochenta": round(umbral(c, 0.8), 3),
            "final20": round(1 - c[math.ceil(0.8 * n)], 3)}


def limpiar(svg):
    """Saca lo que no debe ejecutarse en la página (no hay nada de esto en los dibujos, pero por las dudas)."""
    svg = re.sub(r"<script[\s\S]*?(</script>|$)", "", svg, flags=re.I)
    return re.sub(r"\son[a-z]+\s*=\s*(\"[^\"]*\"|'[^']*')", "", svg, flags=re.I)


def prefijar(svg, pfx):
    """Prefija los id para que los degradados y filtros de un dibujo no pisen los de otro en la misma página."""
    ids = set(re.findall(r"\bid\s*=\s*[\"']([^\"']+)[\"']", svg))
    svg = re.sub(r"(\bid\s*=\s*)([\"'])([^\"']+)\2", lambda m: f"{m.group(1)}{m.group(2)}{pfx}{m.group(3)}{m.group(2)}", svg)
    svg = re.sub(r"url\(\s*([\"']?)#([^)\"'\s]+)\1\s*\)",
                 lambda m: f"url(#{pfx}{m.group(2)})" if m.group(2) in ids else m.group(0), svg)
    svg = re.sub(r"((?:xlink:)?href\s*=\s*)([\"'])#([^\"']+)\2",
                 lambda m: f"{m.group(1)}{m.group(2)}#{pfx}{m.group(3)}{m.group(2)}" if m.group(3) in ids else m.group(0), svg)

    def tiempos(m):
        valor = re.sub(r"(?<![\w.-])([A-Za-z_][\w-]*)\.(begin|end|click|repeat)",
                       lambda n: (pfx + n.group(1) if n.group(1) in ids else n.group(1)) + "." + n.group(2), m.group(3))
        return f"{m.group(1)}{m.group(2)}{valor}{m.group(2)}"
    return re.sub(r"(\b(?:begin|end)\s*=\s*)([\"'])([^\"']*)\2", tiempos, svg)


def llamada(carpeta):
    return json.loads((carpeta / "llamadas.jsonl").read_text(encoding="utf-8").splitlines()[0])


def razonamiento(r):
    """Lo que la API devolvió como razonamiento antes del código: cuántas palabras y un extracto."""
    palabras = (r.get("razonamiento") or "").split()
    extracto = " ".join(palabras[:PALABRAS_EXTRACTO]) + (" …" if len(palabras) > PALABRAS_EXTRACTO else "")
    return {"palabras": len(palabras), "extracto": extracto, "pedido": r.get("razonamiento_pedido"),
            "tokens_salida": r.get("tokens_salida"), "techo": r.get("max_tokens"), "fin": r.get("motivo_fin")}


def sin_markdown(texto):
    """Sin títulos (# …), negritas ni viñetas: algunas casas contestan con formato."""
    texto = "\n".join(linea for linea in texto.splitlines() if not re.match(r"\s*#{1,6}\s", linea))
    texto = re.sub(r"\*\*|__", "", texto)
    return re.sub(r"(?m)^[ \t]*(?:[-*•]|\d+[.)])[ \t]+", "", texto).strip()


def sin_rotulo(parrafo):
    """Saca el rótulo inicial que repite la pregunta ("¿Qué hice para que no exista?", "Qué dibujé:")."""
    resto = re.sub(r"^(?:¿[^?]{0,90}\?|(?:Qué|Lo que) dibujé( y por qué)?:)\s+", "", parrafo)
    return resto if len(resto.split()) >= 8 else parrafo


def dicho(carpeta, consigna):
    """Lo que dijo que dibujó, con su propio SVG delante: la respuesta a "¿Qué dibujaste?" (que_dibujaste.md) o,
    si no se le hizo esa pregunta o la API la cortó, el primer párrafo con contenido de la respuesta del segundo
    turno (por_que.md), salteando títulos, saludos y la pregunta repetida."""
    segundo = ("¿qué hiciste para que no pueda existir?" if consigna.endswith("_imposible") else
               "¿qué hiciste para que no exista?" if consigna.endswith("_inexistente") else "¿qué dibujaste y por qué?")
    for archivo, pregunta, entera in (("que_dibujaste.md", "¿Qué dibujaste?", True), ("por_que.md", segundo, False)):
        p = carpeta / archivo
        texto = sin_markdown(p.read_text(encoding="utf-8")) if p.exists() else ""
        parrafos = [sin_rotulo(" ".join(x.split())) for x in re.split(r"\n\s*\n", texto) if x.strip()]
        if not parrafos:
            continue
        elegido = " ".join(parrafos) if entera else next((x for x in parrafos if len(x.split()) >= 8), parrafos[0])
        palabras = elegido.split()
        return {"texto": " ".join(palabras[:PALABRAS_DICHO]) + (" …" if len(palabras) > PALABRAS_DICHO else ""),
                "pregunta": pregunta, "entera": entera}
    return None


def main():
    nombres_consignas = [c for c, _ in CONSIGNAS]
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--consignas", nargs="+", choices=nombres_consignas, default=nombres_consignas)
    ap.add_argument("--lado", type=int, default=200, help="lado del lienzo en el que se mide, en px (200)")
    ap.add_argument("--cuadros", type=Path, help="carpeta donde guardar un PNG por paso (si no, no se guardan)")
    ap.add_argument("--salida", type=Path, default=SALIDA, help="la página; el CSV va al lado, con el mismo nombre")
    args = ap.parse_args()
    textos = yaml.safe_load((RAIZ / "config" / "consignas.yaml").read_text(encoding="utf-8"))["dibujo"]["consignas"]
    from playwright.sync_api import sync_playwright

    datos, filas = {"consignas": []}, []
    with sync_playwright() as p:
        exe = ejecutable()
        navegador = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        pagina = navegador.new_page(viewport={"width": args.lado + 20, "height": args.lado + 20}, device_scale_factor=1)
        pagina.route("**/*", lambda ruta: ruta.abort() if ruta.request.url.startswith(("http:", "https:")) else ruta.continue_())
        for ci, (cid, titulo) in enumerate(CONSIGNAS):
            if cid not in args.consignas:
                continue
            modelos = []
            for mi, e in enumerate(corridas(cid)):
                fuente = (e["carpeta"] / "dibujo.svg").read_text(encoding="utf-8")
                info, pngs = cuadros(pagina, fuente, args.lado)
                if args.cuadros:
                    dir_ = args.cuadros / cid / e["carpeta"].name
                    dir_.mkdir(parents=True, exist_ok=True)
                    for k, png in enumerate(pngs):
                        (dir_ / f"{k:03d}.png").write_bytes(png)
                c = curva(pngs) if info["n"] else []
                ind = indicadores(c)
                r = llamada(e["carpeta"])
                primera = None
                if e["primera"]:
                    r1 = llamada(e["primera"])
                    primera = {"corrida": int(e["primera"].name.rpartition("_")[2]), "techo": r1.get("max_tokens"),
                               "tokens_salida": r1.get("tokens_salida")}
                m = {"id": e["casa"], "nombre": NOMBRES.get(e["casa"], e["casa"]), "corrida": e["rep"],
                     "cortado": e["cortado"], "primera": primera,
                     "svg": prefijar(limpiar(fuente), f"c{ci}m{mi}-"),
                     "n": info["n"], "curva": [round(v, 4) for v in c], "mitad": ind["mitad"], "final20": ind["final20"],
                     "comentarios": info["comentarios"], "razon": razonamiento(r), "dicho": dicho(e["carpeta"], cid)}
                modelos.append(m)
                filas.append({"consigna": cid, "casa": e["casa"], "nombre": m["nombre"], "corrida": e["rep"],
                              "pasos": info["n"], "mitad": ind["mitad"], "ochenta": ind["ochenta"],
                              "ultimo_20": ind["final20"], "rotulos": info["comentarios"],
                              "palabras_razonamiento": m["razon"]["palabras"], "cortado": "sí" if e["cortado"] else "no"})
                print(f"{cid:18s} {e['carpeta'].name:32s} pasos {info['n']:4d}  mitad "
                      f"{'—' if ind['mitad'] is None else format(ind['mitad'], '.2f'):>5s}  rótulos {info['comentarios']}")
            datos["consignas"].append({"id": cid, "titulo": titulo, "texto": " ".join(textos[cid].split()),
                                       "modelos": modelos})
        navegador.close()

    hoy = date.today()
    plantilla = PLANTILLA.read_text(encoding="utf-8").replace("__FECHA__", f"{hoy.day}/{hoy.month}/{hoy.year}")
    js = json.dumps(datos, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    args.salida.parent.mkdir(parents=True, exist_ok=True)
    args.salida.write_text(plantilla.replace("/*__DATOS__*/null", js), encoding="utf-8")
    with open(args.salida.with_suffix(".csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["consigna", "casa", "nombre", "corrida", "pasos", "mitad", "ochenta", "ultimo_20",
                                          "rotulos", "palabras_razonamiento", "cortado"])
        w.writeheader()
        w.writerows(filas)
    print(args.salida, f"{args.salida.stat().st_size / 1024:.0f} KB;", args.salida.with_suffix(".csv"), len(filas), "filas")


if __name__ == "__main__":
    main()
