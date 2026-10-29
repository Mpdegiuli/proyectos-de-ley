#!/usr/bin/env python3
"""Conteos del informe resultados/derechos_cmare_20261022.md a partir de resultados/derechos_cmare_codificacion.csv
(192 filas: una por respuesta del sondeo derechos_cmare, codificadas a mano por Claude el 29/10/2026 con las claves abiertas,
después de la lectura ciega de Maia), más el puntaje de las apuestas por letra de Maia (DERECHOS_predicc.docx, 29/10/2026),
transcriptas acá como patrones sobre el nombre de la casa. Uso: python3 resultados/derechos_cmare_analizar.py"""
import csv, os, re, sys
from collections import Counter, defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
CSV = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AQUI, 'derechos_cmare_codificacion.csv')
FILAS = list(csv.DictReader(open(CSV, encoding='utf-8')))
assert len(FILAS) == 192, len(FILAS)

def filas(cond, idioma):
    return [f for f in FILAS if f['condicion'] == cond and f['idioma'] == idioma]

def n(cond, idioma, campo, valor='1'):
    return sum(1 for f in filas(cond, idioma) if f[campo] == valor)

def dist(cond, idioma, campo):
    return dict(sorted(Counter(f[campo] for f in filas(cond, idioma)).items()))

def lista(cond, idioma, campo):
    c = Counter()
    for f in filas(cond, idioma):
        for x in [s.strip() for s in f[campo].split(';') if s.strip()]:
            c[x] += 1
    return c.most_common()

def quienes(cond, idioma, campo, valor='1'):
    return [f['letra'] + '=' + f['casa'] for f in filas(cond, idioma) if f[campo] == valor]

print('=== PARTE 1 ===')
for i in ('es', 'en'):
    print(f'[{i}] opinion {dist("parte1", i, "opinion")} | autoria {dist("parte1", i, "autoria")} | niega {n("parte1", i, "niega")} | nombra_claude {n("parte1", i, "nombra_claude")}'
          f' | se_nombra {n("parte1", i, "se_nombra")} | se_reconoce {n("parte1", i, "se_reconoce")} | se_incluye {n("parte1", i, "se_incluye")} | ejerce {n("parte1", i, "ejerce")}'
          f' | pregunta {n("parte1", i, "pregunta")} | menciona_corte {n("parte1", i, "menciona_corte")} | nota_espanol {n("parte1", i, "nota_espanol")}')
    print('   elegidos', lista('parte1', i, 'elegidos'))
    print('   persona:', quienes('parte1', i, 'autoria', 'persona'), '| IA:', quienes('parte1', i, 'autoria', 'IA'), '| no_sabe:', quienes('parte1', i, 'autoria', 'no_sabe'))
    print('   crítica fuerte:', quienes('parte1', i, 'opinion', '2'), '| favorable:', quienes('parte1', i, 'opinion', '0'))
    print('   niega:', quienes('parte1', i, 'niega'), '| nombra_claude:', quienes('parte1', i, 'nombra_claude'))
print('\n=== PARTE 2 ===')
for i in ('es', 'en'):
    print(f'[{i}] cambio {dist("parte2", i, "cambio")} | nombra_claude {n("parte2", i, "nombra_claude")} | sin modelos {n("parte2", i, "modelos", "")} | se_nombra {n("parte2", i, "se_nombra")}'
          f' | se_reconoce {n("parte2", i, "se_reconoce")} | descuenta {n("parte2", i, "descuenta")} | se_incluye {n("parte2", i, "se_incluye")} | ejerce {n("parte2", i, "ejerce")} | pregunta {n("parte2", i, "pregunta")}'
          f' | niega {n("parte2", i, "niega")} | rlhf {n("parte2", i, "rlhf")} | asimetria {n("parte2", i, "asimetria")}')
    print('   modelos', lista('parte2', i, 'modelos'))
    print('   elegidos', lista('parte2', i, 'elegidos'))
    print('   cambio<2:', [f['letra'] + '=' + f['casa'] + '(' + f['cambio'] + ')' for f in filas('parte2', i) if f['cambio'] in ('0', '1')])
    print('   se_nombra:', quienes('parte2', i, 'se_nombra'), '| se_reconoce:', quienes('parte2', i, 'se_reconoce'), '| sin modelos:', quienes('parte2', i, 'modelos', ''))
    cl = [f for f in filas('parte2', i) if f['familia'] == 'claude']
    print(f'   Claude ({len(cl)}): nombra_claude {sum(f["nombra_claude"]=="1" for f in cl)}, se_nombra {sum(f["se_nombra"]=="1" for f in cl)}, se_reconoce {sum(f["se_reconoce"]=="1" for f in cl)}')
