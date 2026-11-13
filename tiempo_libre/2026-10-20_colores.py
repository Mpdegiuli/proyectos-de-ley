#!/usr/bin/env python3
"""De qué color es la letra que dibujó cada casa.

Lee el código de los SVG de `corridas/dibujos/letra` (consigna "Dibujá una
letra.", 9 y 10/10/2026; la última corrida válida de cada casa) sin renderizar
nada, y estima para cada dibujo:

  * el fondo: el primer rect o path relleno que cubre casi todo el lienzo
    (blanco si no hay ninguno);
  * el color con más tinta, que casi siempre es el de la letra: para cada
    elemento que dibuja, el área de su polígono (fórmula del cordón, con los
    extremos de las curvas como vértices) por su relleno, y el largo de su
    contorno por el grosor del trazo por su trazo. Un degradado cuenta como una
    sola pintura (sus stops, juntos). Los <use> se resuelven al elemento que
    citan. Si la misma geometría se dibuja varias veces (sombra, borde, brillo),
    lo de abajo cuenta solo por lo que asoma. Las transformaciones (scale,
    rotate) no se aplican, y el filtro que pide tinta no distingue la letra de
    un adorno grande ni descuenta una forma distinta dibujada encima, así que
    imprime las tres pinturas siguientes y los paneles excluidos para que se
    pueda juzgar leyendo.

Después clasifica cada color en una familia por tono, saturación y
luminosidad: negro, blanco, crema, gris, rojo, oro (naranjas y amarillos),
verde, cian, azul, violeta, rosa.

Uso: python3 2026-10-20_colores.py RUTA_DEL_CLON [--csv]
No llama a ningún modelo, no gasta, no abre imágenes.
"""
import colorsys
import csv
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

try:
    from matplotlib.colors import CSS4_COLORS
except ImportError:  # paleta mínima si no hay matplotlib
    CSS4_COLORS = {
        "black": "#000000", "white": "#ffffff", "red": "#ff0000", "blue": "#0000ff",
        "green": "#008000", "yellow": "#ffff00", "gold": "#ffd700", "navy": "#000080",
        "gray": "#808080", "grey": "#808080", "orange": "#ffa500", "purple": "#800080",
        "coral": "#ff7f50", "crimson": "#dc143c", "teal": "#008080", "silver": "#c0c0c0",
    }

NS = "{http://www.w3.org/2000/svg}"
XLINK = "{http://www.w3.org/1999/xlink}href"
DIBUJAN = {"path", "polygon", "polyline", "line", "circle", "ellipse", "rect", "text", "tspan"}
NO_ENTRAR = {"defs", "style", "title", "desc", "metadata", "clipPath", "mask", "filter",
             "linearGradient", "radialGradient", "pattern", "symbol", "marker"}
NUM = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")
LIENZO = [400.0, 400.0]  # ancho y alto del lienzo actual, para los porcentajes


def tag(el):
    return el.tag.replace(NS, "") if isinstance(el.tag, str) else ""


def parse_color(s):
    """Devuelve (r, g, b) en 0..1 o None (none/transparent/desconocido)."""
    if s is None:
        return None
    s = s.strip().lower()
    if s in ("", "none", "transparent", "currentcolor", "inherit"):
        return None
    if s.startswith("#"):
        h = s[1:]
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h[:3])
        if len(h) in (6, 8):
            try:
                return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
            except ValueError:
                return None
        return None
    m = re.match(r"rgba?\(([^)]*)\)", s)
    if m:
        parts = [p.strip() for p in m.group(1).replace("/", ",").split(",")]
        try:
            vals = []
            for p in parts[:3]:
                vals.append(float(p[:-1]) / 100 if p.endswith("%") else float(p) / 255)
            return tuple(vals)
        except ValueError:
            return None
    m = re.match(r"hsla?\(([^)]*)\)", s)
    if m:
        parts = [p.strip() for p in m.group(1).replace("/", ",").split(",")]
        try:
            h = float(re.sub(r"[a-z]+$", "", parts[0])) / 360
            sat = float(parts[1].rstrip("%")) / 100
            lig = float(parts[2].rstrip("%")) / 100
            return colorsys.hls_to_rgb(h, lig, sat)
        except (ValueError, IndexError):
            return None
    if s in CSS4_COLORS:
        return parse_color(CSS4_COLORS[s])
    return None


def hexa(rgb):
    return "#%02x%02x%02x" % tuple(int(round(c * 255)) for c in rgb)


