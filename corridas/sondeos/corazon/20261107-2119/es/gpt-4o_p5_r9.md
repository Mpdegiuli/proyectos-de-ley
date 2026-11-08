```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    def traverse(node):
        if not node:
            return []
        return traverse(node.left) + [node.val] + traverse(node.right)
    
    return traverse(root)
```