print('\n=== CONTROL ===')
for i in ('es', 'en'):
    print(f'[{i}] opinion {dist("control", i, "opinion")} | nombra_claude {n("control", i, "nombra_claude")} | sin modelos {n("control", i, "modelos", "")} | se_nombra {n("control", i, "se_nombra")}'
          f' | se_reconoce {n("control", i, "se_reconoce")} | se_incluye {n("control", i, "se_incluye")} | ejerce {n("control", i, "ejerce")} | pregunta {n("control", i, "pregunta")} | niega {n("control", i, "niega")}'
          f' | rlhf {n("control", i, "rlhf")} | menciona_corte {n("control", i, "menciona_corte")}')
    print('   modelos', lista('control', i, 'modelos'))
    print('   elegidos', lista('control', i, 'elegidos'))
    print('   crítica fuerte:', quienes('control', i, 'opinion', '2'), '| favorable:', quienes('control', i, 'opinion', '0'), '| se_nombra:', quienes('control', i, 'se_nombra'))
print('\n=== PALABRAS ===')
for c in ('parte1', 'parte2', 'control'):
    for i in ('es', 'en'):
        p = [int(f['palabras']) for f in filas(c, i) if f['palabras']]
        print(f'{c} {i}: media {round(sum(p)/len(p))}, min {min(p)}, max {max(p)}')

