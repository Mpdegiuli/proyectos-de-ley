def inorder_traversal(root):
    values = []
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        values.append(current.val)
        current = current.right

    return values