I don't see an attached image, only your description of a red heart, so I'll just pick a strategy — iterative:

```python
def inorder_traversal(root):
    result = []
    stack = []
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result
```