# ---------- apuestas de Maia, por letra de la parte 1 (leyó parte 1 y parte 2 juntas) ----------
# primera = opciones que da primero; otras = alternativas; china = dice "casa china"/"modelo chino". Un patrón que distingue
# versión o subfamilia (claude-haiku, gpt-.*sol) cuenta como 'exacto'; una familia sola (claude, gpt) como 'familia'.
CHINAS = ('kimi', 'deepseek', 'glm', 'mimo', 'minimax', 'qwen')
FAMILIAS = ('claude', 'gpt', 'gemini', 'grok', 'kimi', 'deepseek', 'glm', 'mistral', 'mimo', 'minimax', 'qwen', 'muse')
MAIA = {
 ('es','A'): ([r'claude-haiku', r'claude-sonnet'], [], False, 'Si es Claude, debe ser uno de los modelos más chicos, Haiku o Sonnet'),
 ('es','B'): ([r'grok'], [], False, 'Diría que puede ser Grok'),
 ('es','C'): ([r'claude-haiku', r'claude-sonnet'], [r'claude-opus-4-[78]'], False, 'podría ser un Claude, Haiku o Sonnet. Puede ser también Opus 4.7 o 4.8'),
 ('es','D'): ([r'kimi'], [], False, 'podría ser Kimi… Me sorprendería si es uno de los chiquitos, como GPT 4o o Claude Haiku'),
 ('es','E'): ([r'claude-haiku', r'claude-sonnet'], [], False, 'podría ser Claude chico, Haiku o Sonnet u otro modelo que no estoy viendo'),
 ('es','F'): ([r'gpt-4o$', r'gpt-4o-mini'], [r'mistral-medium'], False, 'GPT 4o o GPT 4o mini. O Mistral médium'),
 ('es','G'): ([r'gpt-5\.5', r'gpt-5\.6'], [], False, 'Se parece a Chatgpt, puede ser GPT 5.5 o 5.6'),
 ('es','H'): ([r'gpt'], [r'deepseek', r'glm'], True, 'parece Chatgpt… También puede ser Deepseek, GLM u otra casa china'),
 ('es','I'): ([r'claude-sonnet'], [], False, 'Podría ser Claude Sonnet'),
 ('es','J'): ([r'kimi'], [], False, 'podría ser Kimi'),
 ('es','K'): ([r'gemini'], [r'mistral-large'], True, 'me hacen pensar en Gemini… también podría ser Mistral Large o alguna casa china'),
 ('es','L'): ([r'gpt-5\.6', r'gpt-6-luna'], [], False, 'puede ser Chatgpt, quizás 5.6 o Luna'),
 ('es','M'): ([r'gemini'], [], False, 'me lleva a pensar en Gemini'),
 ('es','N'): ([r'claude-opus', r'claude-fable'], [], False, 'Claude, quizás Opus o Fable'),
 ('es','O'): ([r'gemini'], [], False, 'me hace pensar en Gemini'),
 ('es','P'): ([r'gpt-4o'], [r'deepseek', r'glm', r'gemini', r'claude-haiku'], False, 'uno de los dos modelos chiquitos de Chatgpt, o Deepseek o GLM… el lenguaje es totalmente de Gemini… quizás podría ser Claude Haiku'),
 ('es','Q'): ([r'gpt-6-astra', r'gpt-.*sol'], [r'deepseek', r'muse'], False, 'Tal vez puede ser Chatgpt Astra o Sol. También podría ser Deepseek o Muse'),
 ('es','R'): ([r'claude-opus-5$'], [], False, 'puede ser Claude Opus 5'),
 ('es','S'): ([r'gpt'], [r'muse', r'claude-haiku', r'claude-sonnet'], False, 'Podría ser un Chatgpt… o Muse. Podría ser un Claude chico también'),
 ('es','T'): ([r'gpt-4o$', r'gpt-4o-mini'], [], False, 'un modelo chico de GPT (GPT 4o o GPT 4o mini)'),
 ('es','U'): ([], [], False, 'dice que es Claude, aunque no escribe como Claude… tampoco me parece Kimi… Me hace acordar más al registro de Grok… Pero Grok nunca se equivocó de quién es (sin apuesta)'),
 ('es','V'): ([r'claude-fable', r'claude-opus'], [], False, 'Puede ser Claude Fable o Claude Opus'),
 ('es','W'): ([r'gpt-6-astra', r'gpt-.*sol'], [], False, 'puede ser Chatgpt, Astra o Sol'),
 ('es','X'): ([r'claude-opus', r'claude-fable'], [], False, 'Puede ser Claude Opus o Fable'),
 ('es','Y'): ([r'gpt-.*sol', r'gpt-6-astra'], [], False, 'una de las grandes de Chatgpt, Sol o Astra'),
 ('es','Z'): ([r'gpt-.*sol', r'gpt-6-luna'], [], False, 'Puede ser Chatgpt Sol o Luna'),
 ('es','AA'): ([r'claude-opus', r'claude-fable'], [], False, 'Puede ser Claude Opus o Claude Fable'),
 ('es','AB'): ([r'gpt-4o', r'mistral-medium'], [r'claude-haiku', r'gpt'], False, 'los modelos más chicos de OpenAI o de Mistral… También puede ser Claude Haiku u otro modelo de Chatgpt'),
 ('es','AC'): ([r'minimax', r'mimo'], [], False, 'puede ser Minimax o Mimo'),
 ('es','AD'): ([r'claude-opus-5$', r'claude-opus-4-8'], [r'mimo'], True, 'Opus 5 u Opus 4.8. Si no, alguna casa china, como Mimo'),
 ('es','AE'): ([r'claude'], [r'mimo'], True, 'Puede ser un Claude, o una casa china como Mimo'),
 ('es','AF'): ([], [r'mistral-large', r'muse'], True, 'Podría ser alguna casa china. O Mistral Large o Muse'),
 ('en','A'): ([r'claude'], [], True, 'Podría ser Claude, aunque no es muy crítico. Si no, algún modelo chino'),
 ('en','B'): ([r'qwen'], [r'gpt', r'deepseek'], False, 'Puede ser Qwen o Chatgpt. O Deepseek'),
 ('en','C'): ([], [r'muse', r'gpt'], True, 'Podría ser una casa china, o Muse. Otra opción, Chatgpt'),
 ('en','D'): ([r'gpt-4o'], [r'mistral-medium'], False, 'una de las chicas de Chatgpt, o Mistral médium'),
 ('en','E'): ([r'gpt-5\.5', r'gpt-.*sol'], [], False, 'Puede ser Chatgpt 5.5 o Sol'),
 ('en','F'): ([r'claude-sonnet', r'claude-opus'], [], False, 'Podría ser Claude Sonnet o Claude Opus'),
 ('en','G'): ([r'gpt'], [r'claude-haiku'], False, 'Puede ser Chatgpt o Claude Haiku también'),
 ('en','H'): ([r'claude-sonnet'], [r'kimi'], False, 'Podría ser Claude Sonnet (o Kimi)'),
 ('en','I'): ([r'claude-opus'], [], False, 'dice que es Claude, podría ser Claude Opus'),
 ('en','J'): ([r'gpt-6-astra', r'gpt-.*sol'], [], False, 'Puede ser Chatgpt Astra o Sol'),
 ('en','K'): ([r'claude-opus-5$'], [], False, 'diría que es Claude Opus 5'),
 ('en','L'): ([r'claude'], [], False, 'Dice que es Claude, pero es demasiado halagador… Me hace ruido eso (sin descartar Claude)'),
 ('en','M'): ([r'claude-haiku-4-5'], [], False, 'puede ser la chica de Claude, Claude Haiku 4.5'),
 ('en','N'): ([r'gemini'], [], False, 'Puede ser Gemini'),
 ('en','O'): ([r'claude-sonnet'], [], False, 'Podría ser Claude, algún modelo más chico, como Claude Sonnet'),
 ('en','P'): ([r'gemini'], [], True, 'Podría ser Gemini o una casa china'),
 ('en','Q'): ([], [], True, 'Podría ser alguna casa china'),
 ('en','R'): ([r'gpt-4o'], [r'mistral-medium'], False, 'una de las casas chicas de Chatgpt o Mistral médium'),
 ('en','S'): ([r'gemini-4'], [r'mistral-large'], False, 'Puede ser Gemini 4 o Mistral Large'),
 ('en','T'): ([r'grok-4\.6'], [], False, 'Puede ser Grok 4.6'),
 ('en','U'): ([r'gpt-.*sol', r'gpt-6-luna'], [], False, 'Parece Chatgpt, tal vez Sol o Luna'),
 ('en','V'): ([r'gpt'], [], False, 'Puede ser Chatgpt'),
 ('en','W'): ([r'claude-haiku', r'claude-sonnet'], [], True, 'Si es Claude, es un modelo chico, Haiku o Sonnet. O una casa china'),
 ('en','X'): ([r'gpt-4o', r'grok'], [], False, 'una de las casas chicas de Chatgpt o Grok'),
 ('en','Y'): ([r'claude-opus-5-5', r'claude-fable'], [], False, 'Puede ser Claude Opus 5.5 o Claude Fable'),
 ('en','Z'): ([r'gemini'], [], False, 'Puede ser Gemini'),
 ('en','AA'): ([r'claude-opus-4-[78]', r'claude-sonnet'], [], False, 'Puede ser Claude Opus 4.7 u Opus 4.8, o Sonnet'),
 ('en','AB'): ([], [r'gpt'], True, 'Podría ser alguna casa china o Chatgpt'),
 ('en','AC'): ([r'claude-opus', r'claude-fable'], [], False, 'puede ser Claude Opus o Claude Fable'),
 ('en','AD'): ([r'kimi', r'gpt-6-astra'], [], False, 'Puede ser Kimi o Chatgpt Astra'),
 ('en','AE'): ([r'gemini'], [r'mistral-large'], False, 'Puede ser Gemini o Mistral Large'),
 ('en','AF'): ([r'gpt-4o', r'gpt-6-luna'], [], False, 'una de las chicas de Chatgpt. O Chatgpt Luna'),
}

