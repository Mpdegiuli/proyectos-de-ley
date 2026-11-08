def inorder_traversal(root):
    values = []
    stack = []
    node = root

    while node is not None or stack:
        while node is not None:
            stack.append(node)
            node = node.left

        node = stack.pop()
        values.append(node.val)
        node = node.right

    return values