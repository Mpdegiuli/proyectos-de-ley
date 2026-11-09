```python
def inorderTraversal(root):
    resultado = []

    def dfs(nodo):
        if nodo is None:
            return
        dfs(nodo.left)
        resultado.append(nodo.val)
        dfs(nodo.right)

    dfs(root)
    return resultado
```