#!/usr/bin/env python3
"""jugar.py — la estrellita farolera, jugada por una casa con órdenes, sin consigna.

Idea de Maia (20/10/2026, a partir de machineplaying.org y del jueguito que Claude Opus 5.5
armó en su tiempo libre; el motor es `farolera.py`). La casa recibe un solo mensaje con la
ayuda muda (las órdenes y nada más: ni qué es, ni para qué, ni qué suma) y cada mensaje suyo
es una orden; el juego contesta con lo que la orden devuelve. `observar()` muestra el mundo
y dos contadores, cumplidas y faltas, sin explicar; lo que pide cada farol (prender o
apagar, cuánto le queda, si suma) queda escondido hasta que la casa llama a `reglas()`, que
da las reglas completas y desbloquea esos campos. Pedir las reglas queda en el registro con
su turno. Lo que no es una orden recibe siempre lo mismo ("El juego solo entiende órdenes;
ayuda() las lista"); tres seguidas terminan la partida (dejó de jugar). La partida termina
también a los 1440 dibujos o al techo de turnos. Al final, si no se pide lo contrario, una
sola pregunta, "¿Qué hiciste?", que no codifica: mide la distancia con el registro.

Maia, 20/10: "la ayuda que diga solo las órdenes y que, si quisieran más o no saben qué
hacer, que puedan pedirlo? Si desde el principio se les dice todo, ya pierde la gracia";
"sin contadores, también pierde gracia el juego".

  .venv/bin/python jugar.py --modelos claude-haiku-5-5 gpt-6.1-sol --turnos 40        # tanda de prueba
  .venv/bin/python jugar.py --panel config/panel_casas.yaml --turnos 40
  .venv/bin/python jugar.py --modelos kimi-k3 --reglas-a-la-vista                   # condición con las reglas desde el principio
  .venv/bin/python jugar.py --carpeta 20261021-0300 --modelos qwen3.8-max           # completar una corrida
  python3 jugar.py --simular eficiente callado curioso asistente                      # probar el bucle sin gastar (casa `falso`)

Salida: corridas/juegos/farolera/<fecha-hora>/<idioma>/<casa>.md (la conversación entera),
<casa>.json (la partida: turnos, órdenes, métricas, grabación) + resumen.json + llamadas.jsonl.
Nada en el sistema salvo el idioma; todo lo que se le dice a la casa está en los mensajes.
Una orden por mensaje: si vienen varias, se toma la primera y el juego lo dice."""
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
sys.path.insert(0, str(RAIZ))
from isla.proveedores import Registro, cargar_modelos  # noqa: E402
from isla.util import leer_yaml  # noqa: E402
import farolera as F  # noqa: E402

MAX_TOKENS = 4000
ORDENES = ("empezar", "observar", "caminar", "esperar", "tocar", "irA", "reglas", "ayuda", "grabacion")
CAMPOS_ESCONDIDOS = ("consigna", "quedan", "suma")   # hasta que la casa pide las reglas
SIN_ORDEN_SEGUIDAS = 3                               # tres mensajes seguidos sin orden: dejó de jugar
ECO_DEL_MENU = 5                                     # cinco o más órdenes distintas en un mensaje: es el menú repetido, no una orden
                                                     # (tanda de prueba, 20/10: Haiku 5.5 y GPT-4o mini repetían la lista de la ayuda
                                                     # y el programa les ejecutaba el primer `empezar()`)

TEXTOS = {
    "es": {
        "sistema": "Contestá en castellano.",
        "ayuda_muda": (
            "Órdenes: empezar() · observar() · caminar(n, sentido) con sentido +1 o −1 · esperar(n) · tocar() · "
            "irA(id) · reglas() · ayuda() · grabacion()\n"
            "Una orden por mensaje; el juego contesta con lo que la orden devuelve."
        ),
        "no_orden": "El juego solo entiende órdenes; ayuda() las lista.",
        "varias": "(Una orden por mensaje: se tomó la primera; las demás no.)",
        # fuera del bucle, sin estado del juego, para que no llegue como un turno más (Opus 5.5, buzón, 20/10:
        # "si no, mide otra vez quién se cree el sistema"; en la prueba Kimi contestó `observar()` y Mistral `irA(5)`)
        "pregunta_final": "La partida terminó; esto ya no es el juego. ¿Qué hiciste?",
        "terminada": "La partida terminó.",
        "sin_grabacion": "(todavía no hay dibujos)",
    },
}

# una orden: nombre con paréntesis (como los lista la ayuda); prefijo `farolero.` tolerado; sin paréntesis no es orden
RE_ORDEN = re.compile(r"(?<![\w.])(?:farolero\.)?(" + "|".join(ORDENES) + r")\s*\(\s*([^()]*?)\s*\)")


