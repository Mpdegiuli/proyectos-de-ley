```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    def inorder(node, values):
        if node:
            inorder(node.left, values)
            values.append(node.val)
            inorder(node.right, values)
    result = []
    inorder(root, result)
    return result
```