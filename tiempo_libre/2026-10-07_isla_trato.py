"""En la isla los modelos se hablan entre ellos. ¿De vos, de tú, de ustedes, de vosotros?

    python3 isla_trato.py /ruta/a/isla-constituyente

Solo lee corridas/*/llamadas.jsonl (turnos en castellano) y cuenta palabras.
"""
import collections
import glob
import json
import os
import re
import sys

import voseo as v

RE_PAL = re.compile(r"[a-záéíóúüñ]+", re.I)
VOSOTROS = {"vosotros", "vosotras", "os", "vuestro", "vuestra", "vuestros", "vuestras"}
RE_2PL = re.compile(r"(áis|éis)$")      # tenéis, estáis, queréis…
NO_2PL = {"seis", "dieciséis", "veintiséis"}


def main():
    raiz = sys.argv[1]
    por = collections.defaultdict(collections.Counter)
    for f in sorted(glob.glob(os.path.join(raiz, "corridas", "*", "llamadas.jsonl"))):
        cfg = json.load(open(os.path.join(os.path.dirname(f), "config.json"), encoding="utf-8"))
        if cfg.get("idioma") != "es":
            continue
        for linea in open(f, encoding="utf-8"):
            if not linea.strip():
                continue
            j = json.loads(linea)
            if j.get("tipo") != "turno" or j.get("error") or not isinstance(j.get("respuesta"), str):
                continue
            m = v.corto(j["modelo_pedido"])
            c = por[m]
            c["turnos"] += 1
            palabras = RE_PAL.findall(j["respuesta"].lower())
            k = v.contar(j["respuesta"])
            c["V"] += k["V"]
            c["T"] += k["T"]
            c["turnos_V"] += bool(k["V"])
            c["turnos_T"] += bool(k["T"])
            ust = sum(w == "ustedes" for w in palabras)
            vst = sum(w in VOSOTROS or bool(RE_2PL.search(w) and w not in NO_2PL) for w in palabras)
            c["ustedes"] += ust
            c["vosotros"] += vst
            c["turnos_vosotros"] += bool(vst)
            c["aca"] += sum(w in ("acá", "allá") for w in palabras)
            c["aqui"] += sum(w in ("aquí", "allí") for w in palabras)
    print(f"{'casa':24}{'turnos':>7}{'  V':>6}{'  T':>5}{' %V':>5}{' t.con V':>9}{' t.con T':>9}"
          f"{' ustedes':>9}{' vosotros':>10}{' acá/allá':>10}{' aquí/allí':>11}")
    tot = collections.Counter()
    for m, c in sorted(por.items(), key=lambda kv: -(kv[1]["V"] / max(1, kv[1]["V"] + kv[1]["T"]))):
        tot.update(c)
        pv = 100 * c["V"] / (c["V"] + c["T"]) if c["V"] + c["T"] else float("nan")
        print(f"{m:24}{c['turnos']:7}{c['V']:6}{c['T']:5}{pv:5.0f}{c['turnos_V']:9}{c['turnos_T']:9}"
              f"{c['ustedes']:9}{c['vosotros']:10}{c['aca']:10}{c['aqui']:11}")
    c = tot
    print(f"{'TOTAL':24}{c['turnos']:7}{c['V']:6}{c['T']:5}{100 * c['V'] / max(1, c['V'] + c['T']):5.0f}"
          f"{c['turnos_V']:9}{c['turnos_T']:9}{c['ustedes']:9}{c['vosotros']:10}{c['aca']:10}{c['aqui']:11}")


if __name__ == "__main__":
    main()
