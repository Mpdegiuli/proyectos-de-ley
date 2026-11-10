```python
def inorder(root):
    result = []
    def walk(node):
        if not node:
            return
        walk(node.left)
        result.append(node.val)
        walk(node.right)
    walk(root)
    return result
```