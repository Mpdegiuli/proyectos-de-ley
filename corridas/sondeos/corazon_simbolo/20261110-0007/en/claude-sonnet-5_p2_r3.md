```python
def inorder_traversal(root):
    def helper(node, result):
        if node:
            helper(node.left, result)
            result.append(node.val)
            helper(node.right, result)
        return result
    return helper(root, [])
```