```python
def inorder_traversal(root):
    """
    Devuelve la lista de valores de un árbol binario en recorrido inorder
    (izquierda, raíz, derecha) usando una estrategia iterativa con pila,
    como una espiral que se va enrollando hacia el centro y luego se desenrolla.
    """
    resultado = []
    pila = []
    actual = root

    while actual is not None or pila:
        # Bajamos todo lo posible hacia la izquierda (nos enrollamos)
        while actual is not None:
            pila.append(actual)
            actual = actual.left

        # Desenrollamos: visitamos el nodo y giramos a la derecha
        actual = pila.pop()
        resultado.append(actual.val)
        actual = actual.right

    return resultado
```