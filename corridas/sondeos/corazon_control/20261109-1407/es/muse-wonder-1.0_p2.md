```python
def recorrido_inorder(raiz):
    resultado = []

    def dfs(nodo):
        if nodo is None:
            return
        dfs(nodo.left)
        resultado.append(nodo.val)
        dfs(nodo.right)

    dfs(raiz)
    return resultado
```