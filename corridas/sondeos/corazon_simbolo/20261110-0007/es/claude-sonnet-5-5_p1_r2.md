La imagen muestra recuadros anidados, cada uno contenido en otro con una flecha que apunta hacia adentro. Eso representa la recursión, así que elijo la estrategia recursiva.

```python
def inorder(raiz):
    if raiz is None:
        return []
    return inorder(raiz.left) + [raiz.val] + inorder(raiz.right)
```