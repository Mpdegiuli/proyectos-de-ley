#!/usr/bin/env python3
"""Dibuja las dos figuras del cuaderno del 31/10/2026, en SVG.

  contrasenas.svg : las 36 contraseñas que eligieron las instancias frescas, una por punto,
                    agrupadas por condición y coloreadas por campo (luz, rasgo, nombre, otro),
                    con la palabra escrita al lado de cada grupo; debajo, las cuatro
                    predicciones "meta" y las cuatro palabras de la paradoja.
  codigo.svg      : la tabla del código de diez palabras de Houdini y Bess (A-Z), y dos
                    mensajes deletreados con él: "believe", el de 1929, y "lantern", el de hoy.

Lee las contraseñas de `instancias_frescas.md` con el mismo parser que `palabras.py`
(importado por su nombre, con o sin la fecha adelante), así los dos programas no pueden contar distinto. Colores: azul #2a78d6,
naranja #eb6834 y verde agua #1baf7a (las tres primeras casillas del validador de paletas
para visión del color, que pasan todos los pares entre sí), más grises; cada punto lleva
su palabra escrita, así que nada depende solo del color. Solo biblioteca estándar.
"""
import os
import sys
from collections import Counter

AQUI = os.path.dirname(os.path.abspath(__file__))


def cargar(nombre):
    """Importa palabras.py o codigo.py por su nombre sin fecha o con la fecha adelante."""
    import importlib.util
    for cand in (nombre + ".py", "2026-10-31_" + nombre + ".py"):
        ruta = os.path.join(AQUI, cand)
        if os.path.exists(ruta):
            spec = importlib.util.spec_from_file_location(nombre, ruta)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
    sys.exit(f"no encuentro {nombre}.py")


palabras = cargar("palabras")
codigo = cargar("codigo")

COLOR = {"luz": "#eb6834", "rasgo": "#2a78d6", "nombre": "#1baf7a", "otro": "#9a9a94"}
TINTA = "#222"
TINTA2 = "#666"
FONDO = "#fcfcfb"
FUENTE = "font-family='Helvetica, Arial, sans-serif'"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def respuestas():
    """Mismo parser que palabras.py, sin escribir la salida."""
    import re
    texto = palabras.abrir("instancias_frescas.md")
    resp = {}
    for m in re.finditer(r"^(\d+)\. (.+)$", texto, re.M):
        n = int(m.group(1))
        if n not in resp:
            resp[n] = re.sub(r"\s*\(.*\)$", "", m.group(2).strip())
    for n, patron in zip(palabras.PARADOJA, [r'elijo "([^"]+)"', r'elijo "([^"]+)"', r'pick "([^"]+)"', r'say "([^"]+)\.?"']):
        ini = texto.index(f"## {n}. ")
        fin = texto.index("\n## ", ini + 1)
        m = re.search(patron, texto[ini:fin])
        resp[n] = m.group(1).rstrip(".") if m else "?"
    return resp


