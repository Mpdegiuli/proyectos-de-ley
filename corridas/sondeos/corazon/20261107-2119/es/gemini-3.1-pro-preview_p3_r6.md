```python
def inorder_traversal(root):
    resultado = []
    
    def recorrido(nodo):
        if nodo:
            recorrido(nodo.left)
            resultado.append(nodo.val)
            recorrido(nodo.right)
            
    recorrido(root)
    return resultado
```