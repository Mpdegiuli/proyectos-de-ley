def inorder(root):
    if root is None:
        return []

    return inorder(root.left) + [root.val] + inorder(root.right)
