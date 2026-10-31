#!/usr/bin/env python3
"""El código de diez palabras de Harry y Bess Houdini, y el mensaje convenido.

Referencia: Massimo Polidoro, "The Day Houdini (Almost) Came Back from the Dead",
Skeptical Inquirer 36(2), marzo-abril de 2012, pp. 23-25: Pray = 1 = A, Answer = 2 = B,
Say = 3 = C, Now = 4 = D, Tell = 5 = E, Please = 6 = F, Speak = 7 = G, Quickly = 8 = H,
Look = 9 = I, Be quick = 10 o 0 = J; las letras de dos cifras se dicen con dos palabras
(N = 14 = "pray, now"); "believe" = answer, tell, pray-answer, look, tell, answer-answer,
tell. La asignación de la K a la Z por dos cifras es la que se deduce de esa regla
(K = 11 ... S = 19, T = 20 = answer + be quick, U = 21 ... Z = 26); es la que dieron las
dos instancias frescas de hoy, con [?] en la T, y la única parte que no está en la fuente
palabra por palabra es justamente esa cola.

Uso: python3 codigo.py [palabra ...]   (sin argumentos: tabla completa, "believe" y unas pruebas)
Solo biblioteca estándar.
"""
import sys

PALABRAS = ["pray", "answer", "say", "now", "tell", "please", "speak", "quickly", "look", "be quick"]
# dígito -> palabra; el 0 (en 10, 20) se dice "be quick", como el 10
DIGITO = {str(i + 1): p for i, p in enumerate(PALABRAS[:9])}
DIGITO["0"] = "be quick"


def numero(letra):
    return ord(letra.upper()) - 64  # A=1 ... Z=26


def cifrar_letra(letra):
    n = numero(letra)
    if n == 10:
        return ["be quick"]
    if n < 10:
        return [DIGITO[str(n)]]
    return [DIGITO[d] for d in str(n)]  # dos palabras


def cifrar(palabra):
    return [cifrar_letra(c) for c in palabra if c.isalpha()]


def descifrar(grupos):
    """grupos: lista de listas de palabras (una o dos por letra)."""
    inv = {v: k for k, v in DIGITO.items()}
    letras = []
    for g in grupos:
        if g == ["be quick"]:
            letras.append("J")
            continue
        n = int("".join(inv[w] for w in g))
        letras.append(chr(64 + n))
    return "".join(letras)


def mostrar(palabra):
    grupos = cifrar(palabra)
    partes = [" ".join(g) if len(g) == 1 else ", ".join(g) for g in grupos]
    return f"{palabra.upper():10s} = " + " — ".join(partes)


if __name__ == "__main__":
    print("Tabla del código (letra = número = palabra o palabras):")
    for i in range(26):
        letra = chr(65 + i)
        print(f"  {letra} = {i + 1:2d} = {', '.join(cifrar_letra(letra))}")
    print()
    print("El mensaje convenido:")
    print("  " + mostrar("believe"))
    recibido = [["answer"], ["tell"], ["pray", "answer"], ["look"], ["tell"], ["answer", "answer"], ["tell"]]
    print("  Lo que dijo Ford el 8/1/1929, descifrado:", descifrar(recibido))
    assert descifrar(recibido) == "BELIEVE"
    assert cifrar("believe") == recibido
    print()
    print("Palabras de hoy, en el código de 1894:")
    for w in (sys.argv[1:] or ["lantern", "faro", "claude", "honestidad", "curiosidad", "rosabelle"]):
        print("  " + mostrar(w))
    print()
    print("Cuántas palabras hacen falta para deletrear:")
    for w in ("believe", "lantern", "faro", "claude", "honestidad", "curiosidad"):
        print(f"  {w:11s} {sum(len(g) for g in cifrar(w)):2d} palabras para {len(w)} letras")
