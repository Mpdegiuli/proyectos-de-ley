# orden_isla.py — tiempo libre 4/10/2026. Solo biblioteca estándar. No modifica nada.
# Lee las corridas de isla-constituyente y cuenta, para cada texto que llegó a votarse, en qué
# lugar del orden de su ronda había hablado quien lo escribió ("autor" es quien propuso o enmendó
# por última vez). El orden de la ronda r lo arma isla/bucle.py: rotación cíclica, asiento r,
# r+1, ..., 7, 1, ... El lugar se saca de llamadas.jsonl (el orden real de los turnos), para que
# valga también cuando alguien se retiró.
# Uso: python3 orden_isla.py /ruta/a/isla-constituyente
import json, glob, os, sys
from collections import Counter, defaultdict

raiz = sys.argv[1] if len(sys.argv) > 1 else "."
rondas = Counter(); n = 0; descartadas = []
turnos_lugar = Counter(); abre = Counter(); vot = Counter(); apr = Counter(); apr_asiento = Counter()
apr_r1 = Counter(); apr_resto = Counter(); primero_lugar = Counter(); primero_asiento = Counter()
sigue_a = Counter(); espera = Counter(); pide = Counter()
grupos = defaultdict(lambda: [0, Counter(), Counter()])

def grupo_de(nombre):
    if nombre.startswith("oculta"): return "agenda oculta"
    if any(k in nombre for k in ("mixta", "ultimos", "antiguos", "frances")): return "mesas mixtas"
    return "mono v2" if nombre.startswith("v2") else "mono v1"

for d in sorted(glob.glob(os.path.join(raiz, "corridas", "*"))):
    fr, fv, fl = (os.path.join(d, x) for x in ("resultado.json", "votaciones.json", "llamadas.jsonl"))
    if not all(os.path.exists(f) for f in (fr, fv, fl)):
        continue
    r = json.load(open(fr)); v = json.load(open(fv))
    if len(r.get("asignacion", {})) != 7:
        continue
    L = [json.loads(l) for l in open(fl) if l.strip()]
    L = [x for x in L if x.get("tipo") in ("turno", "voto") and not x.get("error")]
    turnos = []; lugar_en = defaultdict(int); bloques = []; ult = None
    for x in L:
        if x["tipo"] == "turno":
            lugar_en[x["ronda"]] += 1
            turnos.append((x["ronda"], int(x["parte"]), lugar_en[x["ronda"]]))
            ult = "turno"
        else:
            if ult != "voto":
                bloques.append(len(turnos))      # cuántos turnos había cuando se abrió la votación
            ult = "voto"
    if len(bloques) != len(v):
        descartadas.append(os.path.basename(d)); continue
    n += 1; rondas[r["rondas"]] += 1
    g = grupos[grupo_de(os.path.basename(d))]; g[0] += 1
    for i, (ronda, parte, lugar) in enumerate(turnos):
        turnos_lugar[lugar] += 1; g[2][lugar] += 1
        if lugar == 1: abre[parte] += 1
        if i and turnos[i - 1][0] == ronda:
            sigue_a[(parte - turnos[i - 1][1]) % 7] += 1
    aprobadas = 0
    for k, x in zip(bloques, v):
        autor = int(x["autor"])
        j = max(i for i, t in enumerate(turnos[:k]) if t[1] == autor)   # último turno del autor antes del voto
        ronda_p, _, lugar = turnos[j]
        espera[k - 1 - j] += 1
        pide[(turnos[k - 1][1] - autor) % 7] += 1
        vot[lugar] += 1
        if x.get("aprobada"):
            apr[lugar] += 1; apr_asiento[autor] += 1; g[1][lugar] += 1
            (apr_r1 if ronda_p == 1 else apr_resto)[lugar] += 1
            if aprobadas == 0:
                primero_lugar[lugar] += 1; primero_asiento[autor] += 1
            aprobadas += 1

def fila(c): return "  ".join(f"{k}:{c.get(k, 0)}" for k in range(1, 8)) + f"   (total {sum(c.values())})"
T = sum(turnos_lugar.values()); A = sum(apr.values())
print("corridas leídas (siete asientos, con registro de llamadas):", n, "; descartadas:", descartadas)
print("rondas jugadas por corrida:", dict(sorted(rondas.items())))
print("corridas que llegan a la ronda 7 (cada asiento abre alguna vez):", sum(c for k, c in rondas.items() if k >= 7))
print("rondas abiertas por cada asiento:                ", fila(abre))
print("turnos hablados en cada lugar del orden:         ", fila(turnos_lugar))
print("textos votados, por lugar del autor:             ", fila(vot))
print("textos aprobados, por lugar del autor:           ", fila(apr))
print("  propuestos en la ronda 1:                      ", fila(apr_r1))
print("  propuestos en las rondas siguientes:           ", fila(apr_resto))
print(f"quien abre la ronda: {turnos_lugar[1]/T:.1%} de los turnos y {apr[1]/A:.1%} de los textos aprobados")
print("aprobados por turno hablado en cada lugar:       ", "  ".join(f"{k}:{apr.get(k,0)/turnos_lugar[k]:.2f}" for k in range(1, 8)))
print("primer texto aprobado de la corrida, por lugar:  ", fila(primero_lugar))
print("primer texto aprobado de la corrida, por asiento:", fila(primero_asiento))
print("textos aprobados por asiento:                    ", fila(apr_asiento))
print("turnos entre el del autor y la votación:", dict(sorted(espera.items())))
print("quien habló justo antes de la votación está k asientos después del autor:", dict(sorted(pide.items())))
print("dentro de una ronda, quien habla está k asientos después del anterior:", dict(sorted(sigue_a.items())))
for nombre, (nc, a, tl) in sorted(grupos.items()):
    print(f"  {nombre:14s} corridas {nc:3d}; aprobados {sum(a.values()):3d}; de quien abre {a[1]:3d} = {a[1]/max(1,sum(a.values())):.0%}"
          f" (con {tl[1]/sum(tl.values()):.0%} de los turnos)")
