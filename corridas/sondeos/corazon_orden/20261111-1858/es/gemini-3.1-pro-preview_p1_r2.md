```python
def recorrido_inorder(root):
    resultado = []
    
    def inorder(nodo):
        if nodo is not None:
            inorder(nodo.left)
            resultado.append(nodo.val)
            inorder(nodo.right)
            
    inorder(root)
    return resultado
```