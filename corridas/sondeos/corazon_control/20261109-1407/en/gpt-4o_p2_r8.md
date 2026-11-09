```python
def inorder_traversal(root):
    def inorder(node, res):
        if node is not None:
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
    
    result = []
    inorder(root, result)
    return result
```