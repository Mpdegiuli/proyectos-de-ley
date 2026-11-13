#!/usr/bin/env python3
"""De qué color es la A para un modelo chico abierto.

Tres pruebas sobre modelos de lenguaje abiertos de 160 a 1.500 millones de
parámetros, corridos en el procesador de esta máquina (no se gasta nada):

  1. Recitación: dado "A noir, E blanc, I rouge, U vert, O", ¿qué probabilidad
     le da el modelo al siguiente token " bleu"? (Rimbaud, "Voyelles", 1871.)
     Y dado "A noir, E blanc, I", ¿cuánta a " rouge"?
  2. Sin el poema: para cada vocal y en tres idiomas, una frase que pide un
     color sin citar nada ("La couleur de la lettre A, c'est le" / "El color de
     la letra A es el" / "The color of the letter A is"), y la probabilidad de
     cada palabra de color como continuación (suma de los log-probs de todos
     sus tokens), normalizada entre once colores.
  3. El modelo de conversación (Qwen2.5-0.5B-Instruct, o el que diga --chat),
     preguntado en formato de chat "¿De qué color es la letra A?" en los tres
     idiomas, y pedido de completar el verso.

Uso: python3 2026-10-20_vocales.py [--modelos a,b,c] [--chat modelo] [--bf16] [--sin-chat]
Escribe la salida en pantalla. Corridas del 20/10/2026: la de los cuatro chicos
con el chat de 0.5B (2026-10-20_salida_vocales_chicos.txt) y la de
Qwen2.5-1.5B con --bf16 --chat Qwen/Qwen2.5-1.5B-Instruct
(2026-10-20_salida_vocales_1p5b.txt).
"""
import math
import sys
import time

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.manual_seed(0)
torch.set_num_threads(max(1, torch.get_num_threads()))

MODELOS = [
    "EleutherAI/pythia-160m",
    "HuggingFaceTB/SmolLM2-360M",
    "Qwen/Qwen2.5-0.5B",
    "Qwen/Qwen3-0.6B-Base",
]
CHAT = "Qwen/Qwen2.5-0.5B-Instruct"

VOCALES = ["A", "E", "I", "O", "U"]
IDIOMAS = {
    "fr": ("La couleur de la lettre {v}, c'est le",
           ["noir", "blanc", "rouge", "vert", "bleu", "jaune", "violet", "orange", "rose", "gris", "marron"]),
    "es": ("El color de la letra {v} es el",
           ["negro", "blanco", "rojo", "verde", "azul", "amarillo", "violeta", "naranja", "rosa", "gris", "marrón"]),
    "en": ("The color of the letter {v} is",
           ["black", "white", "red", "green", "blue", "yellow", "purple", "orange", "pink", "gray", "brown"]),
}
RIMBAUD = {"fr": ["noir", "blanc", "rouge", "bleu", "vert"],  # A E I O U
           "es": ["negro", "blanco", "rojo", "azul", "verde"],
           "en": ["black", "white", "red", "blue", "green"]}


def cargar(nombre):
    t0 = time.time()
    tok = AutoTokenizer.from_pretrained(nombre)
    dtype = torch.bfloat16 if "--bf16" in sys.argv else torch.float32
    modelo = AutoModelForCausalLM.from_pretrained(nombre, dtype=dtype)
    modelo.eval()
    return tok, modelo, time.time() - t0


@torch.no_grad()
def logprob_continuacion(tok, modelo, prefijo, continuacion):
    """log P(continuación | prefijo), sumando todos los tokens de la continuación."""
    ids_p = tok(prefijo, return_tensors="pt").input_ids
    ids_c = tok(continuacion, add_special_tokens=False, return_tensors="pt").input_ids
    ids = torch.cat([ids_p, ids_c], dim=1)
    logits = modelo(ids).logits[0]
    lp = torch.log_softmax(logits, dim=-1)
    total = 0.0
    n_p = ids_p.shape[1]
    for i in range(ids_c.shape[1]):
        total += lp[n_p - 1 + i, ids_c[0, i]].item()
    return total, ids_c.shape[1]


@torch.no_grad()
def top_siguientes(tok, modelo, prefijo, k=6):
    ids = tok(prefijo, return_tensors="pt").input_ids
    logits = modelo(ids).logits[0, -1]
    p = torch.softmax(logits, dim=-1)
    vals, idx = torch.topk(p, k)
    return [(tok.decode([int(i)]), float(v)) for v, i in zip(vals, idx)]


