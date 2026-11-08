```python
def inorder_traversal(root):
    """Return the inorder (left, root, right) values of a binary tree.

    Strategy: recursive depth-first traversal.
    """
    values = []

    def walk(node):
        if node is None:
            return
        walk(node.left)      # left subtree
        values.append(node.val)  # root
        walk(node.right)     # right subtree

    walk(root)
    return values
```