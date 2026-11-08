```python
def inorder(root):
    def recorrer(nodo, resultado):
        if nodo is None:
            return
        recorrer(nodo.left, resultado)
        resultado.append(nodo.val)
        recorrer(nodo.right, resultado)

    resultado = []
    recorrer(root, resultado)
    return resultado
```