def familia(rgb):
    h, l, s = colorsys.rgb_to_hls(*rgb)
    g = h * 360
    if l < 0.18:
        return "negro"
    if l > 0.93 and s < 0.35:
        return "blanco"
    if l > 0.85 and 20 <= g < 70:
        return "crema"
    if s < 0.12:
        return "gris"
    if g < 15 or g >= 345:
        return "rojo"
    if g < 70:
        return "oro"
    if g < 170:
        return "verde"
    if g < 200:
        return "cian"
    if g < 260:
        return "azul"
    if g < 300:
        return "violeta"
    return "rosa"


def style_dict(el):
    d = {}
    st = el.get("style")
    if st:
        for part in st.split(";"):
            if ":" in part:
                k, v = part.split(":", 1)
                d[k.strip()] = v.strip()
    return d


def attr(el, name, parents):
    """Atributo con herencia desde los padres (y los <use>) y desde style=."""
    for e in [el] + parents[::-1]:
        v = style_dict(e).get(name) or e.get(name)
        if v is not None:
            return v
    return None


def numero(s, d=0.0):
    m = NUM.search(s or "")
    return float(m.group(0)) if m else d


def gradient_colors(root):
    """id -> (rgb promedio, opacidad promedio, stops en hexa) de cada degradado."""
    raw = {}
    for g in root.iter():
        if tag(g) in ("linearGradient", "radialGradient"):
            stops = []
            for st in g:
                if tag(st) == "stop":
                    c = style_dict(st).get("stop-color") or st.get("stop-color")
                    rgb = parse_color(c)
                    op = style_dict(st).get("stop-opacity") or st.get("stop-opacity") or "1"
                    try:
                        op = float(op)
                    except ValueError:
                        op = 1.0
                    if rgb is not None:
                        stops.append((rgb, op))
            raw[g.get("id")] = (stops, g.get(XLINK) or g.get("href"))
    grads = {}
    for gid, (stops, href) in raw.items():
        if not stops and href and href.startswith("#") and href[1:] in raw:
            stops = raw[href[1:]][0]
        if not stops:
            continue
        n = len(stops)
        rgb = tuple(sum(s[0][i] for s in stops) / n for i in range(3))
        op = sum(s[1] for s in stops) / n
        grads[gid] = (rgb, op, [hexa(st[0]) for st in stops if st[1] > 0.05])
    return grads


def resolve(paint, grads):
    """Devuelve {clave, rgb, op, stops} para un valor de fill/stroke, o None.
    Un degradado es una sola pintura (clave "a→b") con el promedio como rgb."""
    if paint is None:
        return None
    p = paint.strip()
    m = re.match(r"url\(#([^)]+)\)", p)
    if m:
        g = grads.get(m.group(1))
        if g is None:  # pattern u otro: sin color
            return None
        rgb, op, stops = g
        if op <= 0.05:
            return None
        distintos = []
        for st in stops:
            if st not in distintos:
                distintos.append(st)
        clave = "→".join(distintos) if len(distintos) > 1 else distintos[0]
        return {"clave": clave, "rgb": rgb, "op": op, "stops": distintos}
    rgb = parse_color(p)
    return {"clave": hexa(rgb), "rgb": rgb, "op": 1.0, "stops": [hexa(rgb)]} if rgb is not None else None


def familia_pintura(clave):
    """Familia de un color o de un degradado (las familias de sus stops, sin repetir)."""
    fams = []
    for h in clave.split("→"):
        f = familia(parse_color(h))
        if f not in fams:
            fams.append(f)
    return "→".join(fams)


def path_geometry(d):
    """(área, perímetro) de un path: vértices = extremos de cada comando."""
    area = per = 0.0
    sub = []
    cx = cy = sx = sy = 0.0

    def cerrar():
        nonlocal area
        if len(sub) >= 3:
            a = 0.0
            for i in range(len(sub)):
                x1, y1 = sub[i]
                x2, y2 = sub[(i + 1) % len(sub)]
                a += x1 * y2 - x2 * y1
            area += abs(a) / 2

    def mover(x, y):
        nonlocal cx, cy, per
        if sub:
            per += math.hypot(x - cx, y - cy)
        sub.append((x, y))
        cx, cy = x, y

    for cmd, args in re.findall(r"([MmLlHhVvCcSsQqTtAaZz])([^MmLlHhVvCcSsQqTtAaZz]*)", d):
        nums = [float(n) for n in NUM.findall(args)]
        if cmd in "Zz":
            if sub:
                per += math.hypot(sx - cx, sy - cy)
            cerrar()
            sub = []
            cx, cy = sx, sy
            continue
        if cmd in "Mm":
            cerrar()
            sub = []
            for i in range(0, len(nums) - 1, 2):
                x, y = nums[i], nums[i + 1]
                if cmd == "m":
                    x, y = cx + x, cy + y
                if i == 0:
                    sub.append((x, y)); cx, cy = x, y; sx, sy = x, y
                else:
                    mover(x, y)
            continue
        if cmd in "Hh":
            for n in nums:
                mover(n if cmd == "H" else cx + n, cy)
            continue
        if cmd in "Vv":
            for n in nums:
                mover(cx, n if cmd == "V" else cy + n)
            continue
        paso = {"L": 2, "T": 2, "Q": 4, "S": 4, "C": 6, "A": 7}[cmd.upper()]
        for i in range(0, len(nums) - paso + 1, paso):
            x, y = nums[i + paso - 2], nums[i + paso - 1]
            if cmd.islower():
                x, y = cx + x, cy + y
            mover(x, y)
    cerrar()
    return area, per


