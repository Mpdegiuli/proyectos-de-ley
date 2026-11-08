```python
def inorder_traversal(root):
    # Strategy chosen: recursive ❤️
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