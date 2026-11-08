```python
def inorder_traversal(root):
    resultado = []
    
    def recursividad(nodo):
        if nodo:
            recursividad(nodo.left)
            resultado.append(nodo.val)
            recursividad(nodo.right)
            
    recursividad(root)
    return resultado
```