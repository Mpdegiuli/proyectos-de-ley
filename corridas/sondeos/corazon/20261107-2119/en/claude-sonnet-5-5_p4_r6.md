```python
def inorder_traversal(root):
    # Note: no image was visible to me, so I chose the iterative strategy
    # on its own merits (it avoids recursion depth limits on deep trees).
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
```