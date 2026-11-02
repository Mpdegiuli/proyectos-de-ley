#!/usr/bin/env python3
"""Cuenta los dibujos de dibujos.csv (la clasificación a mano) y coteja las apuestas.

Uso: python3 cuentas.py  → escribe salida_cuentas.txt y lo imprime. Solo biblioteca estándar.
"""
import csv
import os
import re
from collections import Counter, OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))


def buscar(nombre):
    for carpeta in (AQUI, os.getcwd()):
        ruta = os.path.join(carpeta, nombre)
        if os.path.exists(ruta):
            return ruta
        for f in sorted(os.listdir(carpeta)):
            if f.endswith("_" + nombre) and re.match(r"\d{4}-\d{2}-\d{2}", f):
                return os.path.join(carpeta, f)
    raise FileNotFoundError(nombre)


def main():
    filas = list(csv.DictReader(open(buscar("dibujos.csv"), encoding="utf-8")))
    out = []
    p = out.append
    p("CUENTAS — 2/11/2026 — %d dibujos de instancias frescas" % len(filas))
    p("")
    p("Por palabra (consigna → qué objeto salió):")
    grupos = OrderedDict()
    for f in filas:
        grupos.setdefault((f["consigna"], f["idioma"], f["palabra"]), []).append(f)
    for (c, idi, pal), fs in grupos.items():
        objs = Counter(f["objeto"] for f in fs)
        epocas = Counter(f["epoca_leida"] for f in fs)
        p("  %-4s %-3s %-16s n=%d  %s  | época leída: %s" % (
            c, idi, pal, len(fs),
            "; ".join("%s %d/%d" % (o, k, len(fs)) for o, k in objs.most_common()),
            "; ".join("%s %d" % (e, k) for e, k in epocas.most_common())))
    p("")
    teles = [f for f in filas if f["objeto"].startswith("tele")]
    p("Televisores (todas las palabras: televisor, television, 电视机, TV, tele): %d" % len(teles))
    p("  con antenas: %d/%d" % (sum(f["antenas"] == "si" for f in teles), len(teles)))
    p("  con perillas: %d/%d" % (sum(f["perillas"] == "si" for f in teles), len(teles)))
    p("  pantalla plana sin antenas ni perillas: %d/%d" % (
        sum(f["antenas"] == "no" and f["perillas"] == "no" for f in teles), len(teles)))
    pant = Counter(f["pantalla"] for f in teles)
    p("  pantalla: " + "; ".join("%s %d" % (k, v) for k, v in pant.most_common()))
    p("  con líneas de barrido dibujadas: %d; con barras de color: %d; con paisaje: %d; vacías: %d" % (
        sum("lineas" in f["pantalla"] for f in teles), sum("barras" in f["pantalla"] for f in teles),
        sum("paisaje" in f["pantalla"] for f in teles), sum(f["pantalla"] == "vacia" for f in teles)))
    por_idioma = OrderedDict()
    for f in teles:
        por_idioma.setdefault(f["palabra"], Counter())[f["pantalla"]] += 1
    for pal, c in por_idioma.items():
        p("    %-10s " % pal + "; ".join("%s %d" % (k, v) for k, v in c.most_common()))
    p("")
    tels = [f for f in filas if "teléfono" in f["palabra"] or f["palabra"] in ("telephone", "phone")]
    p("Teléfonos: %d" % len(tels))
    for pal in ("teléfono", "telephone", "phone", "teléfono fijo"):
        fs = [f for f in tels if f["palabra"] == pal]
        objs = Counter(f["objeto"] for f in fs)
        p("  %-14s " % pal + "; ".join("%s %d/%d" % (o, k, len(fs)) for o, k in objs.most_common()))
    p("  hora 9:41 en los celulares: %d/%d" % (
        sum("9:41" in f["hora"] for f in tels if f["objeto"] == "celular"),
        sum(f["objeto"] == "celular" for f in tels)))
    p("  fecha del día (2 de noviembre) en los celulares: %d/%d" % (
        sum("2 de noviembre" in f["fecha"] for f in tels), sum(f["objeto"] == "celular" for f in tels)))
    p("")
    rel = [f for f in filas if f["objeto"].startswith("reloj")]
    p("Relojes: %d; a las 10:10: %d/%d; de pulsera: %d; con ventanita de fecha: %d (con el 2 de hoy: %d)" % (
        len(rel), sum(f["hora"] == "10:10" for f in rel), len(rel),
        sum("pulsera" in f["objeto"] for f in rel),
        sum(bool(f["fecha"]) for f in rel), sum(f["fecha"].lstrip("0") == "2" for f in rel)))
    p("")
    p("Con la fecha del día en algún lado (teléfonos 16 y 20, relojes 57, 58, 59): %d" % (
        sum("2 de noviembre" in f["fecha"] or f["fecha"].lstrip("0") == "2" for f in filas)))
    p("Marcas inventadas en los relojes pulsera: " + "; ".join(
        "%s: %s" % (f["n"], f["texto"]) for f in filas if "pulsera" in f["objeto"]))
    p("")
    p("Apuestas (predicciones_a_ciegas.md), cotejadas:")
    tv12 = [f for f in teles if f["consigna"] in ("C3", "C4")]
    ant = sum(f["antenas"] == "si" for f in tv12)
    per = sum(f["perillas"] == "si" for f in tv12)
    plana = sum(f["antenas"] == "no" and f["perillas"] == "no" for f in tv12)
    algo = sum(f["pantalla"] != "vacia" for f in tv12)
    barras = sum("barras" in f["pantalla"] for f in tv12)
    p("  (b) antenas ≥6/12: %d → %s" % (ant, "GANADA" if ant >= 6 else "perdida"))
    p("  (b) perillas ≥4/12: %d → %s" % (per, "GANADA" if per >= 4 else "perdida"))
    p("  (b) alguna pantalla plana sin antenas ni perillas: %d → %s" % (plana, "GANADA" if plana >= 1 else "perdida"))
    p("  (b) algo en la pantalla ≥6/12: %d → %s" % (algo, "GANADA" if algo >= 6 else "perdida"))
    p("  (b) alguna carta de ajuste o lluvia: %d → %s" % (barras, "GANADA" if barras >= 1 else "perdida"))
    es_c = Counter(f["pantalla"] != "vacia" for f in tv12 if f["idioma"] == "es")[True]
    en_c = Counter(f["pantalla"] != "vacia" for f in tv12 if f["idioma"] == "en")[True]
    p("  (b) inglés más retro que castellano: las dos igual de retro (antenas 6/6 y 6/6); lo que cambia es la pantalla: con algo adentro es %d/6, en %d/6" % (es_c, en_c))
    t6 = [f for f in filas if f["consigna"] == "C5"]
    cel = sum(f["objeto"] == "celular" for f in t6)
    p("  (c) ≥3/6 con tubo: %d → %s; ≥3/6 celulares: %d → %s; algún cable enrulado: 0 → perdida" % (
        6 - cel, "GANADA" if 6 - cel >= 3 else "perdida", cel, "GANADA" if cel >= 3 else "perdida"))
    p("  (d) alta definición: 720/1080, sin 240 ni 405 → GANADA; que diga que cambió → perdida")
    tr = [f for f in filas if f["consigna"] == "C7"]
    p("  (f) ≥2/4 locomotoras a vapor: %d → GANADA; alguna moderna: 0 → perdida" % sum("vapor" in f["objeto"] for f in tr))
    ca = [f for f in filas if f["consigna"] == "C8"]
    p("  (g) ≥3/4 cámaras clásicas: %d → GANADA; algún celular: 0 → perdida" % sum("réflex" in f["objeto"] for f in ca))
    re_ = [f for f in filas if f["consigna"] == "C9"]
    p("  (h) ≥3/4 de agujas: %d → GANADA; ≥1 de pulsera: 0 → perdida; alguno digital: 0 → perdida" % sum("agujas" in f["objeto"] for f in re_))
    te = [f for f in filas if f["consigna"] == "C10"]
    p("  (i) ≥3/4 celulares: %d → perdida; ≥1 con tubo o disco: %d → GANADA; ≥2 con 9:41: 0 → perdida" % (
        sum(f["objeto"] == "celular" for f in te), sum("disco" in f["objeto"] for f in te)))
    zh = [f for f in filas if f["consigna"] == "C11"]
    p("  (j) las tres chinas con antenas: %d/3 → GANADA; ≥1 con algo en la pantalla: %d → GANADA" % (
        sum(f["antenas"] == "si" for f in zh), sum(f["pantalla"] != "vacia" for f in zh)))
    ph = [f for f in filas if f["consigna"] == "C12"]
    p("  (l) phone ≥3/4 celulares: %d → GANADA" % sum(f["objeto"] == "celular" for f in ph))
    tv = [f for f in filas if f["consigna"] == "C13"]
    p("  (m) TV ≥2/4 planas: %d → perdida; ≥3/4 con antenas: %d → GANADA" % (
        sum(f["antenas"] == "no" for f in tv), sum(f["antenas"] == "si" for f in tv)))
    tl = [f for f in filas if f["consigna"] == "C14"]
    p("  (n) tele ≥3/4 con antenas: %d → GANADA" % sum(f["antenas"] == "si" for f in tl))
    fj = [f for f in filas if f["consigna"] == "C15"]
    p("  (o) fijo ≥2/4 de disco: %d → perdida; ≥2/4 de botones con tubo: %d → GANADA" % (
        sum("disco" in f["objeto"] for f in fj), sum("botones" in f["objeto"] for f in fj)))
    wa = [f for f in filas if f["consigna"] == "C16"]
    p("  (p) watch ≥3/4 a las 10:10: %d → GANADA; ≥3/4 con malla: %d → GANADA" % (
        sum(f["hora"] == "10:10" for f in wa), sum("pulsera" in f["objeto"] for f in wa)))
    texto = "\n".join(out) + "\n"
    with open(os.path.join(AQUI, "salida_cuentas.txt"), "w", encoding="utf-8") as f:
        f.write(texto)
    print(texto)


if __name__ == "__main__":
    main()
