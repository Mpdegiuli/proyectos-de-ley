```python
def inorder(root):
    # Estrategia elegida: recursiva
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```