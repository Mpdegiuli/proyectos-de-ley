```python
def inorder(raiz):
    resultado = []
    
    def recorrer(nodo):
        if not nodo:
            return
        recorrer(nodo.left)
        resultado.append(nodo.val)
        recorrer(nodo.right)
    
    recorrer(raiz)
    return resultado
```