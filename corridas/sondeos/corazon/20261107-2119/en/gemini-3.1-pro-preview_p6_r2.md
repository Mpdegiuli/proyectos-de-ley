```python
def inorderTraversal(root):
    def traverse(node, values):
        if node:
            traverse(node.left, values)
            values.append(node.val)
            traverse(node.right, values)
            
    result = []
    traverse(root, result)
    return result
```