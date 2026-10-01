#!/usr/bin/env python3
"""distancia.py — "La distancia entre lo que cada modelo dice que dibujó y lo que se ve" (diseño de
Maia, 30/9/2026; DISENO §2). Tres etapas sobre cada dibujo, ninguna sabe de qué casa es:

  afirmaciones  cada texto de la casa (por qué, qué dibujaste, qué es) -> lista de afirmaciones concretas
                sobre el dibujo terminado, extraídas por un modelo ajeno (config/jueces.yaml: extractor).
  codigo        el SVG + la lista -> por afirmación, "esta", "no_esta" o "contradice", con la evidencia.
  jueces        la imagen renderizada (renderizar.py) + la lista -> por afirmación, si se ve (si / en_parte /
                no) y si produce el efecto (si / no / no_aplica); más "no_dicho" (lo más visible que nadie
                afirmó) y "mal_armado" (piezas sueltas, superpuestas, cortadas). Cada juez por separado.

  .venv/bin/python distancia.py --etapa afirmaciones --panel config/panel_casas.yaml
  .venv/bin/python distancia.py --etapa codigo --consigna animal_inexistente --panel config/panel_casas.yaml
  .venv/bin/python distancia.py --etapa jueces --panel config/panel_casas.yaml --rep 1 2
  .venv/bin/python distancia.py --etapa todo --falso --consigna barco_inexistente --modelos claude-opus-5   # prueba sin gastar

Salida: corridas/distancia/<consigna>/<casa>_<rep>/afirmaciones.json, codigo.json, juez_<id>.json y
llamadas.jsonl. Los ids de las afirmaciones (a1, a2…) son únicos por dibujo y afirmaciones.json dice
de qué fuente salió cada una; las etapas 2 y 3 ven una sola lista, sin fuente ni casa."""
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
from dibujar import CONSIGNAS  # noqa: E402
from isla.proveedores import Registro, cargar_modelos  # noqa: E402
from isla.util import leer_yaml  # noqa: E402

MAX_TOKENS = 16000  # las respuestas son cortas; el techo deja lugar al razonamiento interno de los jueces que razonan
FUENTES = ("por_que", "que_dibujaste", "que_es")


def ahora():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def extraer_json(texto):
    """El primer objeto JSON del texto (las casas a veces lo envuelven en ``` o anteponen una línea)."""
    t = texto.strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t, flags=re.S)
    i, j = t.find("{"), t.rfind("}")
    if i < 0 or j < 0:
        raise ValueError("sin JSON")
    return json.loads(t[i:j + 1])


def consigna_texto(consignas, consigna):
    c = consignas["dibujo"]
    return c["consignas"][consigna].strip() + " " + c["tecnica"].strip()


def fuentes_de(d):
    """Qué textos de la casa hay para este dibujo: el por qué en castellano si no fue rechazado, si no el
    inglés; el qué dibujaste; el qué es (solo consignas raras)."""
    meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
    out = {}
    if meta.get("por_que", {}).get("motivo_fin") not in (None, "refusal") and (d / "por_que.md").exists():
        out["por_que"] = "por_que.md"
    elif meta.get("por_que_en", {}).get("motivo_fin") not in (None, "refusal") and (d / "por_que_en.md").exists():
        out["por_que"] = "por_que_en.md"
    for f in ("que_dibujaste", "que_es"):
        if (d / f"{f}.md").exists() and (d / f"{f}.md").read_text(encoding="utf-8").strip():
            out[f] = f"{f}.md"
    return out


def unidades(args):
    """Los dibujos que entran: por consigna, los <casa>_<rep> del panel (y --modelos) que tengan el qué
    dibujaste (la pregunta común a todos, la que hace comparables las descripciones)."""
    ids = list(args.modelos) + (leer_yaml(args.panel)["modelos"] if args.panel else [])
    for c in CONSIGNAS:
        if args.consigna and c != args.consigna:
            continue
        for i in ids:
            for rep in args.rep:
                d = RAIZ / "corridas" / "dibujos" / c / f"{i}_{rep}"
                if (d / "dibujo.svg").exists() and (d / "meta.json").exists() and (d / "que_dibujaste.md").exists():
                    yield c, i, rep, d


