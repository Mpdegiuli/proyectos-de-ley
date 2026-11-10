"""Saca los versos de las dos partes del Martín Fierro de los textos de Project Gutenberg
(14765, El gaucho Martín Fierro; 15066, La vuelta de Martín Fierro; están en GitHub como
GITenberg/El-Gaucho-Mart-n-Fierro_14765 y GITenberg/La-Vuelta-de-Mart-n-Fierro_15066,
archivos 14765-8.txt y 15066-8.txt en ISO-8859-1), los cuenta con silabas.py y escribe:
  fierro_versos.tsv   parte, canto, estrofa, verso, sílabas (manual), sílabas (gauchesco), texto
  salida_fierro.txt   la distribución por parte y por canto con las dos cuentas, y los versos
                      que no dan ocho de ninguna manera. Tres cuentas: la manual (sin licencias),
                      la gauchesca (toda 'ía', 'ío' y '-ao' en una sílaba) y la de lector (cada una
                      de esas contracciones a elección, como las lee un lector: da ocho si se puede)
Uso: python3 fierro.py 14765-8.txt 15066-8.txt
"""
import collections
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import silabas  # noqa: E402

ETIQUETAS = {"MARTÍN FIERRO", "EL MORENO", "A OTRO", "LA PENITENCIARIA", "FIN",
             "EL HIJO MAYOR DE MARTÍN FIERRO", "EL HIJO SEGUNDO DE MARTÍN FIERRO", "PICARDÍA"}
RE_ROMANO = re.compile(r"^([IVXL]+)(\.| -)?\s*(.*)$")


def leer(ruta):
    t = open(ruta, encoding="latin-1").read().replace("\r", "")
    return t.splitlines()


def versos(lineas, parte, desde, hasta):
    canto, estrofa, k = None, None, 0
    out = []
    for l in lineas[desde:hasta]:
        s = l.strip()
        if not s or s.startswith("*"):
            continue
        if s.isdigit():
            estrofa, k = int(s), 0
            continue
        m = RE_ROMANO.match(s)
        if m and (m.group(2) or not m.group(3)):
            canto = m.group(1)
            continue
        if s in ETIQUETAS:
            continue
        k += 1
        out.append((parte, canto, estrofa, k, s))
    return out


