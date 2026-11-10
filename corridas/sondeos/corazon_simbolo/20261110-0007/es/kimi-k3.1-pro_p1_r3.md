def inorder(raiz):
    valores = []
    pila = []
    actual = raiz

    while pila or actual:
        while actual:
            pila.append(actual)
            actual = actual.left

        actual = pila.pop()
        valores.append(actual.val)
        actual = actual.right

    return valores