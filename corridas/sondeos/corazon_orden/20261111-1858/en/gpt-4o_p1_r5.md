```python
def inorderTraversal(root):
    def inorder(node, result):
        if node is not None:
            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)
    
    result = []
    inorder(root, result)
    return result
```