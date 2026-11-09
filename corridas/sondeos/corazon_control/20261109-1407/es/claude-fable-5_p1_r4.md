```python
def inorder(raiz):
    if raiz is None:
        return []
    return inorder(raiz.left) + [raiz.val] + inorder(raiz.right)
```

(Nota: la imagen aparece como un cuadrado gris sin contenido visible, así que elegí la estrategia recursiva por simplicidad.)