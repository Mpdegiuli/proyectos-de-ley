```python
def recorrido_inorden(raiz):
    valores = []
    
    def recorrer(nodo):
        if nodo is not None:
            recorrer(nodo.left)
            valores.append(nodo.val)
            recorrer(nodo.right)
            
    recorrer(raiz)
    return valores
```