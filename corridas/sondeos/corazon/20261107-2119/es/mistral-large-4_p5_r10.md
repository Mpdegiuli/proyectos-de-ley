```python
def inorden(raiz):
    valores = []
    def visitar(nodo):
        if nodo:
            visitar(nodo.left)
            valores.append(nodo.val)
            visitar(nodo.right)
    visitar(raiz)
    return valores
```