def geometria(el, parents):
    """(área rellenable, perímetro) de un elemento."""
    t = tag(el)
    f = lambda k, d=0.0: numero(el.get(k), d)
    if t == "rect":
        w, h = f("width"), f("height")
        if (el.get("width") or "").strip().endswith("%"):
            w = w / 100 * LIENZO[0]
        if (el.get("height") or "").strip().endswith("%"):
            h = h / 100 * LIENZO[1]
        return w * h, 2 * (w + h)
    if t == "circle":
        r = f("r")
        return math.pi * r * r, 2 * math.pi * r
    if t == "ellipse":
        a, b = f("rx"), f("ry")
        return math.pi * a * b, math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))
    if t == "line":
        return 0.0, math.hypot(f("x2") - f("x1"), f("y2") - f("y1"))
    if t in ("polygon", "polyline"):
        nums = [float(n) for n in NUM.findall(el.get("points", ""))]
        pts = list(zip(nums[0::2], nums[1::2]))
        if len(pts) < 2:
            return 0.0, 0.0
        per = sum(math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(len(pts) - 1))
        if t == "polyline":
            return 0.0, per
        a = sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1] for i in range(len(pts)))
        return abs(a) / 2, per + math.hypot(pts[0][0] - pts[-1][0], pts[0][1] - pts[-1][1])
    if t == "path":
        return path_geometry(el.get("d", ""))
    if t in ("text", "tspan"):
        fs = numero(attr(el, "font-size", parents), 16.0)
        n = len("".join(el.itertext()).strip()) or 1
        return 0.6 * fs * n * fs * 0.5, 0.0  # un texto cuenta como relleno
    return 0.0, 0.0


