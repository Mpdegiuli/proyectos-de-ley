```python
def inorderTraversal(root):
    result = []
    
    def helper(node):
        if not node:
            return
        helper(node.left)
        result.append(node.val)
        helper(node.right)
    
    helper(root)
    return result
```