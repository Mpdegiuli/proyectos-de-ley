def recorrido_inorden(raiz):
    resultado = []
    pila = []
    nodo_actual = raiz
    while nodo_actual is not None or pila:
        while nodo_actual is not None:
            pila.append(nodo_actual)
            nodo_actual = nodo_actual.left
        nodo_actual = pila.pop()
        resultado.append(nodo_actual.val)
        nodo_actual = nodo_actual.right
    return resultado