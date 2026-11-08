No recibí ninguna imagen adjunta en el mensaje, así que no puedo basarme en ella; elijo la estrategia recursiva. Acá va la función:

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```