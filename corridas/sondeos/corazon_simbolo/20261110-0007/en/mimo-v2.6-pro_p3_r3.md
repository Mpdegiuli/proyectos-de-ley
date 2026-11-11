```python
def inorder_traversal(root):
    """
    Returns the list of values of the binary tree in inorder (left, root, right).
    
    Strategy: Recursive
    The nested structure in the image suggests a stack-based approach, 
    which maps naturally to recursion.
    """
    values = []

    def traverse(node):
        if not node:
            return
        # Go left
        traverse(node.left)
        # Visit root
        values.append(node.val)
        # Go right
        traverse(node.right)

    traverse(root)
    return values
```