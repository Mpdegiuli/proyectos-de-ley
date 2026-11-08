```python
def inorder(root):
    def recorrido(nodo):
        if nodo is None:
            return
        recorrido(nodo.left)
        resultado.append(nodo.val)
        recorrido(nodo.right)

    resultado = []
    recorrido(root)
    return resultado
```