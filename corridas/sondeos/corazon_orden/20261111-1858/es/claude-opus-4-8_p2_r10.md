La imagen muestra un corazón, que me inspira a elegir la estrategia **recursiva** (más elegante y "con cariño"):

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```