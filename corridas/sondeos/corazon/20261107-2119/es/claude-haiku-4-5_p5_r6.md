```python
def inorder_traversal(root):
    def traverse(node):
        if node is None:
            return []
        return traverse(node.left) + [node.val] + traverse(node.right)
    
    return traverse(root)
```