```python
def inorder_traversal(root):
    result = []
    
    def recursive(node):
        if node:
            recursive(node.left)
            result.append(node.val)
            recursive(node.right)
    
    recursive(root)
    return result
```