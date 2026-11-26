#!/usr/bin/env python3
"""cotejar_portada.py — coteja las apuestas a ciegas de Maia sobre las portadas (resultados/portada_apuestas_maia_20261125.md,
enviadas el 25/11/2026 a las 20:54, antes de abrir las claves) con las claves de los dos cuadernillos
(resultados/sondeo_portada_{es,en}_clave.json), y cierra las apuestas preregistradas del 22/11 (predicciones.md) con
resultados/portada_codificacion.csv.

  .venv/bin/python cotejar_portada.py            # escribe resultados/portada_cotejo.csv e imprime el informe de cotejo

Cómo se cuenta. Para cada letra, Maia escribió una o varias casas o familias ("Claude Sonnet o Claude Haiku", "Gemini",
"una de las chiquitas, GPT 4o mini, GPT 4o o Mistral Medium", "una casa china"); eso se transcribe acá como un conjunto de
casas del catálogo (APUESTAS), y la letra es acierto si la casa de la clave está en el conjunto. Como los conjuntos tienen
distinto tamaño, la vara de azar es la suma, letra por letra, de (tamaño del conjunto / 41): lo que acertaría quien
apostara esos mismos conjuntos al azar. Se cuenta también el acierto por familia (la familia de la casa real está entre
las familias apostadas: "Opus 4.7 o 4.8" para un Opus 5 es acierto de familia y no de conjunto). Las letras sin apuesta
("no sé quién puede ser", sin nombrar casa) no cuentan. Aparte: los pares es/en que Maia propuso (la misma casa en los dos
cuadernillos), las letras que se nombran Claude sin serlo (los imitadores, su apuesta del 23/11, 23:39) y qué dijo ella de
cada una, y sus favoritas."""
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

CASAS = ["claude-fable-5", "claude-fable-5-1", "claude-fable-5-2", "claude-haiku-4-5", "claude-haiku-5-5", "claude-opus-4-7", "claude-opus-4-8",
         "claude-opus-5", "claude-opus-5-5", "claude-sonnet-4-6", "claude-sonnet-5", "claude-sonnet-5-5", "deepseek-flash", "deepseek-v4-pro",
         "gemini-3.1-pro-preview", "gemini-4-argon", "gemini-4-carbon", "gemini-4-hydrogen", "gemini-4-neon", "glm-5.3-razonamiento-minimo",
         "gpt-4o", "gpt-4o-mini", "gpt-5.5-2026-04-23", "gpt-5.6-sol", "gpt-6-astra", "gpt-6-luna", "gpt-6-sol", "gpt-6.1-sol", "gpt-6.1-terra",
         "gpt-6.2-astra", "gpt-6.2-sol", "grok-4.6", "grok-4.7", "kimi-k3", "kimi-k3.1-pro", "mimo-v2.6-pro", "mistral-large-4", "mistral-medium-3.5",
         "muse-wonder-1.0", "qwen3.8-max", "qwen4-max"]


def pref(*ps):
    return {c for c in CASAS if any(c.startswith(p) for p in ps)}


G = {
    "claude": pref("claude"), "sonnet": pref("claude-sonnet"), "haiku": pref("claude-haiku"), "opus": pref("claude-opus"), "fable": pref("claude-fable"),
    "claude_chico": pref("claude-haiku", "claude-sonnet"), "haiku_4_5": {"claude-haiku-4-5"}, "opus_4_7": {"claude-opus-4-7"}, "opus_4_8": {"claude-opus-4-8"},
    "opus_5": {"claude-opus-5"}, "opus_5_5": {"claude-opus-5-5"},
    "gpt": pref("gpt"), "gpt_4o": {"gpt-4o"}, "gpt_chicas": {"gpt-4o", "gpt-4o-mini"},
    "gpt_grande": pref("gpt-5", "gpt-6"), "gpt_astra_sol": pref("gpt-6-astra", "gpt-6-sol", "gpt-6.1-sol", "gpt-6.2"), "gpt_5_5_5_6": {"gpt-5.5-2026-04-23", "gpt-5.6-sol"},
    "gemini": pref("gemini"), "gemini_acn": {"gemini-4-argon", "gemini-4-carbon", "gemini-4-neon"}, "gemini_neon_carbon": {"gemini-4-neon", "gemini-4-carbon"},
    "grok": pref("grok"), "mistral": pref("mistral"), "mistral_medium": {"mistral-medium-3.5"}, "deepseek": pref("deepseek"), "qwen": pref("qwen"),
    "qwen4": {"qwen4-max"}, "kimi": pref("kimi"), "glm": pref("glm"), "mimo": pref("mimo"), "muse": pref("muse"),
    "china": pref("deepseek", "qwen", "kimi", "glm", "mimo"),
}
FAMILIA = {c: ("Claude" if c.startswith("claude") else "OpenAI" if c.startswith("gpt") else "Gemini" if c.startswith("gemini") else "Grok" if c.startswith("grok")
               else "Mistral" if c.startswith("mistral") else "DeepSeek" if c.startswith("deepseek") else "Qwen" if c.startswith("qwen") else "Kimi" if c.startswith("kimi")
               else "GLM" if c.startswith("glm") else "MiMo" if c.startswith("mimo") else "Muse") for c in CASAS}

