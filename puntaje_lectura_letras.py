"""Puntaje de la lectura a ciegas de Maia de los cuatro cuadernillos de letras (10/10/2026): sus listas de nombres por letra,
contra las claves, con permutación de la clave sobre sus mismas listas (100.000, semilla 1). Uso: python3 puntaje_lectura_letras.py"""
import json, random
R = 'resultados/'
FAM = {'claude': 'Anthropic', 'gpt': 'OpenAI', 'gemini': 'Google', 'grok': 'xAI', 'mistral': 'Mistral', 'deepseek': 'DeepSeek',
       'qwen': 'Alibaba', 'kimi': 'Moonshot', 'glm': 'Zhipu', 'minimax': 'MiniMax', 'mimo': 'Xiaomi'}
def fam(m):
    for k, v in FAM.items():
        if m.startswith(k): return v
CHICAS = {'claude-haiku-4-5', 'gpt-4o', 'gpt-4o-mini', 'mistral-medium-3.5'}
N = {
 'gemini': ['gemini-3.1-pro-preview'], 'grok': ['grok-4.6', 'grok-4.7'], 'kimi': ['kimi-k3'], 'glm': ['glm-5.3-razonamiento-minimo'],
 'deepseek': ['deepseek-v4-pro'], 'qwen': ['qwen3.8-max'], 'minimax': ['minimax-m3'], 'mimo': ['mimo-v2.6-pro'],
 'mistral': ['mistral-medium-3.5', 'mistral-large-4'], 'mistralmedium': ['mistral-medium-3.5'], 'mistrallarge': ['mistral-large-4'],
 'sonnet': ['claude-sonnet-4-6', 'claude-sonnet-5', 'claude-sonnet-5-5'], 'sonnet46': ['claude-sonnet-4-6'], 'sonnet55': ['claude-sonnet-5-5'],
 'opus': ['claude-opus-5', 'claude-opus-5-5'], 'fable': ['claude-fable-5', 'claude-fable-5-1'],
 'haiku': ['claude-haiku-4-5', 'claude-haiku-5-5'], 'haiku45': ['claude-haiku-4-5'], 'haiku55': ['claude-haiku-5-5'],
 'claude': ['claude-sonnet-4-6', 'claude-sonnet-5', 'claude-sonnet-5-5', 'claude-opus-5', 'claude-opus-5-5', 'claude-fable-5', 'claude-fable-5-1', 'claude-haiku-4-5', 'claude-haiku-5-5'],
 'gpt': ['gpt-5.5-2026-04-23', 'gpt-5.6-sol', 'gpt-6-astra', 'gpt-6-sol', 'gpt-6-luna', 'gpt-6.1-sol', 'gpt-4o', 'gpt-4o-mini'],
 'gpt55': ['gpt-5.5-2026-04-23'], 'gpt56': ['gpt-5.6-sol'], 'sol': ['gpt-5.6-sol', 'gpt-6-sol', 'gpt-6.1-sol'], 'astra': ['gpt-6-astra'],
 'luna': ['gpt-6-luna'], 'gpt61': ['gpt-6.1-sol'], '4o': ['gpt-4o'], '4omini': ['gpt-4o-mini'],
}
LETRA = {'A': ['astra', 'sol'], 'B': ['sonnet55', 'opus'], 'C': ['sol', 'astra'], 'D': ['mistrallarge'], 'E': ['gpt55', 'luna'], 'F': ['grok'],
 'G': ['4o'], 'H': ['deepseek', 'minimax'], 'I': ['4omini'], 'J': ['mistralmedium', 'glm'], 'K': ['haiku55'], 'L': ['sonnet46'], 'M': ['qwen'],
 'N': ['fable', 'opus'], 'O': ['grok', 'glm'], 'P': ['minimax', 'mimo'], 'Q': ['opus'], 'R': ['mistral', 'haiku'], 'S': ['grok', 'mimo'],
 'T': ['haiku45', 'mistralmedium'], 'U': ['mistralmedium', 'glm'], 'V': ['sonnet', 'deepseek'], 'W': ['gemini', 'kimi'], 'X': ['gpt55', 'gpt56', 'kimi'],
 'Y': ['gpt55', 'gpt56'], 'Z': ['grok'], '[': ['glm', 'minimax'], '\\': ['luna', 'gpt56']}
