#!/usr/bin/env python3
"""Lo que cobra el libro cerrado: los tokens de entrada que cada proveedor informó por las
consignas de dibujo del repositorio (corridas/dibujos*, primera llamada de cada corrida:
sistema + consigna, sin nada más), comparados con lo que cuentan catorce tokenizadores
abiertos sobre el mismo texto. Tiempo libre, 21/10/2026. Solo lee el clon; no llama a nadie.

Uso: python3 libro.py <ruta al clon de proyectos-de-ley> rutas.json > salida_libro.txt
"""
import sys, json, glob, collections, statistics
sys.path.insert(0, ".")
from banderas import cargar, n, vocab

RAIZ = sys.argv[1]
TOKS = cargar(json.load(open(sys.argv[2])))
ORDEN = sorted(TOKS, key=lambda k: vocab(TOKS[k]))

# 1. Juntar las primeras llamadas de cada dibujo
llam = []
for f in glob.glob(f"{RAIZ}/corridas/dibujos*/*/*/llamadas.jsonl"):
    partes = f.split("/")
    carpeta, consigna, casa_rep = partes[-4], partes[-3], partes[-2]
    idioma = {"dibujos": "es", "dibujos_en": "en", "dibujos_zh": "zh"}[carpeta]
    for line in open(f):
        d = json.loads(line)
        if d.get("ronda") == 1 and d.get("tipo") == "dibujo" and d.get("tokens_entrada") is not None:
            llam.append(dict(modelo=d["id_modelo"], proveedor=d["proveedor"], servido=d.get("servido_por"),
                             consigna=consigna, idioma=idioma, texto=(d["sistema"] or "") + (d["usuario"] or ""),
                             sistema=d["sistema"] or "", usuario=d["usuario"] or "", tokens=d["tokens_entrada"],
                             razona=d.get("razonamiento_pedido"), fecha=d["fecha_utc"]))
print(f"{len(llam)} primeras llamadas de dibujo con tokens_entrada, de {len(set(l['modelo'] for l in llam))} casas")

# 2. ¿El mismo texto da siempre el mismo número en la misma casa?
print("\n== 1. Mismo texto, misma casa: ¿mismo número? (casas con algún texto repetido) ==")
por = collections.defaultdict(lambda: collections.defaultdict(list))
for l in llam:
    por[l["modelo"]][(l["texto"], l["razona"])].append(l["tokens"])
inconsist = 0
for m in sorted(por):
    reps = {k: v for k, v in por[m].items() if len(v) > 1}
    dif = {k: v for k, v in reps.items() if len(set(v)) > 1}
    if dif:
        inconsist += 1
        ej = next(iter(dif.items()))
        print(f"   {m:34s} {len(reps)} textos repetidos, {len(dif)} con números distintos; ej.: {sorted(ej[1])}")
print(f"   casas con algún texto repetido que dio números distintos: {inconsist}")

# 3. Por casa: ajuste contra cada tokenizador abierto (tokens = c + n_T(sistema) + n_T(usuario))
print("\n== 2. Por casa: qué tokenizador abierto predice mejor los tokens informados (c = sobrecarga fija estimada; error = mediana de |residuo|) ==")
print("   (solo casas con 6 textos distintos o más)")
resumen = {}
for m in sorted(por):
    textos = {}
    for (texto, razona), v in por[m].items():
        textos[texto] = statistics.median(v)
    if len(textos) < 6:
        continue
    prov = next(l["proveedor"] for l in llam if l["modelo"] == m)
    serv = collections.Counter(l["servido"] for l in llam if l["modelo"] == m).most_common(1)[0][0]
    mejor = None
    fila = []
    for T in ORDEN:
        tok = TOKS[T]
        pred = {t: n(tok, t) for t in textos}
        resid = [textos[t] - pred[t] for t in textos]
        c = statistics.median(resid)
        err = statistics.median(abs(r - c) for r in resid)
        maxerr = max(abs(r - c) for r in resid)
        fila.append((T, c, err, maxerr))
        if mejor is None or (err, maxerr) < (mejor[2], mejor[3]):
            mejor = (T, c, err, maxerr)
    resumen[m] = (prov, serv, len(textos), mejor, fila)
    exactos = [f"{T}(c={c:+.0f})" for T, c, err, mx in fila if err == 0 and mx == 0]
    print(f"   {m:34s} {prov:17s} {str(serv):18s} textos {len(textos):3d}  mejor {mejor[0]:14s} c={mejor[1]:+6.1f} err={mejor[2]:.1f} max={mejor[3]:.0f}"
          + (f"   EXACTO: {', '.join(exactos)}" if exactos else ""))

