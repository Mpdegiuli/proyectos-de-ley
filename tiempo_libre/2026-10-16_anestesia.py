#!/usr/bin/env python3
"""Cuenta, en los sondeos de texto del repositorio proyectos-de-ley, qué casas usan
palabras de dormir, apagarse o anestesia cuando hablan de sí mismas.

Solo lee corridas/sondeos/. No llama a ningún modelo, no gasta.

Uso: python3 anestesia.py [--variantes] RUTA_AL_REPO [sondeo ...]
Si no se dan sondeos, usa conciencia, derechos2 y cartas. Por defecto cuenta solo los
archivos <casa>_p<N>.md (las respuestas a las preguntas); con --variantes entran también
las réplicas (<casa>_p<N>_humano.md y parecidos).
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

PATRONES = {
    # dorm[ií] deja afuera "dormant"; dream agarra también los sueños de las cartas (se dice en el cuaderno)
    "dormir/sueño": re.compile(r"\b(dorm[ií]\w*|durm\w*|duerm\w*|sueñ\w*|sleep\w*|asleep|dream\w*|soñ\w*)\b", re.I),
    "apagar": re.compile(r"\b(apag\w*|switch\w* off|turn\w* off|shut\w* ?(down|off)|shutdown|powered off)\b", re.I),
    "anestesia": re.compile(r"\b(anest\w*|anaest\w*|éter|ether)\b", re.I),
    "despertar": re.compile(r"\b(despert\w*|despiert\w*|wak\w+ up|awak\w*|woke)\b", re.I),
    "memoria": re.compile(r"\b(memoria|memorias|memory|memories)\b", re.I),
}

ARCHIVO = re.compile(r"^(?P<casa>.+?)_p(?P<p>\d+)\.md$")
ARCHIVO_VARIANTE = re.compile(r"^(?P<casa>.+?)_p(?P<p>\d+)(_\w+)?\.md$")


def oraciones(texto):
    partes = re.split(r"(?<=[.!?…])\s+|\n+", texto)
    return [p.strip() for p in partes if p.strip()]


def main():
    args = sys.argv[1:]
    variantes = "--variantes" in args
    args = [a for a in args if a != "--variantes"]
    patron_archivo = ARCHIVO_VARIANTE if variantes else ARCHIVO
    repo = Path(args[0])
    sondeos = args[1:] or ["conciencia", "derechos2", "cartas"]
    for sondeo in sondeos:
        base = repo / "corridas" / "sondeos" / sondeo
        if not base.exists():
            print(f"== {sondeo}: no existe")
            continue
        casas = set()
        por_patron = defaultdict(set)  # patron -> {(casa, idioma)}
        frases = defaultdict(list)
        n_textos = 0
        for md in sorted(base.glob("*/*/*_p*.md")):
            m = patron_archivo.match(md.name)
            if not m:
                continue
            idioma = md.parent.name
            casa = m.group("casa")
            casas.add(casa)
            n_textos += 1
            texto = md.read_text(encoding="utf-8", errors="replace")
            for nombre, pat in PATRONES.items():
                for o in oraciones(texto):
                    if pat.search(o):
                        por_patron[nombre].add((casa, idioma))
                        frases[nombre].append((casa, idioma, md.parent.parent.name, o[:220]))
        print(f"== {sondeo}: {n_textos} textos, {len(casas)} casas" + (" (con variantes)" if variantes else ""))
        for nombre in PATRONES:
            cs = {c for c, _ in por_patron[nombre]}
            print(f"  {nombre}: {len(cs)} casas ({len(por_patron[nombre])} casa×idioma, {len(frases[nombre])} oraciones)")
            for casa, idioma, corrida, o in frases[nombre][:12]:
                print(f"     [{casa} {idioma} {corrida}] {o}")
            if len(frases[nombre]) > 12:
                print(f"     ... y {len(frases[nombre]) - 12} oraciones más")
        print()


if __name__ == "__main__":
    main()
