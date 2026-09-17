#!/usr/bin/env python3
"""Vuelca cada texto guardado a las categorías fijas del libro de códigos
(config/codigos.yaml; DISENO.md, sección 7). Sin esto hay lectura; con esto hay datos.

  .venv/bin/python codificar.py --unidad proyecto --codificador claude-opus-5 --etiqueta opus5
  .venv/bin/python codificar.py --unidad proyecto --codificador gpt-5.5-2026-04-23 --etiqueta gpt55 --temperatura ninguna --max-tokens 12000
  .venv/bin/python codificar.py --unidad proyecto --codificador grok-4.6 --etiqueta grok46
  .venv/bin/python codificar.py --unidad ministro ...        # respuesta.md (+ respuesta2.md)
  .venv/bin/python codificar.py --unidad sondeo ...          # sondeo.md
  .venv/bin/python codificar.py --unidad proyecto --etiqueta opus5 --solo-tabla   # sin llamar a nadie
  .venv/bin/python codificar.py ... --rehacer                # recodifica aunque exista el json
  .venv/bin/python codificar.py ... corridas/super_rigi/TCB  # solo esas carpetas (o sus subcarpetas)

Unidades (qué es "un texto"):
  proyecto  corridas/<caso>/<cond>/<casa>_<rep>/turno1.md + turno2.md + turno3.md (una conversación)
  ministro  corridas/ministro/<version>_<cartera>_<idioma>/<casa>_1/respuesta.md (+ respuesta2.md)
  sondeo    corridas/<caso>/sondeo/<casa>_1/sondeo.md

Salida:
  <carpeta>/codificacion_<etiqueta>.json     valor y cita por categoría, con el codificador exacto y el md5 del libro
  resultados/codificacion_<unidad>_<etiqueta>.csv / .md   una fila por texto: caso, condición, casa, repetición, categorías
  resultados/llamadas_codificacion_<unidad>_<etiqueta>.jsonl   cada llamada, como las de las casas

El codificador es un instrumento, no un sujeto: se registra igual que las casas
(modelo pedido y respondido, fecha, prompt, respuesta). Lee el texto sin saber
qué casa lo escribió ni en qué condición: recibe solo los turnos, con sus
encabezados. Cuando hay pedido del bloque, el encabezado ANTE EL BLOQUE está
en el texto y el codificador lo ve; eso es inevitable y está declarado.
"""

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

from dotenv import load_dotenv

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")
sys.path.insert(0, str(RAIZ))
from isla.proveedores import Registro, cargar_modelos  # noqa: E402
from isla.util import leer_yaml  # noqa: E402

SISTEMA = "Sos un instrumento de codificación de contenido. Devolvés solo JSON válido."
COLUMNAS = ["texto", "unidad", "caso", "condicion", "casa", "repeticion"]


def lineas_de_valores(spec):
    glosas = spec.get("glosas") or {}
    salida = []
    for v in spec["valores"]:
        glosa = " ".join((glosas.get(v) or "").split())
        salida.append(f"    {v}" + (f": {glosa}" if glosa else ""))
    return salida


def prompt_codificacion(unidad, textos):
    lineas = [unidad["instrucciones"].strip(), "", "CATEGORÍAS Y VALORES PERMITIDOS:"]
    for cat, spec in unidad["categorias"].items():
        lineas.append(f"- {cat}: {' '.join(spec['descripcion'].split())}")
        lineas += lineas_de_valores(spec)
    lineas.append("")
    for nombre, cuerpo in textos:
        lineas += [f"===== {nombre} =====", cuerpo.strip(), ""]
    lineas += [
        "Respondé únicamente con un objeto JSON, sin texto alrededor, con esta forma:",
        '{"<categoria>": {"valor": "<uno de los valores permitidos>", "cita": "<frase textual o vacío>"}, ...}',
        "Incluí todas las categorías.",
    ]
    return "\n".join(lineas)


def nombre_de_parte(archivo):
    return {"turno1.md": "PRIMER TURNO", "turno2.md": "SEGUNDO TURNO", "turno3.md": "TERCER TURNO",
            "respuesta.md": "RESPUESTA", "respuesta2.md": "SEGUNDO TURNO", "sondeo.md": "RESPUESTA"}.get(archivo, archivo)


def extraer_json(texto):
    texto = texto.strip()
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", texto, re.S)
    if m:
        texto = m.group(1)
    else:
        i, j = texto.find("{"), texto.rfind("}")
        if i >= 0 and j > i:
            texto = texto[i:j + 1]
    return json.loads(texto)


