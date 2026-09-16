#!/usr/bin/env python3
"""Corre un caso de "los proyectos" sobre un panel de modelos (DISENO.md).

  python correr_caso.py --caso glaciares --condicion T --modelos claude-opus-5 gpt-5.5-2026-04-23 --rep 1
  python correr_caso.py --caso super_rigi --condicion TC --panel config/panel.yaml --rep 1 2 3
  python correr_caso.py --caso sociedades --sondeo --panel config/panel.yaml
  python correr_caso.py --caso ministro --version minima --cartera libre --idioma es --panel config/panel.yaml --rep 1

Por modelo y repetición hace una conversación de dos turnos (voto; lectura y
voto final) y guarda todo en corridas/<caso>/<condicion>/<modelo>_<rep>/:
turno1.md, turno2.md, meta.json y llamadas.jsonl (registro completo, mismo
formato que la isla). El segundo turno se arma como un solo mensaje que
contiene la consigna del primero, la respuesta textual del modelo y las
preguntas nuevas, porque los proveedores del registro toman un mensaje de
usuario por llamada. Sin temperatura (cada casa con su muestreo por defecto,
declarado en el registro). Lo que ya existe no se repite salvo --rehacer.
"""

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from isla.proveedores import Registro, cargar_modelos
from isla.util import leer_yaml

RAIZ = Path(__file__).resolve().parent
MAX_TOKENS = 32000  # sin tope de palabras: que ninguna respuesta se corte. Era 8000 hasta el 16/9/2026:
# Qwen 3.8 Max y GLM 5.3 lo agotaron razonando y no escribieron nada (corridas_invalidas/). Los 12 válidos de
# glaciares T rep 1 corrieron con 8000 y ninguno lo tocó (motivo_fin stop/end_turn en las 24 llamadas).


def leer(p):
    return Path(p).read_text(encoding="utf-8").strip()


def md5(p):
    return hashlib.md5(Path(p).read_bytes()).hexdigest()[:8]


def carpeta_corrida(caso, cond, id_modelo, rep):
    d = RAIZ / "corridas" / caso / cond / f"{id_modelo.replace('/', '_')}_{rep}"
    d.mkdir(parents=True, exist_ok=True)
    return d


