```python
def inorder(root):
    values = []
    def traverse(node):
        if node:
            traverse(node.left)
            values.append(node.val)
            traverse(node.right)
    traverse(root)
    return values
```