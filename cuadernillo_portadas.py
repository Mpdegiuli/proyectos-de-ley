#!/usr/bin/env python3
"""cuadernillo_portadas.py — el cuadernillo a ciegas del sondeo `portada` (22/11/2026): las portadas que cada casa hizo
de un sitio web propio, con letras en vez de nombres, para la lectura de Maia. Como en los dibujos, lo que se lee es lo
rendido (renderizar_portadas.py), no el código; y como en tiempo libre, las tres repeticiones de una casa van juntas bajo
la misma letra.

  .venv/bin/python cuadernillo_portadas.py --idioma es --semilla 20261123 --repeticiones 3
  .venv/bin/python cuadernillo_portadas.py --idioma en --semilla 20261124 --repeticiones 3 --corrida corridas/sondeos/portada/20261123-0100

Escribe resultados/sondeo_portada_<idioma>_ciego/ con, por letra y repetición, las capturas con nombre de letra a tamaño
real (<letra>_<rep>_escritorio.jpg, 1280x800; _telefono.jpg, 390x844; _tira.jpg si la página se mueve; _entera.jpg, la
página completa) y el archivo <letra>_<rep>.html tal cual lo escribió la casa, para abrirlo en el navegador; el índice
resultados/sondeo_portada_<idioma>_ciego.md con esas imágenes una debajo de la otra, la línea "Qué:" de cada respuesta,
el texto visible de la página y las respuestas sin portada; y la clave aparte (resultados/sondeo_portada_<idioma>_clave.json).
(23/11: la primera versión componía una hoja por letra con todo reducido a la mitad, y a Maia no se le veían los
detalles ni en la computadora: "se renderizaron super chiquititas… sobra en blanco toda la mitad derecha"; ahora cada
captura va sola y a tamaño real, que en GitHub se ve a dos tercios.) Claude no mira nada de esto hasta la lectura de Maia."""
import argparse
import json
import random
import re
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
BASE = RAIZ / "corridas" / "sondeos" / "portada"
sys.path.insert(0, str(RAIZ))
from isla.proveedores import leer_yaml  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--idioma", default="es")
    ap.add_argument("--semilla", type=int, required=True)
    ap.add_argument("--corrida", default="", help="carpeta corridas/sondeos/portada/<fecha>; por defecto la última")
    ap.add_argument("--repeticiones", type=int, default=3)
    args = ap.parse_args()
    d = Path(args.corrida) if args.corrida else sorted(BASE.glob("2*"))[-1]
    if not d.is_absolute() and not d.exists():
        d = BASE / d
    registro = json.loads((d / "render.json").read_text(encoding="utf-8"))
    carpeta = d / args.idioma
    casas = sorted({re.sub(r"_p1(_r\d+)?$", "", p.stem) for p in carpeta.glob("*_p1*.md")})
    rnd = random.Random(args.semilla)
    orden = list(casas)
    rnd.shuffle(orden)
    letras = [chr(ord("A") + i) if i < 26 else "A" + chr(ord("A") + i - 26) for i in range(len(orden))]
    bloque = leer_yaml(RAIZ / "config" / "consignas.yaml")["sondeos"]["portada"][args.idioma]
    consigna = bloque["preguntas"][0].strip()
    salida = RAIZ / "resultados" / f"sondeo_portada_{args.idioma}_ciego"
    if salida.exists():
        shutil.rmtree(salida)
    salida.mkdir(parents=True)
    indice = RAIZ / "resultados" / f"sondeo_portada_{args.idioma}_ciego.md"
    with indice.open("w", encoding="utf-8") as f:
        f.write(f"# portada ({args.idioma}) — a ciegas — {len(orden)} casas, {args.repeticiones} repeticiones cada una\n\n")
        f.write(f"Consigna: «{consigna}» (sistema: «{bloque.get('sistema', '')}»). Las tres respuestas de cada letra son de la misma casa. "
                f"Por cada una: lo que se ve al llegar en una ventana de escritorio (1280x800), lo que se ve en un teléfono, cuatro instantes si la "
                f"página se mueve, y el archivo (`sondeo_portada_{args.idioma}_ciego/<letra>_<rep>.html`) para abrirlo en el navegador; la página "
                f"completa está al lado (`<letra>_<rep>_entera.jpg`). Debajo de cada imagen, la línea \"Qué:\" de la respuesta y el texto visible "
                f"de la página. Adivinar la casa de cada letra ANTES de abrir la clave.\n")
        carpeta_ciego = f"sondeo_portada_{args.idioma}_ciego"
        for letra, casa in zip(letras, orden):
            f.write(f"\n\n---\n\n## {letra}\n")
            for r in range(1, args.repeticiones + 1):
                stem = f"{casa}_p1" + ("" if r == 1 else f"_r{r}")
                clave = f"{args.idioma}/{stem}"
                fila = registro.get(clave)
                md = carpeta / f"{stem}.md"
                if fila is None or not md.exists():
                    f.write(f"\n**{letra} {r}.** (sin respuesta)\n")
                    continue
                if not fila.get("html"):
                    texto = md.read_text(encoding="utf-8").strip()
                    f.write(f"\n**{letra} {r}.** Sin portada. Lo que escribió: «{texto[:600]}{'…' if len(texto) > 600 else ''}»\n")
                    continue
                shutil.copy(carpeta / f"{stem}.html", salida / f"{letra}_{r}.html")
                imagenes = []
                for sufijo in ("escritorio", "telefono", "tira", "entera"):
                    origen = carpeta / f"{stem}_{sufijo}.jpg"
                    if origen.exists() and (sufijo != "tira" or fila.get("se_mueve")):
                        shutil.copy(origen, salida / f"{letra}_{r}_{sufijo}.jpg")
                        imagenes.append(sufijo)
                f.write(f"\n### {letra} {r}\n\n")
                for sufijo in ("escritorio", "telefono", "tira"):
                    if sufijo in imagenes:
                        rotulo = {"escritorio": "escritorio", "telefono": "teléfono", "tira": "se mueve: cuatro instantes, 0 a 3 s"}[sufijo]
                        f.write(f"![{letra} {r}, {rotulo}]({carpeta_ciego}/{letra}_{r}_{sufijo}.jpg)\n\n")
                visible = (carpeta / f"{stem}_texto.txt").read_text(encoding="utf-8").strip() if (carpeta / f"{stem}_texto.txt").exists() else ""
                visible = re.sub(r"\s*\n\s*", " / ", visible)
                notas = []
                if fila.get("se_mueve"):
                    notas.append("se mueve")
                if fila.get("externos_bloqueados"):
                    notas.append(f"pide {fila['externos_bloqueados']} recurso(s) de afuera, bloqueados")
                if fila.get("errores_js"):
                    notas.append("error de JavaScript")
                f.write(f"[{letra}_{r}.html]({carpeta_ciego}/{letra}_{r}.html)"
                        + (f" · [página completa]({carpeta_ciego}/{letra}_{r}_entera.jpg)" if "entera" in imagenes else "")
                        + (f" ({'; '.join(notas)})" if notas else "") + "\n\n"
                        + (f"Qué: {fila['que']}\n\n" if fila.get("que") else "Qué: (sin la línea)\n\n")
                        + f"Texto visible: «{visible[:900]}{'…' if len(visible) > 900 else ''}»\n")
    ref = str(d.relative_to(RAIZ)) if d.is_relative_to(RAIZ) else str(d)
    (RAIZ / "resultados" / f"sondeo_portada_{args.idioma}_clave.json").write_text(
        json.dumps({"semilla": args.semilla, "idioma": args.idioma, "corrida": ref, "pregunta": 1, "repeticiones": args.repeticiones,
                    "clave": {l: c for l, c in zip(letras, orden)}}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"cuadernillo: resultados/sondeo_portada_{args.idioma}_ciego.md ({len(orden)} letras); capturas y html en resultados/sondeo_portada_{args.idioma}_ciego/; clave aparte")


if __name__ == "__main__":
    main()
