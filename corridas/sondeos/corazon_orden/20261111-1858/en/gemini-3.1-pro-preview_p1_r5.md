```python
def inorderTraversal(root):
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
            
    result = []
    traverse(root)
    return result
```