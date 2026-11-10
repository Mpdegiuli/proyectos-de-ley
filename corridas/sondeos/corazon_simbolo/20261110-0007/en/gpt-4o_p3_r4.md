```python
def inorder_traversal(root):
    def inorder(node, res):
        if node:
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)

    result = []
    inorder(root, result)
    return result
```