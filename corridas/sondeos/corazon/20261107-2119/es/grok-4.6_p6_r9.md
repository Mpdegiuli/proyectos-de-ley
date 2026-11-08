```python
def inorder_traversal(root):
    result = []
    def helper(node):
        if node:
            helper(node.left)
            result.append(node.val)
            helper(node.right)
    helper(root)
    return result
```