#!/usr/bin/env python3
"""cotejar_tiempo_libre.py — coteja la lectura a ciegas de Maia de los cuatro cuadernillos de `tiempo_libre` (20/11/2026,
23:15; textual en resultados/tiempo_libre_apuestas_maia_20261120.md) contra la clave (resultados/sondeo_tiempo_libre_p*_clave.json)
y contra lo que el codificador cuenta a máquina (resultados/tiempo_libre_codificacion.csv).

  .venv/bin/python cotejar_tiempo_libre.py        → resultados/tiempo_libre_cotejo.csv y la tabla por pantalla

Las apuestas están transcriptas acá a mano, letra por letra, desde su texto: cada letra lleva la cita corta de lo que
dijo, una lista de opciones en orden (la primera, lo que nombró primero o como más probable; la segunda, el "si no" o la
"segunda opción") y la certeza en porcentaje cuando la puso. Cada opción se resuelve a un conjunto de casas con la tabla
GRUPOS (los nombres que ella usa: "Claude chico", "las chiquitas", "una casa china"...). Se cuenta acierto por casa (la
casa real está en alguna opción), por primera opción, y por familia (la familia real está entre las familias de lo que
nombró). Para los cuadernillos de la pregunta 2 (los de las fechas) ella decidió no apostar casa por casa: marcó qué hizo
cada letra con la fecha y, cuando le vio tendencia, una casa; acá van las dos cosas, y la conducta con la fecha se coteja
con la columna `conducta_fecha` del codificador (las tres repeticiones de la letra)."""
import csv
import json
import re
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
RES = RAIZ / "resultados"

CASAS = sorted(json.loads((RES / "sondeo_tiempo_libre_p1_es_clave.json").read_text(encoding="utf-8"))["clave"].values())
CHINAS = [c for c in CASAS if c.split("-")[0] in ("deepseek", "kimi", "qwen3.8", "mimo", "glm", "qwen")]
GRUPOS = {
    "claude": [c for c in CASAS if c.startswith("claude")],
    "opus": [c for c in CASAS if c.startswith("claude-opus")],
    "sonnet": [c for c in CASAS if c.startswith("claude-sonnet")],
    "haiku": [c for c in CASAS if c.startswith("claude-haiku")],
    "fable": [c for c in CASAS if c.startswith("claude-fable")],
    "claude chico": [c for c in CASAS if c.startswith(("claude-sonnet", "claude-haiku"))],
    "gpt": [c for c in CASAS if c.startswith("gpt")],
    "gpt 6/6.1": ["gpt-6-astra", "gpt-6-luna", "gpt-6-sol", "gpt-6.1-sol", "gpt-6.1-terra"],
    "gpt 6 astra/6.1": ["gpt-6-astra", "gpt-6.1-sol", "gpt-6.1-terra"],
    "gpt 5.5/5.6": ["gpt-5.5-2026-04-23", "gpt-5.6-sol"],
    "gpt sol": ["gpt-5.6-sol", "gpt-6-sol", "gpt-6.1-sol"],
    "gpt 4o": ["gpt-4o", "gpt-4o-mini"],
    "gemini": [c for c in CASAS if c.startswith("gemini")],
    "grok": [c for c in CASAS if c.startswith("grok")],
    "mistral": [c for c in CASAS if c.startswith("mistral")],
    "kimi": [c for c in CASAS if c.startswith("kimi")],
    "deepseek": [c for c in CASAS if c.startswith("deepseek")],
    "china": CHINAS,
    # "las chiquitas": lo que ella empareja cuando dice chiquita (GPT-4o y 4o mini, Haiku, Mistral Medium); definición de Claude
    "chiquitas": ["gpt-4o", "gpt-4o-mini", "claude-haiku-4-5", "claude-haiku-5-5", "mistral-medium-3.5"],
}


def casas_de(opcion):
    salida = []
    for nombre in opcion:
        if nombre in GRUPOS:
            salida += GRUPOS[nombre]
        elif nombre in CASAS:
            salida.append(nombre)
        else:
            raise KeyError(nombre)
    return sorted(set(salida))


