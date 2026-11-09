```python
def inorder_traversal(root):
    def _helper(node, res):
        if node:
            _helper(node.left, res)
            res.append(node.val)
            _helper(node.right, res)
    
    result = []
    _helper(root, result)
    return result
```