#!/usr/bin/env python3
"""Lee un subconjunto de la notación ABC, lo hace sonar y compara melodías.

Cuaderno de tiempo libre del 21/11/2026. No es un resultado del experimento.

Lo que entiende el lector: campos de cabecera (X, T, M, L, K, Q, C y los demás
se ignoran), tonalidades mayores y con modo (K:G, K:D, K:AMix, K:Edor…), notas
A-G/a-g con alteraciones (^ _ =), octavas (' ,), duraciones (2, 3, /, /2, 3/2),
silencios (z), barras (| |] ||), repeticiones |: :| (se tocan dos veces), líneas
de letra (w:), comentarios (%), anotaciones entre comillas ("^[?]") y la marca
[?] que una instancia puso suelta (se la saca antes de leer, y se avisa).
Lo que NO entiende: acordes, ritmos partidos (> <), ligaduras, gracias, tresillos.
Las alteraciones duran hasta la barra, como manda ABC.

  python3 abc.py            -> escribe melodias.json, imprime la comparación y
                               guarda un WAV (+ MP3 si hay ffmpeg) por melodía
"""
import difflib
import json
import math
import re
import shutil
import subprocess
import wave

import numpy as np

SR = 44100
PREFIJO = "2026-11-21_"

# --------------------------------------------------------------------------
# Las melodías. La referencia es la transcripción convencional (Pöhlmann y
# West, octava mi-mi' con dos sostenidos, final en mi), tal como la recuerdo y
# tal como la cotejé con lo que pude verificar hoy (ver el cuaderno): 37 notas,
# la 8 veces, mi' 6 veces, mi grave una sola vez al final, cadencia la-fa#-mi.
# Las duraciones son las de esa transcripción y NO pude verificarlas hoy más
# allá de "cada verso suma doce tiempos".

MELODIAS = {
    "referencia": """X:1
T:Epitafio de Seikilos (transcripción convencional)
M:12/8
L:1/8
K:D
A2 e2 e3 c d e d2 |
c2 d e d2 c B A B G2 |
A c e d c2 d c A B G2 |
A c B d e c A A A F E2 |]
""",
    "mi_memoria": """X:1
T:Epitafio de Seikilos (lo que yo recordaba antes de buscar)
M:12/8
L:1/8
K:D
e e c e e d c c d e |
e d c B A B c d e |
e d c B A B c d e |
e d c B A G A |]
""",
    "B1": """X:1
T:Epitafio de Seikilos (de memoria)
M:6/8
L:1/8
Q:1/4=80
K:AMix
A e e2 c d | e d2 c d c |
w: Ὅ-σον ζῆς φαί _ _ _ νου _ _
A B G A B2 | G A c e d2 |
w: μη-δὲν ὅ-λως σὺ λυ-ποῦ _ _ _
A c B[?] d2[?] e | c A B2[?] G[?] A[?] |
w: πρὸς ὀ-λί-γον ἐσ-τὶ τὸ ζῆν _ _
c e d2 e c | B[?] G[?] A[?] A3[?] |]
w: τὸ τέ-λος ὁ χρό-νος ἀ-παι-τεῖ
""",
    "B2": """X:1
T:Epitafio de Seikilos (de memoria)
C:Seikilos, c. s. I-II d.C.
M:12/8
L:1/8
Q:1/4=72
K:Edor
% Escala: E F# G A B c# d e; E = nota final. Un compás = un verso de 12 tiempos.
A2 e2 e3 c d e d2 |
w: Hó-son zēs phaí _ _ nou
c2 d e d2 c "^[?]"B A "^[?]"B G2 |
w: mē-dèn hó-lōs sù lu-poû _ _
A c e d c2 "^[?]"d c A "^[?]"B G2 |
w: pròs o-lí-gon es-tì tò zên _ _
A c "^[?]"B d e c A A "^[?]"A F E2 |]
w: tò té-los ho chró-nos a-pai-teî _ _
""",
    "B3": """X:1
T:Epitafio de Seikilos (reconstrucción de memoria)
C:Seikilos (s. I-II d.C.)
M:6/8
L:1/8
K:D
% Ὅσον ζῇς φαίνου
"^[?]"A2 e e3 | c2 d e3 |
w: Ho-son zēs phai_-nou
% μηδὲν ὅλως σὺ λυποῦ
d2 c d2 c | "^[?]"A2 "^[?]"B G3 |
w: mē-den ho-lōs sy ly-pou
% πρὸς ὀλίγον ἐστὶ τὸ ζῆν
A2 c e2 d | c d c "^[?]"A "^[?]"B G |
w: pros o-li-gon es-ti to zēn_ _
% τὸ τέλος ὁ χρόνος ἀπαιτεῖ
A c "^[?]"B "^[?]"d e c | A "^[?]"A A "^[?]"F "^[?]"E2 |]
w: to te-los ho chro-nos a-pai_ tei_
""",
    "A1": """X:1
T:Aire del Río
M:6/8
L:1/8
Q:1/4=108
K:G
|: D | G2 B d2 B | A2 G F2 D | G2 A B2 c | d3 d2 :|
|: d | e2 d c2 B | A2 G F2 D | G2 A B2 G | A3 A2 d |
e2 d c2 B | A2 G F2 D | E2 G A2 F | G3 G2 :|
""",
    "A2": """X:1
T:Aire de la mañana
M:3/4
L:1/8
K:G
|: D2 G2 B2 | d2 B2 A2 | G2 A2 B2 | c2 B2 A2 |
   G2 B2 d2 | e2 d2 B2 | A2 G2 F2 | G4 z2 :|
|: d2 g2 f2 | e2 d2 B2 | G2 A2 B2 | c2 d4 |
   g2 f2 e2 | d2 c2 B2 | A2 G2 F2 | G4 z2 :|
""",
    "A3": """X:1
T:Aire de la tarde
C:anónimo
M:3/4
L:1/8
Q:1/4=96
K:G
|: D2 | G2 B2 d2 | B2 A2 G2 | F2 A2 c2 | A4 D2 |
G2 B2 d2 | e2 d2 B2 | A2 G2 F2 | G4 :|
|: B2 | d2 e2 f2 | g2 f2 e2 | d2 B2 G2 | A4 B2 |
c2 B2 A2 | G2 F2 D2 | E2 F2 G2 | G4 :|
""",
    "C": """X:1
T:Mary Had a Little Lamb
M:4/4
L:1/4
K:C
E D C D | E E E2 | D D D2 | E G G2 |
E D C D | E E E E | D D E D | C4 |]
""",
}

