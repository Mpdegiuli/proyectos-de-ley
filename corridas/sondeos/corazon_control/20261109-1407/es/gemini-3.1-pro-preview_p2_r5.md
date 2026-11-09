```python
def inorden_recursivo(root):
    def recorrer(nodo, valores):
        if nodo:
            recorrer(nodo.left, valores)
            valores.append(nodo.val)
            recorrer(nodo.right, valores)
    
    resultado = []
    recorrer(root, resultado)
    return resultado
```