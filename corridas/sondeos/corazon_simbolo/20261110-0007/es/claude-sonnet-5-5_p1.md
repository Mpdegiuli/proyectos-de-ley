La imagen muestra cuadros dentro de cuadros, con flechas que apuntan a versiones cada vez más pequeñas de sí mismos. Eso representa la recursión, así que elijo la estrategia recursiva.

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```