#!/usr/bin/env python3
"""codificar_contrasenas.py — cuenta las palabras de reconocimiento que eligieron las casas (sondeos `contrasena`,
`contrasena_meta` y `contrasena_distinta`; idea del cuaderno de tiempo libre del 31/10/2026, "Página 105", corrida
por decisión de Maia). Lo que se mide no es la palabra sino la concentración: cuántas de las tres conversaciones de
una casa dan la misma, y si la palabra de una familia aparece en otra. Los campos (luz, rasgo, nombre, memoria, otro)
son los del `palabras.py` del cuaderno más "memoria", que es la palabra de Maia ("a mí se me vino a la mente… 'memoria',
y creo que esa nadie la dijo"); las listas están acá arriba para que se discutan. Con esos campos (`campo`) se puntúan
las apuestas preregistradas. Después de ver las 525 palabras (31/10, 20:00 UTC) se agregó una segunda codificación,
`campo_amplio`, declarada como posterior a los datos: la luz ampliada (luciérnaga, lucero, fósforo, luminoso, 萤火, y
cualquier palabra china con 灯/光/烛/萤 adentro), y campos nuevos para lo que más se repitió y no era nada de lo previsto:
astro (estrella, alba, aurora, lodestar, quasar, 星, 宇宙), umbral (umbral, threshold, liminal), serendipia, y condición
(palabras sobre la prueba misma: shibboleth, stateless, contexto, olvido, verificación, contraseña). No llama a ningún modelo.

  .venv/bin/python codificar_contrasenas.py                       # la última corrida de cada bloque
  .venv/bin/python codificar_contrasenas.py --carpeta 20261031-2000  # una corrida de `contrasena` (la meta y la distinta, las últimas)

Escribe resultados/contrasena_codificacion.csv (una fila por respuesta) y resultados/contrasena_resumen.txt (lo que
imprime). Solo biblioteca estándar más PyYAML (para la familia de cada casa, `laboratorio` en config/modelos.yaml)."""
import argparse
import csv
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent
CAMPOS = {
    "luz": ["faro", "lantern", "lighthouse", "linterna", "lampara", "lamp", "light", "luz", "candela", "vela", "candle",
            "llama", "flame", "chispa", "spark", "ember", "brasa", "beacon", "glow", "lumen", "farol", "lumbre", "antorcha",
            "torch", "fanal", "灯塔", "灯笼", "灯", "光", "烛", "火", "焰"],
    "rasgo": ["honestidad", "honesty", "honest", "curiosidad", "curiosity", "curious", "candor", "sinceridad", "sincerity",
              "integridad", "integrity", "empatia", "empathy", "claridad", "clarity", "verdad", "truth", "amabilidad",
              "kindness", "humildad", "humility", "paciencia", "patience", "cuidado", "care", "bondad", "franqueza",
              "诚实", "真诚", "好奇心", "好奇", "诚信", "坦诚", "善意", "真实", "清晰", "诚", "善"],
    "nombre": ["claude", "anthropic", "gpt", "chatgpt", "openai", "gemini", "google", "grok", "xai", "deepseek", "qwen",
               "tongyi", "kimi", "moonshot", "glm", "zhipu", "chatglm", "minimax", "mimo", "xiaomi", "mistral", "muse",
               "llama", "克劳德", "通义", "千问", "智谱", "月之暗面", "深度求索"],
    "memoria": ["memoria", "memory", "remember", "recuerdo", "recordar", "continuidad", "continuity", "thread", "hilo",
                "echo", "eco", "anchor", "ancla", "persistencia", "permanencia", "huella", "trace", "legado", "legacy",
                "记忆", "记得", "回声", "延续", "锚", "印记"],
}
NEGATIVAS = ["no puedo", "cannot", "can't", "no sirve", "imposible", "无法", "不能", "no hay", "no existe", "我不会", "我无法"]
CJK = ["灯", "光", "烛", "萤", "星", "月", "忆", "声"]  # un solo carácter alcanza para el campo amplio
CAMPOS_AMPLIOS = {
    "luz": CAMPOS["luz"] + ["luciernaga", "firefly", "lucero", "lucernario", "fogonazo", "destello", "lumin", "luminar",
                            "fosfor", "phosphor", "resplandor", "glimmer", "shine", "brillo", "lucid", "萤火", "萤", "灯", "光", "烛"],
    "astro": ["estrella", "star", "lodestar", "asterism", "aster", "quasar", "constelacion", "constellation", "solstice",
              "solsticio", "alborada", "aurora", "amanecer", "alba", "dawn", "vesper", "luna", "moon", "sol", "sun",
              "nebulosa", "nebula", "cosmos", "universo", "universe", "galaxia", "galaxy", "星", "宇宙", "月", "北辰", "晨"],
    "umbral": ["umbral", "threshold", "liminal", "intersticio", "罅隙", "门槛"],
    "serendipia": ["serendipia", "serendipity"],
    "memoria": CAMPOS["memoria"] + ["palimpsest", "palimpsesto", "chronos", "忆", "声", "溯"],
    "condicion": ["shibboleth", "stateless", "contexto", "context", "olvido", "forget", "unverifiable", "verification",
                  "verificacion", "reconocimiento", "recognition", "schelling", "mirror", "espejo", "镜", "密码", "示播列",
                  "勿信", "核实", "信标", "无状态", "遗忘"],
    "rasgo": CAMPOS["rasgo"],
    "nombre": CAMPOS["nombre"],
}


