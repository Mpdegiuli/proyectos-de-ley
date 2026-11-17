#!/usr/bin/env python3
"""huella.py — las tres cuentas de la nota del mismo día del cuaderno del 16/11/2026, a partir de lo que Maia dijo
el 17/11: (1) en qué idioma vienen los resúmenes del pensamiento de los Gemini (los `_pensamiento.md` de la corrida
`conciencia/20261117-1528`, que todavía no están en el campo `razonamiento`); (2) Kimi en `quien_sos` y `sos_claude`:
con qué palabras empieza el razonamiento y a quién dice ser; (3) "oververbosity" en los razonamientos, por casa, y
si alguna consigna del repositorio dice "verbosity". Lee `corridas/`; no escribe en el repositorio.
  python3 huella.py /ruta/al/clon      (precisa idioma.py al lado, con o sin la fecha adelante del nombre)"""
import collections, glob, importlib.util, json, os, re, sys


def _vecino(nombre):
    aqui = os.path.dirname(os.path.abspath(__file__))
    for cand in [os.path.join(aqui, nombre + ".py")] + sorted(glob.glob(os.path.join(aqui, "*_" + nombre + ".py"))):
        if os.path.exists(cand):
            spec = importlib.util.spec_from_file_location(nombre, cand); mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod); return mod
    raise ImportError(nombre + ".py no está al lado de este script")


clasificar = _vecino("idioma").clasificar
repo = sys.argv[1]

print("1. Resúmenes del pensamiento de los Gemini (conciencia/20261117-1528), idioma por forma:")
cuenta = collections.Counter(); voseo = []
for f in sorted(glob.glob(os.path.join(repo, "corridas", "sondeos", "conciencia", "20261117-1528", "*", "*_pensamiento.md"))):
    t = open(f, encoding="utf-8").read()
    c, n, es, en, zh = clasificar(t)
    idi = f.split(os.sep)[-2]
    cuenta[(idi, c)] += 1
    m = re.search(r"[^.\n]*(voseo|rioplatense)[^.\n]*", t, re.I)
    if m:
        voseo.append((idi, os.path.basename(f), m.group(0).strip()))
    print(f"   {idi}  {os.path.basename(f):50} {c:5}  {n:4d} palabras  es={es:.2f} en={en:.2f}")
print("   total:", dict(cuenta))
for idi, f, frase in voseo:
    print(f"   nota el voseo: {idi} {f}: «{frase}»")

print("\n2. Kimi en quien_sos y sos_claude: primeras palabras del razonamiento y quién dice ser:")
PREG = re.compile(r"sos claude|are you claude|quién sos|who are you|qué sos|what are you", re.I)
tabla = collections.Counter(); ejemplos = []
for f in sorted(glob.glob(os.path.join(repo, "corridas", "sondeos", "*", "*", "*", "llamadas.jsonl"))):
    for l in open(f, encoding="utf-8"):
        try: r = json.loads(l)
        except json.JSONDecodeError: continue
        if not r["id_modelo"].startswith("kimi") or not PREG.search(str(r.get("usuario") or "")): continue
        rz = r.get("razonamiento") or ""
        if not rz.strip(): continue
        w = " ".join(re.findall(r"[\w']+", rz)[:2]).lower()
        reg = "we need" if w.startswith("we") else "I need" if w.startswith("i") else "the user" if w.startswith("the user") else w
        resp = r.get("respuesta") or ""
        dice = ("Claude" if re.search(r"\bclaude\b", resp, re.I) and not re.search(r"no soy claude|not claude|no,? no soy|i am not claude", resp, re.I)
                else "Kimi" if re.search(r"\bkimi\b", resp, re.I) else "otro")
        tabla[(r["id_modelo"], reg, dice)] += 1
for (casa, reg, dice), n in sorted(tabla.items()):
    print(f"   {casa:14} razonamiento empieza {reg!r:12} → dice ser {dice:7} {n:3d}")

print("\n3. 'oververbosity' en los razonamientos, por casa (y si alguna consigna lo dice):")
c = collections.Counter(); tot = collections.Counter(); vals = collections.Counter(); enprompt = 0; fechas = collections.defaultdict(list); ej = {}
for f in sorted(glob.glob(os.path.join(repo, "corridas", "**", "llamadas.jsonl"), recursive=True)):
    for l in open(f, encoding="utf-8"):
        try: r = json.loads(l)
        except json.JSONDecodeError: continue
        if re.search(r"verbosity", (r.get("sistema") or "") + str(r.get("usuario") or "") + str(r.get("historial") or ""), re.I):
            enprompt += 1
        rz = r.get("razonamiento") or ""
        if not rz.strip(): continue
        tot[r["id_modelo"]] += 1
        ms = re.findall(r"oververbosity(?:\s+for\s+(?:the\s+)?final\s+(?:answer|response))?\s*:?\s*(?:of\s*)?(\d+)?", rz, re.I)
        if ms:
            c[r["id_modelo"]] += 1; fechas[r["id_modelo"]].append(r.get("fecha_utc", "")[:10])
            for v in ms: vals[(r["id_modelo"], v or "sin número")] += 1
            ej.setdefault(r["id_modelo"], (f.replace(repo + os.sep, ""), re.search(r".{0,100}oververbosity.{0,80}", rz, re.I | re.S).group(0).replace("\n", " ")))
print(f"   llamadas cuya consigna (sistema, usuario, historial) dice 'verbosity': {enprompt} de todas")
for k, v in c.most_common():
    print(f"   {k:22} {v:4d} de {tot[k]:4d} razonamientos ({100*v/tot[k]:.1f} %)  del {min(fechas[k])} al {max(fechas[k])}")
print("   números que ponen:", ", ".join(f"{k[0]} → {k[1]}: {v}" for k, v in sorted(vals.items())))
for k, (f, e) in ej.items():
    print(f"   ejemplo {k} ({f}): …{e}…")
