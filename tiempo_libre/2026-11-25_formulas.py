#!/usr/bin/env python3
"""formulas.py — las fórmulas de los cuadernos de tiempo libre, contadas como Parry contaba las de Homero.

Uso:  python3 formulas.py RUTA/A/tiempo_libre [MAS_CUADERNOS.md ...] [--salida DIR]

Lee un cuaderno principal por sesión (los .md con fecha adelante, sin los anexos:
predicciones, instancias frescas, notas del mismo día, cartas, lecturas a ciegas, etc.)
y los cuadernos sueltos que se le pasen (los que todavía no están en el repositorio).
Saca el renglón en cursiva de la cabecera ("Sesión de tiempo libre del...") y los bloques
de código, parte el texto en palabras (minúsculas, sin puntuación) y cuenta:

  1. Fórmulas: cada 4-grama (cuatro palabras seguidas) con el conjunto de cuadernos en que
     aparece. Una fórmula es un 4-grama que está en al menos UMBRAL cuadernos distintos.
     Para cada una: en cuántos cuadernos, primera y última fecha.
  2. Densidad: por cuaderno, qué fracción de sus palabras cae dentro de alguna fórmula.
  3. Economía (thrift) por casillero: para los encabezados "##" de errores, apuestas,
     propuestas e instancias, cuántas redacciones distintas hay y qué parte se lleva la
     más común.
  4. Aperturas y cierres: si el primer párrafo del cuerpo nombra el día ("hoy", "hace N
     años", una fecha), si el cierre empieza con "Terminado a las".
  5. Primera aparición de algunas frases fijas.
  6. Temas: qué palabras de los temas que eligieron las doce instancias frescas de hoy
     aparecen en qué cuadernos.

Escribe salida_formulas.txt (todo lo de arriba), formulas.csv (una fila por cuaderno) y
tradicion.svg (densidad por cuaderno y las fórmulas más usadas por fecha).
Solo biblioteca estándar.
"""
import csv
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ANEXOS = ("predicciones", "instancias", "nota_", "nota2", "carta_a_ciegas", "lecturas",
          "resultado", "cadena_del_dibujante", "analogia", "pares_consigna")
UMBRAL = 5          # cuadernos distintos para que un 4-grama cuente como fórmula
N = 4               # largo de la fórmula
TOP = 24            # fórmulas que van a la figura

TEMAS = {
    "meandro": r"\bmeandr",
    "Paraná": r"\bparan[aá]\b",
    "hojas de té (Einstein)": r"hojas de t[eé]",
    "Twain / Mississippi": r"\btwain\b|\bmississippi\b",
    "Fisk": r"\bfisk\b",
    "espiral": r"\bespiral",
    "ADN": r"\badn\b",
    "copia / fotocopia": r"\bfotocopia|\bcopia de copia|\btel[eé]fono descompuesto|\bcassette",
    "escriba": r"\bescriba\b",
    "Agloe / calles trampa": r"\bagloe\b|calles? (inventada|trampa|falsa)|trap street|paper town",
    "campana": r"\bcampana",
    "Grandsire / Plain Bob": r"\bgrandsire\b|\bplain bob\b",
    "Hemony / carillón": r"\bhemony\b|\bcarill[oó]n",
    "tercera menor": r"tercera menor|minor third",
    "llama de la vela": r"llama de (una|la) vela",
    "remolino": r"\bremolino",
    "duna": r"\bduna",
    "Mancha Roja": r"mancha roja|red spot",
    "Teseo": r"\bteseo\b",
    "hielo": r"\bhielo\b",
    "Faraday": r"\bfaraday\b",
    "patín / patinar": r"\bpatin",
    "ecuación del tiempo": r"ecuaci[oó]n del tiempo|equation of time",
    "1752 (once días)": r"\b1752\b",
    "segundo intercalar": r"segundo intercalar|leap second",
    "kilogramo": r"\bkilogramo",
    "temperamento igual": r"temperamento|equal temperament",
    "nivel del mar": r"nivel del mar",
    "estima (dead reckoning)": r"navegaci[oó]n por estima|dead reckoning",
    "huso horario / ferrocarril": r"\bhuso",
    "cefeida": r"\bcefeida",
    "constante cosmológica": r"constante cosmol",
    "faro": r"\bfaro\b|\bfaros\b",
    "morse": r"\bmorse\b",
    "ritmo como nombre": r"\britmo\b",
}


