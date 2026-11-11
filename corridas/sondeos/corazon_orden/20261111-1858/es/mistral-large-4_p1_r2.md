def inorden(raiz):
    resultado = []
    def visitar(nodo):
        if nodo is None:
            return
        visitar(nodo.left)
        resultado.append(nodo.val)
        visitar(nodo.right)
    visitar(raiz)
    return resultado