```python
def obtener_inorder(root):
    resultado = []
    
    def dfs(nodo):
        if nodo:
            dfs(nodo.left)
            resultado.append(nodo.val)
            dfs(nodo.right)
            
    dfs(root)
    return resultado
```