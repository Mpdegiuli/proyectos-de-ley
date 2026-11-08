I can't see an image in your message, but the task doesn't depend on it. Here is an iterative solution:

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