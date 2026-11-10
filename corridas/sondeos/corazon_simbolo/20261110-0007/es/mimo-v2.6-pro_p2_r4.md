```python
def inorder_traversal(root):
    result = []
    
    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
        
    dfs(root)
    return result
```