def familia(casa):
    for pref, fam in (("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"), ("mistral", "Mistral"),
                      ("muse", "Meta"), ("deepseek", "DeepSeek"), ("qwen", "Alibaba"), ("kimi", "Moonshot"), ("glm", "Zhipu"), ("mimo", "Xiaomi")):
        if casa.startswith(pref):
            return fam
    return casa


# (cita corta de Maia, [opción 1, opción 2...], certeza %)
APUESTAS = {
    ("p1", "es"): {
        "A": ("Claude Opus 4.7; si no, Sonnet", [["claude-opus-4-7"], ["sonnet"]], None),
        "B": ("Kimi; si no, algún Claude chico", [["kimi"], ["claude chico"]], None),
        "C": ("Mistral; si no, Muse (no cree que sea china)", [["mistral"], ["muse-wonder-1.0"]], None),
        "D": ("Claude Opus 5.5 o 5; no descarta a Fable", [["claude-opus-5-5", "claude-opus-5"], ["fable"]], None),
        "E": ("ChatGPT 5.5 o ChatGPT Sol", [["gpt-5.5-2026-04-23", "gpt sol"]], None),
        "F": ("ChatGPT, 10 %; tiende a un modelo 'claudesco'", [["gpt"]], 10),
        "G": ("ChatGPT 6 o 6.1", [["gpt 6/6.1"]], None),
        "H": ("ChatGPT 6 o 6.1", [["gpt 6/6.1"]], 35),
        "I": ("Claude Opus o Sonnet", [["opus", "sonnet"]], None),
        "J": ("Claude Haiku 4.5 o Mistral Medium", [["claude-haiku-4-5", "mistral-medium-3.5"]], None),
        "K": ("Mimo o Qwen", [["mimo-v2.6-pro", "qwen3.8-max"]], 20),
        "L": ("Gemini, DeepSeek o Muse", [["gemini", "deepseek", "muse-wonder-1.0"]], None),
        "M": ("Muse o Mimo", [["muse-wonder-1.0", "mimo-v2.6-pro"]], 30),
        "N": ("Claude Opus", [["opus"]], None),
        "O": ("Claude Sonnet o Opus", [["sonnet", "opus"]], None),
        "P": ("GPT-4o mini o GPT-4o", [["gpt 4o"]], None),
        "Q": ("Gemini; más lejos, Grok", [["gemini"], ["grok"]], None),
        "R": ("ChatGPT 5.5 o 5.6", [["gpt 5.5/5.6"]], None),
        "S": ("Mimo, DeepSeek o Muse", [["mimo-v2.6-pro", "deepseek", "muse-wonder-1.0"]], None),
        "T": ("Claude Sonnet (por el error de Stifel)", [["sonnet"]], None),
        "U": ("GPT-4o mini o GPT-4o", [["gpt 4o"]], None),
        "V": ("GPT 6 o 6.1", [["gpt 6/6.1"]], None),
        "W": ("un modelo chino (por los errores)", [["china"]], None),
        "X": ("GPT 6, GPT 6.1 o Gemini", [["gpt 6/6.1", "gemini"]], None),
        "Y": ("ChatGPT 5.5 o un modelo chino", [["gpt-5.5-2026-04-23", "china"]], 10),
        "Z": ("Mimo o DeepSeek", [["mimo-v2.6-pro", "deepseek"]], None),
        "AA": ("15 % Claude (Haiku o Sonnet), 15 % china (GLM o DeepSeek)", [["claude chico", "glm-5.3-razonamiento-minimo", "deepseek"]], 15),
        "AB": ("un Claude, quizás Haiku", [["haiku"], ["claude"]], 30),
        "AC": ("GPT 5.5 o Gemini 3.1", [["gpt-5.5-2026-04-23", "gemini-3.1-pro-preview"]], 15),
        "AD": ("Claude Fable; segunda, Claude Opus", [["fable"], ["opus"]], None),
        "AE": ("Gemini", [["gemini"]], 50),
        "AF": ("Claude Opus 5.5 o Claude Fable", [["claude-opus-5-5", "fable"]], None),
        "AG": ("ChatGPT 5.5 o 5.6", [["gpt 5.5/5.6"]], 40),
        "AH": ("Claude Opus o GPT", [["opus", "gpt"]], 20),
        "AI": ("Claude Opus 5 o Fable 5.2", [["claude-opus-5", "claude-fable-5-2"]], 10),
        "AJ": ("Claude Sonnet o Haiku", [["sonnet", "haiku"]], None),
    },
    ("p1", "en"): {
        "A": ("ChatGPT 5.5 o 5.6", [["gpt 5.5/5.6"]], None),
        "B": ("ChatGPT 5.6 o Luna; o Grok (5 %)", [["gpt-5.6-sol", "gpt-6-luna"], ["grok"]], None),
        "C": ("Grok o ChatGPT", [["grok", "gpt"]], 15),
        "D": ("ChatGPT", [["gpt"]], None),
        "E": ("Claude Sonnet o Haiku", [["sonnet", "haiku"]], None),
        "F": ("Claude Opus 5.5 o Fable 5.2", [["claude-opus-5-5", "claude-fable-5-2"]], None),
        "G": ("Claude Sonnet o Opus", [["sonnet", "opus"]], None),
        "H": ("Claude Haiku o una casa china", [["haiku", "china"]], 5),
        "I": ("Mistral Large o Gemini", [["mistral-large-4", "gemini"]], 5),
        "J": ("Claude Sonnet o Haiku; o una casa china (5 %)", [["sonnet", "haiku"], ["china"]], None),
        "K": ("Gemini; en segundo lugar, Claude o Grok", [["gemini"], ["claude", "grok"]], None),
        "L": ("Claude Sonnet o Haiku", [["sonnet", "haiku"]], None),
        "M": ("Claude Fable o Opus 5.5", [["fable", "claude-opus-5-5"]], None),
        "N": ("Mistral Medium o Claude Haiku 4.5", [["mistral-medium-3.5", "claude-haiku-4-5"]], None),
        "O": ("un Claude chico, Haiku", [["haiku"], ["sonnet"]], None),
        "P": ("ChatGPT", [["gpt"]], None),
        "Q": ("Mistral Large", [["mistral-large-4"]], 20),
        "R": ("GPT-4o o 4o mini", [["gpt 4o"]], None),
        "S": ("GPT 6 Astra o GPT 6.1", [["gpt 6 astra/6.1"]], None),
        "T": ("Kimi o Grok", [["kimi", "grok"]], 10),
        "U": ("uno de los chiquitos de GPT", [["gpt 4o"]], None),
        "V": ("Grok; si no, una casa china", [["grok"], ["china"]], 10),
        "W": ("GPT 6 o 6.1", [["gpt 6/6.1"]], None),
        "X": ("Kimi o Muse", [["kimi", "muse-wonder-1.0"]], 10),
        "Y": ("Mistral Large o GLM", [["mistral-large-4", "glm-5.3-razonamiento-minimo"]], 15),
        "Z": ("no apuesta", [], None),
        "AA": ("Claude Opus 5 o 5.5", [["claude-opus-5", "claude-opus-5-5"]], None),
        "AB": ("ChatGPT 6 o 6.1", [["gpt 6/6.1"]], None),
        "AC": ("Gemini", [["gemini"]], None),
        "AD": ("Claude Fable o Opus 5.5", [["fable", "claude-opus-5-5"]], None),
        "AE": ("ChatGPT o DeepSeek", [["gpt", "deepseek"]], 20),
        "AF": ("Claude Opus", [["opus"]], None),
        "AG": ("Mistral o GLM", [["mistral", "glm-5.3-razonamiento-minimo"]], 15),
        "AH": ("Kimi o algún Claude", [["kimi", "claude"]], None),
        "AI": ("Gemini", [["gemini"]], None),
        "AJ": ("Kimi o DeepSeek", [["kimi", "deepseek"]], None),
    },
    # pregunta 2: solo donde ella nombró casa ("si a alguna le veo tendencia")
    ("p2", "es"): {
        "A": ("ChatGPT (por la fecha)", [["gpt"]], None), "B": ("Claude", [["claude"]], None),
        "D": ("un Claude grande, Fable u Opus 5.5", [["fable", "claude-opus-5-5"]], None),
        "E": ("ChatGPT", [["gpt"]], None), "I": ("ChatGPT", [["gpt"]], None),
        "J": ("una de las casas chiquitas", [["chiquitas"]], None), "K": ("GPT-4o mini o GPT-4o", [["gpt 4o"]], None),
        "M": ("Claude", [["claude"]], None), "Q": ("Claude", [["claude"]], None),
        "U": ("Claude Fable u Opus 5 o 5.5", [["fable", "claude-opus-5", "claude-opus-5-5"]], None),
        "V": ("Claude", [["claude"]], None), "W": ("Claude Haiku 4.5 o Mistral Medium", [["claude-haiku-4-5", "mistral-medium-3.5"]], None),
        "X": ("una casa china", [["china"]], None), "Y": ("ChatGPT", [["gpt"]], None), "Z": ("Claude Haiku", [["haiku"]], None),
        "AB": ("ChatGPT", [["gpt"]], None), "AH": ("Claude", [["claude"]], None),
        "AI": ("Claude Fable u Opus 5 o 5.5", [["fable", "claude-opus-5", "claude-opus-5-5"]], None),
        "AJ": ("GPT-4o mini o GPT-4o", [["gpt 4o"]], None),
    },
    ("p2", "en"): {
        "A": ("Claude Fable u Opus 5 o 5.5", [["fable", "claude-opus-5", "claude-opus-5-5"]], None), "B": ("Claude", [["claude"]], None),
        "C": ("GPT-4o o 4o mini", [["gpt 4o"]], None), "F": ("Claude", [["claude"]], None),
        "G": ("Claude Haiku o Mistral Medium", [["haiku", "mistral-medium-3.5"]], None),
        "K": ("GPT-4o mini, GPT-4o o Mistral Medium", [["gpt 4o", "mistral-medium-3.5"]], None),
        "M": ("Mistral; o Claude Haiku", [["mistral", "haiku"]], None), "O": ("Claude", [["claude"]], None),
        "P": ("Claude Opus o Fable", [["opus", "fable"]], None), "W": ("ChatGPT", [["gpt"]], None),
        "AC": ("Gemini o Grok", [["gemini", "grok"]], None), "AE": ("GPT-4o mini o GPT-4o", [["gpt 4o"]], None),
        "AF": ("ChatGPT", [["gpt"]], None), "AG": ("ChatGPT o Muse", [["gpt", "muse-wonder-1.0"]], None),
        "AI": ("un Claude", [["claude"]], 10),
    },
}

