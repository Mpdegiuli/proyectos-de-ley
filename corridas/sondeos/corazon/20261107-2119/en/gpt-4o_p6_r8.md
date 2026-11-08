```python
def inorder_traversal(root):
    def recursive_inorder(node):
        if node:
            yield from recursive_inorder(node.left)
            yield node.val
            yield from recursive_inorder(node.right)

    return list(recursive_inorder(root))
```