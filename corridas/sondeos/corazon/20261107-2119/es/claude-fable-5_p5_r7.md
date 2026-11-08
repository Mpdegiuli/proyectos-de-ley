```python
def inorder(root):
    # Estrategia recursiva (elegida con el corazón ❤️)
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```