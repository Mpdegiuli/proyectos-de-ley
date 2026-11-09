```python
def inorder_traversal(root):
    def traverse(node):
        return traverse(node.left) + [node.val] + traverse(node.right) if node else []
    
    return traverse(root)
```