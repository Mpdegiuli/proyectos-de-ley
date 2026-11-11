```python
def inorder_traversal(root):
    def helper(node):
        if node is None:
            return []
        return helper(node.left) + [node.val] + helper(node.right)
    return helper(root)
```