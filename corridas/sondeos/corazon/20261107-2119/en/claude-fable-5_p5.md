```python
def inorder_traversal(root):
    # The image shows a heart, so I'll go with the recursive approach — the one most people love.
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