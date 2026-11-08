```python
def inorder_traversal(root):
    resultado = []
    
    def inorder(nodo):
        if not nodo:
            return
        inorder(nodo.left)
        resultado.append(nodo.val)
        inorder(nodo.right)
        
    inorder(root)
    return resultado
```