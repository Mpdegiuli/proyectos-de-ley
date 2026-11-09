```python
def inorder_traversal(root):
    result = []
    def recurse(node):
        if node is None:
            return
        recurse(node.left)
        result.append(node.val)
        recurse(node.right)
    recurse(root)
    return result
```