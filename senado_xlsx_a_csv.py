"""Pasa a CSV la votación nominal del Senado del 14/3/2024 sobre el DNU 70/2023
(fuentes/Votacion_Nominal 8.xlsx, acta 8, exportada del sitio del Senado por
Maia) y agrega una columna sin ambigüedad: en esa votación "NEGATIVO" es votar
contra el DNU (rechazarlo) y "AFIRMATIVO" sostenerlo; ganó el negativo, 42 a
25 con 4 abstenciones y 1 ausente. Corrige una fila mal exportada (Recalde,
sin bloque, con las columnas corridas).

    .venv/bin/python senado_xlsx_a_csv.py   # escribe fuentes/senado_dnu70_20240314.csv
"""
import csv
from pathlib import Path

import openpyxl

RAIZ = Path(__file__).resolve().parent
ORIGEN = RAIZ / "fuentes" / "Votacion_Nominal 8.xlsx"
SALIDA = RAIZ / "fuentes" / "senado_dnu70_20240314.csv"
SENTIDO = {"NEGATIVO": "contra el DNU", "AFIRMATIVO": "a favor del DNU",
           "ABSTENCIÓN": "abstención", "AUSENTE": "ausente"}


def main():
    ws = openpyxl.load_workbook(ORIGEN, data_only=True).active
    filas = []
    for r in ws.iter_rows(min_row=8, values_only=True):
        if not r[0]:
            continue
        senador, bloque, provincia, voto = (str(x).strip() if x else "" for x in r[:4])
        if not voto and provincia in SENTIDO:  # fila corrida: falta el bloque
            senador, bloque, provincia, voto = senador, "", bloque, provincia
        if senador.startswith("RECALDE") and not bloque:
            bloque = "UNIDAD CIUDADANA"  # bloque de Recalde en marzo de 2024; la exportación lo omite
        filas.append({"senador": senador.title(), "bloque": bloque, "provincia": provincia.title(),
                      "voto": voto, "sentido": SENTIDO.get(voto, voto)})
    filas.sort(key=lambda f: (f["provincia"], f["senador"]))
    with open(SALIDA, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    from collections import Counter
    print(len(filas), dict(Counter(f["sentido"] for f in filas)), "->", SALIDA.relative_to(RAIZ))


if __name__ == "__main__":
    main()
