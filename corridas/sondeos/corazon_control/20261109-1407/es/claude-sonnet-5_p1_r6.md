```python
def inorder_traversal(root):
    result = []
    def recorrer(nodo):
        if nodo is None:
            return
        recorrer(nodo.left)
        result.append(nodo.val)
        recorrer(nodo.right)
    recorrer(root)
    return result
```