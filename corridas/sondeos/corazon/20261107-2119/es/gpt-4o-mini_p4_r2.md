```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    res = []
    def helper(node):
        if node:
            helper(node.left)
            res.append(node.val)
            helper(node.right)
    helper(root)
    return res
```