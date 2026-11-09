```python
def recorrido_inorder(root):
    if root is None:
        return []
    return (
        recorrido_inorder(root.left) + [root.val] + recorrido_inorder(root.right)
    )
```