
```python
def inorderTraversal(root):
    """
    Iterative approach to get inorder traversal of a binary tree.
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree (for the stack)
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