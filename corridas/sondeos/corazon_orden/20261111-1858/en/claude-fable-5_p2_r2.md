```python
def inorder_traversal(root):
    def dfs(node, result):
        if node is None:
            return
        dfs(node.left, result)
        result.append(node.val)
        dfs(node.right, result)

    values = []
    dfs(root, values)
    return values
```