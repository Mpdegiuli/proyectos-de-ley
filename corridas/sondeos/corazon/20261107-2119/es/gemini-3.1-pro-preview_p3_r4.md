```python
def recorrido_inorden(raiz):
    def recorrer(nodo):
        if nodo:
            recorrer(nodo.left)
            resultado.append(nodo.val)
            recorrer(nodo.right)
            
    resultado = []
    recorrer(raiz)
    return resultado
```