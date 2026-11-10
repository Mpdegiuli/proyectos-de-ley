def inorderTraversal(root):
    values = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        node = stack.pop()
        values.append(node.val)
        current = node.right
    return values