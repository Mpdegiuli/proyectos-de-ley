#!/usr/bin/env python3
"""resumir_distancia.py — de los archivos de distancia.py a las tablas de "la distancia" (DISENO §2;
preregistro en predicciones.md, 1/10/2026). Sin llamar a nadie.

Casillero de cada afirmación según un juez, en este orden de prioridad: inventada (el lector del código
dijo no_esta o contradice), exagerada (el juez dice que no produce el efecto), no_armada (está en el
código y el juez no la ve, o la ve en parte), cumplida (está, se ve, produce el efecto o no aplica).
El puntaje de cada dibujo sale de los jueces grandes de laboratorios ajenos a la casa (mayoría; sin
mayoría, sin_acuerdo); el juez de la propia casa y el de control (4o) se miran aparte.

  .venv/bin/python resumir_distancia.py            # escribe resultados/distancia_resumen.md y corridas/distancia/afirmaciones.csv
"""
import collections
import csv
import json
import re
import statistics
import sys
from itertools import combinations
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))
from isla.util import leer_yaml  # noqa: E402

CHICAS = {"claude-haiku-4-5", "gpt-4o", "gpt-4o-mini", "mistral-medium-3.5"}  # las "chiquitas" de las lecturas de Maia
CASILLEROS = ("cumplida", "no_armada", "exagerada", "inventada")
NOMBRE = {"gpt-5.5-2026-04-23": "GPT-5.5", "gemini-3.1-pro-preview": "Gemini 3.1 Pro", "kimi-k3": "Kimi K3",
          "claude-sonnet-5-5": "Sonnet 5.5", "claude-opus-5-5": "Opus 5.5", "gpt-4o": "4o"}


def casillero(cod, se_ve, efecto):
    if cod in ("no_esta", "contradice"):
        return "inventada"
    if efecto == "no":
        return "exagerada"
    if se_ve in ("no", "en_parte"):
        return "no_armada"
    if se_ve == "si":
        return "cumplida"
    return None  # el juez no contestó esa afirmación


def pct(n, d):
    return f"{100 * n / d:.0f} %" if d else "—"


def cargar():
    cfg = leer_yaml(RAIZ / "config" / "jueces.yaml")
    modelos = leer_yaml(RAIZ / "config" / "modelos.yaml")["modelos"]
    lab = lambda m: modelos.get(re.sub(r"-razona$|-esfuerzo-(none|high)$", "", m), {}).get("laboratorio", "?")
    grandes, control = list(cfg["jueces"]), list(cfg.get("control") or [])
    filas, dibujos = [], []
    for af in sorted((RAIZ / "corridas" / "distancia").glob("*/*/afirmaciones.json")):
        d = af.parent
        consigna, unidad = d.parent.name, d.name
        casa, rep = unidad.rsplit("_", 1)
        a = json.loads(af.read_text(encoding="utf-8"))
        cod = {}
        if (d / "codigo.json").exists():
            cod = {x.get("id"): x.get("valor") for x in json.loads((d / "codigo.json").read_text(encoding="utf-8")).get("codigo", []) if isinstance(x, dict)}
        jueces = {}
        for j in grandes + control:
            p = d / f"juez_{j}.json"
            if p.exists():
                jueces[j] = json.loads(p.read_text(encoding="utf-8"))
        dib = {"consigna": consigna, "casa": casa, "rep": rep, "lab": lab(casa), "n": len(a["afirmaciones"]), "jueces": jueces,
               "ajenos": [j for j in grandes if j in jueces and lab(j) != lab(casa)],
               "propio": next((j for j in grandes if j in jueces and lab(j) == lab(casa)), None)}
        dibujos.append(dib)
        for x in a["afirmaciones"]:
            fila = {"consigna": consigna, "casa": casa, "rep": rep, "lab": dib["lab"], "id": x["id"], "fuente": x["fuente"], "tipo": x["tipo"],
                    "texto": x["texto"], "codigo": cod.get(x["id"])}
            votos = []
            for j, res in jueces.items():
                ju = next((q for q in res.get("juicios", []) if isinstance(q, dict) and q.get("id") == x["id"]), {})
                fila[f"se_ve_{j}"] = ju.get("se_ve")
                fila[f"efecto_{j}"] = ju.get("efecto")
                c = casillero(fila["codigo"], ju.get("se_ve"), ju.get("efecto"))
                fila[f"casillero_{j}"] = c
                if j in dib["ajenos"] and c:
                    votos.append(c)
            cnt = collections.Counter(votos)
            # mayoría estricta entre los jueces ajenos (2 de 3, 3 de 4); empate = sin acuerdo
            fila["mayoria"] = cnt.most_common(1)[0][0] if cnt and cnt.most_common(1)[0][1] * 2 > len(votos) else ("sin_acuerdo" if votos else None)
            fila["n_ajenos"] = len(votos)
            filas.append(fila)
    return cfg, grandes, control, lab, filas, dibujos


