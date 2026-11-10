```python
def inorder_traversal(root):
    def helper(node):
        return helper(node.left) + [node.val] + helper(node.right) if node else []
    return helper(root)
```