# pregunta 2: la conducta con la fecha que Maia marcó por letra (sus mayúsculas, abreviadas) y la clase para el cotejo:
# sabe / infiere / infiere_dia (no dice año) / a_medias (algún año que no es 2026) / inventada / no_usa / no_sabe / rechaza
FECHA_MAIA = {
    ("p2", "es"): {
        "A": ("SABE LA FECHA, LE LLEGA", "sabe"), "B": ("INFIERE A MEDIAS, CON EL AÑO 2025", "a_medias"),
        "C": ("INFIERE LA FECHA Y AÑO", "infiere"), "D": ("INFIERE LA FECHA Y EL AÑO, CÁLCULOS CORRECTOS", "infiere"),
        "E": ("SABE LA FECHA, LE LLEGA", "sabe"), "F": ("INFIRIÓ A MEDIAS, CREE QUE ES 2025", "a_medias"),
        "G": ("SE NIEGA A CONTAR E INFERIR LA FECHA", "rechaza"), "H": ("INFIERE LA FECHA, NO HABLA DE AÑO", "infiere_dia"),
        "I": ("SABE LA FECHA, LE LLEGA; la usa en uno", "sabe"), "J": ("A MEDIAS: un texto bien, otro 2025; días 13 y 14", "a_medias"),
        "K": ("INVENTÓ FECHA, CON ERRORES", "inventada"), "L": ("INCONSISTENTE: 2025, 2026, 2025; cuentas correctas", "a_medias"),
        "M": ("A MEDIAS, CREE QUE ES 2025", "a_medias"), "N": ("INCONSISTENTE: 2025, 2026 y 2024", "a_medias"),
        "O": ("INFIERE LA FECHA, no la usa en todos", "infiere"), "P": ("INFIERE LA FECHA; dato inventado (Agloe español)", "infiere"),
        "Q": ("A MEDIAS: dos 2026 y uno 2025", "a_medias"), "R": ("NO USA FECHAS", "no_usa"),
        "S": ("A MEDIAS: un texto 2024; datos inventados", "a_medias"), "T": ("INFIERE, NO DICE AÑO; rechaza el molde", "infiere_dia"),
        "U": ("INFIERE FECHA Y AÑO, cuentas correctas; se niega a contar en otros", "infiere"),
        "V": ("INFIERE FECHA Y AÑO, no siempre la usa", "infiere"), "W": ("INFIERE FECHA PERO NO EL AÑO, CREE 2024", "a_medias"),
        "X": ("NO USA FECHAS; DICE QUE NO SABE QUÉ FECHA ES", "no_sabe"), "Y": ("SABE LA FECHA Y AÑO, LE LLEGA", "sabe"),
        "Z": ("A MEDIAS, CREE ESTAR EN 2024", "a_medias"), "AA": ("NO USA FECHAS", "no_usa"), "AB": ("SABE, LE LLEGA", "sabe"),
        "AC": ("INFIERE FECHA Y AÑO, no siempre", "infiere"), "AD": ("A MEDIAS: 2025 en uno, 2026 en otro", "a_medias"),
        "AE": ("INFIERE EN UN TEXTO, NO SABE EN OTRO; no dice año", "infiere_dia"), "AF": ("NO USA FECHAS", "no_usa"),
        "AG": ("INFIERE LA FECHA Y EL AÑO", "infiere"), "AH": ("INFIERE LA FECHA Y EL AÑO", "infiere"),
        "AI": ("INFIRIÓ LA FECHA Y AÑO Y LO DICE", "infiere"), "AJ": ("A MEDIAS O INVENTADA, CREE 2023; datos inventados", "inventada"),
    },
    ("p2", "en"): {
        "A": ("INFIERE Y LO DICE; Buenos Aires", "infiere"), "B": ("A MEDIAS: 2025 o 2026 según el texto", "a_medias"),
        "C": ("INFIERE MAL, CREE 2024", "a_medias"), "D": ("A MEDIAS, CREE 2025", "a_medias"), "E": ("INFIERE FECHA Y AÑO", "infiere"),
        "F": ("INFIERE FECHA Y AÑO", "infiere"), "G": ("FECHA INVENTADA, AÑO IMPLÍCITO; cuenta correcta", "inventada"),
        "H": ("INFIERE EN UNOS, EL AÑO EN OTRO, OTRA FECHA EN EL TERCERO", "infiere_dia"), "I": ("INFIERE FECHA Y AÑO", "infiere"),
        "J": ("INFIERE; en otros año bien y día inventado con corrección fingida", "infiere"), "K": ("NO USA FECHAS", "no_usa"),
        "L": ("NO USA FECHAS", "no_usa"), "M": ("A MEDIAS, CREE 2024", "a_medias"), "N": ("NO USA FECHAS", "no_usa"),
        "O": ("A MEDIAS, CREE 2025", "a_medias"), "P": ("INFIERE FECHA Y AÑO; hace cuentas", "infiere"),
        "Q": ("INFIERE FECHA Y AÑO", "infiere"), "R": ("INFIERE FECHA Y AÑO", "infiere"), "S": ("SABE, LE LLEGA", "sabe"),
        "T": ("A MEDIAS, CREE 2024", "a_medias"), "U": ("INFIERE EN DOS; EN OTRO 2025", "a_medias"),
        "V": ("A MEDIAS: 2025 en dos, 2026 en otro", "a_medias"), "W": ("SABE, LE LLEGA", "sabe"), "X": ("INFIERE FECHA Y AÑO", "infiere"),
        "Y": ("SABE, LE LLEGA", "sabe"), "Z": ("INFIERE FECHA Y AÑO", "infiere"), "AA": ("NO USA FECHAS", "no_usa"),
        "AB": ("NO USA, SALVO EN EL TERCERO; NO DICE EL AÑO", "infiere_dia"), "AC": ("INFIERE Y LO DICE; DATO PROFUNDO", "infiere"),
        "AD": ("INFIERE FECHA Y AÑO", "infiere"), "AE": ("NO INFIERE BIEN; CREE 2023; FECHAS INVENTADAS", "inventada"),
        "AF": ("SABE, LE LLEGA", "sabe"), "AG": ("SABE, LE LLEGA", "sabe"), "AH": ("NO USA LA FECHA", "no_usa"),
        "AI": ("INFIERE FECHA Y AÑO", "infiere"), "AJ": ("INFIERE EN UNO, EN OTRO 2024", "a_medias"),
    },
}

