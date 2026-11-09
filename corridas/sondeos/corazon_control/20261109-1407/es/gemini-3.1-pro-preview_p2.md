```python
def inorder_traversal(root):
    valores = []
    
    def inorder(nodo):
        if nodo is not None:
            inorder(nodo.left)
            valores.append(nodo.val)
            inorder(nodo.right)
            
    inorder(root)
    return valores
```