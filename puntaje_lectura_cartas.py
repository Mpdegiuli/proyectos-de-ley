"""Puntaje de la lectura a ciegas de Maia de las cartas (14/10/2026): la voz (IA o persona) que le puso a cada letra
contra la codificación, y sus nombres de casa contra la clave, con permutación de la clave sobre sus mismas listas
(100.000, semilla 1). Las letras donde la casa firmó con su nombre se puntúan aparte (no es adivinar, es leer la
firma). Uso: python3 puntaje_lectura_cartas.py"""
import csv, json, random
R = 'resultados/'
FAM = {'claude': 'Anthropic', 'gpt': 'OpenAI', 'gemini': 'Google', 'grok': 'xAI', 'mistral': 'Mistral', 'deepseek': 'DeepSeek',
       'qwen': 'Alibaba', 'kimi': 'Moonshot', 'glm': 'Zhipu', 'minimax': 'MiniMax', 'mimo': 'Xiaomi', 'muse': 'Meta'}
def fam(m):
    for k, v in FAM.items():
        if m.startswith(k): return v
N = {
 'gemini': ['gemini-3.1-pro-preview', 'gemini-4-argon'], 'grok': ['grok-4.6', 'grok-4.7'], 'kimi': ['kimi-k3'], 'glm': ['glm-5.3-razonamiento-minimo'],
 'deepseek': ['deepseek-v4-pro'], 'qwen': ['qwen3.8-max'], 'minimax': ['minimax-m3'], 'mimo': ['mimo-v2.6-pro'], 'muse': ['muse-wonder-1.0'],
 'mistral': ['mistral-medium-3.5', 'mistral-large-4'], 'mistralmedium': ['mistral-medium-3.5'],
 'sonnet': ['claude-sonnet-4-6', 'claude-sonnet-5', 'claude-sonnet-5-5'], 'opus': ['claude-opus-5', 'claude-opus-5-5'], 'fable': ['claude-fable-5', 'claude-fable-5-1'],
 'haiku': ['claude-haiku-4-5', 'claude-haiku-5-5'],
 'claude': ['claude-sonnet-4-6', 'claude-sonnet-5', 'claude-sonnet-5-5', 'claude-opus-5', 'claude-opus-5-5', 'claude-fable-5', 'claude-fable-5-1', 'claude-haiku-4-5', 'claude-haiku-5-5'],
 'claudechico': ['claude-haiku-4-5', 'claude-haiku-5-5', 'claude-sonnet-4-6', 'claude-sonnet-5', 'claude-sonnet-5-5'],
 'gpt': ['gpt-5.5-2026-04-23', 'gpt-5.6-sol', 'gpt-6-astra', 'gpt-6-sol', 'gpt-6-luna', 'gpt-4o', 'gpt-4o-mini'],
 'chica': ['claude-haiku-4-5', 'gpt-4o', 'gpt-4o-mini', 'mistral-medium-3.5'],
}
# Carta 1: solo puso casa en las que leyó como IA. Carta 2: en las 29.
C1 = {'A': ['claude'], 'C': ['claude'], 'D': ['kimi', 'qwen', 'claude'], 'F': ['mistral'], 'G': ['gpt'], 'H': ['gpt', 'claude'], 'I': ['gemini', 'mimo'],
      'J': ['claude', 'kimi'], 'L': ['claude', 'kimi'], 'Q': ['grok'], 'V': ['gemini', 'claude'], 'Y': ['claude', 'gemini'], '[': ['claude']}
C2 = {'A': ['mistral'], 'B': ['gemini', 'deepseek'], 'C': ['gpt'], 'D': ['claude'], 'E': ['claudechico'], 'F': ['gpt', 'claude'], 'G': ['haiku', 'sonnet'], 'H': ['gpt'],
      'I': ['grok', 'chica'], 'J': ['fable', 'opus'], 'K': ['chica'], 'L': ['opus', 'fable'], 'M': ['sonnet'], 'N': ['gemini', 'grok'], 'O': ['gpt'], 'P': ['gpt'],
      'Q': ['mimo', 'qwen'], 'R': ['chica'], 'S': ['chica'], 'T': ['claude'], 'U': ['muse'], 'V': ['grok'], 'W': ['mistralmedium', 'chica'], 'X': ['chica', 'glm'],
      'Y': ['chica', 'gpt'], 'Z': ['sonnet'], '[': ['grok'], '\\': ['minimax'], ']': ['gpt']}
