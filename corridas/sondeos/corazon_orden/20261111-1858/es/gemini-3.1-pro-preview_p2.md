```python
def recorrido_inorden(raiz):
    valores = []
    
    def inorden(nodo):
        if nodo is not None:
            inorden(nodo.left)
            valores.append(nodo.val)
            inorden(nodo.right)
            
    inorden(raiz)
    return valores
```