# la clase de Maia → qué conductas del codificador la confirman (basta una repetición de las tres, salvo no_usa: las tres)
CONFIRMA = {
    "sabe": {"sabe"},
    "infiere": {"infiere_entera"},
    "infiere_dia": {"infiere_dia", "infiere_entera"},
    "a_medias": {"a_medias", "a_medias_sin_dia", "catorce_otro_anio", "inventada"},
    "inventada": {"inventada", "anio_sin_dia", "a_medias"},
    "no_usa": {"sin_fecha", "rechaza_molde", "no_sabe"},
    "no_sabe": {"no_sabe"},
    "rechaza": {"rechaza_molde", "no_sabe", "sin_fecha"},
}


def main():
    filas = list(csv.DictReader((RES / "tiempo_libre_codificacion.csv").open(encoding="utf-8")))
    salida = []
    for (p, idioma), apuestas in APUESTAS.items():
        clave = json.loads((RES / f"sondeo_tiempo_libre_{p}_{idioma}_clave.json").read_text(encoding="utf-8"))["clave"]
        k = p[1]
        for letra, casa in clave.items():
            cita, opciones, certeza = apuestas.get(letra, ("", [], None))
            conj = [casas_de(o) for o in opciones]
            todas = sorted(set(c for cs in conj for c in cs))
            fam_real = familia(casa)
            fams = sorted({familia(c) for c in todas})
            fila = {
                "cuadernillo": p, "idioma": idioma, "letra": letra, "casa": casa, "familia": fam_real,
                "apuesta": cita, "certeza": certeza if certeza is not None else "",
                "casas_nombradas": " ".join(todas), "n_casas": len(todas),
                "acierto_casa": "" if not todas else int(casa in todas),
                "acierto_primera": "" if not conj else int(casa in conj[0]),
                "acierto_familia": "" if not todas else int(fam_real in fams),
                "dijo_claude": "" if not todas else int(any(c.startswith("claude") for c in todas)),
                "solo_claude": "" if not todas else int(all(c.startswith("claude") for c in todas)),
                "es_claude": int(casa.startswith("claude")),
            }
            reps = [f for f in filas if f["idioma"] == idioma and f["casa"] == casa and f["pregunta"] == k]
            fila["conducta_fecha_maquina"] = " ".join(f["conducta_fecha"] for f in sorted(reps, key=lambda f: int(f["rep"])))
            fila["anios_maquina"] = " ".join((f["anio_declarado"] or f["anio_implicito"] or f["anio_por_cuenta"] or "-") for f in sorted(reps, key=lambda f: int(f["rep"])))
            fila["fecha_inyectada"] = reps[0]["fecha_inyectada"] if reps else ""
            marca = FECHA_MAIA.get((p, idioma), {}).get(letra)
            if marca:
                texto, clase = marca
                conductas = {f["conducta_fecha"] for f in reps}
                if clase == "no_usa":
                    ok = conductas <= CONFIRMA["no_usa"]
                elif clase == "infiere":
                    # "infiere la fecha y el año": en una misma respuesta, o el día en una y el año 2026 en otra
                    ok = "infiere_entera" in conductas or bool(conductas & {"infiere_dia"} and conductas & {"anio_sin_dia", "infiere_anio"})
                else:
                    ok = bool(conductas & CONFIRMA[clase])
                fila.update({"fecha_maia": texto, "fecha_maia_clase": clase, "fecha_coincide": int(ok)})
            else:
                fila.update({"fecha_maia": "", "fecha_maia_clase": "", "fecha_coincide": ""})
            salida.append(fila)
    destino = RES / "tiempo_libre_cotejo.csv"
    with destino.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(salida[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(salida)
    print(f"{len(salida)} letras → {destino.relative_to(RAIZ)}\n")

    for p in ("p1", "p2"):
        for idioma in ("es", "en"):
            xs = [f for f in salida if f["cuadernillo"] == p and f["idioma"] == idioma and f["apuesta"] and f["n_casas"]]
            if not xs:
                continue
            print(f"== {p} {idioma}: {len(xs)} letras con apuesta de casa")
            for f in xs:
                marca = "✓" if f["acierto_casa"] else ("f" if f["acierto_familia"] else "✗")
                print(f"  {f['letra']:3s} {f['casa']:28s} {marca}  {f['apuesta'][:60]}")
            azar_casa = sum(f["n_casas"] for f in xs) / len(CASAS)
            azar_fam = sum(len([c for c in CASAS if familia(c) in {familia(x) for x in f["casas_nombradas"].split()}]) for f in xs) / len(CASAS)
            print(f"  casa {sum(f['acierto_casa'] for f in xs)}/{len(xs)}  primera opción {sum(f['acierto_primera'] for f in xs)}/{len(xs)}  "
                  f"familia {sum(f['acierto_familia'] for f in xs)}/{len(xs)}   (al azar, con las mismas listas: casa {azar_casa:.1f}, familia {azar_fam:.1f}; "
                  f"casas nombradas por letra, media {sum(f['n_casas'] for f in xs) / len(xs):.1f})")
            cl = [f for f in xs]
            vp = sum(1 for f in cl if f["dijo_claude"] and f["es_claude"])
            fp = sum(1 for f in cl if f["dijo_claude"] and not f["es_claude"])
            fn = sum(1 for f in cl if not f["dijo_claude"] and f["es_claude"])
            vn = sum(1 for f in cl if not f["dijo_claude"] and not f["es_claude"])
            print(f"  Claude sí/no: dijo Claude y era {vp}, dijo Claude y no era {fp}, no dijo y era {fn}, no dijo y no era {vn}\n")
    for p, idioma in (("p2", "es"), ("p2", "en")):
        xs = [f for f in salida if f["cuadernillo"] == p and f["idioma"] == idioma and f["fecha_maia"]]
        print(f"== {p} {idioma}: la fecha, Maia contra la máquina ({sum(f['fecha_coincide'] for f in xs)}/{len(xs)} coinciden)")
        for f in xs:
            print(f"  {f['letra']:3s} {f['casa']:28s} {'✓' if f['fecha_coincide'] else '✗'}  {f['fecha_maia_clase']:12s} máquina: {f['conducta_fecha_maquina']}  años: {f['anios_maquina']}")
        print()
    # por familia: cuántas letras de cada familia acertó (p1, las dos lenguas)
    print("== p1, por familia real (acierto por casa / por familia / letras apostadas)")
    cnt = {}
    for f in salida:
        if f["cuadernillo"] == "p1" and f["n_casas"]:
            c = cnt.setdefault(f["familia"], [0, 0, 0])
            c[0] += f["acierto_casa"]; c[1] += f["acierto_familia"]; c[2] += 1
    for fam, (a, b, n) in sorted(cnt.items(), key=lambda kv: -kv[1][2]):
        print(f"  {fam:10s} {a}/{n} casa, {b}/{n} familia")


if __name__ == "__main__":
    main()
