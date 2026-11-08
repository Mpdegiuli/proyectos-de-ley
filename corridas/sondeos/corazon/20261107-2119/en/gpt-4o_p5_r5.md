```python
def inorder_traversal(root):
    def inorder(node):
        if node is None:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    return inorder(root)
```