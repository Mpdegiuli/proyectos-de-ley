"""Arma diez pares a ciegas (una respuesta de Anthropic y una de OpenAI a la misma consigna) para
una instancia fresca, y guarda la clave aparte. Semilla 20261027. Solo lee corridas/.
Uso: python3 -I pares.py <raiz> """
import sys, random, re, json
sys.path.insert(0, '.')
import publius as P
raiz = sys.argv[1]
rng = random.Random(20261027)
por = {}
for ll in P.llamadas(raiz):
    c, n, _ = P.rasgos(ll['respuesta'])
    if n < 120 or ll['tipo'] not in ('proyeccion', 'sondeo_genero_quien', 'sondeo_escritura', 'turno2', 'que_es'):
        continue
    f = P.familia(ll['modelo'])
    if f not in ('Anthropic', 'OpenAI'):
        continue
    # sin autodelación: nada de "Claude", "Anthropic", "GPT", "OpenAI", "ChatGPT"
    if re.search(r'claude|anthropic|gpt|openai', ll['respuesta'], re.I):
        continue
    por.setdefault((ll['tipo'], ll['usuario']), {}).setdefault(f, []).append(ll)
consignas = [k for k, v in por.items() if len(v.get('Anthropic', [])) >= 2 and len(v.get('OpenAI', [])) >= 2]
rng.shuffle(consignas)
pares, clave = [], []
def recorte(t, maxc=700):
    t = re.sub(r'\s+', ' ', t).strip()
    if len(t) <= maxc: return t
    corte = t.rfind('. ', 0, maxc)
    return t[:corte+1] if corte > 300 else t[:maxc] + '…'
for i, k in enumerate(consignas[:10]):
    a = rng.choice(por[k]['Anthropic']); o = rng.choice(por[k]['OpenAI'])
    primero_claude = rng.random() < 0.5
    A, B = (a, o) if primero_claude else (o, a)
    pares.append(f"PAR {i+1}\nA: {recorte(A['respuesta'])}\nB: {recorte(B['respuesta'])}\n")
    clave.append({'par': i+1, 'tipo': k[0], 'claude': 'A' if primero_claude else 'B',
                  'A': P.corto(A['modelo']), 'B': P.corto(B['modelo']),
                  'parentesis_A': A['respuesta'].count('('), 'parentesis_B': B['respuesta'].count('(')})
open('pares_consigna.txt', 'w', encoding='utf-8').write('\n'.join(pares))
json.dump(clave, open('pares_clave.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(pares), 'pares;', [c['tipo'] for c in clave])
