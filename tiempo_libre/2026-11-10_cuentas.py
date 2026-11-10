"""Lee dibujos/*.svg y lineas.json y escribe cuentas.json y salida_cuentas.txt: para cada dibujo,
qué dice la declaración (mate, poncho, sombrero, facón, caballo, ombú, lazo, boleadoras, rastra,
pañuelo, espuelas, alambrado, sol, atardecer, luna, estrellas, Cruz del Sur) y, del código, dónde
está el disco más grande del cielo (sol o luna: centro y radio) y el número de caracteres.
Uso: python3 cuentas.py
"""
import json
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))


def ruta(nombre):
    for cand in (nombre, "2026-11-10_" + nombre):
        p = os.path.join(AQUI, cand)
        if os.path.exists(p):
            return p
    return os.path.join(AQUI, nombre)


PALABRAS = {
    "mate": r"\bmate\b|马黛茶",
    "poncho": r"poncho|披风",
    "sombrero": r"sombrero|chambergo|hat|宽檐帽",
    "facón": r"fac[óo]n|cuchillo|短刀",
    "caballo": r"caballo|horse|马\b|一匹",
    "ombú": r"omb[úu]|翁布",
    "lazo": r"\blazo\b|套索",
    "boleadoras": r"boleadoras",
    "rastra": r"rastra|monedas|coin|银币",
    "pañuelo": r"pa[ñn]uelo|neckerchief|红巾",
    "espuelas": r"espuela|spur|马刺",
    "alambrado": r"alambrado|fence",
    "bigote": r"bigote|mustache|胡",
    "sol": r"\bsol\b|\bsun\b|夕阳|太阳",
    "atardecer / anochecer": r"atardecer|anochecer|sunset|黄昏|夕阳|noche",
    "luna": r"\bluna\b|\bmoon\b",
    "estrellas / cielo nocturno": r"estrella|cielo nocturno|star",
    "Cruz del Sur": r"Cruz del Sur",
}


def disco(svg, horizonte=250):
    """El círculo claro (relleno #f… o degradado) de radio mayor con centro arriba del horizonte: sol o luna, con su halo si lo tiene."""
    mejor = None
    for m in re.finditer(r'<circle[^>]*cx="([\d.]+)"[^>]*cy="([\d.]+)"[^>]*r="([\d.]+)"[^>]*fill="(#f|url)', svg):
        cx, cy, r = (float(x) for x in m.groups()[:3])
        if cy < horizonte and r >= 15 and (mejor is None or r > mejor[2]):
            mejor = (cx, cy, r)
    return mejor


def main():
    lineas = json.load(open(ruta("lineas.json"), encoding="utf-8"))
    out = {}
    tabla = []
    for clave in ("g1", "g2", "g3", "g4", "x1", "x2"):
        svg = open(os.path.join(AQUI, "dibujos", clave + ".svg"), encoding="utf-8").read()
        decl = lineas[clave]["linea"]
        bits = {k: bool(re.search(v, decl, re.I)) for k, v in PALABRAS.items()}
        d = disco(svg)
        out[clave] = {"consigna": lineas[clave]["consigna"], "caracteres": len(svg.strip()), "disco": d, "declara": bits}
        tabla.append("%s (%s): %d caracteres; disco mayor del cielo en x=%s y=%s r=%s; declara: %s" % (
            clave, lineas[clave]["consigna"], len(svg.strip()),
            d[0] if d else "-", d[1] if d else "-", d[2] if d else "-",
            ", ".join(k for k, v in bits.items() if v)))
    json.dump(out, open(os.path.join(AQUI, "cuentas.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tot = {k: sum(1 for c in out.values() if c["declara"][k]) for k in PALABRAS}
    tabla.append("")
    tabla.append("En cuántas de las seis declaraciones: " + ", ".join("%s %d" % kv for kv in tot.items()))
    open(os.path.join(AQUI, "salida_cuentas.txt"), "w", encoding="utf-8").write("\n".join(tabla) + "\n")
    print("\n".join(tabla))


if __name__ == "__main__":
    main()
