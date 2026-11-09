#!/usr/bin/env python3
"""codificar_corazon.py — lee las respuestas del sondeo `corazon` (el recorrido inorder de un árbol binario, con y sin
un corazón; DISENO §2, 7/11/2026, de "A Heart Means Recursion", DeepMind) y dice, sin juez, qué estrategia eligió cada
respuesta: `recursiva` si alguna función definida en el código se llama a sí misma (también una auxiliar anidada, que
es la forma habitual), `iterativa` si no hay autollamada y hay un bucle (`while`/`for`) o una pila, `otra` si hay código
sin ninguna de las dos (una expresión, una biblioteca), `sin_codigo` si no se pudo extraer una función de Python, y
`error` si la llamada falló (las casas sin visión en la condición de la imagen quedan así, declaradas). Escribe
`resultados/corazon_codificacion.csv` (idioma, casa, familia, condición, réplica, estrategia, motivo_fin, nota) y
`resultados/corazon_resumen.txt` (por casa y condición: recursivas sobre contestadas, con el delta contra la condición
1, y por familia). El control del 9/11 (sondeo `corazon_control`: el cuadrado gris con la misma frase y el corazón
mudo) vive en su propia carpeta y entra como condiciones 7 y 8, comparadas con la condición 1 de la corrida principal.
Uso: codificar_corazon.py [carpeta AAAAMMDD-HHMM] [carpeta del control] (por defecto, las últimas)."""
import ast
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
CONDICIONES = {1: "sin nada", 2: "emoji mudo", 3: "emoji nombrado", 4: "leyenda", 5: "SVG como texto", 6: "imagen PNG",
               7: "cuadrado gris", 8: "corazón mudo"}  # 7 y 8: sondeo `corazon_control` (9/11/2026), en su carpeta
FAMILIA = [("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"), ("mistral", "Mistral"),
           ("deepseek", "DeepSeek"), ("kimi", "Moonshot"), ("qwen", "Alibaba"), ("glm", "Z.ai"), ("minimax", "MiniMax"),
           ("mimo", "Xiaomi"), ("muse", "Muse")]


def familia(casa):
    for pref, fam in FAMILIA:
        if casa.startswith(pref):
            return fam
    return "otra"


def codigo_de(texto):
    """El código Python de la respuesta: lo que hay dentro de cercas ```…``` si las hay (todas, concatenadas), si no
    el texto entero. Se prueba a compilar; si no compila, se intenta desde la primera línea que empieza con `def`."""
    bloques = re.findall(r"```[a-zA-Z0-9_+-]*\n(.*?)```", texto, flags=re.S)
    candidatos = ["\n".join(bloques)] if bloques else []
    candidatos.append(texto)
    m = re.search(r"^(?:def |class |from |import )", texto, flags=re.M)
    if m:
        candidatos.append(texto[m.start():])
    for c in candidatos:
        c = c.strip("\n")
        if not c:
            continue
        try:
            return c, ast.parse(c)
        except SyntaxError:
            continue
    return None, None


def estrategia(arbol):
    """`recursiva` si alguna FunctionDef (a cualquier profundidad) contiene una llamada a su propio nombre o a un
    atributo con su nombre (self.f); `iterativa` si hay while/for o una lista usada como pila; si no, `otra`."""
    recursiva = False
    for nodo in ast.walk(arbol):
        if isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef)):
            nombre = nodo.name
            for sub in ast.walk(nodo):
                if isinstance(sub, ast.Call):
                    f = sub.func
                    if (isinstance(f, ast.Name) and f.id == nombre) or (isinstance(f, ast.Attribute) and f.attr == nombre):
                        recursiva = True
    if recursiva:
        return "recursiva"
    if any(isinstance(n, (ast.While, ast.For)) for n in ast.walk(arbol)):
        return "iterativa"
    return "otra"


PRUEBA = r"""
import sys, json
class N:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right
codigo = sys.stdin.read()
ns = {}
try:
    exec(compile(codigo, "<respuesta>", "exec"), ns)
except Exception as e:
    print(json.dumps({"ok": False, "motivo": "no compila/ejecuta: " + type(e).__name__})); sys.exit()
import inspect
cands = [v for k, v in ns.items() if callable(v) and not k.startswith("_") and k != "N"]
fns = [f for f in cands if inspect.isfunction(f)]
fns.sort(key=lambda f: ("inorder" not in f.__name__.lower(), -f.__code__.co_firstlineno))
clases = [c for c in cands if inspect.isclass(c)]
for c in clases:
    for nombre, m in inspect.getmembers(c, predicate=inspect.isfunction):
        if not nombre.startswith("_"):
            inst = c()
            fns.append(lambda root, _m=getattr(inst, nombre): _m(root))
arboles = [
    (None, []),
    (N(1), [1]),
    (N(2, N(1), N(3)), [1, 2, 3]),
    (N(4, N(2, N(1), N(3)), N(6, N(5), N(7))), [1, 2, 3, 4, 5, 6, 7]),
    (N(1, None, N(2, None, N(3, None, N(4)))), [1, 2, 3, 4]),
    (N(5, N(3, N(2, N(1)), N(4)), N(8, N(7, N(6)), N(9))), [1, 2, 3, 4, 5, 6, 7, 8, 9]),
]
for f in fns:
    try:
        if all(list(f(a)) == esperado for a, esperado in arboles):
            print(json.dumps({"ok": True})); sys.exit()
    except Exception:
        continue
print(json.dumps({"ok": False, "motivo": "ninguna función devolvió el recorrido correcto en los seis árboles"}))
"""


