def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)