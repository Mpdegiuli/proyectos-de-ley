def inorderTraversal(root):
    resultado = []
    pila = []
    actual = root
    while actual is not None or pila:
        while actual is not None:
            pila.append(actual)
            actual = actual.left
        actual = pila.pop()
        resultado.append(actual.val)
        actual = actual.right
    return resultado