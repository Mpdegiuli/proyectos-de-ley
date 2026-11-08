def inorder_traversal(root):
    resultado = []
    pila = []
    nodo = root
    while nodo or pila:
        while nodo:
            pila.append(nodo)
            nodo = nodo.left
        nodo = pila.pop()
        resultado.append(nodo.val)
        nodo = nodo.right
    return resultado