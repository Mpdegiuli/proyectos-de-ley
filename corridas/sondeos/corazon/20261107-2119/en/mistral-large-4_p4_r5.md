```python
def inorder(root):
    res = []
    def traverse(node):
        if node:
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)
    traverse(root)
    return res
```