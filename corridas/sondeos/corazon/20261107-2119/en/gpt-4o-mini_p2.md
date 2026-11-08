```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    def traversal(node):
        if node:
            traversal(node.left)
            result.append(node.val)
            traversal(node.right)
    traversal(root)
    return result
```