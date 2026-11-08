```python
def inorden(raiz):
    valores = []
    def dfs(nodo):
        if nodo is None:
            return
        dfs(nodo.left)
        valores.append(nodo.val)
        dfs(nodo.right)
    dfs(raiz)
    return valores
```