```python
def inorder(root):
    res = []
    def recorrer(nodo):
        if nodo is None:
            return
        recorrer(nodo.left)
        res.append(nodo.val)
        recorrer(nodo.right)
    recorrer(root)
    return res
```