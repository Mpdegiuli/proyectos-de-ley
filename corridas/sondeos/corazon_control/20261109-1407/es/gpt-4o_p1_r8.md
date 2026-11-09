```python
def inorder_traversal(root):
    def traverse(node):
        if not node:
            return []
        return traverse(node.left) + [node.val] + traverse(node.right)

    return traverse(root)
```