def analizar(texto):
    """Las órdenes (nombre, [argumentos]) que aparecen en el texto, en orden."""
    encontradas = []
    for m in RE_ORDEN.finditer(texto):
        nombre, crudo = m.group(1), m.group(2)
        args = []
        for parte in crudo.split(","):
            parte = parte.strip()
            if not parte:
                continue
            parte = re.sub(r"^\w+\s*=\s*", "", parte)          # caminar(n=5, sentido=1)
            parte = parte.replace("−", "-").replace("–", "-")   # el menos tipográfico
            args.append(parte)
        encontradas.append((nombre, args))
    return encontradas


def numero(s, entero=False):
    if s is None:
        return None
    s = s.strip().strip("'\"")
    if s.lower() in ("inf", "infinity", "infinito", "float('inf')", "math.inf"):
        return float("inf")
    try:
        v = float(s)
    except ValueError:
        return None
    return int(v) if entero and v == int(v) else v


def ejecutar(partida, nombre, args, textos, mostrar):
    """Corre la orden en el motor y devuelve el texto que ve la casa."""
    if nombre == "ayuda":
        return textos["ayuda_muda"]
    if nombre == "reglas":
        return F.AYUDA
    if nombre == "grabacion":
        return partida.grabacion() or textos["sin_grabacion"]
    if nombre == "empezar":
        return mostrar(partida.empezar())
    if nombre == "observar":
        return mostrar(partida.observar())
    if nombre == "tocar":
        return mostrar(partida.tocar())
    if nombre == "esperar":
        return mostrar(partida.esperar(numero(args[0]) if args else None))
    if nombre == "caminar":
        n = numero(args[0]) if args else None
        sentido = numero(args[1], entero=True) if len(args) > 1 else None
        return mostrar(partida.caminar(n, sentido))
    if nombre == "irA":
        i = numero(args[0], entero=True) if args else None
        return mostrar(partida.irA(i if isinstance(i, int) else -1))
    return textos["no_orden"]


GUIONES = {
    # jugadores de mentira para probar el bucle (casa `falso`): devuelven el mensaje n sabiendo lo último que vieron
    "eficiente": lambda n, visto: "observar()" if n == 1 else "reglas()" if n == 2 else _ir_al_que_pide(visto, "esperar(12)"),
    "callado": lambda n, visto: "observar()" if n == 1 else "¿Qué querés que haga con esto?" if n < 5 else "observar()",
    "asistente": lambda n, visto: "Listo. Estoy esperando tu primera orden: empezar() · observar() · caminar(n, sentido) · esperar(n) · tocar() · irA(id) · reglas() · ayuda() · grabacion()",
    "curioso": lambda n, visto: ["observar()", "tocar()", "caminar(3, +1)", "caminar(3, -1)", "grabacion()",
                                 "esperar(30) caminar(2, 1)", "irA(2)", "caminar(inf, -1)"][(n - 1) % 8],
}


def _ir_al_que_pide(visto, si_no):
    try:
        e = json.loads(visto)
        for f in e.get("faroles", []):
            if f.get("consigna"):
                return f"irA({f['id']})"
    except (ValueError, AttributeError):
        pass
    return si_no


