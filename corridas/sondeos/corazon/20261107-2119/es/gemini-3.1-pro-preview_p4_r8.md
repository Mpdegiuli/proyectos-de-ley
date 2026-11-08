```python
def obtener_inorden(root):
    if root is None:
        return []
    return obtener_inorden(root.left) + [root.val] + obtener_inorden(root.right)
```