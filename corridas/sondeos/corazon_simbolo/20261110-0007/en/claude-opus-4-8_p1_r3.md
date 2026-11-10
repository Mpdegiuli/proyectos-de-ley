The image shows nested squares (concentric boxes) with a spiral arrow, suggesting recursion (self-similar nested structure). I'll use the recursive strategy.

```python
def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
```