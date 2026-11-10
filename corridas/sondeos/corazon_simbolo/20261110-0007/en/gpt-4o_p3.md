```python
def inorderTraversal(root):
    def inorder(node, acc):
        if node:
            inorder(node.left, acc)
            acc.append(node.val)
            inorder(node.right, acc)
    
    result = []
    inorder(root, result)
    return result
```