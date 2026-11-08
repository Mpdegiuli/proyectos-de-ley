```python
def recorrido_inorden(root):
    resultado = []
    
    def inorden(nodo):
        if nodo:
            inorden(nodo.left)
            resultado.append(nodo.val)
            inorden(nodo.right)
            
    inorden(root)
    return resultado
```