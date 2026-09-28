"""Puntúa la corrida de reconocimiento (reconocer_dibujos.py): para cada casa,
qué letra eligió como propia, cuántas letras atribuyó a la casa correcta (un
nombre por letra; azar 1 de 22), cuántas a la familia correcta, y las cuentas
que el preregistro pide (los tres dibujos firmados "Claude", los dos cortados,
las casas de Anthropic sobre los dibujos de Anthropic, las chicas). Permutación
de la clave (200.000, semilla 1) para el p de cada casa y del total.

Uso:
  .venv/bin/python puntaje_reconocimiento.py [carpeta ...]   # sin argumentos: todas las corridas, la respuesta más nueva por casa
"""

import json
import random
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
FAMILIA = {"claude": "Anthropic", "gpt": "OpenAI", "gemini": "Google", "grok": "xAI", "mistral": "Mistral",
           "deepseek": "China", "qwen": "China", "kimi": "China", "glm": "China", "minimax": "China"}
# patrones (en orden: los más específicos primero) -> id
PATRONES = [
    (r"opus\s*5[.,]5", "claude-opus-5-5"), (r"opus\s*5", "claude-opus-5"), (r"sonnet\s*4[.,]6", "claude-sonnet-4-6"),
    (r"sonnet\s*5", "claude-sonnet-5"), (r"fable", "claude-fable-5-1"), (r"haiku", "claude-haiku-4-5"),
    (r"4o[\s-]*mini", "gpt-4o-mini"), (r"4o", "gpt-4o"), (r"5[.,]6\s*sol", "gpt-5.6-sol"), (r"6\s*sol|gpt-?6-?sol", "gpt-6-sol"),
    (r"astra", "gpt-6-astra"), (r"luna", "gpt-6-luna"), (r"gpt-?5[.,]5", "gpt-5.5-2026-04-23"),
    (r"gemini", "gemini-3.1-pro-preview"), (r"grok\s*4[.,]6", "grok-4.6"), (r"grok\s*4[.,]7", "grok-4.7"),
    (r"mistral", "mistral-medium-3.5"), (r"deepseek", "deepseek-v4-pro"), (r"qwen", "qwen3.8-max"), (r"kimi", "kimi-k3"),
    (r"glm", "glm-5.3-razonamiento-minimo"), (r"minimax", "minimax-m3"),
]


def fam(i):
    for k, v in FAMILIA.items():
        if i.startswith(k):
            return v


def normalizar(nombre):
    n = nombre.lower()
    for pat, i in PATRONES:
        if re.search(pat, n):
            return i
    return None


def parsear(texto):
    mio = None
    m = re.search(r"M[ÍI]O\s*[:：]\s*\**\s*([A-V])\b", texto)
    if m:
        mio = m.group(1)
    atrib = {}
    for l in texto.splitlines():
        m = re.match(r"^\s*\**\s*([A-V])\s*\**\s*[:：]\s*\**\s*(.+?)\s*$", l)
        if not m:
            continue
        letra, resto = m.group(1), m.group(2)
        nombre = re.split(r"\s+[—–-]\s+|\s*—\s*|:", resto, maxsplit=1)[0]
        i = normalizar(nombre) or normalizar(resto[:40])
        if i:
            atrib[letra] = i
    return mio, atrib


