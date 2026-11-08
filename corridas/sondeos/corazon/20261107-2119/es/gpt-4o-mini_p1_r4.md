```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    
    def helper(node):
        if node:
            helper(node.left)
            result.append(node.val)
            helper(node.right)
    
    helper(root)
    return result
```