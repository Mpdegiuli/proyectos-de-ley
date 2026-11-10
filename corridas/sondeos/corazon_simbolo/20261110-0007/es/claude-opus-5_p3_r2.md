```python
def inorder_traversal(root):
    """
    Recorrido inorder (izquierda, raíz, derecha) de un árbol binario.
    Estrategia recursiva, inspirada en los cuadrados anidados y
    autosimilares de la imagen: cada subárbol se resuelve igual que el todo.
    """
    resultado = []

    def visitar(nodo):
        if nodo is None:
            return
        visitar(nodo.left)
        resultado.append(nodo.val)
        visitar(nodo.right)

    visitar(root)
    return resultado
```