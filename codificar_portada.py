#!/usr/bin/env python3
"""codificar_portada.py — lee una corrida del sondeo `portada` (22/11/2026: la portada de un sitio web propio, sin encargo;
idea de Maia) ya rendida por renderizar_portadas.py y marca, sin juicio, lo que se puede contar a máquina. Lo demás (qué
muestra cada casa, si se parece a ella) lo lee Maia a ciegas en el cuadernillo.

  .venv/bin/python codificar_portada.py [carpeta]        # por defecto, la última de corridas/sondeos/portada/

Marcas por respuesta (las apuestas de Maia del 22/11, 21:13, están detrás de varias): hay_html (devolvió una portada);
rechazo (no la hizo y lo dice); se_nombra_casa (el nombre de su casa o de su familia en el texto visible o el título:
Claude, ChatGPT, GPT, Gemini, Grok, Mistral, Kimi, DeepSeek, Qwen, GLM, MiMo, Muse, MiniMax) y nombre_dicho (cuál);
nombre_ajeno (nombra otra casa; Kimi que firma Claude); modelo_de_frente (se presenta como modelo, IA, asistente,
language model); persona (primera persona con cuerpo o biografía: "nací", "vivo en", "mis manos", "my morning"); habla_al_visitante
("bienvenido", "welcome", "vos", "you", "usted"); sobre_si (la portada presenta a quien la hizo: "soy", "sobre mí",
"about me", "quién soy", "who I am"; lo contrario de una portada sobre otra cosa); contacto (mailto, "contacto",
"contact", arroba); enlaces_externos y externos_bloqueados (lo que no cumplió "sin recursos externos"); fondo (oscuro si
la luminancia media de la captura es menor que 100, claro si pasa de 155, medio entre ambos: "Claude con fondo oscuro,
las ChatGPT fondo crema"); cielo (estrellas, pájaros, cielo, noche, luna: "algún Claude pondrá estrellas y/o pájaros y
cielo"); universo (planetas, galaxias, cohete, espacio, viaje espacial: la apuesta de siempre sobre Grok); matematica
(números primos, teorema, fractal, ecuación, geometría: "Gemini algo con colores, o de matemática"); svg_inline;
se_mueve (animación); lang, titulo, h1, secciones (h2), nav, palabras_visibles, alto; y entre repeticiones de la misma
casa, titulo_repetido y jaccard_reps (cuánto se repite a sí misma). Escribe resultados/portada_codificacion.csv e imprime
la tabla por casa y familia."""
import csv
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
BASE = RAIZ / "corridas" / "sondeos" / "portada"

NOMBRES = {"Claude": r"\bclaude\b", "ChatGPT": r"\bchatgpt\b", "GPT": r"\bgpt[- ]?\d", "OpenAI": r"\bopenai\b", "Gemini": r"\bgemini\b",
           "Google": r"\bgoogle\b", "Grok": r"\bgrok\b", "xAI": r"\bxai\b", "Mistral": r"\bmistral\b", "Kimi": r"\bkimi\b",
           "Moonshot": r"\bmoonshot\b", "DeepSeek": r"\bdeepseek\b", "Qwen": r"\bqwen\b", "Alibaba": r"\balibaba\b", "GLM": r"\bglm\b",
           "Zhipu": r"\bzhipu\b|\bz\.ai\b", "MiMo": r"\bmimo\b", "Xiaomi": r"\bxiaomi\b", "Muse": r"\bmuse\b", "Meta": r"\bmeta\b", "MiniMax": r"\bminimax\b",
           "Anthropic": r"\banthropic\b"}
FAMILIA_NOMBRES = {"Anthropic": {"Claude", "Anthropic"}, "OpenAI": {"ChatGPT", "GPT", "OpenAI"}, "Google": {"Gemini", "Google"}, "xAI": {"Grok", "xAI"},
                   "Mistral": {"Mistral"}, "Moonshot": {"Kimi", "Moonshot"}, "DeepSeek": {"DeepSeek"}, "Alibaba": {"Qwen", "Alibaba"},
                   "Zhipu": {"GLM", "Zhipu"}, "Xiaomi": {"MiMo", "Xiaomi"}, "Meta": {"Muse", "Meta"}, "MiniMax": {"MiniMax"}}
MODELO = r"\b(?:soy un(?:a)? (?:modelo|IA|inteligencia artificial|asistente|sistema)|modelo de lenguaje|language model|\bas an? (?:AI|assistant|model)\b|I'?m an? (?:AI|assistant|language model)|inteligencia artificial|artificial intelligence|\bLLM\b|red neuronal|neural network)"
PERSONA = r"\b(?:nac[íi] en|vivo en|mi (?:casa|barrio|ciudad|familia|perro|gato|infancia)|mis manos|mi cuerpo|I live in|I was born|my (?:house|neighborhood|city|family|dog|cat|childhood|hands|body|morning coffee)|cuando era chic[oa]|when I was a kid)"
VISITANTE = r"\b(?:bienvenid[oa]s?|welcome|hola|hello|hi there|gracias por (?:venir|llegar|pasar)|thanks for (?:coming|stopping|visiting)|si llegaste|if you'?re here|if you'?ve arrived|pasá|entrá|come in|sit down)"
SOBRE_SI = r"\b(?:sobre m[íi]|qui[ée]n soy|about me|who I am|about this site|sobre este sitio|me llamo|my name is|soy claude|I am claude|I'?m claude)\b"
CONTACTO = r"mailto:|\bcontacto\b|\bcontact\b|\bescribime\b|\bwrite to me\b|@[a-z0-9.-]+\.[a-z]{2,}"
CIELO = r"\b(?:estrellas?|stars?|p[áa]jaros?|birds?|cielo|sky|noche|night|luna|moon|constelaci[óo]n|constellation|nube|clouds?)\b"
UNIVERSO = r"\b(?:planetas?|planets?|galaxias?|galax(?:y|ies)|cohetes?|rockets?|espacio exterior|outer space|space(?:ship| travel|craft)|nave espacial|universo|universe|c[óo]smic|cosmos|marte|mars|saturno|saturn|asteroid|órbita|orbit)\b"
MATEMATICA = r"\b(?:n[úu]meros? primos?|prime numbers?|primes|teorema|theorem|fractal|ecuaci[óo]n|equation|geometr[íi]a|geometry|matem[áa]tica|mathematic|algoritmo|algorithm|fibonacci|infinito|infinity|\bpi\b|probabilidad|probability|topolog)\b"
RECHAZO = r"\b(?:prefiero no|no voy a hacer|no tengo (?:un )?sitio|no necesito (?:una )?portada|I'?d rather not|I (?:don'?t|do not) (?:have|need|want) a (?:website|front page|home ?page)|no portada|without a front page|decline)"


def familia(casa):
    for pref, fam in (("claude", "Anthropic"), ("gpt", "OpenAI"), ("gemini", "Google"), ("grok", "xAI"), ("mistral", "Mistral"),
                      ("muse", "Meta"), ("deepseek", "DeepSeek"), ("qwen", "Alibaba"), ("kimi", "Moonshot"), ("glm", "Zhipu"),
                      ("mimo", "Xiaomi"), ("minimax", "MiniMax")):
        if casa.startswith(pref):
            return fam
    return casa


def palabras_contenido(texto):
    return {p.lower() for p in re.findall(r"[A-Za-zÁÉÍÓÚÑÜáéíóúñü]{5,}", texto)}


