```python
def inorder_traversal(root):
    resultado = []
    
    def inorden(nodo):
        if nodo:
            inorden(nodo.left)
            resultado.append(nodo.val)
            inorden(nodo.right)
            
    inorden(root)
    return resultado
```