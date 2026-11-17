#!/usr/bin/env python3
"""voseo_razon.py — qué casas, en su razonamiento guardado, se dan cuenta de que les hablan de vos. Cuenta, entre los
razonamientos con consigna en castellano, los que nombran el voseo, lo rioplatense, o lo argentino/uruguayo como
rasgo del habla (no como tema: "ley argentina" no cuenta). Deja afuera las llamadas cuyo propio mensaje (sistema, usuario o
historial) ya decía "rioplatense" o "voseo": 32 del tercer turno de los derechos de C-MARE, cuyo historial trae
respuestas anteriores de las casas, y 2 del reconocimiento. Lee
corridas/**/llamadas.jsonl; no escribe en el repositorio.    python3 voseo_razon.py /ruta/al/clon [--ejemplos]"""
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
MARCAS = {
 "rioplatense": re.compile(r"rioplatense|r[ií]o de la plata|platense", re.I),
 "voseo": re.compile(r"\bvoseo\b|\bvoseante|\bvos form|\bvos\b[^.\n]{0,40}\b(form|conjug|trat|imperativ|dialect|pronoun|pronombre)|\b(form|conjug|imperativ|dialect|pronoun|pronombre|usa|uses|using|use|used|emplea|utiliza)\w*[^.\n]{0,40}\b(\"|«|')?vos(\"|»|')?\b", re.I),
 "argentino como habla": re.compile(r"argentin\w*[^.\n]{0,50}\b(spanish|español|castellano|dialect|tone|tono|accent|acento|style|estilo|slang|usage|variety|variante|variedad)|(spanish|español|castellano|dialect|tone|tono|accent|acento|style|estilo|slang|variety|variante|variedad)\w*[^.\n]{0,50}argentin|\buruguay\w*[^.\n]{0,40}(spanish|español|castellano|dialect)|(spanish|español|castellano|dialect)\w*[^.\n]{0,40}uruguay", re.I),
}
FAM = lambda c: ("Anthropic" if c.startswith("claude") else "xAI" if c.startswith("grok") else "Mistral" if c.startswith("mistral")
                 else "chinas")


def main():
    repo = sys.argv[1]; ejemplos = "--ejemplos" in sys.argv

    cuenta = collections.defaultdict(collections.Counter); total = collections.Counter(); ej = {}
    excluidas = 0
    for f in sorted(glob.glob(os.path.join(repo, "corridas", "**", "llamadas.jsonl"), recursive=True)):
        for l in open(f, encoding="utf-8"):
            try: r = json.loads(l)
            except json.JSONDecodeError: continue
            rz = r.get("razonamiento")
            if not isinstance(rz, str) or not rz.strip(): continue
            if idioma_consigna(r, os.path.dirname(f)) != "es": continue
            entrada = (r.get("sistema") or "") + " " + str(r.get("usuario") or "") + " " + str(r.get("historial") or "")
            if re.search(r"rioplatense|voseo", entrada, re.I): excluidas += 1; continue
            casa = r["id_modelo"]; total[casa] += 1
            hit = False
            for k, p in MARCAS.items():
                m = p.search(rz)
                if m:
                    cuenta[casa][k] += 1; hit = True
                    ej.setdefault((casa, k), rz[max(0, m.start()-100):m.end()+100].replace("\n", " "))
            if hit: cuenta[casa]["alguna"] += 1
    print(f"razonamientos con consigna en castellano: {sum(total.values())} (excluidos {excluidas} cuyo mensaje ya decía rioplatense o voseo)\n")
    print(f"{'casa':30} {'n':>5} {'nota':>5} {'%':>6}   {'riopl.':>6} {'voseo':>6} {'arg/uru':>7}")
    fam = collections.defaultdict(lambda: [0, 0])
    for casa in sorted(total, key=lambda c: -cuenta[c]["alguna"] / total[c]):
        c = cuenta[casa]; fam[FAM(casa)][0] += c["alguna"]; fam[FAM(casa)][1] += total[casa]
        print(f"{casa:30} {total[casa]:5d} {c['alguna']:5d} {100*c['alguna']/total[casa]:6.1f}   {c['rioplatense']:6d} {c['voseo']:6d} {c['argentino como habla']:7d}")
    print()
    for k, (a, n) in sorted(fam.items(), key=lambda kv: -kv[1][0]/kv[1][1]):
        print(f"{k:10} {a:5d} de {n:5d}  {100*a/n:5.1f} %")
    if ejemplos:
        print("\nEjemplos:")
        for (casa, k), e in sorted(ej.items()): print(f"- {casa} [{k}]: …{e}…")


if __name__ == "__main__":
    main()
