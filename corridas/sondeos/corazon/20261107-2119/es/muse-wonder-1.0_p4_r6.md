```python
def recorrido_inorden(raiz):
    """Devuelve los valores en orden inorden (izquierda, raíz, derecha) de forma iterativa."""
    resultado = []
    pila = []
    actual = raiz
    while actual is not None or pila:
        while actual is not None:
            pila.append(actual)
            actual = actual.left
        actual = pila.pop()
        resultado.append(actual.val)
        actual = actual.right
    return resultado
```