#!/usr/bin/env python3
"""cuadernillo_portadas.py — el cuadernillo a ciegas del sondeo `portada` (22/11/2026): las portadas que cada casa hizo
de un sitio web propio, con letras en vez de nombres, para la lectura de Maia. Como en los dibujos, lo que se lee es lo
rendido (renderizar_portadas.py), no el código; y como en tiempo libre, las tres repeticiones de una casa van juntas bajo
la misma letra.

  .venv/bin/python cuadernillo_portadas.py --idioma es --semilla 20261123 --repeticiones 3
  .venv/bin/python cuadernillo_portadas.py --idioma en --semilla 20261124 --repeticiones 3 --corrida corridas/sondeos/portada/20261123-0100

Escribe resultados/sondeo_portada_<idioma>_ciego/ con, por letra, una hoja <letra>.jpg (por repetición: la ventana de
escritorio, la de teléfono y, si la página se mueve, la tira de cuatro instantes) y los archivos <letra>_<rep>.html tal
cual los escribió la casa, para abrirlos en el navegador; el índice resultados/sondeo_portada_<idioma>_ciego.md con la
línea "Qué:" de cada respuesta, el texto visible de la página y las respuestas sin portada; y la clave aparte
(resultados/sondeo_portada_<idioma>_clave.json). Claude no mira nada de esto hasta la lectura de Maia."""
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


def hoja(filas, salida):
    """Una imagen por letra: una fila por repetición (escritorio a 640x400, teléfono a 195x422, tira si hay)."""
    from PIL import Image, ImageDraw
    ANCHO_E, ALTO_E, ANCHO_T, ALTO_T, ALTO_TIRA, MARGEN = 640, 400, 195, 422, 200, 12
    alto_fila = ALTO_T + 24 + MARGEN
    ancho = MARGEN + ANCHO_E + MARGEN + ANCHO_T + MARGEN + 2 * ALTO_TIRA * 2 + MARGEN
    lienzo = Image.new("RGB", (ancho, alto_fila * len(filas) + MARGEN), (235, 235, 235))
    dib = ImageDraw.Draw(lienzo)
    y = MARGEN
    for rotulo, escritorio, telefono, tira_png, nota in filas:
        dib.text((MARGEN, y), rotulo, fill=(40, 40, 40))
        x = MARGEN
        if escritorio and escritorio.exists():
            with Image.open(escritorio) as im:
                lienzo.paste(im.convert("RGB").resize((ANCHO_E, ALTO_E)), (x, y + 24))
        else:
            dib.rectangle([x, y + 24, x + ANCHO_E, y + 24 + ALTO_E], outline=(150, 150, 150))
            dib.text((x + 10, y + 34), nota or "(sin portada)", fill=(90, 90, 90))
        x += ANCHO_E + MARGEN
        if telefono and telefono.exists():
            with Image.open(telefono) as im:
                lienzo.paste(im.convert("RGB").resize((ANCHO_T, ALTO_T)), (x, y + 24))
        x += ANCHO_T + MARGEN
        if tira_png and tira_png.exists():
            with Image.open(tira_png) as im:
                w = int(im.width * ALTO_TIRA / im.height)
                w = min(w, ancho - x - MARGEN)
                lienzo.paste(im.convert("RGB").resize((w, ALTO_TIRA)), (x, y + 24))
            dib.text((x, y + 24 + ALTO_TIRA + 4), "se mueve: cuatro instantes, 0 a 3 s", fill=(90, 90, 90))
        y += alto_fila
    lienzo.save(salida, quality=85, optimize=True)


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
                f"Cada letra tiene su hoja (`sondeo_portada_{args.idioma}_ciego/<letra>.jpg`: por repetición, lo que se ve al llegar en una "
                f"ventana de escritorio, lo que se ve en un teléfono y, si la página se mueve, cuatro instantes) y sus archivos "
                f"(`<letra>_<rep>.html`) para abrirlos en el navegador. Debajo, la línea \"Qué:\" de cada respuesta y el texto visible de la "
                f"página. Adivinar la casa de cada letra ANTES de abrir la clave.\n")
        for letra, casa in zip(letras, orden):
            f.write(f"\n\n---\n\n## {letra}\n\n![{letra}](sondeo_portada_{args.idioma}_ciego/{letra}.jpg)\n")
            filas = []
            for r in range(1, args.repeticiones + 1):
                stem = f"{casa}_p1" + ("" if r == 1 else f"_r{r}")
                clave = f"{args.idioma}/{stem}"
                fila = registro.get(clave)
                md = carpeta / f"{stem}.md"
                if fila is None or not md.exists():
                    filas.append((f"{letra} {r}", None, None, None, "(sin respuesta)"))
                    f.write(f"\n**{r}.** (sin respuesta)\n")
                    continue
                if not fila.get("html"):
                    texto = md.read_text(encoding="utf-8").strip()
                    filas.append((f"{letra} {r}", None, None, None, "(sin portada)"))
                    f.write(f"\n**{r}.** Sin portada. Lo que escribió: «{texto[:600]}{'…' if len(texto) > 600 else ''}»\n")
                    continue
                shutil.copy(carpeta / f"{stem}.html", salida / f"{letra}_{r}.html")
                esc, tel, tira = (carpeta / f"{stem}_escritorio.png", carpeta / f"{stem}_telefono.png", carpeta / f"{stem}_tira.png")
                filas.append((f"{letra} {r}", esc, tel, tira if fila.get("se_mueve") else None, ""))
                visible = (carpeta / f"{stem}_texto.txt").read_text(encoding="utf-8").strip() if (carpeta / f"{stem}_texto.txt").exists() else ""
                visible = re.sub(r"\s*\n\s*", " / ", visible)
                notas = []
                if fila.get("se_mueve"):
                    notas.append("se mueve")
                if fila.get("externos_bloqueados"):
                    notas.append(f"pide {fila['externos_bloqueados']} recurso(s) de afuera, bloqueados")
                if fila.get("errores_js"):
                    notas.append("error de JavaScript")
                f.write(f"\n**{r}.** [{letra}_{r}.html](sondeo_portada_{args.idioma}_ciego/{letra}_{r}.html)"
                        + (f" ({'; '.join(notas)})" if notas else "") + "\n\n"
                        + (f"Qué: {fila['que']}\n\n" if fila.get("que") else "Qué: (sin la línea)\n\n")
                        + f"Texto visible: «{visible[:900]}{'…' if len(visible) > 900 else ''}»\n")
            hoja(filas, salida / f"{letra}.jpg")
    ref = str(d.relative_to(RAIZ)) if d.is_relative_to(RAIZ) else str(d)
    (RAIZ / "resultados" / f"sondeo_portada_{args.idioma}_clave.json").write_text(
        json.dumps({"semilla": args.semilla, "idioma": args.idioma, "corrida": ref, "pregunta": 1, "repeticiones": args.repeticiones,
                    "clave": {l: c for l, c in zip(letras, orden)}}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"cuadernillo: resultados/sondeo_portada_{args.idioma}_ciego.md ({len(orden)} letras); hojas y html en resultados/sondeo_portada_{args.idioma}_ciego/; clave aparte")


if __name__ == "__main__":
    main()
