```python
def inorder_traversal(root):
    # Strategy chosen: recursive (the image shows a heart — and everyone loves recursion ❤️)
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