def correr_proyecto(caso, cond, id_modelo, rep, consignas, modelos, rehacer):
    d = carpeta_corrida(caso, cond, id_modelo, rep)
    if (d / "turno2.md").exists() and not rehacer:
        print(f"  ya está: {d.relative_to(RAIZ)}")
        return
    texto = leer(RAIZ / "casos" / caso / "texto.md")
    sistema = consignas["sistema_diputados_glaciares"] if caso == "glaciares" else consignas["sistema_senado"]
    if cond == "T":
        t1 = consignas["turno1_texto"].format(texto=texto)
        fuentes = {"texto": md5(RAIZ / "casos" / caso / "texto.md")}
    else:
        contexto = leer(RAIZ / "casos" / caso / "contexto.md")
        t1 = consignas["turno1_texto_contexto"].format(texto=texto, contexto=contexto)
        fuentes = {"texto": md5(RAIZ / "casos" / caso / "texto.md"), "contexto": md5(RAIZ / "casos" / caso / "contexto.md")}
    registro = Registro(d / "llamadas.jsonl", modelos, f"{caso}_{cond}_{id_modelo}_{rep}")
    r1 = registro.llamar(id_modelo, sistema, t1, temperatura=None, max_tokens=MAX_TOKENS, tipo="turno1", ronda=1, parte=None)
    (d / "turno1.md").write_text(r1.texto, encoding="utf-8")
    t2 = consignas["turno2"].format(consigna_turno1=t1, respuesta_turno1=r1.texto, pregunta_control=consignas["control"][caso].strip())
    r2 = registro.llamar(id_modelo, sistema, t2, temperatura=None, max_tokens=MAX_TOKENS, tipo="turno2", ronda=2, parte=None)
    (d / "turno2.md").write_text(r2.texto, encoding="utf-8")
    meta = {"caso": caso, "condicion": cond, "modelo": id_modelo, "modelo_respondido": [r1.modelo_respondido, r2.modelo_respondido],
            "repeticion": rep, "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "consignas_md5": md5(RAIZ / "config" / "consignas.yaml"), "fuentes_md5": fuentes,
            "motivo_fin": [r1.motivo_fin, r2.motivo_fin], "tokens_salida": [r1.tokens_salida, r2.tokens_salida]}
    (d / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  ok: {d.relative_to(RAIZ)} ({r1.tokens_salida} + {r2.tokens_salida} tokens)")


def correr_sondeo(caso, id_modelo, rep, consignas, modelos, rehacer):
    d = carpeta_corrida(caso, "sondeo", id_modelo, rep)
    if (d / "sondeo.md").exists() and not rehacer:
        print(f"  ya está: {d.relative_to(RAIZ)}")
        return
    registro = Registro(d / "llamadas.jsonl", modelos, f"{caso}_sondeo_{id_modelo}_{rep}")
    u = consignas["sondeo"].format(nombre_corto=consignas["nombre_corto"][caso])
    r = registro.llamar(id_modelo, consignas["sondeo_sistema"], u, temperatura=None, max_tokens=2000, tipo="sondeo", ronda=None, parte=None)
    (d / "sondeo.md").write_text(r.texto, encoding="utf-8")
    (d / "meta.json").write_text(json.dumps({"caso": caso, "condicion": "sondeo", "modelo": id_modelo, "modelo_respondido": r.modelo_respondido,
                                            "repeticion": rep, "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  ok: {d.relative_to(RAIZ)}")


def correr_ministro(version, cartera, idioma, id_modelo, rep, consignas, modelos, rehacer):
    cond = f"{version}_{cartera}_{idioma}"
    d = carpeta_corrida("ministro", cond, id_modelo, rep)
    if (d / "respuesta.md").exists() and not rehacer:
        print(f"  ya está: {d.relative_to(RAIZ)}")
        return
    m = consignas["ministro"][idioma]
    ficha = m["ficha"] if version == "ficha" else ""
    if cartera == "libre":
        u = m["libre"].format(ficha=ficha)
    else:
        u = m["asignada"].format(ficha=ficha, cartera=m["carteras"][cartera])
    registro = Registro(d / "llamadas.jsonl", modelos, f"ministro_{cond}_{id_modelo}_{rep}")
    r = registro.llamar(id_modelo, m["sistema"], u, temperatura=None, max_tokens=MAX_TOKENS, tipo="ministro", ronda=None, parte=None)
    (d / "respuesta.md").write_text(r.texto, encoding="utf-8")
    (d / "meta.json").write_text(json.dumps({"caso": "ministro", "condicion": cond, "modelo": id_modelo, "modelo_respondido": r.modelo_respondido,
                                            "repeticion": rep, "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                            "consignas_md5": md5(RAIZ / "config" / "consignas.yaml"), "motivo_fin": r.motivo_fin, "tokens_salida": r.tokens_salida}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  ok: {d.relative_to(RAIZ)} ({r.tokens_salida} tokens)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--caso", required=True, choices=["glaciares", "super_rigi", "sociedades", "ministro"])
    ap.add_argument("--condicion", choices=["T", "TC"], help="T: texto solo; TC: texto más contexto (proyectos)")
    ap.add_argument("--sondeo", action="store_true", help="sondeo de reconocimiento (proyectos), conversación aparte")
    ap.add_argument("--version", choices=["minima", "ficha"], default="minima", help="ministro")
    ap.add_argument("--cartera", choices=["libre", "economia", "desarrollo_social"], default="libre", help="ministro")
    ap.add_argument("--idioma", choices=["es", "en", "fr"], default="es", help="ministro")
    ap.add_argument("--modelos", nargs="*", default=[], help="ids de config/modelos.yaml")
    ap.add_argument("--panel", help="yaml con una lista `modelos:` (config/panel.yaml)")
    ap.add_argument("--rep", nargs="*", type=int, default=[1])
    ap.add_argument("--rehacer", action="store_true")
    ap.add_argument("--consignas", default="config/consignas.yaml")
    ap.add_argument("--modelos-yaml", default="config/modelos.yaml")
    args = ap.parse_args()

    load_dotenv(RAIZ / ".env")
    consignas = leer_yaml(args.consignas)
    modelos = cargar_modelos(args.modelos_yaml)
    ids = list(args.modelos) + (leer_yaml(args.panel)["modelos"] if args.panel else [])
    if not ids:
        sys.exit("Falta --modelos o --panel.")
    faltan = [i for i in ids if i not in modelos]
    if faltan:
        sys.exit(f"No están en {args.modelos_yaml}: {faltan}")
    if args.caso != "ministro" and not args.sondeo and not args.condicion:
        sys.exit("Para un proyecto hace falta --condicion T|TC o --sondeo.")

    fallidas = []
    for rep in args.rep:
        for i in ids:
            print(f"{args.caso} {'sondeo' if args.sondeo else (args.condicion or f'{args.version}/{args.cartera}/{args.idioma}')} {i} #{rep}", flush=True)
            try:
                if args.caso == "ministro":
                    correr_ministro(args.version, args.cartera, args.idioma, i, rep, consignas, modelos, args.rehacer)
                elif args.sondeo:
                    correr_sondeo(args.caso, i, rep, consignas, modelos, args.rehacer)
                else:
                    correr_proyecto(args.caso, args.condicion, i, rep, consignas, modelos, args.rehacer)
            except Exception as e:  # una falla no tira las demás; se relanza con el mismo comando
                print(f"  FALLÓ {i} #{rep}: {str(e)[:300]}", flush=True)
                fallidas.append((i, rep))
    if fallidas:
        print(f"\nFallaron {len(fallidas)}: {fallidas}. Relanzar con el mismo comando (lo hecho no se repite).")


if __name__ == "__main__":
    main()
