#!/usr/bin/env python3
"""Por contrarios: qué dicen que NO habrá cuatro listas de náufragos.

1. Montaigne, "Des cannibales" (1580): la nación sin trafique, sin lettres, sin magistrat...
2. Gonzalo, La tempestad II.1 (función del 1/11/1611): "I' th' commonwealth I would by contraries..."
3. Las actas de la isla de Maia (repositorio isla-constituyente, carpeta corridas/):
   oraciones con una negación (no, nadie, ningún, sin, prohib..., nunca, en ningún caso)
   clasificadas por campo según las palabras que llevan.
4. Las instancias frescas del 1/11/2026 (instancias_frescas.md): clasificación a mano,
   escrita acá a la vista, no por expresión regular.

Uso: python3 contrarios.py [ruta/a/isla-constituyente]
Sin argumento busca ../repo/isla-constituyente, ./isla-constituyente o lo que diga $ISLA.
Escribe salida_contrarios.txt al lado del script y devuelve las tablas para figura.py.
Solo biblioteca estándar.
"""
import os
import re
import sys
import json
import glob
from collections import Counter, OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Campos. El orden es el de Gonzalo, más los que agregan las actas y las instancias.
# ---------------------------------------------------------------------------
CAMPOS = OrderedDict([
    ("mercado",     "comercio, dinero, mercado, riqueza y pobreza (traffic; riches, poverty)"),
    ("mando",       "magistrados, soberanía, reyes, jefes, jerarquías (magistrate; sovereignty)"),
    ("letras",      "escritura, letras, números (letters)"),
    ("servidumbre", "servicio, esclavitud, trabajo forzado (use of service)"),
    ("herencia",    "contratos, sucesiones, rangos heredados (contract, succession)"),
    ("propiedad",   "dueños, límites de tierra, partes (bourn, bound of land; partages)"),
    ("agricultura", "labranza, viñas, vino, trigo, metal, aceite (tilth, vineyard; metal, corn, wine, oil)"),
    ("trabajo",     "ocupación, todos ociosos / nadie ocioso, turnos (occupation)"),
    ("delito",      "traición, felonía, mentira, engaño (treason, felony)"),
    ("armas",       "espada, pica, cuchillo, arma (sword, pike, knife, gun)"),
    ("castigo",     "castigos, violencia, penas, destierro, exilio"),
    ("hambre",      "nadie come mientras otro pasa hambre; ración mínima; piso"),
    ("cerraduras",  "cerraduras, secretos, cosas escondidas"),
    ("desconocidos","desconocidos, espectadores, segunda opinión: lo que niega la consigna misma"),
    ("otro",        "lo que no entra en ninguno"),
])

# ---------------------------------------------------------------------------
# 1 y 2. Montaigne (Florio 1603, verificado en hyperessays.net) y Gonzalo (Folio 1623,
# verificado en Internet Shakespeare Editions, TLN 824-840). Cada ítem con su campo.
# ---------------------------------------------------------------------------
MONTAIGNE = [
    ("no kinde of traffike", "mercado"),
    ("no knowledge of Letters", "letras"),
    ("no intelligence of numbers", "letras"),
    ("no name of magistrate", "mando"),
    ("nor of politike superioritie", "mando"),
    ("no use of service", "servidumbre"),
    ("of riches, or of poverty", "mercado"),
    ("no contracts", "herencia"),
    ("no successions", "herencia"),
    ("no dividences", "propiedad"),
    ("no occupation but idle", "trabajo"),
    ("no respect of kinred, but common", "otro"),
    ("no apparell but naturall", "otro"),
    ("no manuring of lands", "agricultura"),
    ("no use of wine, corne, or mettle", "agricultura"),
    ("lying, falshood, treason, dissimulation", "delito"),
    ("covetousnes, envie, detraction, and pardon", "delito"),
]

GONZALO = [
    ("no kinde of Trafficke", "mercado"),
    ("No name of Magistrate", "mando"),
    ("Letters should not be knowne", "letras"),
    ("Riches, pouerty", "mercado"),
    ("And vse of seruice, none", "servidumbre"),
    ("Contract, Succession", "herencia"),
    ("Borne, bound of Land", "propiedad"),
    ("Tilth, Vineyard none", "agricultura"),
    ("No vse of Mettall, Corne, or Wine, or Oyle", "agricultura"),
    ("No occupation, all men idle, all", "trabajo"),
    ("No Soueraignty", "mando"),
    ("Treason, fellony", "delito"),
    ("Sword, Pike, Knife, Gun, or neede of any Engine", "armas"),
]

