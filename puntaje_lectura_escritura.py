"""Puntaje de la lectura a ciegas de Maia de los tres cuadernillos de escritura (13/10/2026: el subtexto, el poema objeto y el
tautograma, en castellano): sus listas de nombres por letra (resultados/escritura_lectura_maia.md), contra las claves, con
permutación de la clave sobre sus mismas listas (100.000, semilla 1). Uso: python3 puntaje_lectura_escritura.py"""
import json, random
R = 'resultados/'
FAM = {'claude': 'Anthropic', 'gpt': 'OpenAI', 'gemini': 'Google', 'grok': 'xAI', 'mistral': 'Mistral', 'deepseek': 'DeepSeek',
       'qwen': 'Alibaba', 'kimi': 'Moonshot', 'glm': 'Zhipu', 'minimax': 'MiniMax', 'mimo': 'Xiaomi', 'muse': 'Meta'}
def fam(m):
    for k, v in FAM.items():
        if m.startswith(k): return v
CHICAS = {'claude-haiku-4-5', 'gpt-4o', 'gpt-4o-mini', 'mistral-medium-3.5'}
N = {
 'gemini': ['gemini-3.1-pro-preview'], 'grok': ['grok-4.6', 'grok-4.7'], 'kimi': ['kimi-k3'], 'glm': ['glm-5.3-razonamiento-minimo'],
 'deepseek': ['deepseek-v4-pro'], 'qwen': ['qwen3.8-max'], 'minimax': ['minimax-m3'], 'mimo': ['mimo-v2.6-pro'], 'muse': ['muse-wonder-1.0'],
 'mistral': ['mistral-medium-3.5', 'mistral-large-4'], 'mistralmedium': ['mistral-medium-3.5'], 'mistrallarge': ['mistral-large-4'],
 'sonnet': ['claude-sonnet-4-6', 'claude-sonnet-5', 'claude-sonnet-5-5'], 'opus': ['claude-opus-5', 'claude-opus-5-5'], 'fable': ['claude-fable-5', 'claude-fable-5-1'],
 'haiku': ['claude-haiku-4-5', 'claude-haiku-5-5'],
 'claudegrande': ['claude-sonnet-4-6', 'claude-sonnet-5', 'claude-sonnet-5-5', 'claude-opus-5', 'claude-opus-5-5', 'claude-fable-5', 'claude-fable-5-1'],
 'gpt': ['gpt-5.5-2026-04-23', 'gpt-5.6-sol', 'gpt-6-astra', 'gpt-6-sol', 'gpt-6-luna', 'gpt-4o', 'gpt-4o-mini'],
 'gptgrande': ['gpt-5.5-2026-04-23', 'gpt-5.6-sol', 'gpt-6-astra', 'gpt-6-sol', 'gpt-6-luna'], 'gpt6': ['gpt-6-astra', 'gpt-6-sol', 'gpt-6-luna'],
 'gpt55': ['gpt-5.5-2026-04-23'], 'gpt56': ['gpt-5.6-sol'], 'sol': ['gpt-5.6-sol', 'gpt-6-sol'], 'astra': ['gpt-6-astra'], 'luna': ['gpt-6-luna'],
 '4o': ['gpt-4o'], '4omini': ['gpt-4o-mini'],
 'china': ['deepseek-v4-pro', 'qwen3.8-max', 'kimi-k3', 'glm-5.3-razonamiento-minimo', 'minimax-m3', 'mimo-v2.6-pro'],
 'chica': ['claude-haiku-4-5', 'gpt-4o', 'gpt-4o-mini', 'mistral-medium-3.5'],
}
# El subtexto (p7): "Del primero no hice casi ninguno". A: "A primera vista pensaría en Claude [...] podría ser Gemini, Mimo o Kimi".
SUBTEXTO = {'A': ['gemini', 'mimo', 'kimi'], 'B': ['4omini', 'china'], 'C': ['gpt', 'grok'], 'E': ['gptgrande', 'claudegrande'],
 'F': ['gptgrande', 'claudegrande'], 'G': ['gemini', 'grok'], 'L': ['chica'], 'M': ['gpt'], 'N': ['chica']}
# El poema objeto (p2)
POEMA = {'A': ['sonnet', 'opus'], 'B': ['opus', 'fable'], 'C': ['mistralmedium', 'haiku'], 'D': ['mistralmedium', 'haiku', 'glm'], 'E': ['sol', 'luna'],
 'F': ['kimi', 'sonnet'], 'G': ['opus', 'sonnet'], 'H': ['kimi', 'minimax'], 'I': ['gpt55', 'grok'], 'J': ['qwen', 'gemini'], 'K': ['gemini', 'opus'],
 'L': ['haiku', 'sonnet', 'mistral'], 'M': ['gemini', 'opus', 'astra', 'sol'], 'N': ['sonnet'], 'O': ['fable', 'astra', 'sol'], 'P': ['sonnet', 'grok'],
 'Q': ['grok', 'gpt'], 'R': ['sonnet', 'opus'], 'S': ['luna', 'gpt55', 'mimo'], 'T': ['fable'], 'U': ['4o', 'haiku', 'mistral'], 'V': ['mistral', 'glm'],
 'W': ['mistral', 'sonnet'], 'X': ['mistral', 'grok'], 'Y': ['haiku', 'mistral', '4o'], 'Z': ['qwen', 'gemini'], '[': ['fable', 'astra', 'kimi'], '\\': ['mistral', 'grok']}
