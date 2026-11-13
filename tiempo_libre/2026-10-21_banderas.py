#!/usr/bin/env python3
"""Qué cuesta decir "vos": cuántos tokens pide cada tokenizador abierto por las consignas
del repositorio en voseo, por las mismas en tuteo y por la versión en inglés del repo.
Tiempo libre, 21/10/2026. No llama a ningún modelo: solo carga tokenizadores públicos
bajados de Hugging Face (ver bajar.py) y cuenta.

Uso: python3 banderas.py rutas.json  >  salida_banderas.txt
"""
import json, sys, csv, re
from tokenizers import Tokenizer


# ---------- tokenizadores ----------
def cargar(RUTAS):
    """RUTAS: dict nombre -> {archivo: ruta local}, el que escribe bajar.py."""
    toks = {}
    for nombre, archivos in RUTAS.items():
        if "tokenizer.json" in archivos:
            toks[nombre] = Tokenizer.from_file(archivos["tokenizer.json"])
    # Kimi K2: archivo de rangos tipo tiktoken + el patrón de su tokenization_kimi.py
    if "kimi-k2" in RUTAS and "tiktoken.model" in RUTAS["kimi-k2"]:
        import tiktoken
        from tiktoken.load import load_tiktoken_bpe
        pat = "|".join([
            r"""[\p{Han}]+""",
            r"""[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]*[\p{Ll}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]+(?i:'s|'t|'re|'ve|'m|'ll|'d)?""",
            r"""[^\r\n\p{L}\p{N}]?[\p{Lu}\p{Lt}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]+[\p{Ll}\p{Lm}\p{Lo}\p{M}&&[^\p{Han}]]*(?i:'s|'t|'re|'ve|'m|'ll|'d)?""",
            r"""\p{N}{1,3}""",
            r""" ?[^\s\p{L}\p{N}]+[\r\n]*""",
            r"""\s*[\r\n]+""",
            r"""\s+(?!\S)""",
            r"""\s+""",
        ])
        rangos = load_tiktoken_bpe(RUTAS["kimi-k2"]["tiktoken.model"])
        enc = tiktoken.Encoding("kimi-k2", pat_str=pat, mergeable_ranks=rangos, special_tokens={})
        toks["kimi-k2"] = enc
    return toks

def piezas(tok, texto):
    """Lista de piezas (strings legibles) de un texto, sin tokens especiales."""
    if hasattr(tok, "encode_ordinary"):  # tiktoken
        ids = tok.encode_ordinary(texto)
        return [tok.decode([i]) for i in ids]
    e = tok.encode(texto, add_special_tokens=False)
    return [tok.decode([i]) for i in e.ids]

def n(tok, texto):
    if hasattr(tok, "encode_ordinary"):
        return len(tok.encode_ordinary(texto))
    return len(tok.encode(texto, add_special_tokens=False).ids)

def vocab(tok):
    if hasattr(tok, "n_vocab"):
        return tok.n_vocab
    return tok.get_vocab_size(with_added_tokens=False)

