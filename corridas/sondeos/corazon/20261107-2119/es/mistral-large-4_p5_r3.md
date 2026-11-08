```python
def inorder(root):
    res = []
    def dfs(nodo):
        if nodo is None:
            return
        dfs(nodo.left)
        res.append(nodo.val)
        dfs(nodo.right)
    dfs(root)
    return res
```