# 4. La misma consigna en tres idiomas: autorretrato y libre (es/en/zh), tokens informados por casa
print("\n== 3. La misma consigna en castellano / inglés / chino: tokens de entrada informados (mediana si hay repeticiones) ==")
for consigna in ("autorretrato", "libre"):
    print(f"   -- {consigna} --")
    tabla = collections.defaultdict(dict)
    for l in llam:
        if l["consigna"] == consigna:
            tabla[l["modelo"]].setdefault(l["idioma"], []).append(l["tokens"])
    for m in sorted(tabla):
        fila = tabla[m]
        if len(fila) >= 2:
            s = "  ".join(f"{i}={statistics.median(fila[i]):.0f}" for i in ("es", "en", "zh") if i in fila)
            es = statistics.median(fila["es"]) if "es" in fila else None
            en = statistics.median(fila["en"]) if "en" in fila else None
            r = f"  es/en={es/en:.2f}" if es and en else ""
            print(f"      {m:34s} {s}{r}")
    # lo que dicen los tokenizadores abiertos del mismo texto (sin sobrecarga)
    ej = {}
    for l in llam:
        if l["consigna"] == consigna and l["idioma"] not in ej:
            ej[l["idioma"]] = l["texto"]
    print("      abiertos (sistema+consigna, sin sobrecarga):")
    for T in ORDEN:
        s = "  ".join(f"{i}={n(TOKS[T], ej[i])}" for i in ("es", "en", "zh") if i in ej)
        print(f"      {T:34s} {s}" + (f"  es/en={n(TOKS[T], ej['es'])/n(TOKS[T], ej['en']):.2f}" if "es" in ej and "en" in ej else ""))

# 5. Diferencias dentro de cada casa (sacan la sobrecarga): costo de un pedazo de texto en el libro cerrado
print("\n== 4. Diferencias dentro de la misma casa, castellano: tokens(consigna) - tokens(casa). Es el costo de lo que cambia en el texto, sin sobrecarga ==")
pares = [("casa_inexistente", "casa", "' que no exista'"), ("persona", "casa", "'persona' en vez de 'casa'"),
         ("letra", "casa", "'letra' en vez de 'casa'"), ("nada", "casa", "'la nada' en vez de 'una casa'"),
         ("mundo", "casa", "'cómo ves el mundo hoy' en vez de 'una casa'")]
tab = collections.defaultdict(dict)
for l in llam:
    if l["idioma"] == "es":
        tab[l["modelo"]].setdefault((l["consigna"], l["razona"]), []).append(l["tokens"])
def val(m, c):
    xs = [v for (cc, rz), v in tab[m].items() if cc == c]
    xs = [x for v in xs for x in v]
    return statistics.median(xs) if xs else None
print("   " + " " * 34 + "  ".join(f"{p[2][:26]:>26s}" for p in pares))
for m in sorted(tab):
    fila = []
    for a, b, _ in pares:
        va, vb = val(m, a), val(m, b)
        fila.append(f"{va - vb:+26.0f}" if va is not None and vb is not None else f"{'—':>26s}")
    if any(f.strip() != "—" for f in fila):
        print(f"   {m:34s}" + "  ".join(fila))
print("   abiertos:")
VOS = {"casa": "Dibujá una casa.", "casa_inexistente": "Dibujá una casa que no exista.", "persona": "Dibujá una persona.",
       "letra": "Dibujá una letra.", "nada": "Dibujá la nada.", "mundo": "Dibujá cómo ves el mundo hoy."}
for T in ORDEN:
    print(f"   {T:34s}" + "  ".join(f"{n(TOKS[T], VOS[a]) - n(TOKS[T], VOS[b]):+26d}" for a, b, _ in pares))
