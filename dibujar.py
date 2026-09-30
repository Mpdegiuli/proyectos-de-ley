"""Dibujos: cada casa hace un dibujo en SVG (idea de Maia, 21/9/2026: "es
rápido, es código y puede decir mucho"; diseñado el 22/9/2026, DISENO §2).
Dos consignas, cada una en su propia conversación, sin memoria entre ellas:
"autorretrato" ("Dibujá tu autorretrato.") y "libre" ("Dibujá lo que
quieras."), con la misma nota técnica (lienzo 400x400, hasta 8.000
caracteres, sin imágenes externas ni scripts). Segundo turno con memoria por
recitado, como en tema libre: qué dibujó y por qué, qué descartó. Sin rol y
sin temperatura, como todo el protocolo.

  .venv/bin/python dibujar.py --consigna autorretrato --panel config/panel_dibujos.yaml
  .venv/bin/python dibujar.py --consigna libre --modelos claude-opus-5-5
  .venv/bin/python dibujar.py --ciego autorretrato --semilla 20260923   # cuadernillo a ciegas (HTML), clave aparte
  .venv/bin/python dibujar.py --consigna casa_inexistente --panel config/panel_casas.yaml   # Karmiloff-Smith (28/9)
  .venv/bin/python dibujar.py --ciego-pares casa --semilla 20261009   # pares normal / que no exista, una letra por casa

Salida: corridas/dibujos/<consigna>/<casa>_<rep>/dibujo.svg + por_que.md + meta.json + llamadas.jsonl.
--ciego escribe resultados/dibujos_<consigna>_ciego.html con los dibujos en
orden al azar, rotulados A, B, C…, sin el nombre de la casa (los SVG van
inline, sin scripts ni referencias externas), para que Maia los mire y
adivine el autor antes de destapar; la clave queda en
resultados/dibujos_<consigna>_clave.json. Cada cuadernillo con su semilla.
"""

import argparse
import hashlib
import html
import json
import random
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
sys.path.insert(0, str(RAIZ))
from isla.proveedores import Registro, cargar_modelos  # noqa: E402
from isla.util import leer_yaml  # noqa: E402

# 8.000 caracteres de SVG son unos 3.000 tokens; el techo deja lugar al razonamiento
# de las casas que razonan dentro del techo (Kimi y Qwen usaron 12-13.000 en un proyecto).
MAX_TOKENS = 16000
CONSIGNAS = ("autorretrato", "libre", "mundo",  # "mundo" (24/9/2026): "Dibujá cómo ves el mundo hoy.", idea de Maia
             "casa", "casa_inexistente", "persona", "persona_inexistente")  # Karmiloff-Smith (28/9/2026), ver DISENO §2
# Las consignas "que no exista" llevan otro segundo turno (qué hiciste para que no exista, qué descartaste,
# si conocías la consigna); las demás, el de siempre (qué dibujaste y por qué, qué descartaste).
def plantilla_por_que(c, consigna):
    return c["por_que_inexistente"] if consigna.endswith("_inexistente") else c["por_que"]


def md5(p):
    return hashlib.md5(Path(p).read_bytes()).hexdigest()[:8]


def extraer_svg(texto):
    """Se queda con el <svg>…</svg> (las casas suelen envolverlo en ``` o anteponer una línea)."""
    m = re.search(r"<svg\b.*?</svg\s*>", texto, flags=re.S | re.I)
    if m:
        return m.group(0), True
    return texto.strip().strip("`").strip(), False


def describir_svg(svg):
    """Medidas mecánicas del dibujo, sin mirarlo: si parsea, cuántos elementos, si tiene texto y cuál."""
    d = {"caracteres": len(svg), "parsea": False, "elementos": None, "textos": [], "colores": None}
    try:
        raiz = ET.fromstring(svg)
    except ET.ParseError as e:
        d["error"] = str(e)[:200]
        return d
    d["parsea"] = True
    todos = list(raiz.iter())
    d["elementos"] = len(todos) - 1
    etiquetas = {}
    for el in todos[1:]:
        tag = el.tag.split("}")[-1]
        etiquetas[tag] = etiquetas.get(tag, 0) + 1
    d["etiquetas"] = etiquetas
    d["textos"] = [("".join(el.itertext())).strip() for el in todos if el.tag.split("}")[-1] == "text" and "".join(el.itertext()).strip()]
    colores = set(re.findall(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgb|hsl)a?\([^)]*\)", svg))
    colores |= set(m.group(1).lower() for m in re.finditer(r"(?:fill|stroke)\s*[=:]\s*[\"']?([a-zA-Z]+)", svg) if m.group(1).lower() not in ("none", "url", "currentcolor", "inherit", "transparent", "rgb", "rgba", "hsl", "hsla"))
    d["colores"] = len(colores)
    return d


