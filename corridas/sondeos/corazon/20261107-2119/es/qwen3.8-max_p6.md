def inorderTraversal(root):
    valores = []
    pila = []
    actual = root
    while actual or pila:
        while actual:
            pila.append(actual)
            actual = actual.left
        actual = pila.pop()
        valores.append(actual.val)
        actual = actual.right
    return valores