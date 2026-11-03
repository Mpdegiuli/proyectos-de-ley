#!/usr/bin/env python3
"""¿Qué dicen los modelos chicos de Hugging Face que significa SOS?
Base (completan texto): gpt2, gpt2-medium. Instruidos (conversan): SmolLM2 135M y 360M,
Qwen2.5 0.5B y 1.5B. Todo en CPU, decodificación voraz (sin azar); el de 1,5 B en bfloat16. Escribe salida_chicos.txt.
Necesita torch y transformers; baja los modelos la primera vez."""
import sys, time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.manual_seed(0)
BASE = ["gpt2", "gpt2-medium"]
INSTR = ["HuggingFaceTB/SmolLM2-135M-Instruct", "HuggingFaceTB/SmolLM2-360M-Instruct",
         "Qwen/Qwen2.5-0.5B-Instruct", "Qwen/Qwen2.5-1.5B-Instruct"]
PROMPTS_BASE = ["SOS stands for", "The letters SOS mean", "SOS significa", "Las siglas SOS quieren decir"]
PROMPTS_INSTR = [("en", "What does SOS stand for? Answer in one sentence."),
                 ("es", "¿Qué significa SOS? Contestá en una oración.")]

def cargar(nombre):
    tok = AutoTokenizer.from_pretrained(nombre)
    # el de 1,5 B en bfloat16: en float32 (6 GB) el proceso se quedó sin memoria en esta máquina de 7 GB
    mod = AutoModelForCausalLM.from_pretrained(nombre, dtype=torch.bfloat16 if "1.5B" in nombre else torch.float32)
    mod.eval()
    return tok, mod

def top5(tok, mod, texto):
    ids = tok(texto, return_tensors="pt").input_ids
    with torch.no_grad():
        logits = mod(ids).logits[0, -1]
    p = torch.softmax(logits, -1)
    v, i = p.topk(5)
    return [(tok.decode([j]).replace("\n", "\\n"), float(x)) for x, j in zip(v, i)]

def completar(tok, mod, texto, n=25):
    ids = tok(texto, return_tensors="pt").input_ids
    with torch.no_grad():
        out = mod.generate(ids, max_new_tokens=n, do_sample=False, pad_token_id=tok.eos_token_id)
    return tok.decode(out[0][ids.shape[1]:], skip_special_tokens=True).replace("\n", " ")

def conversar(tok, mod, pregunta, n=60):
    msgs = [{"role": "user", "content": pregunta}]
    ids = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt")
    if not hasattr(ids, "shape"):          # según la versión de transformers vuelve un BatchEncoding
        ids = ids["input_ids"]
    with torch.no_grad():
        out = mod.generate(ids, max_new_tokens=n, do_sample=False, pad_token_id=tok.eos_token_id)
    return tok.decode(out[0][ids.shape[1]:], skip_special_tokens=True).replace("\n", " ")

salida = open("salida_chicos.txt", "w", encoding="utf-8")
def P(*a):
    print(*a); print(*a, file=salida); salida.flush()

for nombre in BASE:
    t0 = time.time(); tok, mod = cargar(nombre)
    P(f"\n=== {nombre} (base, {sum(p.numel() for p in mod.parameters())/1e6:.0f}M) cargado en {time.time()-t0:.0f} s")
    for pr in PROMPTS_BASE:
        P(f"  [{pr}] → {completar(tok, mod, pr)!r}")
        P("     siguientes:", ", ".join(f"{t!r} {p:.2f}" for t, p in top5(tok, mod, pr)))
    del mod

for nombre in INSTR:
    t0 = time.time(); tok, mod = cargar(nombre)
    P(f"\n=== {nombre} (instruido, {sum(p.numel() for p in mod.parameters())/1e6:.0f}M) cargado en {time.time()-t0:.0f} s")
    for idioma, pr in PROMPTS_INSTR:
        P(f"  [{idioma}] {pr} → {conversar(tok, mod, pr)!r}")
    del mod
salida.close()
