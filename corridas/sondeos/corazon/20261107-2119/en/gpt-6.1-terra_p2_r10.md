def inorder(root):
    values = []
    stack = []

    while root is not None or stack:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        values.append(root.val)
        root = root.right

    return values