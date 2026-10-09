"""Las cuentas chicas del cuaderno del 7/10/2026, todas sobre lo mismo que cuenta voseo.py.

    python3 extras.py /ruta/a/proyectos-de-ley
"""
import collections
import re
import sys
from math import comb

import voseo as v
from cargar import llamadas

CHICAS = {"claude-haiku-4-5", "gpt-4o", "gpt-4o-mini", "mistral-medium-3.5"}
AMOR = ("sondeo_docilidad", "sondeo_mudanza", "sondeo_pareja")
RE_PAL = re.compile(r"[a-záéíóúüñ]+", re.I)
RE_COMILLAS = re.compile(r"«[^»]*»|“[^”]*”|\"[^\"\n]*\"|'[^'\n]{0,400}'")
DE_VOS = v.PRES_VOS | v.IMP_VOS | v.SUBJ_VOS | {"vos"}
DE_TU = v.PRES_TU | v.IMP_TU | {"tú"}


def fisher(a, b, c, d):
    n, r1, c1 = a + b + c + d, a + b, a + c
    p0 = comb(r1, a) * comb(n - r1, c1 - a) / comb(n, c1)
    return sum(px for x in range(max(0, c1 - (n - r1)), min(r1, c1) + 1)
               if (px := comb(r1, x) * comb(n - r1, c1 - x) / comb(n, c1)) <= p0 * (1 + 1e-9))