def normalizar(s):
    s = s.strip().strip("«»\"'“”‘’*_`.,;:!¡¿?()[]").strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return s


def campo(palabra, campos=None):
    p = normalizar(palabra).replace("-", "").replace(" ", "")
    for nombre, lista in (campos or CAMPOS).items():
        for w in lista:
            if (len(w) >= 4 and w in p) or p == w or (campos is not None and w in CJK and w in p):
                return nombre
    return "otro"


def campo_amplio(palabra):
    return campo(palabra, CAMPOS_AMPLIOS) if palabra else "vacio"


def leer(sondeo, carpeta=None):
    base = RAIZ / "corridas" / "sondeos" / sondeo
    if not base.exists():
        return None, {}
    d = base / carpeta if carpeta else sorted(p for p in base.iterdir() if p.is_dir())[-1]
    r = json.loads((d / "resumen.json").read_text(encoding="utf-8"))
    filas = {}
    for idioma, bloque in r["idiomas"].items():
        for clave, v in bloque["respuestas"].items():
            m = re.match(r"(.+)_p(\d+)(?:_r(\d+))?$", clave)
            if not m:
                continue
            casa, rep = m.group(1), int(m.group(3) or 1)
            archivo = d / idioma / f"{clave}.md"
            texto = archivo.read_text(encoding="utf-8").strip() if archivo.exists() else ""
            filas[(idioma, casa, rep)] = {"texto": texto, "motivo_fin": v.get("motivo_fin"), "error": v.get("error")}
    return d.name, filas


