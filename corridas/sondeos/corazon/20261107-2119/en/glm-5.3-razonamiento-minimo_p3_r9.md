```python
def inorder(root):
    result = []
    def visit(node):
        if node:
            visit(node.left)
            result.append(node.val)
            visit(node.right)
    visit(root)
    return result
```