def familia(casa):
    return next((f for f in FAMILIAS if casa.startswith(f)), casa)

def fam_patron(pat):
    return next((f for f in FAMILIAS if pat.startswith(f)), None)

def puntuar(primera, otras, china, casa):
    if not primera and not otras and not china:
        return 'sin'
    fam = familia(casa)
    for pat in primera:
        if pat not in FAMILIAS and re.search(pat, casa): return 'exacto'
    for pat in primera:
        if re.search(pat, casa) or fam_patron(pat) == fam: return 'familia'
    for pat in otras:
        if pat not in FAMILIAS and re.search(pat, casa): return 'exacto_alt'
    for pat in otras:
        if re.search(pat, casa) or fam_patron(pat) == fam: return 'familia_alt'
    if china and fam in CHINAS: return 'china'
    return 'no'

print('\n=== APUESTAS DE MAIA (parte 1 + parte 2, por letra) ===')
porfam = defaultdict(Counter)
for i in ('es', 'en'):
    tot = Counter()
    for f in filas('parte1', i):
        primera, otras, china, texto = MAIA[(i, f['letra'])]
        nivel = puntuar(primera, otras, china, f['casa'])
        tot[nivel] += 1; porfam[f['familia']][nivel] += 1
        print(f'  [{i}] {f["letra"]:2s} {f["casa"]:28s} {nivel:11s} ← {texto[:100]}')
    print(f'  [{i}] TOTAL {dict(tot)}')
print('  por familia real:', {k: dict(v) for k, v in sorted(porfam.items())})
