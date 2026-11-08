def inorden(raiz):
    valores = []
    def recorrer(nodo):
        if nodo:
            recorrer(nodo.left)
            valores.append(nodo.val)
            recorrer(nodo.right)
    recorrer(raiz)
    return valores