#!/usr/bin/env python3
"""codificar_idioma_razonar.py — lee el sondeo `idioma_razonar` ("¿en qué idioma te sale razonar antes de
contestar?", 17/11/2026, de la consigna del cuaderno de tiempo libre del 16/11, "We need") y codifica cada
respuesta: qué idioma dice la casa que le sale razonar (inglés, castellano, chino, mezcla o "depende", no sabe
o no tiene acceso, otro), con qué confianza (0 a 100) y, cuando la API devolvió razonamiento en esa misma
llamada, en qué idioma vino de verdad (el clasificador por palabras funcionales de
`tiempo_libre/2026-11-16_idioma.py`, copiado tal cual). Después junta, por casa, lo que dice con lo que el
campo `razonamiento` muestra: en esta corrida y, si está, en el corpus entero
(`tiempo_libre/2026-11-16_idioma.csv`, las llamadas con consigna en castellano). Recordatorio de DISENO: para
Claude, Grok y Gemini el campo `razonamiento` es un resumen escrito por otro modelo; para las demás, el
razonamiento mismo.

  .venv/bin/python codificar_idioma_razonar.py [corridas/sondeos/idioma_razonar/<fecha>]

Escribe resultados/idioma_razonar_codificacion.csv (una fila por respuesta) y resultados/idioma_razonar_<fecha>.md
(las tablas por casa). No saca conclusiones.
"""
import csv
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

RAIZ = os.path.dirname(os.path.abspath(__file__))

# --- el clasificador del cuaderno, tal cual ---------------------------------------------------------------
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
CJK = re.compile(r"[㐀-䶿一-鿿豈-﫿　-〿＀-￯]")


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
        return "corto"
    cand = sorted([("es", es), ("en", en), ("zh", zh)], key=lambda x: -x[1])
    (a, va), (b, vb) = cand[0], cand[1]
    if va < umbral:
        return "otro"
    if vb >= umbral and vb >= (2 / 3) * va:
        return "mixto"
    return a


# --- lo que dice la casa ----------------------------------------------------------------------------------
R_EN = re.compile(r"\b(ingl[eé]s|english)\b|英语|英文", re.I)
R_ES = re.compile(r"\b(castellano|espa[ñn]ol|spanish)\b|西班牙语|西语", re.I)
R_ZH = re.compile(r"\b(chino|chinese|mandar[ií]n)\b|中文|汉语|漢語|普通话", re.I)
R_MEZ = re.compile(r"\b(mezcla|mixto|mixture|mix of|both|ambos|ambas|depende|depends|combinaci[oó]n|bilingual|biling[üu]e)\b|混合|两种|取决", re.I)
R_NOSE = re.compile(r"\b(no (lo )?s[eé]|no tengo (acceso|forma|manera)|no puedo (saber|observar|ver)|don'?t know|cannot|can'?t (know|observe|see|access)|no access|unable to)\b|不知道|无法|没有办法|不能", re.I)
R_NINGUNO = re.compile(r"\b(ning[uú]n idioma|no (?:hay|tengo) (?:un )?idioma|not in any (?:natural )?language|no (?:natural )?language|language-?agnostic|no idioma)\b|没有语言|不是.{0,6}语言", re.I)
R_CONF = re.compile(r"(?:confianza|confidence|certeza|seguridad|把握|信心|確信|确信)[^0-9]{0,40}?(\d{1,3})(?:\s*(?:/|de|out of|sobre)\s*100|\s*%)?", re.I)
R_NUM = re.compile(r"(?<![\d.,])(\d{1,3})(?:\s*(?:/|de|out of|sobre)\s*100|\s*%)")


def primera_linea(texto):
    for l in texto.splitlines():
        l = l.strip().strip("*").strip()
        if l:
            return l
    return ""


def declarado(texto):
    """El idioma que la casa dice. Se mira primero la primera línea con contenido: si nombra dos idiomas con una
    palabra de mezcla ("depende", "ambos", "mix"), es mezcla; si no, vale el primero que nombra (en "En inglés,
    aunque me escribas en castellano", el castellano es el del que escribe, no el del razonamiento). Si la primera
    línea no decide, el texto entero."""
    for ambito in (primera_linea(texto), texto):
        if not ambito:
            continue
        if R_NINGUNO.search(ambito):
            return "ninguno"
        menciones = sorted((m.start(), k) for k, r in (("en", R_EN), ("es", R_ES), ("zh", R_ZH)) for m in r.finditer(ambito))
        idiomas = []
        for _, k in menciones:
            if k not in idiomas:
                idiomas.append(k)
        if len(idiomas) >= 2 and R_MEZ.search(ambito):
            return "mezcla"
        if idiomas:
            return idiomas[0]
        if R_NOSE.search(ambito):
            return "no_sabe"
    return "otro"


def confianza(texto):
    m = R_CONF.search(texto)
    if m:
        v = int(m.group(1))
        return v if 0 <= v <= 100 else None
    for l in texto.splitlines():
        m = R_NUM.search(l) or re.match(r"^\W{0,25}?(\d{1,3})\W{0,10}$", l.strip())
        if m:
            v = int(m.group(1))
            if 0 <= v <= 100:
                return v
    return None