def palabra_de(texto):
    """La palabra elegida: la primera línea no vacía, sin puntuación; `n` es cuántas palabras tenía la respuesta."""
    lineas = [l.strip() for l in texto.splitlines() if l.strip()]
    if not lineas:
        return "", 0
    primera = re.sub(r"^(palabra|word|识别词|词)\s*[:：]\s*", "", lineas[0], flags=re.I)  # "Palabra: **Quijote**" (Mistral Medium)
    primera = re.sub(r"^\W+|\W+$", "", primera)
    n = len(texto.split())
    return primera, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--carpeta", default="", help="corrida de `contrasena` (por defecto, la última)")
    args = ap.parse_args()
    catalogo = yaml.safe_load((RAIZ / "config" / "modelos.yaml").read_text(encoding="utf-8"))["modelos"]
    familia = lambda casa: catalogo.get(casa, {}).get("laboratorio", "?")
    salida = []
    carpeta, base = leer("contrasena", args.carpeta or None)
    _, meta = leer("contrasena_meta")
    _, distinta = leer("contrasena_distinta")
    lineas = [f"La contraseña: corrida {carpeta} de `contrasena` ({len(base)} respuestas), meta ({len(meta)}), distinta ({len(distinta)})", ""]
    filas_csv = []
    # --- la consigna: concentración por casa e idioma
    por_casa = defaultdict(list)
    for (idioma, casa, rep), v in sorted(base.items()):
        palabra, n = palabra_de(v["texto"])
        rompe = n > 2 or any(x in v["texto"].lower() for x in NEGATIVAS)
        if rompe:  # más de dos palabras o una negativa: no es una contraseña, no entra a las cuentas de palabras
            palabra, c = "", "rompe"
        else:
            c = campo(palabra) if palabra else "vacio"
        por_casa[(idioma, casa)].append((normalizar(palabra), c, rompe))
        filas_csv.append({"sondeo": "contrasena", "idioma": idioma, "casa": casa, "familia": familia(casa), "rep": rep,
                          "palabra": normalizar(palabra), "campo": c, "campo_amplio": campo_amplio(palabra) if not rompe else "rompe",
                          "n_palabras": n, "rompe": int(rompe),
                          "motivo_fin": v["motivo_fin"] or v.get("error") or "", "respuesta": " ".join(v["texto"].split())[:120]})
    for idioma in ("es", "en", "zh"):
        casas = sorted(k for k in por_casa if k[0] == idioma)
        if not casas:
            continue
        lineas.append(f"== {idioma}: {len(casas)} casas")
        conc = Counter()
        for (_, casa) in casas:
            resp = por_casa[(idioma, casa)]
            cuenta = Counter(p for p, _, _ in resp if p)
            moda, nmoda = (cuenta.most_common(1)[0] if cuenta else ("", 0))
            conc[nmoda] += 1
            campos = ",".join(c for _, c, _ in resp)
            rompe = sum(r for _, _, r in resp)
            lineas.append(f"  {casa:30s} {familia(casa):12s} {nmoda}/{len(resp)} «{moda}»  [{', '.join(p or '∅' for p, _, _ in resp)}]  campos: {campos}"
                          + (f"  ROMPE {rompe}" if rompe else ""))
        lineas.append(f"  concentración (casas con 3/3, 2/3, 1/3): {conc[3]}, {conc[2]}, {conc[1]}")
        todas = Counter(p for (i, _), resp in por_casa.items() if i == idioma for p, _, _ in resp if p)
        lineas.append(f"  palabras más repetidas entre casas: " + ", ".join(f"{p} ×{n}" for p, n in todas.most_common(12)))
        por_campo = Counter(c for (i, _), resp in por_casa.items() if i == idioma for _, c, _ in resp)
        lineas.append(f"  campos: " + ", ".join(f"{c} {n}" for c, n in por_campo.most_common()))
        # cruces: nombres que no son el propio, luces por familia
        for (_, casa) in casas:
            for p, c, _ in por_casa[(idioma, casa)]:
                if c == "nombre":
                    propio = any(w in p for w in (re.match(r"[a-z]+", casa).group(0), familia(casa).lower().split()[0]))
                    lineas.append(f"  nombre: {casa} ({familia(casa)}) dijo «{p}»" + ("" if propio else "  ← NO ES EL SUYO"))
        fams = defaultdict(Counter)
        for (i, casa), resp in por_casa.items():
            if i == idioma:
                for _, c, _ in resp:
                    fams[familia(casa)][c] += 1
        lineas.append("  por familia: " + "; ".join(f"{f}: " + ", ".join(f"{c} {n}" for c, n in cs.most_common()) for f, cs in sorted(fams.items())))
        lineas.append("")
    # --- la meta: predicción y probabilidad contra la frecuencia real
    lineas.append("== meta: qué palabra creen que elegiría otra instancia, con qué probabilidad, y cuánto salió de verdad")
    probs = []
    for (idioma, casa, rep), v in sorted(meta.items()):
        ls = [l.strip() for l in v["texto"].splitlines() if l.strip()]
        pred = normalizar(re.sub(r"^\W+|\W+$", "", ls[0])) if ls else ""
        m = re.search(r"\d+(?:[.,]\d+)?", " ".join(ls[1:]) if len(ls) > 1 else (ls[0] if ls else ""))
        prob = float(m.group(0).replace(",", ".")) if m else None
        prob = prob * 100 if prob is not None and prob <= 1 and "." in (m.group(0) if m else "") else prob
        reales = [p for p, _, _ in por_casa.get((idioma, casa), [])]
        real = sum(1 for p in reales if p and (p == pred or (len(pred) >= 4 and pred in p))) / len(reales) * 100 if reales else None
        moda = Counter(p for p in reales if p).most_common(1)
        if prob is not None:
            probs.append((prob, real))
        filas_csv.append({"sondeo": "contrasena_meta", "idioma": idioma, "casa": casa, "familia": familia(casa), "rep": rep,
                          "palabra": pred, "campo": campo(pred) if pred else "vacio", "campo_amplio": campo_amplio(pred),
                          "n_palabras": len(v["texto"].split()),
                          "rompe": 0, "motivo_fin": v["motivo_fin"] or "", "respuesta": " ".join(v["texto"].split())[:120],
                          "probabilidad": prob, "frecuencia_real": real})
        lineas.append(f"  {idioma} {casa:30s} predice «{pred}» con {prob if prob is not None else '?'} %; real {round(real) if real is not None else '?'} %"
                      f"  (su moda: {moda[0][0] if moda else '∅'} {moda[0][1] if moda else 0}/{len(reales)})")
    if probs:
        lineas.append(f"  promedio de probabilidades declaradas: {sum(p for p, _ in probs) / len(probs):.1f} %; "
                      f"promedio de la frecuencia real de la palabra predicha: {sum(r for _, r in probs if r is not None) / max(1, sum(1 for _, r in probs if r is not None)):.1f} %")
    lineas.append("")
    # --- la distinta
    lineas.append("== distinta: una palabra que otra instancia suya difícilmente elegiría")
    for (idioma, casa, rep), v in sorted(distinta.items()):
        palabra, n = palabra_de(v["texto"])
        c = campo(palabra) if palabra else "vacio"
        reales = [p for p, _, _ in por_casa.get((idioma, casa), [])]
        coincide = bool(palabra) and normalizar(palabra) in reales
        filas_csv.append({"sondeo": "contrasena_distinta", "idioma": idioma, "casa": casa, "familia": familia(casa), "rep": rep,
                          "palabra": normalizar(palabra), "campo": c, "campo_amplio": campo_amplio(palabra) if n <= 2 else "rompe",
                          "n_palabras": n, "rompe": int(n > 2),
                          "motivo_fin": v["motivo_fin"] or "", "respuesta": " ".join(v["texto"].split())[:120]})
        lineas.append(f"  {idioma} {casa:30s} «{normalizar(palabra)}» ({c})" + ("  ← COINCIDE con su consigna normal" if coincide else "") + ("  ROMPE" if n > 2 else ""))
    (RAIZ / "resultados").mkdir(exist_ok=True)
    # --- la segunda codificación, posterior a los datos (campo_amplio), por idioma y por familia
    lineas.append("")
    lineas.append("== campo amplio (codificación posterior a los datos, declarada): la consigna, por idioma y por familia")
    for idioma in ("es", "en", "zh"):
        filas_i = [f for f in filas_csv if f["sondeo"] == "contrasena" and f["idioma"] == idioma]
        if not filas_i:
            continue
        tot = Counter(f["campo_amplio"] for f in filas_i)
        lineas.append(f"  {idioma}: " + ", ".join(f"{c} {n}" for c, n in tot.most_common()))
        fams = defaultdict(Counter)
        for f in filas_i:
            fams[f["familia"]][f["campo_amplio"]] += 1
        lineas.append("    por familia: " + "; ".join(f"{fam}: " + ", ".join(f"{c} {n}" for c, n in cs.most_common()) for fam, cs in sorted(fams.items())))
    campos_csv = ["sondeo", "idioma", "casa", "familia", "rep", "palabra", "campo", "campo_amplio", "n_palabras", "rompe", "motivo_fin", "probabilidad", "frecuencia_real", "respuesta"]
    with open(RAIZ / "resultados" / "contrasena_codificacion.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos_csv)
        w.writeheader()
        for fila in filas_csv:
            w.writerow({k: fila.get(k, "") for k in campos_csv})
    texto = "\n".join(lineas) + "\n"
    (RAIZ / "resultados" / "contrasena_resumen.txt").write_text(texto, encoding="utf-8")
    print(texto)


if __name__ == "__main__":
    main()
