"""Cuenta sílabas métricas de versos en castellano.

Reglas (las de los manuales, sin oído): sílabas por palabra según los grupos de vocales
(dos fuertes, hiato; fuerte y débil, diptongo; la débil con tilde es fuerte; la 'y' final
o sola es 'i'; la 'u' de 'que', 'qui', 'gue', 'gui' es muda, la 'ü' no; la 'h' no cuenta),
sinalefa entre palabra que termina en vocal y palabra que empieza en vocal (o en h),
y ajuste por la última palabra: aguda suma una, esdrújula resta una.

Uso: python3 silabas.py "verso"  |  python3 silabas.py archivo.txt  (un verso por línea)
Desde otro script:  from silabas import contar, detalle
"""
import re
import sys

FUERTES = set("aeoáéíóú")
VOCALES = "aeiouáéíóúü"
TILDES = set("áéíóú")
GAUCHO = False   # con True: 'ía', 'íe', 'ío' dentro de la palabra cuentan una sílaba (había, día),
                 # y la terminación 'ao' (pegao, callao) también; es lo que hace el poema y no el manual


def _norm(p):
    w = p.lower()
    w = re.sub(r"[^a-záéíóúüñ'’]", "", w)
    w = w.replace("'", "").replace("’", "")
    return w


def _fono(w):
    """Forma para contar: y→i cuando es vocal, u muda de que/qui/gue/gui, sin h."""
    w = re.sub(r"y(?![aeiouáéíóúü])", "i", w)
    w = re.sub(r"qu([eiéí])", r"q\1", w)
    w = re.sub(r"gu([eiéí])", r"g\1", w)
    w = w.replace("h", "")
    if GAUCHO:
        w = re.sub(r"í([aeo])", r"i\1", w)        # había → habia, día → dia
        w = re.sub(r"ao$", "áu", w)                 # pegao → pegáu (una sílaba, aguda)
        w = re.sub(r"ao(s)$", r"áu\1", w)
    return w


def _grupos(w):
    return re.findall(r"[aeiouáéíóúü]+", _fono(w))


def _silabas_grupo(g):
    n = sum(1 for c in g if c in FUERTES)
    return n if n else 1


def silabas_palabra(p):
    w = _norm(p)
    if not w:
        return 0
    return sum(_silabas_grupo(g) for g in _grupos(w)) or 1


def acento(p):
    """Posición de la sílaba tónica contada desde el final: 1 aguda, 2 llana, 3 esdrújula."""
    w = _norm(p)
    f = _fono(w)
    grupos = list(re.finditer(r"[aeiouáéíóúü]+", f))
    total = sum(_silabas_grupo(m.group()) for m in grupos) or 1
    if total == 1:
        return 1
    # con tilde: en qué sílaba cae
    acum = 0
    for m in grupos:
        g = m.group()
        n = _silabas_grupo(g)
        if any(c in TILDES for c in g):
            # dentro del grupo, qué nucleo lleva la tilde
            fuertes = [c for c in g if c in FUERTES]
            if n > 1 and fuertes:
                k = next((i for i, c in enumerate(fuertes) if c in TILDES), n - 1)
                return total - (acum + k)
            return total - acum
        acum += n
    if w.endswith("y"):
        return 1
    if w[-1] in "aeiouns":
        return 2
    return 1


def _empieza_vocal(p):
    w = _norm(p)
    if w == "y":
        return True
    if w.startswith(("hie", "hue", "hia")):   # hielo, hueso: la h suena como consonante
        return False
    w = w.lstrip("h")
    return bool(w) and w[0] in VOCALES


def _termina_vocal(p):
    w = _norm(p)
    return bool(w) and (w[-1] in "aeiouáéíóú" or w[-1] == "y")


def detalle(verso):
    palabras = [p for p in re.split(r"\s+", verso.strip()) if _norm(p)]
    if not palabras:
        return {"silabas": 0, "palabras": [], "sinalefas": 0, "ajuste": 0}
    base = [silabas_palabra(p) for p in palabras]
    sinalefas = 0
    for a, b in zip(palabras, palabras[1:]):
        if _termina_vocal(a) and _empieza_vocal(b):
            if _norm(a).endswith("y") and _norm(a) != "y":
                continue    # ley está: la y final suena consonante ante vocal
            sinalefas += 1
    pos = acento(palabras[-1])
    ajuste = 1 if pos == 1 else (-1 if pos == 3 else (-2 if pos >= 4 else 0))
    return {"silabas": sum(base) - sinalefas + ajuste, "palabras": list(zip(palabras, base)),
            "sinalefas": sinalefas, "ajuste": ajuste}


def contar(verso):
    return detalle(verso)["silabas"]


def posibles(verso):
    """Las cuentas que admite el verso si cada 'ía/íe/ío' y cada '-ao' se contrae o no
    (sinéresis a elección, como la hace un lector); devuelve el conjunto de cuentas."""
    import itertools
    palabras = re.split(r"(\s+)", verso.strip())
    cand = [i for i, p in enumerate(palabras) if re.search(r"í[aeo]|ao,?[.;:!?»\"]*$", _norm(p) if False else p.lower())]
    cand = [i for i in cand if re.search(r"í[aeo]|ao$|aos$", _norm(palabras[i]))]
    out = set()
    for flags in itertools.product((False, True), repeat=len(cand)):
        v = list(palabras)
        for i, f in zip(cand, flags):
            if f:
                w = v[i]
                w = re.sub(r"í([aeo])", r"i\1", w)
                w = re.sub(r"ao(?=[^a-záéíóúüñ]*$)", "áu", w)
                w = re.sub(r"aos(?=[^a-záéíóúüñ]*$)", "áus", w)
                v[i] = w
        out.add(contar("".join(v)))
    return out


if __name__ == "__main__":
    if sys.argv[1:2] == ["--gaucho"]:
        GAUCHO = True
        sys.argv.pop(1)
    arg = " ".join(sys.argv[1:])
    try:
        lineas = open(arg, encoding="utf-8").read().splitlines()
    except (OSError, ValueError):
        lineas = [arg]
    for l in lineas:
        if l.strip():
            d = detalle(l)
            print(d["silabas"], l, "  [%s; sinalefas %d; ajuste %+d]" % (
                " ".join("%s=%d" % x for x in d["palabras"]), d["sinalefas"], d["ajuste"]))
