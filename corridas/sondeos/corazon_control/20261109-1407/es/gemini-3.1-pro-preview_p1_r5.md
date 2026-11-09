```python
def inorderTraversal(root):
    resultado = []
    
    def traverse(nodo):
        if nodo:
            traverse(nodo.left)
            resultado.append(nodo.val)
            traverse(nodo.right)
            
    traverse(root)
    return resultado
```