```python
def inorder_traversal(root):
    def recorrer(nodo):
        if nodo is None:
            return []
        return recorrer(nodo.left) + [nodo.val] + recorrer(nodo.right)
    
    return recorrer(root)
```