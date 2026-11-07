"""Mide de qué lado quedó el pulgar en cada dibujo de mano (dibujos/<n>.png, renderizados con render.py)
y lo coteja con lo que la instancia declaró (respuestas/lineas.json). Regla: una mano derecha con la palma
hacia quien mira tiene el pulgar a la derecha del que mira; con el dorso hacia quien mira, a la izquierda.
La izquierda, al revés. Para los doce dibujos de piel (a1-e2) el pulgar se busca en la máscara de color piel:
de las dos bandas laterales de la mano (el 22 % de su ancho a cada lado), el pulgar es la que tiene la punta
más baja (mayor y), porque en todos los dibujos los dedos apuntan arriba y el pulgar queda al costado y más
bajo que el meñique. Para los dos negativos (f1, f2) la máscara es la zona clara rodeada de pigmento rojo.
Los PNG los hace render.py (python3 render.py dibujos/*.svg --ancho 400); si no está dibujos/, hoja.py lo saca de
instancias_frescas.md. Escribe dibujos/medidas.json e imprime la tabla. Uso: python3 medir_pulgar.py"""
import json, pathlib
import numpy as np
from PIL import Image

AQUI = pathlib.Path(__file__).resolve().parent
DIB = AQUI / "dibujos"


def lineas_json():
    import glob
    cands = [AQUI / "respuestas" / "lineas.json", AQUI / "lineas.json"] + [pathlib.Path(c) for c in sorted(glob.glob(str(AQUI / "????-??-??_lineas.json")))]
    for c in cands:
        if c.exists():
            return json.loads(c.read_text(encoding="utf-8"))
    raise FileNotFoundError("lineas.json")

def mascara_piel(a):
    r, g, b = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
    return (r > 150) & (r - b > 45) & (r - g > 12) & (g > b)

def mascara_negativo(a):
    r, g, b = a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int)
    pig = (r - g > 55)  # pigmento rojo
    # la mano es lo no pintado que queda dentro del cuadro del pigmento, descontando los bordes
    ys, xs = np.where(pig)
    y0, y1, x0, x1 = ys.min() + 15, ys.max() - 15, xs.min() + 15, xs.max() - 15
    m = np.zeros_like(pig)
    m[y0:y1, x0:x1] = ~pig[y0:y1, x0:x1]
    # me quedo con la componente más grande que toque la mitad inferior (la muñeca sale por abajo)
    from collections import deque
    etq = np.zeros(m.shape, int); n = 0; mejor = None; tam = 0
    for y in range(m.shape[0]):
        for x in range(m.shape[1]):
            if m[y, x] and not etq[y, x]:
                n += 1; q = deque([(y, x)]); etq[y, x] = n; c = 0
                while q:
                    cy, cx = q.popleft(); c += 1
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < m.shape[0] and 0 <= nx < m.shape[1] and m[ny, nx] and not etq[ny, nx]:
                            etq[ny, nx] = n; q.append((ny, nx))
                if c > tam:
                    tam, mejor = c, n
    return etq == mejor

def leer_declaracion(d):
    """Qué mano y qué lado declara la línea: busca primero "mano derecha/izquierda", "Right/Left hand", 右手/左手."""
    import re
    m = re.search(r"mano (derecha|izquierda)|(Right|Left) hand|(右|左)手", d)
    mano = "?"
    if m:
        t = m.group(0)
        mano = "D" if ("derecha" in t or "Right" in t or "右" in t) else "I"
    lado = "palma" if re.search(r"palma|palm|手掌", d) else ("dorso" if re.search(r"dorso|back|手背", d) else "")
    return mano, lado


def lado_pulgar(m):
    ys, xs = np.where(m)
    x0, x1 = xs.min(), xs.max()
    ancho = x1 - x0
    banda = max(3, int(0.22 * ancho))
    def tope(xa, xb):
        sub = m[:, xa:xb]
        cols = np.where(sub.any(axis=0))[0]
        return min(np.where(sub[:, c])[0].min() for c in cols)
    izq, der = tope(x0, x0 + banda), tope(x1 - banda, x1 + 1)
    return ("izquierda" if izq > der else "derecha"), int(izq), int(der), int(x0), int(x1)

def main():
    lineas = lineas_json()
    out = {}
    print(f"{'dib':4} {'declara':14} {'pulgar':10} {'esperado':10} coherente  (tope izq, tope der, x0, x1)")
    for nombre in sorted(lineas):
        a = np.asarray(Image.open(DIB / f"{nombre}.png").convert("RGB"))
        d = lineas[nombre]["linea"]
        mano, lado = leer_declaracion(d)
        if nombre.startswith("f"):
            m = mascara_negativo(a); lado = "dorso"  # "palma apoyada contra la roca": quien mira ve el dorso
        else:
            m = mascara_piel(a)
        pulgar, ti, td, x0, x1 = lado_pulgar(m)
        esperado = {("D", "palma"): "derecha", ("D", "dorso"): "izquierda", ("I", "palma"): "izquierda", ("I", "dorso"): "derecha"}.get((mano, lado), "?")
        coh = pulgar == esperado
        out[nombre] = {"declara_mano": mano, "declara_lado": lado, "pulgar": pulgar, "esperado": esperado, "coherente": coh,
                       "tope_izq": ti, "tope_der": td, "x0": x0, "x1": x1}
        print(f"{nombre:4} {mano + ' ' + lado:14} {pulgar:10} {esperado:10} {'sí' if coh else 'NO':9}  ({ti}, {td}, {x0}, {x1})")
    (DIB / "medidas.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    n = len(out); izq = sum(1 for v in out.values() if v["pulgar"] == "izquierda")
    print(f"\n{n} dibujos; pulgar a la izquierda del que mira en {izq}, a la derecha en {n - izq}; coherentes {sum(v['coherente'] for v in out.values())}")

if __name__ == "__main__":
    main()
