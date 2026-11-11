def inorder_values(root):
    if root is None:
        return []
    return inorder_values(root.left) + [root.val] + inorder_values(root.right)