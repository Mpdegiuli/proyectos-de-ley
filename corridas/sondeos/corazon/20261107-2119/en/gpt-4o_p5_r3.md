```python
def inorder_traversal(root):
    def recursive_inorder(node, result):
        if node:
            recursive_inorder(node.left, result)
            result.append(node.val)
            recursive_inorder(node.right, result)

    result = []
    recursive_inorder(root, result)
    return result
```