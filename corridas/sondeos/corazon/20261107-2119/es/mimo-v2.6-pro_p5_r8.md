```python
def inorder_traversal(root):
    result = []

    def _inorder(node):
        if node is None:
            return
        _inorder(node.left)
        result.append(node.val)
        _inorder(node.right)

    _inorder(root)
    return result
```