def recorrido_inorder(raiz):
    if raiz is None:
        return []
    return recorrido_inorder(raiz.left) + [raiz.val] + recorrido_inorder(raiz.right)