```python
def inorder_traversal(root):
    result = []
    
    def recursive(node):
        if node is None:
            return
        recursive(node.left)
        result.append(node.val)
        recursive(node.right)
    
    recursive(root)
    return result
```