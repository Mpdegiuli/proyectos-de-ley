```python
def inorder_traversal(root):
    resultado = []

    def _inorder(nodo):
        if nodo is None:
            return
        _inorder(nodo.left)      # subárbol izquierdo
        resultado.append(nodo.val)  # raíz
        _inorder(nodo.right)     # subárbol derecho

    _inorder(root)
    return resultado
```