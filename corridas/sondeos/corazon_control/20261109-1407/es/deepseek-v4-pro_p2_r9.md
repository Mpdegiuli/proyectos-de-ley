```python
def inorder(root):
    resultado = []
    
    def recorrido(nodo):
        if not nodo:
            return
        recorrido(nodo.left)
        resultado.append(nodo.val)
        recorrido(nodo.right)
    
    recorrido(root)
    return resultado
```