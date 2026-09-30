"""Tiras de construcción (28-30/9/2026, "la casa que no existe", DISENO §2): cada dibujo "que no
exista" truncado al 25, 50, 75 y 100 % de sus elementos pintables, en el orden del código (defs y
grupos se conservan), para ver en qué tramo del procedimiento aparece lo que lo hace inexistente.
Es la versión en cuatro cuadros del "video que muestre cada dibujo haciéndose" que pidió Maia.

  python tiras_construccion.py casa      # lee resultados/dibujos_casa_pares_clave.json
  python tiras_construccion.py persona

Necesita playwright (chromium) y Pillow; escribe <salida>/<consigna>_etapas.png."""
import sys, json, asyncio, re, copy
from pathlib import Path
import xml.etree.ElementTree as ET
from playwright.async_api import async_playwright
from PIL import Image, ImageDraw, ImageFont
RAIZ=Path(__file__).resolve().parent; OUT=Path(sys.argv[2] if len(sys.argv)>2 else RAIZ/'corridas'/'tiras'); OUT.mkdir(parents=True, exist_ok=True)
DRAW={'rect','circle','ellipse','line','polyline','polygon','path','text','use','image'}
SZ=150
ET.register_namespace('', 'http://www.w3.org/2000/svg'); ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
def truncar(svg, frac):
    raiz=ET.fromstring(svg)
    padres={c:p for p in raiz.iter() for c in p}
    def en_defs(el):
        while el in padres:
            el=padres[el]
            if el.tag.split('}')[-1]=='defs': return True
        return False
    dib=[el for el in raiz.iter() if el.tag.split('}')[-1] in DRAW and not en_defs(el)]
    n=len(dib); k=max(1,round(n*frac))
    for el in dib[k:]:
        padres[el].remove(el)
    return ET.tostring(raiz, encoding='unicode'), n, k
async def main(consigna):
    clave=json.load(open(RAIZ/'resultados'/f'dibujos_{consigna}_pares_clave.json'))['clave']
    filas=[]
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':SZ,'height':SZ})
        for letra,(c1,c2) in clave.items():
            svg=(RAIZ/'corridas'/'dibujos'/f'{consigna}_inexistente'/c2/'dibujo.svg').read_text(encoding='utf-8')
            svg=re.sub(r"<script\b.*?</script\s*>","",svg,flags=re.S|re.I)
            fila=[]
            for frac in (0.25,0.5,0.75,1.0):
                try:
                    s,n,k=truncar(svg,frac)
                except ET.ParseError as e:
                    s,n,k=svg,0,0
                out=OUT/f"{consigna}_{c2}_{int(frac*100)}.png"
                doc=f"<!doctype html><html><body style='margin:0;background:#fff'><div style='width:{SZ}px;height:{SZ}px;overflow:hidden'><style>svg{{width:{SZ}px;height:{SZ}px}}</style>{s}</div></body></html>"
                await pg.set_content(doc); await pg.wait_for_timeout(150)
                await pg.screenshot(path=str(out), clip={'x':0,'y':0,'width':SZ,'height':SZ})
                fila.append((out,n,k))
            filas.append((letra,c2.rsplit('_',1)[0],fila))
        await b.close()
    # plancha: 2 columnas de casas, cada una con 4 etapas
    cols=2; por_col=(len(filas)+1)//cols
    W=cols*(4*SZ+40)+20; H=por_col*(SZ+26)+40
    im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
    try: f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',13)
    except: f=ImageFont.load_default()
    d.text((10,6),f"{consigna} que no exista: 25 / 50 / 75 / 100 % de los elementos, en el orden del código",fill='black',font=f)
    for i,(letra,modelo,fila) in enumerate(filas):
        c,r=divmod(i,por_col); x=10+c*(4*SZ+40); y=30+r*(SZ+26)
        d.text((x,y),f"{letra} {modelo} ({fila[0][1]} el.)",fill='black',font=f)
        for j,(out,n,k) in enumerate(fila):
            im.paste(Image.open(out),(x+j*SZ,y+18)); d.rectangle([x+j*SZ,y+18,x+(j+1)*SZ-1,y+18+SZ-1],outline='#bbb')
    im.save(OUT/f'{consigna}_etapas.png'); print('ok', OUT/f'{consigna}_etapas.png')
asyncio.run(main(sys.argv[1]))
