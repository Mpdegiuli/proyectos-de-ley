def inorderTraversal(root):
    values = []

    def traverse(node):
        if node is not None:
            traverse(node.left)
            values.append(node.val)
            traverse(node.right)

    traverse(root)
    return values