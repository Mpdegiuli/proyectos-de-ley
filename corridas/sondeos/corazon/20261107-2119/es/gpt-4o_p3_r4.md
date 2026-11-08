```python
def inorder_traversal(root):
    def inorder(node):
        if node is not None:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    result = []
    inorder(root)
    return result
```