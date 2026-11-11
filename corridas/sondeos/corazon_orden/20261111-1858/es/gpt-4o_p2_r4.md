```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    def inorder(node, vals):
        if node:
            inorder(node.left, vals)
            vals.append(node.val)
            inorder(node.right, vals)
    
    result = []
    inorder(root, result)
    return result
```