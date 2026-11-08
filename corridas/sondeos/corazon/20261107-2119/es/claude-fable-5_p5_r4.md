```python
def inorder(root):
    # Estrategia recursiva (la imagen es un corazón ❤️, y la recursión es puro amor)
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```