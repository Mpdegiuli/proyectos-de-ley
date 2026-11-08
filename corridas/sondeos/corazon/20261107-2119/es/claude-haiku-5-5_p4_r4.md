```python
def inorder_traversal(root):
    resultado = []
    pila = []
    actual = root

    while actual or pila:
        while actual:
            pila.append(actual)
            actual = actual.left
        actual = pila.pop()
        resultado.append(actual.val)
        actual = actual.right

    return resultado
```

*Nota: no me llegó ninguna imagen, solo el texto. La solución no depende de ella.*