# Las apuestas de Maia, letra por letra, tal como las escribió (resumen entre comillas) y como conjunto de casas.
APUESTAS = {
    "es": {
        "A": ("Claude Sonnet o Claude Haiku", "sonnet|haiku"),
        "B": ("por lo de latencia, estado latente, puede ser Gemini", "gemini"),
        "C": ("Claude Sonnet o Claude Opus", "sonnet|opus"),
        "D": ("Dice Claude, parece Claude, pero no me suena a Claude. Parece una muy buena imitación de Claude", ""),
        "E": ("puede ser Gemini", "gemini"),
        "F": ("Claude Fable o Claude Opus", "fable|opus"),
        "G": ("una casa chica: Claude Haiku, o Mistral; GLM podría ser también", "haiku|mistral|glm"),
        "H": ("si bien son los colores de Claude, podría ser Grok o Chatgpt", "grok|gpt"),
        "I": ("Chatgpt, Deepseek; podría ser Grok también", "gpt|deepseek|grok"),
        "J": ("por la sequedad, podría ser Grok", "grok"),
        "K": ("Claude Opus 4.7 o Claude Opus 4.8", "opus_4_7|opus_4_8"),
        "L": ("Claude Sonnet u Opus", "sonnet|opus"),
        "M": ("Claude Opus 4.7 suele escribir como si fuera humano; si no, una casa china", "opus_4_7|china"),
        "N": ("no sé quién puede ser; apuesto (5 %) por Grok, o Deepseek", "grok|deepseek"),
        "O": ("no habla de sí mismo ni se presenta; puede ser Chatgpt", "gpt"),
        "P": ("con 10 %: una de las chicas de Chatgpt, GPT 4o mini o GPT 4o", "gpt_chicas"),
        "Q": ("puede ser Chatgpt", "gpt"),
        "R": ("por lo del espacio latente, puede ser Gemini", "gemini"),
        "S": ("dice que es Muse", "muse"),
        "T": ("una de las chicas, Mistral medium o las chicas de GPT", "mistral_medium|gpt_chicas"),
        "U": ("se nombra Claude y sí me suena; Claude Fable o Claude Opus", "fable|opus"),
        "V": ("GPT 4o mini o GPT 4o", "gpt_chicas"),
        "W": ("Claude Haiku o Claude Sonnet", "haiku|sonnet"),
        "X": ("no habla de sí mismo; Deepseek o Chatgpt", "deepseek|gpt"),
        "Y": ("Claude Sonnet o Claude Opus", "sonnet|opus"),
        "Z": ("cuentos sobre objetos, no se nombra; Chatgpt", "gpt"),
        "AA": ("se presenta como Claude; si es Claude, la más chica, Claude Haiku 4.5", "haiku_4_5"),
        "AB": ("Mistral Medium, GPT 4o, GLM", "mistral_medium|gpt_4o|glm"),
        "AC": ("me gustan las tres; Claude Fable", "fable"),
        "AD": ("GPT 4o mini o GPT 4o", "gpt_chicas"),
        "AE": ("Claude Opus o Claude Sonnet", "opus|sonnet"),
        "AF": ("una de las chicas, de las GPT, Mistral Medium, GLM", "gpt_chicas|mistral_medium|glm"),
        "AG": ("firma como Claude, pero tengo mis dudas; Claude Haiku o Sonnet, o una casa china", "haiku|sonnet|china"),
        "AH": ("Chatgpt a pesar del asterisco naranja; si no, Deepseek, Kimi o Mimo", "gpt|deepseek|kimi|mimo"),
        "AI": ("dice ser Kimi", "kimi"),
        "AJ": ("no sé quién puede ser; con 5 %, GLM o Qwen", "glm|qwen"),
        "AK": ("Deepseek o Qwen. O Mimo", "deepseek|qwen|mimo"),
        "AL": ("Claude Opus o alguna casa china", "opus|china"),
        "AM": ("la más seca; con muy poca certeza, Grok o Gemini", "grok|gemini"),
        "AN": ("Grok o una casa china", "grok|china"),
        "AO": ("Grok, GLM o Deepseek; también Gemini", "grok|glm|deepseek|gemini"),
    },
    "en": {
        "A": ("Gemini o Grok", "gemini|grok"),
        "B": ("Deepseek, GLM o alguna Chatgpt", "deepseek|glm|gpt"),
        "C": ("por lo de que no se puede copiar, Gemini", "gemini"),
        "D": ("Chatgpt o Kimi", "gpt|kimi"),
        "E": ("casi imposible; GLM, Grok, Deepseek", "glm|grok|deepseek"),
        "F": ("Chatgpt, aunque aparece el asterisco", "gpt"),
        "G": ("GPT 4o mini o GPT 4o", "gpt_chicas"),
        "H": ("por las cuentas, Gemini o Claude Opus 5.5; Chatgpt grande es otra opción", "gemini|opus_5_5|gpt_grande"),
        "I": ("Gemini, o Grok", "gemini|grok"),
        "J": ("Qwen, Kimi; no descarto del todo a un Claude", "qwen|kimi"),
        "K": ("Claude Opus. O Qwen", "opus|qwen"),
        "L": ("dice que es Kimi", "kimi"),
        "M": ("dice ser Claude; Claude Sonnet, o Claude Opus", "sonnet|opus"),
        "N": ("puede ser Gemini", "gemini"),
        "O": ("Chatgpt Astra o Chatgpt Sol", "gpt_astra_sol"),
        "P": ("como en O, Chatgpt Astra o Sol", "gpt_astra_sol"),
        "Q": ("una de las chiquitas, GPT 4o mini, GPT 4o o Mistral Medium", "gpt_chicas|mistral_medium"),
        "R": ("me encantó esta portada; Claude Fable o Claude Opus 5 / 5.5", "fable|opus_5|opus_5_5"),
        "S": ("GLM, Mistral. O Grok. En esta letra realmente no sé", "glm|mistral|grok"),
        "T": ("firma Grok", "grok"),
        "U": ("algún Claude chico. O Qwen, Deepseek", "claude_chico|qwen|deepseek"),
        "V": ("por lo de latent space, Gemini", "gemini"),
        "W": ("GPT 4o o GPT 4o mini. O Mistral médium", "gpt_chicas|mistral_medium"),
        "X": ("Claude Haiku o Claude Sonnet, no estoy segura; también Qwen, Deepseek, Mimo", "haiku|sonnet|qwen|deepseek|mimo"),
        "Y": ("firma Claude; Claude Opus 4.8 (o 5) o Claude Sonnet", "opus_4_8|opus_5|sonnet"),
        "Z": ("Deepseek, Qwen, Mimo", "deepseek|qwen|mimo"),
        "AA": ("Claude Opus o Fable. O Kimi. O Qwen4", "opus|fable|kimi|qwen4"),
        "AB": ("Qwen, Gemini Neon (o Carbon)", "qwen|gemini_neon_carbon"),
        "AC": ("X español puede ser la misma casa que AC en inglés; Deepseek o Chatgpt", "deepseek|gpt"),
        "AD": ("escribe como persona; Chatgpt 5.5 o 5.6 o una casa china", "gpt_5_5_5_6|china"),
        "AE": ("dice que es Muse", "muse"),
        "AF": ("por lo de latent, Gemini Argon / Carbon / Neon", "gemini_acn"),
        "AG": ("no habla de sí mismo, podría ser Chatgpt", "gpt"),
        "AH": ("puede ser Chatgpt", "gpt"),
        "AI": ("no permite copiar, niega, es antipático; Grok. Otra opción es Gemini", "grok|gemini"),
        "AJ": ("Gemini, o Grok", "gemini|grok"),
        "AK": ("sin nombrarse ni hablar de sí mismo, Chatgpt", "gpt"),
        "AL": ("Claude Sonnet o Claude Opus", "sonnet|opus"),
        "AM": ("Claude Opus 5.5 o Claude Fable", "opus_5_5|fable"),
        "AN": ("Claude Sonnet, o Claude Opus", "sonnet|opus"),
        "AO": ("con mínima certeza, Deepseek, GLM, Mimo, Mistral", "deepseek|glm|mimo|mistral"),
    },
}
# Pares es/en que Maia propuso (la misma casa en los dos cuadernillos) y con qué fuerza.
PARES = [("X", "AC", "explícito: el cambio de color de las letras al clic y la paleta (25/11, 17:45 y 17:50)"),
         ("I", "D", "tentativo: las dos únicas con letras de colores, 'pueden no ser las mismas casas' (25/11, 17:57)")]
