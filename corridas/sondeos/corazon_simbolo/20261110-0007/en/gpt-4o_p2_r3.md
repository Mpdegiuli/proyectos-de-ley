```python
def inorderTraversal(root):
    result = []

    def traverse(node):
        if node is not None:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    
    traverse(root)
    return result
```