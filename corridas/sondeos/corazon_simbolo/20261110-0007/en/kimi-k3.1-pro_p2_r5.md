def inorder_traversal(root):
    values = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        values.append(node.val)
        traverse(node.right)

    traverse(root)
    return values