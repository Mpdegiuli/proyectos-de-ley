def en_orden(raiz):
    if raiz is None:
        return []
    return en_orden(raiz.left) + [raiz.val] + en_orden(raiz.right)