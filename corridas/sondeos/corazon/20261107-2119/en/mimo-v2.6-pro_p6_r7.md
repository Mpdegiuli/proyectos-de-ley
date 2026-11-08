```python
def inorder_traversal(root):
    res = []
    
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        res.append(node.val)
        traverse(node.right)
    
    traverse(root)
    return res
```