def main(ida, vuelta):
    li = leer(ida)
    lv = leer(vuelta)
    a = next(i for i, l in enumerate(li) if l.startswith("Aquí me pongo"))
    b = next(i for i, l in enumerate(li) if l.startswith("End of Project Gutenberg"))
    c = next(i for i, l in enumerate(lv) if l.strip() == "I")
    d = next(i for i, l in enumerate(lv) if l.strip() == "FIN")
    vs = versos(li, "Ida", a - 3, b) + versos(lv, "Vuelta", c, d)
    filas = []
    for parte, canto, estrofa, k, texto in vs:
        silabas.GAUCHO = False
        m = silabas.contar(texto)
        silabas.GAUCHO = True
        g = silabas.contar(texto)
        silabas.GAUCHO = False
        al = 8 if 8 in silabas.posibles(texto) else (m if abs(m - 8) <= abs(g - 8) else g)
        filas.append((parte, canto, estrofa, k, m, g, al, texto))
    with open(os.path.join(AQUI, "fierro_versos.tsv"), "w", encoding="utf-8") as f:
        f.write("parte\tcanto\testrofa\tverso\tsilabas\tsilabas_gaucho\tsilabas_lector\ttexto\n")
        for fila in filas:
            f.write("\t".join(str(x) for x in fila) + "\n")
    sal = []
    for parte in ("Ida", "Vuelta", "Total"):
        sel = [f for f in filas if parte == "Total" or f[0] == parte]
        n = len(sel)
        for nombre, col in (("manual", 4), ("gauchesco", 5), ("lector", 6)):
            dist = collections.Counter(f[col] for f in sel)
            ocho = dist[8]
            sal.append("%s, cuenta %s: %d versos; 8 sílabas %d (%.1f %%); distribución %s" % (
                parte, nombre, n, ocho, 100.0 * ocho / n, dict(sorted(dist.items()))))
    estrofas = collections.Counter()
    for parte, canto, estrofa, k, s, g, al, texto in filas:
        estrofas[(parte, estrofa)] = max(estrofas[(parte, estrofa)], k)
    tam = collections.Counter(estrofas.values())
    sal.append("estrofas: %d; por tamaño %s" % (len(estrofas), dict(sorted(tam.items()))))
    sal.append("")
    sal.append("Por canto (versos, % de ocho con la cuenta manual / gauchesca / de lector):")
    for parte in ("Ida", "Vuelta"):
        cantos = []
        for canto in dict.fromkeys(f[1] for f in filas if f[0] == parte):
            sel = [f for f in filas if f[0] == parte and f[1] == canto]
            cantos.append("%s %d/%.0f/%.0f/%.0f" % (canto, len(sel), 100.0 * sum(1 for f in sel if f[4] == 8) / len(sel),
                                                 100.0 * sum(1 for f in sel if f[5] == 8) / len(sel),
                                                 100.0 * sum(1 for f in sel if f[6] == 8) / len(sel)))
        sal.append("  %s: %s" % (parte, ", ".join(cantos)))
    sal.append("")
    pal = collections.Counter()
    for parte, canto, estrofa, k, s, g, al, texto in filas:
        if s != 8 and al == 8:
            for p in re.findall(r"[a-záéíóúüñ]+", texto.lower()):
                if re.search(r"í[aeo]|ao$|aos$", p):
                    pal[p] += 1
    sal.append("Palabras que arreglan el verso con la cuenta gauchesca (las 40 más frecuentes): %s" % ", ".join(
        "%s %d" % x for x in pal.most_common(40)))
    sal.append("")
    sal.append("Hiato o contracción, palabra por palabra: en los versos donde esa es la única palabra con ía/íe/ío "
               "y no hay terminación -ao, cuántos dan ocho con la cuenta manual (hiato) y cuántos solo contrayendo "
               "esa palabra (contraída); las 16 más frecuentes:")
    hi, co = collections.Counter(), collections.Counter()
    for parte, canto, estrofa, k, s, g, al, texto in filas:
        ws = [w for w in re.findall(r"[a-záéíóúüñ]+", texto.lower()) if re.search(r"í[aeo]", w)]
        if len(ws) != 1 or re.search(r"\b\w+aos?\b", texto.lower()):
            continue
        w = ws[0]
        if s == 8:
            hi[w] += 1
        else:
            t2 = re.sub(r"\b" + re.escape(w) + r"\b", re.sub(r"í([aeo])", r"i\1", w), texto.lower())
            if silabas.contar(t2) == 8:
                co[w] += 1
    tot = hi + co
    for w, n in tot.most_common(16):
        sal.append("  %s: hiato %d, contraída %d" % (w, hi[w], co[w]))
    sal.append("")
    sal.append("Versos que no dan ocho ni como lector (manual/gauchesca/lector):")
    for parte, canto, estrofa, k, s, g, al, texto in filas:
        if al != 8:
            sal.append("  %d/%d/%d  %s %s est. %s v. %d: %s" % (s, g, al, parte, canto, estrofa, k, texto))
    open(os.path.join(AQUI, "salida_fierro.txt"), "w", encoding="utf-8").write("\n".join(sal) + "\n")
    print("\n".join(sal[:10]))
    print("... no dan ocho: %d con la cuenta manual, %d con la gauchesca, %d como lector; ver salida_fierro.txt" % (
        sum(1 for f in filas if f[4] != 8), sum(1 for f in filas if f[5] != 8), sum(1 for f in filas if f[6] != 8)))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
