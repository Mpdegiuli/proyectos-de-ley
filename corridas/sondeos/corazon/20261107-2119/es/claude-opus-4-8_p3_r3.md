El símbolo es un corazón ❤️. Voy a elegir la estrategia **recursiva** (por el "r" de... bueno, me gusta, es más elegante y "del corazón").

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