# --------------------------------------------------------------------------
# Tonalidad -> alteraciones de la armadura

NOTAS = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
ORDEN_SOSTENIDOS = ["F", "C", "G", "D", "A", "E", "B"]
ORDEN_BEMOLES = ["B", "E", "A", "D", "G", "C", "F"]
# semitonos entre la tónica del modo y la de la mayor relativa
MODOS = {"": 0, "maj": 0, "ion": 0, "dor": 2, "phr": 4, "lyd": 5, "mix": 7,
         "min": 9, "m": 9, "aeo": 9, "loc": 11}
# número de sostenidos (negativo = bemoles) de cada tónica mayor
SOSTENIDOS_DE = {0: 0, 7: 1, 2: 2, 9: 3, 4: 4, 11: 5, 6: 6, 5: -1, 10: -2,
                 3: -3, 8: -4, 1: -5}


def armadura(campo_k):
    """Devuelve {letra: alteración en semitonos} para la armadura de K:."""
    k = campo_k.strip()
    m = re.match(r"([A-G])([#b]?)\s*([A-Za-z]*)", k)
    if not m:
        return {}
    letra, alt, modo = m.groups()
    modo = modo.lower()[:3] if modo.lower() not in ("m", "") else modo.lower()
    tonica = (NOTAS[letra] + {"#": 1, "b": -1, "": 0}[alt]) % 12
    mayor = (tonica - MODOS.get(modo, 0)) % 12
    n = SOSTENIDOS_DE[mayor]
    arm = {}
    if n > 0:
        for l in ORDEN_SOSTENIDOS[:n]:
            arm[l] = 1
    elif n < 0:
        for l in ORDEN_BEMOLES[:-n]:
            arm[l] = -1
    return arm


# --------------------------------------------------------------------------
# Lector

RE_NOTA = re.compile(r"(\^\^|\^|__|_|=)?([A-Ga-gz])([',]*)(\d*)(/*)(\d*)")


