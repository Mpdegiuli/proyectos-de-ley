La imagen muestra cuadros dentro de cuadros, con flechas que apuntan cada vez más adentro. Eso representa la recursión, así que elijo la estrategia recursiva.

```python
def inorder(raiz):
    if raiz is None:
        return []
    return inorder(raiz.left) + [raiz.val] + inorder(raiz.right)
```