```python
def inorder(root):
    resultado = []
    pila = []
    actual = root

    while actual or pila:
        # Descender por la izquierda apilando los nodos
        while actual:
            pila.append(actual)
            actual = actual.left

        # Visitar el nodo (raíz) y pasar a su derecha
        actual = pila.pop()
        resultado.append(actual.val)
        actual = actual.right

    return resultado
```