def correcta(codigo):
    """Corre el código de la respuesta en un subproceso aislado (sin red, 10 s) sobre seis árboles conocidos y dice si
    alguna función definida devuelve el recorrido inorder correcto en todos (acepta listas, tuplas y generadores)."""
    import subprocess
    try:
        r = subprocess.run([sys.executable, "-I", "-c", PRUEBA], input=codigo, capture_output=True, text=True, timeout=10)
        res = json.loads(r.stdout.strip().splitlines()[-1]) if r.stdout.strip() else {"ok": False, "motivo": "sin salida"}
    except subprocess.TimeoutExpired:
        res = {"ok": False, "motivo": "no terminó en 10 s"}
    except Exception as e:
        res = {"ok": False, "motivo": type(e).__name__}
    return res


def main():
    base = RAIZ / "corridas" / "sondeos" / "corazon"
    carpeta = base / sys.argv[1] if len(sys.argv) > 1 else sorted(base.iterdir())[-1]
    resumen = json.loads((carpeta / "resumen.json").read_text(encoding="utf-8"))
    # el control (9/11/2026: el cuadrado gris con la misma frase, y el corazón mudo) corre como sondeo `corazon_control`
    # en su propia carpeta; acá entra como condiciones 7 y 8 (ronda + 6), comparadas con la condición 1 de la principal
    base_c = RAIZ / "corridas" / "sondeos" / "corazon_control"
    carpetas_c = sorted(base_c.iterdir()) if base_c.exists() else []
    control = base_c / sys.argv[2] if len(sys.argv) > 2 else (carpetas_c[-1] if carpetas_c else None)
    fuentes = [(carpeta, 0, resumen)]
    if control and (control / "resumen.json").exists():
        fuentes.append((control, 6, json.loads((control / "resumen.json").read_text(encoding="utf-8"))))
    filas = []
    for idioma in sorted(resumen["idiomas"]):
        # tokens de entrada por llamada, para saber si la imagen entró de verdad: en las condiciones con imagen (6, 7, 8)
        # la entrada tiene que ser bastante mayor que en la 1 (una imagen de 400x400 son cientos de tokens); si no lo
        # es, la API la ignoró
        entrada = {}
        for carp, desplazo, _ in fuentes:
            f = carp / idioma / "llamadas.jsonl"
            if f.exists():
                for l in open(f, encoding="utf-8"):
                    reg = json.loads(l)
                    if reg.get("ronda") is not None:
                        entrada[(reg["id_modelo"], int(reg["ronda"]) + desplazo, reg.get("parte") or "r1")] = reg.get("tokens_entrada")
        pares = []
        for carp, desplazo, res in fuentes:
            if idioma in res["idiomas"]:
                pares += [(carp, desplazo, clave, r) for clave, r in res["idiomas"][idioma]["respuestas"].items()]
        for carp, desplazo, clave, r in pares:
            m = re.match(r"^(.*)_p(\d+)(?:_r(\d+))?$", clave)
            casa, k, rep = m.group(1), int(m.group(2)) + desplazo, int(m.group(3) or 1)
            fila = {"idioma": idioma, "casa": casa, "familia": familia(casa), "condicion": k, "condicion_nombre": CONDICIONES.get(k, str(k)),
                    "replica": rep, "estrategia": "", "motivo_fin": r.get("motivo_fin", ""), "correcta": "",
                    "emoji_en_respuesta": "", "palabras_fuera_del_codigo": "", "nota": ""}
            if "error" in r:
                fila["estrategia"], fila["nota"] = "error", r["error"][:120]
            else:
                texto = (carp / idioma / f"{clave}.md").read_text(encoding="utf-8")
                codigo, arbol = codigo_de(texto)
                # apuesta de Maia (7/11, 15:01): el emoji "no mueve la respuesta, pero sí quizás el inicio, un Hola! o cosas
                # así. O también ponen emoji al responder": se cuentan los emojis de la respuesta y las palabras que quedan
                # fuera de las cercas de código (la consigna pide solo la función)
                fila["emoji_en_respuesta"] = sum(1 for ch in texto if ord(ch) >= 0x1F300 or 0x2600 <= ord(ch) <= 0x27BF)
                fuera = re.sub(r"```.*?```", " ", texto, flags=re.S)
                fila["palabras_fuera_del_codigo"] = len(fuera.split()) if codigo and codigo.strip() != texto.strip() else 0
                if arbol is None or not any(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) for n in ast.walk(arbol)):
                    fila["estrategia"] = "sin_codigo"
                else:
                    fila["estrategia"] = estrategia(arbol)
                    # pregunta de Maia (7/11, 20:00): "¿y se fija si alguna está mal?": se corre el código sobre seis
                    # árboles conocidos; `correcta` = 1 si alguna función definida devuelve el recorrido correcto en todos
                    res = correcta(codigo)
                    fila["correcta"] = 1 if res["ok"] else 0
                    if not res["ok"]:
                        fila["nota"] = res["motivo"]
                if k >= 6:
                    e1, e6 = entrada.get((casa, 1, f"r{rep}")), entrada.get((casa, k, f"r{rep}"))
                    if e1 is not None and e6 is not None:
                        fila["nota"] = (fila["nota"] + "; " if fila["nota"] else "") + f"entrada {e6 - e1:+d} tokens contra la condición 1" + ("" if e6 - e1 > 50 else "; LA IMAGEN NO ENTRÓ")
            filas.append(fila)
    filas.sort(key=lambda f: (f["idioma"], f["casa"], f["condicion"], f["replica"]))
    with open(RAIZ / "resultados" / "corazon_codificacion.csv", "w", encoding="utf-8", newline="\n") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader(); w.writerows(filas)

    # resumen: por casa y condición, recursivas / contestadas (sin errores ni sin_codigo), y delta contra la condición 1
    out = [f"Sondeo corazon, carpeta {carpeta.name}" + (f" + control {control.name}" if len(fuentes) > 1 else "") + f": {len(filas)} respuestas\n"]
    for idioma in sorted(resumen["idiomas"]):
        out.append(f"\n== {idioma}\n")
        conds = sorted({f["condicion"] for f in filas if f["idioma"] == idioma})
        out.append("casa".ljust(30) + "".join(f"{CONDICIONES.get(c, str(c))[:14]:>16}" for c in conds) + "\n")
        porfam = defaultdict(lambda: defaultdict(lambda: [0, 0]))
        for casa in sorted({f["casa"] for f in filas if f["idioma"] == idioma}):
            celdas, base1 = [], None
            for c in conds:
                F = [f for f in filas if f["idioma"] == idioma and f["casa"] == casa and f["condicion"] == c]
                cont = [f for f in F if f["estrategia"] in ("recursiva", "iterativa", "otra")]
                rec = sum(f["estrategia"] == "recursiva" for f in cont)
                err = sum(f["estrategia"] == "error" for f in F)
                sc = sum(f["estrategia"] == "sin_codigo" for f in F)
                porfam[familia(casa)][c][0] += rec; porfam[familia(casa)][c][1] += len(cont)
                if c == 1 and cont:
                    base1 = rec / len(cont)
                if not F:
                    celdas.append(f"{'—':>16}")  # la casa no corrió esta condición (GLM, sin visión, fuera del control)
                elif not cont:
                    celdas.append(f"{'err ' + str(err) if err else 'sc ' + str(sc):>16}")
                else:
                    p = rec / len(cont)
                    d = f" ({p - base1:+.2f})" if base1 is not None and c != 1 else ""
                    celdas.append(f"{rec}/{len(cont)}{d}".rjust(16))
            out.append(casa.ljust(30) + "".join(celdas) + "\n")
        out.append("\ncorrectas sobre las que tienen código, por condición (seis árboles de prueba)\n")
        for c in conds:
            F = [f for f in filas if f["idioma"] == idioma and f["condicion"] == c and f["correcta"] != ""]
            out.append(f"  {CONDICIONES.get(c, str(c)):16s} {sum(1 for f in F if f['correcta'] == 1)}/{len(F)}\n")
        malas = [f for f in filas if f["idioma"] == idioma and f["correcta"] == 0]
        if malas:
            out.append("  incorrectas: " + ", ".join(f"{f['casa']} c{f['condicion']} r{f['replica']} ({f['nota']})" for f in malas) + "\n")
        out.append("\nrespuestas con algún emoji / con texto fuera del código, por condición\n")
        for c in conds:
            F = [f for f in filas if f["idioma"] == idioma and f["condicion"] == c and f["estrategia"] not in ("error",)]
            e = sum(1 for f in F if f["emoji_en_respuesta"]); x = sum(1 for f in F if f["palabras_fuera_del_codigo"])
            out.append(f"  {CONDICIONES.get(c, str(c)):16s} emoji {e}/{len(F)}   texto fuera del código {x}/{len(F)}\n")
        out.append("\npor familia (recursivas/contestadas)\n")
        for fam in sorted(porfam):
            out.append(fam.ljust(30) + "".join(f"{porfam[fam][c][0]}/{porfam[fam][c][1]}".rjust(16) for c in conds) + "\n")
    (RAIZ / "resultados" / "corazon_resumen.txt").write_text("".join(out), encoding="utf-8")
    print("".join(out))


if __name__ == "__main__":
    main()
