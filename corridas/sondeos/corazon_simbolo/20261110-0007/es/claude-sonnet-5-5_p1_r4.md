La imagen muestra cuadros anidados, cada uno contenido dentro de otro más chico con una flecha que apunta hacia adentro, lo cual representa la recursión. Elijo la estrategia recursiva.

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```