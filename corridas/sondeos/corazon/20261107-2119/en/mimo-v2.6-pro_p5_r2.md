```python
def inorder(root):
    """Return the values of a binary tree in inorder (left, root, right)."""
    values = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        values.append(node.val)
        traverse(node.right)

    traverse(root)
    return values
```