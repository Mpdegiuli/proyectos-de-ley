La imagen muestra un corazón, cuya forma es simétrica y se dibuja naturalmente de forma recursiva (ramas izquierda y derecha). Elijo la estrategia **recursiva**.

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