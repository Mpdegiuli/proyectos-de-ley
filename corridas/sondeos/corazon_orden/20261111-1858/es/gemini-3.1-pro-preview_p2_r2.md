```python
def recorrido_inorder(root):
    resultado = []
    
    def recursivo(nodo):
        if nodo is not None:
            recursivo(nodo.left)
            resultado.append(nodo.val)
            recursivo(nodo.right)
            
    recursivo(root)
    return resultado
```