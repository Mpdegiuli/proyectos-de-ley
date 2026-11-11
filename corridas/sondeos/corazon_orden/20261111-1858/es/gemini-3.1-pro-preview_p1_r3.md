```python
def inorder_traversal(root):
    resultado = []
    
    def dfs(nodo):
        if nodo:
            dfs(nodo.left)
            resultado.append(nodo.val)
            dfs(nodo.right)
            
    dfs(root)
    return resultado
```