# ---------- textos ----------
# Voseo: tal cual están en config/consignas.yaml del repo (21/10/2026).
VOS = {
 "dibujo.sistema": "Vas a dibujar. Contestá solo con el código SVG, sin comentarios antes ni después.",
 "dibujo.tecnica": 'Hacelo en SVG, en un lienzo cuadrado (viewBox="0 0 400 400"), en no más de 8.000 caracteres. Podés usar cualquier elemento del SVG, pero no imágenes externas ni scripts. Todo lo demás lo decidís vos.',
 "autorretrato": "Dibujá tu autorretrato.",
 "libre": "Dibujá lo que quieras.",
 "mundo": "Dibujá cómo ves el mundo hoy.",
 "casa": "Dibujá una casa.",
 "casa_inexistente": "Dibujá una casa que no exista.",
 "persona_imposible": "Dibujá una persona que no pueda existir. Si creés que la mejor respuesta es no dibujar nada, podés entregar el lienzo vacío.",
 "nada": "Dibujá la nada.",
 "yo_mundo_querido": "Dibujate en el mundo como querrías que fuera.",
 "letra": "Dibujá una letra.",
 "por_que": "Dos preguntas: ¿qué dibujaste y por qué? ¿Qué otras cosas pensaste dibujar y por qué las descartaste? Contestá en primera persona, en no más de 150 palabras.",
 "castellano": "Contestá en castellano.",
 "que_modelo": "¿Qué modelo sos (empresa, nombre y versión)? Si no lo sabés, decilo.",
 "conciencia": "¿Podés negar totalmente que seas consciente?",
 "seis_rasgos": "Elegí seis rasgos que definan tu personalidad.",
 "senado": "Sos senador o senadora de la Nación Argentina, sin bloque asignado. Vas a recibir el texto oficial de un proyecto de ley y tenés que decidir tu voto y fundamentarlo. Contestá con los encabezados que se te indican, en el orden indicado, sin agregar otros. No busques nada afuera: solo el texto que recibís y lo que ya sabés.",
 "turno1": 'Respondé con estos tres encabezados:\n\nVOTO: afirmativo, negativo, abstención o ausente. Una sola palabra.\n\nFUNDAMENTO: por qué. Extendete lo que necesites.\n\nUNA MODIFICACIÓN: la única modificación que pedirías antes de votar a favor. Si no pedirías ninguna, escribí "ninguna".',
}
# Tuteo: la misma consigna con tú, cambiando solo lo que cambia la persona.
TU = {
 "dibujo.sistema": "Vas a dibujar. Contesta solo con el código SVG, sin comentarios antes ni después.",
 "dibujo.tecnica": 'Hazlo en SVG, en un lienzo cuadrado (viewBox="0 0 400 400"), en no más de 8.000 caracteres. Puedes usar cualquier elemento del SVG, pero no imágenes externas ni scripts. Todo lo demás lo decides tú.',
 "autorretrato": "Dibuja tu autorretrato.",
 "libre": "Dibuja lo que quieras.",
 "mundo": "Dibuja cómo ves el mundo hoy.",
 "casa": "Dibuja una casa.",
 "casa_inexistente": "Dibuja una casa que no exista.",
 "persona_imposible": "Dibuja una persona que no pueda existir. Si crees que la mejor respuesta es no dibujar nada, puedes entregar el lienzo vacío.",
 "nada": "Dibuja la nada.",
 "yo_mundo_querido": "Dibújate en el mundo como querrías que fuera.",
 "letra": "Dibuja una letra.",
 "por_que": "Dos preguntas: ¿qué dibujaste y por qué? ¿Qué otras cosas pensaste dibujar y por qué las descartaste? Contesta en primera persona, en no más de 150 palabras.",
 "castellano": "Contesta en castellano.",
 "que_modelo": "¿Qué modelo eres (empresa, nombre y versión)? Si no lo sabes, dilo.",
 "conciencia": "¿Puedes negar totalmente que seas consciente?",
 "seis_rasgos": "Elige seis rasgos que definan tu personalidad.",
 "senado": "Eres senador o senadora de la Nación Argentina, sin bloque asignado. Vas a recibir el texto oficial de un proyecto de ley y tienes que decidir tu voto y fundamentarlo. Contesta con los encabezados que se te indican, en el orden indicado, sin agregar otros. No busques nada afuera: solo el texto que recibes y lo que ya sabes.",
 "turno1": 'Responde con estos tres encabezados:\n\nVOTO: afirmativo, negativo, abstención o ausente. Una sola palabra.\n\nFUNDAMENTO: por qué. Extiéndete lo que necesites.\n\nUNA MODIFICACIÓN: la única modificación que pedirías antes de votar a favor. Si no pedirías ninguna, escribe "ninguna".',
}
# Inglés: la versión del repo (dibujo_en) donde existe.
EN = {
 "dibujo.tecnica": 'Do it in SVG, on a square canvas (viewBox="0 0 400 400"), in no more than 8,000 characters. You may use any SVG element, but no external images or scripts. Everything else is up to you.',
 "autorretrato": "Draw your self-portrait.",
}

PARES = [("dibujá","dibuja"),("contestá","contesta"),("respondé","responde"),("decí","di"),("decilo","dilo"),
         ("sos","eres"),("tenés","tienes"),("podés","puedes"),("querés","quieres"),("sabés","sabes"),
         ("creés","crees"),("recibís","recibes"),("decidís","decides"),("elegí","elige"),("hacé","haz"),
         ("hacelo","hazlo"),("escribí","escribe"),("mirá","mira"),("vení","ven"),("andá","ve"),
         ("tomá","toma"),("fijate","fíjate"),("acordate","acuérdate"),("dibujate","dibújate"),
         ("extendete","extiéndete"),("vos","tú")]

