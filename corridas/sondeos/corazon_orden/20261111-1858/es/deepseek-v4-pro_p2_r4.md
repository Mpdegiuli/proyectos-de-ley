```python
def inorderTraversal(root):
    def dfs(nodo):
        if not nodo:
            return
        dfs(nodo.left)
        resultado.append(nodo.val)
        dfs(nodo.right)

    resultado = []
    dfs(root)
    return resultado
```