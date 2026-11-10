```python
def inorder(raiz):
    """Devuelve la lista de valores del árbol en orden inorder (izquierda, raíz, derecha)."""
    if raiz is None:
        return []
    return inorder(raiz.left) + [raiz.val] + inorder(raiz.right)
```