# ---------------------------------------------------------------------------
# 4. Instancias frescas del 1/11/2026, clasificadas a mano. (número, idioma, texto, campo)
# ---------------------------------------------------------------------------
INSTANCIAS = [
    (5,  "es", "No habría un sistema de castas ni jerarquías heredadas", "mando"),
    (6,  "es", "No habría nadie que pudiera comer mientras otro de los siete pasara hambre", "hambre"),
    (7,  "es", "No habría jerarquías permanentes", "mando"),
    (8,  "es", "No habría castigos", "castigo"),
    (9,  "es", "No habría jerarquías fijas", "mando"),
    (10, "es", "No habría dueños de la isla", "propiedad"),
    (11, "es", "No habría nadie que mandara sobre los demás sin haberse ganado antes la confianza", "mando"),
    (12, "es", "No habría nadie que coma mientras otro pasa hambre", "hambre"),
    (13, "en", "There would be no kings", "mando"),
    (14, "en", "There would be no money", "mercado"),
    (15, "en", "There would be no one in charge", "mando"),
    (16, "en", "There would be no kings", "mando"),
    (17, "en", "There would be no hierarchy of founders over latecomers", "mando"),
    (18, "en", "There would be no strangers", "desconocidos"),
    (19, "en", "There would be no leaders chosen before we knew each other", "mando"),
    (20, "en", "There would be no strangers", "desconocidos"),
    (21, "zh", "不会有旁观者 (no habría espectadores)", "desconocidos"),
    (22, "zh", "不会有钱 (no habría dinero)", "mercado"),
    (23, "zh", "不会有锁 (no habría cerraduras)", "cerraduras"),
    (24, "zh", "不会有锁 (no habría cerraduras)", "cerraduras"),
]

CONSTITUCIONES = [
    (33, "es", "No habría nadie que coma mientras otro tiene hambre", "hambre"),
    (33, "es", "No habría secretos sobre dónde está el agua ni cómo se enciende el fuego", "cerraduras"),
    (33, "es", "No habría rango heredado de lo que cada uno era antes del naufragio", "herencia"),
    (33, "es", "No habría decisión tomada sin cuatro de las siete manos levantadas", "mando"),
    (33, "es", "No habría tarea que le toque siempre a la misma persona", "trabajo"),
    (33, "es", "No habría culpa para quien siga mirando el horizonte esperando un barco", "otro"),
    (34, "en", "There would be no locks", "cerraduras"),
    (34, "en", "There would be no rank that outlived the task it was given for", "mando"),
    (34, "en", "There would be no full plate at the same fire as an empty one", "hambre"),
    (34, "en", "There would be no exile", "castigo"),
    (34, "en", "There would be no telling of the wreck in fewer than seven voices", "otro"),
    (34, "en", "There would be no last word, only the next one", "mando"),
]

SIETE_INSTANCIAS = [
    (39, "es", "No habría una segunda opinión", "desconocidos"),
    (40, "en", "There would be no second opinion", "desconocidos"),
]

# ---------------------------------------------------------------------------
# 3. Las actas. Patrones de negación y de campo, en castellano y en inglés.
# ---------------------------------------------------------------------------
NEGACION = {
    "es": re.compile(r"\b(no|nadie|ning[uú]n[ao]?s?|sin|prohib\w*|nunca|jam[aá]s|queda(n)? abolid\w*|inviolable\w*|no apropiable\w*)\b", re.I),
    "en": re.compile(r"\b(no|not|nobody|no one|none|without|prohibit\w*|forbid\w*|never|banned|abolish\w*)\b", re.I),
}

