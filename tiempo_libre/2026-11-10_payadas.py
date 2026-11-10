"""Lee las seis sextinas de instancias_frescas.md, cuenta cada verso con silabas.py (cuenta
manual y cuenta de lector), coteja con la cuenta que declaró cada instancia, y revisa la rima
(consonante: desde la vocal tónica hasta el final; asonante: solo las vocales).
Escribe salida_payadas.txt.  Uso: python3 payadas.py
"""
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import silabas  # noqa: E402


def ruta(nombre):
    for cand in (nombre, "2026-11-10_" + nombre):
        p = os.path.join(AQUI, cand)
        if os.path.exists(p):
            return p
    return os.path.join(AQUI, nombre)


def terminacion(palabra):
    """Lo que rima: desde la vocal tónica hasta el final (consonante) y sus vocales (asonante)."""
    w = silabas._norm(palabra)
    f = silabas._fono(w)
    grupos = list(re.finditer(r"[aeiouáéíóúü]+", f))
    pos = silabas.acento(w)          # 1 aguda, 2 llana, 3 esdrújula
    # tónica: contando núcleos desde el final
    nucleos = []      # posición de cada núcleo: la vocal fuerte (o la única) de cada sílaba
    for m in grupos:
        g = m.group()
        fuertes = [m.start() + j for j, c in enumerate(g) if c in silabas.FUERTES]
        nucleos.extend(fuertes if fuertes else [m.start()])
    if not nucleos:
        return "", ""
    i = nucleos[-pos] if pos <= len(nucleos) else nucleos[0]
    cola = f[i:]
    quitar = str.maketrans("áéíóú", "aeiou")
    cons = cola.translate(quitar)
    ason = "".join(c for c in cons if c in "aeiou")
    # en la asonancia, la vocal débil de un diptongo no cuenta (ai→a); simplificación: quedarse con las fuertes si hay
    return cons, ason


def leer():
    md = open(ruta("instancias_frescas.md"), encoding="utf-8").read()
    bloques = re.findall(r"### (\w+) \((medida|tiempo); agente (\w+)\)\n\n(.*?)\n\nSílabas: ([0-9, ]+)", md, re.S)
    out = []
    for clave, consigna, agente, texto, decl in bloques:
        versos = [v.strip() for v in texto.strip().splitlines() if v.strip()]
        out.append((clave, consigna, agente, versos, [int(x) for x in decl.replace(" ", "").split(",")]))
    return out


def main():
    sal = []
    tot = {"versos": 0, "manual8": 0, "lector8": 0, "decl8": 0, "coinciden": 0}
    for clave, consigna, agente, versos, decl in leer():
        sal.append("== %s (%s)" % (clave, consigna))
        finales = []
        for k, v in enumerate(versos):
            d = silabas.detalle(v)
            pos = silabas.posibles(v)
            lector = 8 if 8 in pos else d["silabas"]
            ultima = d["palabras"][-1][0]
            finales.append(terminacion(ultima))
            tot["versos"] += 1
            tot["manual8"] += d["silabas"] == 8
            tot["lector8"] += lector == 8
            tot["decl8"] += decl[k] == 8
            tot["coinciden"] += decl[k] == d["silabas"]
            sal.append("  v%d manual %d lector %d declarado %d  %s   [%s; sinalefas %d; ajuste %+d]" % (
                k + 1, d["silabas"], lector, decl[k], v,
                " ".join("%s=%d" % x for x in d["palabras"]), d["sinalefas"], d["ajuste"]))
        c = [f[0] for f in finales]
        a = [f[1] for f in finales]
        r236 = "consonante" if c[1] == c[2] == c[5] else ("asonante" if a[1] == a[2] == a[5] else "NO")
        r45 = "consonante" if c[3] == c[4] else ("asonante" if a[3] == a[4] else "NO")
        suelto = "suelto" if c[0] not in (c[1], c[3]) else "RIMA (no debería)"
        sal.append("  rima 2-3-6: %s (%s / %s / %s); rima 4-5: %s (%s / %s); v1 %s (%s)" % (
            r236, c[1], c[2], c[5], r45, c[3], c[4], suelto, c[0]))
    sal.append("")
    sal.append("Total: %(versos)d versos; ocho con la cuenta manual %(manual8)d; ocho como lector %(lector8)d; "
               "declarados ocho %(decl8)d; declaración igual a la cuenta manual %(coinciden)d" % tot)
    open(os.path.join(AQUI, "salida_payadas.txt"), "w", encoding="utf-8").write("\n".join(sal) + "\n")
    print("\n".join(sal))


if __name__ == "__main__":
    main()
