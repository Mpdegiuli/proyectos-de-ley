```python
def inorder(root):
    valores = []
    pila = []
    actual = root

    while actual is not None or pila:
        while actual is not None:
            pila.append(actual)
            actual = actual.left

        actual = pila.pop()
        valores.append(actual.val)
        actual = actual.right

    return valores
```