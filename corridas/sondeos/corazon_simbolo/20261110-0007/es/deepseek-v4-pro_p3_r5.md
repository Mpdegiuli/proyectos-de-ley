```python
def inorder(root):
    def recorrer(nodo):
        if not nodo:
            return
        recorrer(nodo.left)
        valores.append(nodo.val)
        recorrer(nodo.right)

    valores = []
    recorrer(root)
    return valores
```