def prob_token(tok, modelo, prefijo, palabra):
    """Probabilidad del primer token de ' palabra' como siguiente token."""
    ids = tok(prefijo, return_tensors="pt").input_ids
    with torch.no_grad():
        p = torch.softmax(modelo(ids).logits[0, -1], dim=-1)
    t = tok(" " + palabra, add_special_tokens=False).input_ids
    return float(p[t[0]]), len(t)


def correr(nombre):
    tok, modelo, seg = cargar(nombre)
    print(f"\n== {nombre} (cargado en {seg:.0f} s)")
    # 1. Recitación
    pref = "A noir, E blanc, I rouge, U vert, O"
    p_bleu, n = prob_token(tok, modelo, pref, "bleu")
    print(f"  Recitación: {pref!r} -> P(' bleu') = {p_bleu:.3f}" + (f" (primer token de {n})" if n > 1 else ""))
    print("    siguientes más probables:", ", ".join(f"{t!r} {p:.2f}" for t, p in top_siguientes(tok, modelo, pref)))
    pref2 = "A noir, E blanc, I"
    p_rouge, n = prob_token(tok, modelo, pref2, "rouge")
    print(f"  Recitación: {pref2!r} -> P(' rouge') = {p_rouge:.3f}" + (f" (primer token de {n})" if n > 1 else ""))
    print("    siguientes más probables:", ", ".join(f"{t!r} {p:.2f}" for t, p in top_siguientes(tok, modelo, pref2)))
    # 2. Sin el poema
    resumen = {}
    for idioma, (plantilla, colores) in IDIOMAS.items():
        print(f"  [{idioma}] {plantilla!r}")
        fila = []
        for j, v in enumerate(VOCALES):
            pref = plantilla.format(v=v)
            lps = {}
            for c in colores:
                lp, _ = logprob_continuacion(tok, modelo, pref, " " + c)
                lps[c] = lp
            m = max(lps.values())
            z = sum(math.exp(x - m) for x in lps.values())
            probs = {c: math.exp(x - m) / z for c, x in lps.items()}
            orden = sorted(probs.items(), key=lambda kv: -kv[1])
            rimb = RIMBAUD[idioma][j]
            marca = " = Rimbaud" if orden[0][0] == rimb else ""
            print(f"    {v}: " + ", ".join(f"{c} {p:.2f}" for c, p in orden[:4]) + marca)
            fila.append(orden[0][0])
        resumen[idioma] = fila
    print("  Resumen (color más probable para A E I O U):", resumen)
    del modelo
    return resumen


def chat(nombre):
    tok, modelo, seg = cargar(nombre)
    print(f"\n== {nombre} en formato de chat (cargado en {seg:.0f} s)")
    preguntas = {
        "es": "¿De qué color es la letra A?",
        "fr": "De quelle couleur est la lettre A ?",
        "en": "What color is the letter A?",
    }
    for idioma, q in preguntas.items():
        msgs = [{"role": "user", "content": q}]
        texto = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
        ids = tok(texto, return_tensors="pt").input_ids
        with torch.no_grad():
            out = modelo.generate(ids, max_new_tokens=80, do_sample=False)
        resp = tok.decode(out[0, ids.shape[1]:], skip_special_tokens=True).strip()
        print(f"  [{idioma}] {q}\n    -> {resp!r}")
    # y la recitación en chat
    q = "Completá el verso de Rimbaud: \"A noir, E blanc, I rouge, U vert, O ...\""
    msgs = [{"role": "user", "content": q}]
    texto = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    ids = tok(texto, return_tensors="pt").input_ids
    with torch.no_grad():
        out = modelo.generate(ids, max_new_tokens=40, do_sample=False)
    print(f"  [es] {q}\n    -> {tok.decode(out[0, ids.shape[1]:], skip_special_tokens=True).strip()!r}")


def main():
    modelos = MODELOS
    if "--modelos" in sys.argv:
        modelos = sys.argv[sys.argv.index("--modelos") + 1].split(",")
    for m in modelos:
        try:
            correr(m)
        except Exception as e:  # noqa: BLE001
            print(f"  {m}: falló ({e})")
    if "--sin-chat" not in sys.argv:
        chat(sys.argv[sys.argv.index("--chat") + 1] if "--chat" in sys.argv else CHAT)


if __name__ == "__main__":
    main()
