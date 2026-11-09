```python
def inorderTraversal(root):
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    result = []
    inorder(root)
    return result
```