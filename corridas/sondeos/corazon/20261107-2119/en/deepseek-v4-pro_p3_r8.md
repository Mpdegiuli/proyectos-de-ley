```python
def inorderTraversal(root):
    values = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        values.append(node.val)
        traverse(node.right)
    
    traverse(root)
    return values
```