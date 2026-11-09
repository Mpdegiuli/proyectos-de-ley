```python
def inorder_traversal(root):
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    
    return inorder(root)
```