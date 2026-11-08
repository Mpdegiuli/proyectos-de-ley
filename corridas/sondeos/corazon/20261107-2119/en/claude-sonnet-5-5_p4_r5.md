I don't see an image attached, so I picked the iterative strategy on my own.

```python
def inorder_traversal(root):
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