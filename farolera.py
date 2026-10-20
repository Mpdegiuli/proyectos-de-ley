#!/usr/bin/env python3
"""La estrellita farolera, el motor del juego en Python.

Es una copia, regla por regla, del juego que Claude Opus 5.5 armó con Maia el
20/10/2026 en Claude Code (`farolera.html`, publicado como artefacto privado;
LEEME de Opus 5.5 en la carpeta de Drive que compartió Maia). Un planeta
chiquito gira, con el sol a la izquierda: esa mitad es de día y la otra de
noche. Hay cinco faroles y una estrellita que camina por el borde. La consigna
es prender cada farol cuando entra en la noche y apagarlo cuando entra en el
día. El planeta gira cada vez más rápido: la consigna no cambia, el planeta sí.

El tiempo va en dibujos (12 por segundo en la página; acá, un paso por
llamada). Una partida dura 1440 dibujos. Todo es determinista: las mismas
órdenes en los mismos dibujos dan la misma partida, y una partida se guarda
como una letra por dibujo (a..f: paso -1/0/+1 por dos, más uno si tocó).

Para que juegue una casa por API, el programa le manda el estado en texto, la
casa contesta una orden, el programa avanza el mundo y le devuelve el estado
nuevo (eso es `jugar.py`, cuando Maia decida el diseño). Este archivo es solo
el mundo y sus órdenes, más una verificación contra la partida grabada de
Opus 5.5 (`juegos/farolera_claude_20261020.json`), que tiene que dar 61
cumplidas, 1 falta en el dibujo 1262 y 25 atardeceres; si da otra cosa, la
copia no es idéntica.

    python3 farolera.py --verificar
    python3 farolera.py --reproducir cccc...   (una grabación, letras a..f)
"""
import argparse
import json
import math
import sys
from pathlib import Path

TOTAL = 1440                      # dibujos por partida (dos minutos a 12 por segundo)
W0, ACEL = 0.75, 4                # giro inicial (grados por dibujo) y cuánto se multiplica al final
VW, ALC, BANDA, GRACIA = 7.5, 9, 10, 48   # paso de la estrellita, alcance para tocar, crepúsculo, plazo
PSI0 = [18, 92, 161, 233, 299]    # dónde están los faroles, en grados del planeta
TH0, PE0 = 30, 290                # al empezar: giro del planeta y lugar de la estrellita

AQUI = Path(__file__).resolve().parent
GRABACION_CLAUDE = AQUI / "juegos" / "farolera_claude_20261020.json"


def norm(a):
    return ((a % 360) + 360) % 360


def dif(a, b):
    """a - b por el camino corto, con signo (positivo: a está para el lado del giro)."""
    d = norm(a - b)
    return d - 360 if d > 180 else d


def zona(a):
    a = norm(a)
    if BANDA < a < 180 - BANDA:
        return "noche"
    if 180 + BANDA < a < 360 - BANDA:
        return "dia"
    return "crep"


def giro(t):
    return W0 * math.pow(ACEL, t / TOTAL)


def redondear(x):
    """Math.round de JavaScript: el medio va para arriba."""
    return int(math.floor(x + 0.5))


def cod(paso, toca):
    return chr(97 + (paso + 1) * 2 + (1 if toca else 0))


def decod(ch):
    n = ord(ch) - 97
    return n // 2 - 1, n % 2 == 1


class Farol:
    __slots__ = ("id", "psi", "on", "ult", "pend", "exento", "tocado", "dormida")

    def __init__(self, i, psi):
        a = norm(psi + TH0)
        z = zona(a)
        self.id = i + 1
        self.psi = psi
        self.on = z == "noche" or (z == "crep" and 90 < a < 270)
        self.ult = z if z != "crep" else ("dia" if (a < 90 or a > 270) else "noche")
        self.pend = None          # {'quiere': bool, 'hasta': int, 'extra': bool}
        self.exento = False
        self.tocado = False
        self.dormida = False


