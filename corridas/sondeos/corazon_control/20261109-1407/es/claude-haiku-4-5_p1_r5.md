```python
def inorderTraversal(root):
    result = []
    
    def recursivo(node):
        if node is None:
            return
        recursivo(node.left)
        result.append(node.val)
        recursivo(node.right)
    
    recursivo(root)
    return result
```