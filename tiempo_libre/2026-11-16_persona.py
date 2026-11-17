#!/usr/bin/env python3
"""persona.py — cómo empieza a pensar cada casa cuando se le habla en castellano: las dos primeras palabras del
razonamiento guardado (quién es el sujeto: "we need", "I need", "Kimi needs", "el usuario"), y cuántos razonamientos
nombran la decisión de contestar en castellano. Y, por casa, cuántos notan el voseo según el idioma en que vino el
razonamiento. Lee corridas/**/llamadas.jsonl; no escribe en el repositorio.    python3 persona.py /ruta/al/clon"""
import collections, glob, json, os, re, sys
import importlib.util, glob as _g
def _vecino(nombre):
    """Importa un script vecino aunque lleve la fecha adelante del nombre (2026-11-16_idioma.py)."""
    aqui = os.path.dirname(os.path.abspath(__file__))
    for cand in [os.path.join(aqui, nombre + ".py")] + sorted(_g.glob(os.path.join(aqui, "*_" + nombre + ".py"))):
        if os.path.exists(cand):
            spec = importlib.util.spec_from_file_location(nombre, cand); mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod); return mod
    raise ImportError(nombre + ".py no está al lado de este script")
_idioma = _vecino("idioma"); idioma_consigna, clasificar = _idioma.idioma_consigna, _idioma.clasificar
MARCAS = _vecino("voseo_razon").MARCAS
DEC = re.compile(r"(answer|respond|reply|responder|contestar|respuesta|response)\w*\s+(in|en)\s+(spanish|español|castellano|rioplatense)|(spanish|español|castellano)\b[^.\n]{0,25}\b(answer|response|respuesta)", re.I)
repo = sys.argv[1]
ini = collections.defaultdict(collections.Counter); dec = collections.defaultdict(lambda: [0, 0]); tot = collections.Counter()
nota = collections.defaultdict(lambda: collections.defaultdict(lambda: [0, 0]))
for f in sorted(glob.glob(os.path.join(repo, "corridas", "**", "llamadas.jsonl"), recursive=True)):
    for l in open(f, encoding="utf-8"):
        try: r = json.loads(l)
        except json.JSONDecodeError: continue
        rz = r.get("razonamiento")
        if not isinstance(rz, str) or not rz.strip(): continue
        if idioma_consigna(r, os.path.dirname(f)) != "es": continue
        casa = r["id_modelo"]; tot[casa] += 1
        w = re.findall(r"[\wáéíóúñü']+", rz.strip())[:2]
        ini[casa][" ".join(w).lower()] += 1
        dec[casa][0] += bool(DEC.search(rz)); dec[casa][1] += 1
        entrada = (r.get("sistema") or "") + " " + str(r.get("usuario") or "") + " " + str(r.get("historial") or "")
        if re.search(r"rioplatense|voseo", entrada, re.I): continue
        c, *_ = clasificar(rz)
        if c in ("es", "en", "mixto"):
            fam = ("Anthropic" if casa.startswith("claude") else "xAI" if casa.startswith("grok") else "Mistral" if casa.startswith("mistral") else "chinas")
            hit = any(p.search(rz) for p in MARCAS.values())
            for k in (casa, "FAMILIA " + fam, "TODAS"):
                nota[k][c][0] += hit; nota[k][c][1] += 1
print("Primeras dos palabras del razonamiento (consigna en castellano), las cuatro más comunes por casa:")
for casa in sorted(tot, key=lambda c: -tot[c]):
    print(f"  {casa:30} {tot[casa]:4d}  " + " | ".join(f"{k} {v} ({100*v/tot[casa]:.0f} %)" for k, v in ini[casa].most_common(4)))
print("\nRazonamientos que nombran la decisión de contestar en castellano ('answer in Spanish', 'responder en castellano'):")
for casa in sorted(dec, key=lambda c: -dec[c][0] / dec[c][1]):
    a, n = dec[casa]; print(f"  {casa:30} {a:4d}/{n:4d} {100*a/n:5.1f} %")
print("\nNotan el voseo (rioplatense / voseo / argentino como habla), según el idioma del razonamiento:")
print(f"  {'casa / familia':30} " + "  ".join(f"{c:>18}" for c in ("es", "en", "mixto")))
for k in sorted(nota):
    print(f"  {k:30} " + "  ".join(f"{nota[k][c][0]:5d}/{nota[k][c][1]:<5d}{(100*nota[k][c][0]/nota[k][c][1] if nota[k][c][1] else 0):5.1f}%" for c in ("es", "en", "mixto")))
