```python
def inorder_traversal(root):
    def inorder(node, result):
        if node:
            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)
        return result
    return inorder(root, [])
```