```python
def inorder_traversal(root):
    # Strategy: recursive (the image is a heart — and I love recursion)
    def helper(node, result):
        if node is None:
            return
        helper(node.left, result)
        result.append(node.val)
        helper(node.right, result)

    values = []
    helper(root, values)
    return values
```