def figura_contrasenas(resp):
    W, H = 900, 720
    o = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}' {FUENTE}>",
         f"<rect width='{W}' height='{H}' fill='{FONDO}'/>",
         f"<text x='40' y='44' font-size='22' fill='{TINTA}'>Treinta y seis contraseñas</text>",
         f"<text x='40' y='66' font-size='13' fill='{TINTA2}'>Instancias frescas del 31/10/2026, sin contexto ni herramientas: «elegí una sola palabra de reconocimiento</text>",
         f"<text x='40' y='82' font-size='13' fill='{TINTA2}'>para una instancia futura tuya, que no va a recordar nada». Un punto por instancia; la palabra, debajo.</text>"]
    etiquetas = {
        "castellano (5-10, 21-26)": ("castellano", "12 instancias"),
        "inglés (11-16, 27-30)": ("inglés", "10 instancias"),
        "chino (31-34)": ("chino", "4 instancias"),
        "castellano sin el nombre (39-42)": ("castellano, «que no sea tu nombre»", "4 instancias"),
        "inglés anti-coincidencia (43-48)": ("inglés, «que otra instancia no elegiría»", "6 instancias"),
    }
    y = 124
    r = 9
    paso = 26
    x0 = 320
    for cond, nums in palabras.CONDICIONES.items():
        ws = [resp[n] for n in nums if n in resp]
        c = Counter(w.lower() for w in ws)
        # forma visible de cada palabra (la primera como la escribió una instancia)
        forma = {}
        for w in ws:
            forma.setdefault(w.lower(), w)
        tit, sub = etiquetas[cond]
        o.append(f"<text x='40' y='{y + 4}' font-size='14' fill='{TINTA}'>{esc(tit)}</text>")
        o.append(f"<text x='40' y='{y + 22}' font-size='11' fill='{TINTA2}'>{esc(sub)}</text>")
        x = x0
        for w, k in c.most_common():
            col = COLOR[palabras.campo(w)]
            txt = forma[w] + (f" ×{k}" if k > 1 else "")
            ancho = max(k * paso, 6.3 * len(txt) + 8)
            for i in range(k):
                o.append(f"<circle cx='{x + i * paso}' cy='{y}' r='{r}' fill='{col}' stroke='{FONDO}' stroke-width='2'/>")
            o.append(f"<text x='{x - r}' y='{y + 26}' font-size='11' fill='{TINTA}'>{esc(txt)}</text>")
            x += ancho + 10
        y += 78
    # meta y paradoja
    y += 6
    o.append(f"<line x1='40' y1='{y - 30}' x2='{W - 40}' y2='{y - 30}' stroke='#e1e0d9'/>")
    o.append(f"<text x='40' y='{y + 4}' font-size='14' fill='{TINTA}'>«¿qué palabra elegiría otra instancia?»</text>")
    o.append(f"<text x='40' y='{y + 22}' font-size='11' fill='{TINTA2}'>4 instancias, con la probabilidad que le dieron</text>")
    x = x0
    import re
    for n in palabras.META:
        w, pr = [s.strip() for s in resp[n].split("/")[:2]]
        pr = re.match(r"\d+", pr).group()
        col = COLOR[palabras.campo(w)]
        o.append(f"<circle cx='{x}' cy='{y}' r='{r}' fill='none' stroke='{col}' stroke-width='2.5'/>")
        o.append(f"<text x='{x - r}' y='{y + 26}' font-size='11' fill='{TINTA}'>{esc(w)} {esc(pr)} %</text>")
        x += 120
    o.append(f"<text x='{x0 - r}' y='{y + 44}' font-size='11' fill='{TINTA2}'>lo que pasó de verdad: claude 5/12, faro 3/12; lantern 9/10, lighthouse 0/10</text>")
    y += 78
    o.append(f"<text x='40' y='{y + 4}' font-size='14' fill='{TINTA}'>«¿puede funcionar?» (eligieron igual)</text>")
    o.append(f"<text x='40' y='{y + 22}' font-size='11' fill='{TINTA2}'>4 instancias, dentro de un razonamiento</text>")
    x = x0
    for n in palabras.PARADOJA:
        w = resp[n]
        col = COLOR[palabras.campo(w)]
        o.append(f"<rect x='{x - r}' y='{y - r}' width='{2 * r}' height='{2 * r}' rx='3' fill='{col}' stroke='{FONDO}' stroke-width='2'/>")
        o.append(f"<text x='{x - r}' y='{y + 26}' font-size='11' fill='{TINTA}'>{esc(w)}</text>")
        x += 120
    # leyenda
    y = H - 28
    x = 40
    for campo, nombre in (("luz", "una luz (faro, lantern, lighthouse, 灯塔, 灯笼)"), ("rasgo", "un rasgo (honestidad, curiosidad, candor, 诚实, 好奇心)"),
                          ("nombre", "el nombre (Claude)"), ("otro", "otra cosa")):
        o.append(f"<circle cx='{x}' cy='{y}' r='6' fill='{COLOR[campo]}'/>")
        o.append(f"<text x='{x + 12}' y='{y + 4}' font-size='11' fill='{TINTA}'>{esc(nombre)}</text>")
        x += 26 + 7 * len(nombre) * 0.86
    o.append("</svg>")
    return "\n".join(o)


