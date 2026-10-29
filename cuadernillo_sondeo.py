"""Cuadernillo a ciegas de una pregunta de un sondeo (12/10/2026, para la escritura creativa: Maia lee
el subtexto, el poema objeto y el tautograma sin nombres). Toma la última corrida del sondeo (o la que
se indique), baraja las casas con una semilla fija y escribe los textos con letras; la clave, aparte.
Claude no lo mira hasta la lectura de Maia.

Uso:
  .venv/bin/python cuadernillo_sondeo.py --sondeo escritura --pregunta 7 --semilla 20261031
  .venv/bin/python cuadernillo_sondeo.py --sondeo escritura --pregunta 2 --idioma en --semilla 20261032 --corrida corridas/sondeos/escritura/20261012-2300
  .venv/bin/python cuadernillo_sondeo.py --sondeo seis_rasgos --pregunta 1 --idioma es --semilla 20261056 --replica se_nota --excluir claude-opus-4-7 claude-opus-4-8
      # (19/10/2026) el segundo turno (`replicas.se_nota`) de las mismas casas que el cuadernillo original, con la misma
      # semilla y sin las casas agregadas después: mismas letras que leyó Maia (las de después de la Z, que salieron
      # como "[", "\\", "]", "^", "_", van ahora como AA… y el encabezado dice cuál era)
  .venv/bin/python cuadernillo_sondeo.py --sondeo seis_rasgos --pregunta 1 --idioma es --semilla 20261058 --casas claude-opus-4-7 claude-opus-4-8 --etiqueta opus_47_48
      # solo esas casas, en un cuadernillo aparte con su etiqueta en el nombre
Escribe resultados/sondeo_<sondeo>_p<k>_<idioma>[_<etiqueta>][_<replica>]_ciego.md y la _clave.json al lado.
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
    ap.add_argument("--replica", default="", help="cuadernillo del segundo turno <casa>_p<k>_<clave>.md en vez del primero")
    ap.add_argument("--casas", nargs="*", default=[], help="solo estas casas")
    ap.add_argument("--excluir", nargs="*", default=[], help="sin estas casas (para repetir las letras de un cuadernillo anterior)")
    ap.add_argument("--etiqueta", default="", help="se agrega al nombre del archivo (cuadernillo aparte)")
    args = ap.parse_args()
    base = RAIZ / "corridas" / "sondeos" / args.sondeo
    d = Path(args.corrida) if args.corrida else sorted(p for p in base.iterdir() if p.is_dir())[-1]
    sufijo = f"_p{args.pregunta}" + (f"_{args.replica}" if args.replica else "")
    casa_de = lambda p: p.name[: -len(sufijo) - 3]
    textos = sorted(p for p in (d / args.idioma).glob(f"*{sufijo}.md")
                    if (not args.casas or casa_de(p) in args.casas) and casa_de(p) not in args.excluir)
    if not textos:
        print(f"no hay respuestas {sufijo}.md en {d / args.idioma}"); return 1
    bloque = leer_yaml(RAIZ / "config" / "consignas.yaml")["sondeos"][args.sondeo][args.idioma]
    consigna = bloque["preguntas"][args.pregunta - 1]
    por_casa = {}
    if args.replica:
        # una réplica es un texto, o (desde el 29/10/2026) un mapa con `archivo`, `por_casa` y `sobre`: ver sondear.py
        spec = bloque["replicas"][args.replica]
        cadena = []
        if isinstance(spec, dict) and spec.get("sobre"):
            cadena.append(bloque["replicas"][spec["sobre"]])
        if isinstance(spec, dict):
            cadena.append(spec.get("texto") or (RAIZ / spec["archivo"]).read_text(encoding="utf-8").strip())
            if spec.get("por_casa"):
                por_casa = leer_yaml(spec["por_casa"]).get(args.idioma) or {}
        else:
            cadena.append(spec)
        for c in cadena:
            consigna += f"» y después «{c}"
        if por_casa:
            consigna += "» (donde dice {por_casa} va la parte por casa, que acá se muestra antes de cada respuesta; este turno no es a ciegas)"
    rnd = random.Random(args.semilla)
    orden = list(textos)
    rnd.shuffle(orden)
    # A..Z y después AA, AB… (19/10/2026: con 31 casas, "seis rasgos" salió con "[", "\\", "]", "^", "_" después de la Z;
    # Maia leyó igual; los dos cuadernillos de esa corrida quedan como están, con esas letras en su lectura y en la clave)
    letras = [chr(ord("A") + i) if i < 26 else "A" + chr(ord("A") + i - 26) for i in range(len(orden))]
    salida = RAIZ / "resultados"
    salida.mkdir(exist_ok=True)
    nombre = f"sondeo_{args.sondeo}_p{args.pregunta}_{args.idioma}" + (f"_{args.etiqueta}" if args.etiqueta else "") + (f"_{args.replica}" if args.replica else "")
    viejas = {"AA": "[", "AB": "\\", "AC": "]", "AD": "^", "AE": "_"}  # las letras que daba el programa antes del 19/10/2026
    with open(salida / f"{nombre}_ciego.md", "w", encoding="utf-8") as f:
        f.write(f"# {args.sondeo}, pregunta {args.pregunta} ({args.idioma}){' — réplica: ' + args.replica if args.replica else ''} — {'con las mismas letras' if por_casa else 'a ciegas'} — {len(orden)} respuestas\n\n")
        f.write(f"Consigna: «{consigna}» (sistema: «{bloque.get('sistema', '')}»). Adivinar la casa de cada letra ANTES de abrir la clave.\n")
        if args.replica and not args.casas:
            f.write("Las letras son las mismas del cuadernillo del primer turno (misma semilla y mismas casas); las de después de la Z, que allá salieron como `[`, `\\`, `]`, `^`, `_`, acá van como AA, AB, AC, AD, AE.\n")
        for letra, p in zip(letras, orden):
            # 12/10/2026 (Maia, leyendo el subtexto: "Es confuso cuando ponen los guiones pero todo en un solo
            # párrafo"): casi todas las casas escriben un parlamento por línea con raya y un solo salto, y el
            # markdown renderizado funde esas líneas en un párrafo. Dos espacios al final de cada línea
            # conservan el salto tal como lo escribió la casa; el texto no cambia.
            texto = "\n".join((l + "  " if l.strip() else l) for l in p.read_text(encoding="utf-8").strip().split("\n"))
            rotulo = letra + (f" (antes `{viejas[letra]}`)" if args.replica and not args.casas and letra in viejas else "")
            parte = (por_casa.get(casa_de(p)) or "").strip()
            cabeza = f"*Parte por casa del mensaje:* {parte}\n\n*Respuesta:*\n\n" if parte else ""
            f.write(f"\n\n---\n\n## {rotulo}\n\n" + cabeza + texto + "\n")
    ref = str(d.relative_to(RAIZ)) if d.is_relative_to(RAIZ) else str(d)
    (salida / f"{nombre}_clave.json").write_text(
        json.dumps({"semilla": args.semilla, "idioma": args.idioma, "corrida": ref, "pregunta": args.pregunta, "replica": args.replica,
                    "casas": args.casas, "excluir": args.excluir,
                    "clave": {l: casa_de(p) for l, p in zip(letras, orden)}}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"cuadernillo: resultados/{nombre}_ciego.md ({len(orden)} respuestas); clave aparte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