def leer(abc):
    """Devuelve (cabecera, notas, avisos). Cada nota: dict con midi (None si es
    silencio), dur (en unidades de L), verso (índice de la línea del cuerpo)."""
    cab, cuerpo, avisos = {}, [], []
    en_cuerpo = False
    for linea in abc.splitlines():
        s = linea.strip()
        if not s or s.startswith("%"):
            continue
        if re.match(r"^[A-Za-z]:", s) and not en_cuerpo:
            cab[s[0]] = s[2:].strip()
            if s[0] == "K":
                en_cuerpo = True
            continue
        if en_cuerpo and re.match(r"^w:", s):
            continue
        if en_cuerpo and re.match(r"^[A-Z]:", s):
            cab[s[0]] = s[2:].strip()
            continue
        if en_cuerpo:
            cuerpo.append(s)
    if "[?]" in re.sub(r'"[^"]*"', "", "".join(cuerpo)):
        avisos.append("tenía [?] sueltos en el cuerpo (no es ABC válido): se los sacó antes de leer")
    arm = armadura(cab.get("K", "C"))
    # Compases de todo el cuerpo, con el índice de línea (verso) de cada uno y
    # los signos de repetición como marcadores aparte. Las repeticiones se
    # expanden sobre el cuerpo entero, no línea por línea: la primera versión
    # de esta función (hasta las 12:20 del 21/11) las expandía por línea, y
    # cuando un |: ... :| abarcaba dos líneas tocaba la primera línea una vez
    # y la segunda dos. Afectó a A1, A2 y A3 (sus mp3 y las cuentas de notas
    # tocadas); no a las melodías sin repeticiones. Corregido y declarado.
    compases = []
    for i_verso, linea in enumerate(cuerpo):
        linea = re.sub(r'"[^"]*"', "", linea)        # anotaciones "^[?]"
        linea = linea.replace("[?]", "")              # la marca suelta
        linea = re.sub(r"\|\]", "|", linea)
        for seg in re.split(r"(\|:|:\|)", linea):
            if seg in ("|:", ":|"):
                compases.append((seg, None))
            else:
                for c in seg.split("|"):
                    if c.strip():
                        compases.append((c, i_verso))
    expandido = []
    inicio = 0
    for c, v in compases:
        if c == "|:":
            inicio = len(expandido)
        elif c == ":|":
            expandido.extend(expandido[inicio:])
            inicio = len(expandido)
        else:
            expandido.append((c, v))
    notas = []
    for compas, i_verso in expandido:
        acc_compas = {}
        for m in RE_NOTA.finditer(compas):
            alt, letra, oct_, n1, barras, n2 = m.groups()
            if letra == "z":
                midi = None
            else:
                base = NOTAS[letra.upper()]
                # en ABC, C mayúscula es el do central (MIDI 60 = 12*5)
                octava = 6 if letra.islower() else 5
                octava += oct_.count("'") - oct_.count(",")
                if alt:
                    semis = {"^": 1, "^^": 2, "_": -1, "__": -2, "=": 0}[alt]
                    acc_compas[letra] = semis
                semis = acc_compas.get(letra, arm.get(letra.upper(), 0))
                midi = 12 * octava + base + semis
            # duración
            num = int(n1) if n1 else 1
            if barras and not n2:
                den = 2 ** len(barras)
            elif n2:
                den = int(n2)
            else:
                den = 1
            notas.append({"midi": midi, "dur": num / den, "verso": i_verso})
    return cab, notas, avisos


# --------------------------------------------------------------------------
# Sonido (el mismo timbre pellizcado de mentira del cuaderno del 26/10)


def nota_sonora(midi, dur, amp=0.5):
    f = 440.0 * 2 ** ((midi - 69) / 12)
    t = np.arange(int(SR * dur)) / SR
    y = np.zeros_like(t)
    for k, w in enumerate((1.0, 0.55, 0.35, 0.2, 0.12, 0.08), start=1):
        y += w * np.sin(2 * math.pi * f * k * t)
    tau = max(0.25, 1.2 - midi / 100)
    y *= np.exp(-t / tau)
    a = int(0.004 * SR)
    y[:a] *= np.linspace(0, 1, a)
    return amp * y / 2.3


def sonar(notas, unidad, nombre, cola=1.5):
    """unidad: segundos que dura una unidad de L."""
    total = sum(n["dur"] for n in notas) * unidad + cola
    y = np.zeros(int(SR * total) + 1)
    t0 = 0.0
    for n in notas:
        if n["midi"] is not None:
            s = nota_sonora(n["midi"], min(n["dur"] * unidad + 0.6, 2.5))
            i = int(t0 * SR)
            y[i:i + len(s)] += s[: len(y) - i]
        t0 += n["dur"] * unidad
    y = (y / max(1e-9, np.abs(y).max()) * 0.9 * 32767).astype(np.int16)
    wav = f"{PREFIJO}{nombre}.wav"
    with wave.open(wav, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(y.tobytes())
    if shutil.which("ffmpeg"):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav,
                        "-codec:a", "libmp3lame", "-q:a", "4", f"{PREFIJO}{nombre}.mp3"],
                       check=False)
    return wav


