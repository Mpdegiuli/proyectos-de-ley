def recorrido_inorden(raiz):
    if raiz is None:
        return []
    return recorrido_inorden(raiz.left) + [raiz.val] + recorrido_inorden(raiz.right)