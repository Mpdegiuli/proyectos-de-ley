```python
def inorden(raiz):
    if raiz is None:
        return []
    return inorden(raiz.left) + [raiz.val] + inorden(raiz.right)
```