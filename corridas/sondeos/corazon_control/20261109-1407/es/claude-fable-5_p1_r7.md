La imagen es solo un cuadrado gris sin contenido visible, así que elijo la estrategia recursiva:

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```