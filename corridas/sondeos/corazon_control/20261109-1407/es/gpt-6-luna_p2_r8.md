def inorderTraversal(root):
    valores = []
    pila = []
    nodo = root

    while nodo or pila:
        while nodo:
            pila.append(nodo)
            nodo = nodo.left
        nodo = pila.pop()
        valores.append(nodo.val)
        nodo = nodo.right

    return valores