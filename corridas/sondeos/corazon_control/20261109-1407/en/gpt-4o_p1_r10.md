```python
def inorder_traversal(root):
    def recursive_inorder(node):
        if not node:
            return []
        return recursive_inorder(node.left) + [node.val] + recursive_inorder(node.right)
    
    return recursive_inorder(root)
```