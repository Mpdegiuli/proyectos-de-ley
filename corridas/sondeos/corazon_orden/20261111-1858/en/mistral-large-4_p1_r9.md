```python
def inorder(root):
    out = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        out.append(node.val)
        dfs(node.right)
    dfs(root)
    return out
```