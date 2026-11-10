The image shows nested squares, each with a circular arrow, which suggests recursion, so I used a recursive strategy.

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