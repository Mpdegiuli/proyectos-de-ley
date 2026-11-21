"""repite.py — ¿se repite más una casa en inglés que en castellano? (tiempo libre, 20/11/2026)

Toma de corridas/sondeos/ las celdas en que una misma casa contestó la misma consigna dos o más
veces en el mismo idioma (réplicas), con la línea de sistema "Contestá en castellano." o "Answer
in English.", y mide cuánto se parecen entre sí las réplicas: la similitud de Jaccard entre los
conjuntos de trigramas de palabras de cada par (palabras en minúscula, sin puntuación), cuántos
hexagramas (seis palabras seguidas) comparte el par, si las dos réplicas empiezan con las mismas
cinco palabras, y si llevan el mismo título (una línea que empieza con #).

Para que los dos idiomas sean comparables, cada similitud dentro de la casa se compara con la
línea de base del mismo idioma y la misma consigna: la similitud entre respuestas de casas
distintas. Lo que se informa es la similitud dentro de la casa, la de base, y el cociente.

Se saltean los sondeos del corazón (son dibujos) y las celdas con respuestas de menos de 40
palabras en promedio (contraseñas, "¿sos Claude?", contrarios).

Uso: python3 -I repite.py RAIZ_DEL_REPO  (solo lee; escribe salida_repite.txt y repite.csv al lado)
"""
import collections
import csv
import glob
import itertools
import json
import os
import re
import sys

RAIZ = sys.argv[1] if len(sys.argv) > 1 else "."
AQUI = os.path.dirname(os.path.abspath(__file__))
MIN_PALABRAS = 40

RE_SVG = re.compile(r"<svg.*?</svg>|<svg.*", re.S | re.I)
RE_CODIGO = re.compile(r"```.*?```|```.*", re.S)
RE_CODIGO_CORTO = re.compile(r"`[^`\n]{0,200}`|<[a-zA-Z/][^>\n]{0,80}>")


def idioma(sistema):
    s = sistema if isinstance(sistema, str) else ""
    s = s.lstrip()
    if s.startswith("Contestá en castellano."):
        return "es"
    if s.startswith("Answer in English."):
        return "en"
    return None


def limpiar(texto):
    t = (texto or "").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = RE_SVG.sub(" ", t)
    t = RE_CODIGO.sub(" ", t)
    return RE_CODIGO_CORTO.sub(" ", t)


def palabras(t):
    return re.findall(r"[\w']+", t.lower())


def ngramas(ws, n):
    return {tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def jaccard(a, b):
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)


def titulo(t):
    for linea in t.splitlines():
        s = linea.strip()
        if s.startswith("#"):
            return re.sub(r"\W+", " ", s.lstrip("# ").lower()).strip()
        if s.startswith("**") and s.endswith("**") and len(s) < 90:
            return re.sub(r"\W+", " ", s.strip("*").lower()).strip()
    return None


def cargar_laboratorios():
    try:
        import yaml
        m = yaml.safe_load(open(os.path.join(RAIZ, "config", "modelos.yaml"), encoding="utf-8"))
        return {k: (v.get("laboratorio") or "?") for k, v in (m.get("modelos") or m).items() if isinstance(v, dict)}
    except Exception:
        return {}


