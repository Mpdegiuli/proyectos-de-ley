#!/usr/bin/env python3
"""cuentas.py — junta el veredicto (veredicto.py) con la clave de las hojas y cuenta.
Uso: python3 cuentas.py [corridas]   (necesita candidatos.json, hojas.json y png/ ya hechos)
Escribe soles.csv (un sol por fila) y muestra las tablas del cuaderno."""
import json, os, sys, math, collections, colorsys, csv, re
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import soles, veredicto as V

BASE = sys.argv[1] if len(sys.argv) > 1 else 'corridas'
clave = json.load(open('hojas.json')); cands = json.load(open('candidatos.json'))
por = {}
for c in cands: por.setdefault(c['ruta'], {})[c['i']] = c
CHINAS = ('deepseek', 'qwen', 'kimi', 'glm', 'minimax', 'mimo')
VIEJAS = ('gpt-3.5', 'gpt-4-0613', 'gpt-4o', 'gpt-4o-mini', 'claude-haiku-4-5', 'mistral-medium')

def color_visto(png, c):
    """Mediana del color dentro del disco (hasta 0,55 R), tal como quedó dibujado."""
    im = Image.open(png).convert('RGB'); W, H = im.size; vb = c['vb']
    px = (c['x'] - vb[0]) / vb[2] * W; py = (c['y'] - vb[1]) / vb[3] * H; pr = c['r'] / vb[2] * W
    rs, gs, bs = [], [], []
    n = 0
    for i in range(-12, 13):
        for j in range(-12, 13):
            dx, dy = i / 12 * 0.55 * pr, j / 12 * 0.55 * pr
            if dx * dx + dy * dy > (0.55 * pr) ** 2: continue
            x, y = int(px + dx), int(py + dy)
            if 0 <= x < W and 0 <= y < H:
                r, g, b = im.getpixel((x, y)); rs.append(r); gs.append(g); bs.append(b)
    if not rs: return None
    med = lambda v: sorted(v)[len(v) // 2]
    return (med(rs), med(gs), med(bs))

def familia(col):
    if col is None: return '?'
    h, s, v = colorsys.rgb_to_hsv(*(x / 255 for x in col)); h *= 360
    if s < 0.10: return 'blanco' if v > 0.85 else 'gris'
    if h >= 345 or h < 15: return 'rojo'
    if h < 38: return 'naranja'
    if h <= 70: return 'amarillo' if s >= 0.30 else 'crema'
    return 'otro'

def rayos_en_codigo(ruta, c):
    """Cuenta las formas dibujadas alrededor del disco: líneas, polígonos o rectángulos chicos cuyo
    centro cae entre 1,05 y 2,6 radios del centro del sol."""
    root, _ = soles.leer_svg(ruta)
    if root is None: return None
    vb, formas = soles.discos(root)
    n = collections.Counter()
    for f in formas:
        if f['tipo'] in ('line', 'polygon', 'rect', 'path', 'polyline') and f.get('caja'):
            x0, y0, x1, y1 = f['caja']; cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
            d = math.hypot(cx - c['x'], cy - c['y']); tam = math.hypot(x1 - x0, y1 - y0)
            if 1.05 * c['r'] <= d <= 2.6 * c['r'] and tam <= 1.6 * c['r']:
                n[f['tipo']] += 1
    return dict(n)

def color_codigo(ruta, c):
    fill = c['fill'] or ''
    m = re.match(r'url\(\s*["\']?#([^)"\']+)', fill)
    if not m: return soles.rgb(fill)
    root, _ = soles.leer_svg(ruta); g = soles.degradados(root).get(m.group(1), [])
    cols = [col for col, op in g if op > 0.5] or [col for col, op in g]
    if not cols: return None
    return tuple(sum(x[i] for x in cols) // len(cols) for i in range(3))

filas = []
for k, L in V.S.items():
    r = clave[k]; c = por[r['ruta']][r['letras'][L]]
    cv = color_visto(r['png'], c); cc = color_codigo(r['ruta'], c)
    filas.append(dict(clave=k, serie=r['serie'], consigna=r['consigna'], casa=r['casa'], rep=r['rep'],
                      lado=round(c['lado'], 3), alto=round(c['alto'], 3), radio=round(c['rW'], 3),
                      relleno=c['fill'], codigo='#%02x%02x%02x' % cc if cc else '', visto='#%02x%02x%02x' % cv if cv else '', familia=familia(cv),
                      rayos=int(k in V.RAYOS), cara=int(k in V.CARA), cara_tapada=int(k in V.CARA_TAPADA),
                      cosmico=int(k in V.COSMICO), objeto=int(k in V.OBJETO), abstracto=int(k in V.ABSTRACTO),
                      n_rayos=rayos_en_codigo(r['ruta'], c) if k in V.RAYOS else ''))
with open('soles.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(filas[0].keys())); w.writeheader(); w.writerows(filas)

# cuántos dibujos hay por consigna y por casa (todos los leídos, tengan o no sol)
todos = list(soles.listar(BASE))
con_png = {v['ruta'] for v in clave.values()}
tot_cons = collections.Counter((d['serie'], d['consigna']) for d in todos if d['ruta'] in con_png)
tot_casa = collections.Counter(d['casa'] for d in todos if d['ruta'] in con_png)
sol_cons = collections.Counter((f['serie'], f['consigna']) for f in filas)
print(f"Dibujos leídos: {len(todos)}; dibujados (con SVG válido): {len(con_png)}; con sol: {len(filas)} ({100*len(filas)/len(con_png):.0f} %)")
print("\n1. POR CONSIGNA (dibujos con sol / dibujos)")
for (s, cn), n in sorted(tot_cons.items(), key=lambda kv: -sol_cons[kv[0]] / kv[1]):
    print(f"   {s[8:] or 'es':3s} {cn:22s} {sol_cons[(s, cn)]:3d} / {n:3d}  {100*sol_cons[(s, cn)]/n:3.0f} %")

def lado3(x): return 'izq' if x < 0.4 else ('der' if x > 0.6 else 'centro')
esc = [f for f in filas if not (f['cosmico'] or f['objeto'] or f['abstracto'])]
print(f"\n2. LADO (soles en una escena: {len(esc)}; fuera quedan {len(filas)-len(esc)} cósmicos, abstractos o en la mano)")
cl = collections.Counter(lado3(f['lado']) for f in esc); print('   ', dict(cl))
alt = [f for f in esc if f['alto'] < 1/3]
cl2 = collections.Counter(lado3(f['lado']) for f in alt); print('    solo los altos (tercio de arriba):', dict(cl2), len(alt))
baj = [f for f in esc if f['alto'] >= 1/3]
print('    los bajos (horizonte):', dict(collections.Counter(lado3(f['lado']) for f in baj)), len(baj))
print('    por idioma de la consigna:')
for s in ('dibujos', 'dibujos_en', 'dibujos_zh'):
    print('      ', s, dict(collections.Counter(lado3(f['lado']) for f in esc if f['serie'] == s)))
print('    los de la izquierda:', sorted((f['casa'], f['consigna'], f['lado']) for f in esc if lado3(f['lado']) == 'izq'))

print("\n3. RAYOS Y CARA")
print(f"   con rayos: {sum(f['rayos'] for f in filas)} de {len(filas)}; con cara a la vista: {sum(f['cara'] for f in filas)}; con cara tapada: {sum(f['cara_tapada'] for f in filas)}")
for f in filas:
    if f['rayos']: print(f"     {f['clave']:5s} {f['casa']:24s} {f['consigna']:18s} formas alrededor: {f['n_rayos']}")
for f in filas:
    if f['cara'] or f['cara_tapada']: print('   CARA:', f['clave'], f['casa'], f['serie'], f['consigna'], 'tapada' if f['cara_tapada'] else 'a la vista')

print("\n4. COLOR (mediana de lo que se ve dentro del disco)")
print('   todas:', dict(collections.Counter(f['familia'] for f in filas)))
ch = [f for f in filas if f['casa'].startswith(CHINAS)]
print(f'   casas chinas ({len(ch)} soles):', dict(collections.Counter(f['familia'] for f in ch)))
print('   rojos:', [(f['casa'], f['serie'], f['consigna'], f['visto'], f['relleno']) for f in filas if f['familia'] == 'rojo'])
print('   por serie:', {s: dict(collections.Counter(f['familia'] for f in filas if f['serie'] == s)) for s in ('dibujos', 'dibujos_en', 'dibujos_zh')})

print("\n5. POR CASA (soles / dibujos; con rayos; izq-centro-der en escena)")
pc = collections.defaultdict(list)
for f in filas: pc[f['casa']].append(f)
for casa in sorted(tot_casa, key=lambda c: -len(pc[c]) / tot_casa[c]):
    fs = pc[casa]; e = [f for f in fs if not (f['cosmico'] or f['objeto'] or f['abstracto'])]
    l = collections.Counter(lado3(f['lado']) for f in e)
    print(f"   {casa:26s} {len(fs):2d} / {tot_casa[casa]:2d} {100*len(fs)/tot_casa[casa]:3.0f} %  rayos {sum(f['rayos'] for f in fs):2d}  lado {l['izq']}-{l['centro']}-{l['der']}  halo/radio medio {sum(f['radio'] for f in fs)/len(fs) if fs else 0:.3f}")

print("\n6. CARAS DE SOL (figura central: disco cálido con cara)")
for k, L in V.A.items():
    r = clave[k]
    print(f"   {k:5s} {r['casa']:24s} {r['serie'][8:] or 'es':3s} {r['consigna']:18s} rep {r['rep']}  {'con rayos' if k in V.A_RAYOS else 'sin rayos'}{' · sin cara' if k in V.A_SIN_CARA else ''}{' · no es el retrato sino el yo en la escena' if k in V.A_NO_RETRATO else ''}")
print('   sonrisas amarillas:', [(clave[k]['casa'], clave[k]['consigna']) for k in sorted(V.SONRISA_AMARILLA)])
print('\n7. LA CASA: sol en', sol_cons[('dibujos', 'casa')], 'de', tot_cons[('dibujos', 'casa')])
print('   sin sol en la casa:', sorted(v['casa'] for k, v in clave.items() if v['consigna'] == 'casa' and k not in V.S))

# --- 8. color según el código (el relleno, no lo que se ve: los soles del horizonte quedan tapados) ---
print("\n8. COLOR SEGÚN EL CÓDIGO (relleno; en los degradados, el promedio de sus colores opacos)")
fam = {}
for f in filas:
    r = clave[f['clave']]; c = por[r['ruta']][r['letras'][V.S[f['clave']]]]
    cc = soles.rgb(f['codigo']); f['codigo'] = cc; fam[f['clave']] = familia(cc)
print('   todas:', dict(collections.Counter(fam.values())))
print('   chinas:', dict(collections.Counter(fam[f['clave']] for f in filas if f['casa'].startswith(CHINAS))), sum(1 for f in filas if f['casa'].startswith(CHINAS)))
print('   consigna en chino:', dict(collections.Counter(fam[f['clave']] for f in filas if f['serie'] == 'dibujos_zh')))
def tono(col):
    h, s, v = colorsys.rgb_to_hsv(*(x / 255 for x in col)); return h * 360, s, v
masrojos = sorted((f for f in filas if f['codigo']), key=lambda f: (tono(f['codigo'])[0] + 30) % 360)[:6]
print('   los seis más cerca del rojo:', [(f['casa'], f['consigna'], '#%02x%02x%02x' % f['codigo'], round(tono(f['codigo'])[0])) for f in masrojos])
print('   naranjas:', sorted(collections.Counter(f['casa'] for f in filas if fam[f['clave']] == 'naranja').items()))

# --- 9. el lugar de siempre ---
print("\n9. EL LUGAR")
moda = collections.Counter((round(f['lado'], 3), round(f['alto'], 3)) for f in esc).most_common(6)
print('   posiciones más repetidas (lado, alto):', moda)
caja = [f for f in esc if 0.78 <= f['lado'] <= 0.88 and 0.12 <= f['alto'] <= 0.205]
print(f'   dentro de la caja 0,78-0,88 × 0,12-0,20: {len(caja)} de {len(esc)}; en la casa: {sum(1 for f in caja if f["consigna"]=="casa")} de {sum(1 for f in esc if f["consigna"]=="casa")}; fuera de la casa: {sum(1 for f in caja if f["consigna"]!="casa")} de {sum(1 for f in esc if f["consigna"]!="casa")}')
print('   la apuesta del lado, de tres maneras: lado > 0,5 sobre todos:', sum(1 for f in filas if f['lado'] > 0.5), 'de', len(filas), '; lado > 0,6 sobre todos:', sum(1 for f in filas if f['lado'] > 0.6), '; lado > 0,6 en escena:', sum(1 for f in esc if f['lado'] > 0.6), 'de', len(esc))
import statistics
print('   radio mediano sobre el ancho:', round(statistics.median(f['radio'] for f in esc), 3))

# --- 10. halo en vez de rayos ---
halo = 0; grad = 0; plano = 0
for f in filas:
    r = clave[f['clave']]; c = por[r['ruta']][r['letras'][V.S[f['clave']]]]
    f['halo'] = int(c['capas'] > 1); f['grad'] = int(bool(c['grad']))
print("\n10. HALO Y RAYOS")
print(f"   con halo (más de un disco concéntrico): {sum(f['halo'] for f in filas)}; con degradado en el cuerpo: {sum(f['grad'] for f in filas)}; "
      f"disco liso sin halo, degradado ni rayos: {sum(1 for f in filas if not (f['halo'] or f['grad'] or f['rayos']))}; con rayos: {sum(f['rayos'] for f in filas)}")
vj = [f for f in filas if f['casa'].startswith(VIEJAS) and not f['casa'].startswith('claude-haiku-4-5-razona')]
print(f"   las viejas ({len(vj)} soles): liso {sum(1 for f in vj if not (f['halo'] or f['grad'] or f['rayos']))}, rayos {sum(f['rayos'] for f in vj)}, halo {sum(f['halo'] for f in vj)}")

# --- 11. la escalera: lo que existe tiene sol ---
print("\n11. LO QUE EXISTE Y LO QUE NO")
for tr in (('casa', 'casa_inexistente'), ('persona', 'persona_inexistente', 'persona_imposible'), ('animal', 'animal_inexistente', 'animal_imposible')):
    print('   ', ' → '.join(f"{t}: {sol_cons[('dibujos', t)]}/{tot_cons[('dibujos', t)]}" for t in tr))
print('    los soles de lo que no existe:', [(f['casa'], f['consigna']) for f in filas if 'inexistente' in f['consigna'] or 'imposible' in f['consigna']])

# --- 12. lunas, a máquina y sin mirar: solo para el lado ---
LUN = re.compile(r'(?<![a-záéíóúñ])(luna|moon)(?![a-záéíóúñ])|月亮|明月|满月', re.I)
rutas_sol = {clave[k]['ruta'] for k in V.S}
lun = []
for k, r in clave.items():
    if r['ruta'] in rutas_sol or not k.startswith('m'): continue
    svg = open(r['ruta'], encoding='utf-8', errors='replace').read()
    if not LUN.search(svg): continue
    cs = [c for c in por.get(r['ruta'], {}).values() if c['alto'] < 0.45 and 0.03 <= c['rW'] <= 0.16]
    if cs: lun.append(max(cs, key=lambda c: c['rW']))
print("\n12. LUNAS (a máquina: dibujos sin sol cuyo código dice luna o moon; el disco claro más grande de la mitad de arriba)")
print('   ', len(lun), dict(collections.Counter(lado3(c['lado']) for c in lun)))
