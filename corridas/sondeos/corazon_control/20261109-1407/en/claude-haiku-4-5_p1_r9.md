```python
def inorder_traversal(root):
    """
    Iterative approach using a stack to traverse binary tree in inorder.
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
        result.append(current.val)
        
        # Visit the right subtree
        current = current.right
    
    return result
```