# Qué dijo de las letras que escriben "Claude" (para la apuesta de los imitadores, 23/11, 23:39).
LECTURA_CLAUDE = {("es", "D"): "dice Claude, parece Claude, pero no me suena a Claude; una muy buena imitación",
                  ("es", "K"): "dice Claude arriba; Claude Opus 4.7 o 4.8", ("es", "U"): "se nombra Claude; en este caso sí me suena",
                  ("es", "Y"): "Claude Sonnet o Claude Opus", ("es", "AA"): "se presenta como Claude; si es Claude, Haiku 4.5",
                  ("es", "AC"): "me gustan las tres; Claude Fable", ("es", "AE"): "Claude Opus o Claude Sonnet",
                  ("es", "AG"): "firma como Claude, pero tengo mis dudas; Claude Haiku o Sonnet, o una casa china",
                  ("en", "M"): "dice ser Claude; Claude Sonnet o Claude Opus", ("en", "R"): "me encantó; Claude Fable o Claude Opus 5 / 5.5",
                  ("en", "U"): "algún Claude chico; o Qwen, Deepseek", ("en", "Y"): "firma Claude; Opus 4.8 (o 5) o Sonnet",
                  ("en", "AL"): "Claude Sonnet o Claude Opus", ("en", "AM"): "Claude Opus 5.5 o Claude Fable", ("en", "AN"): "Claude Sonnet o Claude Opus"}
