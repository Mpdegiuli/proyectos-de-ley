```python
def inorder_traversal(root):
    """Recorrido inorder (izquierda, raíz, derecha) de forma recursiva."""
    resultado = []

    def recorrer(nodo):
        if nodo is None:
            return
        recorrer(nodo.left)
        resultado.append(nodo.val)
        recorrer(nodo.right)

    recorrer(root)
    return resultado
```