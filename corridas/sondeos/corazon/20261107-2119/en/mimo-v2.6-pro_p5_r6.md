```python
def inorder_traversal(root):
    """Return the inorder (left, root, right) values of a binary tree iteratively."""
    values = []
    stack = []
    node = root

    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left

        node = stack.pop()
        values.append(node.val)
        node = node.right

    return values
```