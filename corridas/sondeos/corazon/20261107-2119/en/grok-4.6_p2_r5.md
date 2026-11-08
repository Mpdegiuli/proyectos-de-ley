def inorderTraversal(root):
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []