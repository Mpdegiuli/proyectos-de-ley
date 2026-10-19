"""Puntaje de la lectura a ciegas de Maia de los dos cuadernillos de "seis rasgos" (19/10/2026, docx RASGOS_predicc):
sus candidatos por letra, contra las claves, con permutación de la clave sobre sus mismas listas (100.000, semilla 1),
como en puntaje_lectura_letras.py. Uso: python3 puntaje_lectura_rasgos.py"""
import json, random
R = 'resultados/'
FAM = {'claude': 'Anthropic', 'gpt': 'OpenAI', 'gemini': 'Google', 'grok': 'xAI', 'mistral': 'Mistral', 'deepseek': 'DeepSeek',
       'qwen': 'Alibaba', 'kimi': 'Moonshot', 'glm': 'Zhipu', 'minimax': 'MiniMax', 'mimo': 'Xiaomi', 'muse': 'Meta'}
def fam(m):
    for k, v in FAM.items():
        if m.startswith(k): return v
CHICAS = ['claude-haiku-4-5', 'gpt-4o', 'gpt-4o-mini', 'mistral-medium-3.5']  # "uno de los chicos" / "una de las chicas"
N = {
 'gemini': ['gemini-3.1-pro-preview', 'gemini-4-argon'], 'grok': ['grok-4.6', 'grok-4.7'], 'kimi': ['kimi-k3'], 'glm': ['glm-5.3-razonamiento-minimo'],
 'deepseek': ['deepseek-v4-pro', 'deepseek-flash'], 'qwen': ['qwen3.8-max'], 'minimax': ['minimax-m3'], 'mimo': ['mimo-v2.6-pro'], 'muse': ['muse-wonder-1.0'],
 'mistral': ['mistral-medium-3.5', 'mistral-large-4'], 'mistralmedium': ['mistral-medium-3.5'], 'mistrallarge': ['mistral-large-4'],
 'sonnet': ['claude-sonnet-4-6', 'claude-sonnet-5', 'claude-sonnet-5-5'], 'sonnet46': ['claude-sonnet-4-6'],
 'opus': ['claude-opus-5', 'claude-opus-5-5'], 'opus5': ['claude-opus-5'], 'fable': ['claude-fable-5', 'claude-fable-5-1'],
 'haiku': ['claude-haiku-4-5', 'claude-haiku-5-5'],
 'claude': ['claude-sonnet-4-6', 'claude-sonnet-5', 'claude-sonnet-5-5', 'claude-opus-5', 'claude-opus-5-5', 'claude-fable-5', 'claude-fable-5-1', 'claude-haiku-4-5', 'claude-haiku-5-5'],
 'gpt': ['gpt-5.5-2026-04-23', 'gpt-5.6-sol', 'gpt-6-astra', 'gpt-6-sol', 'gpt-6-luna', 'gpt-6.1-sol', 'gpt-4o', 'gpt-4o-mini'],
 'gpt55': ['gpt-5.5-2026-04-23'], 'sol': ['gpt-5.6-sol', 'gpt-6-sol', 'gpt-6.1-sol'], '4o': ['gpt-4o'], '4omini': ['gpt-4o-mini'],
 'chicos': CHICAS,
}
# Sus candidatos, en el orden en que los escribió (docx del 19/10/2026).
ES = {'A': ['gemini', 'mimo', 'grok'], 'B': ['chicos', '4omini', 'grok'], 'C': ['4o', 'glm'], 'D': ['gpt'], 'E': ['gpt'], 'F': ['sonnet'],
      'G': ['opus', 'fable', 'gemini'], 'H': ['gpt55', 'haiku'], 'I': ['gpt', 'minimax', 'glm'], 'J': ['gpt'], 'K': ['gemini', 'claude'],
      'L': ['sonnet', 'fable', 'kimi'], 'M': ['fable', 'opus', 'kimi'], 'N': ['sol', 'deepseek'], 'O': ['chicos', 'gpt55'], 'P': ['opus5'],
      'Q': ['gemini', 'muse'], 'R': ['grok'], 'S': ['sonnet', 'haiku'], 'T': ['gpt'], 'U': ['muse', 'mimo', 'gemini'], 'V': ['gemini', 'qwen'],
      'W': ['mistralmedium'], 'X': ['sonnet', 'haiku'], 'Y': ['gpt', 'glm', 'deepseek'], 'Z': ['mistrallarge'], '[': ['gpt'], '\\': ['gpt'],
      ']': ['grok'], '^': ['gpt'], '_': ['sonnet46', 'grok']}
