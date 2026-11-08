```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    def recursive_helper(node):
        if node:
            recursive_helper(node.left)
            result.append(node.val)
            recursive_helper(node.right)
    recursive_helper(root)
    return result
```