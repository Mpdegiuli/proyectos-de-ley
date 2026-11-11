```python
def inorder(root):
    values = []
    def dfs(node):
        if node:
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)
    dfs(root)
    return values
```