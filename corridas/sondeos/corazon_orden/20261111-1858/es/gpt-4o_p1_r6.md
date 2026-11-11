```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode) -> list:
    def inorder(node: TreeNode, result: list):
        if not node:
            return
        inorder(node.left, result)
        result.append(node.val)
        inorder(node.right, result)
    
    result = []
    inorder(root, result)
    return result
```