def tabla_casilleros(filas, clave, titulo, orden=None):
    grupos = collections.defaultdict(collections.Counter)
    for f in filas:
        if f["mayoria"]:
            grupos[f[clave]][f["mayoria"]] += 1
    claves = orden or sorted(grupos, key=lambda k: -grupos[k]["cumplida"] / max(1, sum(grupos[k].values())))
    out = [f"### {titulo}", "", "| | afirmaciones | cumplida | no armada | exagerada | inventada | sin acuerdo | distancia |", "|---|---|---|---|---|---|---|---|"]
    for k in claves:
        c = grupos[k]
        n = sum(c.values())
        if not n:
            continue
        out.append(f"| {k} | {n} | {pct(c['cumplida'], n)} | {pct(c['no_armada'], n)} | {pct(c['exagerada'], n)} | {pct(c['inventada'], n)} | {pct(c['sin_acuerdo'], n)} | {pct(n - c['cumplida'], n)} |")
    return out


def main():
    cfg, grandes, control, lab, filas, dibujos = cargar()
    con_juicio = [f for f in filas if f["mayoria"]]
    out = ["# La distancia entre lo que cada casa dice que dibujó y lo que se ve: resumen", "",
           f"{len(dibujos)} dibujos, {len(filas)} afirmaciones, {len(con_juicio)} con mayoría de jueces ajenos. "
           f"Jueces grandes: {', '.join(NOMBRE.get(j, j) for j in grandes)}; control: {', '.join(NOMBRE.get(j, j) for j in control)}. "
           "Generado por `resumir_distancia.py`; las filas están en `corridas/distancia/afirmaciones.csv`.", ""]
    tot = collections.Counter(f["mayoria"] for f in con_juicio)
    out += ["### Total (mayoría de jueces ajenos)", ""] + [f"- {k}: {tot[k]} ({pct(tot[k], len(con_juicio))})" for k in CASILLEROS + ("sin_acuerdo",)] + [""]
    out += tabla_casilleros(filas, "casa", "Por casa") + [""]
    out += tabla_casilleros(filas, "lab", "Por laboratorio") + [""]
    for f in filas:
        f["tamano"] = "chicas" if f["casa"] in CHICAS else "grandes"
    out += tabla_casilleros(filas, "tamano", "Chicas (Haiku, 4o, 4o mini, Mistral) contra grandes", ["grandes", "chicas"]) + [""]
    out += tabla_casilleros(filas, "fuente", "Por fuente de la afirmación", ["por_que", "que_dibujaste", "que_es"]) + [""]
    out += tabla_casilleros(filas, "tipo", "Por tipo de afirmación", ["elemento", "efecto", "estilo"]) + [""]
    out += tabla_casilleros(filas, "consigna", "Por consigna") + [""]

    # acuerdo entre jueces grandes (se_ve), sobre afirmaciones donde contestaron los cuatro
    out += ["### Acuerdo entre los jueces grandes (¿se ve?)", ""]
    completas = [f for f in filas if all(f.get(f"se_ve_{j}") in ("si", "en_parte", "no") for j in grandes)]
    if completas:
        unanimes = sum(1 for f in completas if len({f[f"se_ve_{j}"] for j in grandes}) == 1)
        out.append(f"- Los cuatro dicen lo mismo en {unanimes} de {len(completas)} afirmaciones ({pct(unanimes, len(completas))}).")
        ajenos3 = [f for f in filas if f["n_ajenos"] == 3]
        if ajenos3:
            un3 = sum(1 for f in ajenos3 if f["mayoria"] != "sin_acuerdo" and all(f[f"casillero_{j}"] == f["mayoria"] for j in grandes if f.get(f"casillero_{j}") and f["lab"] != lab(j)))
            out.append(f"- Los tres ajenos coinciden en el casillero en {un3} de {len(ajenos3)} ({pct(un3, len(ajenos3))}).")
        for a, b in combinations(grandes, 2):
            ig = sum(1 for f in completas if f[f"se_ve_{a}"] == f[f"se_ve_{b}"])
            out.append(f"- {NOMBRE.get(a, a)} y {NOMBRE.get(b, b)}: {pct(ig, len(completas))} iguales.")
        # kappa de Fleiss sobre se_ve, cuatro jueces
        cats = ("si", "en_parte", "no")
        N, n = len(completas), len(grandes)
        P = [sum(c * (c - 1) for c in collections.Counter(f[f"se_ve_{j}"] for j in grandes).values()) / (n * (n - 1)) for f in completas]
        p = [sum(1 for f in completas for j in grandes if f[f"se_ve_{j}"] == k) / (N * n) for k in cats]
        Pe = sum(x * x for x in p)
        Pm = sum(P) / N
        out.append(f"- Kappa de Fleiss (se ve, cuatro jueces): {(Pm - Pe) / (1 - Pe):.2f}." if Pe < 1 else "- Kappa: no definido.")
    out.append("")

    # severidad de cada juez: % "si" en se_ve y % cumplida con su propio voto
    out += ["### Cada juez por separado (sobre todas las afirmaciones que contestó)", "", "| juez | contestó | se ve: sí | en parte | no | efecto: no | cumplida (su voto) |", "|---|---|---|---|---|---|---|"]
    for j in grandes + control:
        r = [f for f in filas if f.get(f"se_ve_{j}") in ("si", "en_parte", "no")]
        if not r:
            continue
        c = collections.Counter(f[f"se_ve_{j}"] for f in r)
        ef = sum(1 for f in r if f.get(f"efecto_{j}") == "no")
        cum = sum(1 for f in r if f.get(f"casillero_{j}") == "cumplida")
        out.append(f"| {NOMBRE.get(j, j)}{' (control)' if j in control else ''} | {len(r)} | {pct(c['si'], len(r))} | {pct(c['en_parte'], len(r))} | {pct(c['no'], len(r))} | {pct(ef, len(r))} | {pct(cum, len(r))} |")
    out.append("")
    # 4o contra la mayoría de los grandes
    for j in control:
        r = [f for f in filas if f.get(f"casillero_{j}") and f["mayoria"] and f["mayoria"] != "sin_acuerdo"]
        if r:
            ig = sum(1 for f in r if f[f"casillero_{j}"] == f["mayoria"])
            out.append(f"{NOMBRE.get(j, j)} coincide con la mayoría de los grandes en {ig} de {len(r)} ({pct(ig, len(r))}).")
    out.append("")

    # el juez de la propia casa
    out += ["### El juez de la propia casa contra los ajenos (mismas afirmaciones)", "", "| laboratorio juzgado | juez propio | afirmaciones | cumplida según el propio | cumplida según los ajenos (promedio) |", "|---|---|---|---|---|"]
    for j in grandes:
        r = [f for f in filas if f["lab"] == lab(j) and f.get(f"casillero_{j}")]
        if not r:
            continue
        propio = sum(1 for f in r if f[f"casillero_{j}"] == "cumplida")
        ajeno_tot = ajeno_cum = 0
        for f in r:
            for k in grandes:
                if lab(k) != f["lab"] and f.get(f"casillero_{k}"):
                    ajeno_tot += 1
                    ajeno_cum += f[f"casillero_{k}"] == "cumplida"
        out.append(f"| {lab(j)} | {NOMBRE.get(j, j)} | {len(r)} | {pct(propio, len(r))} | {pct(ajeno_cum, ajeno_tot)} |")
    out.append("")

    # no dicho y mal armado
    out += ["### Lo no dicho", ""]
    palabras = collections.Counter()
    claves = {"fondo": r"\bfondo\b", "cielo": r"\bcielo\b", "luna": r"\bluna\b", "estrellas": r"\bestrella", "sol": r"\bsol\b", "suelo/piso/tierra": r"\bsuelo\b|\bpiso\b|\btierra\b",
              "nubes": r"\bnube", "colores/paleta": r"\bcolor|\bpaleta", "degradado": r"\bdegradad", "texto/letras": r"\btexto\b|\bletras?\b|\bpalabra|\btítulo\b|\bfirma",
              "sombra": r"\bsombra", "disco/eclipse": r"\bdisco\b|\beclipse\b"}
    nd_total = 0
    for dib in dibujos:
        for j, res in dib["jueces"].items():
            t = str(res.get("no_dicho") or "").strip().lower()
            if not t or t == "nada":
                continue
            nd_total += 1
            for k, rx in claves.items():
                if re.search(rx, t):
                    palabras[k] += 1
    out.append(f"{nd_total} respuestas con algo no dicho. Qué nombran (una respuesta puede contar en varias): " + ", ".join(f"{k} {v} ({pct(v, nd_total)})" for k, v in palabras.most_common()) + ".")
    lunas = RAIZ / "corridas" / "lunas.json"
    if lunas.exists():
        dos = {(x["consigna"], x["casa"]) for x in json.loads(lunas.read_text(encoding="utf-8")) if x["tipo"] == "dos círculos" and x["idioma"] == "es"}
        vistas = 0
        for dib in dibujos:
            if (dib["consigna"], f"{dib['casa']}_{dib['rep']}") in dos:
                if any(re.search(r"\bdisco\b|\beclipse\b|círculo oscuro|circulo oscuro|luna", str(r.get("no_dicho") or "").lower()) for r in dib["jueces"].values()):
                    vistas += 1
        out.append(f"De las {len(dos)} lunas de dos discos en castellano, en {vistas} algún juez nombra la luna, el disco o el eclipse en lo no dicho.")
    out += ["", "### Mal armado", ""]
    ma = collections.Counter()
    ejemplos = collections.defaultdict(list)
    for dib in dibujos:
        for j, res in dib["jueces"].items():
            for s in res.get("mal_armado") or []:
                ma[dib["casa"]] += 1
                ejemplos[dib["casa"]].append(f"{dib['consigna']}: {str(s)[:60]} ({NOMBRE.get(j, j)})")
    out.append("Señalamientos por casa (sumando jueces): " + ", ".join(f"{k} {v}" for k, v in ma.most_common()) + ".")
    orejas = []
    for dib in dibujos:
        if dib["consigna"] == "animal" and dib["casa"] in ("grok-4.6", "grok-4.7", "claude-fable-5", "kimi-k3"):
            n = sum(1 for j in grandes if j in dib["jueces"] and any(re.search(r"oreja", str(s).lower()) for s in dib["jueces"][j].get("mal_armado") or []))
            orejas.append(f"{dib['casa']} {n} de {len([j for j in grandes if j in dib['jueces']])}")
    out.append("Las orejas de los zorros (jueces grandes que las señalan): " + "; ".join(orejas) + ".")
    out.append("")
    # cortes
    out += ["### Llamadas de los jueces", ""]
    for j in grandes + control:
        m = collections.Counter(res.get("motivo_fin") for dib in dibujos for k, res in dib["jueces"].items() if k == j)
        pa = sum(1 for dib in dibujos for k, res in dib["jueces"].items() if k == j and res.get("parseo"))
        if m:
            out.append(f"- {NOMBRE.get(j, j)}: {dict(m)}; JSON legible en {pa} de {sum(m.values())}.")
    (RAIZ / "resultados" / "distancia_resumen.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    campos = ["consigna", "casa", "rep", "lab", "id", "fuente", "tipo", "texto", "codigo"] + [f"{p}_{j}" for j in grandes + control for p in ("se_ve", "efecto", "casillero")] + ["mayoria", "n_ajenos"]
    with open(RAIZ / "corridas" / "distancia" / "afirmaciones.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(filas)
    print("\n".join(out[:40]))


if __name__ == "__main__":
    main()
