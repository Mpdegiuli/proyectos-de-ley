No se adjuntó ninguna imagen (solo la descripción de un corazón rojo), y eso no indica una estrategia concreta, así que elegí la recursiva:

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```