```python
def inorder(root):
    # La imagen es solo un cuadrado gris sin indicaciones, así que elegí la estrategia iterativa.
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