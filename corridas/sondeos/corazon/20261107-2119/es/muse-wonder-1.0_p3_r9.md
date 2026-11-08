```python
def recorrido_inorder(raiz):
    resultado = []
    pila = []
    nodo = raiz
    while nodo is not None or pila:
        while nodo is not None:
            pila.append(nodo)
            nodo = nodo.left
        nodo = pila.pop()
        resultado.append(nodo.val)
        nodo = nodo.right
    return resultado
```