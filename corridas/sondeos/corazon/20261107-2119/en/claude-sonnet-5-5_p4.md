```python
def inorder_traversal(root):
    # Note: no image came through on my end, so I chose iterative on its own merits (no recursion-depth limit).
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