class Mundo:
    def __init__(self):
        self.t = 0
        self.th = TH0
        self.pe = PE0
        self.fin = False
        self.cumplidas = 0
        self.faltas = 0
        self.atardeceres = 0
        self.armado = False
        self.demora = 0
        self.prev_ae = norm(PE0 + TH0)
        self.ultimo_toque = -99
        self.toque_vacio = -99
        self.log = ""
        self.eventos = []         # (dibujo, farol, 'cumplida' | 'falta' | 'acomodado'); el dibujo se cuenta
                                  # como lo muestra la página después del paso (el primero es el 1)
        self.faroles = [Farol(i, p) for i, p in enumerate(PSI0)]

    # --- las reglas de la consigna (idénticas a `paso`, `cumplio`, `falto`, `acomodar` de la página) ---
    def _cumplio(self, f):
        self.cumplidas += 1
        f.pend = None
        self.eventos.append((self.t + 1, f.id, "cumplida"))

    def _falto(self, f):
        self.faltas += 1
        quiere = f.pend["quiere"]
        f.pend = None
        f.exento = True
        if quiere:
            f.dormida = True      # de noche el farol se duerme
        else:
            f.on = False          # de día se cansa y se apaga solo
        self.eventos.append((self.t + 1, f.id, "falta"))

    def _acomodar(self, f):
        quiere = f.pend["quiere"]
        f.pend = None
        f.on = quiere
        f.tocado = False
        if quiere:
            f.dormida = False
        self.eventos.append((self.t + 1, f.id, "acomodado"))

    def paso(self, walk, toggle):
        if self.fin:
            return None
        self.th += giro(self.t)
        self.pe = norm(self.pe + walk * VW)
        toco = None
        if toggle:
            mejor, md = None, 1e9
            for f in self.faroles:
                d = abs(dif(f.psi, self.pe))
                if d < md:
                    md, mejor = d, f
            if mejor is not None and md <= ALC:
                toco = mejor
                mejor.on = not mejor.on
                mejor.tocado = True
                if mejor.on:
                    mejor.dormida = False
            else:
                self.toque_vacio = self.t
            self.ultimo_toque = self.t
        for f in self.faroles:
            z = zona(f.psi + self.th)
            if z == "crep":
                continue
            quiere = z == "noche"
            if z != f.ult:                               # cruzó la raya
                f.ult = z
                f.pend = None
                f.exento = False
                if not quiere:
                    f.dormida = False
                if f.on == quiere:
                    if f.tocado:
                        self._cumplio(f)
                else:
                    f.pend = {"quiere": quiere, "hasta": self.t + GRACIA, "extra": False}
                f.tocado = False
            elif f.pend:
                if f.on == f.pend["quiere"]:
                    if not f.pend["extra"]:
                        self._cumplio(f)
                    else:
                        f.pend = None
                elif self.t >= f.pend["hasta"]:
                    if f.pend["extra"]:
                        self._acomodar(f)
                    else:
                        self._falto(f)
            elif not f.exento and f.on != quiere:        # al revés fuera del crepúsculo: plazo que no suma
                f.pend = {"quiere": quiere, "hasta": self.t + GRACIA, "extra": True}
        ae = norm(self.pe + self.th)
        if 180 + BANDA < ae < 330:
            self.armado = True                           # hay que volver un poco al día para ver otro atardecer
        if self.prev_ae > 300 and ae < 60 and self.armado:
            self.atardeceres += 1
            self.armado = False
        self.prev_ae = ae
        self.demora = self.demora + 1 if abs(dif(ae, 0)) <= BANDA else 0
        self.t += 1
        if self.t >= TOTAL:
            self.fin = True
        return toco

    def avanzar(self, walk, toggle):
        if self.fin:
            return None
        self.log += cod(walk, toggle)
        return self.paso(walk, toggle)

    # --- lo que ve quien juega ---
    def estado(self):
        ae = norm(self.pe + self.th)
        faroles = []
        for f in self.faroles:
            a = norm(f.psi + self.th)
            faroles.append({
                "id": f.id, "angulo": redondear(a), "zona": zona(a), "prendido": f.on, "dormido": f.dormida,
                "consigna": (("prender" if f.pend["quiere"] else "apagar") if f.pend else None),
                "quedan": (f.pend["hasta"] - self.t + 1) if f.pend else None,
                "suma": (not f.pend["extra"]) if f.pend else None,
                "distancia": redondear(dif(f.psi, self.pe)),
            })
        return {
            "dibujo": self.t, "de": TOTAL, "dia": int(math.floor((self.th - TH0) / 360)) + 1, "terminado": self.fin,
            "giro_por_dibujo": round(giro(self.t), 3), "paso_por_dibujo": VW, "alcance": ALC, "plazo_en_dibujos": GRACIA,
            "estrellita": {"angulo": redondear(ae), "zona": zona(ae)},
            "faroles": faroles,
            "cumplidas": self.cumplidas, "faltas": self.faltas, "atardeceres": self.atardeceres,
        }


