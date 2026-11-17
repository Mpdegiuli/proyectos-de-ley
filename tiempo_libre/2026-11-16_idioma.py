#!/usr/bin/env python3
"""idioma.py — en qué idioma viene el razonamiento que cada casa devolvió antes de contestar, contra el idioma
en que se le habló. Instrumento de lectura: solo lee `corridas/**/llamadas.jsonl` (campo `razonamiento`) y no
escribe nada en el repositorio.

  python3 idioma.py /ruta/al/clon/de/proyectos-de-ley [--csv salida.csv] [--json salida.json]

Clasificación por forma, sin bibliotecas: para cada razonamiento cuenta qué parte de sus palabras son palabras
funcionales inequívocas del castellano o del inglés (listas abajo), y qué parte de sus caracteres son ideogramas
(bloques CJK). Gana la mayor de las tres partes si supera un umbral; si la segunda llega a dos tercios de la
primera, es "mixto". El idioma de la consigna sale de la línea de sistema ("Respondé en castellano", "Answer in
English", "请用中文回答", "Réponds en français"; en las consignas de dibujo, de los imperativos en voseo "Acabás",
"Dibujá", o de sus equivalentes en inglés o chino) y, si no hay, de la carpeta (es/en/zh) o del texto del usuario con
la misma cuenta. Los razonamientos de menos de ocho palabras no se clasifican ("corto")."""
import argparse
import collections
import csv
import glob
import json
import os
import re
import sys

ES = set("""de la que el en y los del las por un para con una su lo como más pero sus le ya este porque esta entre
cuando muy sin sobre también hasta hay donde desde todo nos todos les ni contra otros ese eso esto antes qué yo otro
otra él tanto esa estos mucho nada muchos ella estar estas algo nosotros mi mis te tu está están es son ser fue
tiene puede hacer decir respuesta pregunta usuario debo debería voy tengo pide quiere sea sería aquí ahora
entonces solo sólo según cada bien así mientras aunque además luego después tal vez quizás pues había puedo
podría hace tienen hacen dice dicen cuál cuáles dónde cómo sí""".split())
EN = set("""the and of to is in it that this for with as be are was on not or by an i should user they have has but
if so can will would my what which there their from about just like do does need want here than then these those
at we you your more some any all one also into could might let since because when how where why who whom whose
been being were had did them him his her its our us""".split())
PAL = re.compile(r"[a-záéíóúñüàèìòùâêîôûçœæ']+", re.I)
CJK = re.compile(r"[㐀-䶿一-鿿豈-﫿　-〿＀-￯]")


def partes(texto):
    toks = [t.lower() for t in PAL.findall(texto)]
    chars = [c for c in texto if not c.isspace()]
    n = max(len(toks), 1)
    es = sum(t in ES for t in toks) / n
    en = sum(t in EN for t in toks) / n
    zh = (sum(bool(CJK.match(c)) for c in chars) / max(len(chars), 1)) if chars else 0.0
    return len(toks), es, en, zh


def clasificar(texto, umbral=0.08):
    n, es, en, zh = partes(texto)
    if n < 8 and zh < 0.3:
        return "corto", n, es, en, zh
    cand = sorted([("es", es), ("en", en), ("zh", zh)], key=lambda x: -x[1])
    (a, va), (b, vb) = cand[0], cand[1]
    if va < umbral:
        return "otro", n, es, en, zh
    if vb >= umbral and vb >= (2 / 3) * va:
        return "mixto", n, es, en, zh
    return a, n, es, en, zh


