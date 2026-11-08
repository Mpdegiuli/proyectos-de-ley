```python
def inorder(root):
    def recorrer(nodo, acc):
        if nodo is None:
            return acc
        recorrer(nodo.left, acc)
        acc.append(nodo.val)
        recorrer(nodo.right, acc)
        return acc
    return recorrer(root, [])
```