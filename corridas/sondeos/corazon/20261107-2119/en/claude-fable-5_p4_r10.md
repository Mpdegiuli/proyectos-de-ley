I can't actually see any image in this conversation, so I'll simply choose the recursive strategy:

```python
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
```