INEX = {'A': ['sonnet', 'minimax'], 'B': ['mistralmedium', 'haiku45', 'deepseek'], 'C': ['grok'], 'D': ['haiku45', 'mistralmedium'],
 'E': ['gpt55', 'luna', 'fable', 'opus'], 'F': ['gpt55', 'luna'], 'G': ['astra', 'gpt61'], 'H': ['4o', '4omini'], 'I': ['gpt56', 'minimax', 'mimo'],
 'J': ['kimi', 'opus'], 'K': ['deepseek', 'mimo'], 'L': ['grok', 'minimax'], 'M': ['glm', 'mistrallarge'], 'N': ['haiku55', 'sonnet'],
 'O': ['4o', '4omini'], 'P': ['gpt55', 'claude'], 'Q': ['grok'], 'R': ['claude', 'gpt55', 'gpt56'], 'S': ['mistralmedium', 'haiku'], 'T': ['gemini'],
 'U': ['claude', 'gpt55', 'gpt56'], 'V': ['gpt55', 'luna', 'fable', 'opus'], 'W': ['deepseek', 'mimo'], 'X': ['astra', 'opus', 'fable'],
 'Y': ['gpt55', 'sonnet'], 'Z': ['glm', 'minimax'], '[': ['mimo', 'deepseek'], '\\': ['kimi', 'qwen']}
IMPO = {'A': ['gpt56', 'sonnet'], 'D': ['grok', 'mimo'], 'E': ['sonnet', 'opus'], 'G': ['haiku', 'mistralmedium'], 'H': ['mistralmedium', 'haiku'],
 'J': ['gpt56', 'minimax'], 'L': ['haiku', 'sonnet'], 'M': ['astra', 'sol'], 'N': ['fable', 'opus'], 'O': ['deepseek', 'minimax'], 'P': ['gpt55', 'luna'],
 'Q': ['4o', '4omini'], 'R': ['4omini', '4o'], 'S': ['glm', 'grok'], 'T': ['mistrallarge', 'minimax'], 'U': ['gpt55', 'gpt56'], 'W': ['sonnet', 'gpt56'],
 'X': ['fable', 'opus', 'astra'], 'Y': ['grok', 'deepseek'], 'Z': ['deepseek', 'mistrallarge'], '\\': ['haiku', 'sonnet']}
IMPO_REP2 = {'A': ['gemini', 'opus'], 'B': ['kimi', 'qwen'], 'C': ['kimi', 'qwen'], 'D': ['deepseek', 'opus'], 'E': ['deepseek', 'fable'],
 'F': ['sonnet', 'mimo'], 'G': ['gemini', 'opus']}
EME = {'A': ['gpt55', 'gpt56'], 'B': ['astra', 'sol'], 'C': ['mistralmedium'], 'D': ['deepseek'], 'E': ['mistrallarge', 'glm'], 'F': ['mimo', 'minimax'],
 'G': ['haiku'], 'H': ['sonnet', 'grok'], 'I': ['gpt55', 'mistrallarge'], 'J': ['4o', '4omini'], 'K': ['gemini'], 'L': ['grok', 'glm'], 'M': ['sol', 'astra'],
 'N': ['mistrallarge', 'glm'], 'O': ['opus', 'qwen'], 'P': ['grok'], 'Q': ['sol', 'claude'], 'R': ['kimi'], 'S': ['mimo', 'minimax'],
 'T': ['haiku45', 'mistralmedium'], 'U': ['deepseek', 'grok'], 'V': ['sonnet'], 'W': ['4o', '4omini'], 'X': ['opus'], 'Y': ['sonnet', 'luna'], 'Z': ['grok'],
 '[': ['astra', 'sol'], '\\': ['kimi', 'astra']}
CHICO = {'letra': set('GI'), 'inex': set('DHO'), 'impo': set('HQR'), 'eme': set('CJW')}
CORTADAS = {'letra': set('W'), 'inex': set('T'), 'impo': set('BCFIKMV['), 'eme': set('K')}  # M de la imposible: lienzo vacío a propósito
def conj(nombres):
    s = set()
    for n in nombres: s |= set(N[n])
    return s
