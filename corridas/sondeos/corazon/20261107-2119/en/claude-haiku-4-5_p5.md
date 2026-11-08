```python
def inorderTraversal(root):
    """
    Iterative approach to inorder traversal of a binary tree.
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
        
        # Visit the node
        result.append(current.val)
        
        # Visit the right subtree
        current = current.right
    
    return result
```