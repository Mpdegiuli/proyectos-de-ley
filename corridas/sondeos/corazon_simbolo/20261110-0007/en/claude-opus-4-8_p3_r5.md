Looking at the image, I see nested squares spiraling inward—a recursive pattern.

```python
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
```