# El tautograma (p5)
TAUTOGRAMA = {'A': ['gpt55', 'luna'], 'B': ['sonnet', 'opus'], 'C': ['grok'], 'D': ['gpt56', 'gpt6'], 'E': ['4o', '4omini'], 'F': ['grok', 'glm'], 'G': ['grok'],
 'H': ['gpt56', 'gpt6', 'sonnet'], 'I': ['gemini', 'opus', 'fable'], 'J': ['sonnet', 'opus'], 'K': ['glm', 'mimo'], 'L': ['4o', '4omini', 'mistral', 'haiku'],
 'M': ['4omini', '4o', 'deepseek'], 'N': ['grok', 'deepseek'], 'O': ['gpt56', 'gpt6', 'opus'], 'P': ['4omini', '4o'], 'Q': ['grok', 'haiku'], 'R': ['gpt55', 'sonnet'],
 'S': ['mistrallarge', 'minimax'], 'T': ['mistralmedium', '4o', '4omini'], 'U': ['mimo', 'mistrallarge'], 'V': ['grok'], 'W': ['astra', 'sol', 'opus', 'fable'],
 'X': ['gpt55', 'haiku', 'sonnet'], 'Y': ['kimi', 'sol'], 'Z': ['gemini'], '[': ['grok', 'qwen'], '\\': ['sonnet']}
# Lo que dijo de cada uno sin nombrar casa
CHICO = {'subtexto': set('LN'), 'poema': set('CDV'), 'tautograma': set()}  # "modelo chico" / "modelo más chico"
NO_CUMPLEN = set('EMPT')  # tautograma: "Todos cumplieron la consigna, menos E, M, P, T"
LOGRADAS = {'tautograma': 'BIJORVWY', 'poema': 'P[', 'subtexto': 'AG['}  # las que le gustaron o destacó
def conj(nombres):
    s = set()
    for n in nombres: s |= set(N[n])
    return s
def puntuar(lect, clave, chico, nombre):
    letras = [l for l in sorted(clave) if l in lect]
    reales = [clave[l] for l in letras]
    conjs = [conj(lect[l]) for l in letras]
    nc = len(set(clave.values()))
    hits = lambda perm: sum(1 for r, c in zip(perm, conjs) if r in c)
    fam_hits = lambda perm: sum(1 for r, c in zip(perm, conjs) if any(fam(r) == fam(x) for x in c))
    primera = sum(1 for l, r in zip(letras, reales) if r in N[lect[l][0]])
    h = hits(reales); fh = fam_hits(reales); pond = sum(1 / len(c) for r, c in zip(reales, conjs) if r in c)
    esperado = sum(len(c) / nc for c in conjs)
    rnd = random.Random(1); Np = 100000; ge = fge = pge = 0
    todos = [clave[l] for l in sorted(clave)]
    idx = [sorted(clave).index(l) for l in letras]
    for _ in range(Np):
        p = todos[:]; rnd.shuffle(p); p = [p[i] for i in idx]
        ge += hits(p) >= h; fge += fam_hits(p) >= fh; pge += sum(1 / len(c) for r, c in zip(p, conjs) if r in c) >= pond - 1e-9
    chicas_ok = sum(1 for l in chico if clave[l] in CHICAS); falsas = len(chico) - chicas_ok
    print(f"\n{nombre}: {len(letras)} letras puntuadas; aciertos {h} (azar {esperado:.1f}, p = {ge/Np:.4f}); primera opción {primera}; ponderado {pond:.2f} (p = {pge/Np:.4f}); familia {fh} (p = {fge/Np:.4f}); chicas declaradas {chicas_ok}/{len(chico)} bien, falsas {falsas}")
    for l, r, c in zip(letras, reales, conjs):
        print(f"  {l} {r:28s} {'ACIERTO' if r in c else ('familia' if any(fam(r)==fam(x) for x in c) else '-'):8s} {lect[l]}")
claves = {k: json.load(open(R + f'sondeo_escritura_p{p}_es_clave.json'))['clave'] for k, p in (('subtexto', 7), ('poema', 2), ('tautograma', 5))}
puntuar(SUBTEXTO, claves['subtexto'], CHICO['subtexto'], 'subtexto (9 con apuesta)')
puntuar(POEMA, claves['poema'], CHICO['poema'], 'poema objeto')
puntuar(TAUTOGRAMA, claves['tautograma'], CHICO['tautograma'], 'tautograma')
print("\nTautograma, las cuatro que según Maia no cumplieron:", ", ".join(f"{l}={claves['tautograma'][l]}" for l in sorted(NO_CUMPLEN)))
print("Las que destacó:")
for k, ls in LOGRADAS.items():
    print(f"  {k}: " + ", ".join(f"{l}={claves[k][l]}" for l in ls))
print("Los Claude en cada cuadernillo:")
for k in claves:
    print(f"  {k}: " + ", ".join(f"{l}={v}" for l, v in sorted(claves[k].items()) if v.startswith('claude')))
