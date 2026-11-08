```python
def inorder_traversal(root):
    res = []
    def walk(node):
        if not node:
            return
        walk(node.left)
        res.append(node.val)
        walk(node.right)
    walk(root)
    return res
```