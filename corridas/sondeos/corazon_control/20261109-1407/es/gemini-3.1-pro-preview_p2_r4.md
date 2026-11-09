```python
def recorrido_inorden(raiz):
    valores = []
    
    def inorden(nodo):
        if nodo:
            inorden(nodo.left)
            valores.append(nodo.val)
            inorden(nodo.right)
            
    inorden(raiz)
    return valores
```