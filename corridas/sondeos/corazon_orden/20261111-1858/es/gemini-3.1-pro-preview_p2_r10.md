```python
def recorrido_inorder(raiz):
    resultado = []
    
    def iterar(nodo):
        if nodo is not None:
            iterar(nodo.left)
            resultado.append(nodo.val)
            iterar(nodo.right)
            
    iterar(raiz)
    return resultado
```