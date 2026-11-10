Looking at the image, I see nested squares spiraling inward toward a center point — this suggests a **recursive** strategy.

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