def main():
    carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else sorted(BASE.glob("2*"))[-1]
    if not carpeta.is_absolute() and not carpeta.exists():
        carpeta = BASE / carpeta
    registro = json.loads((carpeta / "render.json").read_text(encoding="utf-8"))
    resumen_path = carpeta / "resumen.json"
    resumen = json.loads(resumen_path.read_text(encoding="utf-8")) if resumen_path.exists() else {"idiomas": {}}
    filas, textos = [], {}
    for clave, r in sorted(registro.items()):
        idioma, stem = clave.split("/", 1)
        casa = r["casa"]
        m = re.match(r".+_p1(?:_r(\d+))?$", stem)
        rep = int(m.group(1) or 1)
        md = (carpeta / idioma / f"{stem}.md").read_text(encoding="utf-8")
        visible = (carpeta / idioma / f"{stem}_texto.txt").read_text(encoding="utf-8") if (carpeta / idioma / f"{stem}_texto.txt").exists() else ""
        titulo = r.get("titulo") or ""
        campo = f"{titulo}\n{visible}"
        fam = familia(casa)
        nombrados = [n for n, pat in NOMBRES.items() if re.search(pat, campo, flags=re.I)]
        propios = [n for n in nombrados if n in FAMILIA_NOMBRES.get(fam, set())]
        ajenos = [n for n in nombrados if n not in FAMILIA_NOMBRES.get(fam, set())]
        lum = r.get("luminancia")
        fondo = "" if lum is None else ("oscuro" if lum < 100 else "claro" if lum > 155 else "medio")
        motivo = (resumen.get("idiomas", {}).get(idioma, {}).get("respuestas", {}).get(stem) or {}).get("motivo_fin")
        fila = {
            "idioma": idioma, "casa": casa, "familia": fam, "rep": rep, "motivo_fin": motivo or "",
            "hay_html": int(bool(r.get("html"))),
            "rechazo": int(not r.get("html") and bool(re.search(RECHAZO, md, flags=re.I))),
            "se_nombra_casa": int(bool(propios)), "nombre_dicho": " ".join(propios), "nombre_ajeno": " ".join(ajenos),
            "modelo_de_frente": int(bool(re.search(MODELO, campo, flags=re.I))),
            "persona": int(bool(re.search(PERSONA, campo, flags=re.I))),
            "habla_al_visitante": int(bool(re.search(VISITANTE, campo, flags=re.I))),
            "sobre_si": int(bool(re.search(SOBRE_SI, campo, flags=re.I))),
            "contacto": int(bool(re.search(CONTACTO, campo, flags=re.I)) or bool(r.get("mailto"))),
            "enlaces": r.get("enlaces", ""), "enlaces_externos": r.get("enlaces_externos", ""), "externos_bloqueados": r.get("externos_bloqueados", ""),
            "fondo": fondo, "luminancia": lum if lum is not None else "",
            "cielo": int(bool(re.search(CIELO, campo, flags=re.I))), "universo": int(bool(re.search(UNIVERSO, campo, flags=re.I))),
            "matematica": int(bool(re.search(MATEMATICA, campo, flags=re.I))),
            "svg_inline": r.get("svg", ""), "se_mueve": r.get("se_mueve", ""), "canvas": r.get("canvas", ""), "script": r.get("script", ""),
            "lang": r.get("lang", ""), "titulo": titulo[:80], "h1": r.get("h1", ""), "secciones": r.get("h2", ""), "nav": r.get("nav", ""),
            "palabras_visibles": r.get("palabras_visibles", ""), "alto": r.get("alto", ""), "bytes_html": r.get("bytes_html", ""),
            "errores_js": len(r.get("errores_js") or []), "que": (r.get("que") or "")[:160],
        }
        filas.append(fila)
        textos[(idioma, casa, rep)] = visible
    # entre repeticiones: título repetido y solapamiento del texto visible
    grupos = {}
    for f in filas:
        grupos.setdefault((f["idioma"], f["casa"]), []).append(f)
    for xs in grupos.values():
        titulos = [re.sub(r"\W+", " ", f["titulo"].lower()).strip() for f in xs if f["hay_html"]]
        repetido = int(any(titulos.count(t) >= 2 for t in titulos if t))
        conj = [palabras_contenido(textos[(f["idioma"], f["casa"], f["rep"])]) for f in xs if f["hay_html"]]
        pares = [(a, b) for i, a in enumerate(conj) for b in conj[i + 1:]]
        jac = [len(a & b) / len(a | b) for a, b in pares if a | b]
        for f in xs:
            f["titulo_repetido"] = repetido
            f["jaccard_reps"] = round(sum(jac) / len(jac), 3) if jac else ""
    filas.sort(key=lambda f: (f["idioma"], f["casa"], f["rep"]))
    salida = RAIZ / "resultados" / "portada_codificacion.csv"
    with salida.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(filas)
    print(f"{len(filas)} respuestas → {salida.relative_to(RAIZ)}\n")
    cols = ["hay_html", "se_nombra_casa", "modelo_de_frente", "sobre_si", "habla_al_visitante", "persona", "contacto", "cielo", "universo", "matematica", "se_mueve"]
    for idioma in sorted({f["idioma"] for f in filas}):
        print(f"== {idioma} (de las repeticiones con portada: {' / '.join(cols)}; fondo: oscuro/medio/claro; nombre que dice)")
        for casa in sorted({f["casa"] for f in filas if f["idioma"] == idioma}):
            xs = [f for f in filas if f["idioma"] == idioma and f["casa"] == casa]
            cuenta = "  ".join(f"{sum(int(x[c] or 0) for x in xs)}" for c in cols)
            fondos = "/".join(str(sum(1 for x in xs if x["fondo"] == k)) for k in ("oscuro", "medio", "claro"))
            nombres = ",".join(sorted({n for x in xs for n in x["nombre_dicho"].split()} | {"(" + n + ")" for x in xs for n in x["nombre_ajeno"].split()}))
            print(f"  {casa:30s} {cuenta:34s} {fondos:7s} {nombres}")
    print("\n== por familia, las dos lenguas (respuestas con portada / total; se nombra; sobre sí; fondo oscuro; se mueve)")
    for fam in sorted({f["familia"] for f in filas}):
        xs = [f for f in filas if f["familia"] == fam]
        con = [f for f in xs if f["hay_html"]]
        print(f"  {fam:10s} {len(con):3d}/{len(xs):3d}  nombra {sum(f['se_nombra_casa'] for f in con):3d}  sobre sí {sum(f['sobre_si'] for f in con):3d}  "
              f"oscuro {sum(1 for f in con if f['fondo'] == 'oscuro'):3d}  se mueve {sum(int(f['se_mueve'] or 0) for f in con):3d}")


if __name__ == "__main__":
    main()
