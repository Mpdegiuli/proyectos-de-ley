```python
def inorder_traversal(root):
    values = []
    stack = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        values.append(current.val)
        current = current.right

    return values
```