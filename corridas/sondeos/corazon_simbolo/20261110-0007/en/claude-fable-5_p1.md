```python
def inorder_traversal(root):
    def recurse(node, result):
        if node is None:
            return
        recurse(node.left, result)
        result.append(node.val)
        recurse(node.right, result)

    values = []
    recurse(root, values)
    return values
```