```python
def inorder_traversal(root):
    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    result = []
    dfs(root)
    return result
```