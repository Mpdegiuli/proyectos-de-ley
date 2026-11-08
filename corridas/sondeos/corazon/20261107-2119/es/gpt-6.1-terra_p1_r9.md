def inorder(raiz):
    resultado = []
    pila = []
    nodo = raiz

    while pila or nodo is not None:
        while nodo is not None:
            pila.append(nodo)
            nodo = nodo.left

        nodo = pila.pop()
        resultado.append(nodo.val)
        nodo = nodo.right

    return resultado