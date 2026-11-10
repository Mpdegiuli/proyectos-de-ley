```python
def inorderTraversal(root):
    values = []

    def walk(node):
        if node is None:
            return
        walk(node.left)
        values.append(node.val)
        walk(node.right)

    walk(root)
    return values
```