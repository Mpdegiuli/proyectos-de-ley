def inorderTraversal(root):
    resultado = []
    pila = []
    nodo = root

    while pila or nodo:
        while nodo:
            pila.append(nodo)
            nodo = nodo.left

        nodo = pila.pop()
        resultado.append(nodo.val)
        nodo = nodo.right

    return resultado