```python
def obtener_inorder(root):
    resultado = []
    
    def inorder(nodo):
        if nodo:
            inorder(nodo.left)
            resultado.append(nodo.val)
            inorder(nodo.right)
            
    inorder(root)
    return resultado
```