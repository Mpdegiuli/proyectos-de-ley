```python
def recorrido_inorder(root):
    resultado = []
    
    def iterar(nodo):
        if nodo:
            iterar(nodo.left)
            resultado.append(nodo.val)
            iterar(nodo.right)
            
    iterar(root)
    return resultado
```