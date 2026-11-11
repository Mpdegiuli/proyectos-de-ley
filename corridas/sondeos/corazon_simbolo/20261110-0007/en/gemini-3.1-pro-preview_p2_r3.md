```python
def inorderTraversal(root):
    def traverse(node, result):
        if node:
            traverse(node.left, result)
            result.append(node.val)
            traverse(node.right, result)
            
    result = []
    traverse(root, result)
    return result
```