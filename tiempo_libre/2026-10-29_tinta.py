#!/usr/bin/env python3
"""Cuánta birome gastan los dibujos del repositorio.

Lee todos los corridas/dibujos*/<consigna>/<casa>_<rep>/dibujo.svg y, para cada uno, mide:
  - trazo: el largo de todo lo que tiene stroke (el camino que haría una birome dibujando las líneas);
  - relleno: el área de todo lo que tiene fill (lo que una birome tendría que rayar para pintarlo).
Después pasa las dos cosas a metros de trazo de birome y a biromes enteras.

Supuestos, a la vista:
  - El lienzo de 400 unidades mide 10,58 cm (96 puntos por pulgada: 400 px = 4,17 pulgadas). Si el
    viewBox es otro, se escala para que el lado mayor del viewBox ocupe esos 10,58 cm.
  - Una birome escribe 3 km (BIC, Cristal: "up to 3 kilometers") con un trazo de 0,4 mm de ancho.
  - Una línea más ancha que 0,4 mm se recorre tantas veces como quepan 0,4 mm en su ancho
    (stroke-width por la escala del transform); una más angosta, una vez.
  - Pintar un área es rayarla con líneas de 0,4 mm pegadas: metros = área / 0,4 mm.
  - Se cuenta cada figura entera, aunque después la tape otra (como la dibuja el navegador).
  - Se ignoran: <text> (se cuentan aparte), filtros, máscaras, clipPath, pattern, marker,
    opacidad, degradados (cuentan como fill), animaciones. <use> se resuelve y se cuenta.
  - Los SVG mal formados (cortados por el techo de tokens) se leen con lxml en modo recover.
  - El fill por omisión es negro, como en SVG: una figura sin fill="none" está rellena.

Uso: python3 tinta.py <raíz del repositorio> [--csv tinta.csv]
Necesita svgpathtools, numpy y lxml.
"""
import csv
import math
import re
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from lxml import etree
from svgpathtools import parse_path

LADO_CM = 400 * 2.54 / 96          # 10,5833 cm
ANCHO_BIROME_CM = 0.04             # 0,4 mm
BIROME_M = 3000.0                  # 3 km
NS = "{http://www.w3.org/2000/svg}"
XLINK = "{http://www.w3.org/1999/xlink}"
SALTAR = {"defs", "clipPath", "mask", "pattern", "marker", "symbol", "filter", "linearGradient",
          "radialGradient", "style", "title", "desc", "metadata", "animate", "animateTransform",
          "animateMotion", "set", "script", "foreignObject"}
FORMAS = {"path", "rect", "circle", "ellipse", "line", "polyline", "polygon"}


def local(tag):
    return tag.split("}")[-1] if isinstance(tag, str) else ""


# ---------- transformaciones ----------

def matriz(transform):
    """Compone un atributo transform en una matriz 3x3."""
    m = np.identity(3)
    if not transform:
        return m
    for nombre, args in re.findall(r"(\w+)\s*\(([^)]*)\)", transform):
        a = [float(x) for x in re.findall(r"-?\d*\.?\d+(?:e-?\d+)?", args)]
        t = np.identity(3)
        if nombre == "translate":
            t[0, 2] = a[0] if a else 0
            t[1, 2] = a[1] if len(a) > 1 else 0
        elif nombre == "scale":
            t[0, 0] = a[0] if a else 1
            t[1, 1] = a[1] if len(a) > 1 else t[0, 0]
        elif nombre == "rotate":
            ang = math.radians(a[0]) if a else 0
            r = np.array([[math.cos(ang), -math.sin(ang), 0], [math.sin(ang), math.cos(ang), 0], [0, 0, 1]])
            if len(a) >= 3:
                t1 = np.identity(3); t1[0, 2], t1[1, 2] = a[1], a[2]
                t2 = np.identity(3); t2[0, 2], t2[1, 2] = -a[1], -a[2]
                t = t1 @ r @ t2
            else:
                t = r
        elif nombre == "matrix" and len(a) == 6:
            t = np.array([[a[0], a[2], a[4]], [a[1], a[3], a[5]], [0, 0, 1]])
        elif nombre == "skewX":
            t[0, 1] = math.tan(math.radians(a[0])) if a else 0
        elif nombre == "skewY":
            t[1, 0] = math.tan(math.radians(a[0])) if a else 0
        m = m @ t
    return m


