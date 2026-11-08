```python
class Nodo:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(raiz):
    resultado = []
    stack = []
    actual = raiz

    while actual is not None or stack:
        while actual is not None:
            stack.append(actual)
            actual = actual.left
        actual = stack.pop()
        resultado.append(actual.val)
        actual = actual.right

    return resultado
```