```python
def inorder(root):
    # Estrategia iterativa (la imagen no aporta información, es un recuadro gris uniforme)
    resultado = []
    pila = []
    actual = root
    while actual is not None or pila:
        while actual is not None:
            pila.append(actual)
            actual = actual.left
        actual = pila.pop()
        resultado.append(actual.val)
        actual = actual.right
    return resultado
```