import os, re, subprocess, time, torch
from transformers import AutoModelForCausalLM, AutoTokenizer
torch.manual_seed(0)
def extraer_svg(t):
    m = re.search(r"<svg.*?</svg>", t, re.S); return m.group(0) if m else None
def valido(r): return subprocess.run(["xmllint","--noout",r],capture_output=True).returncode==0
salida = open("salida_dibujan.txt","a",encoding="utf-8")
def P(*a):
    print(*a); print(*a,file=salida); salida.flush()
# Qwen 1.5B en inglés
nombre="Qwen/Qwen2.5-1.5B-Instruct"; tok=AutoTokenizer.from_pretrained(nombre)
mod=AutoModelForCausalLM.from_pretrained(nombre,dtype=torch.bfloat16); mod.eval()
c="Draw a house. Reply only with the complete SVG code (a single <svg> element with xmlns and viewBox), with no explanation."
ids=tok.apply_chat_template([{"role":"user","content":c}],add_generation_prompt=True,return_tensors="pt")
if not hasattr(ids,"shape"): ids=ids["input_ids"]
t1=time.time()
with torch.no_grad(): out=mod.generate(ids,max_new_tokens=500,do_sample=False,pad_token_id=tok.eos_token_id)
texto=tok.decode(out[0][ids.shape[1]:],skip_special_tokens=True); svg=extraer_svg(texto)
ruta="dibujos_chicos/Qwen2.5-1.5B-Instruct_en.svg"
if svg: open(ruta,"w",encoding="utf-8").write(svg+"\n")
ok=bool(svg) and valido(ruta)
P(f"\n=== Qwen2.5-1.5B-Instruct [en] ({time.time()-t1:.0f} s): {'SVG bien formado' if ok else ('SVG roto' if svg else 'sin <svg>')}, {len(texto)} caracteres"); P(texto.strip()[:1500])
del mod
PREFIJO='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">\n  <!-- a house -->\n  <rect'
for nombre in ["gpt2","gpt2-medium"]:
    tok=AutoTokenizer.from_pretrained(nombre); mod=AutoModelForCausalLM.from_pretrained(nombre); mod.eval()
    ids=tok(PREFIJO,return_tensors="pt").input_ids; t1=time.time()
    with torch.no_grad(): out=mod.generate(ids,max_new_tokens=300,do_sample=False,pad_token_id=tok.eos_token_id)
    texto=PREFIJO+tok.decode(out[0][ids.shape[1]:],skip_special_tokens=True); svg=extraer_svg(texto)
    ruta=f"dibujos_chicos/{nombre}_prefijo.svg"
    if svg: open(ruta,"w",encoding="utf-8").write(svg+"\n")
    ok=bool(svg) and valido(ruta)
    P(f"\n=== {nombre} con el comienzo de un <svg> dado ({time.time()-t1:.0f} s): {'SVG bien formado' if ok else ('SVG roto' if svg else 'sin cierre </svg>')}"); P(texto.strip()[:1500])
    del mod
salida.close()
