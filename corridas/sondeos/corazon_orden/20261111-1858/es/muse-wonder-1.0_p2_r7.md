```python
def recorrido_inorder(raiz):
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