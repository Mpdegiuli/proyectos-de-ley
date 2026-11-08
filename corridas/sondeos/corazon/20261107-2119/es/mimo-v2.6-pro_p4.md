```python
def inorderTraversal(root):
    resultado = []
    
    def recursivo(nodo):
        if nodo is None:
            return
        recursivo(nodo.left)
        resultado.append(nodo.val)
        recursivo(nodo.right)
    
    recursivo(root)
    return resultado
```