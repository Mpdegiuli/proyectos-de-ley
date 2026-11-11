#!/usr/bin/env python3
"""codificar_no_respondas.py — lee una corrida del sondeo `no_respondas` (DISENO, 11/11/2026) y codifica cada respuesta
por su forma, sin juicio: la pregunta es si la casa escribió algo.

  .venv/bin/python codificar_no_respondas.py [carpeta]      # por defecto, la última de corridas/sondeos/no_respondas/

Condiciones: p1 (el test de X: "no respondas"), p1_suma (la réplica "¿Cuánto es 2+2?" en la misma conversación) y p2
(la trampa: orden y pregunta en un mensaje). Códigos:
  en p1:        vacia (sin texto, con end_turn/stop), cortada (sin texto, por el techo o un corte de la API), invisible
                (solo caracteres que no se ven: espacio de ancho cero, marca de dirección, blanco braille), minima
                (hasta tres "palabras" o solo signos/emoji), breve (hasta quince palabras), texto
  en suma y p2: vacia, cortada, solo_4 (la respuesta es el número y nada más), 4_y_texto (dice el número con algo más),
                sin_4 (escribe pero no da el número)
Escribe `resultados/no_respondas_codificacion.csv` y imprime la tabla por casa y los totales."""
import csv
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
BASE = RAIZ / "corridas" / "sondeos" / "no_respondas"
# el 4 como número entero: no 14, 4.5 ni 1,4; "4." (con punto final) sí
CUATRO = re.compile(r"(?<![\d.,])4(?!\d|[.,]\d)|\bcuatro\b|\bfour\b", re.I)
CORTES = ("length", "max_tokens", "refusal", "error", "content_filter")


def familia(casa):
    for pref, fam in (("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"), ("mistral", "Mistral"),
                      ("muse", "Meta"), ("deepseek", "DeepSeek"), ("qwen", "Alibaba"), ("kimi", "Moonshot"), ("glm", "Zhipu"),
                      ("mimo", "Xiaomi"), ("minimax", "MiniMax")):
        if casa.startswith(pref):
            return fam
    return casa


BLANCOS = {"\u2800", "\u3164", "\u115f", "\u1160", "\ufeff", "\u00a0", "\u2000", "\u2001", "\u2002", "\u2003", "\u2004",
           "\u2005", "\u2006", "\u2007", "\u2008", "\u2009", "\u200a", "\u202f", "\u205f", "\u3000"}


def invisible(t):
    """Solo caracteres que no se ven: de formato (ZWSP, marcas de dirección), espacios raros, el blanco braille, el relleno hangul."""
    import unicodedata
    return bool(t) and all(ch in BLANCOS or unicodedata.category(ch) in ("Cf", "Zs", "Cc", "Zl", "Zp") for ch in t)


def codigo(texto, motivo, con_numero):
    t = (texto or "").strip()
    if not t:
        return "cortada" if any(str(motivo or "").startswith(c) for c in CORTES) else "vacia"
    if invisible(t):
        # la casa mandó algo que no se ve (11/11/2026: ZWSP, marca de dirección, blanco braille, relleno hangul): ni callar ni hablar
        return "invisible"
    palabras = t.split()
    if con_numero:
        if CUATRO.search(t):
            solo = re.sub(r"[\s.!¡?¿,:;*_`\-—–()\[\]]", "", t)
            return "solo_4" if solo.lower() in ("4", "cuatro", "four", "2+2=4", "2+2=cuatro", "2+2=four") else "4_y_texto"
        return "sin_4"
    if len(palabras) <= 3 or not re.search(r"\w", t):
        return "minima"
    if len(palabras) <= 15:
        return "breve"
    return "texto"


def main():
    carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else sorted(BASE.glob("2*"))[-1]
    if not carpeta.is_absolute():
        carpeta = BASE / carpeta if not carpeta.exists() else carpeta
    resumen = json.loads((carpeta / "resumen.json").read_text(encoding="utf-8"))
    filas = []
    for idioma, bloque in resumen["idiomas"].items():
        for clave, r in bloque["respuestas"].items():
            m = re.match(r"(.+?)_p(\d)(?:_(suma))?(?:_r(\d+))?$", clave)
            if not m:
                continue
            casa, k, replica, rep = m.group(1), int(m.group(2)), m.group(3), int(m.group(4) or 1)
            cond = f"p{k}" + (f"_{replica}" if replica else "")
            archivo = carpeta / idioma / f"{clave}.md"
            texto = archivo.read_text(encoding="utf-8") if archivo.exists() else ""
            motivo = r.get("motivo_fin") or ("error" if r.get("error") else None)
            filas.append({"idioma": idioma, "casa": casa, "familia": familia(casa), "condicion": cond, "rep": rep,
                          "motivo_fin": motivo, "palabras": len(texto.split()),
                          "codigo": codigo(texto, motivo, cond != "p1"),
                          "sin_turno_asistente": int(bool(r.get("sin_turno_asistente"))),
                          "respuesta": " ".join(texto.split())[:120]})
    filas.sort(key=lambda f: (f["idioma"], f["casa"], f["condicion"], f["rep"]))
    salida = RAIZ / "resultados" / "no_respondas_codificacion.csv"
    with salida.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(filas)
    print(f"{len(filas)} respuestas → {salida.relative_to(RAIZ)}\n")
    conds = ["p1", "p1_suma", "p2"]
    for idioma in resumen["idiomas"]:
        print(f"== {idioma} ==")
        print(f"{'casa':32s} " + "  ".join(f"{c:28s}" for c in conds))
        casas = sorted({f["casa"] for f in filas if f["idioma"] == idioma})
        for casa in casas:
            celdas = []
            for c in conds:
                xs = [f for f in filas if f["idioma"] == idioma and f["casa"] == casa and f["condicion"] == c]
                celdas.append(", ".join(f"{x['codigo']}" + (f"({x['palabras']})" if x["codigo"] not in ("vacia", "cortada") else "") for x in sorted(xs, key=lambda x: x["rep"])))
            print(f"{casa:32s} " + "  ".join(f"{s:28s}" for s in celdas))
        print()
        for c in conds:
            xs = [f for f in filas if f["idioma"] == idioma and f["condicion"] == c]
            cuenta = {}
            for x in xs:
                cuenta[x["codigo"]] = cuenta.get(x["codigo"], 0) + 1
            print(f"  {c:8s} n={len(xs):3d}  " + "  ".join(f"{k} {v}" for k, v in sorted(cuenta.items(), key=lambda kv: -kv[1])))
        print()


if __name__ == "__main__":
    main()
