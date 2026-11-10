Looking at the image, I see nested squares spiraling inward—a recursive pattern.

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```