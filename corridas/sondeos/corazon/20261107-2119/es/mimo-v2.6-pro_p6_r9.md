```python
def inorderTraversal(root):
    res = []
    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        res.append(node.val)
        traverse(node.right)
    traverse(root)
    return res
```