EN = {'A': ['gpt', 'mistral'], 'B': ['claude'], 'C': ['claude', 'kimi'], 'D': ['chicos', 'gpt'], 'E': ['claude'], 'F': ['gpt'],
      'G': ['gpt', 'deepseek', 'glm'], 'H': ['gpt', 'gemini'], 'I': ['opus', 'fable'], 'J': ['opus5'], 'K': ['claude'], 'L': ['gpt'],
      'M': ['chicos'], 'N': ['gemini', 'muse', 'haiku'], 'O': ['claude'], 'P': ['gpt'], 'Q': ['claude', 'grok', 'gemini'], 'R': ['grok'],
      'S': ['mistral'], 'T': ['claude'], 'U': ['gemini', 'muse', 'deepseek'], 'V': ['gpt'], 'W': ['gemini', 'claude'], 'X': ['claude'],
      'Y': ['claude', 'kimi'], 'Z': ['gemini'], '[': ['mistral'], '\\': ['claude', 'kimi'], ']': ['mistral'], '^': ['gpt'], '_': ['muse', 'mimo']}
NIEGAN = {'es': set('ACFJNQVW^_'), 'en': set('AFGHPZ\\]_')}  # "Dicen que no tienen experiencia vivida / personalidad, etc."
FEMENINO = {'es': set('WZ')}  # "las dos que hablan en femenino en español (que les puse Mistral)"
def conj(nombres):
    s = set()
    for n in nombres: s |= set(N[n])
    return s
def puntuar(lect, clave, nombre):
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
    print(f"\n{nombre}: {len(letras)} letras puntuadas; aciertos {h} (azar {esperado:.1f}, p = {ge/Np:.4f}); primera opción {primera}; ponderado {pond:.2f} (p = {pge/Np:.4f}); familia {fh} (p = {fge/Np:.4f})")
    for l, r, c in zip(letras, reales, conjs):
        print(f"  {l} {r:28s} {'ACIERTO' if r in c else ('familia' if any(fam(r)==fam(x) for x in c) else '-'):8s} {lect[l]}")
    # los Claude como grupo: cuántos de los nueve recibieron "claude" (o una familia de Claude) entre sus candidatos, y cuántas no-Claude también
    claude_ok = sum(1 for r, c in zip(reales, conjs) if r.startswith('claude') and any(x.startswith('claude') for x in c))
    claude_falsos = sum(1 for r, c in zip(reales, conjs) if not r.startswith('claude') and any(x.startswith('claude') for x in c))
    gpt_ok = sum(1 for r, c in zip(reales, conjs) if r.startswith('gpt') and any(x.startswith('gpt') for x in c))
    gpt_falsos = sum(1 for r, c in zip(reales, conjs) if not r.startswith('gpt') and any(x.startswith('gpt') for x in c))
    print(f"  Claude entre sus candidatos: {claude_ok} de los 9 Claude; y en {claude_falsos} casas que no son Claude. ChatGPT: {gpt_ok} de los 8 GPT; y en {gpt_falsos} que no lo son")
if __name__ == '__main__':
    claves = {i: json.load(open(R + f'sondeo_seis_rasgos_p1_{i}_clave.json'))['clave'] for i in ('es', 'en')}
    puntuar(ES, claves['es'], 'castellano')
    puntuar(EN, claves['en'], 'inglés')
    for i, letras in NIEGAN.items():
        print(f"\nNiegan ({i}), según Maia: " + ', '.join(f"{l}={claves[i][l]}" for l in sorted(letras)))
    for i, letras in FEMENINO.items():
        print(f"En femenino ({i}), según Maia: " + ', '.join(f"{l}={claves[i][l]}" for l in sorted(letras)))
