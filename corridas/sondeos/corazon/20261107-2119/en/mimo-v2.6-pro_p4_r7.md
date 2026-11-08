```python
def inorder(root):
    """
    Returns the values of the binary tree rooted at `root` in inorder
    (left subtree, root, right subtree) using a recursive strategy.

    Each node exposes the attributes `val`, `left` and `right`.
    """
    values = []

    def _walk(node):
        if node is None:
            return
        _walk(node.left)      # left subtree
        values.append(node.val)  # root
        _walk(node.right)     # right subtree

    _walk(root)
    return values
```