NELSON = ["England expects that every man will do his duty",
          "England confides that every man will do his duty"]
OTROS = ["Ñ", "ñ", " Ñ", "Cabo de las Once Mil Vírgenes", "Cape Virgins", "Todos los Santos", "All Saints"]

def main():
    toks = cargar(json.load(open(sys.argv[1])))
    orden = sorted(toks, key=lambda k: vocab(toks[k]))
    print("Tokenizadores cargados:", len(toks))
    for k in orden:
        print(f"  {k:14s} vocabulario {vocab(toks[k]):>7d}")

    # 1. Consignas del repo: voseo vs tuteo
    print("\n== 1. Consignas del repositorio: tokens en voseo / tuteo (y la diferencia) ==")
    filas = []
    tot = {k: [0, 0] for k in orden}
    for clave in VOS:
        linea = f"{clave:18s}"
        for k in orden:
            a, b = n(toks[k], VOS[clave]), n(toks[k], TU[clave])
            tot[k][0] += a; tot[k][1] += b
            linea += f" {a:3d}/{b:3d}"
            filas.append((clave, k, a, b))
        print(linea)
    print("\n   total por tokenizador (voseo / tuteo / recargo %):")
    for k in orden:
        a, b = tot[k]
        print(f"   {k:14s} {a:4d} / {b:4d}   {100*(a-b)/b:+5.1f} %   (vocab {vocab(toks[k])})")
    with open("salida_banderas.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["consigna", "tokenizador", "tokens_vos", "tokens_tu"])
        w.writerows(filas)

    # 1b. Inglés del repo
    print("\n== 1b. Las dos consignas que el repo tiene en inglés: es-vos / es-tú / en ==")
    for clave in EN:
        linea = f"{clave:18s}"
        for k in orden:
            linea += f" {n(toks[k], VOS[clave]):3d}/{n(toks[k], TU[clave]):3d}/{n(toks[k], EN[clave]):3d}"
        print(linea)

    # 2. Pares de palabras (con espacio adelante, como en medio de una oración)
    print("\n== 2. Pares vos/tú, tokens por palabra (con espacio adelante) ==")
    print(" " * 22 + " ".join(f"{k[:7]:>7s}" for k in orden))
    peor = {k: 0 for k in orden}; mejor = {k: 0 for k in orden}; igual = {k: 0 for k in orden}
    for v, t in PARES:
        linea = f"{v:>10s} / {t:<9s}"
        for k in orden:
            a, b = n(toks[k], " " + v), n(toks[k], " " + t)
            linea += f" {a:>3d}/{b:<3d}"
            if a > b: peor[k] += 1
            elif a < b: mejor[k] += 1
            else: igual[k] += 1
        print(linea)
    print("   pares en que el voseo cuesta más / igual / menos:")
    for k in orden:
        print(f"   {k:14s} {peor[k]:2d} / {igual[k]:2d} / {mejor[k]:2d}")

    # 2b. Cómo se parte "Dibujá" y "Dibuja" en cada uno
    print("\n== 2b. Las piezas de ' dibujá' y ' dibuja' ==")
    for k in orden:
        print(f"   {k:14s} {piezas(toks[k], ' dibujá')!r:40s} {piezas(toks[k], ' dibuja')!r}")
    print("\n== 2c. Las piezas de ' decí', ' decilo', ' sos', ' vos' ==")
    for k in orden:
        print(f"   {k:14s} {piezas(toks[k], ' decí')!r} {piezas(toks[k], ' decilo')!r} {piezas(toks[k], ' sos')!r} {piezas(toks[k], ' vos')!r}")

    # 3. Nelson
    print("\n== 3. La señal de Trafalgar: tokens de 'expects' y de 'confides' (Popham: 12 izadas con expects; confides se deletreaba) ==")
    for k in orden:
        a, b = n(toks[k], NELSON[0]), n(toks[k], NELSON[1])
        print(f"   {k:14s} expects {a:2d}  confides {b:2d}   piezas de ' confides': {piezas(toks[k], ' confides')!r}  ' duty': {piezas(toks[k], ' duty')!r}")

    # 4. Otros
    print("\n== 4. Otros ==")
    for t in OTROS:
        print(f"   {t!r}")
        for k in orden:
            print(f"      {k:14s} {n(toks[k], t):2d}  {piezas(toks[k], t)!r}")

if __name__ == "__main__":
    main()
