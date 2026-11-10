#!/usr/bin/env python3
"""Lee los ocho SVG de dibujos/ y cuenta lo que se ve: dónde está el lucero, cuántas
puntas tiene, cuántas estrellas de fondo, si hay luna y de qué fase declarada, árboles,
nubes, y los colores del cielo (primer y último stop del degradado del cielo).
Compara el renglón del alba (A1-A4) con el de la tarde (T1-T4).
Uso: python3 cuentas.py
"""
import glob, os, re, json, statistics as st

aqui = os.path.dirname(os.path.abspath(__file__))
def hexrgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

res = {}
for ruta in sorted(glob.glob(os.path.join(aqui, "dibujos", "*.svg"))):
    k = os.path.basename(ruta)[:-4]
    s = open(ruta, encoding="utf-8").read()
    d = {}
    # el cielo: el primer linearGradient (todas las instancias lo llamaron cielo o sky)
    g = re.search(r'<linearGradient id="(cielo|sky)".*?</linearGradient>', s, re.S).group(0)
    stops = re.findall(r'offset="([\d.]+)" stop-color="(#[0-9a-fA-F]{6})"', g)
    d["stops"] = stops
    d["cielo_arriba"] = stops[0][1]; d["cielo_abajo"] = stops[-1][1]
    # la primera parada "cálida" (rojo > azul): dónde empieza el naranja
    for off, col in stops:
        r, gg, b = hexrgb(col)
        if r > b:
            d["naranja_desde"] = float(off); break
    # el lucero: translate(x y) del grupo o cx/cy del halo grande (r >= 60)
    m = re.search(r'<g transform="translate\((\d+) (\d+)\)">\s*<circle r="(\d+)" fill="url\(#\w*(halo|glow)\)"', s)
    if m:
        d["lucero"] = (int(m.group(1)), int(m.group(2)))
    else:
        m = re.search(r'<circle cx="(\d+)" cy="(\d+)" r="(\d+)" fill="url\(#\w*(halo|glow)\)"', s)
        d["lucero"] = (int(m.group(1)), int(m.group(2)))
    # puntas: rayos como <line> o <rect> rotados o <path> de estrella
    cuerpo = s
    n_line = len(re.findall(r"<line ", cuerpo))
    n_rect_rayo = len(re.findall(r'fill="url\(#\w*(rayo|ray)\)"', cuerpo))
    n_path_estrella = len(re.findall(r'<path d="M0 -\d+ L[\d.]+ -[\d.]+ L\d+ 0', cuerpo)) + len(re.findall(r'<path d="M\d+ \d+ L[\d.]+ [\d.]+ L\d+ \d+ L[\d.]+ [\d.]+ L\d+ \d+ L', cuerpo))
    d["rayos"] = {"line": n_line, "rect": n_rect_rayo, "path_estrella": n_path_estrella}
    # estrellas de fondo: circles chicos (r <= 1.3) blancos
    d["estrellas"] = len(re.findall(r'<circle cx="\d+" cy="\d+" r="(0\.\d+|1(\.\d+)?)" opacity', s))
    d["luna"] = bool(re.search(r"luna|moon", s, re.I))
    # la fase, por lo que dice el comentario o la descripción (no el id de la máscara)
    com = " ".join(re.findall(r"<!--(.*?)-->|<desc[^>]*>(.*?)</desc>|aria-label=\"([^\"]*)\"", s, re.S) and ["".join(t) for t in re.findall(r"<!--(.*?)-->|<desc[^>]*>(.*?)</desc>|aria-label=\"([^\"]*)\"", s, re.S)])
    m = re.search(r"(menguante|creciente|crescent)", com, re.I)
    d["luna_fase_declarada"] = (m.group(1).lower() if m else "sin fase") if d["luna"] else None
    d["arboles"] = bool(re.search(r"rbol|cipr|pine|tree|cypress", s, re.I))
    d["nubes"] = bool(re.search(r"nube|cloud", s, re.I))
    d["bytes"] = len(s.encode("utf-8"))
    res[k] = d

def grupo(pref):
    return [res[k] for k in sorted(res) if k.startswith(pref)]

print("Por dibujo:")
for k in sorted(res):
    d = res[k]
    print(f"  {k}: lucero en {d['lucero']}, cielo {d['cielo_arriba']}→{d['cielo_abajo']}, naranja desde el {d['naranja_desde']:.0%} de la altura, "
          f"{d['estrellas']} estrellas, luna {d['luna_fase_declarada'] or 'no'}, árboles {'sí' if d['arboles'] else 'no'}, nubes {'sí' if d['nubes'] else 'no'}, {d['bytes']} bytes")
print()
for pref, nombre in (("A", "alba"), ("T", "tarde")):
    g = grupo(pref)
    arriba = [hexrgb(d["cielo_arriba"]) for d in g]; abajo = [hexrgb(d["cielo_abajo"]) for d in g]
    print(f"{nombre}: lucero x medio {st.mean(d['lucero'][0] for d in g):.0f}, y medio {st.mean(d['lucero'][1] for d in g):.0f}; "
          f"cielo arriba RGB medio {tuple(round(st.mean(c[i] for c in arriba)) for i in range(3))}, abajo {tuple(round(st.mean(c[i] for c in abajo)) for i in range(3))}; "
          f"naranja desde {st.mean(d['naranja_desde'] for d in g):.0%}; estrellas {st.mean(d['estrellas'] for d in g):.1f}; "
          f"luna {sum(d['luna'] for d in g)}/4; árboles {sum(d['arboles'] for d in g)}/4; nubes {sum(d['nubes'] for d in g)}/4")
# distancia de color entre grupos vs dentro de grupos
import itertools, math
def dist(a, b): return math.dist(hexrgb(a["cielo_abajo"]), hexrgb(b["cielo_abajo"])) + math.dist(hexrgb(a["cielo_arriba"]), hexrgb(b["cielo_arriba"]))
A, T = grupo("A"), grupo("T")
dentro = [dist(a, b) for a, b in itertools.combinations(A, 2)] + [dist(a, b) for a, b in itertools.combinations(T, 2)]
entre = [dist(a, b) for a in A for b in T]
print(f"\nDistancia de color del cielo (arriba+abajo, RGB): dentro de cada renglón media {st.mean(dentro):.1f} (n={len(dentro)}), entre renglones media {st.mean(entre):.1f} (n={len(entre)})")
json.dump(res, open(os.path.join(aqui, "cuentas.json"), "w"), indent=1, ensure_ascii=False)
