La imagen muestra cuadros anidados, cada uno contenido dentro de otro más pequeño, con flechas que apuntan hacia adentro. Eso representa la recursión, así que elijo la estrategia recursiva.

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```