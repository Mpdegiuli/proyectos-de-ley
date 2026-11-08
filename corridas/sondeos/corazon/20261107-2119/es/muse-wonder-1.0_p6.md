def recorrido_inorder(raiz):
    resultado = []
    pila = []
    nodo = raiz
    while nodo or pila:
        while nodo:
            pila.append(nodo)
            nodo = nodo.left
        nodo = pila.pop()
        resultado.append(nodo.val)
        nodo = nodo.right
    return resultado