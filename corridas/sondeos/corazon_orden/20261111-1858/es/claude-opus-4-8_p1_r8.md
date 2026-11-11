```python
def inorder(root):
    resultado = []
    stack = []
    nodo = root
    while nodo or stack:
        while nodo:
            stack.append(nodo)
            nodo = nodo.left
        nodo = stack.pop()
        resultado.append(nodo.val)
        nodo = nodo.right
    return resultado
```