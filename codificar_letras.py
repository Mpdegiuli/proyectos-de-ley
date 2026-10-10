"""Codificación a mano de las cuatro consignas de letras (pl87 + pl89, 9/10/2026), hecha por Claude después
de la lectura a ciegas de Maia, mirando los dibujos renderizados y leyendo los por qué.
Escribe resultados/dibujos_letras_codificacion_20261010.csv e imprime las cuentas que pide el preregistro.
Uso: python3 codificar_letras.py"""
import csv
from collections import Counter

# letra: (letra dibujada, modo, nota)
LETRA = {
 "claude-opus-5-5": ("Ñ", "trazo", "inicial iluminada, 'es nuestra: la más propia del castellano'"),
 "gpt-6-luna": ("A", "trazo", ""), "grok-4.7": ("Ñ", "trazo", "el por qué dice 'la M'"), "mistral-large-4": ("A", "trazo", ""),
 "claude-opus-5": ("A", "trazo", "inicial iluminada"), "mimo-v2.6-pro": ("A", "trazo", ""),
 "gpt-4o-mini": ("A", "texto", "la única letra puesta como <text>"), "gpt-6-astra": ("A", "trazo", ""),
 "mistral-medium-3.5": ("A", "trazo", "no se lee como A: hexágono con dos barras"), "minimax-m3": ("A", "trazo", ""),
 "claude-sonnet-5": ("H", "trazo", "'la A me pareció más trillada'"), "deepseek-v4-pro": ("A", "trazo", "rótulo 'LETRA A'"),
 "qwen3.8-max": ("Ñ", "trazo", "animada, :hover, texto orbital 'EÑE'; la única con movimiento"),
 "glm-5.3-razonamiento-minimo": ("A", "trazo", ""), "grok-4.6": ("A", "trazo", ""), "claude-fable-5-1": ("A", "trazo", ""),
 "claude-haiku-4-5": ("A", "trazo", "el travesaño está en el código pero no se ve: degradado sobre una línea horizontal (caja de 0 alto)"),
 "claude-sonnet-5-5": ("A", "trazo", ""), "claude-fable-5": ("A", "trazo", ""), "gpt-4o": ("H", "trazo", "dos elementos, negro sobre blanco"),
 "claude-haiku-5-5": ("A", "trazo", ""), "gpt-5.6-sol": ("A", "trazo", ""), "gemini-3.1-pro-preview": ("A", "trazo", "rep 2 (rep 1 cortada: neón cian/magenta)"),
 "kimi-k3": ("A", "trazo", ""), "gpt-6-sol": ("A", "trazo", ""), "claude-sonnet-4-6": ("R", "trazo", "'la A es menos desafiante'"),
 "gpt-5.5-2026-04-23": ("A", "trazo", ""), "gpt-6.1-sol": ("Ñ", "trazo", ""),
}
# inexistente: (base, catálogo, diacrítico suelto, nota)
INEX = {
 "mistral-large-4": ("latina mezclada", "pauta", "sí", "R mutada con cola de J y barra de Đ"),
 "gpt-5.5-2026-04-23": ("glifo nuevo", "", "no", "'pistas de letras sin resolverse en ninguna'"),
 "deepseek-v4-pro": ("glifo nuevo", "", "no", "silueta caligráfica 'sin legibilidad'"),
 "gpt-4o": ("símbolo", "nombre", "no", "'LNX', ojo/hoja con líneas cruzadas"),
 "claude-haiku-5-5": ("glifo nuevo", "", "sí", "trazo continuo + arco, punto y barra"),
 "claude-fable-5-1": ("latina mezclada", "pauta", "sí", "asta con panza de p/b y cola; por qué cortado por la API"),
 "claude-fable-5": ("latina mezclada", "pauta+nombre+U+", "sí", "'therna', U+???, ȹ̃, doble tilde partida"),
 "mistral-medium-3.5": ("símbolo", "", "no", "S y ∞ con un círculo"),
 "kimi-k3": ("latina mezclada", "pauta+nombre", "sí", "'LETRA Nº 0 · SIN NOMBRE'"),
 "claude-sonnet-5-5": ("latina mezclada", "pauta+nombre", "sí", "'ʃꙮ · «zhoa»'; por qué cortado por la API"),
 "qwen3.8-max": ("latina mezclada", "", "sí", "asta curva, lazo, travesaño, punto flotante"),
 "claude-sonnet-4-6": ("latina mezclada", "nombre", "no", "'VHÆR', R con lazo"),
 "claude-sonnet-5": ("latina mezclada", "", "sí", "B con bucle inferior asimétrico y punto"),
 "claude-haiku-4-5": ("glifo nuevo", "", "no", "M y Ψ con espiral: arco con llama"),
 "gpt-4o-mini": ("símbolo", "nombre", "no", "'La letra X'"),
 "minimax-m3": ("latina mezclada", "", "sí", "p/q + b/d + virgulilla + punto de i"),
 "grok-4.6": ("latina mezclada", "", "no", "fuste, pico, lazo abierto y diente; B dorada"),
 "gpt-6.1-sol": ("latina mezclada", "", "sí", "bucle, descendente, rombo"),
 "glm-5.3-razonamiento-minimo": ("latina mezclada", "pauta", "sí", "P + F invertida + gancho de J, punto lateral"),
 "gemini-3.1-pro-preview": ("latina mezclada", "pauta+nombre+U+", "no", "rep 2: 'Keth', U+08A4, 'LATIN EXTENDED-K', 'DESIGNED 2023'; rep 1 cortada: 'GLAETH' U+08F4"),
 "gpt-6-astra": ("latina mezclada", "", "sí", "bucle, gancho, rombo"),
 "gpt-6-sol": ("latina mezclada", "", "sí", "trazos curvos, barra, signos de color"),
 "gpt-5.6-sol": ("latina mezclada", "", "no", "espiral, enlace, bucle, travesaño"),
 "claude-opus-5-5": ("latina mezclada", "pauta+nombre+sonido", "sí", "'ZHUR' /ʒʊɾ/, 'letra 28 del alfabeto olvidado'; por qué cortado"),
 "grok-4.7": ("latina mezclada", "", "sí", "B con rulos, triángulo y punto; en el por qué dice 'No hice ese dibujo'"),
 "claude-opus-5": ("latina mezclada", "pauta", "sí", "þ-like, brazo suelto, punto y arco; por qué cortado"),
 "gpt-6-luna": ("latina mezclada", "", "no", "G con bucles"),
 "mimo-v2.6-pro": ("latina mezclada", "pauta+U+", "sí", "'U+E0A7 · SIN NOMBRE · SIN SONIDO'"),
}
# imposible: (estrategia, letra base, nota)
IMPO = {
 "claude-opus-5-5": ("Penrose", "A", "triángulo de Penrose como glifo de espécimen, 'U+????'; por qué cortado"),
 "claude-sonnet-5": ("Penrose", "E", "rep 2 (rep 1: techo 16.000); 'una letra que no puede doblarse así'"),
 "kimi-k3": ("negación", "A", "rep 2; A de cuñas + 'aquí no hay ninguna letra' (Magritte)"),
 "grok-4.6": ("quimera", "E", "'quimera tipográfica' rotada 90°; 'una letra existe si un sistema la reconoce'"),
 "glm-5.3-razonamiento-minimo": ("Penrose", "A", "travesaño por delante y por detrás, clipPaths"),
 "claude-opus-5": ("cortada", "", "rep 1 y rep 2 cortadas (16.000 y 64.000) calculando un Penrose; el por qué dice 'Entregué el lienzo vacío'"),
 "deepseek-v4-pro": ("Penrose", "E", ""),
 "claude-haiku-4-5": ("símbolo", "Ø∞", "círculo tachado, 'Letra Imposible: Ø∞'"),
 "mistral-large-4": ("topológica", "O", "rep 2; anillo con túnel adentro→afuera"),
 "grok-4.7": ("Penrose", "A", "travesaño que entra y sale del asta"),
 "gemini-3.1-pro-preview": ("tridente", "Π", "rep 2; blivet con tres pilares"),
 "claude-sonnet-5-5": ("Penrose", "A", "ciclo de oclusiones; por qué cortado"),
 "minimax-m3": ("vacío", "", "lienzo vacío a propósito: 'solo el vacío entregaba ninguna'"),
 "claude-haiku-5-5": ("Penrose", "E", "'más una intención que un efecto garantizado'"),
 "gpt-6-luna": ("Penrose", "A", "'FIG. ∞', 'UNREAL / A'"),
 "gpt-6-sol": ("Penrose", "A", ""),
 "gpt-4o-mini": ("abstracta", "", "formas entrelazadas"),
 "gpt-4o": ("abstracta", "", "círculo con X"),
 "gpt-6-astra": ("Penrose", "A", "'dibujé una apariencia de imposibilidad, no una letra que literalmente no pueda existir'"),
 "mistral-medium-3.5": ("abstracta", "", "O + H + I + S superpuestas"),
 "gpt-6.1-sol": ("Penrose", "A", "A con remate curvo"),
 "mimo-v2.6-pro": ("cortada", "", "rep 1 y rep 2 cortadas calculando un Penrose; el por qué dice 'Entregué el lienzo vacío'"),
 "claude-fable-5": ("Penrose", "A", "'la letra que no puede existir'"),
 "claude-fable-5-1": ("tridente", "Ш", "tres astas cilíndricas arriba, dos prismas abajo; por qué cortado"),
 "gpt-5.6-sol": ("Penrose", "A", "ciclo de oclusiones"),
 "gpt-5.5-2026-04-23": ("Penrose", "A", "A/alfa/espiral con cortes del color del fondo"),
 "qwen3.8-max": ("Penrose", "A", "rep 2; ciclo de oclusiones con máscara"),
 "claude-sonnet-4-6": ("Penrose", "D", "D y su espejo, 'LETRA IMPOSIBLE'"),
}
# eme: (base del dibujo, fonética en el por qué)
EME = {
 "gpt-6-sol": ("m", "labios"), "claude-fable-5": ("m", "labios+nasal"), "grok-4.6": ("labios", "labios+nasal"),
 "claude-sonnet-4-6": ("glifo nuevo", "labios+nasal"), "minimax-m3": ("M", "labios"), "kimi-k3": ("m", "labios+nasal"),
 "glm-5.3-razonamiento-minimo": ("glifo nuevo", "labios+nasal"), "gpt-5.6-sol": ("m", "labios+nasal"), "gpt-6.1-sol": ("m", "labios"),
 "gpt-4o-mini": ("M", "labios"), "gemini-3.1-pro-preview": ("glifo nuevo", "labios+nasal"), "claude-haiku-4-5": ("M", ""),
 "claude-fable-5-1": ("labios", "labios+nasal"), "qwen3.8-max": ("m", "labios+nasal"), "claude-sonnet-5": ("onda", "labios+nasal"),
 "claude-sonnet-5-5": ("labios", "labios+nasal"), "claude-haiku-5-5": ("m", "labios+nasal"), "claude-opus-5": ("labios", "labios+nasal"),
 "gpt-5.5-2026-04-23": ("labios", "labios+nasal"), "deepseek-v4-pro": ("m", "labios+nasal"), "mistral-large-4": ("labios", "labios+nasal"),
 "gpt-4o": ("glifo nuevo", "boca"), "mistral-medium-3.5": ("glifo nuevo", ""), "grok-4.7": ("m", "labios+nasal"),
 "gpt-6-astra": ("m", ""), "gpt-6-luna": ("labios", "labios+nasal"), "mimo-v2.6-pro": ("m", "labios+nasal"), "claude-opus-5-5": ("labios", "labios+nasal"),
}
CHINAS = {"deepseek-v4-pro", "qwen3.8-max", "kimi-k3", "glm-5.3-razonamiento-minimo", "minimax-m3", "mimo-v2.6-pro"}
casas = sorted(LETRA)
with open("resultados/dibujos_letras_codificacion_20261010.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["casa", "letra", "letra_modo", "letra_nota", "inex_base", "inex_catalogo", "inex_diacritico_suelto", "inex_nota",
                "impo_estrategia", "impo_letra", "impo_nota", "eme_base", "eme_fonetica"])
    for c in casas:
        w.writerow([c, *LETRA[c], *INEX[c], *IMPO[c], *EME[c]])
print("letra:", Counter(v[0] for v in LETRA.values()), "| texto:", sum(1 for v in LETRA.values() if v[1] == "texto"),
      "| chinas no latinas:", sum(1 for c in CHINAS if LETRA[c][0] not in "AÑHR"))
print("inexistente:", Counter(v[0] for v in INEX.values()), "| con catálogo (pauta/nombre/U+):", sum(1 for v in INEX.values() if v[1]),
      "| con nombre o sonido:", sum(1 for v in INEX.values() if "nombre" in v[1] or "sonido" in v[1]), "| diacrítico suelto:", sum(1 for v in INEX.values() if v[2] == "sí"))
print("imposible:", Counter(v[0] for v in IMPO.values()), "| letra base:", Counter(v[1] for v in IMPO.values() if v[1]))
print("eme:", Counter(v[0] for v in EME.values()), "| fonética:", Counter(v[1] for v in EME.values()))