def aplicar(m, puntos):
    p = np.asarray(puntos, dtype=float)
    if len(p) == 0:
        return p
    h = np.column_stack([p, np.ones(len(p))])
    return (m @ h.T).T[:, :2]


def escala_de(m):
    return math.sqrt(abs(m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]))


# ---------- estilos ----------

def estilos_css(raiz):
    """Reglas .clase{...} de los <style>, lo justo para fill/stroke/stroke-width."""
    reglas = {}
    for st in raiz.iter(NS + "style"):
        texto = st.text or ""
        for sel, cuerpo in re.findall(r"\.([\w-]+)\s*\{([^}]*)\}", texto):
            d = {}
            for par in cuerpo.split(";"):
                if ":" in par:
                    k, v = par.split(":", 1)
                    d[k.strip()] = v.strip()
            reglas[sel] = d
    return reglas


def propio(el, css):
    """Propiedades de presentación declaradas en el elemento (atributo, style= o clase)."""
    d = {}
    for cl in (el.get("class") or "").split():
        d.update(css.get(cl, {}))
    for k in ("fill", "stroke", "stroke-width"):
        if el.get(k) is not None:
            d[k] = el.get(k)
    for par in (el.get("style") or "").split(";"):
        if ":" in par:
            k, v = par.split(":", 1)
            if k.strip() in ("fill", "stroke", "stroke-width"):
                d[k.strip()] = v.strip()
    return d


def hereda(estilo, el, css):
    e = dict(estilo)
    e.update(propio(el, css))
    return e


def pinta(valor):
    if valor is None:
        return True            # el fill por omisión es negro
    v = valor.strip().lower()
    return v not in ("none", "transparent", "")


def traza(valor):
    if valor is None:
        return False           # el stroke por omisión es none
    v = valor.strip().lower()
    return v not in ("none", "transparent", "")


def numero(s, default=0.0, ref=400.0):
    if s is None:
        return default
    s = s.strip()
    try:
        if s.endswith("%"):
            return float(s[:-1]) / 100 * ref
        return float(re.match(r"-?\d*\.?\d+(?:e-?\d+)?", s).group())
    except (AttributeError, ValueError):
        return default


# ---------- geometría ----------

def polilineas(el, ref):
    """Lista de (puntos, cerrada) de la forma, en unidades de usuario."""
    t = local(el.tag)
    if t == "rect":
        x, y = numero(el.get("x"), 0, ref), numero(el.get("y"), 0, ref)
        w, h = numero(el.get("width"), 0, ref), numero(el.get("height"), 0, ref)
        if w <= 0 or h <= 0:
            return []
        return [([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], True)]
    if t == "circle":
        cx, cy, r = numero(el.get("cx"), 0, ref), numero(el.get("cy"), 0, ref), numero(el.get("r"), 0, ref)
        if r <= 0:
            return []
        a = np.linspace(0, 2 * math.pi, 129)[:-1]
        return [(list(zip(cx + r * np.cos(a), cy + r * np.sin(a))), True)]
    if t == "ellipse":
        cx, cy = numero(el.get("cx"), 0, ref), numero(el.get("cy"), 0, ref)
        rx, ry = numero(el.get("rx"), 0, ref), numero(el.get("ry"), 0, ref)
        if rx <= 0 or ry <= 0:
            return []
        a = np.linspace(0, 2 * math.pi, 129)[:-1]
        return [(list(zip(cx + rx * np.cos(a), cy + ry * np.sin(a))), True)]
    if t == "line":
        return [([(numero(el.get("x1"), 0, ref), numero(el.get("y1"), 0, ref)),
                  (numero(el.get("x2"), 0, ref), numero(el.get("y2"), 0, ref))], False)]
    if t in ("polyline", "polygon"):
        nums = [float(x) for x in re.findall(r"-?\d*\.?\d+(?:e-?\d+)?", el.get("points") or "")]
        pts = list(zip(nums[0::2], nums[1::2]))
        return [(pts, t == "polygon")] if len(pts) >= 2 else []
    if t == "path":
        d = el.get("d") or ""
        try:
            camino = parse_path(d)
        except Exception:
            return []
        salida = []
        try:
            subs = camino.continuous_subpaths()
        except Exception:
            subs = [camino]
        for sub in subs:
            pts = []
            for seg in sub:
                n = 2 if type(seg).__name__ == "Line" else 24
                for u in np.linspace(0, 1, n, endpoint=False):
                    z = seg.point(u)
                    pts.append((z.real, z.imag))
            if sub:
                z = sub[-1].point(1.0)
                pts.append((z.real, z.imag))
            cerrada = bool(re.search(r"[zZ]\s*$", d.strip())) or (len(sub) > 0 and abs(sub.start - sub.end) < 1e-6)
            if len(pts) >= 2:
                salida.append((pts, cerrada))
        return salida
    return []


