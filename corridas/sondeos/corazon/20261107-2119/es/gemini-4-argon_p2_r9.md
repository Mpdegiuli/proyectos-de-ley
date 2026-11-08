```python
def recorrido_inorder(raiz):
    if not raiz:
        return []
    return (
        recorrido_inorder(raiz.left)
        + [raiz.val]
        + recorrido_inorder(raiz.right)
    )
```