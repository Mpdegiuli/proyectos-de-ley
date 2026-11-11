```python
def inorder_traversal(root):
    def inorder(node, result):
        if not node:
            return
        inorder(node.left, result)
        result.append(node.val)
        inorder(node.right, result)
    
    result = []
    inorder(root, result)
    return result
```