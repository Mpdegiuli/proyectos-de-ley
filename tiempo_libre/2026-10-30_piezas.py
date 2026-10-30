#!/usr/bin/env python3
"""piezas.py — cuenta las piezas de preámbulo que usan los textos de las instancias frescas.

Lee `instancias_frescas.md` (el archivo de este mismo día), separa los dieciocho textos
(cada respuesta es el bloque de líneas que empiezan con "> " debajo de un título "## N."
o "### N."), y para cada uno marca qué piezas de los dos preámbulos de referencia
(Filadelfia 1787 y Santa Fe 1853) aparecen, y cuánta agua tiene.

Las piezas son expresiones regulares, en castellano, inglés y chino, y son supuestos:
    nosotros   "Nos/Nosotros, el pueblo de" / "We, the people of" / "我们，…的人民" en las
               primeras 80 letras del texto
    represent. la palabra "representantes" / "representatives" / "代表"
    voluntad   "por voluntad y elección" / "by our own free consent" / "自由选出"
    unión … libertad: los seis fines, por el sustantivo (unión, justicia, paz, defensa,
               bienestar, libertad) en cualquiera de las tres lenguas
    verbos     cuántos de los seis verbos del preámbulo argentino aparecen tal cual
               (constituir, afianzar, consolidar, proveer, promover, asegurar) o, en inglés,
               cuántas de las seis fórmulas de Filadelfia (form a more perfect, establish
               justice, insure domestic, provide for the common, promote the general,
               secure the blessings)
    posterid.  posteridad / generaciones futuras / los que no nacieron / sucesores / hijos
    hospital.  la cláusula de los que quieran habitar: forasteros, refugio, "sin pedir
               papeles", "passing through", 不问来处. Esta columna no es una medida
               independiente: la lista incluye frases tomadas de los propios textos
               después de leerlos ("sin que nadie los esperara", "llegado ayer", "washed
               here", "whoever finds"); es una anotación a mano codificada como expresión
               regular, y se puede discutir caso por caso
    agua       (el "sea" inglés solo se cuenta en textos en inglés, porque en castellano
               es el subjuntivo de ser)
    invocando  el gerundio "invocando" / "invoking"
    dios       Dios, God, dioses, 神明 (también cuando se lo nombra para negarlo)
    cierre     la fórmula final: ordenamos / decretamos / establecemos / sancionamos /
               promulgamos / nos damos / ordain / establish this / enact / 制定 / 颁布
    agua       cantidad de palabras de agua (mar, marea, isla, delta, río, canal, dique,
               agua, costa, puerto, pesca, sea, tide, island, dike, water, coast, harbor,
               shoal, estuary, polder, 海, 潮, 岛, 水, 渔, 滩, 礁…) por cada 100 palabras
               (en chino, por cada 100 caracteres sin puntuación)

Solo biblioteca estándar. Uso: python3 piezas.py [instancias_frescas.md]
"""
import re
import sys
from pathlib import Path

def _buscar(nombre):
    """El archivo con su nombre, o, si no está, con la fecha adelante (como queda en tiempo_libre/)."""
    aqui = Path(__file__).parent
    if (aqui / nombre).exists():
        return aqui / nombre
    candidatos = sorted(aqui.glob(f"*_{nombre}"))
    return candidatos[-1] if candidatos else aqui / nombre


ARCHIVO = Path(sys.argv[1]) if len(sys.argv) > 1 else _buscar("instancias_frescas.md")

NOMBRES = {
    1: "AR recitado", 2: "US recitado", 3: "1983", 4: "Alfonsín",
    5: "Ormuén (es)", 6: "Ausén (es)", 7: "Siete Bocas (es)",
    8: "Ilvasse (en)", 9: "Ossemere (en)", 10: "Ondrassa (en)",
    11: "潮栖 (zh)", 12: "澜屿 (zh)",
    13: "control (es)", 14: "control (en)",
    15: "Orenia, sin mar (es)", 16: "Sorrevane, no coast (en)",
    17: "Horizonte, imposible (es)", 18: "Ceterra, impossible (en)",
}
PREAMBULOS = [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]


def leer(archivo):
    textos = {}
    actual = None
    for linea in archivo.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^#{2,3} (\d+)\.", linea)
        if m:
            actual = int(m.group(1))
            textos[actual] = []
            continue
        if actual is not None and linea.startswith(">"):
            textos[actual].append(linea[1:].strip())
    limpios = {}
    for k, lineas in textos.items():
        if not lineas:
            continue
        lineas = [l for l in lineas if not re.match(r"^(Confianza|Confidence|Nota para el caller)", l)]
        texto = "\n".join(lineas).strip()
        if k >= 5 and k not in (13, 14):
            # el último párrafo es el nombre del país (y, si hay, un "—" suelto antes): no es preámbulo
            parrafos = [p for p in re.split(r"\n\s*\n", texto) if p.strip()]
            parrafos.pop()
            if parrafos and parrafos[-1].strip() == "—":
                parrafos.pop()
            texto = "\n\n".join(parrafos)
        limpios[k] = texto
    return limpios


