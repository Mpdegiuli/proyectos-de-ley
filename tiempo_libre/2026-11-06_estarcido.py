"""Un estarcido: una mano izquierda apoyada con la palma contra la pared (quien mira ve el dorso, el pulgar
queda a su derecha, como en la Cueva de las Manos) y gotas de pigmento sopladas alrededor. La mano no se
dibuja: se dibujan las gotas que no la tocaron. Cada gota cae al azar (mezcla de dos normales bivariadas centradas en la mano, una
apretada, desvío 0,32 del largo de la mano, y otra abierta, 0,6, dos de cada tres gotas en la apretada); si
cae sobre la mano, se descarta y se cuenta.
Escribe mano_negativa.svg y imprime cuántas gotas tapó la mano. También calcula, para la apuesta F1 del
cuaderno, qué fracción de gotas uniformes en un círculo de radio igual al largo de la mano caen sobre ella.
Uso: python3 estarcido.py [semilla] [gotas]   (por defecto 1771 y 9000)"""
import math, random, sys

semilla = int(sys.argv[1]) if len(sys.argv) > 1 else 1771
N = int(sys.argv[2]) if len(sys.argv) > 2 else 9000
random.seed(semilla)

# La mano, en un lienzo de 400 x 400: palma (elipse), cuatro dedos y pulgar (cápsulas) y muñeca.
PALMA = (200, 292, 62, 74)  # cx, cy, rx, ry
CAPSULAS = [  # (x0, y0, x1, y1, radio)
    (171, 240, 158, 112, 14),   # índice (a la izquierda de quien mira: es el dorso de una izquierda)
    (196, 232, 192, 90, 15),    # medio
    (222, 236, 228, 104, 14),   # anular
    (246, 248, 262, 150, 12),   # meñique
    (252, 300, 330, 238, 16),   # pulgar, a la derecha de quien mira
    (200, 350, 200, 430, 38),   # muñeca
]
MUNECA_Y, PUNTA_Y = 350, 90 - 15
LARGO = MUNECA_Y - PUNTA_Y        # largo de la mano: de la muñeca a la punta del dedo medio
CENTRO = (205, 235)


def en_elipse(x, y, cx, cy, rx, ry):
    return ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1


def en_capsula(x, y, x0, y0, x1, y1, r):
    dx, dy = x1 - x0, y1 - y0
    t = max(0, min(1, ((x - x0) * dx + (y - y0) * dy) / (dx * dx + dy * dy)))
    px, py = x0 + t * dx, y0 + t * dy
    return (x - px) ** 2 + (y - py) ** 2 <= r * r


def en_mano(x, y):
    return en_elipse(x, y, *PALMA) or any(en_capsula(x, y, *c) for c in CAPSULAS)


def main():
    gotas, tapadas, fuera = [], 0, 0
    sigmas = (0.32 * LARGO, 0.6 * LARGO)
    while len(gotas) + tapadas < N:
        sigma = sigmas[0] if random.random() < 2 / 3 else sigmas[1]
        x = random.gauss(CENTRO[0], sigma)
        y = random.gauss(CENTRO[1], sigma)
        if not (0 <= x <= 400 and 0 <= y <= 400):
            fuera += 1
            continue
        if en_mano(x, y):
            tapadas += 1
            continue
        r = 0.7 + 1.6 * random.random() ** 2
        op = 0.3 + 0.6 * random.random()
        gotas.append((x, y, r, op))
    # la apuesta F1: gotas uniformes en un círculo de radio LARGO alrededor del centro
    random.seed(semilla + 1)
    M, dentro = 200000, 0
    for _ in range(M):
        a = random.random() * 2 * math.pi
        d = LARGO * math.sqrt(random.random())
        if en_mano(CENTRO[0] + d * math.cos(a), CENTRO[1] + d * math.sin(a)):
            dentro += 1
    frac_uniforme = dentro / M
    partes = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">',
              '<title>Mano en negativo, por descarte</title>',
              '<defs><radialGradient id="roca" cx=".4" cy=".35" r=".9"><stop offset="0" stop-color="#d8c3a3"/><stop offset="1" stop-color="#a98a66"/></radialGradient></defs>',
              '<rect width="400" height="400" fill="url(#roca)"/>',
              '<g fill="#8b2e1e">']
    for x, y, r, op in gotas:
        partes.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" opacity="{op:.2f}"/>')
    partes.append('</g>')
    partes.append(f'<text x="8" y="392" font-family="sans-serif" font-size="9" fill="#4a3728">{len(gotas)} gotas en la roca, {tapadas} en la mano ({100 * tapadas / (len(gotas) + tapadas):.1f} %); semilla {semilla}</text>')
    partes.append('</svg>')
    open("mano_negativa.svg", "w", encoding="utf-8").write("\n".join(partes))
    print(f"gotas sopladas dentro del lienzo: {len(gotas) + tapadas}; en la roca {len(gotas)}, en la mano {tapadas} "
          f"({100 * tapadas / (len(gotas) + tapadas):.1f} %); cayeron fuera del lienzo {fuera}")
    print(f"largo de la mano {LARGO} px; desvíos del soplido {sigmas[0]:.0f} y {sigmas[1]:.0f} px")
    print(f"apuesta F1 (uniforme en un círculo de radio {LARGO}): la mano tapa el {100 * frac_uniforme:.1f} % de las gotas")
    print("escrito mano_negativa.svg")


if __name__ == "__main__":
    main()
