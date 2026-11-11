```python
def inorderTraversal(root):
    def inorder(node, values):
        if node is not None:
            inorder(node.left, values)
            values.append(node.val)
            inorder(node.right, values)
    
    result = []
    inorder(root, result)
    return result
```