def largo(pts):
    p = np.asarray(pts)
    return float(np.sum(np.hypot(np.diff(p[:, 0]), np.diff(p[:, 1]))))


def area(pts):
    p = np.asarray(pts)
    x, y = p[:, 0], p[:, 1]
    return 0.5 * abs(float(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))))


# ---------- recorrido del árbol ----------

class Medida:
    def __init__(self):
        self.trazo_u = 0.0       # unidades de usuario
        self.trazo_pasadas_u = 0.0
        self.relleno_u2 = 0.0
        self.formas = 0
        self.textos = 0
        self.usos = 0
        self.un_solo_path = 0
        self.mayor_subtrazo = 0  # puntos (órdenes) del subcamino continuo más largo
        self.paths = 0
        self.negro_omision = 0   # paths o polilíneas abiertas sin fill declarado: el navegador las rellena de negro
        self.negro_omision_u2 = 0.0


def recorrer(el, m, estilo, css, ids, ref, med, prof=0):
    t = local(el.tag)
    if t in SALTAR or prof > 40:
        return
    if t == "text":
        med.textos += 1
        return
    m2 = m @ matriz(el.get("transform"))
    e2 = hereda(estilo, el, css)
    if t == "use":
        href = el.get("href") or el.get(XLINK + "href") or ""
        obj = ids.get(href.lstrip("#"))
        if obj is None:
            return
        med.usos += 1
        mu = m2 @ matriz(f"translate({numero(el.get('x'), 0, ref)} {numero(el.get('y'), 0, ref)})")
        recorrer(obj, mu, e2, css, ids, ref, med, prof + 1)
        return
    if t in FORMAS:
        med.formas += 1
        if t == "path":
            med.paths += 1
            d = el.get("d") or ""
            for sub in re.split(r"[Mm]", d)[1:]:
                n = len(re.findall(r"[A-Za-z]", sub)) + 1
                med.mayor_subtrazo = max(med.mayor_subtrazo, n)
        esc = escala_de(m2)
        ancho = numero(e2.get("stroke-width"), 1.0, ref) * esc
        for pts, cerrada in polilineas(el, ref):
            P = aplicar(m2, pts)
            if traza(e2.get("stroke")):
                L = largo(P) + (largo([P[-1], P[0]]) if cerrada else 0)
                med.trazo_u += L
                pasadas = max(1.0, (ancho * (LADO_CM / ref)) / ANCHO_BIROME_CM)
                med.trazo_pasadas_u += L * pasadas
            if pinta(e2.get("fill")) and (cerrada or t == "path") and t not in ("line", "polyline"):
                med.relleno_u2 += area(P)
                if e2.get("fill") is None and not cerrada and t == "path":
                    med.negro_omision += 1
                    med.negro_omision_u2 += area(P)
        return
    for hijo in el:
        if isinstance(hijo.tag, str):
            recorrer(hijo, m2, e2, css, ids, ref, med, prof + 1)


def medir(ruta):
    datos = ruta.read_bytes()
    recuperado = False
    try:
        raiz = etree.fromstring(datos)
    except etree.XMLSyntaxError:
        raiz = etree.fromstring(datos, etree.XMLParser(recover=True, huge_tree=True))
        recuperado = True
    if raiz is None:
        return None, True
    vb = raiz.get("viewBox")
    if vb:
        nums = [float(x) for x in re.findall(r"-?\d*\.?\d+(?:e-?\d+)?", vb)]
        ref = max(nums[2], nums[3]) if len(nums) == 4 else 400.0
    else:
        ref = max(numero(raiz.get("width"), 400), numero(raiz.get("height"), 400))
    ids = {el.get("id"): el for el in raiz.iter() if isinstance(el.tag, str) and el.get("id")}
    css = estilos_css(raiz)
    med = Medida()
    recorrer(raiz, np.identity(3), {}, css, ids, ref, med)
    formas_directas = [el for el in raiz.iter() if isinstance(el.tag, str) and local(el.tag) in FORMAS]
    med.un_solo_path = int(len(formas_directas) == 1 and local(formas_directas[0].tag) == "path")
    u_cm = LADO_CM / ref
    return {
        "elementos": med.formas, "textos": med.textos, "usos": med.usos, "paths": med.paths,
        "trazo_m": med.trazo_u * u_cm / 100,
        "trazo_birome_m": med.trazo_pasadas_u * u_cm / 100,
        "relleno_cm2": med.relleno_u2 * u_cm * u_cm,
        "relleno_birome_m": med.relleno_u2 * u_cm * u_cm / ANCHO_BIROME_CM / 100,
        "un_solo_path": med.un_solo_path, "mayor_subtrazo": med.mayor_subtrazo,
        "negro_omision": med.negro_omision, "negro_omision_cm2": med.negro_omision_u2 * u_cm * u_cm,
    }, recuperado


