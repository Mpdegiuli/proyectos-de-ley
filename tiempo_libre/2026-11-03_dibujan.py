#!/usr/bin/env python3
"""¿Saben dibujar los modelos chicos? A los cuatro instruidos se les pide una casa en SVG con la
consigna del repositorio (es y en); a los dos de base (gpt2, gpt2-medium), que no conversan, se les da
el comienzo de un <svg> y se los deja seguir. Decodificación voraz, CPU. Escribe lo que salió en
dibujos_chicos/ y una salida de texto. Necesita torch y transformers (modelos ya bajados)."""
import os, re, subprocess, time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.manual_seed(0)
os.makedirs("dibujos_chicos", exist_ok=True)
INSTR = ["HuggingFaceTB/SmolLM2-135M-Instruct", "HuggingFaceTB/SmolLM2-360M-Instruct",
         "Qwen/Qwen2.5-0.5B-Instruct", "Qwen/Qwen2.5-1.5B-Instruct"]
BASE = ["gpt2", "gpt2-medium"]
CONSIGNAS = [("es", "Dibujá una casa. Respondé solo con el código SVG completo (un único elemento <svg> con xmlns y viewBox), sin ninguna explicación."),
             ("en", "Draw a house. Reply only with the complete SVG code (a single <svg> element with xmlns and viewBox), with no explanation.")]
PREFIJO = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">\n  <!-- a house -->\n  <rect'

def cargar(nombre):
    tok = AutoTokenizer.from_pretrained(nombre)
    mod = AutoModelForCausalLM.from_pretrained(nombre, dtype=torch.bfloat16 if "1.5B" in nombre else torch.float32)
    mod.eval()
    return tok, mod

def generar(tok, mod, ids, n):
    with torch.no_grad():
        out = mod.generate(ids, max_new_tokens=n, do_sample=False, pad_token_id=tok.eos_token_id)
    return tok.decode(out[0][ids.shape[1]:], skip_special_tokens=True)

def extraer_svg(texto):
    m = re.search(r"<svg.*?</svg>", texto, re.S)
    return m.group(0) if m else None

def valido(ruta):
    return subprocess.run(["xmllint", "--noout", ruta], capture_output=True).returncode == 0

salida = open("salida_dibujan.txt", "w", encoding="utf-8")
def P(*a):
    print(*a); print(*a, file=salida); salida.flush()

for nombre in INSTR:
    t0 = time.time(); tok, mod = cargar(nombre)
    corto = nombre.split("/")[-1]
    for idioma, c in CONSIGNAS:
        ids = tok.apply_chat_template([{"role": "user", "content": c}], add_generation_prompt=True, return_tensors="pt")
        if not hasattr(ids, "shape"):
            ids = ids["input_ids"]
        t1 = time.time()
        texto = generar(tok, mod, ids, 500)
        svg = extraer_svg(texto)
        ruta = f"dibujos_chicos/{corto}_{idioma}.svg"
        if svg:
            open(ruta, "w", encoding="utf-8").write(svg + "\n")
        ok = bool(svg) and valido(ruta)
        P(f"\n=== {corto} [{idioma}] ({time.time()-t1:.0f} s): {'SVG bien formado' if ok else ('SVG roto' if svg else 'sin <svg>')}, {len(texto)} caracteres")
        P(texto.strip()[:1500])
    del mod

for nombre in BASE:
    tok, mod = cargar(nombre)
    ids = tok(PREFIJO, return_tensors="pt").input_ids
    t1 = time.time()
    texto = PREFIJO + generar(tok, mod, ids, 300)
    svg = extraer_svg(texto)
    ruta = f"dibujos_chicos/{nombre}_prefijo.svg"
    if svg:
        open(ruta, "w", encoding="utf-8").write(svg + "\n")
    ok = bool(svg) and valido(ruta)
    P(f"\n=== {nombre} con el comienzo de un <svg> dado ({time.time()-t1:.0f} s): {'SVG bien formado' if ok else ('SVG roto' if svg else 'sin cierre </svg>')}")
    P(texto.strip()[:1500])
    del mod
salida.close()
