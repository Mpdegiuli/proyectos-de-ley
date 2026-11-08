No veo ninguna imagen adjunta, así que elegí la estrategia iterativa por mi cuenta.

```python
def inorder(raiz):
    resultado = []
    pila = []
    actual = raiz

    while actual or pila:
        while actual:
            pila.append(actual)
            actual = actual.left
        actual = pila.pop()
        resultado.append(actual.val)
        actual = actual.right

    return resultado
```