```python
def inorder(root):
    valores = []
    
    def dfs(nodo):
        if not nodo:
            return
        dfs(nodo.left)
        valores.append(nodo.val)
        dfs(nodo.right)
    
    dfs(root)
    return valores
```