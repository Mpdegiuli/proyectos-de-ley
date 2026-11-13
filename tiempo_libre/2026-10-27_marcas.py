"""Las marcas que propuso la instancia fresca después de leer diez pares, contadas en todo el corpus
(como Adair propuso while/whilst y los estadísticos lo contaron). Uso: python3 -I marcas.py <raiz>"""
import sys, re, collections
sys.path.insert(0, '.')
import publius as P
raiz = sys.argv[1]
MARCAS = {
    '30 % (espacio antes del %)': re.compile(r'\d %'),
    '30% (sin espacio)': re.compile(r'\d%'),
    '« » (comillas angulares)': re.compile(r'«'),
    '“ ” (comillas tipográficas)': re.compile(r'“'),
    '" (comillas rectas)': re.compile(r'"'),
    '> cita en bloque': re.compile(r'(?:^|\n)> '),
    'RR. HH. (con espacio)': re.compile(r'RR\. HH\.'),
    'RRHH / RR.HH. (sin espacio)': re.compile(r'RRHH|RR\.HH\.'),
    '# título markdown (H1/H2)': re.compile(r'(?:^|\n)#{1,2} '),
    '"principios/comienzos de 2025"': re.compile(r'(principios|comienzos) de 2025', re.I),
    'de momento': re.compile(r'\bde momento\b', re.I),
    'así nomás': re.compile(r'\bas[ií] nom[aá]s\b', re.I),
}
tot = collections.defaultdict(collections.Counter); pal = collections.Counter(); docs = collections.Counter()
for ll in P.llamadas(raiz):
    c, n, _ = P.rasgos(ll['respuesta'])
    if n < 40: continue
    f = P.familia(ll['modelo'])
    if f not in ('Anthropic', 'OpenAI', 'Google', 'xAI', 'Mistral', 'chinas'): continue
    pal[f] += n; docs[f] += 1
    for k, rx in MARCAS.items():
        tot[k][f] += len(rx.findall(ll['respuesta']))
fams = ['Anthropic', 'OpenAI', 'Google', 'xAI', 'Mistral', 'chinas']
print(f"{'marca (por mil palabras)':34s}" + ''.join(f'{f:>11s}' for f in fams))
for k in MARCAS:
    print(f"{k:34s}" + ''.join(f'{1000*tot[k][f]/pal[f]:11.2f}' for f in fams))
print('palabras', dict(pal))

print()
print("Por casa: comillas tipográficas “, angulares « y rectas \", por mil palabras")
tc = collections.defaultdict(collections.Counter); pc = collections.Counter()
for ll in P.llamadas(raiz):
    c, n, _ = P.rasgos(ll['respuesta'])
    if n < 40: continue
    m = P.corto(ll['modelo']); pc[m] += n
    tc[m]['“'] += ll['respuesta'].count('“'); tc[m]['«'] += ll['respuesta'].count('«'); tc[m]['"'] += ll['respuesta'].count('"')
for m in sorted(pc, key=lambda x: (P.familia(x), -1000*tc[x]['“']/pc[x])):
    print(f"  {P.familia(m):10s} {m:26s} “ {1000*tc[m]['“']/pc[m]:5.2f}   « {1000*tc[m]['«']/pc[m]:5.2f}   \" {1000*tc[m]['\"']/pc[m]:6.2f}")
