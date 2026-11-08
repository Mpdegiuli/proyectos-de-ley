def recorrido_inorder(raiz):
    valores = []
    pila = []
    actual = raiz

    while pila or actual is not None:
        while actual is not None:
            pila.append(actual)
            actual = actual.left

        actual = pila.pop()
        valores.append(actual.val)
        actual = actual.right

    return valores