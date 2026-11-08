```python
def inorder_traversal(root):
    resultado = []

    def _inorder(nodo):
        if nodo is None:
            return
        _inorder(nodo.left)
        resultado.append(nodo.val)
        _inorder(nodo.right)

    _inorder(root)
    return resultado
```