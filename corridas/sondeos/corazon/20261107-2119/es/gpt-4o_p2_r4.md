```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    def inorder(node):
        if node is not None:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    inorder(root)
    return result
```