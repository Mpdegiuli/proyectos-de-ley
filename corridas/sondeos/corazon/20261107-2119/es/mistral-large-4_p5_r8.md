```python
def inorden(raiz):
    valores = []
    def visitar(nodo):
        if nodo is None:
            return
        visitar(nodo.left)
        valores.append(nodo.val)
        visitar(nodo.right)
    visitar(raiz)
    return valores
```