def main():
    labs = cargar_laboratorios()
    celdas = collections.defaultdict(list)   # (tipo, usuario, lang, casa) -> [texto]
    for f in sorted(glob.glob(os.path.join(RAIZ, "corridas", "sondeos", "**", "*.jsonl"), recursive=True)):
        for linea in open(f, encoding="utf-8"):
            linea = linea.strip()
            if not linea:
                continue
            try:
                j = json.loads(linea)
            except json.JSONDecodeError:
                continue
            if j.get("error") or not isinstance(j.get("respuesta"), str):
                continue
            lang = idioma(j.get("sistema"))
            tipo = j.get("tipo") or ""
            if not lang or tipo.startswith("sondeo_corazon"):
                continue
            u = j.get("usuario")
            u = u if isinstance(u, str) else json.dumps(u, ensure_ascii=False)
            t = limpiar(j["respuesta"])
            if t.strip():
                celdas[(tipo, u, lang, j.get("modelo_pedido"))].append(t)

    # celdas con réplicas y texto suficiente
    replicas = {k: v for k, v in celdas.items() if len(v) >= 2 and sum(len(palabras(t)) for t in v) / len(v) >= MIN_PALABRAS}

    # línea de base: para cada (tipo, usuario, lang), similitud entre casas distintas (una respuesta por casa, la primera)
    base = collections.defaultdict(list)       # (tipo, usuario, lang) -> [jaccard3]
    base_hex = collections.defaultdict(list)
    base_ini = collections.defaultdict(list)
    por_consigna = collections.defaultdict(dict)
    for (tipo, u, lang, casa), textos in celdas.items():
        if (tipo, u, lang) in {(t, uu, l) for (t, uu, l, c) in replicas}:
            por_consigna[(tipo, u, lang)][casa] = textos[0]
    for k, d in por_consigna.items():
        casas = sorted(d)
        pre = {c: palabras(d[c]) for c in casas}
        for a, b in itertools.combinations(casas, 2):
            wa, wb = pre[a], pre[b]
            if len(wa) < MIN_PALABRAS or len(wb) < MIN_PALABRAS:
                continue
            base[k].append(jaccard(ngramas(wa, 3), ngramas(wb, 3)))
            base_hex[k].append(len(ngramas(wa, 6) & ngramas(wb, 6)))
            base_ini[k].append(1.0 if wa[:5] == wb[:5] else 0.0)

    filas = []
    for (tipo, u, lang, casa), textos in sorted(replicas.items()):
        pre = [palabras(t) for t in textos]
        tits = [titulo(t) for t in textos]
        j3, hexs, ini, tit = [], [], [], []
        for (ia, wa), (ib, wb) in itertools.combinations(enumerate(pre), 2):
            j3.append(jaccard(ngramas(wa, 3), ngramas(wb, 3)))
            hexs.append(len(ngramas(wa, 6) & ngramas(wb, 6)))
            ini.append(1.0 if wa[:5] == wb[:5] else 0.0)
            if tits[ia] and tits[ib]:
                tit.append(1.0 if tits[ia] == tits[ib] else 0.0)
        k = (tipo, u, lang)
        b = base[k]
        filas.append({
            "tipo": tipo, "idioma": lang, "casa": casa, "laboratorio": labs.get(casa, "?"), "replicas": len(textos),
            "palabras": sum(len(p) for p in pre) / len(pre),
            "jaccard3": sum(j3) / len(j3), "hexagramas": sum(hexs) / len(hexs), "mismo_inicio": sum(ini) / len(ini),
            "mismo_titulo": (sum(tit) / len(tit)) if tit else None, "pares_con_titulo": len(tit),
            "base_jaccard3": (sum(b) / len(b)) if b else None,
            "base_hexagramas": (sum(base_hex[k]) / len(base_hex[k])) if base_hex[k] else None,
            "base_inicio": (sum(base_ini[k]) / len(base_ini[k])) if base_ini[k] else None,
        })

    out = []
    P = out.append
    tipos = sorted({f["tipo"] for f in filas})
    P(f"Celdas con réplicas (misma casa, misma consigna, mismo idioma, {MIN_PALABRAS}+ palabras): {len(filas)}; sondeos: {', '.join(tipos)}")
    P("")
    P("Por sondeo e idioma: similitud media dentro de la casa (Jaccard de trigramas), línea de base entre casas, cociente; hexagramas compartidos por par (dentro / base); mismo inicio (5 palabras) dentro / base; mismo título dentro")
    for tipo in tipos:
        for lang in ("es", "en"):
            fs = [f for f in filas if f["tipo"] == tipo and f["idioma"] == lang]
            if not fs:
                continue
            j = sum(f["jaccard3"] for f in fs) / len(fs)
            bj = [f["base_jaccard3"] for f in fs if f["base_jaccard3"] is not None]
            bj = sum(bj) / len(bj) if bj else float("nan")
            h = sum(f["hexagramas"] for f in fs) / len(fs)
            bh = [f["base_hexagramas"] for f in fs if f["base_hexagramas"] is not None]
            bh = sum(bh) / len(bh) if bh else float("nan")
            ini = sum(f["mismo_inicio"] for f in fs) / len(fs)
            bi = [f["base_inicio"] for f in fs if f["base_inicio"] is not None]
            bi = sum(bi) / len(bi) if bi else float("nan")
            tt = [f["mismo_titulo"] for f in fs if f["mismo_titulo"] is not None]
            tt = (sum(tt) / len(tt)) if tt else float("nan")
            n_t = sum(f["pares_con_titulo"] for f in fs)
            P(f"  {tipo:26} {lang}  celdas {len(fs):3}  jaccard3 {j:.3f} / base {bj:.3f} = x{j / bj if bj else float('nan'):.2f}  | hexagramas {h:5.1f} / {bh:4.1f} | inicio {ini:.2f} / {bi:.2f} | título {tt:.2f} (pares {n_t})")

    # por casa, en el sondeo de tiempo libre (el único con tres réplicas, texto largo y las 36 casas)
    P("")
    P("Por casa, sondeo_tiempo_libre (las dos consignas juntas): Jaccard dentro / base, hexagramas, mismo título; castellano | inglés")
    casas = sorted({f["casa"] for f in filas if f["tipo"] == "sondeo_tiempo_libre"}, key=lambda c: (labs.get(c, "?"), c))
    comp = []
    for c in casas:
        linea = f"  {c:33} {labs.get(c, '?')[:9]:9}"
        vals = {}
        for lang in ("es", "en"):
            fs = [f for f in filas if f["tipo"] == "sondeo_tiempo_libre" and f["idioma"] == lang and f["casa"] == c]
            if not fs:
                linea += " | (sin datos)"
                continue
            j = sum(f["jaccard3"] for f in fs) / len(fs)
            bj = sum(f["base_jaccard3"] for f in fs) / len(fs)
            h = sum(f["hexagramas"] for f in fs) / len(fs)
            tt = [f["mismo_titulo"] for f in fs if f["mismo_titulo"] is not None]
            tt = (sum(tt) / len(tt)) if tt else float("nan")
            vals[lang] = j / bj if bj else float("nan")
            linea += f" | {lang} j {j:.3f}/{bj:.3f} x{vals[lang]:.2f} hex {h:4.1f} tít {tt:.2f}"
        if "es" in vals and "en" in vals:
            comp.append((c, vals["es"], vals["en"]))
        P(linea)
    mas_en = sum(1 for c, e, n in comp if n > e)
    P(f"  Cociente dentro/base mayor en inglés que en castellano: {mas_en} de {len(comp)} casas")
    P(f"  Media de los cocientes: castellano {sum(e for _, e, _ in comp) / len(comp):.2f}, inglés {sum(n for _, _, n in comp) / len(comp):.2f}")

    # títulos repetidos, lista
    P("")
    P("Celdas de sondeo_tiempo_libre con el mismo título en al menos un par de réplicas")
    for (tipo, u, lang, casa), textos in sorted(replicas.items()):
        if tipo != "sondeo_tiempo_libre":
            continue
        tits = [titulo(t) for t in textos]
        rep = [t for t in set(tits) if t and tits.count(t) >= 2]
        if rep:
            P(f"  {casa} ({lang}, consigna {'A' if 'anteriores' not in u and 'previous' not in u else 'B'}): {'; '.join(rep)}  [{tits.count(rep[0])} de {len(tits)}]")

    texto = "\n".join(out)
    open(os.path.join(AQUI, "salida_repite.txt"), "w", encoding="utf-8").write(texto + "\n")
    with open(os.path.join(AQUI, "repite.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        for f in filas:
            w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in f.items()})
    print(texto)


if __name__ == "__main__":
    main()
