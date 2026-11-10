```python
def inorderTraversal(root):
    result = []
    if root:
        result = inorderTraversal(root.left)
        result.append(root.val)
        result = result + inorderTraversal(root.right)
    return result
```