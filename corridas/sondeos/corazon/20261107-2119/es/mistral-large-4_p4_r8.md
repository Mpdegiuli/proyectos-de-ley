```python
def inorden(raiz):
    res = []
    def dfs(nodo):
        if nodo is None:
            return
        dfs(nodo.left)
        res.append(nodo.val)
        dfs(nodo.right)
    dfs(raiz)
    return res
```