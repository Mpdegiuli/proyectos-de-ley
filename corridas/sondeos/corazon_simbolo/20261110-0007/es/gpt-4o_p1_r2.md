```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    def inorder(node, values):
        if node is not None:
            inorder(node.left, values)
            values.append(node.val)
            inorder(node.right, values)
    
    result = []
    inorder(root, result)
    return result
```