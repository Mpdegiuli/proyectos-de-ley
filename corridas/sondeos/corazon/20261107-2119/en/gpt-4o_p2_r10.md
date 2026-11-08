```python
def inorderTraversal(root):
    result = []

    def recursiveInorder(node):
        if node:
            recursiveInorder(node.left)
            result.append(node.val)
            recursiveInorder(node.right)

    recursiveInorder(root)
    return result
```