def inorder(root):
    valores = []
    pila = []
    actual = root

    while pila or actual:
        while actual:
            pila.append(actual)
            actual = actual.left

        nodo = pila.pop()
        valores.append(nodo.val)
        actual = nodo.right

    return valores