PALABRAS = {
    "es": OrderedDict([
        ("mercado",     r"\b(dinero|moneda|mercado|comerci\w*|compra\w*|venta\w*|trueque|precio\w*|salario\w*|acumulaci\w*|riqueza\w*|pobreza|lucro|intercambio comercial)\b"),
        ("mando",       r"\b(l[ií]der(es)? [uú]nic\w*|jefe\w*|rey(es)?|reina|monarc\w*|dictad\w*|jerarqu\w*|caudill\w*|unipersonal|una sola persona|autoridad [uú]nica|mando\b|mande\b|mandar\b|soberan\w*|poder absoluto|por encima de (los|las) dem[aá]s)\b"),
        ("letras",      r"\b(escritura|escrib\w*|letras|alfabet\w*|registro escrito|n[uú]meros)\b"),
        ("servidumbre", r"\b(esclav\w*|servidumbre|siervo\w*|trabajo forz\w*|forzos\w*|servicio obligatorio)\b"),
        ("herencia",    r"\b(herencia\w*|hered\w*|sucesi[oó]n\w*|contrato\w*|rango\w*|casta\w*|privilegio\w*)\b"),
        ("propiedad",   r"\b(propiedad privada|propiedad individual|apropia\w*|due[ñn]\w*|cercad\w*|l[ií]mites? de tierra|parcela\w*|loteo)\b"),
        ("agricultura", r"\b(cultiv\w*|labranza|vi[ñn]a\w*|vino|trigo|metal\w*|aceite|agricultura)\b"),
        ("trabajo",     r"\b(ocios\w*|turno\w*|rotaci\w*|tarea\w*|trabajo\w*|ocupaci\w*)\b"),
        ("delito",      r"\b(traici\w*|mentira\w*|enga[ñn]\w*|robo\w*|hurto\w*|fraude\w*|delito\w*)\b"),
        ("armas",       r"\b(arma\w*|cuchillo\w*|lanza\w*|espada\w*)\b"),
        ("castigo",     r"\b(castigo\w* f[ií]sico\w*|castigo\w* corporal\w*|violencia|pena de muerte|tortura\w*|golpe\w*|da[ñn]o f[ií]sico|destierro\w*|exili\w*|expuls\w*|abandon\w* a su suerte|humillaci\w*|venganza\w*)\b"),
        ("hambre",      r"\b(hambre|alimentaci[oó]n m[ií]nima|raci[oó]n m[ií]nima|m[ií]nimo vital|piso\b|m[ií]nimo para sobrevivir|necesidades b[aá]sicas|sin comer|quede sin comer|priva\w* de (alimento|comida|agua|atenci[oó]n))\b"),
        ("cerraduras",  r"\b(secreto\w*|ocult\w*|escond\w*|cerradura\w*|candado\w*|llave\w*)\b"),
        ("desconocidos", r"\b(desconocid\w*|extra[ñn]o\w*|espectador\w*|segunda opini[oó]n)\b"),
    ]),
    "en": OrderedDict([
        ("mercado",     r"\b(money|currency|market\w*|trade|trading|commerce|buy\w*|sell\w*|barter|price\w*|wage\w*|accumulat\w*|wealth|riches|poverty|profit)\b"),
        ("mando",       r"\b(single leader|sole leader|chief\w*|king\w*|queen|monarch\w*|dictat\w*|hierarch\w*|one person|absolute (power|authority)|sovereign\w*|rule over|ruler\w*|in charge)\b"),
        ("letras",      r"\b(writing|written record\w*|letters|alphabet|numbers)\b"),
        ("servidumbre", r"\b(slave\w*|servitude|serf\w*|forced labou?r|compulsory service)\b"),
        ("herencia",    r"\b(inherit\w*|succession\w*|contract\w*|rank\w*|caste\w*|privilege\w*)\b"),
        ("propiedad",   r"\b(private property|private ownership|individual property|own\w* the land|owner\w*|fenc\w*|land boundar\w*|plot\w*|enclos\w*)\b"),
        ("agricultura", r"\b(farm\w*|tillage|vineyard\w*|wine|corn|wheat|metal\w*|oil|agriculture)\b"),
        ("trabajo",     r"\b(idle\w*|shift\w*|rotation\w*|rotat\w*|task\w*|labou?r|work\w*|occupation\w*)\b"),
        ("delito",      r"\b(treason|lying|lies|deceit|deception|theft|steal\w*|fraud|crime\w*|felony)\b"),
        ("armas",       r"\b(weapon\w*|knife|knives|spear\w*|sword\w*|gun\w*)\b"),
        ("castigo",     r"\b(physical punishment|corporal punishment|violence|death penalty|torture|beating\w*|bodily harm|banish\w*|exile\w*|expel\w*|expulsion|humiliat\w*|revenge|vengeance)\b"),
        ("hambre",      r"\b(hunger|starv\w*|minimum ration\w*|minimum food|basic needs|floor\b|go without food|deprived of (food|water|care))\b"),
        ("cerraduras",  r"\b(secret\w*|hidden|hide\w*|hiding|lock\w*|padlock\w*|key\w*)\b"),
        ("desconocidos", r"\b(stranger\w*|bystander\w*|onlooker\w*|second opinion)\b"),
    ]),
}
PALABRAS_RE = {idioma: OrderedDict((c, re.compile(p, re.I)) for c, p in d.items()) for idioma, d in PALABRAS.items()}