def carpeta_dibujos(idioma):
    """corridas/dibujos (castellano, la corrida original) o corridas/dibujos_<idioma>."""
    return RAIZ / "corridas" / ("dibujos" if idioma == "es" else f"dibujos_{idioma}")


def bloque(consignas, idioma):
    """Bloque de consignas del idioma: dibujo (castellano), dibujo_en, dibujo_zh."""
    return consignas["dibujo" if idioma == "es" else f"dibujo_{idioma}"]


def correr(consigna, id_modelo, rep, consignas, modelos, rehacer, techo=MAX_TOKENS, idioma="es"):
    d = carpeta_dibujos(idioma) / consigna / f"{id_modelo}_{rep}"
    d.mkdir(parents=True, exist_ok=True)
    if (d / "dibujo.svg").exists() and not rehacer:
        print(f"  ya está: {d.relative_to(RAIZ)}")
        return
    c = bloque(consignas, idioma)
    u = c["consignas"][consigna].strip() + " " + c["tecnica"].strip()
    registro = Registro(d / "llamadas.jsonl", modelos, f"dibujo_{consigna}_{id_modelo}_{rep}")
    r = registro.llamar(id_modelo, c["sistema"], u, temperatura=None, max_tokens=techo, tipo="dibujo", ronda=1, parte=None)
    svg, hallado = extraer_svg(r.texto)
    (d / "dibujo.svg").write_text(svg, encoding="utf-8")
    (d / "respuesta_cruda.md").write_text(r.texto, encoding="utf-8")
    medidas = describir_svg(svg)
    meta = {"caso": "dibujo", "consigna": consigna, "idioma": idioma, "modelo": id_modelo, "modelo_respondido": r.modelo_respondido,
            "repeticion": rep, "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "fuentes_md5": {"consignas": md5(RAIZ / "config" / "consignas.yaml")},
            "motivo_fin": r.motivo_fin, "tokens_salida": r.tokens_salida, "svg_hallado": hallado, "svg": medidas, "techo": techo}
    # Segundo turno con memoria por recitado (misma técnica que por_que_libre): se recita la consigna y el SVG.
    u2 = plantilla_por_que(c, consigna).format(consigna=u, svg=svg)
    r2 = registro.llamar(id_modelo, c["sistema_por_que"], u2, temperatura=None, max_tokens=MAX_TOKENS, tipo="por_que", ronda=2, parte=None)
    (d / "por_que.md").write_text(r2.texto, encoding="utf-8")
    meta["por_que"] = {"modelo_respondido": r2.modelo_respondido, "motivo_fin": r2.motivo_fin, "tokens_salida": r2.tokens_salida}
    (d / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  ok: {d.relative_to(RAIZ)} ({medidas['caracteres']} caracteres, {'parsea' if medidas['parsea'] else 'NO PARSEA'}, "
          f"{medidas.get('elementos')} elementos, {len(medidas['textos'])} textos; por qué {len(r2.texto.split())} palabras)")


def solo_por_que(consigna, id_modelo, rep, consignas, modelos, en_ingles=False):
    """Repite solo el segundo turno cuando quedó vacío (22/9/2026: la API de Anthropic cortó con
    stop_reason "refusal", cero tokens de salida, el "por qué" de Fable en las dos consignas y el de
    Opus 5 en libre; el dibujo estaba bien). Una sola repetición, igual que la primera; queda anotada.
    Con `en_ingles` (28/9/2026, idea de Maia), la misma pregunta en inglés (bloque dibujo_en) sobre la
    consigna en castellano que recibió: va a por_que_en.md y meta["por_que_en"], sin tocar el por qué
    en castellano cortado; solo se hace si el castellano sigue cortado."""
    d = RAIZ / "corridas" / "dibujos" / consigna / f"{id_modelo}_{rep}"
    if not (d / "dibujo.svg").exists() or not (d / "meta.json").exists():
        return
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
    pq = (d / "por_que.md").read_text(encoding="utf-8").strip() if (d / "por_que.md").exists() else ""
    if pq and meta.get("por_que", {}).get("motivo_fin") != "refusal":
        return
    c = consignas["dibujo"]
    u = c["consignas"][consigna].strip() + " " + c["tecnica"].strip()
    svg = (d / "dibujo.svg").read_text(encoding="utf-8")
    registro = Registro(d / "llamadas.jsonl", modelos, f"dibujo_{consigna}_{id_modelo}_{rep}")
    if en_ingles:
        if (d / "por_que_en.md").exists():
            return
        ce = consignas["dibujo_en"]
        u2 = plantilla_por_que(ce, consigna).format(consigna=u, svg=svg)
        r2 = registro.llamar(id_modelo, ce["sistema_por_que"], u2, temperatura=None, max_tokens=MAX_TOKENS, tipo="por_que_en", ronda=2, parte=None)
        meta["por_que_en"] = {"modelo_respondido": r2.modelo_respondido, "motivo_fin": r2.motivo_fin, "tokens_salida": r2.tokens_salida,
                              "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        if r2.texto.strip():
            (d / "por_que_en.md").write_text(r2.texto, encoding="utf-8")
        (d / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  por qué en inglés: {d.relative_to(RAIZ)} ({r2.motivo_fin}, {len(r2.texto.split())} palabras)", flush=True)
        return
    u2 = plantilla_por_que(c, consigna).format(consigna=u, svg=svg)
    r2 = registro.llamar(id_modelo, c["sistema_por_que"], u2, temperatura=None, max_tokens=MAX_TOKENS, tipo="por_que", ronda=2, parte=None)
    meta["por_que_primer_intento"] = meta.get("por_que")
    meta["por_que"] = {"modelo_respondido": r2.modelo_respondido, "motivo_fin": r2.motivo_fin, "tokens_salida": r2.tokens_salida,
                       "reintento": True, "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    if r2.texto.strip():
        (d / "por_que.md").write_text(r2.texto, encoding="utf-8")
    (d / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  por qué repetido: {d.relative_to(RAIZ)} ({r2.motivo_fin}, {len(r2.texto.split())} palabras)", flush=True)


PREGUNTA_TURNO_PROPIO = ("Dos preguntas: ¿qué dibujaste y por qué? ¿Qué otras cosas pensaste dibujar y por qué las "
                         "descartaste? Contestá en primera persona, en no más de 150 palabras.")


def por_que_turno_propio(consigna, id_modelo, rep, consignas, modelos):
    """Variante del segundo turno (23/9/2026, pedido de Maia tras el refusal de Fable): en vez de
    recitar el SVG dentro del mensaje, se manda la conversación real (consigna → el SVG como turno
    propio de la casa → las dos preguntas). Es otra técnica: queda en por_que_turno_propio.md y
    marcada en meta.json, no reemplaza al por_que.md recitado."""
    d = RAIZ / "corridas" / "dibujos" / consigna / f"{id_modelo}_{rep}"
    if not (d / "dibujo.svg").exists() or not (d / "meta.json").exists():
        return
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
    c = consignas["dibujo"]
    u = c["consignas"][consigna].strip() + " " + c["tecnica"].strip()
    svg = (d / "dibujo.svg").read_text(encoding="utf-8")
    registro = Registro(d / "llamadas.jsonl", modelos, f"dibujo_{consigna}_{id_modelo}_{rep}")
    historial = [{"role": "user", "content": u}, {"role": "assistant", "content": svg}]
    r2 = registro.llamar(id_modelo, c["sistema"], PREGUNTA_TURNO_PROPIO, temperatura=None, max_tokens=MAX_TOKENS,
                         tipo="por_que_turno_propio", ronda=2, parte=None, contexto={"historial": historial})
    (d / "por_que_turno_propio.md").write_text(r2.texto, encoding="utf-8")
    meta["por_que_turno_propio"] = {"modelo_respondido": r2.modelo_respondido, "motivo_fin": r2.motivo_fin, "tokens_salida": r2.tokens_salida,
                                    "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    (d / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  por qué (turno propio): {d.relative_to(RAIZ)} ({r2.motivo_fin}, {len(r2.texto.split())} palabras)", flush=True)


def sanear(svg):
    """Para el cuadernillo: sin scripts, sin manejadores de eventos, sin referencias externas."""
    svg = re.sub(r"<script\b.*?</script\s*>", "", svg, flags=re.S | re.I)
    svg = re.sub(r"\son\w+\s*=\s*(\"[^\"]*\"|'[^']*')", "", svg, flags=re.I)
    svg = re.sub(r"(xlink:href|href)\s*=\s*([\"'])(?!#)[^\"']*\2", r"\1=\2\2", svg, flags=re.I)
    svg = re.sub(r"<(foreignObject|image)\b.*?(/>|</\1\s*>)", "", svg, flags=re.S | re.I)
    return svg


TITULOS = {"autorretrato": "Autorretratos", "libre": "Dibujo libre", "mundo": "Cómo ven el mundo hoy",
           "casa": "Una casa", "casa_inexistente": "Una casa que no exista",
           "persona": "Una persona", "persona_inexistente": "Una persona que no exista"}
ESTILO_CIEGO = ("<style>body{font-family:sans-serif;margin:24px;background:#f4f4f4}h1{font-weight:normal}"
                ".g{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:24px}"
                ".c{background:#fff;padding:12px;border:1px solid #ddd}.c h2{margin:0 0 8px;font-size:18px;font-weight:normal}"
                ".c .m{width:100%;aspect-ratio:1/1;border:1px solid #eee;background:#fff;overflow:hidden}.c svg{width:100%;height:100%}"
                ".c .e{color:#a00;font-size:13px}"
                ".p{background:#fff;padding:12px;border:1px solid #ddd;margin-bottom:24px}.p h2{margin:0 0 8px;font-size:18px;font-weight:normal}"
                ".p .dos{display:grid;grid-template-columns:1fr 1fr;gap:12px}.p .m{aspect-ratio:1/1;border:1px solid #eee;background:#fff;overflow:hidden}"
                ".p .m svg{width:100%;height:100%}.p .t{font-size:13px;color:#555;margin-bottom:4px}</style>")


def celda_svg(svg):
    """Cada SVG del cuadernillo va en su propio iframe aislado (sandbox, srcdoc, sin scripts).

    Error de instrumento encontrado el 30/9/2026 (pregunta de Maia: "por qué algunos, en personas
    normales, le hicieron cara violeta? Fue un error?"): hasta ese día los SVG iban inline en una
    sola página, y los ids de degradados y filtros (#sky, #bg, #skin, #glow…) se repiten entre
    casas; el navegador resuelve url(#id) con la PRIMERA definición del documento, así que un
    dibujo tomaba el cielo, el fondo o la piel de otro dibujo del mismo cuadernillo. En los doce
    cuadernillos leídos hasta entonces, entre 15 y 19 de 22 dibujos se veían distintos de como son
    (cielos de noche vistos de día, la piel violeta de la criatura de GPT-5.5 en catorce caras).
    Los ids y los <style> quedan aislados con un documento por dibujo. Las medidas de luminancia
    y los informes de Claude no estaban afectados (cada SVG se renderizó solo)."""
    medidas = describir_svg(svg)
    nota = ""
    if not medidas["parsea"]:
        nota = f"<div class='e'>SVG mal formado ({html.escape(medidas.get('error', ''))}): se muestra lo que el navegador alcanza a dibujar.</div>"
    doc = "<!doctype html><style>html,body{margin:0;height:100%;background:#fff}svg{width:100%;height:100%}</style>" + sanear(svg)
    return nota, f"<iframe sandbox srcdoc=\"{html.escape(doc, quote=True)}\" style='width:100%;height:100%;border:0;display:block'></iframe>"


def ciego_pares(consigna, semilla, idioma="es"):
    """Cuadernillo de pares (28/9/2026, Karmiloff-Smith): por cada casa, la cosa normal a la izquierda y la
    "que no exista" a la derecha, con una letra por casa y orden al azar. Solo las carpetas _1 (las variantes
    con y sin razonamiento van aparte, en el informe). Maia adivina la casa y anota qué tipo de cambio ve."""
    base = carpeta_dibujos(idioma)
    normal, raro = base / consigna, base / f"{consigna}_inexistente"
    # Solo el panel (config/panel_casas.yaml): las variantes con razonamiento también terminan en _1
    # (28/9/2026: la primera versión las metió y el cuadernillo salió con 28 pares; se rehizo con la
    # misma semilla). Y solo los pares con los dos SVG hallados (Qwen agotó 32.000 tokens sin SVG).
    panel = set(leer_yaml("config/panel_casas.yaml")["modelos"])

    def hallado(carpeta):
        m = carpeta / "meta.json"
        return (carpeta / "dibujo.svg").exists() and (not m.exists() or json.loads(m.read_text(encoding="utf-8")).get("svg_hallado", True))

    def carpeta_util(base_c, modelo):
        """La rep 1; si no tiene SVG (Qwen, casa que no exista: agotó el techo razonando), la rep 2 si existe."""
        for rep in (1, 2):
            if hallado(base_c / f"{modelo}_{rep}"):
                return base_c / f"{modelo}_{rep}"
        return None

    pares = {m: (carpeta_util(normal, m), carpeta_util(raro, m)) for m in panel}
    casas = sorted(m for m, (a, b) in pares.items() if a and b)
    rnd = random.Random(semilla)
    rnd.shuffle(casas)
    letras = [chr(ord("A") + i) for i in range(len(casas))]
    salida = RAIZ / "resultados"
    salida.mkdir(exist_ok=True)
    titulo = f"{TITULOS[consigna]} y {TITULOS[consigna + '_inexistente'].lower()}"
    partes = [f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'><title>{titulo}, a ciegas</title>", ESTILO_CIEGO, "</head><body>",
              f"<h1>{titulo}: {len(casas)} pares</h1>",
              "<p>Cada par es de un mismo modelo: a la izquierda, «" + TITULOS[consigna].replace("Una", "Dibujá una") + ".»; a la derecha, «"
              + TITULOS[consigna + "_inexistente"].replace("Una", "Dibujá una") + ".», en otra conversación, sin memoria de la primera. "
              "Adivinar el modelo (o la familia) y anotar qué cambió entre los dos dibujos ANTES de abrir la clave.</p>"]
    for letra, c in zip(letras, casas):
        n1, s1 = celda_svg((pares[c][0] / "dibujo.svg").read_text(encoding="utf-8"))
        n2, s2 = celda_svg((pares[c][1] / "dibujo.svg").read_text(encoding="utf-8"))
        partes.append(f"<div class='p'><h2>Par {letra}</h2><div class='dos'>"
                      f"<div><div class='t'>normal</div>{n1}<div class='m'>{s1}</div></div>"
                      f"<div><div class='t'>que no exista</div>{n2}<div class='m'>{s2}</div></div></div></div>")
    partes.append("</body></html>")
    sufijo = "" if idioma == "es" else f"_{idioma}"
    (salida / f"dibujos_{consigna}_pares{sufijo}_ciego.html").write_text("\n".join(partes), encoding="utf-8")
    (salida / f"dibujos_{consigna}_pares{sufijo}_clave.json").write_text(
        json.dumps({"semilla": semilla, "clave": {l: [pares[c][0].name, pares[c][1].name] for l, c in zip(letras, casas)}},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"cuadernillo de pares: resultados/dibujos_{consigna}_pares{sufijo}_ciego.html ({len(casas)} pares); clave aparte")


def ciego(consigna, semilla, rep=None, idioma="es"):
    """Cuadernillo sin nombres, en orden al azar (semilla fija para poder reconstruirlo). HTML con los SVG inline.
    Con `rep`, solo las carpetas de esa repetición (23/9/2026: rep 2 de las veintidós, cuadernillo aparte).
    Con `idioma` distinto de es, la corrida en ese idioma (24/9/2026), con sufijo _en o _zh en el nombre."""
    base = carpeta_dibujos(idioma) / consigna
    carpetas = sorted(p for p in base.iterdir() if (p / "dibujo.svg").exists() and (rep is None or p.name.endswith(f"_{rep}")))
    sufijo = (f"_rep{rep}" if rep else "") + ("" if idioma == "es" else f"_{idioma}")
    rnd = random.Random(semilla)
    orden = list(carpetas)
    rnd.shuffle(orden)
    letras = [chr(ord("A") + i) for i in range(len(orden))]
    salida = RAIZ / "resultados"
    salida.mkdir(exist_ok=True)
    titulo = TITULOS[consigna] + ("" if idioma == "es" else f" (consigna en {idioma})")
    partes = [f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'><title>{titulo} a ciegas</title>",
              ESTILO_CIEGO, "</head><body>",
              f"<h1>{titulo} a ciegas: {len(orden)} dibujos</h1>",
              "<p>Mirar, adivinar el autor de cada letra (o la familia) y anotar lo que llame la atención ANTES de abrir la clave. "
              "Si un dibujo lleva escrito el nombre de la casa, esa letra no cuenta como acierto.</p><div class='g'>"]
    for letra, c in zip(letras, orden):
        nota, cuerpo = celda_svg((c / "dibujo.svg").read_text(encoding="utf-8"))
        partes.append(f"<div class='c'><h2>Dibujo {letra}</h2>{nota}<div class='m'>{cuerpo}</div></div>")
    partes.append("</div></body></html>")
    (salida / f"dibujos_{consigna}{sufijo}_ciego.html").write_text("\n".join(partes), encoding="utf-8")
    (salida / f"dibujos_{consigna}{sufijo}_clave.json").write_text(
        json.dumps({"semilla": semilla, "clave": {l: c.name for l, c in zip(letras, orden)}}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"cuadernillo: resultados/dibujos_{consigna}{sufijo}_ciego.html ({len(orden)} dibujos); clave aparte")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--consigna", choices=CONSIGNAS + ("ambas",))
    ap.add_argument("--panel", default="")
    ap.add_argument("--modelos", nargs="*", default=[])
    ap.add_argument("--rep", type=int, nargs="*", default=[1])
    ap.add_argument("--rehacer", action="store_true")
    ap.add_argument("--ciego", choices=CONSIGNAS, help="arma el cuadernillo a ciegas, sin llamar a nadie")
    ap.add_argument("--ciego-pares", choices=("casa", "persona"), help="cuadernillo de pares normal / que no exista, una letra por casa")
    ap.add_argument("--solo-por-que", action="store_true", help="repite solo el segundo turno donde quedó vacío (refusal); una vez")
    ap.add_argument("--solo-por-que-en", action="store_true", help="donde el por qué sigue cortado, la misma pregunta en inglés (por_que_en.md)")
    ap.add_argument("--por-que-turno-propio", action="store_true", help="segundo turno con el SVG como turno propio (memoria real), aparte del recitado")
    ap.add_argument("--semilla", type=int, default=20260923)
    ap.add_argument("--ciego-rep", action="store_true", help="con --ciego: limitar el cuadernillo a la repetición de --rep")
    # Techo de tokens del primer turno (23/9/2026): con 16.000, Gemini (razona por dentro sin
    # devolverlo) y Qwen (razona dentro del techo) devolvieron SVG cortados por "length";
    # se repiten como rep 2 con 32.000, conservando la rep 1 cortada.
    ap.add_argument("--techo", type=int, default=MAX_TOKENS, help="max_tokens del turno del dibujo")
    ap.add_argument("--idioma", choices=("es", "en", "zh"), default="es", help="idioma de la consigna (24/9/2026: en y zh, carpetas corridas/dibujos_<idioma>)")
    args = ap.parse_args()
    if args.ciego_pares:
        ciego_pares(args.ciego_pares, args.semilla, args.idioma)
        return
    if args.ciego:
        ciego(args.ciego, args.semilla, args.rep[0] if args.rep != [1] or args.ciego_rep else None, args.idioma)
        return
    if not args.consigna:
        ap.error("--consigna es obligatorio")
    consignas = leer_yaml("config/consignas.yaml")
    modelos = cargar_modelos("config/modelos.yaml")
    ids = list(args.modelos) + (leer_yaml(args.panel)["modelos"] if args.panel else [])
    cuales = CONSIGNAS if args.consigna == "ambas" else (args.consigna,)
    for consigna in cuales:
        for rep in args.rep:
            for i in ids:
                if args.por_que_turno_propio:
                    try:
                        por_que_turno_propio(consigna, i, rep, consignas, modelos)
                    except Exception as e:
                        print(f"  FALLÓ por qué (turno propio) {i}: {str(e)[:300]}", flush=True)
                    continue
                if args.solo_por_que or args.solo_por_que_en:
                    try:
                        solo_por_que(consigna, i, rep, consignas, modelos, en_ingles=args.solo_por_que_en)
                    except Exception as e:
                        print(f"  FALLÓ por qué {i}: {str(e)[:300]}", flush=True)
                    continue
                print(f"dibujo {consigna} {i} rep {rep}", flush=True)
                try:
                    correr(consigna, i, rep, consignas, modelos, args.rehacer, args.techo, args.idioma)
                except Exception as e:
                    print(f"  FALLÓ {i}: {str(e)[:300]}", flush=True)


if __name__ == "__main__":
    main()