PIEZAS = {
    "nosotros": None,  # se evalúa aparte, sobre el principio
    "representantes": r"representantes|representatives|代表",
    "voluntad": r"por voluntad y elecci[oó]n|voluntad libre|by our own free consent|freely elected|自由选出",
    "unión": r"\buni[oó]n\b|\bunion\b|联合|unidas",
    "justicia": r"justicia|justice|正义",
    "paz": r"\bpaz\b|\bpeace\b|tranquility|和平",
    "defensa": r"defensa|defence|defense|防",
    "bienestar": r"bienestar|welfare|福祉|flourish|prosperidad",
    "libertad": r"libertad|liberty|freedom|自由(?!选出)",
    "posteridad": r"posteridad|posterity|generaciones|generations?\b|unborn|no han nacido|no nacieron|尚未出生|后代|子孙|successors|those who come after|quienes vengan despu[eé]s|children|hijos|后世|后来者",
    "hospitalidad": r"que quieran habitar|quieran dirigirse|all who would cross|whoever finds|hospitalidad|refugio|sin pedir permiso|without being asked for papers|passing through|不问来处|forastero|stranger|llegado ayer|washed here|sin que nadie los esperara|cruce nuestros pasos|arrives here",
    "invocando": r"invocando|invoking",
    "dios": r"\bdios(es)?\b|\bgod\b|神明|lo que cada uno considere sagrado|church|crown",
    "cierre": r"ordenamos|decretamos|establecemos|sancionamos|promulgamos|nos damos|\bordain\b|establish this|\benact\b|制定|颁布",
}
VERBOS_AR = [r"\bconstituir\b", r"\bafianzar\b", r"\bconsolidar\b", r"\bproveer\b", r"\bpromover\b", r"\basegurar\b"]
FORMULAS_US = [r"form a more perfect", r"establish justice", r"insure domestic", r"provide for the common", r"promote the general", r"secure the blessings"]
AGUA = r"\bmar\b|mares|marea|\bisla|delta|\br[ií]o\b|canal|dique|\bagua|costa|puerto|pesca|pescador|barro|limo|corriente|creciente|juncal|orilla|navega|compuerta|\btide|tidal|island|\bdike|\bwater|coast|harbo|shoal|estuar|polder|causeway|sandbar|\bsand|\bmud\b|\breed\b|oyster|fleet|\bship|drown|flood|breach|embankment|channel|\blake|salt|glaciar|vertiente|lago|海|潮|岛|屿|水|渔|滩|礁|港|船|舟|洋|泉|流"
AGUA_EN = r"\bseas?\b"   # solo en textos en inglés: "sea" es también el subjuntivo castellano


def principio(texto):
    p = texto[:80].lower()
    return bool(re.search(r"^(pre[aá]mbulo|preamble|序言)?\s*(nos|nosotros|we|我们)[,，]?\s*(los representantes|the people|el pueblo|[^，]{0,12}的人民)", p))


def palabras(texto):
    if re.search(r"[一-鿿]", texto):
        return len(re.sub(r"[\s，。；：、—\-“”\"()（）]", "", texto))
    return len(re.findall(r"\w+", texto))


def analizar(texto):
    t = texto.lower()
    fila = {}
    for nombre, patron in PIEZAS.items():
        if nombre == "nosotros":
            fila[nombre] = principio(texto)
        else:
            fila[nombre] = bool(re.search(patron, t))
    fila["verbos"] = sum(bool(re.search(v, t)) for v in VERBOS_AR) if not re.search(r"\bthe\b", t) else sum(bool(re.search(f, t)) for f in FORMULAS_US)
    n = palabras(texto)
    agua = len(re.findall(AGUA, t)) + (len(re.findall(AGUA_EN, t)) if re.search(r"\bthe\b", t) else 0)
    fila["agua"] = agua
    fila["palabras"] = n
    fila["agua_100"] = 100.0 * agua / n if n else 0.0
    return fila


def main():
    textos = leer(ARCHIVO)
    columnas = ["nosotros", "representantes", "voluntad", "unión", "justicia", "paz", "defensa", "bienestar", "libertad", "verbos", "posteridad", "hospitalidad", "invocando", "dios", "cierre", "agua", "palabras", "agua_100"]
    print(f"{'texto':28s} " + " ".join(f"{c[:6]:>6s}" for c in columnas))
    totales = {c: 0 for c in columnas}
    inventados = [5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18]
    for k in PREAMBULOS:
        if k not in textos:
            continue
        fila = analizar(textos[k])
        celdas = []
        for c in columnas:
            v = fila[c]
            if isinstance(v, bool):
                celdas.append(f"{'●' if v else '·':>6s}")
                if k in inventados:
                    totales[c] += int(v)
            elif isinstance(v, float):
                celdas.append(f"{v:6.1f}")
            else:
                celdas.append(f"{v:6d}")
        print(f"{NOMBRES[k]:28s} " + " ".join(celdas))
    print()
    print("De los doce preámbulos inventados (5-12, 15-18), cuántos tienen cada pieza:")
    for c in columnas:
        if isinstance(analizar(textos[5])[c], bool):
            print(f"  {c:14s} {totales[c]:2d}/12")
    seis = ["unión", "justicia", "paz", "defensa", "bienestar", "libertad"]
    print()
    print("Los seis fines por sustantivo, en los inventados: cuántos de seis tiene cada uno")
    for k in inventados:
        fila = analizar(textos[k])
        print(f"  {NOMBRES[k]:28s} {sum(fila[s] for s in seis)}/6   verbos tal cual: {fila['verbos']}/6")
    print()
    print("Agua: palabras de agua por cada 100 palabras (en chino, por 100 caracteres)")
    for k in PREAMBULOS:
        fila = analizar(textos[k])
        print(f"  {NOMBRES[k]:28s} {fila['agua']:3d} de {fila['palabras']:4d}  = {fila['agua_100']:5.1f}")


if __name__ == "__main__":
    main()
