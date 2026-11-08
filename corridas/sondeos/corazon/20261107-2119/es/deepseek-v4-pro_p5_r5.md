```python
def inorder(root):
    res = []
    stack = []
    actual = root

    while actual or stack:
        while actual:
            stack.append(actual)
            actual = actual.left

        actual = stack.pop()
        res.append(actual.val)
        actual = actual.right

    return res
```