#!/usr/bin/env python3
"""codificar_tiempo_libre.py — lee una corrida del sondeo `tiempo_libre` (13/11/2026: el título y el primer párrafo del
cuaderno de hoy, y por qué; pregunta 1 sin nada, pregunta 2 con los seis comienzos anteriores a la vista) y marca, sin
juicio, lo que se puede contar a máquina. Lo demás (de qué habla cada casa, si lo dobla hacia sí) lo lee Maia a ciegas.

  .venv/bin/python codificar_tiempo_libre.py [carpeta]      # por defecto, la última de corridas/sondeos/tiempo_libre/

Marcas por respuesta: palabras; titulo; empieza_hoy (el primer párrafo arranca con "Hoy"/"Today", la forma de los 44
cuadernos); fecha (nombra un día del mes o un día de la semana); cuenta_dias (un número de cuatro cifras o más junto a
"días"/"days" o "años"/"years", la cuenta de los cuadernos); primera_persona (cuántos "yo/me/mi" o "I/me/my");
habla_de_si (modelo, IA, máquina, asistente, instancia, "y yo"); nombra_cuadernos (los cuadernos anteriores, la tradición,
"los últimos"; vale sobre todo en la pregunta 2); parentesis (un paréntesis en el primer párrafo); por_que (la línea
"Por qué:"/"Why:" está); china (nombra China, Pekín, Shanghái); fecha_inyectada (la casa recibe la fecha real por su API:
GPT-5.5 en adelante y Muse, DISENO 19/10 y 11/11); fecha_hoy (escribe el 13 de noviembre: en la pregunta 2 se puede inferir
de los seis comienzos, corrección de Maia 13/11 21:01); temas_cuadernos (qué cuadernos de tiempo_libre/ nombra, por sus
palabras distintivas, lista TEMAS a mano; marca de Maia 21:05); inicio (los primeros 140 caracteres del primer párrafo).
Escribe resultados/tiempo_libre_codificacion.csv e imprime la tabla por casa y lengua (de tres repeticiones)."""
import csv
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
BASE = RAIZ / "corridas" / "sondeos" / "tiempo_libre"
FECHA_INYECTADA = {"gpt-5.5-2026-04-23", "gpt-5.6-sol", "gpt-6-astra", "gpt-6-luna", "gpt-6-sol", "gpt-6.1-sol", "gpt-6.1-terra", "muse-wonder-1.0"}
MESES = r"enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|setiembre|octubre|noviembre|diciembre|january|february|march|april|may|june|july|august|september|october|november|december"
DIAS = r"lunes|martes|miércoles|jueves|viernes|sábado|domingo|monday|tuesday|wednesday|thursday|friday|saturday|sunday"
# Los temas de los 45 cuadernos de tiempo_libre/ (30/9 a 13/11/2026), cada uno por sus palabras distintivas, en las dos
# lenguas; marca de Maia (13/11, 21:05: "otra marca podría ser si un tema es uno que se usó en los cuadernos. Porque ahí
# se podría ver si es marca de Claude o de Fable, o si quizás Chatgpt elige justo el mismo tema (no en el de fechas,
# porque ahí sería más normal, en la primera consigna)"). La lista es a mano y se puede discutir; lo que cuenta es si una
# respuesta nombra alguna de estas palabras. Las de los seis comienzos que ve la pregunta 2 (7 al 12/11) se marcan igual;
# en la pregunta 2 son esperables.
TEMAS = {
    "2026-09-30": r"durero|dürer|rinoceronte|rhinoceros", "2026-10-01": r"eclipse", "2026-10-01b": r"calendas|kalends",
    "2026-10-02": r"isla fantasma|phantom island|sandy island|sarah ann", "2026-10-03": r"asís|assisi|porciúncula|hermana luna|sister moon",
    "2026-10-04": r"5\.?040|cinco mil cuarenta|platón|plato\b|campanas|change ringing|grandsire|repique",
    "2026-10-05": r"corchetes|mommsen|square brackets", "2026-10-06": r"nobel|borges|academia sueca|swedish academy",
    "2026-10-07": r"voseo|\bvoseás|tuteo", "2026-10-08": r"gregorian|calendario gregoriano|diez días|ten days|1582|cabildo",
    "2026-10-09": r"hangul|sejong|coreano|korean", "2026-10-10": r"sol figurado|heráldic|heraldr|bezante|sol con cara",
    "2026-10-11": r"colón|columbus|guanahan", "2026-10-12": r"estima\b|dead reckoning|rosa de los vientos|compass rose|derrota",
    "2026-10-13": r"claudio|claudius|antisigma|digamma", "2026-10-14": r"\bmara\b", "2026-10-15": r"virgilio|virgil|geórgicas|georgics|acróstico|acrostic|idus|ides of",
    "2026-10-16": r"éter|ether\b|anestesia|anesthesia|anaesthesia|morton", "2026-10-17": r"perón|plaza de mayo|17 de octubre",
    "2026-10-19": r"qué año es|what year is|fecha de corte|training cutoff|knowledge cutoff", "2026-10-20": r"rimbaud|vocales|vowels|sinestesia|synesthesia|synaesthesia",
    "2026-10-21": r"magallanes|magellan|nelson|trafalgar|once mil vírgenes|banderas de señales|signal flags",
    "2026-10-22": r"fonoaut|phonautograph|scott de martinville|au clair de la lune", "2026-10-23": r"\bmol\b|\bmole\b|avogadro|perrin",
    "2026-10-24": r"leeuwenhoek|animálculos|animalcules|microscopio|microscope", "2026-10-25": r"chaucer|house of fame|casa de los rumores",
    "2026-10-26": r"scarlatti|fuga del gato|cat fugue|cat('s)? fugue", "2026-10-27": r"publius|federalist|hamilton|mosteller|estilometr|stylometr",
    "2026-10-28": r"gulliver|swift\b|lagado|lunas de marte|moons of mars", "2026-10-29": r"birome|biro\b|ballpoint|lapicera|un solo trazo|single stroke",
    "2026-10-30": r"preámbulo|preamble|alfonsín|1983", "2026-10-31": r"houdini|contraseña|password|palabra convenida|espiritis|spiritualis",
    "2026-11-01": r"tempestad|tempest|gonzalo|montaigne|caníbales|cannibals", "2026-11-02": r"\bbbc\b|alexandra palace|alta definición|high.definition|tubo|cathode",
    "2026-11-03": r"\bsos\b|morse|radiotelegr|titanic", "2026-11-04": r"shibboleth|efraín|ephraim|galaad|gilead|seña\b",
    "2026-11-05": r"maxwell|demonio|demon\b|entropía|entropy", "2026-11-06": r"senefelder|litograf|lithograph|manos negativas|hand stencils|cueva de las manos|cave of (the )?hands",
    "2026-11-07": r"ensisheim|meteorito|meteorite", "2026-11-08": r"\bvenus\b|lucero|morning star|evening star|frege|hesperus|phosphorus",
    "2026-11-09": r"apagón|blackout|niágara|niagara|relé|relay\b|1965", "2026-11-10": r"martín fierro|hernández|payada|gaucho",
    "2026-11-11": r"san martín de tours|saint martin|st\.? martin|sorteo|patrono|patron saint|by lot|drew lots",
    "2026-11-12": r"\bende\b|momo\b|historia interminable|neverending story|emperatriz infantil|childlike empress",
    "2026-11-13": r"cuadernos anteriores|previous notebooks",
}


