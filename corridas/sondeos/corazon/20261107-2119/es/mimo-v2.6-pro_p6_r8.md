```python
def inorder_traversal(root):
    resultado = []
    def _inorder(node):
        if node is not None:
            _inorder(node.left)
            resultado.append(node.val)
            _inorder(node.right)
    _inorder(root)
    return resultado
```