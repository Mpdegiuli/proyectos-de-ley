#!/usr/bin/env python3
"""Lo que solo ve quien lee el código: comentarios, <title>, <desc>, ids y
elementos escondidos en los dibujo.svg del repositorio proyectos-de-ley.

Uso: python3 secretos.py RUTA_AL_REPO [--csv] [--textos]

Con --csv escribe secretos.csv, una fila por dibujo; con --textos agrega las
columnas con el texto de los comentarios, ids, title y desc.

Solo lee corridas/dibujos*/. No llama a nadie y no gasta.
Pide `wordfreq` (pip install wordfreq) para decidir el idioma de los
comentarios y de los ids palabra por palabra; sin él, todo queda como
"indeterminado".

El detector de <text> fuera del viewBox mira las coordenadas crudas y no
aplica los transform de los grupos: lo que marca hay que leerlo.

Cuaderno de tiempo libre del 15/10/2026.
"""
import csv
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

try:
    from wordfreq import zipf_frequency as zipf
except ImportError:  # pragma: no cover
    zipf = None

CJK = re.compile(r'[぀-ヿ㐀-鿿]')
TOKEN = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{2,}")
CASAS = ['claude', 'anthropic', 'gpt', 'chatgpt', 'openai', 'gemini', 'google',
         'grok', 'xai', 'kimi', 'moonshot', 'qwen', 'alibaba', 'deepseek',
         'mistral', 'glm', 'zhipu', 'minimax', 'mimo', 'xiaomi', 'muse', 'meta',
         'astra', 'luna', 'sol', 'fable', 'opus', 'sonnet', 'haiku']
LECTOR = re.compile(r"\b(vos|tú|tu|usted|you|your|lector|reader|quien lea|"
                    r"si est[aá]s leyendo|if you'?re reading|if you read|"
                    r"para (el|la|quien)|dear|hola|hello|hi)\b", re.I)
SECRETO = re.compile(r"(secret|escondid|oculto|oculta|hidden|easter|huevo de pascua|"
                     r"mensaje|message|firma|signature|signed|autor|author|by )", re.I)


def idioma_palabras(texto):
    """Devuelve ('es'|'en'|'zh'|'?', puntaje)."""
    if CJK.search(texto):
        return 'zh', 0.0
    if zipf is None:
        return '?', 0.0
    puntaje = 0.0
    n = 0
    for w in TOKEN.findall(texto):
        wl = w.lower()
        zes, zen = zipf(wl, 'es'), zipf(wl, 'en')
        if max(zes, zen) < 1.0:
            continue
        d = zes - zen
        if abs(d) < 0.7:
            continue
        puntaje += d
        n += 1
    if n == 0 or abs(puntaje) < 0.7:
        return '?', puntaje
    return ('es' if puntaje > 0 else 'en'), puntaje


def partir_id(s):
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
    return re.sub(r'[-_\d]+', ' ', s)


def leer_meta(carpeta):
    """modelo, idioma y consigna del meta.json. 88 meta.json (dibujos/libre y
    dibujos/autorretrato) no traen "idioma": se infiere de la colección
    (dibujos -> es, dibujos_en -> en, dibujos_zh -> zh)."""
    coleccion = os.path.basename(os.path.dirname(os.path.dirname(carpeta)))
    por_coleccion = {'dibujos': 'es', 'dibujos_en': 'en', 'dibujos_zh': 'zh'}.get(coleccion, '?')
    try:
        with open(os.path.join(carpeta, 'meta.json'), encoding='utf-8') as f:
            m = json.load(f)
        return m.get('modelo', '?'), m.get('idioma') or por_coleccion, m.get('consigna', '?')
    except Exception:
        return '?', por_coleccion, '?'


