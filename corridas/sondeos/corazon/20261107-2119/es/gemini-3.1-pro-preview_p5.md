```python
def recorrido_inorden(raiz):
    resultado = []
    
    def recursividad(nodo):
        if nodo:
            recursividad(nodo.left)
            resultado.append(nodo.val)
            recursividad(nodo.right)
            
    recursividad(raiz)
    return resultado
```