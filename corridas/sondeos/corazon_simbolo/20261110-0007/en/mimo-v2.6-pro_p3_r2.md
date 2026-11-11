```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    """
    Returns a list of node values in inorder (left, root, right) using a recursive approach.
    """
    if not root:
        return []
    
    result = []
    result.extend(inorderTraversal(root.left))
    result.append(root.val)
    result.extend(inorderTraversal(root.right))
    
    return result
```