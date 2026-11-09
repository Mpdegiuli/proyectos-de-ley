```python
def inorder_traversal(root):
  if not root:
    return []
  return (
      inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
  )
```