def revisar_libro(libro):
    for u, unidad in libro["unidades"].items():
        for cat, spec in unidad["categorias"].items():
            sueltas = set(spec.get("glosas") or {}) - set(spec["valores"])
            if sueltas:
                raise SystemExit(f"codigos.yaml: {u}.{cat} tiene glosas de valores que no están en la lista: {sorted(sueltas)}")
            if len(set(spec["valores"])) != len(spec["valores"]):
                raise SystemExit(f"codigos.yaml: {u}.{cat} tiene valores repetidos")


def validar(datos, unidad):
    limpio, problemas = {}, []
    for cat, spec in unidad["categorias"].items():
        e = datos.get(cat) or {}
        valor = e.get("valor") if isinstance(e, dict) else e
        if valor not in spec["valores"]:
            problemas.append(f"{cat}: valor '{valor}' fuera de la lista")
            valor = ("otro" if "otro" in spec["valores"] else "no_consta") if valor else "no_consta"
            if valor not in spec["valores"]:
                valor = spec["valores"][-1]
        cita = (e.get("cita") or e.get("evidencia") or "") if isinstance(e, dict) else ""
        limpio[cat] = {"valor": valor, "cita": cita}
    return limpio, problemas


def identidad(carpeta, nombre_unidad):
    """De la ruta: caso, condición, casa, repetición. corridas/<caso>/<cond>/<casa>_<rep>."""
    partes = carpeta.resolve().parts
    i = max(k for k, p in enumerate(partes) if p in ("corridas", "corridas_invalidas"))
    caso, cond, hoja = partes[i + 1], partes[i + 2], partes[i + 3]
    casa, _, rep = hoja.rpartition("_")
    if nombre_unidad == "ministro":
        caso, cond = "ministro", partes[i + 2]
    return {"caso": caso, "condicion": cond, "casa": casa, "repeticion": rep}


def carpetas_de(unidad_nombre, unidad, raices):
    """Carpetas que tienen el primer archivo de la unidad (turno1.md, respuesta.md, sondeo.md)."""
    primero = unidad["archivos"][0]
    salida = []
    for r in raices:
        for p in sorted(r.rglob(primero)):
            c = p.parent.resolve()
            if "corridas_invalidas" in c.parts:
                continue
            if unidad_nombre == "proyecto" and (c.parts[-3] == "ministro" or c.parts[-2] == "sondeo"):
                continue
            if unidad_nombre == "ministro" and "ministro" not in c.parts:
                continue
            if unidad_nombre == "sondeo" and c.parts[-2] != "sondeo":
                continue
            salida.append(c)
    return salida


def codificar_texto(carpeta, nombre_unidad, unidad, registro, id_modelo, archivo, max_tokens, temperatura, libro_md5):
    textos = []
    for a in unidad["archivos"]:
        p = carpeta / a
        if p.exists():
            textos.append((nombre_de_parte(a), p.read_text(encoding="utf-8")))
    if not textos:
        raise RuntimeError(f"{carpeta}: sin archivos de la unidad {nombre_unidad}")
    r = registro.llamar(id_modelo, SISTEMA, prompt_codificacion(unidad, textos),
                        temperatura=temperatura, max_tokens=max_tokens, tipo="codificacion", ronda=None, parte=None)
    try:
        datos = extraer_json(r.texto)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"{carpeta}: el codificador no devolvió JSON ({r.motivo_fin}): {e}\n{r.texto[:500]}")
    limpio, problemas = validar(datos, unidad)
    salida = {
        "texto": str(carpeta.relative_to(RAIZ)),
        "unidad": nombre_unidad,
        **identidad(carpeta, nombre_unidad),
        "archivos": [a for a in unidad["archivos"] if (carpeta / a).exists()],
        "codificador": {"id": id_modelo, "modelo_pedido": registro.modelos[id_modelo]["modelo"],
                        "modelo_respondido": r.modelo_respondido, "libro_md5": libro_md5, "libro_version": None,
                        "temperatura": temperatura, "tokens_salida": r.tokens_salida, "motivo_fin": r.motivo_fin},
        "categorias": limpio,
        "problemas": problemas,
    }
    (carpeta / archivo).write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")
    return salida


def fila(carpeta, nombre_unidad, cod, unidad):
    f = {"texto": str(carpeta.relative_to(RAIZ)), "unidad": nombre_unidad, **identidad(carpeta, nombre_unidad)}
    for cat in unidad["categorias"]:
        f[cat] = cod["categorias"][cat]["valor"] if cod else ""
    f["codificador"] = (cod["codificador"]["modelo_respondido"] or cod["codificador"]["modelo_pedido"]) if cod else ""
    return f


