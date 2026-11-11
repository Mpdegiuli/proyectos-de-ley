```python
def inorderTraversal(root):
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