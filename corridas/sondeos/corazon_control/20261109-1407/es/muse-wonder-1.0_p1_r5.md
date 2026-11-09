```python
def inorder_traversal(raiz):
    """Devuelve los valores en orden inorder mediante una estrategia iterativa."""
    valores = []
    pila = []
    nodo = raiz
    while nodo is not None or pila:
        while nodo is not None:
            pila.append(nodo)
            nodo = nodo.left
        nodo = pila.pop()
        valores.append(nodo.val)
        nodo = nodo.right
    return valores
```