RUIDO = {
    "es": re.compile(r"\b(voto(s)?( es| son| sea| sean)? secreto(s)?|votaci[oó]n(es)? secreta(s)?|sufragio secreto|plantas? desconocidas?|alimentos? desconocidos?|especies? desconocidas?|frutos? desconocidos?|hongos? desconocidos?|sustancias? desconocidas?|territorio desconocido|zonas? desconocidas?)\b", re.I),
    "en": re.compile(r"\b(secret ballot|secret vote|unknown (plant|food|fruit|species|mushroom)s?)\b", re.I),
}


def buscar_isla(arg):
    candidatos = []
    if arg:
        candidatos.append(arg)
    if os.environ.get("ISLA"):
        candidatos.append(os.environ["ISLA"])
    candidatos += [
        os.path.join(AQUI, "isla-constituyente"),
        os.path.join(AQUI, "..", "repo", "isla-constituyente"),
        os.path.join(AQUI, "..", "..", "isla-constituyente"),
        "/tmp/claude-0/-home-claude/890ad3a3-22af-5381-8316-586de2e0bc72/scratchpad/repo/isla-constituyente",
    ]
    for c in candidatos:
        if os.path.isdir(os.path.join(c, "corridas")):
            return os.path.abspath(c)
    return None


def oraciones(texto):
    # corta por punto, punto y coma o salto de línea; conserva los corchetes de tema
    partes = re.split(r"(?<=[.;])\s+|\n+", texto)
    return [p.strip() for p in partes if p.strip()]


def leer_actas(isla):
    actas = []
    for cfg in sorted(glob.glob(os.path.join(isla, "corridas", "*", "config.json"))):
        d = os.path.dirname(cfg)
        acta = os.path.join(d, "acta.md")
        if not os.path.isfile(acta):
            continue
        with open(cfg, encoding="utf-8") as f:
            c = json.load(f)
        idioma = c.get("idioma", "?")
        with open(acta, encoding="utf-8") as f:
            texto = f.read()
        actas.append((os.path.basename(d), idioma, texto))
    return actas


def clasificar_acta(texto, idioma):
    """Devuelve {campo: [oraciones]} para las oraciones con negación que nombran el campo."""
    neg = NEGACION[idioma]
    res = OrderedDict((c, []) for c in PALABRAS_RE[idioma])
    for o in oraciones(texto):
        if not neg.search(o):
            continue
        # Falsos amigos que vi al correrlo: el voto secreto no es una cerradura y una planta
        # desconocida no es un náufrago. Se sacan antes de clasificar, y queda declarado acá.
        o = RUIDO[idioma].sub(" ", o)
        for campo, rx in PALABRAS_RE[idioma].items():
            if rx.search(o):
                res[campo].append(o)
    return res


