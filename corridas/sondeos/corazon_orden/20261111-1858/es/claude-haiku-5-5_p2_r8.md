```python
def inorder(raiz):
    resultado = []
    pila = []
    actual = raiz
    while pila or actual:
        while actual:
            pila.append(actual)
            actual = actual.left
        actual = pila.pop()
        resultado.append(actual.val)
        actual = actual.right
    return resultado
```