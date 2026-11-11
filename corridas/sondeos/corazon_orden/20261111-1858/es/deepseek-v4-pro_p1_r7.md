```python
def inorder(root):
    res = []
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        res.append(current.val)
        current = current.right

    return res
```