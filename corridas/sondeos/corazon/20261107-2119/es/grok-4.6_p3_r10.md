```python
def inorder(root):
    res = []
    def dfs(n):
        if n:
            dfs(n.left)
            res.append(n.val)
            dfs(n.right)
    dfs(root)
    return res
```