```python
def inorder_traversal(root):
    def traverse(node):
        if node is not None:
            yield from traverse(node.left)
            yield node.val
            yield from traverse(node.right)
    
    return list(traverse(root))
```