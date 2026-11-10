def inorder(root):
    valores = []
    pila = []
    actual = root

    while pila or actual:
        while actual:
            pila.append(actual)
            actual = actual.left

        actual = pila.pop()
        valores.append(actual.val)
        actual = actual.right

    return valores