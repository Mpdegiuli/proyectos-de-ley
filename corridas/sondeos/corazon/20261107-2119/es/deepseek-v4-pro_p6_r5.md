```python
def inorder(root):
    pila = []
    res = []
    actual = root
    while pila or actual:
        while actual:
            pila.append(actual)
            actual = actual.left
        actual = pila.pop()
        res.append(actual.val)
        actual = actual.right
    return res
```