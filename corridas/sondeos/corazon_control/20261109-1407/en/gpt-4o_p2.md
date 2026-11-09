```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode) -> list:
    def inorder(node: TreeNode, acc: list):
        if node:
            inorder(node.left, acc)
            acc.append(node.val)
            inorder(node.right, acc)
    
    result = []
    inorder(root, result)
    return result
```