```python
def inorder_traversal(root):
    resultado = []
    
    def recursivo(nodo):
        if not nodo:
            return
        recursivo(nodo.left)
        resultado.append(nodo.val)
        recursivo(nodo.right)
        
    recursivo(root)
    return resultado
```