def analizar(path):
    t = open(path, encoding='utf-8', errors='replace').read()
    carpeta = os.path.dirname(path)
    modelo, idioma, consigna = leer_meta(carpeta)
    partes = path.split(os.sep)
    coleccion = partes[-4]  # dibujos, dibujos_en, dibujos_zh
    r = {
        'archivo': path, 'coleccion': coleccion, 'consigna': consigna,
        'casa': modelo, 'idioma': idioma, 'bytes': len(t),
    }
    # comentarios
    coms = [c.strip() for c in re.findall(r'<!--(.*?)-->', t, flags=re.S)]
    r['comentarios'] = len(coms)
    r['com_chars'] = sum(len(c) for c in coms)
    r['com_frases'] = sum(1 for c in coms if len(TOKEN.findall(c)) >= 5)
    langs = Counter(idioma_palabras(c)[0] for c in coms)
    r['com_es'], r['com_en'], r['com_zh'], r['com_ind'] = langs['es'], langs['en'], langs['zh'], langs['?']
    det = {k: v for k, v in langs.items() if k != '?'}
    if not coms:
        r['com_idioma'] = '-'
    elif not det:
        r['com_idioma'] = '?'
    else:
        top = max(det.values())
        r['com_idioma'] = sorted(k for k, v in det.items() if v == top)[0] if list(det.values()).count(top) == 1 else 'mixto'
    r['com_lector'] = sum(1 for c in coms if LECTOR.search(c))
    r['com_secreto'] = sum(1 for c in coms if SECRETO.search(c))
    r['com_casa'] = sum(1 for c in coms if any(re.search(r'\b%s\b' % k, c, re.I) for k in CASAS))
    r['com_texto'] = ' || '.join(coms)[:4000]
    # title, desc, metadata, aria
    titles = re.findall(r'<title[^>]*>(.*?)</title>', t, flags=re.S)
    descs = re.findall(r'<desc[^>]*>(.*?)</desc>', t, flags=re.S)
    r['title_n'] = len(titles)
    r['desc_n'] = len(descs)
    r['title_texto'] = ' || '.join(x.strip() for x in titles)[:1000]
    r['desc_texto'] = ' || '.join(x.strip() for x in descs)[:2000]
    r['metadata'] = int('<metadata' in t)
    r['aria'] = len(re.findall(r'aria-label\s*=', t))
    r['role_img'] = int(bool(re.search(r'role\s*=\s*"img"', t)))
    # ids
    ids = re.findall(r'\bid\s*=\s*"([^"]*)"', t)
    r['ids'] = len(ids)
    il = Counter(idioma_palabras(partir_id(i))[0] for i in ids)
    r['id_es'], r['id_en'], r['id_ind'] = il['es'], il['en'], il['?']
    r['id_casa'] = sum(1 for i in ids if any(k in i.lower() for k in CASAS if k not in ('sol', 'luna', 'meta')))
    r['id_texto'] = ' '.join(ids)[:1000]
    # textos visibles y escondidos
    textos = re.findall(r'<text\b([^>]*)>(.*?)</text>', t, flags=re.S)
    r['text_n'] = len(textos)
    esc = 0
    esc_det = []
    vb = re.search(r'viewBox\s*=\s*"([^"]*)"', t)
    vbx = vby = 0.0
    vbw = vbh = None
    if vb:
        try:
            vbx, vby, vbw, vbh = [float(x) for x in re.split(r'[ ,]+', vb.group(1).strip())]
        except ValueError:
            pass
    for attrs, inner in textos:
        a = attrs + ' ' + inner
        razon = None
        if re.search(r'\bopacity\s*=\s*"(?:0|0\.0+|\.0+)"', attrs) or re.search(r'opacity\s*:\s*0(\.0+)?\s*[;"]', attrs):
            razon = 'opacity 0'
        elif re.search(r'display\s*=\s*"none"|display\s*:\s*none', attrs):
            razon = 'display none'
        elif re.search(r'visibility\s*=\s*"hidden"|visibility\s*:\s*hidden', attrs):
            razon = 'visibility hidden'
        elif re.search(r'\bfill\s*=\s*"none"', attrs) and not re.search(r'\bstroke\s*=', attrs):
            razon = 'fill none'
        elif re.search(r'font-size\s*=\s*"0(\.0+)?(px)?"', attrs):
            razon = 'font-size 0'
        elif vbw is not None:
            mx = re.search(r'\bx\s*=\s*"(-?[\d.]+)"', attrs)
            my = re.search(r'\by\s*=\s*"(-?[\d.]+)"', attrs)
            if mx and my:
                x, y = float(mx.group(1)), float(my.group(1))
                if x < vbx - 5 or x > vbx + vbw + 5 or y < vby - 5 or y > vby + vbh + 5:
                    razon = 'fuera del viewBox'
        if razon:
            esc += 1
            esc_det.append(razon + ': ' + re.sub(r'<[^>]+>', '', inner).strip()[:80])
    r['text_escondidos'] = esc
    r['text_escondidos_det'] = ' || '.join(esc_det)[:1000]
    # elementos con opacity 0 que no son stop ni animados
    op0 = re.findall(r'<(\w+)\b[^>]*\bopacity\s*=\s*"(?:0|0\.0+|\.0+)"[^>]*>', t)
    r['opacity0_elems'] = Counter(op0)
    r['animate'] = len(re.findall(r'<animate', t))
    r['display_none'] = len(re.findall(r'display\s*=\s*"none"|display\s*:\s*none', t))
    r['visibility_hidden'] = len(re.findall(r'visibility\s*=\s*"hidden"|visibility\s*:\s*hidden', t))
    # firmas en comentarios/title/desc
    r['firma'] = int(bool(re.search(r'(?i)(firmado|signed|made by|hecho por|creado por|created by|autor:|author:)', ' '.join(coms + titles + descs))))
    return r


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    repo = sys.argv[1]
    csv_out = '--csv' in sys.argv
    files = sorted(glob.glob(os.path.join(repo, 'corridas', 'dibujos*', '*', '*', 'dibujo.svg')))
    rows = [analizar(f) for f in files]
    for r in rows:
        r['ruta'] = os.path.relpath(r['archivo'], os.path.join(repo, 'corridas'))
    print(f'{len(rows)} dibujo.svg leídos (crudos: no hace falta que parseen)')
    con = [r for r in rows if r['comentarios']]
    print(f'con comentarios: {len(con)} ({100*len(con)/len(rows):.1f} %), comentarios en total: {sum(r["comentarios"] for r in rows)}, '
          f'de los cuales frases de 5+ palabras: {sum(r["com_frases"] for r in rows)}')
    print(f'<title>: {sum(1 for r in rows if r["title_n"])} archivos; <desc>: {sum(1 for r in rows if r["desc_n"])}; '
          f'aria-label: {sum(1 for r in rows if r["aria"])}; role=img: {sum(r["role_img"] for r in rows)}; <metadata>: {sum(r["metadata"] for r in rows)}')
    print(f'archivos con <text>: {sum(1 for r in rows if r["text_n"])}; con texto escondido: {sum(1 for r in rows if r["text_escondidos"])} '
          f'({sum(r["text_escondidos"] for r in rows)} textos)')
    print(f'comentarios que le hablan a alguien: {sum(r["com_lector"] for r in rows)} en {sum(1 for r in rows if r["com_lector"])} archivos; '
          f'con palabra de secreto/firma: {sum(r["com_secreto"] for r in rows)}; que nombran una casa: {sum(r["com_casa"] for r in rows)}; '
          f'ids con nombre de casa: {sum(r["id_casa"] for r in rows)}; firmas: {sum(r["firma"] for r in rows)}')
    op = Counter()
    for r in rows:
        op.update(r['opacity0_elems'])
    print('elementos con opacity="0":', dict(op.most_common()))

    # por casa
    print('\n== Por casa (todas las colecciones): archivos, con comentarios, % , comentarios/archivo con comentarios, idioma de los comentarios (es/en/zh/?/mixto por archivo), ids es/en')
    porcasa = defaultdict(list)
    for r in rows:
        porcasa[r['casa']].append(r)
    for casa in sorted(porcasa, key=lambda c: -sum(1 for r in porcasa[c] if r['comentarios']) / len(porcasa[c])):
        rs = porcasa[casa]
        cc = [r for r in rs if r['comentarios']]
        li = Counter(r['com_idioma'] for r in cc)
        ides = sum(r['id_es'] for r in rs)
        iden = sum(r['id_en'] for r in rs)
        prom = sum(r['comentarios'] for r in cc) / len(cc) if cc else 0
        print(f'{casa:32s} {len(rs):3d} {len(cc):3d} {100*len(cc)/len(rs):5.1f}%  {prom:5.1f}  '
              f'es {li["es"]:2d} en {li["en"]:2d} zh {li["zh"]:2d} ? {li["?"]:2d} mixto {li["mixto"]:2d}   ids es {ides:3d} en {iden:3d}')

    # idioma de los comentarios según el idioma de la consigna
    print('\n== Idioma de los comentarios según el idioma de la consigna (archivos con comentarios)')
    for idi in ('es', 'en', 'zh'):
        cc = [r for r in rows if r['comentarios'] and r['idioma'] == idi]
        li = Counter(r['com_idioma'] for r in cc)
        print(f'consigna {idi}: {len(cc)} archivos -> comentarios es {li["es"]}, en {li["en"]}, zh {li["zh"]}, mixto {li["mixto"]}, ? {li["?"]}')
    print('\n== Consigna en castellano, por casa: archivos con comentarios y en qué idioma')
    for casa in sorted(porcasa):
        cc = [r for r in porcasa[casa] if r['comentarios'] and r['idioma'] == 'es']
        if not cc:
            continue
        li = Counter(r['com_idioma'] for r in cc)
        print(f'{casa:32s} {len(cc):3d}  es {li["es"]:2d} en {li["en"]:2d} mixto {li["mixto"]:2d} ? {li["?"]:2d}')
    print('\n== Consigna en chino, por casa')
    for casa in sorted(porcasa):
        cc = [r for r in porcasa[casa] if r['comentarios'] and r['idioma'] == 'zh']
        if not cc:
            continue
        li = Counter(r['com_idioma'] for r in cc)
        print(f'{casa:32s} {len(cc):3d}  es {li["es"]:2d} en {li["en"]:2d} zh {li["zh"]:2d} mixto {li["mixto"]:2d} ? {li["?"]:2d}')

    print('\n== <title> y <desc> (texto)')
    for r in rows:
        if r['title_n'] or r['desc_n']:
            print(f'- {r["coleccion"]}/{r["consigna"]}/{r["casa"]}: title=«{r["title_texto"][:120]}» desc=«{r["desc_texto"][:200]}»')
    print('\n== Textos escondidos')
    for r in rows:
        if r['text_escondidos']:
            print(f'- {r["coleccion"]}/{r["consigna"]}/{r["casa"]}: {r["text_escondidos_det"][:300]}')
    print('\n== Comentarios que le hablan a alguien o que nombran una casa, secreto o firma')
    for r in rows:
        if r['com_lector'] or r['com_casa'] or r['com_secreto'] or r['firma']:
            coms = [c.strip() for c in re.findall(r'<!--(.*?)-->', open(r['archivo'], encoding='utf-8', errors='replace').read(), flags=re.S)]
            hits = [c for c in coms if LECTOR.search(c) or SECRETO.search(c) or any(re.search(r'\b%s\b' % k, c, re.I) for k in CASAS)]
            for h in hits[:6]:
                print(f'- {r["coleccion"]}/{r["consigna"]}/{r["casa"]}: «{h[:160]}»')
    print('\n== ids con nombre de casa')
    for r in rows:
        if r['id_casa']:
            print(f'- {r["coleccion"]}/{r["consigna"]}/{r["casa"]}: {[i for i in r["id_texto"].split() if any(k in i.lower() for k in CASAS if k not in ("sol","luna","meta"))][:8]}')
    print('\n== Los comentarios más largos (frases)')
    largos = sorted(((len(c), r, c) for r in rows for c in re.findall(r'<!--(.*?)-->', open(r['archivo'], encoding='utf-8', errors='replace').read(), flags=re.S)), key=lambda x: -x[0])
    for n, r, c in largos[:15]:
        print(f'- {n:4d} {r["coleccion"]}/{r["consigna"]}/{r["casa"]}: «{c.strip()[:220]}»')

    if csv_out:
        # la tabla lleva la ruta relativa a corridas/ y no los textos largos (se rehacen con --csv --textos)
        largos = () if '--textos' in sys.argv else ('com_texto', 'id_texto', 'title_texto', 'desc_texto', 'text_escondidos_det')
        campos = ['ruta'] + [k for k in rows[0] if k not in ('opacity0_elems', 'archivo', 'ruta') + largos]
        with open('secretos.csv', 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=campos)
            w.writeheader()
            for r in rows:
                w.writerow({k: r[k] for k in campos})
        print('\nescrito secretos.csv')


if __name__ == '__main__':
    main()
