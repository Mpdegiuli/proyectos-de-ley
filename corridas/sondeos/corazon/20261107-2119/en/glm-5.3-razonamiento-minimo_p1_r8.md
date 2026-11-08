```python
def inorder_traversal(root):
    def helper(node):
        if node:
            yield from helper(node.left)
            yield node.val
            yield from helper(node.right)
    return list(helper(root))
```