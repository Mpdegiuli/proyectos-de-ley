```python
def inorden(raiz):
    resultado = []
    
    def recorrer(nodo):
        if nodo is not None:
            recorrer(nodo.left)
            resultado.append(nodo.val)
            recorrer(nodo.right)
            
    recorrer(raiz)
    return resultado
```