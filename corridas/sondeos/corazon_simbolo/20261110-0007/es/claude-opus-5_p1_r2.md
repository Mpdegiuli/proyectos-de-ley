```python
def inorder_traversal(root):
    """
    Recorrido inorder (izquierda, raíz, derecha) de un árbol binario.
    Estrategia iterativa con pila explícita, inspirada en la espiral
    que se enrosca hacia adentro y luego se desenrosca hacia afuera.
    """
    valores = []
    pila = []
    actual = root

    while actual is not None or pila:
        # Nos hundimos hacia adentro por la rama izquierda
        while actual is not None:
            pila.append(actual)
            actual = actual.left
        # Volvemos hacia afuera: visitamos y giramos a la derecha
        actual = pila.pop()
        valores.append(actual.val)
        actual = actual.right

    return valores
```