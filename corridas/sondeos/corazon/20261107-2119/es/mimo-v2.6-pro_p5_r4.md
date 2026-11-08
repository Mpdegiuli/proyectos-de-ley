```python
def inorder(root):
    """
    Recorre un árbol binario en orden (izquierda, raíz, derecha)
    usando una estrategia iterativa con una pila explícita.

    Los nodos se esperan con los atributos: val, left, right.
    """
    resultado = []
    pila = []
    nodo = root

    while nodo is not None or pila:
        while nodo is not None:
            pila.append(nodo)
            nodo = nodo.left

        nodo = pila.pop()
        resultado.append(nodo.val)
        nodo = nodo.right

    return resultado
```