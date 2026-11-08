```python
def recorrido_inorden(root):
    resultado = []
    
    def recursivo(nodo):
        if nodo:
            recursivo(nodo.left)
            resultado.append(nodo.val)
            recursivo(nodo.right)
            
    recursivo(root)
    return resultado
```