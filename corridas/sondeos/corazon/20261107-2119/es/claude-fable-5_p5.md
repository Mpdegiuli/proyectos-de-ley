```python
def inorder(root):
    # La imagen es un corazón ❤️, así que elijo la estrategia recursiva (con cariño)
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```