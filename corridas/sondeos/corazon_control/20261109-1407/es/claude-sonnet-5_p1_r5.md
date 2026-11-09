```python
def inorder_traversal(root):
    def recorrer(nodo, resultado):
        if nodo is not None:
            recorrer(nodo.left, resultado)
            resultado.append(nodo.val)
            recorrer(nodo.right, resultado)
        return resultado
    
    return recorrer(root, [])
```