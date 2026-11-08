def inorder_traversal(root):
    valores = []

    def recorrer(nodo):
        if nodo is None:
            return
        recorrer(nodo.left)
        valores.append(nodo.val)
        recorrer(nodo.right)

    recorrer(root)
    return valores