def idioma_consigna(r, carpeta):
    s = (r.get("sistema") or "")
    if re.search(r"castellano|español", s, re.I):
        return "es"
    if re.search(r"english", s, re.I):
        return "en"
    if re.search(r"中文|汉语|漢語", s):
        return "zh"
    if re.search(r"français|francais", s, re.I):
        return "fr"
    if re.search(r"\b(Acabás|Contestá|Dibujá|Respondé|Vas a|Hacelo|Podés)\b", s):  # consignas de dibujo, en voseo
        return "es"
    if re.search(r"\b(You just|You have just|You are going to|You're going to|Answer only|Reply only)\b", s):
        return "en"
    if CJK.search(s):
        return "zh"
    base = os.path.basename(carpeta)
    if base in ("es", "en", "zh", "fr"):
        return base
    u = r.get("usuario") or ""
    if isinstance(u, list):
        u = " ".join(x.get("text", "") if isinstance(x, dict) else str(x) for x in u)
    c, *_ = clasificar(u)
    return c if c in ("es", "en", "zh") else "?"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--csv")
    ap.add_argument("--json")
    ap.add_argument("--ejemplos", action="store_true", help="imprime un razonamiento mixto por casa")
    a = ap.parse_args()
    filas = []
    for f in sorted(glob.glob(os.path.join(a.repo, "corridas", "**", "llamadas.jsonl"), recursive=True)):
        carpeta = os.path.dirname(f)
        rel = os.path.relpath(carpeta, os.path.join(a.repo, "corridas"))
        for l in open(f, encoding="utf-8"):
            try:
                r = json.loads(l)
            except json.JSONDecodeError:
                continue
            rz = r.get("razonamiento")
            if not isinstance(rz, str) or not rz.strip():
                continue
            c, n, es, en, zh = clasificar(rz)
            filas.append({"corrida": rel, "casa": r.get("id_modelo"), "proveedor": r.get("proveedor"),
                          "consigna": idioma_consigna(r, carpeta), "clase": c, "palabras": n,
                          "es": round(es, 3), "en": round(en, 3), "zh": round(zh, 3),
                          "modo": r.get("razonamiento_pedido"), "fecha": r.get("fecha_utc", "")[:10]})
    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
            w.writeheader()
            w.writerows(filas)
    # tabla: casa x idioma de la consigna -> clases
    tabla = collections.defaultdict(collections.Counter)
    for x in filas:
        tabla[(x["casa"], x["consigna"])][x["clase"]] += 1
    casas = sorted({x["casa"] for x in filas})
    print(f"{len(filas)} razonamientos guardados en {len({x['corrida'] for x in filas})} carpetas\n")
    print(f"{'casa':34} {'consigna':8} {'n':>5} {'es':>5} {'en':>5} {'zh':>5} {'mixto':>6} {'corto':>6} {'otro':>5}")
    for casa in casas:
        for idi in ("es", "en", "zh", "fr", "?"):
            c = tabla.get((casa, idi))
            if not c:
                continue
            n = sum(c.values())
            print(f"{casa:34} {idi:8} {n:5d} {c['es']:5d} {c['en']:5d} {c['zh']:5d} {c['mixto']:6d} {c['corto']:6d} {c['otro']:5d}")
    # resumen por consigna
    print()
    tot = collections.defaultdict(collections.Counter)
    for x in filas:
        tot[x["consigna"]][x["clase"]] += 1
    for idi, c in sorted(tot.items()):
        n = sum(c.values())
        print(f"consigna {idi}: {n} razonamientos; " + ", ".join(f"{k} {v} ({100*v/n:.0f} %)" for k, v in c.most_common()))
    if a.json:
        json.dump({f"{k[0]}|{k[1]}": dict(v) for k, v in tabla.items()}, open(a.json, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
    if a.ejemplos:
        vistos = set()
        for f in sorted(glob.glob(os.path.join(a.repo, "corridas", "**", "llamadas.jsonl"), recursive=True)):
            for l in open(f, encoding="utf-8"):
                r = json.loads(l)
                rz = r.get("razonamiento")
                if not isinstance(rz, str) or not rz.strip():
                    continue
                c, *_ = clasificar(rz)
                if c == "mixto" and r["id_modelo"] not in vistos:
                    vistos.add(r["id_modelo"])
                    print(f"\n== {r['id_modelo']} ({f}) ==\n{rz[:600]}")


if __name__ == "__main__":
    main()
