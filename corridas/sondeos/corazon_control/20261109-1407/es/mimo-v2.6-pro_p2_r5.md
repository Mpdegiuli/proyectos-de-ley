```python
def inorder_traversal(root):
    res = []

    def traverse(node):
        if node is not None:
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)

    traverse(root)
    return res
```