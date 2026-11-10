```python
def inorderTraversal(root):
    result = []
    
    def recurse(node):
        if node:
            recurse(node.left)
            result.append(node.val)
            recurse(node.right)
    
    recurse(root)
    return result
```