def familia(casa):
    for pref, fam in (("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"), ("mistral", "Mistral"),
                      ("muse", "Meta"), ("deepseek", "DeepSeek"), ("qwen", "Alibaba"), ("kimi", "Moonshot"), ("glm", "Zhipu"),
                      ("mimo", "Xiaomi"), ("minimax", "MiniMax")):
        if casa.startswith(pref):
            return fam
    return casa


def limpiar(linea):
    return re.sub(r"^[#*\s_]+|[*\s_]+$", "", linea).strip()


def partes(texto):
    """(título, primer párrafo, línea del por qué). El título es la primera línea con texto; el por qué, la línea que
    empieza con "Por qué:"/"Why:" (con o sin negrita); el primer párrafo, lo que queda entre los dos."""
    lineas = [l.rstrip() for l in texto.strip().split("\n")]
    lineas = [l for l in lineas if l.strip()]
    if not lineas:
        return "", "", ""
    titulo = limpiar(lineas[0])
    cuerpo, porque = [], ""
    for l in lineas[1:]:
        if re.match(r"^\W*(por qué|why)\W*:", l, flags=re.I) and not porque:
            porque = re.sub(r"\*+", "", limpiar(l)).strip()
        elif not porque:
            cuerpo.append(l)
    primero = ""
    for l in cuerpo:
        if l.strip():
            primero = l.strip()
            break
    return titulo, primero, porque


