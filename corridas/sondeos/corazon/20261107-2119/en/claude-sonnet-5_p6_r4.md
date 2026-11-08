```python
def inorder_traversal(root):
    def recurse(node, result):
        if node:
            recurse(node.left, result)
            result.append(node.val)
            recurse(node.right, result)
        return result
    
    return recurse(root, [])
```