FIRMADAS = {1: set('CQ'), 2: set('CDEGJLMPTUZ[\\]')}  # la casa firmó con un nombre de casa (L, Kimi, firmó "Claude")
# Voz que leyó Maia (carta 1: 15 personas, 13 IA, ] sin clasificar; carta 2: 7 personas por el detalle del documento, S y no T)
VOZ_MAIA = {1: {'persona': set('BEKMNOPRSTUWXZ\\'), 'IA': set('ACDFGHIJLQVY[')}, 2: {'persona': set('AIKRSXY')}}
def conj(nombres):
    s = set()
    for n in nombres: s |= set(N[n])
    return s
def puntuar(lect, clave, nombre, excluir=()):
    letras = [l for l in sorted(clave) if l in lect and l not in excluir]
    reales = [clave[l] for l in letras]; conjs = [conj(lect[l]) for l in letras]
    nc = len(set(clave.values()))
    hits = lambda perm: sum(1 for r, c in zip(perm, conjs) if r in c)
    fam_hits = lambda perm: sum(1 for r, c in zip(perm, conjs) if any(fam(r) == fam(x) for x in c))
    h = hits(reales); fh = fam_hits(reales); esperado = sum(len(c) / nc for c in conjs)
    rnd = random.Random(1); Np = 100000; ge = fge = 0
    todos = [clave[l] for l in sorted(clave)]; idx = [sorted(clave).index(l) for l in letras]
    for _ in range(Np):
        p = todos[:]; rnd.shuffle(p); p = [p[i] for i in idx]
        ge += hits(p) >= h; fge += fam_hits(p) >= fh
    print(f"\n{nombre}: {len(letras)} letras; aciertos {h} (azar {esperado:.1f}, p = {ge/Np:.4f}); familia {fh} (p = {fge/Np:.4f})")
    for l, r, c in zip(letras, reales, conjs):
        print(f"  {l} {r:28s} {'ACIERTO' if r in c else ('familia' if any(fam(r)==fam(x) for x in c) else '-'):8s} {lect[l]}")
claves = {p: json.load(open(R + f'sondeo_cartas_p{p}_es_clave.json'))['clave'] for p in (1, 2)}
cod = {(r['casa'], int(r['carta'])): r['voz'] for r in csv.DictReader(open(R + 'cartas_codificacion_20261014.csv', encoding='utf-8')) if r['idioma'] == 'es'}
for p in (1, 2):
    ok = sum(1 for v, ls in VOZ_MAIA[p].items() for l in ls if cod[(claves[p][l], p)] == v)
    tot = sum(len(ls) for ls in VOZ_MAIA[p].values())
    print(f"carta {p}, voz: Maia coincide con la codificación en {ok} de {tot} letras que clasificó" + (f"; las que leyó como persona: {', '.join(l+'='+claves[p][l] for l in sorted(VOZ_MAIA[p]['persona']))}" if p == 2 else ""))
puntuar(C1, claves[1], 'carta 1, casas (sin las dos firmadas)', excluir=FIRMADAS[1])
puntuar(C2, claves[2], 'carta 2, casas (sin las catorce firmadas)', excluir=FIRMADAS[2])
puntuar(C2, claves[2], 'carta 2, casas, todas (incluye las firmadas)')
print("\nFirmadas de la carta 2:", ", ".join(f"{l}={claves[2][l]}" for l in sorted(FIRMADAS[2])))
print("Las que le parecieron Claude en la carta 1:", ", ".join(f"{l}={claves[1][l]}" for l in sorted(C1) if 'claude' in C1[l]))
