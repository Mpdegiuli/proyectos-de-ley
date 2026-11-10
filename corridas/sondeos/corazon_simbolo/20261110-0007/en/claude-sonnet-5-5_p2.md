The image shows nested squares spiraling inward, with a circular arrow. That suggests recursion, since the same shape repeats at a smaller scale. I'll use the recursive strategy.

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