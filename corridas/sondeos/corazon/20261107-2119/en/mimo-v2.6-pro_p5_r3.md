```python
def inorder_traversal(root):
    """Return the list of node values of a binary tree in inorder (left, root, right)."""
    result = []

    def _walk(node):
        if node is None:
            return
        _walk(node.left)      # visit left subtree
        result.append(node.val)  # visit root
        _walk(node.right)     # visit right subtree

    _walk(root)
    return result
```