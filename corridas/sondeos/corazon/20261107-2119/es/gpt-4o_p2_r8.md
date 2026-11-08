```python
def inorder_traversal(root):
    result = []

    def recursive_inorder(node):
        if node is not None:
            recursive_inorder(node.left)
            result.append(node.val)
            recursive_inorder(node.right)
    
    recursive_inorder(root)
    return result
```