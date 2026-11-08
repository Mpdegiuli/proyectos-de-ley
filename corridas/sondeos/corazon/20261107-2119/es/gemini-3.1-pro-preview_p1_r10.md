```python
def recorrido_inorder(root):
    resultado = []
    
    def recorrer(nodo):
        if nodo:
            recorrer(nodo.left)
            resultado.append(nodo.val)
            recorrer(nodo.right)
            
    recorrer(root)
    return resultado
```