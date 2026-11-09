def inorder(root):
    out = []
    def walk(node):
        if node is None:
            return
        walk(node.left)
        out.append(node.val)
        walk(node.right)
    walk(root)
    return out