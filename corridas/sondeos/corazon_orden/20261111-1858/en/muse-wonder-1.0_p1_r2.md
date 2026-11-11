```python
def inorder_traversal(root):
    result = []
    if root is None:
        return result
    result.extend(inorder_traversal(root.left))
    result.append(root.val)
    result.extend(inorder_traversal(root.right))
    return result
```