```python
def inorder_traversal(root):
    """
    Returns the inorder traversal of a binary tree as a list.
    Recursive approach.
    """
    result = []
    
    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    
    traverse(root)
    return result
```