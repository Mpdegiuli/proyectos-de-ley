```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
      
    return inorder(root)
```