```python
def inorder_traversal(root):
    def dfs(node):
        if node:
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)
    return list(dfs(root))
```