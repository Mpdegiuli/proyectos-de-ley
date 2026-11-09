```python
def inorder(root):
    resultado = []
    pila = []
    actual = root
    while pila or actual is not None:
        while actual is not None:
            pila.append(actual)
            actual = actual.left
        actual = pila.pop()
        resultado.append(actual.val)
        actual = actual.right
    return resultado
```