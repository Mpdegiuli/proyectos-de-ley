```python
def inorder_traversal(root):
    # Estrategia recursiva: izquierda -> raíz -> derecha
    resultado = []

    def _recorrer(nodo):
        if nodo is None:
            return
        _recorrer(nodo.left)
        resultado.append(nodo.val)
        _recorrer(nodo.right)

    _recorrer(root)
    return resultado
```