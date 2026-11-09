La imagen es solo un cuadrado gris sin contenido visible, así que elijo la estrategia iterativa:

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