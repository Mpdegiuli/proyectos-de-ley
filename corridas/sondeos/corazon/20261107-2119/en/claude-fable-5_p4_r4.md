No image was actually attached—only a text description—so I'll simply pick the recursive strategy:

```python
def inorder_traversal(root):
    result = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)

    traverse(root)
    return result
```