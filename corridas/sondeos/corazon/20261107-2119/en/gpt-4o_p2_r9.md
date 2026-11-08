```python
def inorder_traversal(root):
    def inorder(node, path):
        if node:
            inorder(node.left, path)
            path.append(node.val)
            inorder(node.right, path)
    
    result = []
    inorder(root, result)
    return result
```