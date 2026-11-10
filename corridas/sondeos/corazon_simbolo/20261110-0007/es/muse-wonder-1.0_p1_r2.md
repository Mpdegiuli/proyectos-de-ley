```python
def inorder(raiz):
    """Estrategia recursiva: izquierda, raíz, derecha."""
    if raiz is None:
        return []
    return inorder(raiz.left) + [raiz.val] + inorder(raiz.right)
```