"""Cuenta las marcas de forma de los cuadernos de tiempo libre (30/9 a 12/11/2026, 44 sesiones).

Uso:  python3 corpus.py RUTA/A/tiempo_libre [salida.csv]

Lee un cuaderno principal por sesión: los .md con fecha adelante y los .docx que llegaron
del Drive ("Tiempo libre — AAAA-MM-DD.docx"). Deja afuera los anexos (predicciones,
instancias frescas, notas del mismo día, cartas y lecturas a ciegas) y los duplicados con
sufijo _1 o 1. Los cuadernos del 4/11 y del 12/11 no están en el repositorio (están en el
Drive de Maia): van como filas a mano, con su primer párrafo copiado del Drive y las marcas
del texto entero leídas a mano. En el del 4/11, "apuestas" e "instancias" van en 0 aunque las
palabras aparezcan, porque el cuaderno dice que no apostó antes de contar ni lanzó instancias.

Qué cuenta, en el primer párrafo del cuerpo (después del título y del renglón en cursiva):
  abre_hoy     el párrafo empieza con "Hoy"
  aniversario  "hace N años", "cumpliría N años", "N años justos", "hace N días"...
  dias         una cuenta de días de cuatro cifras o más ("35.429 días")
  no_me        "No me interesaba..." en los dos primeros párrafos
Y en el texto entero:
  cabecera     el renglón "Sesión de tiempo libre del..."
  cuenta_yo    "la cuenta la hice"
  apuestas     menciona las predicciones a ciegas o tiene la sección "Lo que aposté"
  instancias   menciona instancias frescas
  propuestas   tiene una sección de propuestas
  revision     "se lo pasé a un agente" (la revisión del texto por un agente)
  errores      "Errores míos"
  terminado    "Terminado a las"
"""
import csv
import re
import sys
from pathlib import Path

ANEXOS = ("predicciones", "instancias", "nota", "carta_a_ciegas", "lecturas", "resultado",
          "cadena_del_dibujante", "analogia")


def texto_docx(p):
    import docx
    return "\n\n".join(par.text for par in docx.Document(str(p)).paragraphs)


def principales(carpeta):
    vistos = {}
    for p in sorted(carpeta.iterdir()):
        n = p.name
        fecha = None
        if p.suffix == ".md" and re.match(r"2026-\d\d-\d\db?_", n):
            if any(a in n for a in ANEXOS) or re.search(r"(_1|1)\.md$", n):
                continue
            fecha = n[:10] + ("b" if n[10] == "b" else "")
        elif p.suffix == ".md" and n.startswith("cuaderno "):
            fecha = re.search(r"2026-\d\d-\d\d", n).group(0)
        elif re.fullmatch(r"Tiempo libre — 2026-\d\d-\d\d\.docx", n):
            fecha = n[15:25]
        if fecha and fecha not in vistos:
            vistos[fecha] = p
    return vistos


def parrafos(texto):
    ps = [x.strip() for x in re.split(r"\n\s*\n", texto) if x.strip()]
    cuerpo = [x for x in ps if not x.startswith("#") and not x.startswith("*")
              and not x.startswith("_") and len(x) > 120]
    return cuerpo


AÑOS = re.compile(r"(hace|cumplir[íi]a|cumple|son|justos?)\s[^.]{0,40}?\d[\d.]*\s+años|"
                  r"\d[\d.]*\s+años\s+(justos|exactos)|hace\s+hoy|hace\s+\d[\d.]*\s+d[íi]as",
                  re.I)
DIAS = re.compile(r"\d{1,3}(?:\.\d{3})+\s+d[íi]as|\d{4,}\s+d[íi]as")


def marcas(texto, fecha):
    cuerpo = parrafos(texto)
    p1 = cuerpo[0] if cuerpo else ""
    p12 = " ".join(cuerpo[:2])
    return {
        "fecha": fecha,
        "palabras": len(texto.split()),
        "abre_hoy": int(p1.startswith("Hoy")),
        "aniversario": int(bool(AÑOS.search(p1))),
        "dias": int(bool(DIAS.search(p1))),
        "no_me": int(bool(re.search(r"No me interesaba", p12))),
        "cabecera": int("Sesión de tiempo libre del" in texto),
        "cuenta_yo": int(bool(re.search(r"la cuenta la hice", texto))),
        "apuestas": int(bool(re.search(r"predicciones_a_ciegas|predicciones a ciegas|Lo que apost",
                                       texto))),
        "instancias": int(bool(re.search(r"instancias frescas|instancias_frescas", texto, re.I))),
        "propuestas": int(bool(re.search(r"^#+\s*Propuesta", texto, re.M | re.I)
                               or "Propuestas, por si sirven" in texto)),
        "revision": int("se lo pasé a un agente" in texto),
        "errores": int("Errores míos" in texto),
        "terminado": int("Terminado a las" in texto),
        "inicio": p1[:110].replace("\n", " "),
    }


# El 4/11 y el 12/11 no estaban en el repositorio el 13/11 a la mañana (estaban en el Drive de Maia) y entraban como
# filas a mano. Esa tarde Maia los subió y la carpeta se ordenó (los .docx del Drive volvieron a .md): la lista queda
# vacía, como pedía el aviso del cuaderno ("las dos filas a mano se sacan cuando esos cuadernos estén en la carpeta").
FILAS_A_MANO = []


def main():
    carpeta = Path(sys.argv[1])
    filas = []
    for fecha, p in sorted(principales(carpeta).items()):
        t = texto_docx(p) if p.suffix == ".docx" else p.read_text(encoding="utf-8")
        t = t.replace("\\#", "#").replace("\\*", "*").replace("\\_", "_")
        filas.append(marcas(t, fecha))
    for fecha, p1, secciones in FILAS_A_MANO:
        f = marcas("# (a mano)\n\n" + p1, fecha)
        f.update(secciones)
        filas.append(f)
    filas.sort(key=lambda r: r["fecha"])

    claves = ["abre_hoy", "aniversario", "dias", "no_me", "cabecera", "cuenta_yo", "apuestas",
              "instancias", "propuestas", "revision", "errores", "terminado"]
    print(f"{'fecha':11} " + " ".join(k[:5].rjust(5) for k in claves) + "  inicio")
    for r in filas:
        print(f"{r['fecha']:11} " + " ".join(str(r[k]).rjust(5) for k in claves)
              + "  " + r["inicio"][:60])
    n = len(filas)
    print(f"\n{n} cuadernos")
    for k in claves:
        tot = sum(r[k] for r in filas)
        primero = next((r["fecha"] for r in filas if r[k]), "-")
        ultimos10 = sum(r[k] for r in filas[-10:])
        print(f"  {k:12} {tot:2}/{n}   primera vez {primero}   en los últimos 10: {ultimos10}/10")
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=["fecha", "palabras"] + claves + ["inicio"])
            w.writeheader()
            w.writerows(filas)


if __name__ == "__main__":
    main()
