```python
def inorder_traversal(root):
    resultado = []
    pila = []
    actual = root

    while actual or pila:
        # Bajar por la izquierda, apilando los nodos
        while actual:
            pila.append(actual)
            actual = actual.left
        # Visitar el nodo (raíz)
        actual = pila.pop()
        resultado.append(actual.val)
        # Pasar al subárbol derecho
        actual = actual.right

    return resultado
```