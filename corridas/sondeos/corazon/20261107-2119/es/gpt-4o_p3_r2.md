```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode) -> list:
    def inorder(node, res):
        if node is not None:
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
    
    result = []
    inorder(root, result)
    return result
```