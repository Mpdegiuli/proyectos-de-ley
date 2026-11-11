```python
def inorden(raiz):
    resultado = []
    def visitar(nodo):
        if nodo:
            visitar(nodo.left)
            resultado.append(nodo.val)
            visitar(nodo.right)
    visitar(raiz)
    return resultado
```