```python
def inorder_traversal(root):
    if not root:
        return []
    
    result = []
    
    def dfs(node):
        if node.left:
            dfs(node.left)
        result.append(node.val)
        if node.right:
            dfs(node.right)
            
    dfs(root)
    return result
```