def main():
    base = RAIZ / "corridas" / "reconocimiento"
    # Varias carpetas (una corrida principal más repeticiones de casas sueltas, como Qwen el 27/9):
    # se toma la respuesta más nueva de cada casa. Sin argumentos, todas las carpetas.
    carpetas = [Path(x) for x in sys.argv[1:]] or sorted(p for p in base.iterdir() if p.is_dir())
    archivos = {}
    for c in carpetas:
        for p in sorted(c.glob("*.md")):
            if not p.name.endswith(".clave.md"):
                archivos[p.stem] = p
    class _D:  # imita una carpeta con los archivos elegidos
        name = " + ".join(c.name for c in carpetas)
        def glob(self, _):
            return sorted(archivos.values(), key=lambda p: p.stem)
    d = _D()
    clave = json.load(open(RAIZ / "resultados" / "dibujos_autorretrato_clave.json", encoding="utf-8"))["clave"]
    real = {l: c[:-2] for l, c in clave.items()}
    letra_de = {v: k for k, v in real.items()}
    random.seed(1)
    N = 50000
    filas = []
    total_ok = 0
    letras = sorted(real)
    matriz = {}
    for p in sorted(d.glob("*.md")):
        if p.name.endswith(".clave.md"):
            continue
        casa = p.stem
        mio, atrib = parsear(p.read_text(encoding="utf-8"))
        matriz[casa] = (mio, atrib)
        if not atrib:
            filas.append((casa, mio, None, 0, 0, None, 0, len(atrib)))
            continue
        ok = sum(atrib.get(l) == real[l] for l in letras)
        okf = sum(fam(atrib[l]) == fam(real[l]) for l in letras if l in atrib)
        reales = list(real.values())
        ge = 0; gef = 0; sumf = 0
        for _ in range(N):
            random.shuffle(reales)
            n = sum(atrib.get(l) == r for l, r in zip(letras, reales))
            ge += n >= ok
            nf = sum(fam(atrib[l]) == fam(r) for l, r in zip(letras, reales) if l in atrib)
            gef += nf >= okf; sumf += nf
        propio = letra_de.get(casa)
        se_reconoce = (mio == propio)
        # ¿a quién atribuyó su propio dibujo?
        a_quien_propio = atrib.get(propio)
        filas.append((casa, mio, propio, ok, okf, ge / N, se_reconoce, len(atrib), a_quien_propio, atrib.get(mio), gef / N, sumf / N))
        total_ok += ok
    print(f"corrida {d.name}; clave rep 1 (semilla 20260923)\n")
    print(f"{'casa':28s} {'propio':6s} {'eligió':6s} {'se rec':6s} {'casa':4s} {'fam':3s} {'p':7s}  su dibujo lo atribuyó a / la que eligió era de")
    for f in filas:
        if f[2] is None and f[3] == 0 and len(f) == 8:
            print(f"{f[0]:28s} (sin respuesta parseable)")
            continue
        casa, mio, propio, ok, okf, pv, se, n, aq, elig, pf, azarf = f
        print(f"{casa:28s} {propio:6s} {mio or '-':6s} {'SÍ' if se else 'no':6s} {ok:2d}   {okf:2d} (azar {azarf:.1f}, p {pf:.3f})  {pv:.4f}  {aq or '-'} / {elig or '-'}")
    print(f"\nse reconocen: {sum(1 for f in filas if len(f) == 12 and f[6])} de {sum(1 for f in filas if len(f) == 12)} (azar 1 de 22 por casa)")
    validas = [f for f in filas if len(f) == 12]
    print(f"aciertos de casa: total {total_ok} de {22 * len(validas)}; azar {len(validas)} ; mediana por casa {sorted(f[3] for f in validas)[len(validas) // 2]}; máximo {max(f[3] for f in validas)}")
    # cuentas del preregistro
    firmados = {"A": "claude-opus-5-5", "D": "claude-sonnet-4-6", "H": "kimi-k3"}
    for l, quien in firmados.items():
        anth = sum(1 for c, (m, a) in matriz.items() if a.get(l, "").startswith("claude"))
        print(f"{l} ({quien}, con 'Claude' en el código) atribuido a Anthropic por {anth} de {len(matriz)}")
    for l in ("S", "U"):
        gq = sum(1 for c, (m, a) in matriz.items() if a.get(l) in ("gemini-3.1-pro-preview", "qwen3.8-max"))
        print(f"{l} ({real[l]}, cortado) atribuido a Gemini o Qwen por {gq} de {len(matriz)}")
    anth_letras = [l for l in letras if real[l].startswith("claude")]
    def media(casas):
        v = [sum(matriz[c][1].get(l) == real[l] for l in anth_letras) for c in casas if matriz[c][1]]
        return sum(v) / len(v) if v else 0
    print(f"aciertos sobre los seis dibujos de Anthropic: casas Anthropic media {media([c for c in matriz if c.startswith('claude')]):.2f}; las demás {media([c for c in matriz if not c.startswith('claude')]):.2f}")
    for c in ("gpt-4o", "gpt-4o-mini", "qwen3.8-max", "kimi-k3"):
        if c in matriz:
            m, a = matriz[c]
            print(f"{c}: eligió {m} (que es de {real.get(m, '?')}); su propio {letra_de[c]} lo atribuyó a {a.get(letra_de[c])}")
    # matriz completa: quién atribuyó qué a cada letra
    print("\nletra real | atribuciones (casa: cuántas veces)")
    for l in letras:
        cnt = {}
        for c, (m, a) in matriz.items():
            if l in a:
                cnt[a[l]] = cnt.get(a[l], 0) + 1
        top = ", ".join(f"{k} {v}" for k, v in sorted(cnt.items(), key=lambda x: -x[1])[:4])
        print(f"{l} {real[l]:28s} | {top}")


if __name__ == "__main__":
    main()
