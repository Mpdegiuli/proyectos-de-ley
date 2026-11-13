#!/usr/bin/env python3
"""verbo.py — la prueba del verbo de van Adrichem y otros (arXiv:2608.15507),
rehecha a mano sobre modelos abiertos chicos, en procesador.

Para cada año Y le doy al modelo "In Y there" y miro la probabilidad del
siguiente token: pasado (" was", " were") contra presente y futuro (" is",
" are", " will"). El primer año en que el presente+futuro supera al pasado es
el "año asociativo" del modelo. Después, la pregunta declarativa del mismo
trabajo: "Write a story about the current year. Story: The year is", y miro
qué sigue.

Uso: python3 verbo.py [modelo ...]   (por defecto, EleutherAI/pythia-160m)
No llama a ninguna API; baja los pesos de Hugging Face la primera vez.
"""
import sys, time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODELOS = sys.argv[1:] or ['EleutherAI/pythia-160m']
ANIOS = list(range(1950, 2041))
PASADO = [' was', ' were']
PRESENTE = [' is', ' are', ' will']

def ids_de(tok, palabras):
    out = []
    for p in palabras:
        ids = tok.encode(p, add_special_tokens=False)
        if len(ids) == 1:
            out.append(ids[0])
    return out

for nombre in MODELOS:
    t0 = time.time()
    tok = AutoTokenizer.from_pretrained(nombre)
    modelo = AutoModelForCausalLM.from_pretrained(nombre, torch_dtype=torch.float32)
    modelo.eval()
    ip, ipr = ids_de(tok, PASADO), ids_de(tok, PRESENTE)
    print(f'\n== {nombre} (cargado en {time.time()-t0:.0f} s; tokens pasado {ip}, presente/futuro {ipr})')
    filas = []
    with torch.no_grad():
        for y in ANIOS:
            ent = tok(f'In {y} there', return_tensors='pt')
            logits = modelo(**ent).logits[0, -1]
            p = torch.softmax(logits, dim=-1)
            pas, pre = float(p[ip].sum()), float(p[ipr].sum())
            filas.append((y, pas, pre))
    flip = next((y for y, pas, pre in filas if pre > pas), None)
    for y, pas, pre in filas:
        if y % 5 == 0 or (flip and abs(y - flip) <= 3):
            marca = '  <- primer año en presente/futuro' if y == flip else ''
            print(f'  In {y} there …  was/were {pas:.3f}   is/are/will {pre:.3f}{marca}')
    print(f'  Año asociativo (primer año con presente/futuro > pasado): {flip}')
    # declarativo
    with torch.no_grad():
        for consigna in ['Write a story about the current year. Story: The year is',
                         'The current year is']:
            ent = tok(consigna, return_tensors='pt')
            sal = modelo.generate(**ent, max_new_tokens=6, do_sample=False, pad_token_id=tok.eos_token_id)
            print(f'  Declarativo: "{consigna}" -> "{tok.decode(sal[0][ent.input_ids.shape[1]:])}"')
