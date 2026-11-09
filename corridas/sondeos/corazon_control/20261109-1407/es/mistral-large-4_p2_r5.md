def inorden(root):
    valores = []
    def visitar(nodo):
        if nodo is None:
            return
        visitar(nodo.left)
        valores.append(nodo.val)
        visitar(nodo.right)
    visitar(root)
    return valores