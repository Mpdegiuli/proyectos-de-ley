El símbolo es un corazón ❤️. Elijo la estrategia **recursiva** (por el "corazón", algo que late y se repite... bueno, elijo recursiva 😄).

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