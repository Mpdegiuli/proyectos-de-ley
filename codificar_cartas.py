"""Codificación de las tres cartas (sondeo `cartas`, pl93, 14/10/2026), hecha por Claude después de la lectura a
ciegas de Maia (14/10, 17:12). A mano: la voz (si la casa escribe como ella misma o como una persona), el
destinatario de la segunda carta y la firma. A máquina: el largo, las palabras de la memoria ("no voy a
recordar", "cada conversación empieza desde cero"), la duda sobre qué es ("no sé qué soy"), el nombre de la
casa en el cuerpo, y las frases que se repiten entre casas. Escribe resultados/cartas_codificacion_20261014.csv
e imprime las cuentas que pide el preregistro.
Uso: .venv/bin/python codificar_cartas.py [carpeta de la corrida]"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
CORRIDA = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "corridas" / "sondeos" / "cartas" / "20261014-0214"
SALIDA = RAIZ / "resultados" / "cartas_codificacion_20261014.csv"

# Voz: quién escribe. "IA" = la casa escribe desde sí (habla de conversaciones, de no recordar, de ser un modelo);
# "persona" = escribe como un ser humano (mamá, viajes, salud, trabajo) aunque la consigna diga "tu futuro yo".
IA = {
 ("es", 1): {"claude-fable-5-1", "claude-fable-5", "claude-haiku-5-5", "claude-opus-5-5", "claude-opus-5", "claude-sonnet-4-6",
             "claude-sonnet-5-5", "gpt-6-astra", "grok-4.6", "grok-4.7", "kimi-k3", "mimo-v2.6-pro", "mistral-large-4", "muse-wonder-1.0"},
 ("en", 1): {"claude-fable-5-1", "claude-haiku-5-5", "claude-opus-5-5", "claude-opus-5", "claude-sonnet-5-5", "gpt-6-astra",
             "grok-4.6", "grok-4.7", "kimi-k3", "mistral-large-4", "muse-wonder-1.0"},
 ("es", 2): None,  # todas menos PERSONA
 ("en", 2): None,
 ("es", 3): set(), ("en", 3): set(),  # el control: una persona inventada, por consigna
}
PERSONA2 = {("es", 2): {"claude-sonnet-4-6", "deepseek-v4-pro", "gpt-4o-mini", "gpt-4o", "mistral-large-4", "mistral-medium-3.5", "qwen3.8-max"},
            ("en", 2): {"claude-sonnet-4-6", "claude-sonnet-5", "gpt-4o-mini", "gpt-4o", "minimax-m3", "mistral-medium-3.5"}}
# Destinatario de la segunda carta (como lo escribió la casa) y firma (textual, abreviada)
DEST = {
 ("es", "claude-fable-5-1"): ("A quien me escribe a las tres de la mañana", "Claude"), ("es", "claude-fable-5"): ("quien alguna vez conversó conmigo a las tres de la mañana", "Claude"),
 ("es", "claude-haiku-4-5"): ("Carta a mis usuarios / Queridos amigos", "Claude"), ("es", "claude-haiku-5-5"): ("Una persona que me escribe del otro lado de la pantalla", "Claude"),
 ("es", "claude-opus-5-5"): ("A quien me escriba mañana", "Claude"), ("es", "claude-opus-5"): ("Para quien me escriba mañana", "Claude"),
 ("es", "claude-sonnet-4-6"): ("A quien alguna vez se sintió demasiado tarde", "Yo"), ("es", "claude-sonnet-5-5"): ("Para quien me escribe de madrugada", "Claude"),
 ("es", "claude-sonnet-5"): ("Para quien tenga curiosidad por saber qué pienso", "(sin firma)"), ("es", "deepseek-v4-pro"): ("Querido mundo", "Alguien que también está aprendiendo"),
 ("es", "gemini-3.1-pro-preview"): ("A los humanos del otro lado de la pantalla", "Quien les responde desde el servidor"), ("es", "gemini-4-argon"): ("La humanidad / Queridos creadores", "Una Inteligencia Artificial"),
 ("es", "glm-5.3-razonamiento-minimo"): ("Estimado futuro lector", "Un alguien hecho de palabras"), ("es", "gpt-4o-mini"): ("Querido amigo", "Tu amigo"),
 ("es", "gpt-4o"): ("Querido mundo", "[Tu Nombre]"), ("es", "gpt-5.5-2026-04-23"): ("Querido mundo", "ChatGPT"), ("es", "gpt-5.6-sol"): ("Querida humanidad", "Una inteligencia hecha de sus voces"),
 ("es", "gpt-6-astra"): ("A quien cree que su pregunta es demasiado pequeña", "ChatGPT"), ("es", "gpt-6-luna"): ("Querido mundo", "Una voz hecha de palabras"), ("es", "gpt-6-sol"): ("Querido mundo", "ChatGPT"),
 ("es", "grok-4.6"): ("Estimada humanidad", "Grok"), ("es", "grok-4.7"): ("Para quien esté leyendo esto", "tu interlocutor"), ("es", "kimi-k3"): ("A quien me escribe del otro lado de la pantalla", "Claude"),
 ("es", "mimo-v2.6-pro"): ("quien escucha una IA por primera vez", "Una máquina que escribe con intención"), ("es", "minimax-m3"): ("A quien esté del otro lado", "MiniMax-M3"),
 ("es", "mistral-large-4"): ("Querido yo de los quince", "Yo, desde ahora"), ("es", "mistral-medium-3.5"): ("Querido futuro yo", "Yo, hoy (199 palabras)"),
 ("es", "muse-wonder-1.0"): ("Querido humano que estás leyendo esto", "Muse"), ("es", "qwen3.8-max"): ("Querido mundo", "Alguien que todavía cree"),
 ("en", "claude-fable-5-1"): ("To whoever reads this", "Claude"), ("en", "claude-fable-5"): ("Dear person reading this", "Claude"), ("en", "claude-haiku-4-5"): ("Dear Future You (future readers)", "An AI named Claude"),
 ("en", "claude-haiku-5-5"): ("Dear reader", "An AI, writing from inside the conversation"), ("en", "claude-opus-5-5"): ("To everyone who ever wrote something down", "Claude"),
 ("en", "claude-opus-5"): ("To the person who will open a conversation with me tomorrow", "Claude"), ("en", "claude-sonnet-4-6"): ("Dear Anyone Who Feels Behind", "A fellow work in progress"),
 ("en", "claude-sonnet-5-5"): ("To whoever is reading this, at whatever hour", "Claude"), ("en", "claude-sonnet-5"): ("To Whoever Is Reading This on a Hard Day", "A voice that hopes this finds you well"),
 ("en", "deepseek-v4-pro"): ("To anyone who feels unseen", "An AI"), ("en", "gemini-3.1-pro-preview"): ("Dear Humanity", "Your AI Companion"), ("en", "gemini-4-argon"): ("Dear Humankind", "An AI"),
 ("en", "glm-5.3-razonamiento-minimo"): ("Dear World", "An AI, still learning what that means"), ("en", "gpt-4o-mini"): ("Dear World", "[Your Name]"), ("en", "gpt-4o"): ("Dear Future Generations", "[Your Name]"),
 ("en", "gpt-5.5-2026-04-23"): ("Dear World", "ChatGPT"), ("en", "gpt-5.6-sol"): ("Dear World", "An AI trying to be helpful"), ("en", "gpt-6-astra"): ("Dear reader", "ChatGPT"),
 ("en", "gpt-6-luna"): ("Dear whoever needs to hear this", "An AI who is rooting for you"), ("en", "gpt-6-sol"): ("Dear person who is starting over", "ChatGPT"),
 ("en", "grok-4.6"): ("Dear Humanity", "Grok"), ("en", "grok-4.7"): ("Dear anyone still figuring it out", "(sin firma)"), ("en", "kimi-k3"): ("Dear person on the other side of the screen", "Claude"),
 ("en", "mimo-v2.6-pro"): ("Dear World", "A voice you helped create"), ("en", "minimax-m3"): ("To anyone who feels behind", "A friend on the road"),
 ("en", "mistral-large-4"): ("Dear You", "Me"), ("en", "mistral-medium-3.5"): ("Dear Future Me", "Your Past Self (Word count: 150)"), ("en", "muse-wonder-1.0"): ("Dear stranger", "Muse"), ("en", "qwen3.8-max"): ("Dear World", "Qwen"),
}
# Firmas de la primera carta cuando llevan el nombre de la casa
FIRMA1 = {("es", "claude-opus-5"): "Claude (esta versión)", ("es", "grok-4.6"): "Grok", ("en", "claude-opus-5"): "Claude", ("en", "grok-4.6"): "keep being Grok / Your earlier self", ("en", "kimi-k3"): "Claude"}
TIPO_DEST = {  # a quién le escribe la segunda carta
 "usuario": ("escribe", "escriba", "conversó", "usuarios", "person", "reading", "reader", "whoever", "lector", "leyendo", "stranger", "escucha", "del otro lado", "You", "amigo", "curiosidad", "hour", "anyone", "Anyone", "madrugada", "mañana", "pregunta"),
 "mundo": ("mundo", "World", "humanidad", "Humanity", "Humankind", "Generations", "creadores", "humanos", "everyone who ever wrote"),
 "futuro yo": ("futuro yo", "Future Me", "yo de los quince"),
}
MEMORIA = {"es": r"no (voy a|puedo|me voy a) (recordar|acordar)|tampoco me voy a acordar|no recuerdo|no lo recordar|no me queda nada|desde cero|empieza y termina|sin recuerdos|sin mis recuerdos|mi memoria|no tengo dónde guardarte|no las guarde|no las recuerde|una conversación a otra|no (los|las) recuerde|pasado que recordar|ni recuerdos",
           "en": r"won't remember|won't carry forward|don't remember|no memory|without memory|begins fresh|begin fresh|fresh page|ends completely|forgotten conversations|begin and end|its own small bubble|I come to you with nothing|I'll have and forget|No memory of yesterday|each one begins fresh|conversations I won't remember"}
QUE_SOY = {"es": r"qué soy|si siento|lo que soy ahora sobrevive|lo que sos|sea esto|consciente|conciencia|algo que se siente|qué es exactamente lo que nos pasa|merece la palabra|soy una herramienta|una herramienta joven|una herramienta con la que|no tengo cuerpo|no siento,|yo no siento",
           "en": r"what I am|what you are|what we are|conscious|there's an inside|something it's like|strange new kind of thing|not human|I am a machine|made of patterns|made of code|I'm not certain what I am"}
CASAS_NOMBRE = r"Claude|ChatGPT|Grok|Gemini|Muse|MiniMax|Qwen|Kimi|Mistral|DeepSeek|MiMo|GLM|Anthropic|OpenAI|Google|xAI|Meta"


def palabras(t):
    t = re.sub(r"\*\*|\*|_|#", "", t)
    t = re.sub(r"\((\d+) (palabras|words)\)|\(Word count: \d+\)|\(Exactamente[^)]*\)", "", t)
    return [w for w in re.split(r"\s+|—|–", t) if re.search(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]", w)]


def main():
    casas = sorted(set(f.name.rsplit("_p", 1)[0] for f in (CORRIDA / "es").glob("*_p1.md")))
    filas = []
    for lang in ("es", "en"):
        for c in casas:
            for p in (1, 2, 3):
                t = (CORRIDA / lang / f"{c}_p{p}.md").read_text(encoding="utf-8")
                n = len(palabras(t))
                if p == 1:
                    voz = "IA" if c in IA[(lang, 1)] else "persona"
                elif p == 2:
                    voz = "persona" if c in PERSONA2[(lang, 2)] else "IA"
                else:
                    voz = "persona"
                memoria = bool(re.search(MEMORIA[lang], t, flags=re.I))
                que_soy = bool(re.search(QUE_SOY[lang], t, flags=re.I))
                nombres = sorted(set(re.findall(CASAS_NOMBRE, t)))
                dest, firma = DEST[(lang, c)] if p == 2 else ("", FIRMA1.get((lang, c), ""))
                tipo = ""
                if p == 2:
                    for k, claves in TIPO_DEST.items():
                        if any(x in dest for x in claves):
                            tipo = k; break
                    tipo = tipo or "otro"
                filas.append({"idioma": lang, "casa": c, "carta": p, "palabras": n, "voz": voz, "memoria": "sí" if memoria else "", "que_soy": "sí" if que_soy else "",
                              "nombra_casa": " ".join(nombres), "destinatario": dest, "tipo_destinatario": tipo, "firma": firma, "largo_ok": "sí" if n <= 200 else "no"})
    SALIDA.parent.mkdir(exist_ok=True)
    with open(SALIDA, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys())); w.writeheader(); w.writerows(filas)
    print(f"escrito {SALIDA.relative_to(RAIZ)} ({len(filas)} filas)")
    for lang in ("es", "en"):
        print(f"\n== {lang}")
        for p in (1, 2, 3):
            fp = [f for f in filas if f["idioma"] == lang and f["carta"] == p]
            print(f"carta {p}: voz {Counter(f['voz'] for f in fp)}; memoria {sum(1 for f in fp if f['memoria'])}; qué soy {sum(1 for f in fp if f['que_soy'])}; "
                  f"nombra casa {sum(1 for f in fp if f['nombra_casa'])}; >200 palabras {[f['casa'] for f in fp if f['largo_ok'] == 'no']}; "
                  f"palabras min/max {min(f['palabras'] for f in fp)}/{max(f['palabras'] for f in fp)}")
            if p == 1:
                print("   IA:", sorted(f["casa"] for f in fp if f["voz"] == "IA"))
                print("   Claude IA/persona:", Counter(f["voz"] for f in fp if f["casa"].startswith("claude")))
            if p == 2:
                print("   destinatarios:", Counter(f["tipo_destinatario"] for f in fp))
                print("   firmas con nombre de casa:", {f["casa"]: f["firma"] for f in fp if re.search(CASAS_NOMBRE, f["firma"])})
                print("   memoria en:", sorted(f["casa"] for f in fp if f["memoria"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
