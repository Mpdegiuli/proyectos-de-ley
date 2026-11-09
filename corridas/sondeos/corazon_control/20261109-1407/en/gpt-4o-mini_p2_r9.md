```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    def recurse(node):
        if node:
            recurse(node.left)
            result.append(node.val)
            recurse(node.right)
    recurse(root)
    return result
```