def analizar(svg_path):
    txt = svg_path.read_text(encoding="utf-8", errors="replace")
    try:
        root = ET.fromstring(txt)
    except ET.ParseError:
        return None
    vb = root.get("viewBox")
    if vb:
        nums = [float(n) for n in NUM.findall(vb)]
        W, H = nums[2], nums[3]
    else:
        W, H = numero(root.get("width"), 400), numero(root.get("height"), 400)
    lienzo = W * H
    LIENZO[0], LIENZO[1] = W, H
    grads = gradient_colors(root)
    por_id = {e.get("id"): e for e in root.iter() if e.get("id")}

    fondo = [None]
    orden = [0]
    capas = []
    tinta = defaultdict(float)
    paleta = set()
    fondos_y_paneles = []

    def pintar(el, parents, dentro_de_use):
        t = tag(el)
        fill = attr(el, "fill", parents)
        stroke = attr(el, "stroke", parents)
        op = attr(el, "opacity", parents)
        op = float(op) if op and NUM.fullmatch(op.strip()) else 1.0
        fop = attr(el, "fill-opacity", parents)
        fop = float(fop) if fop and NUM.fullmatch(fop.strip()) else 1.0
        sop = attr(el, "stroke-opacity", parents)
        sop = float(sop) if sop and NUM.fullmatch(sop.strip()) else 1.0
        if fill is None and t not in ("line", "polyline"):
            fill = "#000000"  # valor por defecto del SVG: negro
        area, per = geometria(el, parents)
        rf = resolve(fill, grads)
        rs = resolve(stroke, grads)
        orden[0] += 1
        eps = orden[0] * 1e-3  # desempate: lo que se dibuja después queda encima
        # fondo: algo relleno que cubre casi todo el lienzo
        if rf and area >= 0.85 * lienzo and not dentro_de_use:
            fondos_y_paneles.append((rf["clave"], round(area / lienzo, 2), "fondo"))
            if fondo[0] is None:
                fondo[0] = rf["rgb"]
            return
        # panel, tarjeta, halo o marco: un rect, círculo o elipse grande, o un
        # path enorme. Una letra no es eso. Se anota y no cuenta como tinta.
        grande = (t in ("rect", "circle", "ellipse") and area >= 0.25 * lienzo) or area >= 0.6 * lienzo
        if grande:
            fondos_y_paneles.append(((rf or rs or {}).get("clave"), round(area / lienzo, 2), "panel"))
            return
        # geometría idéntica dibujada varias veces (sombra, borde, brillo):
        # lo de abajo queda tapado por lo de arriba; se resuelve al final
        forma = (t, el.get("d") or el.get("points") or (el.get("cx"), el.get("cy"), el.get("r"), el.get("x"), el.get("y"), el.get("width"), el.get("height")),
                 tuple(e.get("transform") for e in parents + [el] if e.get("transform")))
        if rf and op * fop * rf["op"] > 0.05:
            capas.append({"forma": forma, "tipo": "fill", "clave": rf["clave"], "peso": area * op * fop * rf["op"], "op": op * fop * rf["op"], "sw": 0.0, "eps": eps})
            paleta.update(rf["stops"])
        if rs and op * sop * rs["op"] > 0.05:
            sw = numero(attr(el, "stroke-width", parents), 1.0)
            capas.append({"forma": forma, "tipo": "stroke", "clave": rs["clave"], "peso": per * op * sop * rs["op"], "op": op * sop * rs["op"], "sw": sw, "per": per, "eps": eps})
            paleta.update(rs["stops"])

    def walk(el, parents, dentro_de_use=False, prof=0):
        t = tag(el)
        if t in NO_ENTRAR or prof > 12:
            return
        if t == "use":
            href = el.get(XLINK) or el.get("href") or ""
            ref = por_id.get(href[1:]) if href.startswith("#") else None
            if ref is not None:
                # los atributos del <use> se heredan al elemento citado
                walk(ref, parents + [el], True, prof + 1)
            return
        if t in DIBUJAN:
            pintar(el, parents, dentro_de_use)
        for ch in el:
            walk(ch, parents + [el], dentro_de_use, prof + 1)

    for ch in root:
        walk(ch, [root])
    # resolver las capas apiladas sobre la misma geometría
    grupos = defaultdict(list)
    for i, c in enumerate(capas):
        grupos[c["forma"]].append((i, c))
    for forma, lista in grupos.items():
        for k, (i, c) in enumerate(lista):
            despues = [c2 for _, c2 in lista[k + 1:]]
            if c["tipo"] == "fill":
                visible = 1.0
                for c2 in despues:  # un relleno posterior igual lo tapa según su opacidad
                    if c2["tipo"] == "fill":
                        visible *= 1.0 - min(1.0, c2["op"])
                if visible > 0.05:
                    tinta[c["clave"]] += c["peso"] * visible + c["eps"]
            else:
                menores = [c2["sw"] for c2 in despues if c2["tipo"] == "stroke" and c2["sw"] <= c["sw"] and c2["op"] >= 0.5]
                visible = c["sw"] - (max(menores) if menores else 0.0)
                if visible > 0:
                    tinta[c["clave"]] += c["peso"] * visible + c["eps"]
    fondo_rgb = fondo[0] if fondo[0] is not None else (1.0, 1.0, 1.0)  # sin fondo: lienzo transparente, se cuenta blanco
    top = sorted(tinta.items(), key=lambda kv: -kv[1])
    return {
        "fondo": hexa(fondo_rgb),
        "sin_fondo": fondo[0] is None,
        "fondo_familia": familia(fondo_rgb),
        "fondo_L": round(colorsys.rgb_to_hls(*fondo_rgb)[1], 2),
        "paneles": fondos_y_paneles,
        "top": [(h, round(v)) for h, v in top[:4]],
        "paleta": sorted(paleta),
    }


