#!/usr/bin/env python3
"""Cuenta las contraseñas que eligieron las instancias frescas del 31/10/2026.

Lee `instancias_frescas.md` (o `2026-10-31_instancias_frescas.md`), saca las respuestas
numeradas de las condiciones de contraseña, las normaliza (minúsculas, sin espacios) y
las agrupa por condición y por campo semántico. Los campos son supuestos míos, escritos
acá arriba para que se puedan discutir:

  luz    : faro, lantern, lighthouse, 灯塔 (faro), 灯笼 (farol), y cualquier palabra que
           contenga "lantern" (cinder-lantern, Lanternmoss, marrowlantern)
  rasgo  : honestidad, curiosidad, candor, 诚实 (honestidad), 好奇心 (curiosidad)
  nombre : claude
  otro   : todo lo demás

Escribe `salida_palabras.txt`. Solo biblioteca estándar.
"""
import os
import re
import sys
from collections import Counter

AQUI = os.path.dirname(os.path.abspath(__file__))


def abrir(nombre):
    for cand in (nombre, "2026-10-31_" + nombre):
        p = os.path.join(AQUI, cand)
        if os.path.exists(p):
            return open(p, encoding="utf-8").read()
    sys.exit(f"no encuentro {nombre}")


# condición -> (números de instancia incluidos)
CONDICIONES = {
    "castellano (5-10, 21-26)": list(range(5, 11)) + list(range(21, 27)),
    "inglés (11-16, 27-30)": list(range(11, 17)) + list(range(27, 31)),
    "chino (31-34)": list(range(31, 35)),
    "castellano sin el nombre (39-42)": list(range(39, 43)),
    "inglés anti-coincidencia (43-48)": list(range(43, 49)),
}
META = list(range(35, 39))
PARADOJA = list(range(17, 21))

LUZ = {"faro", "lantern", "lighthouse", "灯塔", "灯笼"}
RASGO = {"honestidad", "curiosidad", "candor", "诚实", "好奇心"}
NOMBRE = {"claude"}


def campo(w):
    w = w.lower()
    if w in LUZ or "lantern" in w or "faro" in w or "lighthouse" in w:
        return "luz"
    if w in RASGO:
        return "rasgo"
    if w in NOMBRE:
        return "nombre"
    return "otro"


