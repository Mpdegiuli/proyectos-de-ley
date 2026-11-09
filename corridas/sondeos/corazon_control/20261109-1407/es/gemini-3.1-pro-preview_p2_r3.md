```python
def obtener_inorder(root):
    valores = []
    
    def recorrer(nodo):
        if nodo:
            recorrer(nodo.left)
            valores.append(nodo.val)
            recorrer(nodo.right)
            
    recorrer(root)
    return valores
```