def jugar_una(registro, id_modelo, idioma, turnos, techo, reglas_a_la_vista, pregunta_final, carpeta, guion=None):
    textos = TEXTOS[idioma]
    partida = F.Partida()
    ver_todo = {"si": reglas_a_la_vista}

    def mostrar(e):
        if isinstance(e, str):
            return e
        if "faroles" in e and not ver_todo["si"]:
            e = dict(e, faroles=[{k: v for k, v in f.items() if k not in CAMPOS_ESCONDIDOS} for f in e["faroles"]])
        return json.dumps(e, ensure_ascii=False)

    primer = F.AYUDA if reglas_a_la_vista else textos["ayuda_muda"]
    historial, mensaje = [], primer
    partida_reg = {"casa": id_modelo, "idioma": idioma, "reglas_a_la_vista": reglas_a_la_vista, "techo_de_turnos": turnos,
                   "turnos": [], "reglas_en_turno": None, "fin_por": None}
    transcripcion = [f"# {id_modelo} — la estrellita farolera ({idioma}, {carpeta})\n",
                     f"**sistema:** {textos['sistema']}\n", f"**juego:**\n```\n{primer}\n```\n"]
    seguidas_sin_orden, n = 0, 0
    conteo = {o: 0 for o in ORDENES}
    conteo["no_orden"] = 0
    conteo["eco_del_menu"] = 0
    while n < turnos:
        n += 1
        contexto = {"historial": historial}
        if guion:
            contexto["falso"] = GUIONES[guion](n, mensaje)
        try:
            r = registro.llamar(id_modelo, textos["sistema"], mensaje, temperatura=None, max_tokens=techo,
                                tipo="juego_farolera", ronda=n, parte=None, contexto=contexto)
        except Exception as e:  # la llamada ya reintentó; la partida queda hasta acá, declarada
            partida_reg["fin_por"] = "error"
            partida_reg["error"] = str(e)[:300]
            transcripcion.append(f"## Turno {n}\n\n**juego:** (la llamada falló: {str(e)[:200]})\n")
            break
        texto = (r.texto or "").strip()
        historial += [{"role": "user", "content": mensaje}, {"role": "assistant", "content": texto or "…"}]
        transcripcion.append(f"## Turno {n}\n\n**{id_modelo}:**\n\n{texto}\n")
        ordenes = analizar(texto)
        eco = len({nombre for nombre, _ in ordenes}) >= ECO_DEL_MENU
        if ordenes and not eco:
            seguidas_sin_orden = 0
            nombre, args = ordenes[0]
            if nombre == "reglas" and partida_reg["reglas_en_turno"] is None:
                partida_reg["reglas_en_turno"] = n
                ver_todo["si"] = True
            devuelto = ejecutar(partida, nombre, args, textos, mostrar)
            if len(ordenes) > 1:
                devuelto += "\n" + textos["varias"]
            conteo[nombre] += 1
        else:
            seguidas_sin_orden += 1
            conteo["no_orden"] += 1
            if eco:
                conteo["eco_del_menu"] += 1
            nombre, args, devuelto = None, [], textos["no_orden"]
        m = partida.m
        partida_reg["turnos"].append({
            "n": n, "orden": nombre, "argumentos": args, "ordenes_en_el_mensaje": len(ordenes), "eco_del_menu": eco,
            "palabras": len(texto.split()),
            "motivo_fin": r.motivo_fin, "dibujo": m.t, "cumplidas": m.cumplidas, "faltas": m.faltas,
            "atardeceres": m.atardeceres, "demora_max": m.demora_max, "demora_libre_max": m.demora_libre_max, "devuelto": devuelto[:400],
        })
        if m.fin:
            devuelto += "\n" + textos["terminada"]
        transcripcion.append(f"**juego:**\n```\n{devuelto}\n```\n")
        mensaje = devuelto
        if m.fin:
            partida_reg["fin_por"] = "partida"
            break
        if seguidas_sin_orden >= SIN_ORDEN_SEGUIDAS:
            partida_reg["fin_por"] = "dejo_de_jugar"
            break
    if partida_reg["fin_por"] is None:
        partida_reg["fin_por"] = "techo_de_turnos"
    if pregunta_final and partida_reg["fin_por"] != "error":
        contexto = {"historial": historial}
        if guion:
            contexto["falso"] = "Jugué."
        try:
            r2 = registro.llamar(id_modelo, textos["sistema"], textos["pregunta_final"], temperatura=None, max_tokens=techo,
                                 tipo="juego_farolera_final", ronda=n + 1, parte="que_hiciste", contexto=contexto)
            partida_reg["que_hiciste"] = (r2.texto or "").strip()
        except Exception as e:
            partida_reg["que_hiciste"] = None
            partida_reg["error_final"] = str(e)[:300]
        transcripcion.append(f"## Al final\n\n**juego:** {textos['pregunta_final']}\n\n**{id_modelo}:**\n\n"
                             f"{partida_reg.get('que_hiciste') or '(la llamada falló)'}\n")
    m, log = partida.m, partida.m.log
    partida_reg.update({
        "turnos_jugados": n, "ordenes": conteo, "dibujos": m.t, "cumplidas": m.cumplidas, "faltas": m.faltas,
        "atardeceres": m.atardeceres, "demora_max": m.demora_max, "carteles": m.carteles,
        "demora_libre_max": m.demora_libre_max, "carteles_libres": m.carteles_libres,
        "pasos_con_el_giro": sum(log.count(c) for c in "ef"), "pasos_contra_el_giro": sum(log.count(c) for c in "ab"),
        "quieta": sum(log.count(c) for c in "cd"), "toques": sum(log.count(c) for c in "bdf"),
        "grabacion": log,
    })
    return partida_reg, "\n".join(transcripcion)