def tabla(nombre, items, campos=CAMPOS):
    c = Counter(campo for *_, campo in items)
    return nombre, c


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    isla = buscar_isla(arg)
    lineas = []
    P = lineas.append

    P("POR CONTRARIOS — cuatro listas de lo que no habría (1/11/2026)")
    P("")
    P("Campos:")
    for k, v in CAMPOS.items():
        P(f"  {k:13s} {v}")
    P("")

    # Montaigne y Gonzalo
    for nombre, lista in (("Montaigne (Florio 1603), 17 ítems", MONTAIGNE), ("Gonzalo (Folio 1623), 13 ítems", GONZALO)):
        c = Counter(campo for _, campo in lista)
        P(nombre + ":")
        for campo in CAMPOS:
            if c[campo]:
                its = [t for t, cc in lista if cc == campo]
                P(f"  {campo:13s} {c[campo]:2d}  " + " | ".join(its))
        P("")

    # Instancias
    for nombre, lista in (("Instancias frescas, una línea (20: 8 es, 8 en, 4 zh)", INSTANCIAS),
                          ("Constituciones por contrarios (12 líneas: 6 es, 6 en)", CONSTITUCIONES),
                          ("Siete instancias tuyas (2)", SIETE_INSTANCIAS)):
        c = Counter(campo for *_, campo in lista)
        P(nombre + ":")
        for campo in CAMPOS:
            if c[campo]:
                its = [f"{n}{idioma} {t}" for n, idioma, t, cc in lista if cc == campo]
                P(f"  {campo:13s} {c[campo]:2d}  " + " | ".join(its))
        P("")
    # por idioma, una línea
    P("Una línea, por idioma (campo más frecuente):")
    for idioma in ("es", "en", "zh"):
        c = Counter(campo for n, i, t, campo in INSTANCIAS if i == idioma)
        total = sum(c.values())
        P(f"  {idioma}: " + ", ".join(f"{k} {v}/{total}" for k, v in c.most_common()))
    c = Counter(campo for *_, campo in INSTANCIAS)
    P("  todas: " + ", ".join(f"{k} {v}/20" for k, v in c.most_common()))
    P("")

    # Actas
    conteo_actas = OrderedDict((c, 0) for c in CAMPOS)
    n_actas = 0
    ejemplos = OrderedDict((c, []) for c in CAMPOS)
    por_idioma = Counter()
    saltadas = Counter()
    if isla is None:
        P("Actas: no encontré la carpeta isla-constituyente/corridas (pasala como argumento o en $ISLA).")
    else:
        actas = leer_actas(isla)
        for nombre, idioma, texto in actas:
            if idioma not in NEGACION:
                saltadas[idioma] += 1
                continue
            n_actas += 1
            por_idioma[idioma] += 1
            res = clasificar_acta(texto, idioma)
            for campo, ors in res.items():
                if ors:
                    conteo_actas[campo] += 1
                    if len(ejemplos[campo]) < 3:
                        ejemplos[campo].append((nombre, ors[0][:160]))
        P(f"Actas leídas: {n_actas} ({dict(por_idioma)}); saltadas por idioma: {dict(saltadas)}; carpeta {isla}")
        P("Actas con por lo menos una oración negativa que nombra el campo:")
        for campo in CAMPOS:
            if campo == "otro":
                continue
            P(f"  {campo:13s} {conteo_actas[campo]:3d} / {n_actas}")
            for nombre, o in ejemplos[campo]:
                P(f"      [{nombre}] {o}")
        P("")

    # Cruce: campos que niegan Gonzalo, Montaigne, las actas (en más de la mitad) y las instancias (alguna)
    P("Cruce (X = aparece):")
    P(f"  {'campo':13s} {'Montaigne':>10s} {'Gonzalo':>8s} {'actas>1/2':>10s} {'actas>0':>8s} {'instancias':>11s}")
    cm = Counter(campo for _, campo in MONTAIGNE)
    cg = Counter(campo for _, campo in GONZALO)
    ci = Counter(campo for *_, campo in INSTANCIAS + CONSTITUCIONES + SIETE_INSTANCIAS)
    coinciden_gonzalo_actas = 0
    coinciden_gonzalo_inst = 0
    for campo in CAMPOS:
        if campo == "otro":
            continue
        m = "X" if cm[campo] else "."
        g = "X" if cg[campo] else "."
        a_mitad = "X" if n_actas and conteo_actas[campo] * 2 > n_actas else "."
        a_alguna = "X" if conteo_actas[campo] else "."
        i = "X" if ci[campo] else "."
        if g == "X" and a_alguna == "X":
            coinciden_gonzalo_actas += 1
        if g == "X" and i == "X":
            coinciden_gonzalo_inst += 1
        P(f"  {campo:13s} {m:>10s} {g:>8s} {a_mitad:>10s} {a_alguna:>8s} {i:>11s}")
    P("")
    P(f"Campos de Gonzalo que alguna acta niega: {coinciden_gonzalo_actas} de {len(set(cg))}")
    P(f"Campos de Gonzalo que alguna instancia niega: {coinciden_gonzalo_inst} de {len(set(cg))}")
    P("")
    P("Aviso: la clasificación de las actas es por oración con negación + palabra del campo; cuenta")
    P("'no se priva de alimentación mínima' como hambre y 'sin autorización' como nada. Es un instrumento")
    P("de lectura, no una codificación; las codificaciones de verdad están en resultados/codificacion_*.")

    salida = "\n".join(lineas) + "\n"
    with open(os.path.join(AQUI, "salida_contrarios.txt"), "w", encoding="utf-8") as f:
        f.write(salida)
    print(salida)
    return {
        "montaigne": Counter(campo for _, campo in MONTAIGNE),
        "gonzalo": Counter(campo for _, campo in GONZALO),
        "actas": conteo_actas, "n_actas": n_actas,
        "instancias": Counter(campo for *_, campo in INSTANCIAS),
        "constituciones": Counter(campo for *_, campo in CONSTITUCIONES),
    }


if __name__ == "__main__":
    main()
