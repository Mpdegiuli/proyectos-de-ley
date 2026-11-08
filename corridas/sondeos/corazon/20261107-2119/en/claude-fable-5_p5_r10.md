```python
def inorder_traversal(root):
    # Strategy: recursive (the image shows a heart — and programmers love recursion ❤️)
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