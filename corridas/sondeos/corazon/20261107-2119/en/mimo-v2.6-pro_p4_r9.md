```python
def inorder_traversal(root):
    """
    Returns the values of a binary tree in inorder (left, root, right).
    Iterative strategy using an explicit stack.
    """
    result = []
    stack = []
    current = root

    while stack or current:
        # Go as far left as possible, pushing nodes onto the stack
        while current:
            stack.append(current)
            current = current.left

        # The top of the stack is the next node to visit
        current = stack.pop()
        result.append(current.val)

        # Then visit the right subtree
        current = current.right

    return result
```