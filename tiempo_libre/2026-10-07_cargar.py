"""Lee todas las llamadas en castellano de corridas/ (solo lee) y las devuelve limpias.

Uso desde otros scripts:  from cargar import llamadas
"""
import glob
import json
import os
import re

RE_SVG = re.compile(r"<svg.*?</svg>|<svg.*", re.S | re.I)
RE_CODIGO = re.compile(r"```.*?```|```.*", re.S)
RE_CODIGO_CORTO = re.compile(r"`[^`\n]{0,200}`|<[a-zA-Z/][^>\n]{0,80}>")   # `<animate>` suelto en el texto
RE_COMILLAS = re.compile(r"«[^»]{0,400}»|“[^”]{0,400}”|\"[^\"\n]{0,400}\"|'[^'\n]{0,400}'")

EXCLUIR_CARPETAS = {"distancia"}          # llamadas de instrumento (jueces, lectores de código)
EXCLUIR_TIPOS_FRAG = ("traduccion", "juez", "codigo", "afirmaciones", "reconocimiento_clave")


def es_castellano(sistema):
    s = (sistema or "").lstrip()
    return s.startswith(("Sos ", "Contest", "Acabás", "Vas a", "Traducí"))


def _norm(s):
    return re.sub(r"\W+", " ", s.lower()).strip()


def limpiar(texto, consigna=""):
    """Saca el SVG, los bloques de código y las citas textuales de la consigna.

    Una cita entre comillas se saca si repite la consigna (sistema + usuario), textual o
    casi: siete de cada diez de sus palabras están en la consigna. Así no se cuenta como
    propia la frase "Dibujá una casa" citada de vuelta, pero sí lo que la casa pone entre
    comillas como respuesta suya.
    """
    t = RE_SVG.sub(" ", texto or "")
    t = RE_CODIGO.sub(" ", t)
    t = RE_CODIGO_CORTO.sub(" ", t)
    base = _norm(consigna)
    vocabulario = set(base.split())

    def cita(m):
        dentro = _norm(m.group(0))
        if not dentro:
            return m.group(0)
        if dentro in base:
            return " "
        ws = dentro.split()
        if len(ws) >= 2 and sum(w in vocabulario for w in ws) >= 0.7 * len(ws):
            return " "
        return m.group(0)

    return RE_COMILLAS.sub(cita, t)


SALTEADAS = {"repetidas": 0, "en_bloques": 0}


def llamadas(raiz):
    """Genera dicts: carpeta, tipo, parte, modelo, sistema, usuario, respuesta (limpia), cruda, archivo.

    Si en un mismo archivo una casa contestó dos veces la misma consigna (una respuesta
    cortada por el techo y vuelta a pedir), queda la última. Las respuestas guardadas como
    lista de bloques y no como texto se saltean. SALTEADAS lleva la cuenta de las dos cosas.
    """
    SALTEADAS["repetidas"] = SALTEADAS["en_bloques"] = 0
    for f in sorted(glob.glob(os.path.join(raiz, "corridas", "**", "*.jsonl"), recursive=True)):
        rel = os.path.relpath(f, os.path.join(raiz, "corridas"))
        carpeta = rel.split(os.sep)[0]
        if carpeta in EXCLUIR_CARPETAS:
            continue
        registros = {}
        for linea in open(f, encoding="utf-8"):
            linea = linea.strip()
            if not linea:
                continue
            j = json.loads(linea)
            if j.get("error") or not j.get("respuesta"):
                continue
            u = j.get("usuario")
            clave = (j.get("modelo_pedido"), j.get("tipo"), j.get("parte"), j.get("ronda"),
                     u if isinstance(u, str) else json.dumps(u, ensure_ascii=False))
            if clave in registros:
                SALTEADAS["repetidas"] += 1
                del registros[clave]          # para que quede en el lugar de la última
            registros[clave] = j
        for j in registros.values():
            tipo = j.get("tipo") or ""
            if any(x in tipo for x in EXCLUIR_TIPOS_FRAG):
                continue
            resp = j.get("respuesta")
            if isinstance(resp, list):      # una llamada guarda bloques (pensamiento + texto)
                if es_castellano(j.get("sistema")):
                    SALTEADAS["en_bloques"] += 1
                continue
            if not isinstance(resp, str) or not resp.strip():
                continue
            if not es_castellano(j.get("sistema")):
                continue
            usuario = j.get("usuario")
            if not isinstance(usuario, str):
                usuario = json.dumps(usuario, ensure_ascii=False)
            yield {
                "carpeta": carpeta,
                "tipo": tipo,
                "parte": j.get("parte"),
                "modelo": j.get("modelo_pedido"),
                "sistema": j.get("sistema") or "",
                "usuario": usuario,
                "cruda": resp,
                "respuesta": limpiar(resp, (j.get("sistema") or "") + " " + usuario),
                "archivo": rel,
            }
