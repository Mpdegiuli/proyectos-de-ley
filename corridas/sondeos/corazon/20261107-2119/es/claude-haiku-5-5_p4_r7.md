No pude ver ninguna imagen en tu mensaje, pero el problema no depende de ella. Usé una estrategia iterativa con pila.

```python
def inorder(root):
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