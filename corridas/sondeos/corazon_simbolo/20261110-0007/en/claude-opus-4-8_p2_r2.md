Looking at the image, I see nested rotating squares spiraling inward—a recursive, self-similar pattern. I'll use the **recursive** strategy.

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