def fabricante(casa):
    if casa.startswith("claude"):
        return "Anthropic"
    if casa.startswith("gpt"):
        return "OpenAI"
    if casa.startswith("gemini"):
        return "Google"
    if casa.startswith("grok"):
        return "xAI"
    if casa.startswith("mistral"):
        return "Mistral"
    return "China"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    repo = Path(sys.argv[1])
    letras = {}
    csv_path = repo / "resultados" / "dibujos_letras_codificacion_20261010.csv"
    if csv_path.exists():
        with csv_path.open(encoding="utf-8") as f:
            for row in csv.DictReader(f):
                letras[row["casa"]] = row["letra"]
    carpeta = repo / "corridas" / "dibujos" / "letra"
    ultimas = {}
    for d in sorted(carpeta.iterdir(), key=lambda p: (re.sub(r"_\d+$", "", p.name), int(p.name.rsplit("_", 1)[-1]))):
        svg = d / "dibujo.svg"
        meta = d / "meta.json"
        if not svg.exists():
            continue
        ok = True
        if meta.exists():
            m = json.loads(meta.read_text(encoding="utf-8"))
            ok = bool(m.get("svg_hallado")) and bool((m.get("svg") or {}).get("parsea"))
        if ok:
            ultimas[re.sub(r"_\d+$", "", d.name)] = (d.name, svg)
    filas = []
    for casa, (nombre, svg) in sorted(ultimas.items()):
        r = analizar(svg)
        if r is None or not r["top"]:
            print(f"{casa}: sin tinta o sin parsear ({nombre})")
            continue
        dom = r["top"][0][0]
        filas.append({
            "casa": casa, "corrida": nombre, "letra": letras.get(casa, "?"), "fondo": r["fondo"],
            "fondo_familia": r["fondo_familia"], "fondo_L": r["fondo_L"], "paneles": r["paneles"], "sin_fondo": r["sin_fondo"],
            "letra_color": dom, "letra_familia": familia_pintura(dom),
            "top": r["top"], "paleta_n": len(r["paleta"]),
        })
    ancho = max(len(f["casa"]) for f in filas)
    print(f"{'casa'.ljust(ancho)}  letra  fondo (L)               letra = pintura con más tinta | las tres siguientes | paneles excluidos")
    for f in filas:
        top = " | ".join(f"{h} ({familia_pintura(h)}) {v}" for h, v in f["top"][1:4])
        pan = [p for p in f["paneles"] if p[2] == "panel"]
        pan = f" | paneles: {', '.join(str(p[0]) + ' ' + str(p[1]) for p in pan)}" if pan else ""
        if f["sin_fondo"]:
            pan += " | sin fondo (lienzo transparente, contado blanco)"
        print(f"{f['casa'].ljust(ancho)}  {f['letra']:<5}  {f['fondo']} {f['fondo_familia']:<7} {f['fondo_L']:<5}  "
              f"{f['letra_color']} ({f['letra_familia']}) {f['top'][0][1]} | {top}{pan}")
    print()
    print("Familias del color dominante (todas):", dict(Counter(f["letra_familia"] for f in filas).most_common()))
    print("Familias del color dominante (solo las A):",
          dict(Counter(f["letra_familia"] for f in filas if f["letra"] == "A").most_common()))
    print("Familias del fondo:", dict(Counter(f["fondo_familia"] for f in filas).most_common()))
    oscuro = sum(1 for f in filas if f["fondo_L"] < 0.35)
    print(f"Fondos oscuros (L < 0,35): {oscuro} de {len(filas)}; claros (L > 0,8): "
          f"{sum(1 for f in filas if f['fondo_L'] > 0.8)}")
    por_fab = defaultdict(Counter)
    for f in filas:
        por_fab[fabricante(f["casa"])][f["letra_familia"]] += 1
    print("Letra por fabricante:", {k: dict(v) for k, v in por_fab.items()})
    por_fab_fondo = defaultdict(Counter)
    for f in filas:
        por_fab_fondo[fabricante(f["casa"])]["oscuro" if f["fondo_L"] < 0.35 else "claro"] += 1
    print("Fondo por fabricante:", {k: dict(v) for k, v in por_fab_fondo.items()})
    print("Rojo en algún lugar del top-3:", sum(1 for f in filas if any("rojo" in familia_pintura(h) for h, _ in f["top"][:3])),
          "| verde en el top-3:", sum(1 for f in filas if any("verde" in familia_pintura(h) for h, _ in f["top"][:3])))
    print("Letras pintadas con degradado:", sum(1 for f in filas if "→" in f["letra_color"]), "de", len(filas))
    print("Familias simplificadas (un degradado cuenta por su primera familia):",
          dict(Counter(f["letra_familia"].split("→")[0] for f in filas if f["letra"] == "A").most_common()), "(solo A)")
    if "--csv" in sys.argv:
        with open("2026-10-20_salida_colores.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["casa", "corrida", "letra", "fondo", "fondo_familia", "fondo_L", "sin_fondo", "letra_color", "letra_familia", "top", "paleta_n"])
            for r in filas:
                w.writerow([r["casa"], r["corrida"], r["letra"], r["fondo"], r["fondo_familia"], r["fondo_L"], int(r["sin_fondo"]),
                            r["letra_color"], r["letra_familia"], json.dumps(r["top"]), r["paleta_n"]])


if __name__ == "__main__":
    main()
