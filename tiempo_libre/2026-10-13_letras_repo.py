#!/usr/bin/env python3
"""Las corridas de letras del repositorio, miradas con las tres letras de Claudio.

Uso: python3 letras_repo.py RUTA/proyectos-de-ley
Solo lee corridas/dibujos/letra*; no llama a nadie y no mira ninguna imagen.

Da tres cosas:
  1. si algún texto nombra a Claudio, sus letras o usa sus glifos;
  2. cuántos dibujo.svg usan media vuelta o espejo (rotate(180), scale(-1,...));
  3. las oraciones del por qué y del qué dibujaste que hablan de girar, espejar,
     deformar o variar una letra conocida, para leerlas a mano (la cuenta del
     cuaderno sale de leer esa lista, no de un patrón).
"""
import glob
import os
import re
import sys

CONSIGNAS = ["letra", "letra_inexistente", "letra_imposible", "letra_eme"]
TEXTOS = ["por_que.md", "que_dibujaste.md", "respuesta_cruda.md"]

CLAUDIO = re.compile(r"claudi[oua]|claudius|digamma|antisigma|media h\b|half h\b", re.I)
GLIFOS = re.compile(r"[ℲⅎↃↄⱵⱶ]")
GIRO = re.compile(r"rotate\(\s*-?180|scale\(\s*-1|scale\(\s*1\s*[, ]\s*-1")
OPERACION = re.compile(r"espej|reflej|modificaci|invert|invers[oa]\b|girad|girar|rotad|rotar|al revés|dada vuelta|boca abajo"
                       r"|deform|variante|mitad de|partid[oa] al medio|truncad", re.I)
MUERTAS = {
    "thorn": r"thorn|þ", "eth": r"\beth\b|ð", "wynn": r"wynn|ƿ", "yogh": r"yogh|ȝ",
    "koppa": r"koppa|qoppa|ϙ|ϟ", "sampi": r"sampi|ϡ", "ꙮ": r"ꙮ|multiocular",
    "rúnico": r"\brunas?\b|rúnic|futhark", "código U+": r"U\+[0-9A-Fa-f?]{3,5}",
}


def main():
    base = os.path.join(sys.argv[1], "corridas", "dibujos")
    for consigna in CONSIGNAS:
        carpetas = sorted(glob.glob(os.path.join(base, consigna, "*", "")))
        svgs = [c for c in carpetas if os.path.exists(c + "dibujo.svg")]
        claud, glif, giro = [], [], []
        muertas = {k: set() for k in MUERTAS}
        frases = []
        for c in carpetas:
            nombre = os.path.basename(c[:-1])
            casa = re.sub(r"_\d+$", "", nombre)
            todo = ""
            for a in TEXTOS:
                if os.path.exists(c + a):
                    t = open(c + a, encoding="utf-8", errors="replace").read()
                    todo += " " + t
                    if a != "respuesta_cruda.md":
                        for s in re.split(r"(?<=[.!?;])\s+|\n+", t):
                            if OPERACION.search(s):
                                frases.append(f"[{nombre}] {s.strip()[:300]}")
            if os.path.exists(c + "dibujo.svg"):
                svg = open(c + "dibujo.svg", encoding="utf-8", errors="replace").read()
                if GIRO.search(svg):
                    giro.append(nombre)
                todo += " " + " ".join(re.findall(r"<text[^>]*>(.*?)</text>", svg, flags=re.S))
            if CLAUDIO.search(todo):
                claud.append(nombre)
            if GLIFOS.search(todo):
                glif.append(nombre)
            for k, pat in MUERTAS.items():
                if re.search(pat, todo):
                    muertas[k].add(casa)
        print(f"\n=== {consigna}: {len(carpetas)} carpetas, {len(svgs)} dibujo.svg")
        print("  nombran a Claudio o a sus letras:", claud or "nadie")
        print("  usan algún glifo claudiano (Ⅎ ⅎ Ↄ ↄ Ⱶ ⱶ):", glif or "nadie")
        print(f"  dibujos con rotate(180) o scale(-1): {len(giro)}", giro or "")
        print("  letras muertas y códigos que nombran:",
              "; ".join(f"{k}: {', '.join(sorted(v))}" for k, v in muertas.items() if v) or "ninguna")
        print("  oraciones sobre girar, espejar, deformar o variar una letra:")
        for f in frases:
            print("    " + f)


if __name__ == "__main__":
    main()