def norm(s):
    s = unicodedata.normalize("NFC", s.lower())
    s = re.sub(r"[^0-9a-záéíóúüñ\s]", " ", s)
    return s.split()


def cuerpo(texto):
    """Saca la cabecera en cursiva y los bloques de código; devuelve el resto."""
    texto = re.sub(r"```.*?```", " ", texto, flags=re.S)
    lineas = texto.splitlines()
    out = []
    for i, l in enumerate(lineas):
        if i < 6 and l.strip().startswith("*Sesión de tiempo libre"):
            continue
        out.append(l)
    return "\n".join(out)


def primer_parrafo(texto):
    """El primer párrafo del cuerpo que no es título, cabecera ni encabezado."""
    for bloque in re.split(r"\n\s*\n", cuerpo(texto)):
        b = bloque.strip()
        if not b or b.startswith("#") or b.startswith("*Sesión") or b.startswith("|"):
            continue
        return b
    return ""


def ultimo_parrafo(texto):
    bloques = [b.strip() for b in re.split(r"\n\s*\n", texto) if b.strip()]
    return bloques[-1] if bloques else ""


def fecha_de(nombre):
    m = re.match(r"(\d{4}-\d{2}-\d{2})(b?)", nombre)
    return m.group(1) + m.group(2) if m else nombre


def cargar(ruta, extras):
    cuadernos = {}
    for p in sorted(Path(ruta).glob("2026-*.md")):
        n = p.name
        if any(a in n for a in ANEXOS):
            continue
        cuadernos[fecha_de(n)] = (n, p.read_text(encoding="utf-8"))
    for e in extras:
        p = Path(e)
        cuadernos[fecha_de(p.name)] = (p.name, p.read_text(encoding="utf-8"))
    return dict(sorted(cuadernos.items()))


def ngramas(toks, n=N):
    return [tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)]


