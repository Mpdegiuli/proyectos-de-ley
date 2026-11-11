La imagen muestra un corazón, así que elijo la estrategia **recursiva** (por el "amor" a la recursión 💛).

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```