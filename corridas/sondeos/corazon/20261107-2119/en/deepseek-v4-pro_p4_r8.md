def inorder(root):
    values = []
    def visit(node):
        if node:
            visit(node.left)
            values.append(node.val)
            visit(node.right)
    visit(root)
    return values