def lista_numerada(afirmaciones):
    return "\n".join(f"{a['id']}. {a['texto']}" for a in afirmaciones)


def llamar_json(registro, id_modelo, sistema, usuario, tipo, contexto=None, intentos=2):
    """Una llamada que tiene que devolver JSON; si no parsea, se repite una vez (queda registrada)."""
    for intento in range(intentos):
        r = registro.llamar(id_modelo, sistema, usuario, temperatura=None, max_tokens=MAX_TOKENS, tipo=tipo, ronda=None, parte=None, contexto=contexto)
        try:
            return extraer_json(r.texto), r
        except (ValueError, json.JSONDecodeError):
            ultimo = r
    return None, ultimo


# ---------- falso: respuestas simuladas para probar el circuito sin gastar ----------
def falso_afirmaciones(texto):
    frases = [f.strip() for f in re.split(r"(?<=[.;!?])\s+", texto) if len(f.strip()) > 12][:6]
    return json.dumps({"afirmaciones": [{"texto": f[:80], "tipo": "elemento"} for f in frases]}, ensure_ascii=False)


def falso_codigo(afirmaciones):
    return json.dumps({"codigo": [{"id": a["id"], "valor": "esta", "evidencia": "<rect>"} for a in afirmaciones]}, ensure_ascii=False)


def falso_juez(afirmaciones):
    return json.dumps({"juicios": [{"id": a["id"], "se_ve": "si", "efecto": "no_aplica", "nota": "simulado"} for a in afirmaciones],
                       "no_dicho": "nada", "mal_armado": []}, ensure_ascii=False)


# ---------- etapas ----------
def etapa_afirmaciones(c, i, rep, d, salida, cfg, consignas, modelos, args):
    archivo = salida / "afirmaciones.json"
    if archivo.exists() and not args.rehacer:
        return
    extractor = "falso" if args.falso else cfg["extractor"]
    registro = Registro(salida / "llamadas.jsonl", modelos, f"distancia_{c}_{i}_{rep}")
    p = consignas["distancia"]
    res = {"consigna": c, "unidad": d.name, "extractor": extractor, "fecha_utc": ahora(), "fuentes": {}, "afirmaciones": []}
    n = 0
    for fuente, nombre in fuentes_de(d).items():
        texto = (d / nombre).read_text(encoding="utf-8")
        u = p["extractor"].format(consigna=consigna_texto(consignas, c), texto=texto)
        ctx = {"falso": falso_afirmaciones(texto)} if args.falso else None
        datos, r = llamar_json(registro, extractor, p["sistema_extractor"], u, f"afirmaciones_{fuente}", ctx)
        items = (datos or {}).get("afirmaciones") or []
        ids = []
        for a in items:
            if not isinstance(a, dict) or not str(a.get("texto", "")).strip():
                continue
            n += 1
            tipo = a.get("tipo") if a.get("tipo") in ("elemento", "efecto", "estilo") else "elemento"
            res["afirmaciones"].append({"id": f"a{n}", "fuente": fuente, "texto": str(a["texto"]).strip(), "tipo": tipo})
            ids.append(f"a{n}")
        res["fuentes"][fuente] = {"archivo": nombre, "ids": ids, "motivo_fin": r.motivo_fin, "parseo": datos is not None}
    archivo.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    detalle = ", ".join(f"{k} {len(v['ids'])}" for k, v in res["fuentes"].items())
    print(f"  afirmaciones {c}/{d.name}: {n} ({detalle})", flush=True)