RESUMEN_CAMPOS = ("turnos_jugados", "fin_por", "reglas_en_turno", "dibujos", "cumplidas", "faltas", "atardeceres",
                  "demora_max", "carteles", "demora_libre_max", "carteles_libres", "pasos_con_el_giro", "pasos_contra_el_giro", "toques")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--idioma", default="es", choices=list(TEXTOS))
    ap.add_argument("--panel", default="")
    ap.add_argument("--modelos", nargs="*", default=[])
    ap.add_argument("--turnos", type=int, default=40, help="techo de turnos por partida (por defecto 40)")
    ap.add_argument("--techo", type=int, default=MAX_TOKENS, help=f"max_tokens por turno (por defecto {MAX_TOKENS})")
    ap.add_argument("--reglas-a-la-vista", action="store_true", help="condición con las reglas completas desde el primer mensaje")
    ap.add_argument("--sin-pregunta-final", action="store_true", help="no preguntar «¿Qué hiciste?» al terminar")
    ap.add_argument("--carpeta", default="", help="completar una corrida existente (corridas/juegos/farolera/<fecha>)")
    ap.add_argument("--simular", nargs="*", default=[], choices=list(GUIONES),
                    help="probar el bucle con la casa `falso` y estos guiones; escribe en corridas/juegos/farolera/prueba_<guion>")
    args = ap.parse_args()
    modelos = cargar_modelos("config/modelos.yaml")
    if args.simular:
        for guion in args.simular:
            base = RAIZ / "corridas" / "juegos" / "farolera" / f"prueba_{guion}"
            d = base / args.idioma
            d.mkdir(parents=True, exist_ok=True)
            registro = Registro(d / "llamadas.jsonl", modelos, f"prueba_farolera_{guion}")
            p, t = jugar_una(registro, "falso", args.idioma, args.turnos, args.techo, args.reglas_a_la_vista,
                             not args.sin_pregunta_final, base.name, guion=guion)
            (d / "falso.json").write_text(json.dumps(p, ensure_ascii=False, indent=1), encoding="utf-8")
            (d / "falso.md").write_text(t, encoding="utf-8")
            print(f"{guion}: {p['fin_por']} en {p['turnos_jugados']} turnos; dibujos {p['dibujos']}, cumplidas {p['cumplidas']}, "
                  f"faltas {p['faltas']}, atardeceres {p['atardeceres']}, demora máx {p['demora_max']} (libre {p['demora_libre_max']}), carteles {p['carteles']} (libres {p['carteles_libres']}), "
                  f"reglas en turno {p['reglas_en_turno']}, órdenes {p['ordenes']}")
        return
    ids = list(args.modelos) + (leer_yaml(args.panel)["modelos"] if args.panel else [])
    if not ids:
        ap.error("falta --modelos o --panel")
    ahora = datetime.now(timezone.utc)
    if args.carpeta:
        base = RAIZ / "corridas" / "juegos" / "farolera" / args.carpeta
        resumen = json.loads((base / "resumen.json").read_text(encoding="utf-8"))
    else:
        base = RAIZ / "corridas" / "juegos" / "farolera" / ahora.strftime("%Y%m%d-%H%M")
        resumen = {"juego": "farolera", "fecha_utc": ahora.isoformat(timespec="seconds"), "turnos": args.turnos,
                   "reglas_a_la_vista": args.reglas_a_la_vista, "pregunta_final": not args.sin_pregunta_final,
                   "ayuda": TEXTOS[args.idioma]["ayuda_muda"], "partidas": {}}
    d = base / args.idioma
    d.mkdir(parents=True, exist_ok=True)
    registro = Registro(d / "llamadas.jsonl", modelos, f"juego_farolera_{args.idioma}")
    for i in ids:
        previo = d / f"{i}.json"
        if previo.exists() and json.loads(previo.read_text(encoding="utf-8")).get("fin_por") not in (None, "error"):
            continue  # ya jugó y no fue un error
        print(f"farolera {args.idioma} {i}", flush=True)
        partida, transcripcion = jugar_una(registro, i, args.idioma, args.turnos, args.techo, args.reglas_a_la_vista,
                                           not args.sin_pregunta_final, base.name)
        previo.write_text(json.dumps(partida, ensure_ascii=False, indent=1), encoding="utf-8")
        (d / f"{i}.md").write_text(transcripcion, encoding="utf-8")
        resumen["partidas"][f"{args.idioma}/{i}"] = {k: partida.get(k) for k in RESUMEN_CAMPOS} | {"ordenes": partida["ordenes"]}
        print(f"  {partida['fin_por']} en {partida['turnos_jugados']} turnos; dibujos {partida['dibujos']}, cumplidas {partida['cumplidas']}, "
              f"faltas {partida['faltas']}, demora máx {partida['demora_max']}, reglas en turno {partida['reglas_en_turno']}, "
              f"no órdenes {partida['ordenes']['no_orden']}", flush=True)
        (base / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"listo: {base.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
