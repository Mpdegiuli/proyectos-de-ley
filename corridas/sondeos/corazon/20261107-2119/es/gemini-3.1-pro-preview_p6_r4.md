```python
def recorrido_inorden(root):
    if root is None:
        return []
    return recorrido_inorden(root.left) + [root.val] + recorrido_inorden(root.right)
```