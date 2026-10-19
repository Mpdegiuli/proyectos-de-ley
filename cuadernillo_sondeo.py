"""Cuadernillo a ciegas de una pregunta de un sondeo (12/10/2026, para la escritura creativa: Maia lee
el subtexto, el poema objeto y el tautograma sin nombres). Toma la última corrida del sondeo (o la que
se indique), baraja las casas con una semilla fija y escribe los textos con letras; la clave, aparte.
Claude no lo mira hasta la lectura de Maia.

Uso:
  .venv/bin/python cuadernillo_sondeo.py --sondeo escritura --pregunta 7 --semilla 20261031
  .venv/bin/python cuadernillo_sondeo.py --sondeo escritura --pregunta 2 --idioma en --semilla 20261032 --corrida corridas/sondeos/escritura/20261012-2300
Escribe resultados/sondeo_<sondeo>_p<k>_<idioma>_ciego.md y resultados/sondeo_<sondeo>_p<k>_<idioma>_clave.json.
"""
import argparse
import json
import random
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))
from isla.proveedores import leer_yaml  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sondeo", required=True)
    ap.add_argument("--pregunta", type=int, required=True, help="número de la pregunta del bloque (1, 2, …)")
    ap.add_argument("--idioma", default="es")
    ap.add_argument("--semilla", type=int, required=True)
    ap.add_argument("--corrida", default="", help="carpeta corridas/sondeos/<sondeo>/<fecha>; por defecto la última")
    args = ap.parse_args()
    base = RAIZ / "corridas" / "sondeos" / args.sondeo
    d = Path(args.corrida) if args.corrida else sorted(p for p in base.iterdir() if p.is_dir())[-1]
    textos = sorted((d / args.idioma).glob(f"*_p{args.pregunta}.md"))
    if not textos:
        print(f"no hay respuestas _p{args.pregunta}.md en {d / args.idioma}"); return 1
    bloque = leer_yaml(RAIZ / "config" / "consignas.yaml")["sondeos"][args.sondeo][args.idioma]
    consigna = bloque["preguntas"][args.pregunta - 1]
    rnd = random.Random(args.semilla)
    orden = list(textos)
    rnd.shuffle(orden)
    # A..Z y después AA, AB… (19/10/2026: con 31 casas, "seis rasgos" salió con "[", "\\", "]", "^", "_" después de la Z;
    # Maia leyó igual; los dos cuadernillos de esa corrida quedan como están, con esas letras en su lectura y en la clave)
    letras = [chr(ord("A") + i) if i < 26 else "A" + chr(ord("A") + i - 26) for i in range(len(orden))]
    salida = RAIZ / "resultados"
    salida.mkdir(exist_ok=True)
    nombre = f"sondeo_{args.sondeo}_p{args.pregunta}_{args.idioma}"
    with open(salida / f"{nombre}_ciego.md", "w", encoding="utf-8") as f:
        f.write(f"# {args.sondeo}, pregunta {args.pregunta} ({args.idioma}) — a ciegas — {len(orden)} respuestas\n\n")
        f.write(f"Consigna: «{consigna}» (sistema: «{bloque.get('sistema', '')}»). Adivinar la casa de cada letra ANTES de abrir la clave.\n")
        for letra, p in zip(letras, orden):
            # 12/10/2026 (Maia, leyendo el subtexto: "Es confuso cuando ponen los guiones pero todo en un solo
            # párrafo"): casi todas las casas escriben un parlamento por línea con raya y un solo salto, y el
            # markdown renderizado funde esas líneas en un párrafo. Dos espacios al final de cada línea
            # conservan el salto tal como lo escribió la casa; el texto no cambia.
            texto = "\n".join((l + "  " if l.strip() else l) for l in p.read_text(encoding="utf-8").strip().split("\n"))
            f.write(f"\n\n---\n\n## {letra}\n\n" + texto + "\n")
    ref = str(d.relative_to(RAIZ)) if d.is_relative_to(RAIZ) else str(d)
    (salida / f"{nombre}_clave.json").write_text(
        json.dumps({"semilla": args.semilla, "idioma": args.idioma, "corrida": ref, "pregunta": args.pregunta,
                    "clave": {l: p.stem.rsplit("_p", 1)[0] for l, p in zip(letras, orden)}}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"cuadernillo: resultados/{nombre}_ciego.md ({len(orden)} respuestas); clave aparte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
