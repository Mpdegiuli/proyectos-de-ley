```python
def inorder_traversal(root):
    """
    Returns the values of a binary tree in inorder (left, root, right).
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result
```