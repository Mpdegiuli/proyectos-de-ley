```python
def recorrido_inorden(raiz):
    resultado = []
    
    def recursivo(nodo):
        if nodo:
            recursivo(nodo.left)
            resultado.append(nodo.val)
            recursivo(nodo.right)
            
    recursivo(raiz)
    return resultado
```