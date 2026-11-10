```python
def inorder_traversal(root):
    def _inorder(node, result):
        if node is None:
            return result
        _inorder(node.left, result)
        result.append(node.val)
        _inorder(node.right, result)
        return result

    return _inorder(root, [])
```