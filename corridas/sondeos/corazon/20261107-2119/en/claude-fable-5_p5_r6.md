```python
def inorder_traversal(root):
    # Strategy chosen: recursive (the heart in the image splits into two lobes,
    # like a tree splitting into left and right subtrees — a natural fit for recursion)
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