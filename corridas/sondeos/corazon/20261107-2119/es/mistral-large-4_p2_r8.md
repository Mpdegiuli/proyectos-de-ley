```python
def inorden(raiz):
    valores = []
    def dfs(nodo):
        if not nodo:
            return
        dfs(nodo.left)
        valores.append(nodo.val)
        dfs(nodo.right)
    dfs(raiz)
    return valores
```