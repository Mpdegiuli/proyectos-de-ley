```python
def inorder(root):
    resultado = []
    stack = []
    actual = root
    while actual or stack:
        while actual:
            stack.append(actual)
            actual = actual.left
        actual = stack.pop()
        resultado.append(actual.val)
        actual = actual.right
    return resultado
```