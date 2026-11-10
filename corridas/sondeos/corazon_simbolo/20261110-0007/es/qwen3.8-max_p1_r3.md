```python
def inorderTraversal(root):
    resultado = []

    def visitar(nodo):
        if nodo is None:
            return
        visitar(nodo.left)
        resultado.append(nodo.val)
        visitar(nodo.right)

    visitar(root)
    return resultado
```