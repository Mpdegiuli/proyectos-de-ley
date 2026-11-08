```python
def recorrido_inorden(raiz):
    resultado = []
    
    def inorden(nodo):
        if nodo:
            inorden(nodo.left)
            resultado.append(nodo.val)
            inorden(nodo.right)
            
    inorden(raiz)
    return resultado
```