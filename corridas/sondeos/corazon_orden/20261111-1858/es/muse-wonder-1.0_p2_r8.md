```python
def inorder(raiz):
    """Devuelve los valores en orden inorder (izquierda, raíz, derecha) de forma iterativa."""
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