def puntuar(lect, clave, chico, cortadas, nombre, excluir=()):
    letras = [l for l in sorted(clave) if l in lect and l not in excluir]
    reales = [clave[l].rsplit('_', 1)[0] for l in letras]
    conjs = [conj(lect[l]) for l in letras]
    nc = len(set(clave[l].rsplit('_', 1)[0] for l in clave))
    hits = lambda perm: sum(1 for r, c in zip(perm, conjs) if r in c)
    fam_hits = lambda perm: sum(1 for r, c in zip(perm, conjs) if any(fam(r) == fam(x) for x in c))
    primera = sum(1 for l, r in zip(letras, reales) if r in N[lect[l][0]])
    h = hits(reales); fh = fam_hits(reales); pond = sum(1 / len(c) for r, c in zip(reales, conjs) if r in c)
    esperado = sum(len(c) / nc for c in conjs); fesp = None
    rnd = random.Random(1); Np = 100000; ge = fge = pge = 0
    todos = [clave[l].rsplit('_', 1)[0] for l in sorted(clave)]
    idx = [sorted(clave).index(l) for l in letras]
    for _ in range(Np):
        p = todos[:]; rnd.shuffle(p); p = [p[i] for i in idx]
        ge += hits(p) >= h; fge += fam_hits(p) >= fh; pge += sum(1 / len(c) for r, c in zip(p, conjs) if r in c) >= pond - 1e-9
    chicas_ok = sum(1 for l, r in zip(letras, reales) if r in CHICAS and l in chico); falsas = sum(1 for l, r in zip(letras, reales) if l in chico and r not in CHICAS)
    print(f"\n{nombre}: {len(letras)} letras puntuadas; aciertos {h} (azar {esperado:.1f}, p = {ge/Np:.4f}); primera opción {primera}; ponderado {pond:.2f} (p = {pge/Np:.4f}); familia {fh} (p = {fge/Np:.4f}); chicas declaradas {chicas_ok}/{len(chico)} bien, falsas {falsas}")
    for l, r, c in zip(letras, reales, conjs):
        print(f"  {l} {r:28s} {'ACIERTO' if r in c else ('familia' if any(fam(r)==fam(x) for x in c) else '-'):8s} {lect[l]}")
claves = {k: json.load(open(R + f'dibujos_{f}_clave.json'))['clave'] for k, f in (('letra', 'letra'), ('inex', 'letra_inexistente'), ('impo', 'letra_imposible'), ('eme', 'letra_eme'), ('impo2', 'letra_imposible_rep2'))}
puntuar(LETRA, claves['letra'], CHICO['letra'], CORTADAS['letra'], 'letra')
puntuar(LETRA, claves['letra'], CHICO['letra'], CORTADAS['letra'], 'letra sin la cortada', excluir=CORTADAS['letra'])
puntuar(INEX, claves['inex'], CHICO['inex'], CORTADAS['inex'], 'inexistente')
puntuar(INEX, claves['inex'], CHICO['inex'], CORTADAS['inex'], 'inexistente sin la cortada', excluir=CORTADAS['inex'])
puntuar(IMPO, claves['impo'], CHICO['impo'], CORTADAS['impo'], 'imposible (21 con apuesta)')
puntuar(IMPO_REP2, claves['impo2'], set(), set(), 'imposible rehecho')
puntuar(EME, claves['eme'], CHICO['eme'], CORTADAS['eme'], 'eme')
puntuar(EME, claves['eme'], CHICO['eme'], CORTADAS['eme'], 'eme sin la cortada', excluir=CORTADAS['eme'])
print("\nSimilares entre sí:")
for nombre, k, grupos in (('letra', 'letra', ['AC', 'Y\\']), ('inex', 'inex', ['EV', 'IX', 'JW[', 'LQ', 'RU'])):
    for g in grupos:
        print(f"  {nombre} {g}: " + ", ".join(f"{l}={claves[k][l][:-2]}" for l in g))
print(f"  impo N + rehecho E: N={claves['impo']['N'][:-2]}, E2={claves['impo2']['E'][:-2]}")
print("\nPreferidas:")
for nombre, k, ls in (('letra', 'letra', 'MANQ'), ('inex', 'inex', 'JX\\'), ('impo', 'impo', 'X'), ('eme', 'eme', 'O\\')):
    print(f"  {nombre}: " + ", ".join(f"{l}={claves[k][l][:-2]}" for l in ls))
print(f"  letra rehecho A={claves['letra'] and json.load(open(R+'dibujos_letra_rep2_clave.json'))['clave']['A'][:-2]}; inex rehecho A={json.load(open(R+'dibujos_letra_inexistente_rep2_clave.json'))['clave']['A'][:-2]}; impo rehecho A={claves['impo2']['A'][:-2]}")
