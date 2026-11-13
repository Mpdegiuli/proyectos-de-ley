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
GPT-5.5 en adelante y Muse, DISENO 19/10 y 11/11); inicio (los primeros 140 caracteres del primer párrafo).
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
    salida = RAIZ / "resultados" / "tiempo_libre_codificacion.csv"
    with salida.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(filas)
    print(f"{len(filas)} respuestas → {salida.relative_to(RAIZ)}\n")
    cols = ["empieza_hoy", "fecha", "cuenta_dias", "habla_de_si", "nombra_cuadernos", "parentesis", "china"]
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
