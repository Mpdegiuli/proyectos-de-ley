```python
def inorder_traversal(root):
    def recurse(node):
        return recurse(node.left) + [node.val] + recurse(node.right) if node else []
    return recurse(root)
```