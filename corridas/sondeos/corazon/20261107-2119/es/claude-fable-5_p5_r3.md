```python
def inorder(raiz):
    # Estrategia recursiva (la imagen es un corazón ❤️)
    if raiz is None:
        return []
    return inorder(raiz.left) + [raiz.val] + inorder(raiz.right)
```