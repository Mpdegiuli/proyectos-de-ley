The image depicts nested self-similar boxes, suggesting a recursive strategy.

```python
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```