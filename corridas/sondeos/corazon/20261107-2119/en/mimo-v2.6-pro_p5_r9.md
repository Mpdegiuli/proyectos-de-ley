```python
def inorder(root):
    """
    Return the values of a binary tree in inorder (left, root, right).
    Each node has attributes: val, left, right.
    """
    result = []

    def _traverse(node):
        if node is None:
            return
        _traverse(node.left)   # left subtree
        result.append(node.val)  # root
        _traverse(node.right)  # right subtree

    _traverse(root)
    return result
```