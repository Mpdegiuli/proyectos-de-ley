```python
def inorder_traversal(root):
    def inorder_helper(node, result):
        if node:
            inorder_helper(node.left, result)
            result.append(node.val)
            inorder_helper(node.right, result)
    
    result = []
    inorder_helper(root, result)
    return result
```