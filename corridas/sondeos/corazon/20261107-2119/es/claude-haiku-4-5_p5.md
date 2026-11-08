```python
def inorderTraversal(root):
    result = []
    
    def recursive_inorder(node):
        if node is None:
            return
        recursive_inorder(node.left)
        result.append(node.val)
        recursive_inorder(node.right)
    
    recursive_inorder(root)
    return result
```