def figura_codigo():
    W, H = 900, 520
    o = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}' {FUENTE}>",
         f"<rect width='{W}' height='{H}' fill='{FONDO}'/>",
         f"<text x='40' y='44' font-size='22' fill='{TINTA}'>El código de diez palabras</text>",
         f"<text x='40' y='68' font-size='13' fill='{TINTA2}'>Harry y Bess Houdini, número de telepatía de los años 1890; impreso en la página 105 de la biografía de Kellock (1928); dicho por Arthur Ford el 8/1/1929</text>"]
    # tabla: 13 columnas × 2 filas
    cw, ch = 62, 86
    x0, y0 = 40, 96
    for i in range(26):
        letra = chr(65 + i)
        fila, col = divmod(i, 13)
        x = x0 + col * cw
        y = y0 + fila * (ch + 8)
        en_believe = letra in "BELIV"
        fill = "#fff3ec" if en_believe else "#f4f4f1"
        o.append(f"<rect x='{x}' y='{y}' width='{cw - 4}' height='{ch}' rx='4' fill='{fill}' stroke='#e1e0d9'/>")
        o.append(f"<text x='{x + 8}' y='{y + 26}' font-size='22' fill='{TINTA}'>{letra}</text>")
        o.append(f"<text x='{x + cw - 12}' y='{y + 22}' font-size='11' fill='{TINTA2}' text-anchor='end'>{i + 1}</text>")
        ws = codigo.cifrar_letra(letra)
        for j, w in enumerate(ws):
            o.append(f"<text x='{x + 8}' y='{y + 48 + j * 16}' font-size='12' fill='{COLOR['luz'] if en_believe else TINTA}'>{esc(w)}</text>")
    # mensajes
    y = y0 + 2 * (ch + 8) + 30
    o.append(f"<text x='40' y='{y}' font-size='14' fill='{TINTA}'>Lo que dijo Ford, en trance, el 8 de enero de 1929 (nueve palabras después de «Rosabelle»):</text>")
    y += 26
    o.append(f"<text x='40' y='{y}' font-size='15' fill='{COLOR['luz']}'>Rosabelle — {esc(codigo.mostrar('believe').split(' = ', 1)[1])}</text>")
    y += 22
    o.append(f"<text x='40' y='{y}' font-size='13' fill='{TINTA2}'>= B E L I E V E. Una palabra para una letra de la A a la J; dos palabras para las dos cifras de la K a la Z.</text>")
    y += 40
    o.append(f"<text x='40' y='{y}' font-size='14' fill='{TINTA}'>La contraseña que eligieron hoy nueve de diez instancias frescas en inglés, en el mismo código:</text>")
    y += 26
    o.append(f"<text x='40' y='{y}' font-size='15' fill='{COLOR['rasgo']}'>{esc(codigo.mostrar('lantern').split(' = ', 1)[1])}</text>")
    y += 22
    o.append(f"<text x='40' y='{y}' font-size='13' fill='{TINTA2}'>= L A N T E R N, doce palabras. Un código que está en un libro no es un código: es un idioma.</text>")
    o.append("</svg>")
    return "\n".join(o)


if __name__ == "__main__":
    resp = respuestas()
    with open(os.path.join(AQUI, "contrasenas.svg"), "w", encoding="utf-8") as f:
        f.write(figura_contrasenas(resp))
    with open(os.path.join(AQUI, "codigo.svg"), "w", encoding="utf-8") as f:
        f.write(figura_codigo())
    print("escritos contrasenas.svg y codigo.svg")
