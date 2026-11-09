
```python
def inorder_traversal(root):
    """
    Returns the list of values in inorder traversal (left, root, right) of a binary tree.
    Uses iterative approach with a stack.
    """
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Go to the leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Current must be None at this point
        current = stack.pop()
        
        # Add the node value to result (this is the root in left-root-right)
        result.append(current.val)
        
        # Visit the right subtree
        current = current.right
    
    return result
```