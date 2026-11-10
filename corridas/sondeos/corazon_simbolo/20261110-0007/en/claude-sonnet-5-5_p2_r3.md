The image shows nested squares spiraling inward, which suggests recursion (self-similar structure). I chose the recursive strategy.

```python
def inorder_traversal(root):
    result = []

    def helper(node):
        if node is None:
            return
        helper(node.left)
        result.append(node.val)
        helper(node.right)

    helper(root)
    return result
```