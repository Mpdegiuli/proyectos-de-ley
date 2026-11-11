```python
def inorder_traversal(root):
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