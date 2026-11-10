```python
def inorder_traversal(root):
    def helper(node, result):
        if node is None:
            return
        helper(node.left, result)
        result.append(node.val)
        helper(node.right, result)
    
    result = []
    helper(root, result)
    return result
```