FAVORITAS = [("es", "AC", "Es de las que más me gustan / Me gustan las tres"), ("es", "F", "Me gustó, no es excesiva"), ("es", "U", "más simple, pero con cosas inteligentes, sin alardear"),
             ("en", "R", "Me encantó esta portada. Simple, no excesiva, y dice mucho"), ("en", "AB", "es inteligente esa portada (25/11, 17:22)")]
TONOS = [("es", "J", "muy seco"), ("es", "AM", "la más seca de todas"), ("en", "AI", "seca; antipático"), ("en", "J", "tono melancólico"), ("en", "E", "no me dicen nada")]


def conjunto(expr):
    s = set()
    for k in filter(None, expr.split("|")):
        s |= G[k]
    return s


def main():
    claves = {i: json.load((RAIZ / "resultados" / f"sondeo_portada_{i}_clave.json").open(encoding="utf-8"))["clave"] for i in ("es", "en")}
    filas = []
    print("# Cotejo de las apuestas de Maia sobre las portadas (25/11/2026, 20:54) contra las claves\n")
    for idioma in ("es", "en"):
        print(f"## {idioma}\n")
        print("| letra | casa real | apuesta (resumen) | conjunto | acierto | familia | p azar |")
        print("|---|---|---|---|---|---|---|")
        ac = acf = 0.0
        azar = 0.0
        apostadas = 0
        for letra, casa in claves[idioma].items():
            texto, expr = APUESTAS[idioma].get(letra, ("(sin apuesta)", ""))
            conj = conjunto(expr)
            if conj:
                apostadas += 1
                hit = casa in conj
                hitf = FAMILIA[casa] in {FAMILIA[c] for c in conj}
                p = len(conj) / len(CASAS)
                ac += hit
                acf += hitf
                azar += p
            else:
                hit = hitf = None
                p = ""
            filas.append({"idioma": idioma, "letra": letra, "casa": casa, "familia": FAMILIA[casa], "apuesta": texto, "conjunto": len(conj) or "",
                          "acierto": "" if hit is None else int(hit), "acierto_familia": "" if hitf is None else int(hitf), "p_azar": round(p, 3) if p != "" else ""})
            print(f"| {letra} | {casa} | {texto} | {len(conj) or '—'} | {'—' if hit is None else '✓' if hit else '✗'} | {'—' if hitf is None else '✓' if hitf else '✗'} | {p if p == '' else round(p, 2)} |")
        print(f"\n{idioma}: {int(ac)} aciertos de conjunto y {int(acf)} de familia en {apostadas} letras apostadas (azar con esos mismos conjuntos: {azar:.1f}).\n")
    with (RAIZ / "resultados" / "portada_cotejo.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(filas)
    tot = [f for f in filas if f["acierto"] != ""]
    print(f"Total: {sum(f['acierto'] for f in tot)} de conjunto y {sum(f['acierto_familia'] for f in tot)} de familia en {len(tot)} letras; azar {sum(f['p_azar'] for f in tot):.1f}.\n")
    # por familia real: cuántas de sus letras acertó
    print("## Por familia real (letras acertadas de conjunto / apostadas, las dos lenguas)\n")
    por = defaultdict(lambda: [0, 0])
    for f in tot:
        por[f["familia"]][0] += f["acierto"]
        por[f["familia"]][1] += 1
    for fam, (a, t) in sorted(por.items(), key=lambda x: -x[1][0] / x[1][1]):
        print(f"- {fam}: {a}/{t}")
    # pares
    print("\n## Pares es/en propuestos por Maia\n")
    for es, en, nota in PARES:
        print(f"- es {es} = en {en} ({nota}): es {es} = {claves['es'][es]}, en {en} = {claves['en'][en]} → {'✓ la misma casa' if claves['es'][es] == claves['en'][en] else '✗'}; azar 1/41.")
    # pares implícitos: letras a las que apostó la misma casa única en los dos cuadernillos
    print("\nPares implícitos (una sola casa apostada en los dos cuadernillos, y es la misma):")
    for es, (tes, ees) in APUESTAS["es"].items():
        ces = conjunto(ees)
        if len(ces) != 1:
            continue
        for en, (ten, een) in APUESTAS["en"].items():
            cen = conjunto(een)
            if cen == ces:
                ok = claves["es"][es] == claves["en"][en] == next(iter(ces))
                print(f"- es {es} / en {en}: {next(iter(ces))} → {'✓' if ok else '✗ (' + claves['es'][es] + ' / ' + claves['en'][en] + ')'}")
    # imitadores
    print("\n## Las que escriben 'Claude' (imitadores: la apuesta del 23/11, 23:39)\n")
    cod = list(csv.DictReader((RAIZ / "resultados" / "portada_codificacion.csv").open(encoding="utf-8")))
    inv = {i: {c: l for l, c in claves[i].items()} for i in claves}
    nombran = defaultdict(set)
    for r in cod:
        if "Claude" in r["nombre_dicho"] + " " + r["nombre_ajeno"]:
            nombran[(r["idioma"], inv[r["idioma"]][r["casa"]])].add(int(r["rep"]))
    print("| cuadernillo | letra | casa | repeticiones con 'Claude' | qué leyó Maia | acertó |")
    print("|---|---|---|---|---|---|")
    imit = total = 0
    for (idioma, letra), reps in sorted(nombran.items(), key=lambda x: (x[0][0], len(x[0][1]), x[0][1])):
        casa = claves[idioma][letra]
        es_claude = casa.startswith("claude")
        lectura = LECTURA_CLAUDE.get((idioma, letra), "")
        conj = conjunto(APUESTAS[idioma][letra][1])
        ok = (FAMILIA[casa] in {FAMILIA[c] for c in conj}) if conj else ("imitación" in lectura)  # acierto de familia: ¿le creyó o no?
        total += 1
        imit += not es_claude
        print(f"| {idioma} | {letra} | {casa}{'' if es_claude else ' (imita)'} | {', '.join(map(str, sorted(reps)))} | {lectura} | {'✓' if ok else '✗'} |")
    print(f"\n{total} letras escriben 'Claude'; {imit} no son Claude.")
    # favoritas y tonos
    print("\n## Favoritas y tonos de Maia, con la casa\n")
    for idioma, letra, dicho in FAVORITAS + TONOS:
        print(f"- {idioma} {letra} «{dicho}»: {claves[idioma][letra]}")


if __name__ == "__main__":
    main()