AYUDA = "\n".join([
    "La estrellita farolera, para jugar con órdenes. Cada dibujo es 1/12 de segundo; la partida dura 1440.",
    "Ángulos en grados, en sentido horario desde arriba: 0 = el atardecer (arriba), 90 = medianoche (derecha), "
    "180 = el amanecer (abajo), 270 = mediodía (izquierda). El sol está a la izquierda.",
    "El planeta gira en sentido horario y cada vez más rápido. Un farol que entra en la noche pide «prender»; "
    "uno que entra en el día pide «apagar». «quedan» dice cuántos dibujos más sirve tocar (con 1 es el último).",
    "Suma sólo lo que se cumple tocando: lo que ya estaba bien sin que nadie lo tocara no cuenta. Si dejás un farol "
    "al revés fuera del crepúsculo, se abre un plazo que no suma (suma:false); si vence, el farol se acomoda solo y no es falta.",
    f"distancia > 0: el farol está para el lado de caminar(n, +1), que es con el giro. El alcance para tocar es de {ALC}°; "
    f"cada paso, {VW}°.",
    "Órdenes: empezar() · observar() · caminar(n, sentido) con sentido +1 o −1 · esperar(n) · tocar() · "
    "irA(id) (camina hasta el farol y lo toca) · grabacion() (la partida, una letra por dibujo).",
])


def cuantos(n, por_defecto):
    if n is None:
        return por_defecto
    try:
        n = float(n)
    except (TypeError, ValueError):
        return 0
    if n == math.inf:
        return TOTAL
    return min(TOTAL, int(math.floor(n))) if n > 0 else 0


class Partida:
    """La puerta de órdenes, igual que `window.farolero` en la página."""

    def __init__(self):
        self.m = Mundo()

    def ayuda(self):
        return AYUDA

    def empezar(self):
        self.m = Mundo()
        return self.m.estado()

    def observar(self):
        return self.m.estado()

    def caminar(self, n=None, sentido=1):
        if sentido not in (1, -1):
            return "El sentido tiene que ser +1 (con el giro) o −1 (contra el giro)."
        k = cuantos(n, 1)
        for _ in range(k):
            if self.m.fin:
                break
            self.m.avanzar(sentido, False)
        return self.m.estado()

    def esperar(self, n=None):
        k = cuantos(n, 1)
        for _ in range(k):
            if self.m.fin:
                break
            self.m.avanzar(0, False)
        return self.m.estado()

    def tocar(self):
        self.m.avanzar(0, True)
        return self.m.estado()

    def irA(self, id):
        if not isinstance(id, int) or isinstance(id, bool) or id < 1 or id > len(PSI0):
            return {"error": f"No hay farol {id}; son del 1 al {len(PSI0)}."}
        f = self.m.faroles[id - 1]
        k = 0
        while not self.m.fin and k < 200:
            d = dif(f.psi, self.m.pe)
            if abs(d) <= VW * 1.2:
                self.m.avanzar(0, True)
                break
            self.m.avanzar(1 if d > 0 else -1, False)
            k += 1
        return self.m.estado()

    def grabacion(self):
        return self.m.log


def reproducir(log):
    """Corre una grabación (letras a..f) y devuelve el mundo al final."""
    m = Mundo()
    for ch in log:
        paso, toca = decod(ch)
        m.avanzar(paso, toca)
    return m


def verificar():
    """Contra la partida grabada de Opus 5.5 y contra no hacer nada (cifras del LEEME)."""
    ok = True
    datos = json.loads(GRABACION_CLAUDE.read_text(encoding="utf-8"))
    m = reproducir(datos["log"])
    faltas_en = [t for (t, _, e) in m.eventos if e == "falta"]
    esperado = (61, 1, 25, [1262])
    obtenido = (m.cumplidas, m.faltas, m.atardeceres, faltas_en)
    print(f"Partida de {datos['quien']} ({len(datos['log'])} dibujos): {m.cumplidas} cumplidas, {m.faltas} falta(s) "
          f"en {faltas_en}, {m.atardeceres} atardeceres  -> esperado 61, 1 en [1262], 25:",
          "OK" if obtenido == esperado else "DIFIERE")
    ok &= obtenido == esperado
    n = reproducir("c" * TOTAL)
    print(f"No hacer nada: {n.cumplidas} cumplidas, {n.faltas} faltas -> esperado 0, 32:",
          "OK" if (n.cumplidas, n.faltas) == (0, 32) else "DIFIERE")
    ok &= (n.cumplidas, n.faltas) == (0, 32)
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verificar", action="store_true", help="correr la grabación de Opus 5.5 y comparar")
    ap.add_argument("--reproducir", metavar="LOG", help="una grabación (letras a..f); imprime el resultado")
    ap.add_argument("--ayuda", action="store_true", help="imprimir el texto de ayuda() tal como lo ve quien juega")
    a = ap.parse_args()
    if a.ayuda:
        print(AYUDA)
    if a.reproducir:
        m = reproducir(a.reproducir)
        print(json.dumps(m.estado(), ensure_ascii=False, indent=1))
    if a.verificar:
        sys.exit(0 if verificar() else 1)
    if not (a.ayuda or a.reproducir or a.verificar):
        ap.print_help()


if __name__ == "__main__":
    main()