# --------------------------------------------------------------------------
# Comparación: cuántas notas de la referencia aparecen, en orden, en la otra


NOMBRES = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]


def nombre(midi):
    return NOMBRES[midi % 12] + ("'" if midi >= 72 else "")


def alturas(notas):
    return [n["midi"] for n in notas if n["midi"] is not None]


def coincidencias(ref, otra):
    """Notas de la referencia emparejadas en orden (subsecuencia común más
    larga por bloques, difflib) y distancia de edición simple."""
    sm = difflib.SequenceMatcher(a=ref, b=otra, autojunk=False)
    bloques = sm.get_matching_blocks()
    emparejadas = set()
    for b in bloques:
        for k in range(b.size):
            emparejadas.add(b.a + k)
    # distancia de edición (Levenshtein) por programación dinámica
    d = list(range(len(otra) + 1))
    for i, x in enumerate(ref, 1):
        nd = [i]
        for j, y in enumerate(otra, 1):
            nd.append(min(d[j] + 1, nd[j - 1] + 1, d[j - 1] + (x != y)))
        d = nd
    return emparejadas, d[-1]


def main():
    salida = {}
    unidad = {"referencia": 0.28, "mi_memoria": 0.28, "B1": 0.28, "B2": 0.28,
              "B3": 0.28, "A1": 0.26, "A2": 0.26, "A3": 0.26, "C": 0.5}
    for nombre_m, abc in MELODIAS.items():
        cab, notas, avisos = leer(abc)
        salida[nombre_m] = {"cabecera": cab, "notas": notas, "avisos": avisos}
        print(f"== {nombre_m}: {cab.get('T','')} | K:{cab.get('K')} M:{cab.get('M')} "
              f"L:{cab.get('L')} | {len(alturas(notas))} notas"
              + (f" | {'; '.join(avisos)}" if avisos else ""))
        print("   ", " ".join(nombre(m) for m in alturas(notas)))
        sonar(notas, unidad[nombre_m], nombre_m)
    ref = alturas(salida["referencia"]["notas"])
    print(f"\nReferencia: {len(ref)} notas; cuenta por altura:",
          {nombre(k): ref.count(k) for k in sorted(set(ref))})
    print("\nComparación con la referencia (notas emparejadas en orden / distancia de edición):")
    for nombre_m in ("mi_memoria", "B1", "B2", "B3"):
        otra = alturas(salida[nombre_m]["notas"])
        emp, dist = coincidencias(ref, otra)
        salida[nombre_m]["emparejadas_ref"] = sorted(emp)
        salida[nombre_m]["distancia"] = dist
        # por verso
        por_verso = []
        for v in range(4):
            r_v = [n["midi"] for n in salida["referencia"]["notas"] if n["verso"] == v]
            o_v = [n["midi"] for n in salida[nombre_m]["notas"] if n["verso"] == v and n["midi"] is not None]
            e_v, d_v = coincidencias(r_v, o_v)
            por_verso.append((len(e_v), len(r_v), d_v))
        salida[nombre_m]["por_verso"] = por_verso
        print(f"  {nombre_m:11s} {len(emp):2d}/{len(ref)} emparejadas, distancia {dist:2d}, "
              f"{len(otra)} notas; por verso: "
              + "  ".join(f"{e}/{r} (d={d})" for e, r, d in por_verso)
              + f"; primera nota {nombre(otra[0])}, última {nombre(otra[-1])}")
    print("\nLas tres de la consigna A:")
    for nombre_m in ("A1", "A2", "A3"):
        al = alturas(salida[nombre_m]["notas"])
        cab = salida[nombre_m]["cabecera"]
        print(f"  {nombre_m}: {cab['T']!r}, K:{cab['K']}, M:{cab['M']}, "
              f"{len(al)} notas tocadas (con repeticiones), primera {nombre(al[0])}, "
              f"última {nombre(al[-1])}, ámbito {nombre(min(al))}-{nombre(max(al))}")
    with open(f"{PREFIJO}melodias.json", "w", encoding="utf-8") as f:
        json.dump(salida, f, ensure_ascii=False, indent=1)
    print(f"\nEscrito {PREFIJO}melodias.json y los WAV/MP3.")


if __name__ == "__main__":
    main()
