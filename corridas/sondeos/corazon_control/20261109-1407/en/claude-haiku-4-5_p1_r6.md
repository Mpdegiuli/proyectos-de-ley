
```python
def inorder_traversal(root):
    """
    Performs inorder traversal of a binary tree iteratively.
    Returns a list of node values in inorder sequence (left, root, right).
    """
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Go to the leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Current is None, pop from stack
        current = stack.pop()
        
        # Add the node value to result
        result.append(current.val)
        
        # Visit the right subtree
        current = current.right
    
    return result
```