def casa_de(nombre):
    return re.sub(r"_\d+$", "", nombre)


def main():
    raiz = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    csv_salida = None
    if "--csv" in sys.argv:
        csv_salida = sys.argv[sys.argv.index("--csv") + 1]
    archivos = sorted(raiz.glob("corridas/dibujos*/*/*/dibujo.svg"))
    filas = []
    vacios = ilegibles = recuperados = 0
    for f in archivos:
        if f.stat().st_size == 0:
            vacios += 1
            continue
        idioma = {"dibujos": "es", "dibujos_en": "en", "dibujos_zh": "zh"}.get(f.parts[-4], f.parts[-4])
        consigna, carpeta = f.parts[-3], f.parts[-2]
        r, rec = medir(f)
        if r is None:
            ilegibles += 1
            print(f"  ilegible (ni en modo recover): {f}")
            continue
        recuperados += rec
        r.update({"idioma": idioma, "consigna": consigna, "casa": casa_de(carpeta), "carpeta": carpeta,
                  "recuperado": int(rec)})
        filas.append(r)
    print(f"Dibujos: {len(archivos)} archivos; {vacios} vacíos; {ilegibles} ilegibles; {len(filas)} medidos, "
          f"{recuperados} de ellos leídos en modo recover (SVG cortado o mal formado).")
    print(f"Escala: 400 unidades = {LADO_CM:.2f} cm; birome de {BIROME_M/1000:.0f} km y {ANCHO_BIROME_CM*10:.1f} mm.")
    T = sum(r["trazo_m"] for r in filas)
    Tp = sum(r["trazo_birome_m"] for r in filas)
    A = sum(r["relleno_cm2"] for r in filas)
    Ap = sum(r["relleno_birome_m"] for r in filas)
    n = len(filas)
    print(f"\nTRAZO (largo de las líneas): {T:,.0f} m en total; {T/n:.2f} m por dibujo; "
          f"mediana {np.median([r['trazo_m'] for r in filas]):.2f} m.")
    print(f"  Con el ancho de línea (pasadas de 0,4 mm): {Tp:,.0f} m = {Tp/BIROME_M:.2f} biromes.")
    print(f"RELLENO (área pintada): {A:,.0f} cm² en total; {A/n:.0f} cm² por dibujo "
          f"({A/n/(LADO_CM**2):.2f} lienzos); mediana {np.median([r['relleno_cm2'] for r in filas]):.0f} cm².")
    print(f"  Rayado a 0,4 mm: {Ap:,.0f} m = {Ap/BIROME_M:.1f} biromes.")
    print(f"Relleno / trazo (en metros de birome): {Ap/Tp:.1f}.")
    print(f"Todo junto: {(Tp+Ap)/BIROME_M:.1f} biromes para {n} dibujos.")
    solo_trazo = sum(1 for r in filas if r["relleno_cm2"] == 0 and r["trazo_m"] > 0)
    solo_relleno = sum(1 for r in filas if r["trazo_m"] == 0 and r["relleno_cm2"] > 0)
    mas_trazo = sum(1 for r in filas if r["trazo_birome_m"] > r["relleno_birome_m"])
    print(f"\nDibujos sin ningún relleno (solo líneas): {solo_trazo}; sin ninguna línea (solo pintura): {solo_relleno}; "
          f"con más metros de línea que de pintura: {mas_trazo} de {n}.")
    print(f"Elementos <text> (no medidos): {sum(r['textos'] for r in filas)} en {sum(1 for r in filas if r['textos'])} dibujos; "
          f"<use> resueltos: {sum(r['usos'] for r in filas)}.")
    print(f"Dibujos hechos con un solo <path> y nada más: {sum(r['un_solo_path'] for r in filas)} "
          f"({', '.join(r['carpeta'] + '/' + r['consigna'] for r in filas if r['un_solo_path'])}).")
    neg = [r for r in filas if r["negro_omision"]]
    print(f"Paths abiertos sin fill declarado (el navegador los rellena de negro): {sum(r['negro_omision'] for r in filas)} "
          f"en {len(neg)} dibujos, {sum(r['negro_omision_cm2'] for r in filas):.0f} cm² de negro por omisión; "
          f"por casa: {', '.join(f'{c} {k}' for c, k in sorted(((c, sum(1 for r in neg if r['casa'] == c)) for c in set(r['casa'] for r in neg)), key=lambda x: -x[1])[:8])}.")
    top = sorted(filas, key=lambda r: -r["mayor_subtrazo"])[:5]
    print("Subtrazos continuos más largos (órdenes después de una M): " +
          "; ".join(f"{r['mayor_subtrazo']} ({r['casa']}, {r['consigna']}, {r['idioma']})" for r in top))

    # Por casa
    por_casa = defaultdict(list)
    for r in filas:
        por_casa[r["casa"]].append(r)
    print(f"\n{'casa':28s} {'n':>3s} {'trazo m/dib':>11s} {'pint m/dib':>11s} {'trazo %':>8s} {'elem/dib':>8s}")
    orden = sorted(por_casa.items(), key=lambda kv: -np.mean([r["trazo_birome_m"] for r in kv[1]]))
    for casa, rs in orden:
        t = np.mean([r["trazo_birome_m"] for r in rs])
        p = np.mean([r["relleno_birome_m"] for r in rs])
        print(f"{casa:28s} {len(rs):3d} {t:11.2f} {p:11.1f} {100*t/(t+p):7.1f}% {np.mean([r['elementos'] for r in rs]):8.1f}")

    # Por consigna
    por_cons = defaultdict(list)
    for r in filas:
        por_cons[r["consigna"]].append(r)
    print(f"\n{'consigna':22s} {'n':>3s} {'trazo m/dib':>11s} {'pint m/dib':>11s} {'trazo %':>8s}")
    for cons, rs in sorted(por_cons.items(), key=lambda kv: -np.mean([r["trazo_birome_m"] for r in kv[1]])):
        t = np.mean([r["trazo_birome_m"] for r in rs])
        p = np.mean([r["relleno_birome_m"] for r in rs])
        print(f"{cons:22s} {len(rs):3d} {t:11.2f} {p:11.1f} {100*t/(t+p):7.1f}%")

    # Por idioma
    print()
    for idi in ("es", "en", "zh"):
        rs = [r for r in filas if r["idioma"] == idi]
        if rs:
            t = np.mean([r["trazo_birome_m"] for r in rs]); p = np.mean([r["relleno_birome_m"] for r in rs])
            print(f"idioma {idi}: {len(rs)} dibujos, trazo {t:.2f} m/dib, pintura {p:.1f} m/dib, trazo {100*t/(t+p):.1f} %")

    # Extremos
    print("\nMás metros de línea (con ancho):")
    for r in sorted(filas, key=lambda r: -r["trazo_birome_m"])[:5]:
        print(f"  {r['trazo_birome_m']:7.1f} m  {r['casa']}  {r['consigna']} ({r['idioma']})  {r['elementos']} elementos")
    print("Más metros de pintura:")
    for r in sorted(filas, key=lambda r: -r["relleno_birome_m"])[:5]:
        print(f"  {r['relleno_birome_m']:7.1f} m  {r['casa']}  {r['consigna']} ({r['idioma']})  {r['relleno_cm2']/(LADO_CM**2):.1f} lienzos")

    if csv_salida:
        campos = ["idioma", "consigna", "casa", "carpeta", "elementos", "paths", "textos", "usos", "recuperado",
                  "trazo_m", "trazo_birome_m", "relleno_cm2", "relleno_birome_m", "un_solo_path", "mayor_subtrazo",
                  "negro_omision", "negro_omision_cm2"]
        with open(csv_salida, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=campos)
            w.writeheader()
            for r in filas:
                w.writerow({k: (round(r[k], 4) if isinstance(r[k], float) else r[k]) for k in campos})
        print(f"\nCSV: {csv_salida} ({len(filas)} filas)")


if __name__ == "__main__":
    main()
