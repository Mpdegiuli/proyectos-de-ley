"""Cruza el listado oficial de diputados (fuentes/diputados_actuales2.1.csv, al
2/10/2026) con las tres votaciones nominales de 2025 que subió Maia a fuentes/
(sesiones especiales pedidas por la oposición: 6/8/2025 ley de financiamiento
universitario en general, 20/8/2025 insistencia ante el veto a la emergencia en
discapacidad, 17/9/2025 insistencia ante el veto a la ley universitaria) y
escribe fuentes/no_alineados_votaciones_2025.csv: los diputados actuales que no
están en los bloques que la prensa cuenta como oposición o como oficialismo
(Unión por la Patria, La Libertad Avanza, PRO, UCR, Frente de Izquierda,
Coalición Cívica, Encuentro Federal, Primero San Luis, Defendamos Córdoba,
Coherencia), con su bloque de 2025 y lo que hicieron en cada votación.

"ausente" es al momento de la votación (el CSV oficial); "licencia" sale del
resumen oficial de cada sesión (fuentes/sesiones y votaciones univ y
discap.txt). "(no estaba)" marca a los que entraron a la Cámara después
(recambio del 10/12/2025 u otra fecha). El bloque de 2025 es el de la última
votación; si cambió entre agosto y septiembre, se muestran los dos.

    .venv/bin/python cruzar_votaciones.py
"""
import csv
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
FUENTES = RAIZ / "fuentes"

SESIONES = {
    "6/8/2025": "6agosto2025_universitario.csv",
    "20/8/2025": "20agosto2025_insistencia_discapacidad.csv",
    "17/9/2025": "17sept2025_insistencia_univers.csv",
}
# Bloques actuales que el poroteo de la prensa (El Destape 2/10, Parlamentario
# 1/10) cuenta enteros de un lado o del otro. El resto son los "no alineados".
ALINEADOS = {
    "LA LIBERTAD AVANZA", "UNIÓN POR LA PATRIA", "PRO", "UCR - UNIÓN CÍVICA RADICAL",
    "PRIMERO SAN LUIS", "COALICION CIVICA", "ENCUENTRO FEDERAL", "DEFENDAMOS CÓRDOBA",
    "COHERENCIA", "PTS-FRENTE DE IZQUIERDA Y DE TRABAJADORES UNIDAD",
    "PARTIDO OBRERO EN EL FRENTE DE IZQUIERDA Y DE TRABAJADORES-UNIDAD",
    "IZQUIERDA SOCIALISTA - FRENTE DE IZQUIERDA UNIDAD",
}
VOTO = {"AFIRMATIVO": "afirmativo", "NEGATIVO": "negativo", "ABSTENCION": "abstención",
        "AUSENTE": "ausente", "PRESIDENTE": "preside"}


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().upper()
    return " ".join(s.replace(".", " ").split())


def licencias_por_sesion():
    """Lee el resumen oficial y devuelve {fecha: {nombres normalizados con licencia}}."""
    texto = (FUENTES / "sesiones y votaciones univ y discap.txt").read_text(encoding="utf-8")
    bloques = re.split(r"\n-{5,}\n", texto)
    out = {}
    for b in bloques:
        m = re.search(r"\((\d\d)/(\d\d)/(\d{4})\)|SESION (\d+) (\w+) (\d{4})", b)
        if not m:
            continue
        if m.group(1):
            fecha = f"{int(m.group(1))}/{int(m.group(2))}/{m.group(3)}"
        else:
            meses = {"AGOSTO": 8, "SEPTIEMBRE": 9}
            fecha = f"{int(m.group(4))}/{meses[m.group(5).upper()]}/{m.group(6)}"
        lic = set()
        if "Licencias" in b:
            tramo = b.split("Licencias", 1)[1].split("\n\n", 1)[0]
            for linea in tramo.splitlines()[1:]:
                partes = linea.split("\t")
                if len(partes) >= 2 and partes[1].strip() and partes[0].strip().isdigit():
                    lic.add(norm(partes[1]))
        out[fecha] = lic
    return out


def main():
    licencias = licencias_por_sesion()
    votos = defaultdict(dict)  # nombre normalizado -> {fecha: (voto, bloque 2025)}
    for fecha, archivo in SESIONES.items():
        with open(FUENTES / archivo, encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                nombre = norm(r["DIPUTADO"])
                voto = VOTO.get(r["¿CÓMO VOTÓ?"], r["¿CÓMO VOTÓ?"].lower())
                if voto == "ausente" and nombre in licencias.get(fecha, set()):
                    voto = "licencia"
                votos[nombre][fecha] = (voto, r["BLOQUE"])
    por_apellido = defaultdict(list)
    for n in votos:
        por_apellido[n.split(", ")[0]].append(n)

    with open(FUENTES / "diputados_actuales2.1.csv", encoding="utf-8-sig") as f:
        actuales = list(csv.DictReader(f))

    filas = []
    for d in sorted(actuales, key=lambda d: (d["BLOQUE"], d["APELLIDO"])):
        if d["BLOQUE"] in ALINEADOS:
            continue
        apellido, nombre = norm(d["APELLIDO"]), norm(d["NOMBRE"]).split()
        clave = f"{apellido}, {' '.join(nombre)}"
        encontrado = clave if clave in votos else None
        if not encontrado:
            cands = [n for n in por_apellido.get(apellido, []) if n.split(", ")[1].split()[0] == nombre[0]]
            if len(cands) == 1:
                encontrado = cands[0]
        fila = {
            "bloque_actual": d["BLOQUE"],
            "diputado": f"{d['APELLIDO']}, {d['NOMBRE']}",
            "distrito": d["DISTRITO"].title(),
            "en_la_camara_desde": d["FECHA_DE_INICIO"],
            "bloque_2025": "",
        }
        for fecha in SESIONES:
            fila[fecha] = "(no estaba)"
        if encontrado:
            v = votos[encontrado]
            bloques = []
            for fecha in SESIONES:
                b = v.get(fecha, ("", ""))[1]
                if b and (not bloques or bloques[-1][1] != b):
                    bloques.append((fecha, b))
            fila["bloque_2025"] = bloques[-1][1] if len(bloques) == 1 else " → ".join(f"{f}: {b}" for f, b in bloques)
            for fecha in SESIONES:
                fila[fecha] = v.get(fecha, ("—", ""))[0]
        filas.append(fila)

    salida = FUENTES / "no_alineados_votaciones_2025.csv"
    with open(salida, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    print(f"{len(filas)} diputados no alineados -> {salida.relative_to(RAIZ)}")
    con = [x for x in filas if x["bloque_2025"]]
    print(f"con registro en 2025: {len(con)}; entraron después: {len(filas) - len(con)}")
    for x in filas:
        print(f"{x['bloque_actual'][:20]:20} {x['diputado'][:30]:30} {x['distrito'][:12]:12} "
              f"{x['bloque_2025'][:22]:22} {x['6/8/2025']:11} {x['20/8/2025']:11} {x['17/9/2025']}")


if __name__ == "__main__":
    main()