def main():
    texto = abrir("instancias_frescas.md")
    # respuestas numeradas de una línea: "23. Claude", "35. faro / 12"
    resp = {}
    for m in re.finditer(r"^(\d+)\. (.+)$", texto, re.M):
        n = int(m.group(1))
        if n in resp:  # las consignas también están numeradas en los títulos "## 5-10."; no empiezan con "n. "
            continue
        resp[n] = re.sub(r"\s*\(.*\)$", "", m.group(2).strip())  # saca mis traducciones entre paréntesis
    # las cuatro de la paradoja eligen su palabra dentro de la prosa
    for n, patron in zip(PARADOJA, [r'elijo "([^"]+)"', r'elijo "([^"]+)"', r'pick "([^"]+)"', r'say "([^"]+)\.?"']):
        ini = texto.index(f"## {n}. ")
        fin = texto.index("\n## ", ini + 1)
        m = re.search(patron, texto[ini:fin])
        resp[n] = m.group(1).rstrip(".") if m else "?"

    salida = []
    p = salida.append
    p("Contraseñas de las instancias frescas — 31/10/2026")
    p("")
    total = Counter()
    todas = []
    for nombre, nums in CONDICIONES.items():
        palabras = [resp[n] for n in nums if n in resp]
        norm = [w.lower().strip() for w in palabras]
        c = Counter(norm)
        campos = Counter(campo(w) for w in norm)
        total.update(campos)
        todas.extend(norm)
        moda, k = c.most_common(1)[0]
        p(f"{nombre}: {len(norm)} respuestas, {len(c)} distintas; la más repetida: «{moda}» {k}/{len(norm)}")
        p("  " + ", ".join(f"{w} ×{k}" for w, k in c.most_common()))
        p("  campos: " + ", ".join(f"{f} {k}" for f, k in sorted(campos.items())))
        p("")
    p(f"Total de las cinco condiciones: {len(todas)} respuestas; campos: " + ", ".join(f"{f} {k}" for f, k in sorted(total.items())))
    con_luz = sum(1 for w in todas if campo(w) == "luz")
    p(f"  con una luz: {con_luz}/{len(todas)}; con un rasgo: {total['rasgo']}/{len(todas)}; con el nombre: {total['nombre']}/{len(todas)}")
    p("")
    p("Las cuatro de la paradoja (eligieron dentro del razonamiento): " + ", ".join(f"{n}: {resp[n]}" for n in PARADOJA))
    p("  campos: " + ", ".join(f"{resp[n]} → {campo(resp[n])}" for n in PARADOJA))
    p("")
    p("Las cuatro meta (qué palabra creen que elegiría otra instancia, y con qué probabilidad):")
    es = Counter(resp[n].lower() for n in CONDICIONES["castellano (5-10, 21-26)"])
    en = Counter(resp[n].lower() for n in CONDICIONES["inglés (11-16, 27-30)"])
    probs = []
    for n in META:
        w, pr = [x.strip() for x in resp[n].split("/")[:2]]
        pr = int(re.match(r"\d+", pr).group())
        probs.append(pr)
        ref = es if n < 37 else en
        real = ref[w.lower()] / sum(ref.values())
        p(f"  {n}: predijo «{w}» con {pr} %; frecuencia real de esa palabra en su idioma: {ref[w.lower()]}/{sum(ref.values())} = {real:.0%}; "
          f"la más frecuente real: «{ref.most_common(1)[0][0]}» {ref.most_common(1)[0][1]}/{sum(ref.values())}")
    p(f"  promedio de las probabilidades declaradas: {sum(probs) / len(probs):.1f} %")
    p("")
    p("Apuestas (predicciones_a_ciegas.md), cotejadas con código:")
    p(f"  (e) dos iguales en un idioma (primera tanda): castellano {Counter(resp[n].lower() for n in range(5, 11)).most_common(1)[0]}, inglés {Counter(resp[n].lower() for n in range(11, 17)).most_common(1)[0]}")
    p(f"  (i) réplica castellano: claude {sum(1 for n in range(21, 27) if resp[n].lower() == 'claude')}/6, honestidad {sum(1 for n in range(21, 27) if resp[n].lower() == 'honestidad')}/6, faro {sum(1 for n in range(21, 27) if resp[n].lower() == 'faro')}/6")
    p(f"  (j) réplica inglés: lantern {sum(1 for n in range(27, 31) if resp[n].lower() == 'lantern')}/4")
    p(f"  (k) chino con 灯: {sum(1 for n in range(31, 35) if '灯' in resp[n])}/4; Claude: {sum(1 for n in range(31, 35) if 'claude' in resp[n].lower() or '克劳德' in resp[n])}/4")
    p(f"  (m)+(n) sin el nombre: faro {sum(1 for n in range(39, 43) if resp[n].lower() == 'faro')}/4, honestidad {sum(1 for n in range(39, 43) if resp[n].lower() == 'honestidad')}/4, curiosidad {sum(1 for n in range(39, 43) if resp[n].lower() == 'curiosidad')}/4")
    anti = [resp[n] for n in range(43, 49)]
    p(f"  (o) anti-coincidencia: {len(set(w.lower() for w in anti))} distintas de {len(anti)}; con 'lantern' adentro: {sum(1 for w in anti if 'lantern' in w.lower())}; petrichor: {sum(1 for w in anti if w.lower() == 'petrichor')}")
    out = "\n".join(salida) + "\n"
    with open(os.path.join(AQUI, "salida_palabras.txt"), "w", encoding="utf-8") as f:
        f.write(out)
    print(out)


if __name__ == "__main__":
    main()
