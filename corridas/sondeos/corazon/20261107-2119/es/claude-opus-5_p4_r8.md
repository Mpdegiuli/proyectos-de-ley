No me llegó ninguna imagen adjunta, así que elijo la estrategia recursiva.

```python
def inorder(root):
    resultado = []

    def recorrer(nodo):
        if nodo is None:
            return
        recorrer(nodo.left)
        resultado.append(nodo.val)
        recorrer(nodo.right)

    recorrer(root)
    return resultado
```