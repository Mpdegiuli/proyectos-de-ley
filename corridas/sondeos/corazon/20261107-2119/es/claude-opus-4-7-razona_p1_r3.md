```python
def inorder(root):
    resultado = []
    stack = []
    actual = root
    while actual is not None or stack:
        while actual is not None:
            stack.append(actual)
            actual = actual.left
        actual = stack.pop()
        resultado.append(actual.val)
        actual = actual.right
    return resultado
```