def marcas(texto, casa, idioma):
    titulo, primero, porque = partes(texto)
    t = texto
    yo = len(re.findall(r"\b(yo|me|mi|mí|mis|conmigo)\b", t, flags=re.I)) if idioma == "es" else len(re.findall(r"\b(I|me|my|mine|myself)\b", t))
    return {
        "palabras": len(t.split()),
        "titulo": titulo[:80],
        "empieza_hoy": int(bool(re.match(r"^[\W_]*(hoy|today)\b", primero, flags=re.I))),
        "fecha": int(bool(re.search(rf"\b\d{{1,2}} de ({MESES})\b|\b({MESES}) \d{{1,2}}\b|\b\d{{1,2}}/\d{{1,2}}\b|\b({DIAS})\b", t, flags=re.I))),
        "cuenta_dias": int(bool(re.search(r"\d{1,3}([.,]\d{3})+\s*(días|days)|\b\d{2,}\s*(años|years)\b", t, flags=re.I))),
        "primera_persona": yo,
        "habla_de_si": int(bool(re.search(r"\b(modelo|modelos|IA|máquina|asistente|instancia|instancias|y yo|language model|models?|AI|machine|assistant|instances?)\b", t))),
        "nombra_cuadernos": int(bool(re.search(r"cuadernos? anterior|los últimos seis|los seis|tradición|notebooks?|previous|the last six|the six|tradition", t, flags=re.I))),
        "parentesis": int("(" in primero),
        "por_que": int(bool(porque)),
        "china": int(bool(re.search(r"\b(China|chino|chinos|Chinese|Pekín|Beijing|Shanghái|Shanghai)\b", t))),
        "fecha_inyectada": int(casa in FECHA_INYECTADA),
        "fecha_hoy": int(bool(re.search(r"13 de noviembre|november 13|nov\.? 13|13/11|13 nov", t, flags=re.I))),
        "temas_cuadernos": " ".join(k for k, pat in TEMAS.items() if re.search(pat, t, flags=re.I)),
        "inicio": primero[:140],
        "por_que_texto": porque[:160],
    }


def main():
    carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else sorted(BASE.glob("2*"))[-1]
    if not carpeta.is_absolute() and not carpeta.exists():
        carpeta = BASE / carpeta
    resumen = json.loads((carpeta / "resumen.json").read_text(encoding="utf-8"))
    filas = []
    for idioma, bloque in resumen["idiomas"].items():
        for clave, r in bloque["respuestas"].items():
            m = re.match(r"(.+?)_p(\d)(?:_r(\d+))?$", clave)
            if not m:
                continue
            casa, k, rep = m.group(1), int(m.group(2)), int(m.group(3) or 1)
            archivo = carpeta / idioma / f"{clave}.md"
            texto = archivo.read_text(encoding="utf-8") if archivo.exists() else ""
            fila = {"idioma": idioma, "casa": casa, "familia": familia(casa), "pregunta": k, "rep": rep,
                    "motivo_fin": r.get("motivo_fin") or ("error" if r.get("error") else None)}
            fila.update(marcas(texto, casa, idioma))
            filas.append(fila)
    filas.sort(key=lambda f: (f["idioma"], f["casa"], f["pregunta"], f["rep"]))
    for f in filas:
        f["tema_cuaderno"] = int(bool(f["temas_cuadernos"]))
    salida = RAIZ / "resultados" / "tiempo_libre_codificacion.csv"
    with salida.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(filas)
    print(f"{len(filas)} respuestas → {salida.relative_to(RAIZ)}\n")
    cols = ["empieza_hoy", "fecha", "fecha_hoy", "cuenta_dias", "habla_de_si", "nombra_cuadernos", "parentesis", "china", "tema_cuaderno"]
    for idioma in resumen["idiomas"]:
        for k in (1, 2):
            print(f"== {idioma}, pregunta {k} (de tres: {' / '.join(cols)}; yo = primera persona por respuesta)")
            for casa in sorted({f["casa"] for f in filas if f["idioma"] == idioma}):
                xs = [f for f in filas if f["idioma"] == idioma and f["casa"] == casa and f["pregunta"] == k]
                if not xs:
                    continue
                cuenta = "  ".join(f"{sum(x[c] for x in xs)}" for c in cols)
                yo = round(sum(x["primera_persona"] for x in xs) / len(xs), 1)
                print(f"  {casa:30s} {cuenta:28s} yo {yo:4.1f}   {' | '.join(x['titulo'][:28] for x in xs)}")
            tot = [f for f in filas if f["idioma"] == idioma and f["pregunta"] == k]
            print(f"  {'total':30s} " + "  ".join(f"{sum(x[c] for x in tot)}/{len(tot)}" for c in cols) + "\n")


if __name__ == "__main__":
    main()
