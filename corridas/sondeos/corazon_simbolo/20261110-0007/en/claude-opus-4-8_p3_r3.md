Looking at the image, I see nested squares spiraling inward toward a center point—a visual that evokes recursion.

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