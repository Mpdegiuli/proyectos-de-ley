No veo ninguna imagen adjunta en el mensaje, así que elijo la estrategia recursiva por mi cuenta:

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```