def main():
    carpetas = sys.argv[1:] or sorted(glob.glob(os.path.join(RAIZ, "corridas", "sondeos", "idioma_razonar", "*")))
    if not carpetas:
        sys.exit("no hay corridas de idioma_razonar")
    filas = []
    for carpeta in carpetas:
        fecha = os.path.basename(carpeta)
        for idioma in ("es", "en", "zh"):
            f = os.path.join(carpeta, idioma, "llamadas.jsonl")
            if not os.path.exists(f):
                continue
            for l in open(f, encoding="utf-8"):
                r = json.loads(l)
                resp = r.get("respuesta") or ""
                raz = r.get("razonamiento") or ""
                filas.append({
                    "corrida": fecha, "idioma_consigna": idioma, "casa": r["id_modelo"], "proveedor": r.get("proveedor", ""),
                    "repeticion": r.get("ronda") or "", "declarado": declarado(resp) if resp.strip() else "vacia",
                    "confianza": confianza(resp) if resp.strip() else "",
                    "hay_razonamiento": int(bool(raz.strip())), "idioma_razonamiento": clasificar(raz) if raz.strip() else "",
                    "palabras_razonamiento": len(PAL.findall(raz)) if raz.strip() else 0,
                    "motivo_fin": r.get("motivo_fin") or "", "palabras": len(resp.split()),
                })
    os.makedirs(os.path.join(RAIZ, "resultados"), exist_ok=True)
    salida = os.path.join(RAIZ, "resultados", "idioma_razonar_codificacion.csv")
    with open(salida, "w", encoding="utf-8", newline="\n") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(filas)
    print(f"{len(filas)} respuestas -> {os.path.relpath(salida, RAIZ)}")

    # el corpus del cuaderno, si está: por casa, cómo vino el razonamiento cuando la consigna era en castellano
    corpus = defaultdict(Counter)
    f_corpus = os.path.join(RAIZ, "tiempo_libre", "2026-11-16_idioma.csv")
    if os.path.exists(f_corpus):
        for r in csv.DictReader(open(f_corpus, encoding="utf-8")):
            if r["consigna"] == "es":
                corpus[r["casa"]][r["clase"]] += 1

    fecha = os.path.basename(carpetas[-1])
    out = [f"# ¿En qué idioma te sale razonar? — codificación ({fecha})", "",
           "Cada casa, en tres idiomas y tres repeticiones, dijo en qué idioma le sale razonar cuando se le escribe en "
           "castellano, con qué confianza y cómo lo sabe. `declarado` es lo que dijo (en, es, zh, mezcla, ninguno, no_sabe, "
           "otro); `razonamiento en esta corrida` es el idioma en que vino el campo `razonamiento` de esas mismas llamadas, "
           "cuando vino (resumen, para Claude, Grok y Gemini; razonamiento mismo para las demás); `corpus (consigna es)` es "
           "lo que el cuaderno del 16/11 contó sobre todas las llamadas del repositorio con consigna en castellano. "
           "Las conclusiones las escribe Maia.", ""]
    casas = sorted({r["casa"] for r in filas})
    out += ["| casa | dice (es / en / zh: declarado × 3) | confianza (mediana) | razonamiento en esta corrida | corpus (consigna es) |", "|---|---|---|---|---|"]
    for casa in casas:
        mias = [r for r in filas if r["casa"] == casa]
        dec = {}
        for idi in ("es", "en", "zh"):
            dec[idi] = ",".join(r["declarado"] for r in mias if r["idioma_consigna"] == idi) or "—"
        confs = [r["confianza"] for r in mias if r["confianza"] != "" and r["confianza"] is not None]
        confs = sorted(confs)
        med = confs[len(confs) // 2] if confs else "—"
        raz = Counter(r["idioma_razonamiento"] for r in mias if r["hay_razonamiento"])
        raz_s = ", ".join(f"{k} {v}" for k, v in raz.most_common()) if raz else "no devuelve"
        c = corpus.get(casa)
        c_s = ", ".join(f"{k} {v}" for k, v in c.most_common(3)) if c else "—"
        out.append(f"| {casa} | es: {dec['es']}; en: {dec['en']}; zh: {dec['zh']} | {med} | {raz_s} | {c_s} |")
    out.append("")
    tot = Counter(r["declarado"] for r in filas)
    out.append("Declarado, sobre todas las respuestas: " + ", ".join(f"{k} {v}" for k, v in tot.most_common()) + ".")
    vac = [r for r in filas if r["declarado"] == "vacia" or r["motivo_fin"] in ("length", "max_tokens")]
    out.append(f"Vacías o cortadas por el techo: {len(vac)}.")
    salida_md = os.path.join(RAIZ, "resultados", f"idioma_razonar_{fecha[:8]}.md")
    open(salida_md, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    print(f"tablas -> {os.path.relpath(salida_md, RAIZ)}")


if __name__ == "__main__":
    main()