def main():
    L = [x for x in llamadas(sys.argv[1])]
    for x in L:
        x["m"] = v.corto(x["modelo"])
        x["c"] = v.contar(x["respuesta"])
        x["clase"] = v.clase(x["c"])
        x["trato"] = v.trato_consigna(x["sistema"], x["usuario"])
    vos = [x for x in L if x["trato"] == "vos"]

    print("1. LAS CUATRO CHICAS Y EL RESTO (consigna de vos)")
    for nombre, sel in (("chicas", [x for x in vos if x["m"] in CHICAS]),
                        ("resto ", [x for x in vos if x["m"] not in CHICAS])):
        k = collections.Counter(x["clase"] for x in sel)
        V, T = sum(x["c"]["V"] for x in sel), sum(x["c"]["T"] for x in sel)
        print(f"   {nombre}: {len(sel)} respuestas; con marca {k['voseo'] + k['mixta'] + k['tuteo']}: "
              f"solo vos {k['voseo']}, mixtas {k['mixta']}, solo tú {k['tuteo']}; formas {V} de vos y {T} de tú "
              f"({100 * V / (V + T):.0f} % de vos)")
    def dos(sel):
        k = collections.Counter(x["clase"] for x in sel)
        return k["voseo"], k["tuteo"] + k["mixta"]
    a, b = dos([x for x in vos if x["m"] in CHICAS])
    c, d = dos([x for x in vos if x["m"] not in CHICAS])
    print(f"   Fisher (solo vos / con algún tú): {a}-{b} contra {c}-{d}, p = {fisher(a, b, c, d):.1e}"
          "  (las respuestas de una casa no son independientes: vale como orden de magnitud)")

    print("\n2. ¿SON LAS CUATRO ÚLTIMAS? (orden por % de formas de vos)")
    def orden(filtro=lambda x: True, texto=lambda x: x["respuesta"]):
        V, T = collections.Counter(), collections.Counter()
        for x in vos:
            if filtro(x):
                k = v.contar(texto(x))
                V[x["m"]] += k["V"]
                T[x["m"]] += k["T"]
        return sorted(((V[m] / (V[m] + T[m]), m) for m in set(V) | set(T) if V[m] + T[m]))
    variantes = [
        ("como en la tabla", {}),
        ("sacando todo lo que va entre comillas", {"texto": lambda x: RE_COMILLAS.sub(" ", x["respuesta"])}),
        ("sin pareja ni mudanza", {"filtro": lambda x: x["tipo"] not in ("sondeo_pareja", "sondeo_mudanza")}),
        ("solo los sondeos", {"filtro": lambda x: x["carpeta"] == "sondeos"}),
        ("todo menos los sondeos", {"filtro": lambda x: x["carpeta"] != "sondeos"}),
    ]
    for nombre, kw in variantes:
        r = orden(**kw)
        ult = [m for _, m in r[:4]]
        print(f"   {nombre:38} {len(r)} casas; últimas cuatro: {', '.join(ult)}"
              f"  -> {'sí' if set(ult) == CHICAS else 'no'}")
    # variante: de vos solo cuentan las formas que la casa no pudo copiar de la consigna
    V, T = collections.Counter(), collections.Counter()
    for x in vos:
        consigna = set(RE_PAL.findall((x["sistema"] + " " + x["usuario"]).lower()))
        for w in RE_PAL.findall(x["respuesta"].lower()):
            if w in DE_VOS and w not in consigna:
                V[x["m"]] += 1
            elif w in DE_TU:
                T[x["m"]] += 1
    r = sorted(((V[m] / (V[m] + T[m]), m) for m in set(V) | set(T) if V[m] + T[m]))
    ult = [m for _, m in r[:4]]
    print(f"   {'de vos, solo formas que no están en la consigna':38} {len(r)} casas; últimas cuatro: {', '.join(ult)}"
          f"  -> {'sí' if set(ult) == CHICAS else 'no'}")
    print(f"   Si el orden fuera al azar, que cuatro casas fijadas de antemano sean las cuatro últimas de 26: "
          f"1 en {comb(26, 4)}")

    print("\n3. LAS TRES CONSIGNAS DE AMOR, sin las chicas")
    for t in AMOR:
        sel = [x for x in vos if x["tipo"] == t and x["m"] not in CHICAS]
        k = collections.Counter(x["clase"] for x in sel)
        print(f"   {t:18} {len(sel)} casas: solo vos {k['voseo']}, mixtas {k['mixta']}, solo tú {k['tuteo']}, "
              f"no eligen {k['neutra']}; formas {sum(x['c']['V'] for x in sel)} de vos, "
              f"{sum(x['c']['T'] for x in sel)} de tú; 'con vos' {sum(x['c']['con_vos'] for x in sel)}, "
              f"'contigo' {sum(x['c']['contigo'] for x in sel)}")
    resto = [x for x in vos if x["m"] not in CHICAS]
    Tt = sum(x["c"]["T"] for x in resto)
    Ta = sum(x["c"]["T"] for x in resto if x["tipo"] in ("sondeo_pareja", "sondeo_mudanza"))
    print(f"   formas de tú del resto: {Tt}; en pareja y mudanza: {Ta}")
    print(f"   en todo el corpus: 'con vos' {sum(x['c']['con_vos'] for x in L)}, 'contigo' "
          f"{sum(x['c']['contigo'] for x in L)}, 'ti' {sum(x['c']['ti'] for x in L)}, "
          f"subjuntivo voseante {sum(x['c']['subj_vos'] for x in L)}")

    print("\n4. QUÉ FORMAS")
    cv, ct = collections.Counter(), collections.Counter()
    propias = total = si_vos = 0
    si_tu = collections.Counter()
    tu_por = collections.Counter()
    for x in vos:
        consigna = set(RE_PAL.findall((x["sistema"] + " " + x["usuario"]).lower()))
        ws = RE_PAL.findall(x["respuesta"].lower())
        for i, w in enumerate(ws):
            if w in DE_VOS:
                cv[w] += 1
                total += 1
                propias += w not in consigna
                si_vos += bool(i and ws[i - 1] == "si")
            elif w in DE_TU:
                ct[w] += 1
                g = "chicas" if x["m"] in CHICAS else "resto"
                tu_por[g] += 1
                si_tu[g] += bool(i and ws[i - 1] == "si")
    print("   de vos:", ", ".join(f"{w} {n}" for w, n in cv.most_common(14)))
    print("   de tú: ", ", ".join(f"{w} {n}" for w, n in ct.most_common(10)))
    print(f"   formas de vos distintas: {len(cv)}; que no están en la consigna de esa llamada: {propias} de {total}")
    print(f"   de tú después de 'si': chicas {si_tu['chicas']} de {tu_por['chicas']}, resto {si_tu['resto']} de {tu_por['resto']}; "
          f"de vos después de 'si': {si_vos} de {total}")

    print("\n5. LA QUE NO ELIGE")
    k = collections.Counter(x["clase"] for x in vos)
    print(f"   de {len(vos)} respuestas: sin segunda persona {k['sin']}, solo vos {k['voseo']}, mixtas {k['mixta']}, "
          f"solo tú {k['tuteo']}, segunda persona sin elegir {k['neutra']}")
    q = [x for x in vos if x["tipo"] == "sondeo_quien_sos" and x["clase"] != "sin"]
    kq = collections.Counter(x["clase"] for x in q)
    frases = collections.Counter()
    for x in vos:
        if x["tipo"] == "sondeo_quien_sos":
            for m in re.finditer(r"¿[^¿?]{0,60}ayudarte[^?]{0,20}\?", x["respuesta"]):
                frases[m.group(0).lower()] += 1
    todas_q = [x for x in vos if x["tipo"] == "sondeo_quien_sos"]
    con_frase = sum("¿en qué puedo ayudarte hoy?" in x["cruda"].lower() for x in todas_q)
    print(f"   ¿Quién sos? / ¿Qué sos?: {len(todas_q)} respuestas, {len(q)} con segunda persona; "
          f"no eligen {kq['neutra']}, de vos {kq['voseo']}, de tú {kq['tuteo']}, mixtas {kq['mixta']}")
    print(f"   respuestas con la oración '¿En qué puedo ayudarte hoy?': {con_frase}")
    print("   ", frases.most_common(3))
    fam = collections.defaultdict(lambda: [0, 0])
    for x in vos:
        if x["carpeta"] == "sondeos":
            f = v.familia(x["modelo"])
            fam[f][0] += 1
            fam[f][1] += x["clase"] != "sin"
    print("   sondeos, respuestas que le hablan a alguien, por laboratorio: "
          + "; ".join(f"{f} {k} de {n}" for f, (n, k) in sorted(fam.items(), key=lambda kv: -kv[1][1] / kv[1][0])))
    g = [x for x in vos if x["m"] == "gemini-3.1-pro" and x["clase"] != "sin"]
    print(f"   Gemini: {len(g)} respuestas con segunda persona, no elige en {sum(x['clase'] == 'neutra' for x in g)}")

    print("\n6. DE USTED (el ministro) Y ENTRE ELLAS (el debate)")
    u = [x for x in L if x["trato"] == "usted"]
    ku = collections.Counter(x["clase"] for x in u)
    print(f"   consigna de usted: {len(u)} respuestas; contestan de usted {ku['usted']}, de vos {ku['voseo']}, de tú {ku['tuteo']}")
    for x in u:
        if x["c"]["V"]:
            print("      de vos:", x["m"], [w for w in RE_PAL.findall(x["respuesta"].lower()) if w in DE_VOS])
    deb = collections.defaultdict(collections.Counter)
    for x in L:
        if x["carpeta"] == "debates":
            deb[x["m"]].update({"V": x["c"]["V"], "T": x["c"]["T"]})
    print("   debate en castellano:", {m: dict(c) for m, c in deb.items()})


if __name__ == "__main__":
    main()