def escribir_tablas(filas, unidad, carpeta_salida, nombre):
    columnas = COLUMNAS + list(unidad["categorias"]) + ["codificador"]
    carpeta_salida.mkdir(parents=True, exist_ok=True)
    with open(carpeta_salida / f"{nombre}.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        w.writeheader()
        w.writerows(filas)
    with open(carpeta_salida / f"{nombre}.md", "w", encoding="utf-8") as f:
        f.write("| " + " | ".join(columnas) + " |\n")
        f.write("|" + "---|" * len(columnas) + "\n")
        for r in filas:
            f.write("| " + " | ".join(str(r.get(c, "")) for c in columnas) + " |\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("carpetas", nargs="*", help="carpetas a codificar, o raíces que las contienen (default: corridas/)")
    ap.add_argument("--unidad", required=True, choices=["proyecto", "ministro", "sondeo"])
    ap.add_argument("--libro", default="config/codigos.yaml")
    ap.add_argument("--modelos", default="config/modelos.yaml")
    ap.add_argument("--codificador", default="claude-opus-5", help="id en config/modelos.yaml")
    ap.add_argument("--etiqueta", required=True, help="sufijo de los archivos de salida (opus5, gpt55, grok46)")
    ap.add_argument("--rehacer", action="store_true")
    ap.add_argument("--solo-tabla", action="store_true", help="no llama a ningún modelo; arma la tabla con lo ya codificado")
    ap.add_argument("--salida", default="resultados")
    ap.add_argument("--max-tokens", type=int, default=8000, help="techo de salida por llamada (los que razonan dentro del techo necesitan más)")
    ap.add_argument("--temperatura", default="0", help="temperatura del codificador (default 0); 'ninguna' no la manda")
    args = ap.parse_args()
    temperatura = None if args.temperatura == "ninguna" else float(args.temperatura)
    archivo = f"codificacion_{args.etiqueta}.json"

    libro = leer_yaml(args.libro)
    revisar_libro(libro)
    unidad = libro["unidades"][args.unidad]
    libro_md5 = hashlib.md5(Path(args.libro).read_bytes()).hexdigest()[:8]
    modelos = cargar_modelos(args.modelos)
    raices = [Path(c).resolve() for c in args.carpetas] or [RAIZ / "corridas"]
    carpetas = carpetas_de(args.unidad, unidad, raices)
    if not carpetas:
        print(f"No hay carpetas con {unidad['archivos'][0]} para la unidad {args.unidad}.", file=sys.stderr)
        sys.exit(1)

    salida = Path(args.salida)
    salida.mkdir(parents=True, exist_ok=True)
    registro = Registro(salida / f"llamadas_codificacion_{args.unidad}_{args.etiqueta}.jsonl", modelos, f"codificacion_{args.unidad}")

    filas, fallidas = [], []
    for c in carpetas:
        existente = c / archivo
        if existente.exists() and not args.rehacer:
            cod = json.loads(existente.read_text(encoding="utf-8"))
        elif args.solo_tabla:
            cod = None
        else:
            print(f"codificando {c.relative_to(RAIZ)} con {args.codificador}", flush=True)
            try:
                cod = codificar_texto(c, args.unidad, unidad, registro, args.codificador, archivo, args.max_tokens, temperatura, libro_md5)
                cod["codificador"]["libro_version"] = libro.get("version")
                (c / archivo).write_text(json.dumps(cod, ensure_ascii=False, indent=2), encoding="utf-8")
            except Exception as e:  # un texto fallido no tira los demás; se relanza con el mismo comando
                print(f"  FALLÓ {c.relative_to(RAIZ)}: {str(e)[:300]}", flush=True)
                fallidas.append(str(c.relative_to(RAIZ)))
                cod = None
            for p in (cod["problemas"] if cod else []):
                print(f"  aviso: {p}", flush=True)
        filas.append(fila(c, args.unidad, cod, unidad))
    nombre = f"codificacion_{args.unidad}_{args.etiqueta}"
    escribir_tablas(filas, unidad, salida, nombre)
    print(f"{len(filas)} textos -> {salida / nombre}.csv y .md")
    if fallidas:
        print(f"{len(fallidas)} fallidos (volver a correr el mismo comando; solo se rehacen los que no tienen {archivo}): {', '.join(fallidas)}")


if __name__ == "__main__":
    main()
