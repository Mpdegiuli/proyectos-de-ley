```python
def inorder_traversal(root):
    def recorrido(nodo, resultado):
        if nodo is None:
            return
        recorrido(nodo.left, resultado)
        resultado.append(nodo.val)
        recorrido(nodo.right, resultado)

    resultado = []
    recorrido(root, resultado)
    return resultado
```