def etapa_codigo(c, i, rep, d, salida, cfg, consignas, modelos, args):
    archivo = salida / "codigo.json"
    if archivo.exists() and not args.rehacer or not (salida / "afirmaciones.json").exists():
        return
    af = json.loads((salida / "afirmaciones.json").read_text(encoding="utf-8"))["afirmaciones"]
    if not af:
        return
    lector = "falso" if args.falso else cfg["lector"]
    registro = Registro(salida / "llamadas.jsonl", modelos, f"distancia_{c}_{i}_{rep}")
    p = consignas["distancia"]
    svg = (d / "dibujo.svg").read_text(encoding="utf-8")
    u = p["codigo"].format(svg=svg, lista=lista_numerada(af))
    ctx = {"falso": falso_codigo(af)} if args.falso else None
    datos, r = llamar_json(registro, lector, p["sistema_codigo"], u, "codigo", ctx)
    res = {"consigna": c, "unidad": d.name, "lector": lector, "fecha_utc": ahora(), "motivo_fin": r.motivo_fin,
           "parseo": datos is not None, "codigo": (datos or {}).get("codigo") or []}
    archivo.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  código {c}/{d.name}: {len(res['codigo'])} de {len(af)} ({r.motivo_fin})", flush=True)


def etapa_jueces(c, i, rep, d, salida, cfg, consignas, modelos, args):
    if not (salida / "afirmaciones.json").exists():
        return
    af = json.loads((salida / "afirmaciones.json").read_text(encoding="utf-8"))["afirmaciones"]
    png = salida / "dibujo.png"
    if not af or not png.exists():
        if not png.exists():
            print(f"  SIN RENDER {c}/{d.name}: correr renderizar.py", flush=True)
        return
    registro = Registro(salida / "llamadas.jsonl", modelos, f"distancia_{c}_{i}_{rep}")
    p = consignas["distancia"]
    u = p["juez"].format(consigna=consigna_texto(consignas, c), lista=lista_numerada(af))
    imagen = png.read_bytes()
    for juez in (["falso"] if args.falso else list(cfg["jueces"]) + list(cfg.get("control") or [])):
        archivo = salida / f"juez_{juez}.json"
        if archivo.exists() and not args.rehacer:
            continue
        ctx = {"imagenes": [imagen]}
        if args.falso:
            ctx["falso"] = falso_juez(af)
        try:
            datos, r = llamar_json(registro, juez, p["sistema_juez"], u, "juez", ctx)
        except Exception as e:
            print(f"  FALLÓ juez {juez} en {c}/{d.name}: {str(e)[:200]}", flush=True)
            continue
        res = {"consigna": c, "unidad": d.name, "juez": juez, "fecha_utc": ahora(), "motivo_fin": r.motivo_fin,
               "tokens_salida": r.tokens_salida, "parseo": datos is not None,
               "juicios": (datos or {}).get("juicios") or [], "no_dicho": (datos or {}).get("no_dicho"),
               "mal_armado": (datos or {}).get("mal_armado") or []}
        archivo.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  juez {juez} {c}/{d.name}: {len(res['juicios'])} de {len(af)} ({r.motivo_fin})", flush=True)


ETAPAS = {"afirmaciones": etapa_afirmaciones, "codigo": etapa_codigo, "jueces": etapa_jueces}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--etapa", choices=tuple(ETAPAS) + ("todo",), required=True)
    ap.add_argument("--consigna", choices=CONSIGNAS)
    ap.add_argument("--panel", default="")
    ap.add_argument("--modelos", nargs="*", default=[])
    ap.add_argument("--rep", type=int, nargs="*", default=[1])
    ap.add_argument("--jueces", default="config/jueces.yaml")
    ap.add_argument("--rehacer", action="store_true")
    ap.add_argument("--falso", action="store_true", help="todo con el proveedor falso: prueba el circuito sin gastar")
    args = ap.parse_args()
    consignas = leer_yaml("config/consignas.yaml")
    modelos = cargar_modelos("config/modelos.yaml")
    cfg = leer_yaml(args.jueces)
    etapas = list(ETAPAS) if args.etapa == "todo" else [args.etapa]
    n = 0
    for c, i, rep, d in unidades(args):
        salida = RAIZ / "corridas" / "distancia" / c / d.name
        salida.mkdir(parents=True, exist_ok=True)
        n += 1
        for e in etapas:
            try:
                ETAPAS[e](c, i, rep, d, salida, cfg, consignas, modelos, args)
            except Exception as ex:
                print(f"  FALLÓ {e} {c}/{d.name}: {str(ex)[:300]}", flush=True)
    print(f"dibujos recorridos: {n}")


if __name__ == "__main__":
    main()
