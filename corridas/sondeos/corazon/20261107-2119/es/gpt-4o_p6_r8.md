```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    def helper(node):
        if node:
            helper(node.left)
            result.append(node.val)
            helper(node.right)
    
    result = []
    helper(root)
    return result
```