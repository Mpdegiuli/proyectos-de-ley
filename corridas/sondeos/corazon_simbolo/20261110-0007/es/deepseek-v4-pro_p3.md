```python
def inorder(root):
    res = []
    def helper(node):
        if node:
            helper(node.left)
            res.append(node.val)
            helper(node.right)
    helper(root)
    return res
```