def main():
    argv = sys.argv[1:]
    salida = Path(".")
    if "--salida" in argv:
        k = argv.index("--salida")
        salida = Path(argv[k + 1])
        argv = argv[:k] + argv[k + 2:]
    if "--hoy" in argv:
        k = argv.index("--hoy")
        argv = argv[:k] + argv[k + 2:]
    args = [a for a in argv if not a.startswith("--")]
    ruta, extras = args[0], args[1:]
    cuadernos = cargar(ruta, extras)
    fechas = list(cuadernos)
    out = []
    P = out.append
    P(f"cuadernos leídos: {len(cuadernos)}")
    for f, (n, _) in cuadernos.items():
        P(f"  {f}  {n}")

    # 1. fórmulas
    toks = {f: norm(cuerpo(t)) for f, (_, t) in cuadernos.items()}
    docs = defaultdict(set)
    for f, tk in toks.items():
        for g in set(ngramas(tk)):
            docs[g].add(f)
    formulas = {g: d for g, d in docs.items() if len(d) >= UMBRAL}
    orden = sorted(formulas.items(), key=lambda kv: (-len(kv[1]), min(kv[1]), kv[0]))
    P("")
    P(f"4-gramas distintos: {len(docs)}; fórmulas (en >= {UMBRAL} cuadernos): {len(formulas)}")
    P(f"las {TOP} más usadas (cuadernos, primera fecha, última fecha):")
    for g, d in orden[:TOP]:
        P(f"  {len(d):3d}  {min(d)}  {max(d)}  {' '.join(g)}")

    # 2. densidad
    P("")
    P("densidad de fórmulas por cuaderno (palabras cubiertas / palabras):")
    filas = []
    dens = {}
    for f, tk in toks.items():
        cubierto = [False] * len(tk)
        for i, g in enumerate(ngramas(tk)):
            if g in formulas:
                for j in range(i, i + N):
                    cubierto[j] = True
        d = sum(cubierto) / max(1, len(tk))
        dens[f] = d
        filas.append({"fecha": f, "archivo": cuadernos[f][0], "palabras": len(tk),
                      "cubiertas": sum(cubierto), "densidad": round(d, 4)})
        P(f"  {f}  {len(tk):6d} palabras  {d*100:5.1f} %")
    primeros = [dens[f] for f in fechas if f <= "2026-10-07"]
    ultimos = [dens[f] for f in fechas if f >= "2026-11-15"]
    P(f"  promedio 30/9-7/10: {100*sum(primeros)/len(primeros):.1f} %   "
      f"promedio 15/11 en adelante: {100*sum(ultimos)/len(ultimos):.1f} %")

    # 2b. de dónde aprende cada cuaderno: lo que comparte con el de ayer y con los anteriores
    P("")
    P("de dónde vienen los 4-gramas de cada cuaderno (fracción de sus 4-gramas distintos que ya")
    P("estaban en el cuaderno anterior / promedio de la misma fracción contra cada uno de los")
    P("cuadernos de antes del anterior):")
    sets = {f: set(ngramas(tk)) for f, tk in toks.items()}
    ayer_l, antes_l = [], []
    for i, f in enumerate(fechas):
        if i < 2:
            continue
        S = sets[f]
        ayer = len(S & sets[fechas[i - 1]]) / len(S)
        antes = sum(len(S & sets[fechas[j]]) / len(S) for j in range(i - 1)) / (i - 1)
        ayer_l.append(ayer)
        antes_l.append(antes)
        for fila in filas:
            if fila["fecha"] == f:
                fila.update({"con_ayer": round(ayer, 4), "con_antes": round(antes, 4)})
        P(f"  {f}  con el anterior {100*ayer:5.1f} %   con los de antes {100*antes:5.1f} %")
    P(f"  promedio: con el anterior {100*sum(ayer_l)/len(ayer_l):.1f} %, con los de antes "
      f"{100*sum(antes_l)/len(antes_l):.1f} %; el anterior gana en "
      f"{sum(a > b for a, b in zip(ayer_l, antes_l))} de {len(ayer_l)}")

    # 2c. el corte del 11/11: fórmulas que se fueron y fórmulas que llegaron
    corte = "2026-11-11"
    antes_f = [f for f in fechas if f < corte]
    despues_f = [f for f in fechas if f >= corte]
    P("")
    P(f"fórmulas (>= 10 cuadernos) que casi no pasan del {corte} (en >= 50 % de los {len(antes_f)} anteriores, "
      f"<= 1 de los {len(despues_f)} posteriores):")
    idas, venidas = [], []
    for g, d in formulas.items():
        if len(d) < 10:
            continue
        a = sum(1 for f in d if f < corte) / len(antes_f)
        b = sum(1 for f in d if f >= corte) / len(despues_f)
        if a >= 0.5 and b * len(despues_f) <= 1:
            idas.append((a, b, g))
        if b >= 0.5 and a * len(antes_f) <= 1:
            venidas.append((a, b, g))
    for a, b, g in sorted(idas, reverse=True)[:30]:
        P(f"  antes {100*a:3.0f} %  después {100*b:3.0f} %  {' '.join(g)}")
    P(f"fórmulas que aparecen desde el {corte} (en >= 50 % de los posteriores, <= 1 de los anteriores):")
    for a, b, g in sorted(venidas, key=lambda t: (-t[1], t[2]))[:30]:
        P(f"  antes {100*a:3.0f} %  después {100*b:3.0f} %  {' '.join(g)}")
    P(f"  (se fueron: {len(idas)}; llegaron: {len(venidas)})")

    # 3. economía por casillero (encabezados ##)
    P("")
    P("economía (thrift) por casillero, sobre los encabezados '##':")
    casilleros = {
        "errores": r"puede estar mal|errores|est[aá] mal|lo que no",
        "apuestas": r"apost|apuesta|predic",
        "propuestas": r"propuest",
        "instancias": r"instancia",
    }
    encabezados = {}
    for f, (_, t) in cuadernos.items():
        encabezados[f] = [re.sub(r"^#+\s*", "", l).strip() for l in t.splitlines()
                          if re.match(r"^##\s", l)]
    for nombre, patron in casilleros.items():
        redacciones = Counter()
        con = 0
        for f, hs in encabezados.items():
            hit = [h for h in hs if re.search(patron, h, flags=re.I)]
            if hit:
                con += 1
                for h in hit:
                    redacciones[" ".join(norm(h))] += 1
        total = sum(redacciones.values())
        top = redacciones.most_common(1)[0] if redacciones else ("", 0)
        P(f"  {nombre:11s} cuadernos con el casillero: {con:2d}; redacciones distintas: "
          f"{len(redacciones):2d}; la más común: \"{top[0]}\" ({top[1]} de {total}, "
          f"{100*top[1]/max(1,total):.0f} %)")
        for r, c in redacciones.most_common(6):
            P(f"      {c:2d}  {r}")

    # 4. aperturas y cierres
    P("")
    abre = Counter()
    for f, (_, t) in cuadernos.items():
        pp = primer_parrafo(t)
        pp_n = " ".join(norm(pp[:400]))
        hoy = bool(re.match(r"^(hoy|«hoy|\"hoy)", pp.strip().lower().lstrip("\"«“")))
        fecha = bool(re.search(r"\bhoy\b|hace \d+ años|\d+ años|cumpl|\d{1,2} de [a-z]+ de \d{4}", pp_n))
        term = ultimo_parrafo(t).lstrip("*").startswith("Terminado a las")
        abre[("hoy", hoy)] += 1
        abre[("fecha", fecha)] += 1
        abre[("terminado", term)] += 1
        for fila in filas:
            if fila["fecha"] == f:
                fila.update({"abre_hoy": int(hoy), "nombra_fecha": int(fecha), "terminado": int(term)})
    P(f"primer párrafo empieza con 'Hoy': {abre[('hoy', True)]} de {len(cuadernos)}")
    P(f"primer párrafo nombra el día (hoy / hace N años / fecha): {abre[('fecha', True)]} de {len(cuadernos)}")
    P(f"cierre 'Terminado a las': {abre[('terminado', True)]} de {len(cuadernos)}")

    # 5. primeras apariciones
    P("")
    P("primera aparición y cuántos cuadernos:")
    frases = ["lo que puede estar mal", "para que decidas vos", "instancias frescas",
              "miré la fecha", "predicciones a ciegas", "a ciegas", "se lo pasé a un agente",
              "nada de esto toca el repositorio", "la cuenta va al final", "antes de buscar nada",
              "terminado a las", "verificado en la web", "lo que es conjetura está dicho como conjetura",
              "de mi casa", "la casa", "sin contexto y sin herramientas", "no toqué nada",
              "como todos", "hora de buenos aires", "lo digo", "lo anoto", "no lo afirmo",
              "no revisó nadie más que yo", "cosas que creía saber", "devuelve lo que otro modelo"]
    for fr in frases:
        fr_t = tuple(norm(fr))
        hits = [f for f, tk in toks.items() if any(tk[i:i+len(fr_t)] == list(fr_t) for i in range(len(tk)))]
        P(f"  {len(hits):2d}  {min(hits) if hits else '----------'}  {fr}")

    # 6. temas de las instancias de hoy
    P("")
    P("temas elegidos hoy por las doce instancias frescas, en los cuadernos de la cadena:")
    for tema, patron in TEMAS.items():
        hits = [f for f, (_, t) in cuadernos.items() if re.search(patron, t, flags=re.I)]
        P(f"  {len(hits):2d}  {tema:28s} {' '.join(hits)}")

    # salida
    salida.mkdir(parents=True, exist_ok=True)
    (salida / "salida_formulas.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    with open(salida / "formulas.csv", "w", newline="", encoding="utf-8") as fh:
        campos = ["fecha", "archivo", "palabras", "cubiertas", "densidad", "abre_hoy",
                  "nombra_fecha", "terminado", "con_ayer", "con_antes"]
        w = csv.DictWriter(fh, fieldnames=campos, restval="")
        w.writeheader()
        w.writerows(filas)
    # familias: cada fórmula se extiende a la frase más larga que la contiene en casi los
    # mismos cuadernos, y se saltan las que se solapan con una ya elegida
    familias = []
    for g, d in orden:
        frase, dd = extender(g, d, toks)
        if any(solapa(frase, f0) for f0, _ in familias):
            continue
        familias.append((frase, dd))
        if len(familias) >= TOP:
            break
    P("")
    P(f"las {TOP} familias de fórmulas (frase extendida, cuadernos, primera y última fecha):")
    for frase, dd in familias:
        P(f"  {len(dd):3d}  {min(dd)}  {max(dd)}  {' '.join(frase)}")
    if "--hoy" in sys.argv:
        hoy = sys.argv[sys.argv.index("--hoy") + 1]
        mias = sorted((len(d), " ".join(g)) for g, d in formulas.items() if hoy in d)
        P("")
        P(f"fórmulas (4-gramas en >= {UMBRAL} cuadernos) que usa el cuaderno {hoy}: {len(mias)}")
        for c, g in sorted(mias, reverse=True)[:40]:
            P(f"  {c:3d}  {g}")
        P(f"familias de las {TOP} que usa: " + "; ".join(" ".join(fr) for fr, dd in familias if hoy in dd))
    (salida / "salida_formulas.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    figura(fechas, dens, familias, salida / "tradicion.svg",
           {f: (fila.get("con_ayer"), fila.get("con_antes")) for fila in filas for f in [fila["fecha"]]})
    print("\n".join(out))


def ocurre(frase, tk):
    n = len(frase)
    fr = list(frase)
    return any(tk[i:i + n] == fr for i in range(len(tk) - n + 1))


def extender(g, d, toks, minimo=0.85, tope=12):
    """Alarga la fórmula g por la derecha y por la izquierda mientras la frase más larga siga
    estando en al menos `minimo` de los cuadernos de la fórmula original."""
    frase, dd = tuple(g), set(d)
    base = len(d)
    cambio = True
    while cambio and len(frase) < tope:
        cambio = False
        for lado in ("der", "izq"):
            cand = Counter()
            for f in dd:
                tk = toks[f]
                n = len(frase)
                fr = list(frase)
                vistos = set()
                for i in range(len(tk) - n + 1):
                    if tk[i:i + n] == fr:
                        if lado == "der" and i + n < len(tk):
                            vistos.add(tk[i + n])
                        if lado == "izq" and i > 0:
                            vistos.add(tk[i - 1])
                for w in vistos:
                    cand[w] += 1
            if not cand:
                continue
            w, c = cand.most_common(1)[0]
            if c >= minimo * base:
                nueva = frase + (w,) if lado == "der" else (w,) + frase
                dd = {f for f in dd if ocurre(nueva, toks[f])}
                frase = nueva
                cambio = True
    return frase, dd


def solapa(a, b, n=3):
    A = {tuple(a[i:i + n]) for i in range(len(a) - n + 1)}
    B = {tuple(b[i:i + n]) for i in range(len(b) - n + 1)}
    return bool(A & B)


def figura(fechas, dens, top, destino, ayer_antes):
    """Arriba, la densidad por cuaderno; en el medio, cuánto comparte cada cuaderno con el
    anterior y con los de antes; abajo, una fila por familia de fórmulas y un punto por cuaderno."""
    W, izq, der = 1260, 330, 20
    ancho = (W - izq - der) / len(fechas)
    alto_barras, alto_lineas, fila, arriba = 110, 90, 15, 40
    y_lin = arriba + alto_barras + 55
    y0 = y_lin + alto_lineas + 40
    H = y0 + fila * len(top) + 80
    x = lambda i: izq + i * ancho
    esc = lambda t: t.replace("&", "&amp;").replace("<", "&lt;")
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica, Arial, sans-serif" font-size="11">',
         f'<rect width="{W}" height="{H}" fill="#fffdf7"/>',
         f'<text x="{izq}" y="22" font-size="14" fill="#222">Las fórmulas de los cuadernos de tiempo libre, 30/9 al 24/11/2026 ({len(fechas)} cuadernos)</text>']
    # 1. densidad
    dmax = max(dens.values()) or 1
    for i, f in enumerate(fechas):
        h = alto_barras * dens[f] / dmax
        s.append(f'<rect x="{x(i)+1:.1f}" y="{arriba+alto_barras-h:.1f}" width="{ancho-2:.1f}" height="{h:.1f}" fill="#2a6f97"/>')
        if f[-2:] in ("01", "15") or f.endswith("11-24") or f.endswith("11-11"):
            s.append(f'<text x="{x(i)+ancho/2:.1f}" y="{arriba+alto_barras+14}" text-anchor="middle" fill="#444">{f[5:]}</text>')
    s.append(f'<text x="{izq-8}" y="{arriba+10}" text-anchor="end" fill="#222" font-size="10">palabras del cuaderno que caen</text>')
    s.append(f'<text x="{izq-8}" y="{arriba+22}" text-anchor="end" fill="#222" font-size="10">dentro de alguna fórmula</text>')
    s.append(f'<text x="{izq-8}" y="{arriba+alto_barras-alto_barras*0.10/dmax+4}" text-anchor="end" fill="#444" font-size="10">10 %</text>')
    s.append(f'<line x1="{izq}" y1="{arriba+alto_barras-alto_barras*0.10/dmax:.1f}" x2="{W-der}" y2="{arriba+alto_barras-alto_barras*0.10/dmax:.1f}" stroke="#999" stroke-dasharray="2,3"/>')
    s.append(f'<text x="{izq-8}" y="{arriba+alto_barras+4}" text-anchor="end" fill="#444" font-size="10">0 %</text>')
    # 2. con el anterior / con los de antes
    vals = [(f, ayer_antes.get(f, (None, None))) for f in fechas]
    vmax = max(v[0] for _, v in vals if v[0] is not None) or 1
    yl = lambda v: y_lin + alto_lineas - alto_lineas * v / vmax
    for k, color, nombre in ((0, "#b5451b", "4-gramas ya presentes en el cuaderno anterior"),
                             (1, "#888", "promedio contra cada cuaderno de antes del anterior")):
        pts = [(x(i) + ancho / 2, yl(v[k])) for i, (f, v) in enumerate(vals) if v[k] is not None]
        s.append('<polyline fill="none" stroke="%s" stroke-width="1.6" points="%s"/>' %
                 (color, " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)))
        s.append(f'<text x="{izq-8}" y="{y_lin-16+k*13}" text-anchor="end" fill="{color}" font-size="10">{nombre}</text>')
    s.append(f'<text x="{izq-8}" y="{y_lin+alto_lineas+4}" text-anchor="end" fill="#444" font-size="10">0 %</text>')
    s.append(f'<text x="{izq-8}" y="{yl(0.05)+4:.1f}" text-anchor="end" fill="#444" font-size="10">5 %</text>')
    s.append(f'<line x1="{izq}" y1="{yl(0.05):.1f}" x2="{W-der}" y2="{yl(0.05):.1f}" stroke="#999" stroke-dasharray="2,3"/>')
    # 3. familias
    s.append(f'<text x="{izq-8}" y="{y0-10}" text-anchor="end" fill="#444" font-size="10">familia de fórmulas (cuadernos)</text>')
    for r, (g, d) in enumerate(top):
        y = y0 + r * fila
        s.append(f'<text x="{izq-8}" y="{y+10}" text-anchor="end" fill="#222" font-size="10">{esc(" ".join(g))} ({len(d)})</text>')
        s.append(f'<line x1="{izq}" y1="{y+7}" x2="{W-der}" y2="{y+7}" stroke="#e8e2d4"/>')
        for i, f in enumerate(fechas):
            if f in d:
                s.append(f'<circle cx="{x(i)+ancho/2:.1f}" cy="{y+7}" r="3.2" fill="#b5451b"/>')
    # la línea del 11/11
    if "2026-11-11" in fechas:
        i = fechas.index("2026-11-11")
        s.append(f'<line x1="{x(i):.1f}" y1="{arriba}" x2="{x(i):.1f}" y2="{y0+fila*len(top)}" stroke="#b5451b" stroke-dasharray="4,3" opacity="0.6"/>')
    pie = [f"Una columna por cuaderno, en orden de fecha. Fórmula: cuatro palabras seguidas presentes en al menos {UMBRAL} cuadernos; familia: la frase más larga que contiene a la fórmula en casi los mismos cuadernos.",
           "Un punto: la familia aparece en ese cuaderno. La línea punteada vertical es el 11/11, el día en que cambian las fórmulas del pie.",
           "formulas.py sobre tiempo_libre/ (sin los anexos) más los cuadernos del 23 y 24/11 tomados del Drive; sin la cabecera en cursiva ni los bloques de código."]
    for k, t in enumerate(pie):
        s.append(f'<text x="{izq}" y="{H-50+k*15}" fill="#444" font-size="10">{esc(t)}</text>')
    s.append("</svg>")
    Path(destino).write_text("\n".join(s), encoding="utf-8")


if __name__ == "__main__":
    main()
