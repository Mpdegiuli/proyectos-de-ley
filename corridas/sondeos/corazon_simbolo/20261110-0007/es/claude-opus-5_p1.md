```python
def inorder_traversal(root):
    """
    Recorrido inorder (izquierda, raíz, derecha) de un árbol binario.
    Estrategia iterativa con pila explícita, en espiral hacia adentro:
    se baja siempre por la izquierda, se visita y se gira a la derecha.
    """
    resultado = []
    pila = []
    actual = root

    while actual is not None or pila:
        # Espiral hacia adentro: bajar todo lo posible por la izquierda
        while actual is not None:
            pila.append(actual)
            actual = actual.left

        # Visitar el nodo más profundo pendiente
        actual = pila.pop()
        resultado.append(actual.val)

        # Girar hacia la derecha y repetir
        actual = actual.right

    return resultado
```