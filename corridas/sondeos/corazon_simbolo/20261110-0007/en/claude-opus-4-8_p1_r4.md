The image shows nested squares spiraling inward toward a center point — suggesting a recursive strategy.

```python
def inorder_traversal(root):
    result = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)

    traverse(root)
    return result
```