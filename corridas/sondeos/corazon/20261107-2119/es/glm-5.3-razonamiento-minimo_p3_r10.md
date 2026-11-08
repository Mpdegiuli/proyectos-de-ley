```python
def inorder(root):
    def recorrer(nodo):
        if nodo is None:
            return
        recorrer(nodo.left)
        resultado.append(nodo.val)
        recorrer(nodo.right)

    resultado = []
    recorrer(root)
    return resultado
```