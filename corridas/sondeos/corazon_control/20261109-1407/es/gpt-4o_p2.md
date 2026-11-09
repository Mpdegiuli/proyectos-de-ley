```python
def inorder_traversal(root):
    def helper(node):
        if not node:
            return []
        return helper(node.left) + [node.val] + helper(node.right)
    
    return helper(root)
```